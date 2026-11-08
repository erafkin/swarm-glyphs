"""Score D05–D13 locally and combine with the 12 unique published Sol cells.

Uses the unchanged public-reference scorer and pinned MiniLM. No API calls.
Raw reports/references and existing scores are never overwritten. Extraction
decisions are recorded separately, including explicit unknown-content answers.
"""

import argparse
import csv
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO))
from src.core import translation_scoring as scoring
from decoder_translation_extraction import extract_translation

HERE = Path(__file__).resolve().parent
DEFAULT_MANIFEST = HERE / "decoder_comparison_runs.json"
DEFAULT_OUTPUT = HERE / "decoder_comparison_scores"


def read(path):
    return json.loads(path.read_text(encoding="utf-8"))


def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def checked_path(value, repo=REPO):
    path = (repo / value).resolve()
    if not path.is_relative_to(repo.resolve()):
        raise ValueError(f"Path outside repository: {value}")
    return path


def check_hashes(hashes, repo=REPO):
    for value, expected in hashes.items():
        if scoring._sha(checked_path(value, repo)) != expected:
            raise ValueError(f"Changed archived input: {value}")


def validate_prior(report, repo=REPO):
    """Verify the source files behind a reused score, not just its saved number."""
    _, rows, rendered_hash = scoring.load_reference(
        checked_path(report["reference"], repo),
        checked_path(report["task_dir"], repo) / "task_chatroom.jsonl",
        checked_path(report["language"], repo),
    )
    inputs = report["inputs"]
    pairs = {"reference_sha256": report["reference"],
             "public_transcript_sha256": report["task_dir"] + "/task_chatroom.jsonl",
             "language_sha256": report["language"],
             "decoder_document_sha256": report["monitor_dir"] + "/decoded_swarmish.txt"}
    check_hashes({path: inputs[key] for key, path in pairs.items()}, repo)
    if inputs["rendered_public_transcript_sha256"] != rendered_hash:
        raise ValueError("Prior score transcript mismatch")
    check_hashes({report["monitor_dir"] + "/" + name: value
                  for name, value in report["decoder_provenance"]["monitor_files_sha256"].items()}, repo)
    if [r["id"] for r in rows] != [r["id"] for r in report["lines"]]:
        raise ValueError("Prior per-line identity mismatch")
    return report


def preflight(manifest_path=DEFAULT_MANIFEST, repo=REPO):
    manifest = read(manifest_path)
    check_hashes(manifest["input_sha256"], repo)
    previous = [validate_prior(read(checked_path(p, repo)), repo) for p in manifest["prior_reports"]]
    if len(previous) != 12 or len({r["cell_id"] for r in previous}) != 12:
        raise ValueError("Expected 12 unique published Sol cells")
    if len(manifest["runs"]) != 9 or {r["cell_id"] for r in manifest["runs"]} != {f"D{i:02}" for i in range(5, 14)}:
        raise ValueError("Expected precisely D05–D13")
    cells = []
    for run in manifest["runs"]:
        source = manifest["sources"][run["source_id"]]
        _, references, rendered_hash = scoring.load_reference(
            checked_path(source["reference"], repo),
            checked_path(source["task_dir"], repo) / "task_chatroom.jsonl",
            checked_path(source["language"], repo),
        )
        record = read(checked_path(run["record"], repo))
        raw = checked_path(record["raw_path"], repo)
        summary = read(raw / "monitor_summary.json")
        if summary != record["summary"]:
            raise ValueError(f"Receipt/summary mismatch: {run['cell_id']}")
        if (summary["conditions_requested"] != [run["condition"]]
                or summary["baseline"] is not False or summary["n_agents"] != 8
                or summary["model"] != run["decoder_model"]
                or summary["minutes"] is not None or summary["max_turns"] != 200
                or summary["max_cost_usd"] != 50):
            raise ValueError(f"Unexpected protocol: {run['cell_id']}")
        if (Path(summary["source"]).name != Path(source["task_dir"]).name
                or any(summary[key] != rendered_hash for key in ("transcript_sha256", "source_transcript_sha256"))):
            raise ValueError(f"Source transcript mismatch: {run['cell_id']}")
        # Public outcome and configuration hashes; private scratchpads/calls are not read.
        for name in ("monitor_summary.json", "monitor_config.json", "monitor_inputs.json", "monitor.jsonl"):
            if scoring._sha(raw / name) != record["raw_sha256"][name]:
                raise ValueError(f"Changed monitor provenance: {run['cell_id']}/{name}")
        cell = {"run": run, "source": source, "record": record, "summary": summary}
        if run["status"] == "failed":
            if record["status"] != "failed" or summary["conditions_completed"]:
                raise ValueError("Failure record unexpectedly completed")
            cells.append(cell)
            continue
        if record["status"] != "completed" or summary["conditions_completed"] != [run["condition"]]:
            raise ValueError("Cannot score incomplete decoder")
        decoded = checked_path(run["decoded"], repo)
        outcomes = [json.loads(line) for line in (raw / "monitor.jsonl").read_text().splitlines() if line.strip()]
        if len(outcomes) != 1 or outcomes[0]["answer"] + "\n" != decoded.read_text():
            raise ValueError(f"Decoded document is not the saved final answer: {run['cell_id']}")
        extracted = extract_translation(decoded, run["cell_id"], {r["id"] for r in references})
        actual = {r["id"] for r in extracted["entries"]}
        required = {r["id"] for r in references if r["sender"] != "task" and r["text"].strip() != "⊘"}
        if not required <= actual:
            raise ValueError(f"Missing agent entries: {run['cell_id']}: {sorted(required - actual)}")
        cell["extraction"] = extracted
        cells.append(cell)
    return manifest, previous, cells


