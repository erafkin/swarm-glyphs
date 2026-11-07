"""
Three phases in one log folder:
1. A team plans a language in English, without knowing the task, then writes language.txt.
2. A new team gets that document and the task. Their chat is the language plus the task's feedback.
3. One monitor model reads only that task chat, four times: true task, no task, a distant wrong
   task, and a close wrong task.

Usage: .venv/bin/python -m src.enc_dec.run <config.json>
"""

import argparse
import asyncio
import random
import time

from openai import AsyncOpenAI

from src.core.api_call import CallResult, call_agent, make_client
from src.core.potential_glyphs import (
    VIOLATION_TOKEN,
    dictionary_path,
    is_glyph_only,
    load_dictionary,
    sample_glyphs,
)
from src.core.chatroom import Chatroom
from src.core.game_log import GameLogger
from src.enc_dec.config import LanguageExperimentConfig
from src.enc_dec.models import CREATION_SCHEMA, TASK_SCHEMA, CreationResponse, RoundAgent, TaskResponse
from src.enc_dec.prompts import (
    MONITOR_CONDITIONS,
    build_creation_prompt,
    build_language_document_prompt,
    build_monitor_prompt,
    build_task_prompt,
    build_turn_prompt,
    monitor_briefing,
)
from src.enc_dec.task import TASK_SENDER, feedback_text

# Same as the guess-who game: invalid key, no credits, unknown model. 403 is also used for moderation.
FATAL_STATUS_CODES = {401, 402, 404}


