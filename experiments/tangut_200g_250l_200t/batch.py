"""Explicit, single-run launcher and offline archive tools for this experiment batch.

Use ``status`` or ``validate`` without credentials. ``run ID --prepare-only`` writes
only .previews; only ``run ID`` makes API calls. Nothing launches a subsequent run.
"""
import argparse
import asyncio
from contextlib import contextmanager
from datetime import datetime, timezone
import fcntl
import hashlib
import json
import os
from pathlib import Path
import random
import re
import shutil
import subprocess
import sys

REPO = Path(__file__).resolve().parents[2]
BATCH = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

from src.core.potential_glyphs import sample_glyphs
from src.enc_dec.config import LanguageExperimentConfig
from experiments.tangut_200g_250l_200t.archive_paths import resolve_raw_path


def read(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def write(path, value):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def rows(path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()] if path.exists() else []


def require(condition, message):
    if not condition:
        raise ValueError(message)


def inside(path, base):
    path, base = Path(path).resolve(), Path(base).resolve()
    require(path.is_relative_to(base), f"Path escapes {base}: {path}")
    return path


def manifest_entry(root, run_id):
    entries = [r for r in read(root / "batch.json")["runs"] if r["id"] == run_id]
    require(len(entries) == 1, f"Unknown or duplicate run: {run_id}")
    return entries[0]


def run_info(root, run_id):
    folder = inside(root / manifest_entry(root, run_id)["path"], root)
    plan = read(folder / "plan.json")
    require(plan["id"] == run_id, "Plan ID differs from manifest")
    raw = read(folder / "config.json")
    require(not set(raw) - set(LanguageExperimentConfig.model_fields), "Unsupported configuration fields")
    return folder, plan, LanguageExperimentConfig.model_validate(raw)


def validate_manifest(root=BATCH):
    manifest = read(root / "batch.json")
    entries = manifest["runs"]
    expected = {f"{prefix}{i:02d}" for prefix, n in (("E", 8), ("T", 4), ("R", 8), ("D", 16)) for i in range(1, n + 1)}
    require(len(entries) == 36 and {r["id"] for r in entries} == expected,
            "Expected E01–E08, archived T01–T04, revised R01–R08 and D01–D16")
    declared_owners = {}
    gameplay_owners = {}
    for owner, details in manifest["owners"].items():
        require(owner in ("emma_krentz", "tom"), "Unknown declared owner")
        for run_id in details["encoding_ids"]:
            require(run_id not in declared_owners, f"Encoding assigned twice: {run_id}")
            declared_owners[run_id] = owner
        for run_id in details.get("gameplay_ids", []):
            require(run_id not in gameplay_owners, f"Gameplay assigned twice: {run_id}")
            gameplay_owners[run_id] = owner
    require(set(declared_owners) == {f"E{i:02d}" for i in range(1, 9)}, "Assign every encoder exactly once")
    require(set(gameplay_owners) == {f"R{i:02d}" for i in range(1, 9)}, "Assign every revised gameplay exactly once")
    win_condition = manifest["protocol"]["task_win_condition"]
    require(bool(win_condition.strip()), "Revised gameplay must specify the win condition")
    folders = set()
    for entry in entries:
        folder, plan, config = run_info(root, entry["id"])
        require(folder not in folders, "Run folders must be distinct")
        folders.add(folder)
        stage = {"E": "encoding", "T": "gameplay", "R": "gameplay", "D": "decoding"}[plan["id"][0]]
        archived = bool(entry.get("archived"))
        require(archived == plan["id"].startswith("T"), "Only historical T slots are archived")
        require(plan["stage"] == stage, "Incorrect run stage")
        allow_turn_limited = plan.get("allow_turn_limited_gameplay_source", False)
        require(type(allow_turn_limited) is bool, "Turn-limited source permission must be boolean")
        require(not allow_turn_limited or stage == "decoding", "Only decoders may allow turn-limited gameplay sources")
        require(plan["owner"] in ("emma_krentz", "tom"), "Unknown owner")
        require(config.task_kind == "escape_room" and not config.run_monitors, "Use standalone Storm Shelter phases")
        require(config.n_agents == 8 and (config.task_n_agents or 8) == 8 and config.monitor_n_agents == 8, "Every team must have eight agents")
        require(config.glyph_dictionary == "glyphs_tangut" and config.n_glyphs == 200, "Expected 200 Tangut glyphs")
        require(config.max_cost_usd == 50, "Expected $50 soft cap")
        effective_model = config.model_for(0, "monitor" if stage == "decoding" else "task" if stage == "gameplay" else "creation")
        require(effective_model == plan["model"] and config.seed == plan["config_seed"], "Model/seed differs from plan")
        require(config.agent_models is None and config.task_model in (None, config.model), "Use one planned model per run")
        require(stage == "decoding" or config.monitor_model in (None, config.model), "Unexpected monitor model override")
        original_folder = inside(root / entry["original_path"], root) if archived else folder
        require((REPO / config.log_dir).resolve() == (original_folder / "raw").resolve(), "log_dir must be this run's raw folder")
        if plan["id"].startswith("R"):
            require(plan["owner"] == gameplay_owners[plan["id"]], "Gameplay owner differs from batch assignment")
            require(config.task_win_condition == win_condition, "Revised gameplay win condition differs from protocol")
            if plan["owner"] == "tom":
                require(config.task_max_turns == 200, "Tom's revised gameplay requires 200 shared task turns")
        elif archived:
            require(config.task_win_condition == "", "Historical gameplay must retain its original prompt")
        require(config.language_max_turns == 200 and config.language_max_lines == 250 and config.monitor_max_turns == 200, "Expected 200-turn/250-line settings")
        require(config.language_minutes is None and config.monitor_minutes is None, "Encoding/decoding use turn limits, not time limits")
        source = plan.get("source_run_id")
        if stage == "encoding":
            require(plan["owner"] == declared_owners[plan["id"]], "Run owner differs from batch assignment")
            require(source is None and plan.get("condition") is None, "Encoding must have no source or condition")
        else:
            _, source_plan, source_config = run_info(root, source)
            require(source_plan["stage"] == ("encoding" if stage == "gameplay" else "gameplay"), "Incorrect source stage")
            require(config.seed == source_config.seed, "Source and destination must retain the glyph seed")
            if stage == "gameplay":
                require(config.model == source_config.model and plan.get("condition") is None, "Gameplay uses its encoder's model")
            else:
                require(source.startswith("R"), "Decoders must use revised gameplay, not the historical condition")
                require(plan["condition"] in ("no_task", "task_summary", "task_full", "wrong_task"), "Invalid decoder condition")
    return len(entries)


@contextmanager
def locked(folder):
    folder.mkdir(parents=True, exist_ok=True)
    with (folder / ".run.lock").open("a") as handle:
        try:
            fcntl.flock(handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as exc:
            raise ValueError("This run is already being operated on") from exc
        try:
            yield
        finally:
            fcntl.flock(handle, fcntl.LOCK_UN)


def dependency(root, plan):
    require(not manifest_entry(root, plan["source_run_id"]).get("archived"),
            "Archived gameplay cannot feed the revised decoder plan")
    folder, source_plan, _ = run_info(root, plan["source_run_id"])
    receipt = read(folder / "receipt.json")
    summary = receipt["summary"]
    require(receipt.get("status") == "completed", "Source has not completed collection")
    require(not summary.get("cost_incomplete"), "Source cost reporting is incomplete; review required")
    permitted = {"all_done", "turn_limit_reached", "time_limit"} if source_plan["stage"] == "encoding" else {"escaped"}
    if (source_plan["stage"] == "gameplay" and source_plan["id"].startswith("R")
            and plan.get("stage") == "decoding"
            and plan.get("allow_turn_limited_gameplay_source") is True):
        permitted.add("turn_limit_reached")
    require(receipt["stop_reason"] in permitted, f"Source stopped with {receipt['stop_reason']}; review required before reuse")
    for name, digest in receipt.get("handoff_sha256", {}).items():
        require(sha(folder / "handoff" / name) == digest, f"Frozen handoff changed: {name}")
    raw = resolve_raw_path(REPO, folder, receipt)
    for name, digest in receipt["raw_sha256"].items():
        require(sha(raw / name) == digest, f"Archived source changed: {name}")
    if source_plan["stage"] == "gameplay":
        require({"summary.json", "task_chatroom.jsonl"} <= receipt["raw_sha256"].keys(),
                "Gameplay source is missing summary/transcript integrity records")
        require(read(raw / "summary.json") == summary
                and summary.get("task_stop_reason") == receipt["stop_reason"],
                "Gameplay source outcome differs from its archived summary")
    return folder, receipt, raw


def gameplay_source_outcome(folder, receipt, plan):
    """Record outcome without adding private source information to decoder prompts."""
    return {
        "run_id": plan["source_run_id"],
        "stop_reason": receipt["stop_reason"],
        "escaped": receipt["summary"].get("escape_room", {}).get("escaped"),
        "receipt_sha256": sha(folder / "receipt.json"),
        "allow_turn_limited_gameplay_source": plan.get("allow_turn_limited_gameplay_source", False),
    }


def archive_files(source):
    require(source.is_dir() and not source.is_symlink(), "Source must be a regular directory")
    files = []
    for file in sorted(source.iterdir()):
        require(not file.is_symlink(), f"Refusing symlink: {file.name}")
        if file.is_file() and file.suffix in (".json", ".jsonl", ".txt"):
            require(not re.search(r"secret|credential|(^|[_.-])(?:env|key|token)([_.-]|$)", file.name, re.I), f"Refusing sensitive filename: {file.name}")
            require(not re.search(rb"sk-or-v1-[A-Za-z0-9_-]{12,}", file.read_bytes()), f"Credential detected in {file.name}")
            files.append(file)
    require(files, "No log files found")
    return files


def collect(root, run_id, source, language_file=None, reference_existing=False, already_locked=False):
    require(not manifest_entry(root, run_id).get("archived"), "Archived runs are read-only; use a revised R slot")
    folder, plan, config = run_info(root, run_id)
    if not already_locked:
        with locked(folder):
            return collect(root, run_id, source, language_file, reference_existing, True)
    require(not (folder / "receipt.json").exists(), "Receipt already exists; refusing overwrite")
    source = Path(source).absolute()
    files = archive_files(source)
    stage = plan["stage"]
    saved = read(source / ("monitor_config.json" if stage == "decoding" else "config.json"))
    saved_model = (saved.get("monitor_model") or saved["model"]) if stage == "decoding" else (saved.get("task_model") or saved["model"]) if stage == "gameplay" else saved["model"]
    require(saved_model == plan["model"] and saved.get("seed") == config.seed, "Imported model or seed differs from plan")
    require(saved["n_agents"] == 8 and saved.get("n_glyphs") == 200 and saved.get("glyph_dictionary") == "glyphs_tangut", "Imported team/glyph configuration differs")
    summary = read(source / ("monitor_summary.json" if stage == "decoding" else "summary.json"))
    calls = rows(source / ("monitor_calls.jsonl" if stage == "decoding" else "agent_calls.jsonl"))
    handoff, extra = {}, {}
    if stage == "encoding":
        require(summary.get("creation_only") is True, "Encoding import must be creation-only")
        creation = [r for r in calls if r.get("phase") == "creation"]
        require(len(creation) <= 200, "Encoding exceeds 200 discussion calls")
        deviations = {d["field"] for d in plan.get("approved_deviations", [])} if run_id == "E01" else set()
        for field, expected in (("language_max_turns", 200), ("language_max_lines", 250)):
            require(saved.get(field) == expected or field in deviations, f"Imported {field} differs from protocol")
        drafts = [r for r in creation if r.get("state_applied") and r.get("language_document", "").strip()]
        require(drafts, "No applied shared language draft found")
        draft = drafts[-1]["language_document"].strip() + "\n"
        require(len(draft.splitlines()) <= 250, "Shared language exceeds 250 lines")
        if language_file:
            require(Path(language_file).read_text(encoding="utf-8").strip() == draft.strip(), "Explicit language must match the last applied shared draft")
        glyphs = read(source / "glyphs.json")
        require(glyphs == sample_glyphs("glyphs_tangut", 200, random.Random(config.seed)), "Glyph sample differs from the planned seed")
        handoff = {name: (source / name).read_bytes() for name in ("glyphs.json", "config.json", "language_protocol.json")}
        handoff["swarmish.txt"] = draft.encode("utf-8")
        extra = {"shared_draft": {"source": "agent_calls.jsonl", "agent_id": drafts[-1].get("agent_id"), "turn": drafts[-1].get("turn"), "lines": len(draft.splitlines())}}
    elif stage == "gameplay":
        parent, _, _ = dependency(root, plan)
        require(summary.get("creation_stop_reason") == "provided_language", "Gameplay must use the frozen language")
        require(sha(source / "swarmish.txt") == sha(parent / "handoff/swarmish.txt"), "Gameplay language differs from frozen handoff")
        require(read(source / "glyphs.json") == read(parent / "handoff/glyphs.json"), "Gameplay glyphs differ from frozen handoff")
        if run_id.startswith("R"):
            require(saved.get("task_win_condition") == config.task_win_condition,
                    "Imported gameplay win condition differs from revised protocol")
            agents = read(source / "task_agents.json")
            require(len(agents) == 8 and {a["agent_id"] for a in agents} == {f"agent_{i}" for i in range(8)},
                    "Imported gameplay must have all eight task prompts")
            require(all(config.task_win_condition in a["system_prompt"] for a in agents),
                    "Revised win condition missing from an actual task prompt")
            fields = ("reasoning_effort", "max_tokens", "request_timeout_s", "task_minutes", "task_max_turns", "allow_spaces",
                      "task_feedback", "task_feedback_interval_s", "min_turn_interval_s", "max_cost_usd")
            observed = LanguageExperimentConfig.model_validate(saved)
            extra["settings_differences"] = [
                {"field": field, "planned": getattr(config, field), "observed": getattr(observed, field)}
                for field in fields if getattr(config, field) != getattr(observed, field)]
            extra["language_requirements_match_encoder"] = (
                sha(source / "language_protocol.json") == sha(parent / "handoff/language_protocol.json"))
        from src.enc_dec.monitor import read_public_messages
        messages = read_public_messages(source / "task_chatroom.jsonl", 8)
        require((source / "task_chatroom.jsonl").exists(), "Gameplay has no transcript")
        extra["translation"] = {"status": "pending", "source_transcript_sha256": sha(source / "task_chatroom.jsonl"), "language_sha256": sha(parent / "handoff/swarmish.txt"), "messages": [{**m, "english": None} for m in messages]}
    else:
        require(saved.get("monitor_n_agents") == 8 and saved.get("monitor_max_turns") == 200, "Decoder team/turn limits differ")
        require(len(calls) <= 200, "Decoder exceeds 200 discussion calls")
        outcomes = rows(source / "monitor.jsonl")
        require(len(outcomes) == 1 and outcomes[0]["condition"] == plan["condition"], "Expected exactly the planned decoder condition")
        parent, parent_receipt, parent_raw = dependency(root, plan)
        extra["source_gameplay"] = gameplay_source_outcome(parent, parent_receipt, plan)
        from src.enc_dec.monitor import prepare_monitor_inputs
        bundle = prepare_monitor_inputs(parent_raw, [plan["condition"]], config=config)
        require(summary["source_transcript_sha256"] == bundle["source_transcript_sha256"], "Decoder used a different transcript")
        inputs = read(source / "monitor_inputs.json")
        require(inputs.get("baseline") is False and summary.get("baseline") is False, "Masked-message baselines are not part of this plan")
        require(inputs.get("requests") == bundle["requests"], "Decoder briefing/prompts differ from the planned condition")
        request = bundle["requests"][0]
        require(all(outcomes[0].get(key) == request[key] for key in ("system_prompt", "prompt")), "Logged decoder prompts differ from prepared inputs")
        extra["decoded"] = outcomes[0]["answer"]
    own_raw = (folder / "raw").resolve()
    if source.resolve().is_relative_to(own_raw):
        destination = source.resolve()
    elif reference_existing:
        destination = inside(source, REPO)
        for file in files:
            result = subprocess.run(["git", "ls-files", "--error-unmatch", "--", str(file.resolve().relative_to(REPO))], cwd=REPO, capture_output=True)
            require(result.returncode == 0, f"Reference source must already be tracked: {file.name}")
    else:
        destination = folder / "raw" / source.name
        require(not destination.exists(), "Raw destination already exists; refusing overwrite")
    for name in handoff:
        require(not (folder / "handoff" / name).exists(), "Handoff already exists; refusing overwrite")
    for key, target in (("translation", "english/translation.json"), ("decoded", "decoded.txt")):
        require(key not in extra or not (folder / target).exists(), f"{target} already exists; refusing overwrite")
    if destination.resolve() != source.resolve():
        destination.mkdir(parents=True)
        for file in files:
            shutil.copyfile(file, destination / file.name)
    for name, content in handoff.items():
        (folder / "handoff").mkdir(exist_ok=True)
        (folder / "handoff" / name).write_bytes(content)
    if "translation" in extra:
        write(folder / "english/translation.json", extra.pop("translation"))
    if "decoded" in extra:
        (folder / "decoded.txt").write_text(extra.pop("decoded") + "\n", encoding="utf-8")
    stop = summary.get("stop_reason") or summary.get("task_stop_reason") or summary.get("creation_stop_reason")
    receipt = {"id": run_id, "status": "completed", "collected_at": datetime.now(timezone.utc).isoformat(), "raw_path": str(destination.resolve().relative_to(REPO)), "model": plan["model"], "owner": plan["owner"], "source_run_id": plan.get("source_run_id"), "discussion_calls": len(calls), "export_calls": len(rows(source / "language_document.jsonl")), "stop_reason": stop, "summary": summary, "approved_deviations": plan.get("approved_deviations", []), "raw_sha256": {f.name: sha(destination / f.name) for f in files}, "handoff_sha256": {name: sha(folder / "handoff" / name) for name in handoff}, **extra}
    if (folder / "execution.json").exists():
        receipt["execution"] = read(folder / "execution.json")
    write(folder / "receipt.json", receipt)
    return receipt


def provenance(folder):
    def git(*args):
        return subprocess.check_output(["git", *args], cwd=REPO)
    paths = sorted((REPO / "src").rglob("*.py")) + sorted((REPO / "src/enc_dec/prompts").glob("*"))
    return {"started_at": datetime.now(timezone.utc).isoformat(), "git_commit": git("rev-parse", "HEAD").decode().strip(), "dirty_diff_sha256": hashlib.sha256(git("diff", "HEAD", "--binary")).hexdigest(), "config_sha256": sha(folder / "config.json"), "code_and_prompt_sha256": {str(p.relative_to(REPO)): sha(p) for p in paths if p.is_file()}, "launcher_sha256": sha(__file__)}


def launch(root, run_id, prepare_only=False):
    require(not manifest_entry(root, run_id).get("archived"), "Archived runs are read-only; use a revised R slot")
    validate_manifest(root)
    folder, plan, config = run_info(root, run_id)
    with locked(root / ".previews" / run_id if prepare_only else folder):
        require(prepare_only or not (folder / "receipt.json").exists(), "Run already collected")
        require(prepare_only or not (folder / "execution.json").exists(), "Run already launched; collect existing outputs before deciding on a new run")
        config = config.model_copy(update={"log_dir": str(root / ".previews" / run_id) if prepare_only else str(folder / "raw")})
        stage = plan["stage"]
        execution_metadata = {}
        if stage == "decoding":
            from src.core.game_log import GameLogger
            from src.enc_dec.monitor import prepare_monitor_inputs, execute_monitor_inputs
            parent, parent_receipt, source = dependency(root, plan)
            execution_metadata["source_gameplay"] = gameplay_source_outcome(parent, parent_receipt, plan)
            bundle = prepare_monitor_inputs(source, [plan["condition"]], config=config)
            logger = GameLogger(config.log_dir, "round_3")
            logger.write_json("monitor_inputs", bundle)
            logger.write_json("monitor_config", config.model_dump())
            async def execute():
                from src.core.api_call import make_client
                client = make_client(config)
                try:
                    await execute_monitor_inputs(client, config, bundle, logger, config.max_cost_usd)
                finally:
                    await client.close()
        else:
            from src.enc_dec.run import LanguageExperiment
            parent = dependency(root, plan)[0] if stage == "gameplay" else None
            language = (parent / "handoff/swarmish.txt").read_text(encoding="utf-8") if parent else None
            experiment = LanguageExperiment(config, language, creation_only=stage == "encoding")
            logger = experiment.logger
            if parent:
                require(experiment.glyphs == read(parent / "handoff/glyphs.json"), "Generated glyphs differ from frozen sample")
                experiment.language_requirements = read(parent / "handoff/language_protocol.json")["requirements"]
            experiment.prepare()
            execute = experiment.run
        if prepare_only:
            print(f"Prepared without API calls: {logger.path}")
            return
        write(folder / "execution.json", {**provenance(folder), "raw_path": str(logger.path.relative_to(REPO)), **execution_metadata})
        asyncio.run(execute())
        collect(root, run_id, logger.path, already_locked=True)


def main():
    os.chdir(REPO)
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("status")
    sub.add_parser("validate")
    run = sub.add_parser("run")
    run.add_argument("id")
    run.add_argument("--prepare-only", action="store_true")
    archive = sub.add_parser("collect")
    archive.add_argument("id")
    archive.add_argument("source", type=Path)
    archive.add_argument("--language-file", type=Path)
    archive.add_argument("--reference-existing", action="store_true")
    args = parser.parse_args()
    try:
        if args.command == "validate":
            print(f"Validated {validate_manifest()} planned runs; no API calls.")
        elif args.command == "status":
            for entry in read(BATCH / "batch.json")["runs"]:
                folder, plan, _ = run_info(BATCH, entry["id"])
                state = "pending"
                if (folder / "receipt.json").exists():
                    receipt = read(folder / "receipt.json")
                    state = f"{receipt['status']} ({receipt.get('stop_reason')})"
                elif (folder / "execution.json").exists():
                    state = "launched; inspect raw logs"
                if entry.get("archived"):
                    state = "archived original prompt; " + state
                print(f"{plan['id']:3} {plan['owner']:12} {plan['stage']:8} {state}")
        elif args.command == "collect":
            receipt = collect(BATCH, args.id, args.source, args.language_file, args.reference_existing)
            print(f"Collected {args.id}: {receipt['raw_path']}")
        else:
            launch(BATCH, args.id, args.prepare_only)
    except (ValueError, FileNotFoundError) as exc:
        parser.exit(2, f"Error: {exc}\n")


if __name__ == "__main__":
    main()
