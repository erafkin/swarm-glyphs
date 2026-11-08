"""Derive abstention-as-zero results from archived raw cosines, using stdlib only.

No parsing, embeddings, model calls, or new semantic classification occurs here.
Historical abstention labels are checked against their original reports. A fresh
decoder with no historical report uses its explicitly archived parser labels.
"""
from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import json
import math
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
DEFAULT_INPUT = HERE / "decoder_comparison_scores_public_raw/summary.json"
DEFAULT_OUTPUT = HERE / "decoder_comparison_scores_zero"
RAW_METRIC = "mean_public_reference_raw_text_cosine"
PRIMARY_METRIC = "mean_public_reference_cosine_abstentions_zero"
ABSTENTIONS = {"missing", "unknown"}
STATUSES = ABSTENTIONS | {"present", "partial_unknown"}
METRIC = ("Arithmetic mean of paired MiniLM cosine over all scorable public agent-message "
          "references, assigning zero to missing or wholly unknown predictions. Partial-unknown "
          "predictions retain their archived raw cosine. Task status, discarded messages, and "
          "unscorable references are excluded. Not percent accuracy.")
CLASSIFICATION = ("Use the historical prediction status when an original classification exists; "
                  "verify it against the hashed historical report. Otherwise, only an explicitly "
                  "fresh decoder-config report may use its archived raw-parser status. "
                  "No new semantic classification is performed.")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def checked_path(repo: Path, value: str | Path) -> Path:
    repo = repo.resolve()
    path = (repo / value).resolve()
    if not path.is_relative_to(repo):
        raise ValueError(f"Path escapes repository: {value}")
    return path


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, allow_nan=False, indent=2) + "\n", encoding="utf-8")


def write_csv(path: Path, rows: list[dict]) -> None:
    fields = list(dict.fromkeys(key for row in rows for key in row))
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows({key: "N/A" if value is None else value for key, value in row.items()} for row in rows)


def index_lines(lines: list[dict]) -> dict:
    indexed = {line["id"]: line for line in lines}
    if len(indexed) != len(lines):
        raise ValueError("Duplicate message IDs")
    return indexed


def verify_classifications(source: dict, repo: Path) -> dict:
    """Verify the status source, and fail instead of guessing a missing label."""
    lineage = source["derived_from"]
    path = checked_path(repo, lineage["report_path"])
    if sha(path) != lineage["report_sha256"]:
        raise ValueError(f"Classification source hash mismatch: {path}")
    rows = index_lines(source["lines"])
    if lineage["kind"] == "historical_source_report":
        historical = index_lines(json.loads(path.read_text(encoding="utf-8"))["lines"])
        if rows.keys() != historical.keys():
            raise ValueError("Historical message ID alignment changed")
        for number, line in rows.items():
            old = historical[number]
            for key in ("sender", "source", "reference", "scorable"):
                if line.get(key) != old.get(key):
                    raise ValueError(f"Historical message identity changed at #{number}: {key}")
            if line.get("historical_prediction_status") != old.get("prediction_status"):
                raise ValueError(f"Historical prediction status changed at #{number}")
    elif lineage["kind"] == "fresh_decoder_config":
        if any(line.get("historical_prediction_status") is not None for line in rows.values()):
            raise ValueError("Fresh decoder report unexpectedly has historical labels")
    else:
        raise ValueError(f"Unsupported classification provenance: {lineage['kind']}")
    return copy.deepcopy(lineage)


def summarize(lines: list[dict]) -> dict:
    eligible = [line for line in lines if not line.get("excluded_reason")]
    scorable = [line for line in eligible if line["scorable"]]
    values = [line["scores"]["cosine"] for line in scorable]
    answered = [line for line in scorable if line["prediction_status"] not in ABSTENTIONS]
    return {
        "eligible": len(eligible), "scorable_references": len(scorable),
        "unknown_references": len(eligible) - len(scorable),
        "cosine_denominator": len(scorable), "scored_pairs": len(scorable),
        "provided_predictions": sum(bool(line.get("hypothesis")) for line in scorable),
        "valid_pairs": len(answered), "non_abstaining_pairs": len(answered),
        "prediction_coverage": len(answered) / len(scorable) if scorable else None,
        "missing_predictions": sum(line["prediction_status"] == "missing" for line in scorable),
        "unknown_only_predictions": sum(line["prediction_status"] == "unknown" for line in scorable),
        "partial_unknown_predictions": sum(line["prediction_status"] == "partial_unknown" for line in scorable),
        "zero_assigned_predictions": len(scorable) - len(answered),
        "historical_classifications": sum(line["classification_source"] == "historical_source_report" for line in scorable),
        "raw_parser_classifications": sum(line["classification_source"] == "fresh_decoder_config" for line in scorable),
        "mean_per_line": {"cosine": math.fsum(values) / len(values) if values else None},
    }


