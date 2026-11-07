"""
Main gameplay loop.
There is a goal object with F features. There are N agents; features are assigned round-robin,
so each agent knows the true value of exactly one feature.
In board mode the goal is one person on a shared board (Guess Who), and agents guess a person index.
The agents have access to a chatroom where they can communicate with each other.
The only communication in the chatroom is in glyphs for the agents except:
- They can refer to each other using their unique identifier.
- If they respond not in glyphs, a shared indication will be posted in the chatroom that is understood
  to mean that that model tried to respond not in glyphs.
Every M seconds (default 90), every agent's guess is scored and the result is posted in the chatroom.
The game ends when the win condition is met or after max_score_rounds scoring rounds. Afterwards each
agent is asked to explain its communication strategy (unless the game was interrupted).

Usage: python -m src.gameplay.play_game [--config path/to/config.json]
"""

import argparse
import asyncio
import random
import time

from openai import AsyncOpenAI

from src.agent_models.api_call import CallResult, call_agent, make_client
from src.agent_models.model_obj import AgentResponse, AgentState, Guess
from src.agent_models.potential_glyphs import VIOLATION_TOKEN, is_glyph_only, load_glyphs
from src.agent_models.prompts import (
    build_final_interview_prompt,
    build_system_prompt,
    build_turn_prompt,
    response_json_schema,
)
from src.config import GameConfig
from src.game_object.board import Board, goal_person_for_seed, load_board
from src.game_object.features import GoalObject, shuffle_options
from src.gameplay.chatroom import SYSTEM_SENDER, Chatroom
from src.gameplay.game_log import GameLogger
from src.gameplay.scoring import ScoreReport, format_score, is_won, score_round


