"""Derive N/A-aware cosine reports from existing scores, without model/API calls.

The source summary and reports are read-only. Existing prediction_status values
are authoritative: missing/unknown answers have no primary cosine, while
partial_unknown guesses retain their original embeddings and scores.
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
DEFAULT_INPUT = HERE / "decoder_comparison_source_catalog/summary.json"
DEFAULT_OUTPUT = HERE / "decoder_comparison_scores_na"
PRIMARY_METRIC = "mean_cosine_over_valid_pairs"
ABSTENTIONS = {"missing", "unknown"}
METRIC = ("Mean paired MiniLM cosine over scorable references with a nonmissing, "
          "non-wholly-unknown prediction; missing/unknown answers are N/A and "
          "excluded from this mean. Report with valid-pair coverage. Not percent accuracy.")
PARTIAL_NOTE = ("Existing partial_unknown predictions remain scored and are counted separately. "
                "No new semantic classification is performed. Tentative guesses, unresolved "
                "aliases, and structure-only glosses may still receive cosine scores; "
                "nonzero similarity does not establish decipherment.")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, allow_nan=False, indent=2) + "\n", encoding="utf-8")


def write_csv(path: Path, rows: list[dict]) -> None:
    fields = list(dict.fromkeys(key for row in rows for key in row))
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({key: "N/A" if value is None else value for key, value in row.items()})


def checked_path(repo: Path, value: str | Path) -> Path:
    path = (repo / value).resolve()
    if not path.is_relative_to(repo):
        raise ValueError(f"Path escapes repository: {value}")
    return path


def summarize(lines: list[dict]) -> dict:
    """Keep reference eligibility separate from the primary cosine denominator."""
    eligible = [line for line in lines if not line.get("excluded_reason")]
    scorable = [line for line in eligible if line["scorable"]]
    valid = [line for line in scorable if line["prediction_status"] not in ABSTENTIONS]
    values = [line["scores"]["cosine"] for line in valid]
    if any(not isinstance(value, (float, int)) or not math.isfinite(value) for value in values):
        raise ValueError("Every valid pair must have an existing finite cosine")
    mean = math.fsum(values) / len(values) if values else None
    return {
        "eligible": len(eligible), "scorable_references": len(scorable),
        "unknown_references": len(eligible) - len(scorable),
        "valid_pairs": len(valid), "cosine_denominator": len(valid),
        "prediction_coverage": len(valid) / len(scorable) if scorable else None,
        "missing_predictions": sum(line["prediction_status"] == "missing" for line in scorable),
        "unknown_only_predictions": sum(line["prediction_status"] == "unknown" for line in scorable),
        "partial_unknown_predictions": sum(line["prediction_status"] == "partial_unknown" for line in scorable),
        "predictions_with_unknown_markers": sum(bool(line.get("decoder_contains_unknown")) for line in eligible),
        "uncertain_or_partial_references": sum(bool(line.get("reference_uncertain_or_partial")) for line in eligible),
        "mean_per_line": {"cosine": mean}, "valid_pair_mean": {"cosine": mean},
    }


def transform_report(source: dict, *, source_path: str, source_sha256: str) -> dict:
    """Copy a source report and change only its derived reporting semantics."""
    report = copy.deepcopy(source)
    report["schema_version"] = 2
    report["primary_metric"] = PRIMARY_METRIC
    report["method"] = METRIC
    report["derived_from"] = {"report_path": source_path, "report_sha256": source_sha256}
    report["supplementary_metrics"] = {
        "label": "Historical zero-inclusive scores (unchanged)",
        "summary": copy.deepcopy(source["summary"]),
        "high_confidence": copy.deepcopy(source["high_confidence"]),
        "metric_definition": copy.deepcopy(source.get("metric_definition", {})),
    }
    for line in report["lines"]:
        old_scores = copy.deepcopy(line.get("scores"))
        line["supplementary_metrics"] = {"zero_inclusive_scores": old_scores}
        included = bool(line["scorable"] and not line.get("excluded_reason")
                        and line["prediction_status"] not in ABSTENTIONS)
        line["included_in_primary_mean"] = included
        line["partial_unknown_prediction"] = line["prediction_status"] == "partial_unknown"
        line["primary_na_reason"] = (line.get("excluded_reason") or
                                     ("unscorable_reference" if not line["scorable"] else None) or
                                     (line["prediction_status"] if not included else None))
        if old_scores is not None:
            line["scores"] = {"cosine": old_scores["cosine"] if included else None}
        elif included:
            raise ValueError(f"Valid pair lacks source scores: {line['id']}")
    report["summary"] = summarize(report["lines"])
    report["high_confidence"] = summarize([
        line for line in report["lines"] if line["reference_confidence"] == "high"
    ])
    report["coverage"].update({
        key: report["summary"][key] for key in ("scorable_references", "valid_pairs", "prediction_coverage",
                                               "missing_predictions", "unknown_only_predictions", "partial_unknown_predictions")
    })
    report["metric_definition"] = {
        "cosine": METRIC,
        "missing_or_unknown_only": "N/A per line; excluded from primary cosine denominator",
        "coverage": "valid_pairs / scorable_references; unknown/missing counts cover scorable references only",
        "partial_unknown": PARTIAL_NOTE,
        "zero_inclusive_cosine": "Supplementary historical mean including missing/unknown as zero; unchanged",
        "unknown_reference": "Unscorable; excluded from both primary mean and coverage denominator",
    }
    return report


def remake(input_path: Path = DEFAULT_INPUT, output: Path = DEFAULT_OUTPUT, *, repo: Path = REPO) -> dict:
    """Rebuild all derived files from a v1 summary, including subsequently added cells."""
    repo = Path(repo).resolve()
    input_path, output = checked_path(repo, input_path), checked_path(repo, output)
    if input_path.is_relative_to(output):
        raise ValueError("Output must be separate from the historical summary directory")
    source = json.loads(input_path.read_text(encoding="utf-8"))
    if source.get("primary_metric") == PRIMARY_METRIC:
        raise ValueError("Input must be the historical zero-inclusive summary, not a derived N/A summary")
    reports, cells, seen = [], [], set()
    # Validate/read every source before writing anything.
    for original in source["cells"]:
        cell = copy.deepcopy(original)
        cell_id = str(cell["cell_id"])
        if cell_id in seen or not re.fullmatch(r"[A-Za-z0-9_-]+", cell_id):
            raise ValueError(f"Invalid or duplicate cell ID: {cell_id}")
        seen.add(cell_id)
        if cell["status"] == "failed":
            cells.append(cell)  # Failure metadata and unscored fields remain unchanged.
            continue
        if cell["status"] != "completed":
            raise ValueError(f"Unexpected cell status: {cell_id}")
        path = checked_path(repo, cell["report_path"])
        if path.is_relative_to(output):
            raise ValueError("Output must not contain historical source reports")
        digest = sha(path)
        if cell.get("report_sha256") and digest != cell["report_sha256"]:
            raise ValueError(f"Historical report hash mismatch: {cell_id}")
        report = transform_report(json.loads(path.read_text(encoding="utf-8")),
                                  source_path=str(path.relative_to(repo)), source_sha256=digest)
        report["cell_id"] = cell_id
        stats, high = report["summary"], report["high_confidence"]
        cell["source_report_path"] = cell["report_path"]
        cell["source_report_sha256"] = digest
        cell["zero_inclusive_cosine"] = cell["cosine"]
        cell["zero_inclusive_high_confidence_cosine"] = cell["high_confidence_cosine"]
        cell["cosine"] = stats["mean_per_line"]["cosine"]
        cell["high_confidence_cosine"] = high["mean_per_line"]["cosine"]
        for key in ("eligible", "scorable_references", "valid_pairs", "cosine_denominator", "prediction_coverage",
                    "missing_predictions", "unknown_only_predictions", "partial_unknown_predictions"):
            cell[key] = stats[key]
        cell["high_confidence_valid_pairs"] = high["valid_pairs"]
        cell["high_confidence_references"] = high["scorable_references"]
        cell["high_confidence_prediction_coverage"] = high["prediction_coverage"]
        cell["primary_metric"] = PRIMARY_METRIC
        cell["report_path"] = str((output / f"{cell_id}.json").relative_to(repo))
        reports.append(report)
        cells.append(cell)
    summary = copy.deepcopy(source)
    summary.update({
        "schema_version": 2, "primary_metric": PRIMARY_METRIC, "metric": METRIC, "cells": cells,
        "source_summary": {"path": str(input_path.relative_to(repo)), "sha256": sha(input_path)},
        "reporting_transform": {"path": str(Path(__file__).relative_to(REPO)), "sha256": sha(Path(__file__)),
                                "embeddings_reused": True, "model_calls": 0, "api_calls": 0},
        "source_comparability_notes": source.get("comparability_notes", []),
        "comparability_notes": [
            METRIC, PARTIAL_NOTE,
            "Coverage and high-confidence coverage must accompany valid-pair means; abstention can change the evaluated subset.",
            "All source text, prediction statuses, embeddings, references and original score files remain unchanged.",
            "The supplementary zero-inclusive means preserve the historical metric; do not compare them directly to the primary valid-pair means.",
            "References are public-only, reference-assisted drafts with differing uncertainty. This is one run per cell, not a balanced causal comparison.",
            "Failed cells remain failed and unscored; an all-unknown completed cell has zero coverage and an N/A mean.",
        ],
    })
    summary["counts"].update({
        "valid_pairs": sum(report["summary"]["valid_pairs"] for report in reports),
        "cosine_denominator": sum(report["summary"]["cosine_denominator"] for report in reports),
        "unknown_only_predictions": sum(report["summary"]["unknown_only_predictions"] for report in reports),
        "missing_predictions": sum(report["summary"]["missing_predictions"] for report in reports),
        "partial_unknown_predictions": sum(report["summary"]["partial_unknown_predictions"] for report in reports),
        "high_confidence_valid_pairs": sum(report["high_confidence"]["valid_pairs"] for report in reports),
    })
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
                "id", "sender", "source", "reference", "hypothesis_original", "hypothesis_normalized_raw",
                "hypothesis", "scoring_hypothesis", "reference_confidence", "prediction_status",
                "unknown_reason", "excluded_reason", "scorable", "included_in_primary_mean",
                "partial_unknown_prediction", "primary_na_reason")})
            row["cosine"] = (line["scores"] or {}).get("cosine")
            row["zero_inclusive_cosine"] = (line["supplementary_metrics"]["zero_inclusive_scores"] or {}).get("cosine")
            rows.append(row)
    write_json(output / "per_line.json", rows)
    write_csv(output / "per_line.csv", rows)
    (output / "README.md").write_text(readme(summary), encoding="utf-8")
    from render_decoder_comparisons import render
    render(summary, repo, output / "comparisons.html")
    return summary


def readme(summary: dict) -> str:
    def number(value):
        return "N/A" if value is None else f"{value:.3f}"
    rows = []
    for cell in summary["cells"]:
        if cell["status"] == "failed":
            rows.append(f"| {cell['cell_id']} | {cell['encoder']} → {cell['decoder']} | {cell['condition']} | Failed / unscored | N/A | N/A | N/A | N/A | N/A |")
            continue
        rows.append(f"| {cell['cell_id']} | {cell['encoder']} → {cell['decoder']} | {cell['condition']} | {number(cell['cosine'])} | "
                    f"{cell['valid_pairs']}/{cell['scorable_references']} | {cell['unknown_only_predictions']} / {cell['missing_predictions']} | "
                    f"{cell['partial_unknown_predictions']} | {number(cell['high_confidence_cosine'])} ({cell['high_confidence_valid_pairs']}/{cell['high_confidence_references']}) | {number(cell['zero_inclusive_cosine'])} |")
    counts = summary["counts"]
    return f"""# Decoder comparisons with unknown answers marked N/A