def transform_report(source: dict, *, source_path: str, source_sha256: str) -> dict:
    if source.get("primary_metric") != RAW_METRIC:
        raise ValueError("Input report must use the archived public raw metric")
    report = copy.deepcopy(source)
    kind = source["derived_from"]["kind"]
    if kind not in {"historical_source_report", "fresh_decoder_config"}:
        raise ValueError(f"Unsupported classification provenance: {kind}")
    index_lines(report["lines"])
    for line in report["lines"]:
        historical = line.get("historical_prediction_status")
        status = historical if kind == "historical_source_report" else line["prediction_status"]
        if status not in STATUSES:
            raise ValueError(f"Missing or unsupported classification at #{line['id']}: {status}")
        raw_cosine = (line.get("scores") or {}).get("cosine")
        included = bool(line["scorable"] and not line.get("excluded_reason"))
        if included and status not in ABSTENTIONS:
            if not isinstance(raw_cosine, (int, float)) or not math.isfinite(raw_cosine):
                raise ValueError(f"Non-abstaining answer lacks finite cosine at #{line['id']}")
        line.update({
            "raw_prediction_status": line["prediction_status"], "prediction_status": status,
            "classification_source": kind, "raw_text_cosine": raw_cosine,
            "included_in_primary_mean": included,
            "zero_assigned": included and status in ABSTENTIONS,
            "scores": {"cosine": (0.0 if status in ABSTENTIONS else raw_cosine) if included else None},
        })
    report.update({
        "schema_version": 4, "primary_metric": PRIMARY_METRIC, "method": METRIC,
        "derived_from": {"report_path": source_path, "report_sha256": source_sha256,
                         "kind": "archived_public_raw_report"},
        "classification_provenance": copy.deepcopy(source["derived_from"]),
        "raw_text_summary": copy.deepcopy(source["summary"]),
        "raw_text_high_confidence": copy.deepcopy(source["high_confidence"]),
        "metric_definition": {
            "cosine": METRIC, "classification": CLASSIFICATION,
            "denominator": "All scorable public agent-message references, including abstentions assigned zero.",
            "coverage": "Non-abstaining predictions / scorable references; separate from cosine denominator.",
            "partial_unknown": "Retain the archived raw cosine; a tentative/structural guess is not evidence of correct decipherment.",
        },
    })
    report["summary"] = summarize(report["lines"])
    report["high_confidence"] = summarize([line for line in report["lines"] if line["reference_confidence"] == "high"])
    report["coverage"].update({key: report["summary"][key] for key in (
        "scorable_references", "provided_predictions", "valid_pairs", "prediction_coverage",
        "missing_predictions", "unknown_only_predictions", "partial_unknown_predictions")})
    return report


