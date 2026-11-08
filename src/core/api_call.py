"""
OpenRouter API calls (OPENROUTER_API_KEY and optional OPENROUTER_API_KEY_SECONDARY).

Each call sends a system prompt and a turn prompt. With a schema, the reply is parsed into
response_model. With both set to None, the reply is free text and only `raw` is filled in.
The caller logs the result.
"""

import asyncio
import json
import os
import re
from typing import Any, Protocol

from dotenv import load_dotenv
from openai import APIStatusError, AsyncOpenAI, BadRequestError
from pydantic import BaseModel, ValidationError


class ModelSettings(Protocol):
    request_timeout_s: float
    max_tokens: int
    temperature: float | None
    reasoning_effort: Any

OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"


def _exhausted_key(exc: APIStatusError) -> bool:
    """Rotate only for depleted credit, never request-size or policy limits."""
    if exc.status_code not in {402, 403}:
        return False
    body = exc.body if isinstance(exc.body, dict) else {}
    error = body.get("error", body)
    error = error if isinstance(error, dict) else {}
    metadata = error.get("metadata") or {}
    if not isinstance(metadata, dict):
        return False
    source, reason = metadata.get("limit_source"), metadata.get("reason")
    if reason in {"weight_exceeds_budget", "in_flight_budget_exhausted"}:
        return False
    if source == "openrouter_key_limit":
        return True
    if exc.status_code != 402:
        return False
    if source == "openrouter_credits":
        return True
    if metadata:
        # An unfamiliar restriction is not permission to spend another key.
        return False
    message = str(error.get("message", "")).lower()
    if re.search(r"afford|max[_ -]?tokens|in[_ -]?flight|reservation|concurrent|budget|guardrail|workspace", message):
        return False
    return bool(re.search(
        r"\b(?:insufficient credits?|(?:out of|no|not enough) credits?|credits? (?:are |is )?exhausted|exhausted credits?)\b",
        message,
    ))


class OpenRouterClient:
    """Fixed credentials with a one-way, concurrency-safe credit fallback."""

    def __init__(self, primary: AsyncOpenAI, secondary: AsyncOpenAI | None = None):
        self._clients = (primary,) if secondary is None else (primary, secondary)
        self._active = 0
        self._promotion_lock = asyncio.Lock()

    async def create_completion(self, **kwargs) -> tuple[Any, str]:
        selected = self._active
        try:
            result = await self._clients[selected].chat.completions.create(**kwargs)
        except APIStatusError as exc:
            if selected != 0 or len(self._clients) == 1 or not _exhausted_key(exc):
                raise
            async with self._promotion_lock:
                # Other primary requests may fail after another task has switched.
                # Their retries share the same secondary; existing successes survive.
                self._active = 1
            selected = 1
            result = await self._clients[selected].chat.completions.create(**kwargs)
        return result, "primary" if selected == 0 else "secondary"

    async def close(self) -> None:
        await asyncio.gather(*(client.close() for client in self._clients))


class CallResult(BaseModel):
    raw: str
    parsed: BaseModel | None  # instance of the response_model passed to call_agent
    parse_error: str | None = None
    used_structured_output: bool
    usage: dict | None = None
    finish_reason: str | None = None


def make_client(config: ModelSettings) -> OpenRouterClient:
    load_dotenv()
    primary_key = os.environ["OPENROUTER_API_KEY"].strip()
    secondary_key = os.environ.get("OPENROUTER_API_KEY_SECONDARY", "").strip()
    kwargs = {"base_url": OPENROUTER_BASE_URL, "timeout": config.request_timeout_s}
    primary = AsyncOpenAI(api_key=primary_key, **kwargs)
    secondary = AsyncOpenAI(api_key=secondary_key, **kwargs) if secondary_key and secondary_key != primary_key else None
    return OpenRouterClient(primary, secondary)


async def _create_completion(client: AsyncOpenAI | OpenRouterClient, **kwargs) -> tuple[Any, str | None]:
    if isinstance(client, OpenRouterClient):
        return await client.create_completion(**kwargs)
    # Preserve direct SDK clients and lightweight offline test clients.
    return await client.chat.completions.create(**kwargs), None


def parse_response(raw: str, response_model: type[BaseModel]) -> BaseModel:
    """Parse a model's text into response_model, tolerating code fences or surrounding prose."""
    text = re.sub(r"^```(?:json)?\s*|\s*```$", "", raw.strip())
    start, end = text.find("{"), text.rfind("}")
    if start == -1 or end == -1:
        raise ValueError("no JSON object found in response")
    data = json.loads(text[start : end + 1])
    try:
        # Check both literal provider text and JSON-decoded fields before they
        # can enter shared state, the next API request, or a UTF-8 text export.
        # Proper escaped surrogate pairs decode to valid non-BMP characters.
        raw.encode("utf-8")
        json.dumps(data, ensure_ascii=False).encode("utf-8")
    except UnicodeEncodeError as exc:
        code_point = ord(exc.object[exc.start])
        raise ValueError(f"response contains an unpaired Unicode surrogate U+{code_point:04X}") from exc
    return response_model.model_validate(data)


async def call_agent(
    client: AsyncOpenAI | OpenRouterClient,
    model: str,
    system_prompt: str,
    turn_prompt: str,
    json_schema: dict | None,
    response_model: type[BaseModel] | None,
    config: ModelSettings,
) -> CallResult:
    """With json_schema/response_model set to None, the reply is free text and only `raw` is filled in."""
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": turn_prompt},
    ]
    extra_body: dict = {"usage": {"include": True}}  # asks OpenRouter to report per-call cost
    if config.reasoning_effort is not None:
        extra_body["reasoning"] = {"effort": config.reasoning_effort}
    kwargs = dict(model=model, messages=messages, max_tokens=config.max_tokens, extra_body=extra_body)
    if config.temperature is not None:
        kwargs["temperature"] = config.temperature

    # Prefer schema-enforced output; some OpenRouter models reject response_format, so fall back to plain text.
    structured = json_schema is not None
    completion = None
    key_slot = None
    if structured:
        try:
            completion, key_slot = await _create_completion(
                client, **kwargs, response_format={"type": "json_schema", "json_schema": json_schema}
            )
        except BadRequestError:
            structured = False
    if completion is None:
        completion, key_slot = await _create_completion(client, **kwargs)

    raw = completion.choices[0].message.content or ""
    usage = completion.usage.model_dump() if completion.usage else None
    if usage is not None and key_slot is not None:
        usage["api_key_slot"] = key_slot
    if response_model is None:
        return CallResult(raw=raw, parsed=None, used_structured_output=False, usage=usage,
                          finish_reason=completion.choices[0].finish_reason)
    try:
        parsed, error = parse_response(raw, response_model), None
    except (ValueError, ValidationError) as e:
        parsed, error = None, str(e)

    return CallResult(raw=raw, parsed=parsed, parse_error=error, used_structured_output=structured, usage=usage,
                      finish_reason=completion.choices[0].finish_reason)
