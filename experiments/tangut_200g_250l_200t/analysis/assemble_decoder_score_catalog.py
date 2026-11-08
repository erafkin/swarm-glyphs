"""Consolidate existing score reports without scoring, model loading, or API calls.

The catalog combines the original comparison batch, the D14 follow-up, and the
published seed-2 context extension. Original reports and summaries stay read-only.
Run remake_decoder_scores_na.py afterward to derive the primary N/A results.
"""
from __future__ import annotations

import copy
import json
from pathlib import Path

from remake_decoder_scores_na import REPO, HERE, checked_path, sha, write_json

OUTPUT = HERE / "decoder_comparison_source_catalog/summary.json"
BASE = HERE / "decoder_comparison_scores/summary.json"
FOLLOWUP = HERE / "haiku_to_sol_full_task_scores/summary.json"
SEED2 = HERE / "sol_seed2_context_scores/summary.json"
EMBEDDING_KEYS = ("model_name", "resolved_revision", "packages", "max_seq_length")


def read(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def flatten_seed2(report: dict, path: Path) -> dict:
    stats, high, provenance = report["summary"], report["high_confidence"], report["decoder_provenance"]
    return {
        "cell_id": report["cell_id"], "encoder": "Sol", "seed": report["seed"],
        "decoder": "Sol", "decoder_model": provenance["model"], "condition": report["condition"],
        "status": "completed", "source_escaped": True, "protocol": report["protocol"],
        "cosine": stats["mean_per_line"]["cosine"], "high_confidence_cosine": high["mean_per_line"]["cosine"],
        **{key: stats[key] for key in ("eligible", "scorable_references", "valid_pairs", "missing_predictions",
                                      "unknown_only_predictions", "prediction_coverage")},
        "partial_unknown_predictions": sum(line["scorable"] and line["prediction_status"] == "partial_unknown"
                                           for line in report["lines"]),
        "high_confidence_references": high["scorable_references"],
        "high_confidence_reference_fraction": report["coverage"]["high_confidence_reference_fraction"],
        **{key: report["embedding_truncation"][key]
           for key in ("reference_lines_truncated", "hypothesis_lines_truncated")},
        "decoder_cost_usd": provenance["total_cost_usd"],
        "report_path": str(path.relative_to(REPO)), "report_sha256": sha(path), "reused_published_score": True,
    }


def assemble() -> dict:
    base, followup, seed2 = read(BASE), read(FOLLOWUP), read(SEED2)
    cells = copy.deepcopy(base["cells"])
    by_id = {cell["cell_id"]: cell for cell in cells}
    if len(by_id) != len(cells):
        raise ValueError("Duplicate cell ID in base summary")
    # A re-scored publication must not silently replace the source measurements
    # that the previously published N/A view used.
    overlap = []
    for cell in followup["cells"]:
        if cell["cell_id"] in by_id:
            current = by_id[cell["cell_id"]]
            if cell["status"] != current["status"] or cell.get("report_sha256") != current.get("report_sha256"):
                raise ValueError(f"Changed historical source report: {cell['cell_id']}")
            overlap.append(cell["cell_id"])
    d14 = [cell for cell in followup["cells"] if cell["cell_id"] == "D14"]
    if len(d14) != 1 or "D14" in by_id:
        raise ValueError("Expected exactly one new D14 follow-up")
    cells.extend(copy.deepcopy(d14))
    source_reports = {cell["cell_id"]: cell for cell in seed2["cells"]}
    for cell_id in ("R02_task_summary", "R02_wrong_task"):
        if cell_id in by_id:
            raise ValueError(f"Duplicate extension: {cell_id}")
        path = SEED2.parent / f"{cell_id}.json"
        report = read(path)
        if report["cell_id"] != cell_id or report["seed"] != 2 or report["run_id"] != "R02":
            raise ValueError(f"Unexpected source identity: {cell_id}")
        for key in ("inputs", "summary", "high_confidence", "embedding_model", "decoder_provenance"):
            if report[key] != source_reports[cell_id][key]:
                raise ValueError(f"Seed-2 report differs from its published summary: {cell_id}: {key}")
        cells.append(flatten_seed2(report, path))
    reports = []
    for cell in cells:
        if cell["status"] == "failed":
            continue
        path = checked_path(REPO, cell["report_path"])
        if sha(path) != cell["report_sha256"]:
            raise ValueError(f"Source report hash mismatch: {cell['cell_id']}")
        report = read(path)
        if report["cell_id"] != cell["cell_id"] or report.get("private_annotations_used") is not False:
            raise ValueError(f"Unexpected source identity or reference mode: {cell['cell_id']}")
        for key in EMBEDDING_KEYS:
            if report["embedding_model"][key] != base["embedding_model"][key]:
                raise ValueError(f"Embedding provenance mismatch: {cell['cell_id']}: {key}")
        reports.append(report)
    counts = {
        "completed": len(reports), "failed_unscored": sum(cell["status"] == "failed" for cell in cells),
        "scorable_pairs": sum(report["summary"]["scorable_references"] for report in reports),
        "high_confidence_pairs": sum(report["high_confidence"]["scorable_references"] for report in reports),
        "public_rows": sum(report["coverage"]["public_messages"] for report in reports),
        **{key: sum(report["coverage"][key] for report in reports)
           for key in ("task_status_excluded", "discarded_excluded")},
    }
    summary = copy.deepcopy(base)
    summary.update({
        "schema_version": 2, "cells": cells, "counts": counts,
        "source_catalog": {
            "inputs": [{"path": str(path.relative_to(REPO)), "sha256": sha(path)}
                       for path in (BASE, FOLLOWUP, SEED2)],
            "assembler": {"path": str(Path(__file__).relative_to(REPO)), "sha256": sha(Path(__file__))},
            "overlapping_followup_cells_verified": overlap,
            "embedding_reports_reused": True, "model_calls": 0, "api_calls": 0,
        },
        "comparability_notes": list(dict.fromkeys([
            *base["comparability_notes"], *followup["comparability_notes"], seed2["comparability_note"],
            "The two seed-2 context reports are reused from their published score files. Their existing full-task and no-task cells are included once, from the original comparison summary.",
        ])),
    })
    write_json(OUTPUT, summary)
    return summary


if __name__ == "__main__":
    print(json.dumps(assemble()["counts"], indent=2))