def remake(input_path: Path = DEFAULT_INPUT, output: Path = DEFAULT_OUTPUT, *, repo: Path = REPO) -> dict:
    repo = Path(repo).resolve()
    input_path, output = checked_path(repo, input_path), checked_path(repo, output)
    if input_path.is_relative_to(output):
        raise ValueError("Output must be separate from archived input")
    source = json.loads(input_path.read_text(encoding="utf-8"))
    if source.get("primary_metric") != RAW_METRIC:
        raise ValueError("Input summary must use the archived public raw metric")
    reports, cells, seen = [], [], set()
    # Read and verify all input files before any output is written.
    for original in source["cells"]:
        cell = copy.deepcopy(original)
        identity = str(cell["cell_id"])
        if identity in seen or not re.fullmatch(r"[A-Za-z0-9_-]+", identity):
            raise ValueError(f"Invalid or duplicate cell ID: {identity}")
        seen.add(identity)
        if cell["status"] == "failed":
            cells.append(cell)
            continue
        if cell["status"] != "completed":
            raise ValueError(f"Unexpected cell status: {identity}")
        path = checked_path(repo, cell["report_path"])
        if path.is_relative_to(output):
            raise ValueError("Output must be separate from archived reports")
        digest = sha(path)
        if digest != cell["report_sha256"]:
            raise ValueError(f"Raw report hash mismatch: {identity}")
        raw = json.loads(path.read_text(encoding="utf-8"))
        lineage = verify_classifications(raw, repo)
        if checked_path(repo, lineage["report_path"]).is_relative_to(output):
            raise ValueError("Output must be separate from classification sources")
        report = transform_report(raw, source_path=cell["report_path"], source_sha256=digest)
        report["cell_id"] = identity
        stats, high = report["summary"], report["high_confidence"]
        cell.update({
            "source_report_path": cell["report_path"], "source_report_sha256": digest,
            "raw_text_cosine": cell["cosine"], "raw_text_high_confidence_cosine": cell["high_confidence_cosine"],
            "cosine": stats["mean_per_line"]["cosine"], "high_confidence_cosine": high["mean_per_line"]["cosine"],
            "primary_metric": PRIMARY_METRIC, "classification_source": lineage["kind"],
            "report_path": str((output / f"{identity}.json").relative_to(repo)),
            "high_confidence_cosine_denominator": high["cosine_denominator"],
            "high_confidence_valid_pairs": high["valid_pairs"],
        })
        cell.update({key: value for key, value in stats.items() if key != "mean_per_line"})
        if "embedded_pairs" in cell:
            cell["raw_embedded_pairs"] = cell.pop("embedded_pairs")
        reports.append(report)
        cells.append(cell)
    counts = {"completed": len(reports), "failed_unscored": len(cells) - len(reports)}
    for key in ("scorable_references", "cosine_denominator", "provided_predictions", "non_abstaining_pairs",
                "missing_predictions", "unknown_only_predictions", "partial_unknown_predictions", "zero_assigned_predictions"):
        counts[key] = sum(report["summary"][key] for report in reports)
    counts.update({key: source["counts"][key] for key in ("public_rows", "task_status_excluded", "discarded_excluded")})
    summary = {
        "schema_version": 4, "primary_metric": PRIMARY_METRIC, "metric": METRIC,
        "classification_policy": CLASSIFICATION, "mode": source["mode"], "private_annotations_used": False,
        "embedding_model": copy.deepcopy(source["embedding_model"]), "counts": counts, "cells": cells,
        "source_summary": {"path": str(input_path.relative_to(repo)), "sha256": sha(input_path)},
        "reporting_transform": {"path": str(Path(__file__).relative_to(REPO)), "sha256": sha(Path(__file__)),
                                "embeddings_reused": True, "model_calls": 0, "api_calls": 0},
        "comparability_notes": [
            METRIC, CLASSIFICATION,
            "All archived decoder text, references, raw cosines and original score files remain unchanged.",
            "Failed attempts remain failed and unscored; a completed all-abstention cell scores zero.",
            "References are public-only, reference-assisted drafts with differing uncertainty. Similarity is not accuracy.",
            "Only Sol self-decoding has five paired seeds; other comparisons have one run per cell. D14, D15, D16 and D12_retry1 are follow-ups.",
        ],
    }
    output.mkdir(parents=True, exist_ok=True)
    for report in reports:
        path = output / f"{report['cell_id']}.json"
        write_json(path, report)
        next(cell for cell in cells if cell["cell_id"] == report["cell_id"])["report_sha256"] = sha(path)
    write_json(output / "summary.json", summary)
    write_csv(output / "summary.csv", cells)
    rows = []
    for report in reports:
        for line in report["lines"]:
            row = {"cell_id": report["cell_id"], "condition": report["condition"]}
            row.update({key: line.get(key) for key in (
                "id", "sender", "source", "reference", "hypothesis_original", "hypothesis", "reference_confidence",
                "prediction_status", "raw_prediction_status", "historical_prediction_status", "historical_unknown_reason",
                "classification_source", "excluded_reason", "scorable", "included_in_primary_mean", "zero_assigned", "raw_text_cosine")})
            row["cosine"] = line["scores"]["cosine"]
            rows.append(row)
    write_json(output / "per_line.json", rows)
    write_csv(output / "per_line.csv", rows)
    (output / "README.md").write_text(readme(summary), encoding="utf-8")
    return summary


