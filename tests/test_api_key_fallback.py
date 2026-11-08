"""Offline checks for credit fallback without changing experiment budgets."""

import asyncio
import json
import os
import tempfile
import unittest
from types import SimpleNamespace
from unittest.mock import AsyncMock, patch

from openai import APIStatusError, BadRequestError

from src.core.api_call import OpenRouterClient, _exhausted_key, call_agent, make_client
from src.core.game_log import GameLogger
from src.enc_dec.config import LanguageExperimentConfig
from src.enc_dec.models import DECODE_SCHEMA, DecodeResponse
from src.enc_dec.monitor import execute_monitor_inputs


def api_error(status=402, *, source=None, reason=None, message="Insufficient credits", wrapped=False):
    body = {"message": message}
    if source is not None or reason is not None:
        body["metadata"] = {"limit_source": source, "reason": reason}
    if wrapped:
        body = {"error": body}
    error_class = BadRequestError if status == 400 else APIStatusError
    return error_class(message, response=SimpleNamespace(status_code=status, request=None, headers={}), body=body)


def completion(cost=0.01, *, missing_usage=False):
    return SimpleNamespace(
        choices=[SimpleNamespace(message=SimpleNamespace(content=json.dumps({
            "message": "Offline reply", "document": "Translation", "done": False,
        })), finish_reason="stop")],
        usage=None if missing_usage else SimpleNamespace(model_dump=lambda: {"cost": cost}),
    )


def client(create):
    return SimpleNamespace(chat=SimpleNamespace(completions=SimpleNamespace(create=create)), close=AsyncMock())


def settings():
    return LanguageExperimentConfig(
        task_prompt="Offline test", model="offline-model", glyph_dictionary="glyphs_latin",
        monitor_n_agents=1, monitor_minutes=None, monitor_max_turns=10, min_turn_interval_s=0,
    )


