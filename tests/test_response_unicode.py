"""Malformed provider Unicode must be retained in logs without poisoning a team."""

import asyncio
import json
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import AsyncMock

from src.core.api_call import call_agent, parse_response
from src.core.game_log import GameLogger
from src.enc_dec.config import LanguageExperimentConfig
from src.enc_dec.models import DECODE_SCHEMA, DecodeResponse
from src.enc_dec.monitor import execute_monitor_inputs


def completion(raw):
    return SimpleNamespace(
        choices=[SimpleNamespace(message=SimpleNamespace(content=raw), finish_reason="stop")],
        usage=SimpleNamespace(model_dump=lambda: {"cost": 0.001}),
    )


def client_with(create):
    return SimpleNamespace(chat=SimpleNamespace(completions=SimpleNamespace(create=create)))


def settings(**overrides):
    return LanguageExperimentConfig(**{
        "task_prompt": "Offline test", "model": "offline-model",
        "glyph_dictionary": "glyphs_latin", "monitor_n_agents": 1,
        "monitor_minutes": None, "monitor_max_turns": 3, "min_turn_interval_s": 0,
        **overrides,
    })


class ResponseUnicodeTests(unittest.IsolatedAsyncioTestCase):
    def test_logger_retains_surrogates_and_readable_tangut(self):
        record = {"raw": "𗏔\ud869 text \udb84", "nested": {"\udc00": ["𗄪"]}}
        with tempfile.TemporaryDirectory() as directory:
            logger = GameLogger(directory)
            logger.log("calls", record)
            logger.write_json("summary", record)
            for filename in ("calls.jsonl", "summary.json"):
                text = (logger.path / filename).read_text(encoding="utf-8")
                self.assertIn("𗏔", text)
                self.assertIn("𗄪", text)
                self.assertIn(r"\ud869", text)
                self.assertIn(r"\udb84", text)
                self.assertEqual(json.loads(text), record)

    def test_parser_rejects_literal_and_json_escaped_surrogates(self):
        for raw in (
            '{"message":"bad\ud869","document":"bad","done":true}',
            r'{"message":"fine","document":"bad\udb84","done":true}',
            r'{"message":"fine","document":"fine","extra":{"\udc00":[]}}',
            '\ud869 prose {"message":"fine","document":"fine"}',
        ):
            with self.subTest(raw=ascii(raw)), self.assertRaisesRegex(ValueError, "unpaired Unicode surrogate"):
                parse_response(raw, DecodeResponse)

    def test_parser_accepts_normal_tangut_and_valid_escaped_pairs(self):
        expected = {"message": "𗏔 𗄪", "document": "Valid 𘙠", "done": True}
        for ensure_ascii in (True, False):
            with self.subTest(ensure_ascii=ensure_ascii):
                parsed = parse_response(json.dumps(expected, ensure_ascii=ensure_ascii), DecodeResponse)
                self.assertEqual(parsed.model_dump(), expected)

    async def test_rejected_response_keeps_raw_usage_and_finish_reason(self):
        raw = '{"message":"bad\ud869","document":"draft","done":true}'
        client = client_with(AsyncMock(return_value=completion(raw)))
        result = await call_agent(client, "offline-model", "system", "turn", DECODE_SCHEMA, DecodeResponse, settings())
        self.assertIsNone(result.parsed)
        self.assertIn("U+D869", result.parse_error)
        self.assertEqual(result.raw, raw)
        self.assertEqual(result.usage, {"cost": 0.001})
        self.assertEqual(result.finish_reason, "stop")

    async def test_decoder_continues_after_bad_unicode_without_applying_state(self):
        raws = [
            '{"message":"REJECTED CHAT","document":"bad\ud869","done":true}',
            r'{"message":"REJECTED CHAT","document":"bad\udb84","done":true}',
            '{"message":"Accepted 𗏔","document":"Good final 𗄪","done":true}',
        ]
        seen = []

        async def create(**kwargs):
            for message in kwargs["messages"]:
                message["content"].encode("utf-8")
                self.assertNotIn("REJECTED CHAT", message["content"])
                self.assertNotIn("bad", message["content"])
            seen.append(kwargs)
            return completion(raws[len(seen) - 1])

        request = {
            "condition": "task_full", "label": "Full task knowledge", "prompt": "Transcript",
            "system_prompt": "Offline decoder", "system_prompts": {"decoder_0": "Offline decoder"},
        }
        bundle = {
            "requests": [request], "baseline": False, "source": "offline-source",
            "transcript_sha256": "offline", "source_transcript_sha256": "offline",
        }
        with tempfile.TemporaryDirectory() as directory:
            logger = GameLogger(directory)
            summary = await asyncio.wait_for(execute_monitor_inputs(
                client_with(create), settings(), bundle, logger, 50,
            ), timeout=5)
            self.assertEqual(summary["conditions_completed"], ["task_full"])
            self.assertAlmostEqual(summary["total_cost_usd"], 0.003)
            calls = [json.loads(line) for line in (logger.path / "monitor_calls.jsonl").read_text().splitlines()]
            self.assertEqual([row["state_applied"] for row in calls], [False, False, True])
            self.assertEqual([row["raw"] for row in calls], raws)
            self.assertTrue(all(row["response"] is None and row["parse_error"] for row in calls[:2]))
            chat = [json.loads(line) for line in (logger.path / "monitor_chat_task_full.jsonl").read_text().splitlines()]
            self.assertEqual([row["text"] for row in chat], ["Accepted 𗏔"])
            outcome = json.loads((logger.path / "monitor.jsonl").read_text())
            self.assertEqual(outcome["stop_reason"], "all_done")
            self.assertEqual(outcome["answer"], "Good final 𗄪")
            self.assertEqual(outcome["turns"], {"decoder_0": 3})
            # The same final report can also be exported as ordinary UTF-8 text.
            Path(directory, "decoded.txt").write_text(outcome["answer"], encoding="utf-8")
            self.assertTrue((logger.path / "monitor_summary.json").exists())


if __name__ == "__main__":
    unittest.main()