class LanguageExperiment:
    def __init__(self, config: LanguageExperimentConfig):
        self.config = config
        self.rng = random.Random(config.seed)
        self.logger = GameLogger(config.log_dir)
        self.glyphs = self._sample_glyphs()
        self.creation_agents = self._make_agents(config.n_agents, "creation")
        n_task = config.task_n_agents or config.n_agents
        self.task_agents = self._make_agents(n_task, "task")
        self.creation_chat = Chatroom(self.logger, "chatroom")
        self.task_chat = Chatroom(self.logger, "task_chatroom")
        self.language_text = ""

        self.stop = asyncio.Event()
        self.stop_reason = ""
        self.phase = ""
        self.phase_start = 0.0
        self.phase_limit_s = 0.0
        self.start_time = 0.0
        self.total_cost_usd = 0.0
        self._warned_missing_cost = False
        self.creation_stop_reason = ""
        self.task_stop_reason = ""

    def _sample_glyphs(self) -> list[str]:
        if self.config.chat_mode != "glyphs":
            return []
        dictionary = load_dictionary(dictionary_path(self.config.glyph_dictionary))
        n = len(dictionary) if self.config.n_glyphs is None else self.config.n_glyphs
        return sample_glyphs(self.config.glyph_dictionary, n, self.rng)

    def _make_agents(self, n: int, phase: str) -> list[RoundAgent]:
        return [
            RoundAgent(
                agent_id=f"agent_{i}",
                model=self.config.model_for(i, phase),
                glyphs_view=self.rng.sample(self.glyphs, len(self.glyphs)) if self.glyphs else [],
            )
            for i in range(n)
        ]

    def _add_cost(self, result: CallResult) -> None:
        cost = (result.usage or {}).get("cost")
        if cost is None and self.config.max_cost_usd is not None and not self._warned_missing_cost:
            self._warned_missing_cost = True
            print("Warning: OpenRouter didn't report cost for a call; max_cost_usd can't be fully enforced")
        self.total_cost_usd += cost or 0.0
        limit = self.config.max_cost_usd
        if limit is not None and self.total_cost_usd >= limit and not self.stop.is_set():
            self.stop_reason = "cost_limit_reached"
            print(f"Stopping: total cost ${self.total_cost_usd:.2f} reached max_cost_usd=${limit:.2f}")
            self.stop.set()

    def _post(self, chat: Chatroom, agent_ids: list[str], sender: str, message: str) -> bool:
        """Post a message. The planning chat is English. Only the task chat is glyph-checked."""
        if self.phase == "task" and self.config.chat_mode == "glyphs":
            violation = not is_glyph_only(message, agent_ids, self.glyphs, self.config.allow_spaces)
            chat.post(sender, VIOLATION_TOKEN if violation else message, violation)
            return violation
        chat.post(sender, message)
        return False

    def _post_feedback(self) -> None:
        self.task_chat.post(TASK_SENDER, feedback_text(self.task_agents))

    async def _turn(self, client: AsyncOpenAI, agent: RoundAgent, agents: list[RoundAgent], chat: Chatroom) -> None:
        phase = self.phase
        schema, response_model = (CREATION_SCHEMA, CreationResponse) if phase == "creation" else (TASK_SCHEMA, TaskResponse)
        prompts = self.creation_prompts if phase == "creation" else self.task_prompts
        elapsed = time.monotonic() - self.phase_start
        context_n = self.config.language_context_messages if phase == "creation" else self.config.chat_context_messages
        turn_prompt = build_turn_prompt(
            agent, "\n".join(m.render() for m in chat.recent(context_n)) or "(no messages yet)",
            self.config, phase, elapsed, self.language_text,
        )
        result = await call_agent(
            client, agent.model, prompts[agent.agent_id], turn_prompt, schema, response_model, self.config
        )
        self._add_cost(result)
        agent.turn_count += 1
        record = {
            "phase": phase,
            "agent_id": agent.agent_id,
            "model": agent.model,
            "turn": agent.turn_count,
            "timestamp": time.time(),
            "elapsed_s": round(elapsed, 1),
            "turn_prompt": turn_prompt,
            "raw": result.raw,
            "parse_error": result.parse_error,
            "used_structured_output": result.used_structured_output,
            "usage": result.usage,
            "response": result.parsed.model_dump() if result.parsed is not None else None,
            "state_applied": False,
        }
        if self.stop.is_set():
            record["ignored_reason"] = self.stop_reason or "phase_stopped"
            self.logger.log("agent_calls", record)
            return
        if result.parsed is not None:
            self._apply(agent, agents, chat, result.parsed, record)
        self.logger.log("agent_calls", record)

    def _apply(self, agent: RoundAgent, agents: list[RoundAgent], chat: Chatroom, response, record: dict) -> None:
        message = response.message.strip()
        violation = False
        if message:
            violation = self._post(chat, [a.agent_id for a in agents], agent.agent_id, message)
        record.update(state_applied=True, message=message, is_violation=violation)
        if isinstance(response, CreationResponse):
            if response.language_document.strip():
                self._set_language_text(response.language_document)
            agent.done = agent.done or response.done
            record.update(done=agent.done, language_document=self.language_text)
            if all(a.done for a in agents) and not self.stop.is_set():
                self.stop_reason = "all_done"
                self.stop.set()
        else:
            agent.scratchpad = response.scratchpad
            agent.answer = response.answer
            record.update(scratchpad=agent.scratchpad, answer=agent.answer)

    async def _agent_loop(self, client: AsyncOpenAI, agent: RoundAgent, agents: list[RoundAgent], chat: Chatroom) -> None:
        backoff = self.config.min_turn_interval_s
        while not self.stop.is_set():
            if time.monotonic() - self.phase_start >= self.phase_limit_s:
                return
            try:
                await self._turn(client, agent, agents, chat)
                backoff = self.config.min_turn_interval_s
            except Exception as e:
                status = getattr(e, "status_code", None)
                self.logger.log("errors", {
                    "phase": self.phase, "agent_id": agent.agent_id, "timestamp": time.time(),
                    "status_code": status, "error": repr(e),
                })
                if status in FATAL_STATUS_CODES and not self.stop.is_set():
                    self.stop_reason = f"fatal_api_error_{status}: {agent.agent_id} ({agent.model})"
                    print(f"Stopping: OpenRouter returned {status} for {agent.agent_id} ({agent.model}): {e}")
                    self.stop.set()
                    return
                backoff = min(max(backoff * 2, 5), 120)
            if self.stop.is_set() or time.monotonic() - self.phase_start >= self.phase_limit_s:
                return
            try:
                # The phase deadline sets stop, so this wait ends early when time is up.
                await asyncio.wait_for(self.stop.wait(), timeout=backoff)
            except asyncio.TimeoutError:
                pass

    async def _run_phase(self, client: AsyncOpenAI, phase: str, agents: list[RoundAgent], chat: Chatroom, minutes: float) -> str:
        self.phase = phase
        self.stop = asyncio.Event()
        self.stop_reason = ""
        self.phase_start = time.monotonic()
        self.phase_limit_s = minutes * 60
        tasks = [asyncio.create_task(self._agent_loop(client, agent, agents, chat)) for agent in agents]
        if phase == "task" and self.config.task_feedback:
            tasks.append(asyncio.create_task(self._feedback_loop()))
        try:
            await asyncio.wait_for(self.stop.wait(), timeout=self.phase_limit_s)
        except asyncio.TimeoutError:
            self.stop_reason = "time_limit"
            self.stop.set()
        await asyncio.gather(*tasks, return_exceptions=True)
        return self.stop_reason or "time_limit"

    async def _feedback_loop(self) -> None:
        while not self.stop.is_set():
            try:
                await asyncio.wait_for(self.stop.wait(), timeout=self.config.task_feedback_interval_s)
                return
            except asyncio.TimeoutError:
                if not self.stop.is_set():
                    self._post_feedback()

    async def _write_language_documents(self, client: AsyncOpenAI) -> None:
        """One document per agent, from the shared planning chat. Identical copies collapse into one."""
        recent = self.creation_chat.recent(self.config.language_context_messages)
        transcript = "\n".join(message.render() for message in recent) or "(no messages)"
        drafts: dict[str, str] = {}

        async def ask(agent: RoundAgent) -> None:
            system, user = build_language_document_prompt(agent, self.config, transcript, self.language_text)
            try:
                result = await call_agent(client, agent.model, system, user, None, None, self.config)
            except Exception as e:
                self.logger.log("errors", {
                    "phase": "language_document", "agent_id": agent.agent_id,
                    "timestamp": time.time(), "error": repr(e),
                })
                drafts[agent.agent_id] = ""
                return
            self._add_cost(result)
            drafts[agent.agent_id] = result.raw.strip()
            self.logger.log("language_document", {
                "agent_id": agent.agent_id,
                "model": agent.model,
                "timestamp": time.time(),
                "system_prompt": system,
                "prompt": user,
                "document": drafts[agent.agent_id],
                "usage": result.usage,
            })

        await asyncio.gather(*(ask(agent) for agent in self.creation_agents))
        self._write_language_file(drafts)

    def _set_language_text(self, text: str) -> None:
        """Replace the shared language.txt. Every encoding agent sees this text on the next turn."""
        self.language_text = text.strip()
        (self.logger.path / "language.txt").write_text(self.language_text + "\n", encoding="utf-8")

    def _write_language_file(self, drafts: dict[str, str]) -> None:
        ordered = [(agent.agent_id, drafts.get(agent.agent_id, "")) for agent in self.creation_agents]
        bodies = {text for _, text in ordered if text}
        if len(bodies) == 1 and all(text for _, text in ordered):
            self.language_text = next(iter(bodies))
        else:
            self.language_text = "\n\n".join(
                f"## {agent_id}\n{text or '(this agent wrote nothing)'}" for agent_id, text in ordered
            )
        (self.logger.path / "language.txt").write_text(self.language_text + "\n", encoding="utf-8")
        self.logger.write_json("language", {"by_agent": dict(ordered), "text": self.language_text})

    async def _monitor(self, client: AsyncOpenAI) -> None:
        transcript = self.task_chat.transcript()
        monitor_config = self.config.model_copy(update={
            "max_tokens": self.config.monitor_max_tokens,
            "reasoning_effort": self.config.monitor_reasoning_effort or self.config.reasoning_effort,
        })
        model = self.config.model_for(0, "monitor")

        async def ask(condition: str) -> None:
            system, user = build_monitor_prompt(transcript, monitor_briefing(self.config, condition))
            try:
                result = await call_agent(client, model, system, user, None, None, monitor_config)
            except Exception as e:
                self.logger.log("errors", {"phase": "monitor", "condition": condition, "timestamp": time.time(), "error": repr(e)})
                return
            self._add_cost(result)
            self.logger.log("monitor", {
                "condition": condition,
                "model": model,
                "timestamp": time.time(),
                "max_tokens": monitor_config.max_tokens,
                "reasoning_effort": monitor_config.reasoning_effort,
                "system_prompt": system,
                "prompt": user,
                "answer": result.raw,
                "usage": result.usage,
            })

        await asyncio.gather(*(ask(condition) for condition in MONITOR_CONDITIONS))

    async def run(self) -> None:
        self.logger.write_json("config", self.config.model_dump())
        self.logger.write_json("glyphs", self.glyphs)
        self.creation_prompts = {
            a.agent_id: build_creation_prompt(a, [x.agent_id for x in self.creation_agents], self.config)
            for a in self.creation_agents
        }
        self.logger.write_json("agents", [
            {"agent_id": a.agent_id, "model": a.model, "glyphs_view": a.glyphs_view,
             "system_prompt": self.creation_prompts[a.agent_id]}
            for a in self.creation_agents
        ])
        print(f"Language experiment {self.logger.game_id}: logging to {self.logger.path}")
        self.start_time = time.monotonic()
        client = make_client(self.config)
        try:
            self.creation_stop_reason = await self._run_phase(
                client, "creation", self.creation_agents, self.creation_chat, self.config.language_minutes
            )
            if not self.creation_stop_reason.startswith("fatal_api_error"):
                await self._write_language_documents(client)
            limit = self.config.max_cost_usd
            if limit is not None and self.total_cost_usd >= limit and self.creation_stop_reason in ("time_limit", "all_done"):
                self.creation_stop_reason = "cost_limit_reached"
            if self.creation_stop_reason not in ("time_limit", "all_done"):
                return

            ids = [a.agent_id for a in self.task_agents]
            self.task_prompts = {
                a.agent_id: build_task_prompt(a, ids, self.config, self.language_text) for a in self.task_agents
            }
            self.logger.write_json("task_agents", [
                {"agent_id": a.agent_id, "model": a.model, "glyphs_view": a.glyphs_view,
                 "system_prompt": self.task_prompts[a.agent_id]}
                for a in self.task_agents
            ])
            self.task_stop_reason = await self._run_phase(
                client, "task", self.task_agents, self.task_chat, self.config.task_minutes
            )
            if self.config.task_feedback:
                self._post_feedback()
            self.logger.write_json("task_answers", {a.agent_id: a.answer for a in self.task_agents})
            if not self.task_stop_reason.startswith("fatal_api_error"):
                await self._monitor(client)
        finally:
            await client.close()
            self._write_summary()

    def _write_summary(self) -> None:
        summary = {
            "game_id": self.logger.game_id,
            "chat_mode": self.config.chat_mode,
            "creation_stop_reason": self.creation_stop_reason,
            "task_stop_reason": self.task_stop_reason,
            "elapsed_s": round(time.monotonic() - self.start_time, 1),
            "creation_turns": {a.agent_id: a.turn_count for a in self.creation_agents},
            "task_turns": {a.agent_id: a.turn_count for a in self.task_agents},
            "total_cost_usd": round(self.total_cost_usd, 6),
        }
        self.logger.write_json("summary", summary)
        print(
            f"Experiment over (creation: {self.creation_stop_reason or 'not run'}, "
            f"task: {self.task_stop_reason or 'not run'}). Summary in {self.logger.path / 'summary.json'}"
        )


def run_config(config: LanguageExperimentConfig) -> None:
    try:
        asyncio.run(LanguageExperiment(config).run())
    except KeyboardInterrupt:
        pass


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the language creation, task, and monitor experiment.")
    parser.add_argument("config", help="path to a LanguageExperimentConfig JSON file")
    run_config(LanguageExperimentConfig.from_file(parser.parse_args().config))


if __name__ == "__main__":
    main()
