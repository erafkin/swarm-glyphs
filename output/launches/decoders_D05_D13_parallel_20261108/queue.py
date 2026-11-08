"""Run the nine authorized decoder cells once, with at most three live runs."""
import fcntl
import hashlib
import json
import os
from pathlib import Path
import subprocess
import time
from datetime import datetime, timezone

REPO = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
BATCH = REPO / "experiments/tangut_200g_250l_200t"
PYTHON = REPO / ".venv/bin/python"
RUNS = ["D05", "D08", "D11", "D06", "D09", "D12", "D07", "D10", "D13"]
MAX_PARALLEL = 3


def now():
    return datetime.now(timezone.utc).isoformat()


def read(path):
    return json.loads(path.read_text())


def save(state):
    pending = HERE / "queue_state.json.tmp"
    pending.write_text(json.dumps(state, indent=2) + "\n")
    pending.replace(HERE / "queue_state.json")


def fingerprints(dirs):
    paths = set((REPO / "src").rglob("*.py"))
    paths.update(p for p in (REPO / "src/enc_dec/prompts").glob("*") if p.is_file())
    paths.add(BATCH / "batch.py")
    for run_id in RUNS:
        paths.update(dirs[run_id] / name for name in ("config.json", "plan.json"))
    return {str(p.relative_to(REPO)): hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)}


def main():
    with (HERE / ".queue.lock").open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        return run_queue()


def run_queue():
    if (HERE / "queue_state.json").exists():
        raise RuntimeError("Queue already initialized; refusing a duplicate launch")
    manifest = read(BATCH / "batch.json")
    dirs = {r["id"]: BATCH / r["path"] for r in manifest["runs"]}
    for run_id in RUNS:
        config = read(dirs[run_id] / "config.json")
        plan = read(dirs[run_id] / "plan.json")
        expected = {"monitor_n_agents": 8, "monitor_max_turns": 200,
                    "monitor_minutes": None, "max_cost_usd": 50, "monitor_max_tokens": 16000}
        if any(config.get(k) != v for k, v in expected.items()):
            raise RuntimeError(f"{run_id}: limits differ from authorized settings")
        if plan["source_run_id"] not in ("R06", "R07", "R08"):
            raise RuntimeError(f"{run_id}: unexpected gameplay source")
        if any((dirs[run_id] / name).exists() for name in ("execution.json", "receipt.json")):
            raise RuntimeError(f"{run_id} already launched or collected")
    baseline = fingerprints(dirs)
    state = {"status": "running", "started_at": now(), "pid": os.getpid(),
             "max_parallel_runs": MAX_PARALLEL, "max_agents_in_flight": 24,
             "runs": RUNS, "pending": list(RUNS), "active": {}, "completed": [], "failed": [],
             "notes": "Independent decoder teams and logs. Concurrent runs share the OpenRouter key; wall-clock timings are recorded under overlap. No retries or Sol-to-Sol launches.",
             "code_and_plan_sha256": baseline,
             "git_commit": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=REPO, text=True).strip()}
    save(state)
    active = {}
    stop_launching = False
    try:
        while state["pending"] or active:
            if not stop_launching:
                current = fingerprints(dirs)
                changed = sorted(p for p in baseline.keys() | current.keys() if baseline.get(p) != current.get(p))
                if changed or (HERE / "PAUSE_AFTER_ACTIVE").exists():
                    stop_launching = True
                    state.update(status="draining_for_review", pause_reason="Code/config change or operator pause", changed_paths=changed)
                    save(state)
            while not stop_launching and state["pending"] and len(active) < MAX_PARALLEL:
                run_id = state["pending"][0]
                console = HERE / f"{run_id}.console.log"
                handle = console.open("x")
                try:
                    process = subprocess.Popen([str(PYTHON), "-u", str(BATCH / "batch.py"), "run", run_id],
                                               cwd=REPO, stdout=handle, stderr=subprocess.STDOUT)
                finally:
                    handle.close()
                state["pending"].pop(0)
                active[run_id] = process
                state["active"][run_id] = {"pid": process.pid, "started_at": now(), "console": str(console)}
                save(state)
            if not active:
                break
            time.sleep(2)
            for run_id, process in list(active.items()):
                code = process.poll()
                if code is None:
                    continue
                started = state["active"].pop(run_id)
                del active[run_id]
                receipt_path = dirs[run_id] / "receipt.json"
                receipt = read(receipt_path) if receipt_path.exists() else None
                result = {"id": run_id, **started, "finished_at": now(), "returncode": code,
                          "receipt": str(receipt_path) if receipt else None}
                valid = code == 0 and receipt is not None
                if receipt:
                    summary = receipt["summary"]
                    outcomes = [json.loads(line) for line in (REPO / receipt["raw_path"] / "monitor.jsonl").read_text().splitlines() if line.strip()]
                    outcome = outcomes[0] if len(outcomes) == 1 else {}
                    result.update(calls=receipt["discussion_calls"], cost_usd=summary.get("total_cost_usd"),
                                  stop_reason=summary.get("stop_reason"), team_stop_reason=outcome.get("stop_reason"),
                                  raw_path=receipt["raw_path"])
                    valid = valid and not summary.get("cost_incomplete") and summary.get("stop_reason") == "completed"
                    valid = valid and outcome.get("stop_reason") in ("all_done", "turn_limit_reached")
                    valid = valid and receipt["discussion_calls"] <= 200
                if valid:
                    state["completed"].append(result)
                else:
                    state["failed"].append(result)
                    state.update(status="draining_for_review", pause_reason="Run failed or hit a nonstandard stop; queued runs remain unstarted")
                    stop_launching = True
                save(state)
        state.update(status="completed" if not state["pending"] and not state["failed"] else "needs_review", finished_at=now())
        save(state)
        return 0 if state["status"] == "completed" else 1
    except BaseException as exc:
        state.update(status="needs_review", error=type(exc).__name__ + ": " + str(exc), updated_at=now())
        save(state)
        # Already-started runs keep their own logs and caps. Never launch replacements here.
        raise


if __name__ == "__main__":
    raise SystemExit(main())
