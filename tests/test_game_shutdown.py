"""Offline regressions for preserving paid completions during budget shutdown."""

import asyncio
import json
import tempfile
import time
import unittest
from types import SimpleNamespace
from unittest.mock import AsyncMock, patch

from src.agent_models.api_call import CallResult
from src.agent_models.model_obj import AgentResponse
from src.config import GameConfig
from src.gameplay.play_game import Game


class GameShutdownTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.logs = tempfile.TemporaryDirectory(prefix="shutdown-offline-")
        self.addCleanup(self.logs.cleanup)
        self.game = Game(GameConfig(
            mode="features",
            n_agents=8,
            max_cost_usd=0.01,
            score_interval_s=240,
            min_turn_interval_s=0,
            final_interview=False,
            log_dir=self.logs.name,
        ))
        self.game.start_time = time.monotonic()

    def records(self, stream):
        path = self.game.logger.path / f"{stream}.jsonl"
        return [json.loads(line) for line in path.read_text().splitlines()]

    def completion(self, agent_id, cost=0.01):
        response = AgentResponse(
            scratchpad=f"Unaccepted private state from {agent_id}",
            message=self.game.glyphs[0],
            guess=self.game.goal.values,
        )
        return CallResult(
            raw=response.model_dump_json(),
            parsed=response,
            used_structured_output=True,
            usage={"cost": cost, "prompt_tokens": 100, "completion_tokens": 50},
        )

    def assert_state_unchanged(self, agent, before):
        self.assertEqual(agent.model_dump(exclude={"turn_count"}), before)
        self.assertEqual(len(self.game.chatroom), 0)

    async def test_cost_crossing_response_is_logged_without_applying_state(self):
        agent = self.game.agents[0]
        before = agent.model_dump(exclude={"turn_count"})
        result = self.completion(agent.agent_id)
        with patch("src.gameplay.play_game.call_agent", AsyncMock(return_value=result)):
            await self.game.take_turn(object(), agent)

        self.assertTrue(self.game.stop.is_set())
        self.assertEqual(self.game.stop_reason, "cost_limit_reached")
        self.assertEqual(agent.turn_count, 1)
        self.assert_state_unchanged(agent, before)
        self.assertAlmostEqual(self.game.total_cost_usd, 0.01)
        records = self.records("agent_calls")
        self.assertEqual(len(records), 1)
        record = records[0]
        self.assertEqual(record["agent_id"], agent.agent_id)
        self.assertEqual(record["turn"], 1)
        self.assertEqual(record["raw"], result.raw)
        self.assertEqual(record["response"], result.parsed.model_dump())
        self.assertEqual(record["usage"], result.usage)
        self.assertIsNone(record["parse_error"])
        self.assertFalse(record["state_applied"])
        self.assertEqual(record["ignored_reason"], "cost_limit_reached")
        self.assertTrue(record["used_structured_output"])
        self.assertTrue(record["turn_prompt"])

    async def test_unparseable_cost_crossing_response_preserves_raw_and_error(self):
        agent = self.game.agents[0]
        before = agent.model_dump(exclude={"turn_count"})
        result = CallResult(
            raw="unfinished JSON {",
            parsed=None,
            parse_error="JSON object incomplete",
            used_structured_output=False,
            usage={"cost": 0.02, "completion_tokens": 16000},
        )
        with patch("src.gameplay.play_game.call_agent", AsyncMock(return_value=result)):
            await self.game.take_turn(object(), agent)

        self.assertEqual(agent.turn_count, 1)
        self.assert_state_unchanged(agent, before)
        self.assertAlmostEqual(self.game.total_cost_usd, 0.02)
        records = self.records("agent_calls")
        self.assertEqual(len(records), 1)
        self.assertEqual(records[0]["raw"], result.raw)
        self.assertEqual(records[0]["usage"], result.usage)
        self.assertEqual(records[0]["parse_error"], result.parse_error)
        self.assertIsNone(records[0]["response"])
        self.assertFalse(records[0]["state_applied"])
        self.assertEqual(records[0]["ignored_reason"], "cost_limit_reached")

    async def test_budget_shutdown_drains_all_eight_inflight_calls(self):
        all_started = asyncio.Event()
        release_first = asyncio.Event()
        release_remaining = asyncio.Event()
        requests = []
        returned = []
        cancelled = []
        agent_for_prompt = {prompt: agent_id for agent_id, prompt in self.game.system_prompts.items()}
        before = {a.agent_id: a.model_dump(exclude={"turn_count"}) for a in self.game.agents}
        results = {a.agent_id: self.completion(a.agent_id, (i + 1) / 100)
                   for i, a in enumerate(self.game.agents)}

        async def fake_call(client, model, system_prompt, turn_prompt, schema, response_model, config):
            agent_id = agent_for_prompt[system_prompt]
            requests.append(agent_id)
            if len(requests) == 8:
                all_started.set()
            try:
                await all_started.wait()
                await (release_first if agent_id == "agent_0" else release_remaining).wait()
            except asyncio.CancelledError:
                cancelled.append(agent_id)
                raise
            returned.append(agent_id)
            return results[agent_id]

        client = SimpleNamespace(close=AsyncMock())
        with patch("src.gameplay.play_game.make_client", return_value=client), \
             patch("src.gameplay.play_game.call_agent", side_effect=fake_call):
            run_task = asyncio.create_task(self.game.run())
            try:
                await asyncio.wait_for(all_started.wait(), timeout=2)
                release_first.set()
                await asyncio.wait_for(self.game.stop.wait(), timeout=2)
                self.assertEqual(self.game.stop_reason, "cost_limit_reached")
                self.assertEqual(returned, ["agent_0"])
                release_remaining.set()
                await asyncio.wait_for(run_task, timeout=2)
            finally:
                release_first.set()
                release_remaining.set()
                if not run_task.done():
                    run_task.cancel()
                await asyncio.gather(run_task, return_exceptions=True)

        client.close.assert_awaited_once()
        self.assertEqual(cancelled, [])
        self.assertCountEqual(requests, self.game.agent_ids)
        self.assertCountEqual(returned, self.game.agent_ids)
        self.assertAlmostEqual(self.game.total_cost_usd, 0.36)
        records = self.records("agent_calls")
        self.assertEqual(len(records), 8)
        self.assertCountEqual([r["agent_id"] for r in records], self.game.agent_ids)
        self.assertAlmostEqual(sum(r["usage"]["cost"] for r in records), 0.36)
        for record in records:
            result = results[record["agent_id"]]
            self.assertEqual(record["raw"], result.raw)
            self.assertEqual(record["response"], result.parsed.model_dump())
            self.assertFalse(record["state_applied"])
            self.assertEqual(record["ignored_reason"], "cost_limit_reached")
            self.assertEqual(record["turn"], 1)
        for agent in self.game.agents:
            self.assertEqual(agent.turn_count, 1)
            self.assert_state_unchanged(agent, before[agent.agent_id])
        summary = json.loads((self.game.logger.path / "summary.json").read_text())
        self.assertEqual(summary["stop_reason"], "cost_limit_reached")
        self.assertEqual(summary["total_cost_usd"], 0.36)
        self.assertEqual(summary["turns_per_agent"], {agent_id: 1 for agent_id in self.game.agent_ids})
        self.assertFalse((self.game.logger.path / "errors.jsonl").exists())
        self.assertFalse((self.game.logger.path / "final_interviews.jsonl").exists())


if __name__ == "__main__":
    unittest.main()