class ApiKeyFallbackTests(unittest.IsolatedAsyncioTestCase):
    def test_only_confirmed_credit_errors_rotate(self):
        accepted = [
            api_error(source="openrouter_credits"),
            api_error(source="openrouter_credits", wrapped=True),
            api_error(source="openrouter_key_limit"),
            api_error(403, source="openrouter_key_limit"),
            api_error(message="Your account has insufficient credits."),
            api_error(message="Credits are exhausted."),
            api_error(message="You are out of credits."),
        ]
        rejected = [
            api_error(code, source="openrouter_credits") for code in (400, 401, 403, 404, 429, 500, 503)
        ] + [
            api_error(source="openrouter_credits", reason="weight_exceeds_budget"),
            api_error(source="openrouter_credits", reason="in_flight_budget_exhausted"),
            api_error(source="openrouter_in_flight_budget", reason="in_flight_budget_exhausted"),
            api_error(403, source="openrouter_guardrail_budget"),
            api_error(403, source="openrouter_workspace_budget"),
            api_error(source="unknown_limit"),
            api_error(403),
            api_error(message="Insufficient credits for the requested max_tokens."),
            api_error(message="Insufficient credits: in-flight reservation exhausted."),
            api_error(message="Insufficient credits for this workspace budget."),
            api_error(message="Insufficient credits: can only afford 20 tokens."),
            api_error(message="Payment required"),
        ]
        # Explicit legacy text is accepted only when metadata is absent/empty.
        # Unknown metadata may represent a restriction we should not bypass.
        unknown_metadata = api_error()
        unknown_metadata.body["metadata"] = {"provider_name": None}
        rejected.append(unknown_metadata)
        for error in accepted:
            with self.subTest(accepted=error.body):
                self.assertTrue(_exhausted_key(error))
        for error in rejected:
            with self.subTest(rejected=error.body, status=error.status_code):
                self.assertFalse(_exhausted_key(error))

    async def test_primary_success_and_close(self):
        first = client(AsyncMock(return_value=completion()))
        second = client(AsyncMock(return_value=completion()))
        pool = OpenRouterClient(first, second)
        result = await call_agent(pool, "offline", "system", "turn", None, None, settings())
        self.assertEqual(result.usage, {"cost": 0.01, "api_key_slot": "primary"})
        second.chat.completions.create.assert_not_called()
        await pool.close()
        first.close.assert_awaited_once()
        second.close.assert_awaited_once()

    async def test_exhaustion_retries_same_request_and_sticks(self):
        first = client(AsyncMock(side_effect=api_error(403, source="openrouter_key_limit")))
        second = client(AsyncMock(return_value=completion()))
        pool = OpenRouterClient(first, second)
        request = {"model": "offline", "messages": [{"role": "user", "content": "test"}], "max_tokens": 123}
        _, slot = await pool.create_completion(**request)
        self.assertEqual(slot, "secondary")
        first.chat.completions.create.assert_awaited_once_with(**request)
        second.chat.completions.create.assert_awaited_once_with(**request)
        await pool.create_completion(**request)
        self.assertEqual(first.chat.completions.create.await_count, 1)
        self.assertEqual(second.chat.completions.create.await_count, 2)

    async def test_concurrent_failures_and_late_primary_success(self):
        all_started = asyncio.Event()
        release_errors = asyncio.Event()
        release_success = asyncio.Event()
        started = 0

        async def primary(**kwargs):
            nonlocal started
            started += 1
            if started == 3:
                all_started.set()
            if kwargs["model"] == "late-success":
                await release_success.wait()
                return completion(0.02)
            await release_errors.wait()
            raise api_error(source="openrouter_credits")

        first = client(AsyncMock(side_effect=primary))
        second = client(AsyncMock(return_value=completion(0.03)))
        pool = OpenRouterClient(first, second)
        late = asyncio.create_task(pool.create_completion(model="late-success"))
        failures = [asyncio.create_task(pool.create_completion(model=f"failure-{i}")) for i in range(2)]
        await asyncio.wait_for(all_started.wait(), timeout=1)
        release_errors.set()
        replies = await asyncio.wait_for(asyncio.gather(*failures), timeout=1)
        self.assertEqual([slot for _, slot in replies], ["secondary", "secondary"])
        _, slot = await pool.create_completion(model="after-promotion")
        self.assertEqual(slot, "secondary")
        release_success.set()
        late_result, late_slot = await asyncio.wait_for(late, timeout=1)
        self.assertEqual(late_slot, "primary")
        self.assertEqual(late_result.usage.model_dump()["cost"], 0.02)
        self.assertEqual(first.chat.completions.create.await_count, 3)
        self.assertEqual(second.chat.completions.create.await_count, 3)

    async def test_secondary_failure_never_cycles(self):
        first = client(AsyncMock(side_effect=api_error()))
        secondary_error = api_error(source="openrouter_credits")
        second = client(AsyncMock(side_effect=secondary_error))
        pool = OpenRouterClient(first, second)
        for _ in range(2):
            with self.assertRaises(APIStatusError) as caught:
                await pool.create_completion(model="offline")
            self.assertIs(caught.exception, secondary_error)
        self.assertEqual(first.chat.completions.create.await_count, 1)
        self.assertEqual(second.chat.completions.create.await_count, 2)

    async def test_unrelated_errors_and_missing_secondary_propagate(self):
        for error in (api_error(401), api_error(429), api_error(403), api_error(message="Payment required"), RuntimeError("offline")):
            with self.subTest(error=type(error).__name__, status=getattr(error, "status_code", None)):
                second = client(AsyncMock())
                pool = OpenRouterClient(client(AsyncMock(side_effect=error)), second)
                with self.assertRaises(type(error)) as caught:
                    await pool.create_completion(model="offline")
                self.assertIs(caught.exception, error)
                second.chat.completions.create.assert_not_called()
        error = api_error()
        pool = OpenRouterClient(client(AsyncMock(side_effect=error)))
        with self.assertRaises(APIStatusError) as caught:
            await pool.create_completion(model="offline")
        self.assertIs(caught.exception, error)

    async def test_schema_fallback_after_promotion(self):
        first = client(AsyncMock(side_effect=api_error()))
        second = client(AsyncMock(side_effect=[api_error(400, message="Unsupported schema"), completion()]))
        result = await call_agent(OpenRouterClient(first, second), "offline", "system", "turn", DECODE_SCHEMA, DecodeResponse, settings())
        self.assertFalse(result.used_structured_output)
        self.assertIsInstance(result.parsed, DecodeResponse)
        self.assertEqual(result.usage["api_key_slot"], "secondary")
        self.assertEqual(first.chat.completions.create.await_count, 1)
        self.assertEqual(second.chat.completions.create.await_count, 2)
        first_request = first.chat.completions.create.call_args.kwargs
        secondary_requests = [call.kwargs for call in second.chat.completions.create.call_args_list]
        self.assertEqual(first_request, secondary_requests[0])
        self.assertIn("response_format", first_request)
        self.assertNotIn("response_format", secondary_requests[1])

    async def test_usage_absence_and_direct_fake_compatibility(self):
        result = await call_agent(OpenRouterClient(client(AsyncMock(return_value=completion(missing_usage=True)))), "offline", "system", "turn", None, None, settings())
        self.assertIsNone(result.usage)
        result = await call_agent(client(AsyncMock(return_value=completion())), "offline", "system", "turn", None, None, settings())
        self.assertEqual(result.usage, {"cost": 0.01})

    def test_environment_ignores_empty_and_duplicate_backup(self):
        for secondary, expected in ((None, 1), (" ", 1), (" primary-test ", 1), ("secondary-test", 2)):
            environment = {"OPENROUTER_API_KEY": "primary-test"}
            if secondary is not None:
                environment["OPENROUTER_API_KEY_SECONDARY"] = secondary
            with self.subTest(secondary=secondary), patch.dict(os.environ, environment, clear=True), patch("src.core.api_call.load_dotenv"), patch("src.core.api_call.AsyncOpenAI") as constructor:
                pool = make_client(settings())
                self.assertEqual(constructor.call_count, expected)
                self.assertEqual(len(pool._clients), expected)

    async def test_monitor_cost_cap_spans_both_keys(self):
        first = client(AsyncMock(side_effect=[completion(0.06), api_error()]))
        second = client(AsyncMock(return_value=completion(0.06)))
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
            summary = await asyncio.wait_for(execute_monitor_inputs(OpenRouterClient(first, second), settings(), bundle, logger, 0.1), timeout=2)
            self.assertAlmostEqual(summary["total_cost_usd"], 0.12)
            calls = [json.loads(line) for line in (logger.path / "monitor_calls.jsonl").read_text().splitlines()]
            self.assertEqual([row["usage"]["api_key_slot"] for row in calls], ["primary", "secondary"])
            outcome = json.loads((logger.path / "monitor.jsonl").read_text())
            self.assertEqual(outcome["stop_reason"], "cost_limit_reached")
            self.assertEqual(len(calls), 2)
            self.assertEqual(first.chat.completions.create.await_count, 2)
            self.assertEqual(second.chat.completions.create.await_count, 1)


if __name__ == "__main__":
    unittest.main()
