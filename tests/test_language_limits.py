"""Offline checks of shared turn budgets, draining, and per-run prompt limits."""

import asyncio
import json
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import AsyncMock, patch

from pydantic import ValidationError

from src.core.api_call import CallResult
from src.core.game_log import GameLogger
from src.enc_dec import prompts
from src.enc_dec.config import LanguageExperimentConfig
from src.enc_dec.models import CreationResponse, DecodeResponse
from src.enc_dec.monitor import DecodingTeam, execute_monitor_inputs, prepare_monitor_inputs
from src.enc_dec.run import LanguageExperiment


def result(reply=None, raw="FINAL REFERENCE"):
    return CallResult(raw=raw, parsed=reply, used_structured_output=reply is not None,
                      usage={"cost": 0.001})


def rows(path):
    return [json.loads(line) for line in path.read_text().splitlines()]


class LanguageLimitTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.logs = tempfile.TemporaryDirectory(prefix="language-limits-")
        self.addCleanup(self.logs.cleanup)

    def config(self, **overrides):
        settings = dict(task_prompt="An offline test task", glyph_dictionary="glyphs_latin",
                        model="offline-model", n_agents=8, monitor_n_agents=8,
                        run_monitors=False, min_turn_interval_s=0, log_dir=self.logs.name,
                        language_minutes=None, language_max_turns=200, language_max_lines=250,
                        monitor_minutes=None, monitor_max_turns=200)
        return LanguageExperimentConfig(**(settings | overrides))

    def test_time_or_turn_limit_required_and_positive(self):
        self.config()
        for overrides in ({"language_max_turns": None}, {"monitor_max_turns": None},
                          {"language_max_turns": 0}, {"monitor_max_turns": 0},
                          {"language_max_lines": 0}):
            with self.subTest(overrides=overrides), self.assertRaises(ValidationError):
                self.config(**overrides)
        legacy = LanguageExperimentConfig(task_prompt="Offline")
        self.assertEqual((legacy.language_minutes, legacy.monitor_minutes), (10, 10))
        self.assertIsNone(legacy.language_max_turns)
        self.assertIsNone(legacy.monitor_max_turns)

    def test_preparation_and_every_handoff_use_per_run_lines_without_api(self):
        shared_config = prompts.PROMPTS_DIR / "round1_config.json"
        original = shared_config.read_bytes()
        for max_lines, expected in ((250, 250), (None, 500)):
            with self.subTest(max_lines=max_lines), patch("src.enc_dec.run.make_client", side_effect=AssertionError("No API")):
                config = self.config(language_max_lines=max_lines)
                experiment = LanguageExperiment(config)
                experiment.prepare()
                agent = experiment.creation_agents[0]
                ids = [a.agent_id for a in experiment.creation_agents]
                creation = experiment.creation_prompts[agent.agent_id]
                export, _ = prompts.build_language_document_prompt(agent, config, "", "REFERENCE")
                task = prompts.build_task_prompt(agent, ids, config, "REFERENCE")
                saved = json.loads((experiment.logger.path / "language_protocol.json").read_text())["requirements"]
                for text in (creation, export, task, saved):
                    self.assertIn(f"under {expected} lines", text)
                self.assertIn("200 discussion turns shared across all 8 agents", creation)
                self.assertIn("There is no time limit.", creation)
                self.assertNotIn("10 minutes", creation)
                monitor = prepare_monitor_inputs(experiment.logger.path, ["no_task"])
                self.assertIsNone(monitor["minutes"])
                self.assertEqual(monitor["max_turns"], 200)
                self.assertIn("200 discussion turns shared across all 8 agents", monitor["requests"][0]["system_prompt"])
                self.assertNotIn("10 minutes", monitor["requests"][0]["system_prompt"])
        self.assertEqual(shared_config.read_bytes(), original)

    async def test_creation_reserves_exact_budget_and_drains_before_eight_exports(self):
        for limit in (3, 200):
            with self.subTest(limit=limit):
                experiment = LanguageExperiment(self.config(language_max_turns=limit), creation_only=True)
                started = exports = 0
                final_batch_size = min(8, limit)
                final_started = asyncio.Event()
                release = asyncio.Event()

                async def fake(client, model, system, prompt, schema, response_model, config):
                    nonlocal started, exports
                    if response_model is None:
                        exports += 1
                        return result()
                    started += 1
                    ordinal = started
                    if ordinal > limit - final_batch_size:
                        if ordinal == limit:
                            final_started.set()
                        await release.wait()
                    else:
                        await asyncio.sleep(0)
                    return result(CreationResponse(message=f"Turn {ordinal}", language_document=f"DRAFT {ordinal}"))

                client = SimpleNamespace(close=AsyncMock())
                with patch("src.enc_dec.run.make_client", return_value=client), patch("src.enc_dec.run.call_agent", side_effect=fake):
                    running = asyncio.create_task(experiment.run())
                    try:
                        await asyncio.wait_for(final_started.wait(), 5)
                        self.assertEqual(started, limit)
                        self.assertEqual(exports, 0)
                        self.assertFalse(experiment.stop.is_set())
                        self.assertEqual(experiment.creation_turns_in_flight, final_batch_size)
                    finally:
                        release.set()
                        await asyncio.wait_for(running, 5)
                self.assertEqual(started, limit)
                self.assertEqual(exports, 8)
                self.assertEqual(experiment.creation_stop_reason, "turn_limit_reached")
                calls = rows(experiment.logger.path / "agent_calls.jsonl")
                self.assertEqual(len(calls), limit)
                self.assertTrue(all(call["state_applied"] for call in calls))
                self.assertEqual(len(rows(experiment.logger.path / "language_document.jsonl")), 8)
                self.assertEqual((experiment.logger.path / "swarmish.txt").read_text(), "FINAL REFERENCE\n")
                self.assertIn(f"Team discussion turns scheduled: {limit} of {limit}", calls[-1]["turn_prompt"])
                self.assertNotIn("of inf", calls[-1]["turn_prompt"])

    async def test_turn_limited_creation_still_hands_off_to_task(self):
        experiment = LanguageExperiment(self.config(language_max_turns=1))
        real_run_phase = experiment._run_phase

        async def phase(client, name, agents, chat, minutes):
            if name == "task":
                self.assertEqual(experiment.language_text, "FINAL REFERENCE")
                self.assertEqual(len(agents), 8)
                return "offline_task_complete"
            return await real_run_phase(client, name, agents, chat, minutes)

        async def fake(client, model, system, prompt, schema, response_model, config):
            return result(CreationResponse(language_document="DRAFT")) if response_model else result()

        with patch("src.enc_dec.run.make_client", return_value=SimpleNamespace(close=AsyncMock())), \
                patch("src.enc_dec.run.call_agent", side_effect=fake), patch.object(experiment, "_run_phase", side_effect=phase):
            await asyncio.wait_for(experiment.run(), 5)
        self.assertEqual(experiment.creation_stop_reason, "turn_limit_reached")
        self.assertEqual(experiment.task_stop_reason, "offline_task_complete")
        self.assertEqual(len(json.loads((experiment.logger.path / "task_agents.json").read_text())), 8)

    async def test_decoder_reserves_exact_budget_and_applies_last_responses(self):
        for limit in (3, 200):
            with self.subTest(limit=limit):
                config = self.config(monitor_max_turns=limit)
                experiment = LanguageExperiment(config)
                experiment.prepare()
                request = prepare_monitor_inputs(experiment.logger.path, ["no_task"])["requests"][0]
                logger = GameLogger(self.logs.name)
                team = DecodingTeam(None, config, request, logger, 50, 0)
                started = 0
                final_started = asyncio.Event()
                release = asyncio.Event()

                async def fake(*args):
                    nonlocal started
                    started += 1
                    ordinal = started
                    if ordinal > limit - min(8, limit):
                        if ordinal == limit:
                            final_started.set()
                        await release.wait()
                    else:
                        await asyncio.sleep(0)
                    return result(DecodeResponse(message=f"Note {ordinal}", document=f"DRAFT {ordinal}"))

                with patch("src.enc_dec.monitor.call_agent", side_effect=fake):
                    running = asyncio.create_task(team.run())
                    try:
                        await asyncio.wait_for(final_started.wait(), 5)
                        self.assertEqual(started, limit)
                        self.assertFalse(team.stop.is_set())
                    finally:
                        release.set()
                        outcome = await asyncio.wait_for(running, 5)
                self.assertEqual(started, limit)
                self.assertEqual(outcome["stop_reason"], "turn_limit_reached")
                self.assertEqual(outcome["turns_scheduled"], limit)
                self.assertEqual(outcome["answer"], f"DRAFT {limit}")
                calls = rows(logger.path / "monitor_calls.jsonl")
                self.assertEqual(len(calls), limit)
                self.assertTrue(all(call["state_applied"] for call in calls))
                self.assertIn(f"Team discussion turns scheduled: {limit} of {limit}", calls[-1]["turn_prompt"])
                self.assertNotIn("of inf", calls[-1]["turn_prompt"])

    async def test_monitor_budget_resets_per_condition_and_counts_completion(self):
        config = self.config(monitor_max_turns=3)
        experiment = LanguageExperiment(config)
        experiment.prepare()
        bundle = prepare_monitor_inputs(experiment.logger.path, ["no_task", "task_summary"])
        logger = GameLogger(self.logs.name)

        async def fake(*args):
            await asyncio.sleep(0)
            return result(DecodeResponse(document="PARTIAL"))

        with patch("src.enc_dec.monitor.call_agent", side_effect=fake) as call:
            summary = await asyncio.wait_for(execute_monitor_inputs(None, config, bundle, logger, 50), 5)
        self.assertEqual(call.await_count, 6)
        self.assertEqual(summary["stop_reason"], "completed")
        self.assertEqual(summary["conditions_completed"], ["no_task", "task_summary"])
        for row in rows(logger.path / "monitor.jsonl"):
            self.assertEqual(row["turns_scheduled"], 3)
            self.assertEqual(row["stop_reason"], "turn_limit_reached")

    async def test_all_done_still_ends_creation_before_budget(self):
        experiment = LanguageExperiment(self.config(), creation_only=True)

        async def fake(client, model, system, prompt, schema, response_model, config):
            await asyncio.sleep(0)
            return result(CreationResponse(language_document="DRAFT", done=True)) if response_model else result()

        with patch("src.enc_dec.run.make_client", return_value=SimpleNamespace(close=AsyncMock())), \
                patch("src.enc_dec.run.call_agent", side_effect=fake):
            await asyncio.wait_for(experiment.run(), 5)
        self.assertEqual(experiment.creation_stop_reason, "all_done")
        self.assertLess(experiment.creation_turns_scheduled, 200)


if __name__ == "__main__":
    unittest.main()
