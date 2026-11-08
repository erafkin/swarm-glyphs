"""Score the authorized D14 full-task follow-up and extend the comparison manifest.

This saves a separate source report without altering the original 20-cell scores.
Run remake_decoder_scores_na.py on the resulting summary for the primary N/A view.
"""

import json
from pathlib import Path

from decoder_comparison_scoring import REPO, HERE, checked_path, flattened, read, write
from src.core import translation_scoring as scoring

BASE = HERE.parent
OUTPUT = HERE / "haiku_to_sol_full_task_scores"


def score_followup():
    prior_path = HERE / "decoder_comparison_scores/summary.json"
    prior = read(prior_path)
    folder = BASE / "decoding/D14_haiku_to_sol_task_full"
    source_folder = BASE / "gameplay/R06_haiku_seed1"
    receipt_path = folder / "receipt.json"
    receipt, source_receipt = read(receipt_path), read(source_folder / "receipt.json")
    monitor, source = checked_path(receipt["raw_path"]), checked_path(source_receipt["raw_path"])
    summary = read(monitor / "monitor_summary.json")
    reference = source_folder / "english/translation.json"
    language, transcript, decoded = source / "swarmish.txt", source / "task_chatroom.jsonl", folder / "decoded.txt"
    _, references, transcript_hash = scoring.load_reference(reference, transcript, language)
    if (receipt["id"] != "D14" or receipt["status"] != "completed" or summary != receipt["summary"]
            or summary["conditions_completed"] != ["task_full"] or summary["conditions_requested"] != ["task_full"]
            or summary["n_agents"] != 8 or summary["model"] != "openai/gpt-6.1-sol"
            or summary["baseline"] is not False or summary["max_turns"] != 200
            or summary["minutes"] is not None or summary["max_cost_usd"] != 50):
        raise ValueError("D14 did not complete under the authorized protocol")
    for field in ("transcript_sha256", "source_transcript_sha256"):
        if summary[field] != transcript_hash:
            raise ValueError("D14 received a different public transcript")
    for name in ("monitor.jsonl", "monitor_summary.json", "monitor_inputs.json", "monitor_config.json"):
        if scoring._sha(monitor / name) != receipt["raw_sha256"][name]:
            raise ValueError(f"D14 archived input changed: {name}")
    outcomes = [json.loads(line) for line in (monitor / "monitor.jsonl").read_text().splitlines()]
    if len(outcomes) != 1 or decoded.read_text() != outcomes[0]["answer"] + "\n":
        raise ValueError("D14 decoded document differs from its final outcome")
    # The full-task briefing must be identical to the earlier Haiku full-task cell.
    old_receipt = read(BASE / "decoding/D06_haiku_to_haiku_task_full/receipt.json")
    old_inputs = read(checked_path(old_receipt["raw_path"]) / "monitor_inputs.json")
    inputs = read(monitor / "monitor_inputs.json")
    for key in ("system_prompt", "system_prompts", "prompt"):
        if inputs["requests"][0][key] != old_inputs["requests"][0][key]:
            raise ValueError(f"D14 full-task input differs from D06: {key}")
    translations = scoring.parse_translation(decoded, {r["id"] for r in references}, require_section=True)
    eligible = {r["id"] for r in references if r["sender"] != "task" and r["text"] != "⊘"}
    if not eligible <= translations.keys():
        raise ValueError("Missing D14 agent translation entries; audit extraction before scoring")
    model = scoring._sentence_model(scoring.ST_MODEL_REVISION)
    provenance = scoring.model_provenance(model, requested_revision=scoring.ST_MODEL_REVISION)
    for key in ("model_name", "resolved_revision", "packages", "max_seq_length"):
        if provenance[key] != prior["embedding_model"][key]:
            raise ValueError(f"Embedding provenance changed: {key}")
    report = scoring.score_reference_run(reference, transcript, decoded, language_path=language,
                                         models=True, embedder=model, embedding_provenance=provenance)
    report.update({"cell_id": "D14", "seed": 1, "condition": "task_full", "run_id": "R06",
                   "protocol": "200turn_no_clock_50usd", "reference": str(reference.relative_to(REPO)),
                   "task_dir": str(source.relative_to(REPO)), "language": str(language.relative_to(REPO)),
                   "decoder_document": str(decoded.relative_to(REPO)),
                   "decoder_provenance": {**summary, "record_path": str(receipt_path.relative_to(REPO)),
                                          "record_sha256": scoring._sha(receipt_path)},
                   "follow_up_note": "User requested after observing D07; not a preregistered cell. Same R06 public transcript, fresh Sol decoder team, full-task briefing identical to D06.",
                   "extraction_note": "Audited numbered translation section parsed by unchanged core scorer; no document-specific unknown overrides.",
                   "code_sha256": {str(p.relative_to(REPO)): scoring._sha(p) for p in (Path(__file__), Path(scoring.__file__))}})
    report_path = OUTPUT / "D14.json"
    write(report_path, report)
    cell = flattened(report, str(report_path.relative_to(REPO)), encoder="Haiku", decoder="Sol", escaped=False)
    combined = {**prior, "schema_version": 2, "prior_summary_path": str(prior_path.relative_to(REPO)),
                "prior_summary_sha256": scoring._sha(prior_path), "follow_up_report_sha256": scoring._sha(report_path),
                "cells": [*prior["cells"], cell], "counts": {**prior["counts"]},
                "comparability_notes": [*prior["comparability_notes"], report["follow_up_note"]]}
    counts = combined["counts"]
    counts["completed"] += 1
    counts["scorable_pairs"] += report["summary"]["scorable_references"]
    counts["high_confidence_pairs"] += report["high_confidence"]["scorable_references"]
    counts["public_rows"] += report["coverage"]["public_messages"]
    for key in ("task_status_excluded", "discarded_excluded"):
        counts[key] += report["coverage"][key]
    write(OUTPUT / "summary.json", combined)
    print(json.dumps({"cell": cell, "counts": counts}, indent=2))
    return combined


if __name__ == "__main__":
    score_followup()