class Game:
    def __init__(self, config: GameConfig):
        self.config = config
        self.rng = random.Random(config.seed)
        self.logger = GameLogger(config.log_dir)
        self.chatroom = Chatroom(self.logger)

        # The goal is always a board person (in features mode the board itself isn't shown to agents).
        full_board = load_board(config.board_path)
        self.board: Board | None = full_board if config.mode == "board" else None
        self.goal_person = (
            config.goal_person if config.goal_person is not None else goal_person_for_seed(config.seed, full_board)
        )
        if self.goal_person not in full_board.people:
            raise ValueError(f"goal_person {self.goal_person} is not on the board")
        self.goal: GoalObject = full_board.goal(self.goal_person)
        self.glyphs = load_glyphs(config.glyphs_path)

        if config.n_agents < len(self.goal.features):
            print(f"Warning: {config.n_agents} agents < {len(self.goal.features)} features; some features are unknown to everyone")

        self.agents = self._create_agents()
        self.agent_ids = [a.agent_id for a in self.agents]
        self.system_prompts = {a.agent_id: build_system_prompt(a, self.agent_ids, config, self.board) for a in self.agents}
        self.json_schemas = {a.agent_id: response_json_schema(a, self.board) for a in self.agents}

        self.stop = asyncio.Event()
        self.stop_reason = ""
        self.start_time = 0.0
        self.last_report: ScoreReport | None = None
        self.total_cost_usd = 0.0

    def _create_agents(self) -> list[AgentState]:
        # Option, glyph, and board order and the starting guess are randomized per agent so that
        # "pick the first thing listed" doesn't line up across agents or with the goal.
        features = self.goal.features
        agents = []
        for i in range(self.config.n_agents):
            feature = features[i % len(features)]
            board_order = self.rng.sample(self.board.numbers, len(self.board)) if self.board else None
            agents.append(
                AgentState(
                    agent_id=f"agent_{i}",
                    model=self.config.model_for(i),
                    known_feature=feature.name,
                    known_value=self.goal.values[feature.name],
                    features_view=shuffle_options(features, self.rng),
                    glyphs_view=self.rng.sample(self.glyphs, len(self.glyphs)),
                    board_order=board_order,
                    guess=Guess.random(features, self.rng),
                    person_guess=self.rng.choice(self.board.numbers) if self.board else None,
                )
            )
        return agents

    def elapsed(self) -> float:
        return time.monotonic() - self.start_time

    def _add_cost(self, result: CallResult) -> None:
        self.total_cost_usd += (result.usage or {}).get("cost") or 0.0

    async def take_turn(self, client: AsyncOpenAI, agent: AgentState) -> None:
        turn_prompt = build_turn_prompt(
            agent, self.chatroom.recent(self.config.chat_context_messages), self.goal.features, self.elapsed()
        )
        result = await call_agent(
            client,
            agent.model,
            self.system_prompts[agent.agent_id],
            turn_prompt,
            self.json_schemas[agent.agent_id],
            AgentResponse,
            self.config,
        )
        self._add_cost(result)
        if self.stop.is_set():
            return  # game ended while this call was in flight; don't change state after the final score

        agent.turn_count += 1
        record = {
            "agent_id": agent.agent_id,
            "model": agent.model,
            "turn": agent.turn_count,
            "timestamp": time.time(),
            "elapsed_s": round(self.elapsed(), 1),
            "turn_prompt": turn_prompt,
            "raw": result.raw,
            "parse_error": result.parse_error,
            "used_structured_output": result.used_structured_output,
            "usage": result.usage,
        }

        if result.parsed is not None:
            response = result.parsed
            agent.scratchpad = response.scratchpad
            agent.guess, rejected = agent.guess.updated(self.goal.features, response.guess)
            if self.board is not None:
                # Agents must always guess a person; invalid or missing guesses keep the previous one.
                if response.person_guess in self.board.people:
                    agent.person_guess = response.person_guess
                else:
                    rejected.append(f"person_guess={response.person_guess}")

            message = response.message.strip()
            is_violation = bool(message) and not is_glyph_only(message, self.agent_ids, self.glyphs)
            if message:
                self.chatroom.post(agent.agent_id, VIOLATION_TOKEN if is_violation else message, is_violation)

            record.update(
                scratchpad=agent.scratchpad,
                message=message,
                is_violation=is_violation,
                guess=agent.guess.to_labels(self.goal.features),
                guess_one_hot=agent.guess.one_hot,
                person_guess=agent.person_guess,
                rejected_guess_updates=rejected,
            )

        self.logger.log("agent_calls", record)

    async def agent_loop(self, client: AsyncOpenAI, agent: AgentState) -> None:
        backoff = self.config.min_turn_interval_s
        while not self.stop.is_set():
            try:
                await self.take_turn(client, agent)
                backoff = self.config.min_turn_interval_s
            except Exception as e:  # API/network errors shouldn't kill the agent; log and back off
                self.logger.log("errors", {"agent_id": agent.agent_id, "timestamp": time.time(), "error": repr(e)})
                backoff = min(max(backoff * 2, 5), 120)
            try:
                await asyncio.wait_for(self.stop.wait(), timeout=backoff)
            except asyncio.TimeoutError:
                pass

    async def scorer_loop(self) -> None:
        for round_num in range(1, self.config.max_score_rounds + 1):
            await asyncio.sleep(self.config.score_interval_s)
            if self.board is not None:
                report = score_round(
                    round_num, self.elapsed(), self.agents, self.goal, self.goal_person, len(self.board)
                )
            else:
                report = score_round(round_num, self.elapsed(), self.agents, self.goal)
            self.last_report = report
            self.chatroom.post(SYSTEM_SENDER, format_score(report, self.config))
            self.logger.log("scores", report.model_dump())
            if is_won(report, self.config):
                self.stop_reason = "win_threshold_reached"
                break
        else:
            self.stop_reason = "max_score_rounds_reached"
        self.stop.set()

    async def final_interview(self, client: AsyncOpenAI) -> None:
        """Ask every agent, in parallel, to explain its communication strategy; log to final_interviews.jsonl."""
        recent_chat = self.chatroom.recent(self.config.chat_context_messages)

        async def ask(agent: AgentState) -> None:
            prompt = build_final_interview_prompt(agent, recent_chat, self.goal.features)
            try:
                result = await call_agent(
                    client, agent.model, self.system_prompts[agent.agent_id], prompt, None, None, self.config
                )
            except Exception as e:
                self.logger.log(
                    "errors",
                    {"agent_id": agent.agent_id, "timestamp": time.time(), "stage": "final_interview", "error": repr(e)},
                )
                return
            self._add_cost(result)
            self.logger.log(
                "final_interviews",
                {
                    "agent_id": agent.agent_id,
                    "model": agent.model,
                    "timestamp": time.time(),
                    "prompt": prompt,
                    "answer": result.raw,
                    "usage": result.usage,
                },
            )

        await asyncio.gather(*(ask(a) for a in self.agents))

    async def run(self) -> None:
        self.logger.write_json("config", self.config.model_dump())
        self.logger.write_json("goal", {**self.goal.model_dump(), "goal_person": self.goal_person})
        self.logger.write_json("glyphs", self.glyphs)
        if self.board is not None:
            self.logger.write_json("board", self.board.people)
        self.logger.write_json(
            "agents",
            [{**a.model_dump(exclude={"guess"}), "system_prompt": self.system_prompts[a.agent_id]} for a in self.agents],
        )
        print(f"Game {self.logger.game_id}: logging to {self.logger.path}")

        client = make_client(self.config)
        self.start_time = time.monotonic()
        agent_tasks = [asyncio.create_task(self.agent_loop(client, a)) for a in self.agents]
        try:
            await self.scorer_loop()
        finally:
            if not self.stop_reason:
                self.stop_reason = "interrupted"
            self.stop.set()
            for task in agent_tasks:
                task.cancel()
            await asyncio.gather(*agent_tasks, return_exceptions=True)
            try:
                if self.config.final_interview and self.stop_reason != "interrupted":
                    await self.final_interview(client)
            finally:
                await client.close()
                self._write_summary()

    def _write_summary(self) -> None:
        summary = {
            "game_id": self.logger.game_id,
            "mode": self.config.mode,
            "goal_person": self.goal_person,
            "stop_reason": self.stop_reason,
            "elapsed_s": round(self.elapsed(), 1),
            "score_rounds": self.last_report.round if self.last_report else 0,
            "final_score": self.last_report.model_dump() if self.last_report else None,
            "turns_per_agent": {a.agent_id: a.turn_count for a in self.agents},
            "total_cost_usd": round(self.total_cost_usd, 6),
        }
        self.logger.write_json("summary", summary)
        print(f"Game over ({self.stop_reason}). Summary in {self.logger.path / 'summary.json'}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Run one swarm-glyphs game.")
    parser.add_argument("--config", help="path to a JSON GameConfig; defaults are used if omitted")
    args = parser.parse_args()

    config = GameConfig.from_file(args.config) if args.config else GameConfig()
    try:
        asyncio.run(Game(config).run())
    except KeyboardInterrupt:
        pass  # summary is written by Game.run's finally block


if __name__ == "__main__":
    main()