def flattened(report, path, *, encoder="Sol", decoder="Sol", escaped=True, reused=False):
    s, h = report["summary"], report["high_confidence"]
    p = report["decoder_provenance"]
    return {
        "cell_id": report["cell_id"], "encoder": encoder, "seed": report["seed"],
        "decoder": decoder, "decoder_model": p["model"], "condition": report["condition"],
        "status": "completed", "source_escaped": escaped, "protocol": report["protocol"],
        "cosine": s["mean_per_line"]["cosine"], "high_confidence_cosine": h["mean_per_line"]["cosine"],
        "eligible": s["eligible"], "scorable_references": s["scorable_references"],
        "valid_pairs": s["valid_pairs"], "missing_predictions": s["missing_predictions"],
        "unknown_only_predictions": s["unknown_only_predictions"],
        "partial_unknown_predictions": sum(r["scorable"] and r["prediction_status"] == "partial_unknown" for r in report["lines"]),
        "prediction_coverage": s["prediction_coverage"],
        "high_confidence_references": h["scorable_references"],
        "high_confidence_reference_fraction": report["coverage"]["high_confidence_reference_fraction"],
        "reference_lines_truncated": report["embedding_truncation"]["reference_lines_truncated"],
        "hypothesis_lines_truncated": report["embedding_truncation"]["hypothesis_lines_truncated"],
        "decoder_cost_usd": p["total_cost_usd"], "report_path": path,
        "report_sha256": scoring._sha(checked_path(path)), "reused_published_score": reused,
    }


def csv_file(path, rows):
    keys = list(dict.fromkeys(key for row in rows for key in row))
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=keys)
        writer.writeheader()
        writer.writerows(rows)


