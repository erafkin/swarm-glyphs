"""Offline regression tests for the shared gameplay turn budget and pending replies."""

import asyncio
import json
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import AsyncMock, patch

from pydantic import ValidationError

from src.core.api_call import CallResult
from src.enc_dec.config import LanguageExperimentConfig
from src.enc_dec.escape_room import EscapeAction
from src.enc_dec.models import EscapeTaskResponse
from src.enc_dec.run import LanguageExperiment


def records(path):
    return [json.loads(line) for line in path.read_text().splitlines()] if path.exists() else []


def reply(ordinal=1, action=None, cost=0.001):
    parsed = EscapeTaskResponse(
        scratchpad=f"Private turn {ordinal}", message=f"a{ordinal}",
        intended_meaning=f"Public turn {ordinal}",
        action=action or EscapeAction(kind="wait", code=None),
    )
    return CallResult(raw=parsed.model_dump_json(), parsed=parsed, used_structured_output=True,
                      usage={"cost": cost}, finish_reason="stop")


class TaskTurnLimitTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.logs = tempfile.TemporaryDirectory(prefix="task-turn-limit-")
        self.addCleanup(self.logs.cleanup)
        self.client = SimpleNamespace(close=AsyncMock())

    def config(self, limit, **overrides):
        settings = dict(
            task_kind="escape_room", glyph_dictionary="glyphs_latin", model="offline-model",
            n_agents=8, run_monitors=False, task_minutes=None, task_max_turns=limit,
            min_turn_interval_s=0, max_cost_usd=50, log_dir=self.logs.name,
        )
        return LanguageExperimentConfig(**(settings | overrides))

    def experiment(self, limit, **overrides):
        return LanguageExperiment(self.config(limit, **overrides), language_text="FROZEN REFERENCE")

    async def run_offline(self, experiment, fake):
        with patch("src.enc_dec.run.make_client", return_value=self.client), \
                patch("src.enc_dec.run.call_agent", side_effect=fake) as call:
            await asyncio.wait_for(experiment.run(), 3)
        return call.await_count

    def test_task_budget_is_optional_but_must_be_positive(self):
        self.assertIsNone(self.config(None).task_max_turns)
        self.assertEqual(self.config(1).task_max_turns, 1)
        for limit in (0, -1):
            with self.subTest(limit=limit), self.assertRaises(ValidationError):
                self.config(limit)

    async def test_exact_team_budget_under_eight_and_with_overlapping_batches(self):
        for limit in (3, 13):
            with self.subTest(limit=limit):
                experiment = self.experiment(limit)
                started = 0
                final_pending = min(8, limit)
                at_budget = asyncio.Event()
                release = asyncio.Event()

                async def fake(*args):
                    nonlocal started
                    started += 1
                    ordinal = started
                    if ordinal > limit - final_pending:
                        if ordinal == limit:
                            at_budget.set()
                        await release.wait()
                    else:
                        await asyncio.sleep(0)
                    return reply(ordinal)

                with patch("src.enc_dec.run.make_client", return_value=self.client), \
                        patch("src.enc_dec.run.call_agent", side_effect=fake):
                    running = asyncio.create_task(experiment.run())
                    try:
                        await asyncio.wait_for(at_budget.wait(), 3)
                        # No further calls may start, and exhausting reservations must
                        # not discard the final responses before they arrive.
                        self.assertEqual(started, limit)
                        self.assertEqual(experiment.task_turns_scheduled, limit)
                        self.assertEqual(experiment.task_turns_in_flight, final_pending)
                        self.assertFalse(experiment.stop.is_set())
                        self.assertFalse(running.done())
                    finally:
                        release.set()
                        await asyncio.wait_for(running, 3)

                self.assertEqual(started, limit)
                self.assertEqual(experiment.task_stop_reason, "turn_limit_reached")
                self.assertEqual(experiment.task_turns_in_flight, 0)
                calls = records(experiment.logger.path / "agent_calls.jsonl")
                self.assertEqual(len(calls), limit)
                self.assertTrue(all(row["state_applied"] for row in calls))
                self.assertFalse(any(row.get("ignored_reason") for row in calls))
                public = records(experiment.logger.path / "task_chatroom.jsonl")
                messages = [row["text"] for row in public if row["sender"] != "task"]
                self.assertCountEqual(messages, [f"a{i}" for i in range(1, limit + 1)])
                summary = json.loads((experiment.logger.path / "summary.json").read_text())
                self.assertEqual(summary["task_turns_scheduled"], limit)
                self.assertEqual(sum(summary["task_turns"].values()), limit)
                self.assertAlmostEqual(summary["total_cost_usd"], 0.001 * limit)
                self.assertEqual(summary["creation_stop_reason"], "provided_language")
                self.assertEqual(summary["creation_turns_scheduled"], 0)
                last_prompt = calls[-1]["turn_prompt"]
                self.assertIn(f"{limit} of {limit}", last_prompt)
                self.assertIn("scheduled", last_prompt.lower())
                self.assertNotIn("of inf", last_prompt)
                for prompt in experiment.task_prompts.values():
                    self.assertIn(str(limit), prompt)
                    self.assertIn("shared", prompt.lower())
                    self.assertIn("8", prompt)

    async def test_malformed_response_consumes_the_last_turn(self):
        experiment = self.experiment(1)

        async def malformed(*args):
            return CallResult(raw="not JSON", parsed=None, parse_error="no JSON object",
                              used_structured_output=False, usage={"cost": 0.001}, finish_reason="stop")

        self.assertEqual(await self.run_offline(experiment, malformed), 1)
        self.assertEqual(experiment.task_stop_reason, "turn_limit_reached")
        self.assertEqual(experiment.task_turns_scheduled, 1)
        calls = records(experiment.logger.path / "agent_calls.jsonl")
        self.assertEqual(len(calls), 1)
        self.assertEqual(calls[0]["parse_error"], "no JSON object")
        self.assertFalse(calls[0]["state_applied"])
        self.assertEqual(len(records(experiment.logger.path / "task_chatroom.jsonl")), 1)

    async def test_recoverable_api_error_consumes_turn_without_backoff_or_retry(self):
        experiment = self.experiment(1)

        async def recoverable(*args):
            raise RuntimeError("offline temporary connection failure")

        self.assertEqual(await self.run_offline(experiment, recoverable), 1)
        self.assertEqual(experiment.task_stop_reason, "turn_limit_reached")
        self.assertEqual(experiment.task_turns_scheduled, 1)
        self.assertEqual(experiment.task_turns_in_flight, 0)
        self.assertEqual(records(experiment.logger.path / "agent_calls.jsonl"), [])
        self.assertEqual(len(records(experiment.logger.path / "errors.jsonl")), 1)
        summary = json.loads((experiment.logger.path / "summary.json").read_text())
        self.assertEqual(summary["task_turns_scheduled"], 1)
        self.assertEqual(sum(summary["task_turns"].values()), 0)

    async def test_escape_takes_priority_before_or_on_the_final_budget_turn(self):
        actions = [EscapeAction(kind="enter_cabinet_code", code="2748")]
        actions += [EscapeAction(kind=kind, code=None) for kind in ("drain", "crank", "signal", "boot")]
        actions += [EscapeAction(kind="enter_exit_code", code="9796")]
        for limit in (6, 20):
            with self.subTest(limit=limit):
                experiment = self.experiment(limit)
                started = 0

                async def solve(*args):
                    nonlocal started
                    ordinal = started
                    started += 1
                    # All permitted first-batch calls overlap, so the responses
                    # after escape must still be logged and charged, not applied.
                    await asyncio.sleep(0)
                    action = actions[ordinal] if ordinal < len(actions) else None
                    return reply(ordinal + 1, action)

                self.assertEqual(await self.run_offline(experiment, solve), min(8, limit))
                self.assertTrue(experiment.room.escaped)
                self.assertEqual(experiment.task_stop_reason, "escaped")
                calls = records(experiment.logger.path / "agent_calls.jsonl")
                self.assertEqual(sum(row["state_applied"] for row in calls), 6)
                self.assertTrue(all(row.get("ignored_reason") == "escaped" for row in calls[6:]))
                self.assertEqual(experiment.task_turns_in_flight, 0)

    async def test_cost_and_fatal_error_take_priority_over_exhausted_budget(self):
        experiment = self.experiment(1, max_cost_usd=0.001)

        async def expensive(*args):
            return reply(cost=0.002)

        self.assertEqual(await self.run_offline(experiment, expensive), 1)
        self.assertEqual(experiment.task_stop_reason, "cost_limit_reached")
        calls = records(experiment.logger.path / "agent_calls.jsonl")
        self.assertEqual(len(calls), 1)
        self.assertEqual(calls[0]["usage"]["cost"], 0.002)

        experiment = self.experiment(1)

        async def fatal(*args):
            error = RuntimeError("offline invalid request")
            error.status_code = 400
            raise error

        self.assertEqual(await self.run_offline(experiment, fatal), 1)
        self.assertTrue(experiment.task_stop_reason.startswith("fatal_api_error_400"))
        self.assertEqual(experiment.task_turns_scheduled, 1)
        self.assertEqual(experiment.task_turns_in_flight, 0)


if __name__ == "__main__":
    unittest.main()
