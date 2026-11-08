"""Prepare or explicitly launch a fresh D12 retry, preserving the failed attempt."""
import argparse
import asyncio
from datetime import datetime, timezone
import json
from pathlib import Path
import sys

REPO = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO))

from experiments.tangut_200g_250l_200t import batch
from src.core.api_call import make_client
from src.core.game_log import GameLogger
from src.enc_dec.monitor import execute_monitor_inputs, prepare_monitor_inputs

FOLDER = Path(__file__).resolve().parent
ATTEMPT = FOLDER / "attempts/retry1"


def prepare():
    folder, plan, config = batch.run_info(batch.BATCH, "D12")
    failure = batch.read(folder / "failure.json")
    batch.require(failure["status"] == "failed", "Original D12 must remain recorded as failed")
    original_raw = REPO / failure["raw_path"]
    for name, digest in failure["raw_sha256"].items():
        batch.require(batch.sha(original_raw / name) == digest, f"Original failure archive changed: {name}")
    source_folder, source_receipt, source_raw = batch.dependency(batch.BATCH, plan)
    config = config.model_copy(update={"log_dir": str(ATTEMPT / "raw")})
    bundle = prepare_monitor_inputs(source_raw, ["task_full"], config=config)
    previous = batch.read(original_raw / "monitor_inputs.json")
    for key in ("requests", "transcript", "transcript_sha256", "source_transcript_sha256",
                "n_agents", "max_turns", "minutes", "baseline"):
        batch.require(bundle[key] == previous[key], f"Retry would change decoder input: {key}")
    batch.require(config.monitor_max_turns == 200 and config.monitor_n_agents == 8
                  and config.monitor_minutes is None and config.max_cost_usd == 50
                  and config.monitor_max_tokens == 16000
                  and config.monitor_reasoning_effort == "high", "Retry settings differ")
    ATTEMPT.mkdir(parents=True, exist_ok=True)
    batch.write(ATTEMPT / "config.json", config.model_dump())
    batch.write(ATTEMPT / "plan.json", {
        **plan, "attempt_id": "D12_retry1", "retry_of": "D12",
        "reason": "Fresh attempt after Unicode logging failure; invalid Unicode is now rejected before shared state changes.",
        "original_failure_sha256": batch.sha(folder / "failure.json"),
        "fresh_agents": True, "original_prompts_and_transcript_unchanged": True,
        "protocol_deviation": "Malformed Unicode structured responses are logged losslessly and treated as parse errors.",
    })
    batch.write(ATTEMPT / "prepared_inputs.json", bundle)
    return config, bundle, batch.gameplay_source_outcome(source_folder, source_receipt, plan)


def launch():
    with batch.locked(ATTEMPT):
        batch.require(not (ATTEMPT / "execution.json").exists(), "Retry already launched; inspect its saved outputs")
        config, bundle, source_outcome = prepare()
        logger = GameLogger(config.log_dir, "round_3")
        logger.write_json("monitor_inputs", bundle)
        logger.write_json("monitor_config", config.model_dump())
        batch.write(ATTEMPT / "execution.json", {
            **batch.provenance(ATTEMPT), "attempt_id": "D12_retry1",
            "retry_launcher_sha256": batch.sha(__file__),
            "raw_path": str(logger.path.relative_to(REPO)), "source_gameplay": source_outcome,
        })
        print(f"Launched D12_retry1: {logger.path}", flush=True)

        async def execute():
            client = make_client(config)
            try:
                return await execute_monitor_inputs(client, config, bundle, logger, config.max_cost_usd)
            finally:
                await client.close()

        summary = asyncio.run(execute())
        outcomes = batch.rows(logger.path / "monitor.jsonl")
        completed = summary["conditions_completed"] == ["task_full"]
        batch.require(len(outcomes) == 1 and outcomes[0]["condition"] == "task_full", "Missing final retry outcome")
        outcome = outcomes[0]
        if completed:
            batch.require(bool(outcome["answer"].strip()), "Completed retry lacks a decoder document")
            (ATTEMPT / "decoded.txt").write_text(outcome["answer"] + "\n", encoding="utf-8")
        calls = batch.rows(logger.path / "monitor_calls.jsonl")
        batch.require(len(calls) <= 200, "Retry exceeded shared call limit")
        batch.write(ATTEMPT / "receipt.json", {
            "schema_version": 1, "id": "D12_retry1", "retry_of": "D12",
            "status": "completed" if completed else "failed",
            "collected_at": datetime.now(timezone.utc).isoformat(),
            "raw_path": str(logger.path.relative_to(REPO)), "summary": summary,
            "source_gameplay": source_outcome, "discussion_calls": len(calls),
            "stop_reason": outcome["stop_reason"],
            "parse_errors": sum(bool(call.get("parse_error")) for call in calls),
            "unicode_parse_errors": sum("Unicode" in (call.get("parse_error") or "") for call in calls),
            "raw_sha256": {path.name: batch.sha(path) for path in batch.archive_files(logger.path)},
            "notes": ["The original D12 failure and all its raw files remain unchanged.",
                      "This is a fresh decoder team, with the original full-task prompts and public transcript."],
        })
        print(json.dumps({"attempt": "D12_retry1", "status": "completed" if completed else "failed",
                          "calls": len(calls), "cost_usd": summary["total_cost_usd"],
                          "stop_reason": outcome["stop_reason"]}), flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--execute", action="store_true", help="Make paid API calls; otherwise prepare only")
    args = parser.parse_args()
    if args.execute:
        launch()
    else:
        prepare()
        print(f"Prepared D12_retry1 without API calls: {ATTEMPT}")