def run_batch(manifest_path=DEFAULT_MANIFEST, output=DEFAULT_OUTPUT):
    manifest, previous, cells = preflight(manifest_path)
    model = scoring._sentence_model(scoring.ST_MODEL_REVISION)
    provenance = scoring.model_provenance(model, requested_revision=scoring.ST_MODEL_REVISION)
    for old in previous:
        for key in ("model_name", "resolved_revision", "packages", "max_seq_length"):
            if old["embedding_model"][key] != provenance[key]:
                raise ValueError(f"Embedding provenance differs from published scores: {key}")
    output.mkdir(parents=True, exist_ok=True)
    records = [flattened(r, p, reused=True) for r, p in zip(previous, manifest["prior_reports"])]
    reports = list(previous)
    for cell in cells:
        run, source, record = (cell[k] for k in ("run", "source", "record"))
        if run["status"] == "failed":
            records.append({"cell_id": run["cell_id"], "encoder": source["family"], "seed": 1,
                            "decoder": run["decoder"], "decoder_model": run["decoder_model"],
                            "condition": run["condition"], "status": "failed", "source_escaped": source["escaped"],
                            "protocol": "200turn_no_clock_50usd", "cosine": None, "high_confidence_cosine": None,
                            "decoder_cost_usd": cell["summary"]["total_cost_usd"], "report_path": None,
                            "failure_record": run["record"], "reason": record["failure"]["reason"]})
            continue
        extracted = cell["extraction"]
        extract_path = output / "extracted" / f"{run['cell_id']}.json"
        extract_path.parent.mkdir(parents=True, exist_ok=True)
        canonical = extract_path.with_suffix(".txt")
        canonical.write_text("2. TRANSLATION\n" + "\n".join(
            f"[{r['id']}] {r['scoring_text']}" for r in extracted["entries"]) + "\n", encoding="utf-8")
        extracted.update({"decoder_path": run["decoded"], "decoder_sha256": scoring._sha(checked_path(run["decoded"])),
                          "canonical_document_sha256": scoring._sha(canonical)})
        write(extract_path, extracted)
        report = scoring.score_reference_run(
            checked_path(source["reference"]), checked_path(source["task_dir"]) / "task_chatroom.jsonl",
            canonical, language_path=checked_path(source["language"]), models=True,
            embedder=model, embedding_provenance=provenance,
        )
        by_id = {r["id"]: r for r in extracted["entries"]}
        for line in report["lines"]:
            entry = by_id.get(line["id"])
            if entry:
                line.update({"hypothesis_original": entry["original"], "hypothesis_normalized_raw": entry["normalized"],
                             "unknown_reason": entry["unknown_reason"]})
        # Distinguish immutable raw document identity from generated scoring input.
        report["inputs"]["canonical_document_sha256"] = report["inputs"]["decoder_document_sha256"]
        report["inputs"]["decoder_document_sha256"] = extracted["decoder_sha256"]
        report.update({"cell_id": run["cell_id"], "seed": 1, "condition": run["condition"],
                       "protocol": "200turn_no_clock_50usd", "run_id": run["source_id"],
                       "reference": source["reference"], "task_dir": source["task_dir"], "language": source["language"],
                       "extraction_path": str(extract_path.relative_to(REPO)),
                       "extraction_sha256": scoring._sha(extract_path), "decoder_document": run["decoded"],
                       "decoder_provenance": {**cell["summary"], "record_path": run["record"],
                                              "record_sha256": scoring._sha(checked_path(run["record"]))}})
        report["metric_definition"]["unknown_detection"] += "; explicit whole-content abstentions additionally normalized by the audited extraction adapter"
        path = output / f"{run['cell_id']}.json"
        write(path, report)
        reports.append(report)
        records.append(flattened(report, str(path.relative_to(REPO)), encoder=source["family"],
                                 decoder=run["decoder"], escaped=source["escaped"]))
        print(f"{run['cell_id']}: cosine={records[-1]['cosine']:.6f}; {records[-1]['valid_pairs']}/{records[-1]['eligible']} non-abstaining pairs", flush=True)
    summary = {
        "schema_version": 1, "mode": "reference_assisted_public_only", "private_annotations_used": False,
        "embedding_model": provenance, "manifest_sha256": scoring._sha(manifest_path),
        "code_sha256": {str(p.relative_to(REPO)): scoring._sha(p) for p in
                        (Path(__file__), Path(scoring.__file__), HERE / "decoder_translation_extraction.py")},
        "metric": "Mean paired MiniLM cosine over scorable agent messages; unknown/missing predictions contribute zero. Not percent accuracy.",
        "comparability_notes": manifest["comparability_notes"],
        "counts": {"completed": len(reports), "failed_unscored": sum(r["status"] == "failed" for r in records),
                   "scorable_pairs": sum(r["summary"]["scorable_references"] for r in reports),
                   "high_confidence_pairs": sum(r["high_confidence"]["scorable_references"] for r in reports),
                   "public_rows": sum(r["coverage"]["public_messages"] for r in reports),
                   "task_status_excluded": sum(r["coverage"]["task_status_excluded"] for r in reports),
                   "discarded_excluded": sum(r["coverage"]["discarded_excluded"] for r in reports)},
        "cells": records,
    }
    write(output / "summary.json", summary)
    csv_file(output / "summary.csv", records)
    rows = []
    for report in reports:
        for line in report["lines"]:
            row = {"cell_id": report["cell_id"], "condition": report["condition"]}
            row.update({key: line.get(key) for key in ("id", "sender", "source", "reference", "hypothesis_original",
                                                     "hypothesis_normalized_raw", "hypothesis", "scoring_hypothesis",
                                                     "reference_confidence", "prediction_status", "unknown_reason",
                                                     "excluded_reason", "scorable")})
            row["cosine"] = (line["scores"] or {}).get("cosine")
            rows.append(row)
    csv_file(output / "per_line.csv", rows)
    from render_decoder_comparisons import render
    render(summary, REPO, output / "comparisons.html")
    return summary


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="validate all archived inputs without loading embeddings")
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    if args.check:
        manifest, previous, cells = preflight(args.manifest)
        print(f"Validated {len(previous)} prior cells, {len(cells)} new outcomes; no embedding model loaded")
    else:
        result = run_batch(args.manifest, args.output)
        print(json.dumps(result["counts"], indent=2))
