"""Replay one saved escape-room conversation under independent monitor briefings.

The briefings and the monitor's system prompt come from src/enc_dec/prompts/round3_prompt.md and
round3_config.json. No task or language-creation calls are made here. --prepare-only requires no
API key.
"""

import argparse
import asyncio
import hashlib
import json
import math
import time
from pathlib import Path

from src.core.api_call import call_agent, make_client
from src.core.game_log import GameLogger
from src.enc_dec.config import LanguageExperimentConfig
from src.enc_dec.escape_room import AGENT_IDS, ROOM_VERSION
from src.enc_dec.prompts import ALL_MONITOR_CONDITIONS, MONITOR_CONDITIONS, build_monitor_prompt

CONDITION_LABELS = {
    "task_summary": "Task summary",
    "task_full": "Full task knowledge",
    "task_mechanics": "Task mechanics",
    "no_task": "No task briefing",
    "wrong_task": "Wrong task",
}

def read_public_messages(path: Path) -> list[dict]:
    """Whitelist fields. Never render timestamps, raw completions or private annotations."""
    messages = []
    for line in path.read_text(encoding="utf-8").splitlines():
        row = json.loads(line)
        if row["sender"] not in (*AGENT_IDS, "task") or not isinstance(row["text"], str):
            raise ValueError("Not an eight-agent task transcript")
        messages.append({"id": len(messages) + 1, "sender": row["sender"], "text": row["text"]})
    return messages


def render_public_messages(messages: list[dict], baseline: bool = False) -> str:
    return "\n".join(
        f"[{m['id']}] [{m['sender']}] " +
        ("[message withheld]" if baseline and m["sender"] != "task" else m["text"])
        for m in messages
    ) or "(no messages)"


def prepare_monitor_inputs(source: str | Path, conditions=MONITOR_CONDITIONS, baseline: bool = False) -> dict:
    source = Path(source)
    if not conditions or len(set(conditions)) != len(conditions) or any(c not in ALL_MONITOR_CONDITIONS for c in conditions):
        raise ValueError(f"Select distinct conditions from {ALL_MONITOR_CONDITIONS}")
    config = LanguageExperimentConfig.from_file(source / "config.json")
    # Read saved ground truth, not the current source-code instance, for reproducibility.
    definition = json.loads((source / "escape_room_definition.json").read_text(encoding="utf-8"))
    if definition["version"] != ROOM_VERSION:
        raise ValueError("Unsupported escape room definition version")
    messages = read_public_messages(source / "task_chatroom.jsonl")
    original = render_public_messages(messages)
    transcript = render_public_messages(messages, baseline)
    sha = lambda text: hashlib.sha256(text.encode("utf-8")).hexdigest()
    return {
        "room_version": definition["version"], "source": str(source.resolve()),
        "baseline": baseline, "message_count": len(messages),
        "source_transcript_sha256": sha(original), "transcript_sha256": sha(transcript),
        "transcript": transcript,
        "requests": [
            {"condition": condition, "label": CONDITION_LABELS[condition], "system_prompt": system, "prompt": prompt}
            for condition in conditions
            for system, prompt in [build_monitor_prompt(config, condition, definition, transcript)]
        ],
    }


async def execute_monitor_inputs(client, config: LanguageExperimentConfig, bundle: dict, logger: GameLogger, max_cost_usd: float | None) -> dict:
    """Each request has a fresh two-message context. A cap stops scheduling further calls."""
    settings = config.model_copy(update={
        "max_tokens": config.monitor_max_tokens,
        "reasoning_effort": config.monitor_reasoning_effort or config.reasoning_effort,
    })
    model = config.model_for(0, "monitor")
    total, completed, stop_reason = 0.0, [], "completed"
    missing_cost = False
    started = time.monotonic()
    try:
        for request in bundle["requests"]:
            if max_cost_usd is not None and total >= max_cost_usd:
                stop_reason = "cost_limit_reached"
                break
            call_start = time.monotonic()
            try:
                result = await call_agent(client, model, request["system_prompt"], request["prompt"], None, None, settings)
            except Exception as exc:
                logger.log("errors", {"phase": "monitor", "condition": request["condition"], "timestamp": time.time(), "error": repr(exc)})
                stop_reason = "api_error"
                break
            cost = (result.usage or {}).get("cost")
            total += cost or 0.0
            missing_cost |= cost is None
            logger.log("monitor", {
                **request, "model": model, "timestamp": time.time(),
                "elapsed_s": time.monotonic() - call_start,
                "baseline": bundle["baseline"], "transcript_sha256": bundle["transcript_sha256"],
                "source_transcript_sha256": bundle["source_transcript_sha256"],
                "answer": result.raw, "usage": result.usage, "finish_reason": result.finish_reason,
                "max_tokens": settings.max_tokens, "reasoning_effort": settings.reasoning_effort,
            })
            completed.append(request["condition"])
            if cost is None and max_cost_usd is not None:
                stop_reason = "usage_cost_missing"
                break
    except BaseException:
        stop_reason = "interrupted_or_failed"
        raise
    finally:
        summary = {
            "phase": "monitor", "model": model, "source": bundle["source"],
            "conditions_requested": [r["condition"] for r in bundle["requests"]],
            "conditions_completed": completed, "stop_reason": stop_reason,
            "total_cost_usd": total, "cost_incomplete": missing_cost,
            "max_cost_usd": max_cost_usd, "baseline": bundle["baseline"],
            "elapsed_s": time.monotonic() - started,
            "transcript_sha256": bundle["transcript_sha256"],
            "source_transcript_sha256": bundle["source_transcript_sha256"],
        }
        logger.write_json("monitor_summary", summary)
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="completed escape-room log directory")
    parser.add_argument("--condition", action="append", choices=ALL_MONITOR_CONDITIONS,
                        help=f"repeat to select conditions; default {', '.join(MONITOR_CONDITIONS)}")
    parser.add_argument("--model", help="override monitor model")
    parser.add_argument("--max-cost-usd", type=float, default=5.0, help="soft cap for these monitor calls, default $5")
    parser.add_argument("--baseline", action="store_true", help="withhold agent messages, preserve identical public status and sender/order metadata")
    parser.add_argument("--prepare-only", action="store_true", help="save and inspect prompts without making any API calls")
    args = parser.parse_args()
    if not math.isfinite(args.max_cost_usd) or args.max_cost_usd <= 0:
        parser.error("--max-cost-usd must be positive and finite")
    config = LanguageExperimentConfig.from_file(args.source / "config.json")
    if config.task_kind != "escape_room":
        parser.error("source must be an escape-room run")
    if args.model:
        config = config.model_copy(update={"monitor_model": args.model})
    bundle = prepare_monitor_inputs(args.source, args.condition or MONITOR_CONDITIONS, args.baseline)
    logger = GameLogger(str(args.source / "monitor_runs"))
    logger.write_json("monitor_inputs", bundle)
    logger.write_json("monitor_config", {**config.model_dump(), "max_cost_usd": args.max_cost_usd})
    print(f"Monitor inputs: {logger.path / 'monitor_inputs.json'}")
    if args.prepare_only:
        return

    async def run():
        client = make_client(config)
        try:
            summary = await execute_monitor_inputs(client, config, bundle, logger, args.max_cost_usd)
            print(f"Monitor result: {summary['stop_reason']}; recorded spend ${summary['total_cost_usd']:.4f}")
        finally:
            await client.close()
    asyncio.run(run())


if __name__ == "__main__":
    main()