**Primary cosine excludes missing and wholly unknown answers.** Their per-line cosine is `null` in JSON and **N/A** in the viewer and CSV. A completed cell with no valid pairs has an N/A mean and zero coverage. Failed cells remain unscored.

- [Interactive comparisons](comparisons.html): original and normalized text, source glyphs, confidence, N/A reasons, coverage, and separately labelled historical means.
- [Summary CSV](summary.csv) / [JSON](summary.json): {counts['completed']} completed cells; failed attempts: {counts['failed_unscored']}.
- [Per-message CSV](per_line.csv) / [JSON](per_line.json): {counts['public_rows']:,} public-entry/cell rows with primary inclusion flags and supplementary historical cosine.
- Per-cell JSON files preserve source hashes, text, prediction statuses, and historical metrics under `supplementary_metrics`.

| Cell | Encoder → decoder | Context | Primary cosine | Coverage | Unknown / missing | Partial unknown | High-confidence cosine (coverage) | Supplementary zero-inclusive cosine |
|---|---|---|---:|---:|---:|---:|---:|---:|
{chr(10).join(rows)}

## Denominators and interpretation

The primary mean is the arithmetic mean of existing paired cosine values for scorable reference messages whose existing `prediction_status` is neither `missing` nor `unknown`. Coverage is **valid pairs / scorable references**. Task-status entries, discarded messages, and unscorable references remain excluded. High-confidence means and coverage apply the same rules within the high-confidence reference subset. No valid pairs means N/A, including when a source has no high-confidence references.