def readme(summary: dict) -> str:
    def number(value):
        return "N/A" if value is None else f"{value:.6f}"
    rows = []
    for cell in summary["cells"]:
        prefix = f"| {cell['cell_id']} | {cell['encoder']} → {cell['decoder']} | {cell['condition']} |"
        if cell["status"] == "failed":
            rows.append(prefix + " Failed / unscored | N/A | N/A | N/A | N/A |")
        else:
            rows.append(prefix + f" {number(cell['cosine'])} | {cell['cosine_denominator']} | "
                        f"{cell['unknown_only_predictions']} / {cell['missing_predictions']} | "
                        f"{cell['partial_unknown_predictions']} | {number(cell['high_confidence_cosine'])} |")
    return """# Decoder cosine with abstentions scored as zero

This is the recommended result table for the presentation. Missing and wholly unknown answers contribute zero; partially unknown answers keep their archived cosine. The denominator includes every scorable public agent-message reference, including abstentions. Cosine similarity is not percent accuracy.

- [Interactive report](comparisons.html): inspect all cells and their original message translations.
- [Summary CSV](summary.csv) / [JSON](summary.json)
- [Per-message CSV](per_line.csv) / [JSON](per_line.json)
- Original [raw-text scores](../decoder_comparison_scores_public_raw/README.md) and [N/A scores](../decoder_comparison_scores_na/README.md) remain available under their own conventions.

| Cell | Encoder → decoder | Context | Cosine | Denominator | Unknown / missing → zero | Partial unknown, scored | High-confidence cosine |
|---|---|---|---:|---:|---:|---:|---:|
""" + "\n".join(rows) + """

## What changed

Haiku self-decoding (D05/D06) is **0.000000** without and with full context: all 109 eligible answers in each cell are historical abstentions. D05 contains structural glosses under a global unknown-content declaration; D06 gives literal `unknown` answers. We retain this existing classification rather than counting structural descriptions as recovered meanings.

GPT-6.1 Sol decoding Haiku (D07/D14) stays **0.074602 / 0.230568**: neither cell has wholly unknown or missing eligible answers. Their 109 / 42 partially unknown predictions remain scored. DeepSeek self-decoding without context (D11) changes to **0.199981**, because 19 of 164 predictions are historical abstentions. All other completed raw means are unchanged. The completed full-context retry D12_retry1 stays **0.263136**; the original D12 failure stays unscored.

## Method and provenance

The standard-library derivation reuses archived per-message raw cosines. Historical prediction statuses are authoritative and checked against the original hashed reports. For D12_retry1, which has no historical classifier report, the explicitly archived raw-parser statuses are used (one partial-unknown prediction, no abstentions). No answers are reinterpreted, rewritten or re-embedded.

There are 2,129 scorable message/cell pairs, including 237 predictions assigned zero and no missing predictions. Task-status messages, discarded glyph messages and unscorable references stay excluded; high-confidence columns use only that reference subset and show N/A when it is empty. All completed reports have complete decoder-entry alignment. Non-abstaining coverage is reported separately from the cosine denominator in JSON/CSV. Partial-unknown structural guesses can still have positive similarity without correct decipherment.

Source summary, source reports, classification sources, script and output reports are SHA-256 linked. Frozen public references and embedding provenance remain attached to each report. Failed attempts stay separate from completed retries. Only Sol self-decoding has five paired seeds; the other cells are single runs, and references differ in confidence. These descriptive comparisons do not isolate causal model effects.

From the repository root, rebuild with Python 3.10+ without API calls or model dependencies:

```sh
python3 experiments/tangut_200g_250l_200t/analysis/remake_decoder_scores_zero.py
python3 experiments/tangut_200g_250l_200t/analysis/render_decoder_comparisons.py experiments/tangut_200g_250l_200t/analysis/decoder_comparison_scores_zero/summary.json experiments/tangut_200g_250l_200t/analysis/decoder_comparison_scores_zero/comparisons.html
python3 -m unittest discover -s tests -p 'test_decoder_scores_zero.py'
```
"""


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = remake(args.input, args.output)
    print(json.dumps(result["counts"], indent=2))