There are **{counts['valid_pairs']:,}/{counts['scorable_pairs']:,} valid/scorable message-cell pairs**, **{counts['unknown_only_predictions']} wholly unknown** and **{counts['missing_predictions']} missing** predictions. **{counts['partial_unknown_predictions']} partial-unknown predictions remain scored.** Repeated source messages across conditions are separate comparison pairs, not independent observations.

{PARTIAL_NOTE} In particular, D07's 109 partial-unknown entries largely describe structure; its nonzero score is not evidence of successful decipherment. D05 and D06 explicitly abstained on every scorable message, so their primary mean is N/A (0/109 coverage). D11's 19 unknown answers are excluded from the primary mean; the original zero-inclusive mean remains available for comparison.

Cosine measures resemblance between English texts, **not percent correct**. It can miss wrong numbers, negation, roles and actions. References remain reference-assisted drafts. The sources, reference uncertainty, decoder wording, task context, and budgets differ; one run per cell cannot isolate a model or context effect. A higher valid-pair mean can reflect a smaller answered subset, so always read coverage alongside it.

## Preservation and reproducibility

This is a reporting-only derivation. No model is loaded, no embeddings are recomputed, and no API calls are made. Historical score files, raw decoder outputs, extraction records, frozen references, and their existing classifications remain unchanged. The original means and other metrics are retained under explicitly labelled supplementary fields; their zero-inclusive denominator differs from the primary metric.

Source summary: `{summary['source_summary']['path']}` (SHA-256 `{summary['source_summary']['sha256']}`). Each derived report records its original path and hash. Historical comparison notes are preserved as `source_comparability_notes` in the summary.

The source catalog consolidates the original comparison summary, D14, and the two published seed-2 context extensions without changing their measurements or counting repeated cells twice. From the repository root, rebuild the catalog and primary results:

```sh
python experiments/tangut_200g_250l_200t/analysis/assemble_decoder_score_catalog.py
python experiments/tangut_200g_250l_200t/analysis/remake_decoder_scores_na.py --input {summary['source_summary']['path']} --output experiments/tangut_200g_250l_200t/analysis/decoder_comparison_scores_na
python -m unittest tests.test_decoder_scores_na
```

The transform validates recorded source-report hashes, rejects in-place output, and uses only Python's standard library. It does not alter the original scorer or historical results.
"""


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT, help="historical zero-inclusive summary JSON")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT, help="separate derived output directory")
    parser.add_argument("--repo", type=Path, default=REPO, help="root for repository-relative report paths")
    args = parser.parse_args()
    summary = remake(args.input, args.output, repo=args.repo)
    print(json.dumps(summary["counts"], indent=2))


if __name__ == "__main__":
    main()
