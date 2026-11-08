"""Score the ten archived Sol decoder cells against public-only English references.

No decoder calls are made. MiniLM is opt-in; the existing self-report/BERT API is
separate. Run from the repository root with --models after installing the optional
scoring dependencies. JSON reports are canonical; CSVs are inspection aids.
"""

import argparse
import csv
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))

from src.core import translation_scoring as scoring

DEFAULT_MANIFEST = Path(__file__).with_name("sol_translation_runs.json")
DEFAULT_OUTPUT = Path(__file__).with_name("sol_translation_scores")
PROTOCOLS = {
    "legacy_10min_10usd": {"minutes": 10.0, "max_turns": None, "max_cost_usd": 10.0},
    "200turn_no_clock_40usd": {"minutes": None, "max_turns": 200, "max_cost_usd": 40.0},
}


def _path(repo: Path, value: str) -> Path:
    path = (repo / value).resolve()
    if not path.is_relative_to(repo.resolve()):
        raise ValueError(f"Manifest path escapes repository: {value}")
    return path


def preflight(manifest_path: Path, repo: Path = REPO) -> tuple[dict, list[dict]]:
    """Validate all ten alignments and provenance before loading a model or writing."""
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    sources = manifest["sources"]
    if len(sources) != 5 or {s["seed"] for s in sources} != set(range(1, 6)):
        raise ValueError("Manifest must select the five distinct Sol seeds")
    by_id = {s["run_id"]: s for s in sources}
    if len(by_id) != len(sources):
        raise ValueError("Duplicate source run ID")
    expected = {(run_id, condition) for run_id in by_id for condition in ("task_full", "no_task")}
    runs = manifest["runs"]
    if len(runs) != 10 or {(r["source_run_id"], r["condition"]) for r in runs} != expected:
        raise ValueError("Manifest must select exactly one full-task and one no-task cell per seed")
    if len({r["cell_id"] for r in runs}) != len(runs):
        raise ValueError("Duplicate decoder cell ID")
    prepared = {}
    for source in sources:
        task = _path(repo, source["task_dir"])
        reference = _path(repo, source["reference"])
        language = _path(repo, source["language"])
        transcript = task / "task_chatroom.jsonl"
        _, rows, rendered_hash = scoring.load_reference(reference, transcript, language)
        prepared[source["run_id"]] = {
            "reference_path": reference, "transcript_path": transcript,
            "language_path": language, "expected_ids": {r["id"] for r in rows},
            "rendered_hash": rendered_hash, "source": source,
        }
    cells = []
    for run in runs:
        if not re.fullmatch(r"[A-Za-z0-9_-]+", run["cell_id"]):
            raise ValueError("Unsafe decoder cell ID")
        source = prepared[run["source_run_id"]]
        monitor = _path(repo, run["monitor_dir"])
        summary_path = monitor / "monitor_summary.json"
        summary = json.loads(summary_path.read_text(encoding="utf-8"))
        if any(summary.get(k) != [run["condition"]] for k in ("conditions_requested", "conditions_completed")):
            raise ValueError(f"Decoder context mismatch: {run['cell_id']}")
        if summary.get("baseline") is not False:
            raise ValueError(f"Masked/baseline decoder is not eligible: {run['cell_id']}")
        if Path(summary["source"]).name != source["transcript_path"].parent.name:
            raise ValueError(f"Decoder source run mismatch: {run['cell_id']}")
        for key in ("transcript_sha256", "source_transcript_sha256"):
            if summary.get(key) != source["rendered_hash"]:
                raise ValueError(f"Decoder public transcript hash mismatch: {run['cell_id']}")
        protocol = PROTOCOLS.get(run["protocol"])
        if protocol is None or any(summary.get(k) != v for k, v in protocol.items()):
            raise ValueError(f"Decoder budget/protocol mismatch: {run['cell_id']}")
        decoded = monitor / "decoded_swarmish.txt"
        scoring.parse_translation(decoded, source["expected_ids"], require_section=True)
        files = [summary_path, monitor / "monitor_config.json", monitor / "monitor_inputs.json"]
        cells.append({**source, "run": run, "decoded_path": decoded,
                      "decoder_provenance": {
                          "monitor_files_sha256": {p.name: scoring._sha(p) for p in files},
                          "model": summary.get("model"), "baseline": False,
                          "condition": run["condition"], "protocol": run["protocol"],
                          **protocol, "n_agents": summary.get("n_agents"),
                          "elapsed_s": summary.get("elapsed_s"),
                          "total_cost_usd": summary.get("total_cost_usd"),
                      }})
    return manifest, cells


def _flat_summary(report: dict) -> dict:
    row = {k: report[k] for k in ("cell_id", "seed", "family", "condition", "protocol")}
    for group in ("summary", "high_confidence"):
        data = report[group]
        prefix = "all" if group == "summary" else "high_confidence"
        for key in ("eligible", "scorable_references", "unknown_references", "missing_predictions",
                    "unknown_only_predictions", "predictions_with_unknown_markers", "valid_pairs", "prediction_coverage"):
            row[f"{prefix}_{key}"] = data[key]
        for key, value in data["mean_per_line"].items():
            row[f"{prefix}_{key}"] = value
        for key, value in data["valid_pair_mean"].items():
            row[f"{prefix}_valid_pair_{key}"] = value
        row[f"{prefix}_corpus_bleu"] = data["corpus_bleu"]
    row["high_confidence_reference_fraction"] = report["coverage"]["high_confidence_reference_fraction"]
    if report["embedding_truncation"]:
        row.update(report["embedding_truncation"])
    return row


def _write_csv(path: Path, rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def score_batch(manifest_path: str | Path = DEFAULT_MANIFEST,
                output_dir: str | Path = DEFAULT_OUTPUT, *, models: bool = False,
                embedder=None, model_revision: str = scoring.ST_MODEL_REVISION,
                repo: Path = REPO) -> dict:
    """Preflight all cells, load MiniLM once, then save full and summarized results."""
    manifest_path, output_dir = Path(manifest_path), Path(output_dir)
    manifest, cells = preflight(manifest_path, repo)
    if embedder is not None and not models:
        raise ValueError("An injected embedder requires models=True")
    provenance = None
    if models:
        if embedder is None:
            embedder = scoring._sentence_model(model_revision)
            provenance = scoring.model_provenance(embedder, requested_revision=model_revision)
        else:
            provenance = scoring.model_provenance(embedder)
            provenance["injected_model"] = True
            provenance["provenance_sha256"] = scoring._object_sha({k: v for k, v in provenance.items() if k != "provenance_sha256"})
    reports = []
    for cell in cells:
        report = scoring.score_reference_run(
            cell["reference_path"], cell["transcript_path"], cell["decoded_path"],
            language_path=cell["language_path"], models=models,
            embedder=embedder, embedding_provenance=provenance,
        )
        report.update({k: cell["run"][k] for k in ("cell_id", "condition", "protocol", "monitor_dir")})
        report.update({k: cell["source"][k] for k in ("run_id", "seed", "family", "reference", "task_dir", "language")})
        report["decoder_provenance"] = cell["decoder_provenance"]
        report["comparability_note"] = manifest["comparability_note"]
        reports.append(report)
    summary = {
        "schema_version": 1, "mode": "reference_assisted_public_only",
        "private_annotations_used": False, "decoder_archive_commit": manifest["decoder_archive_commit"],
        "comparability_note": manifest["comparability_note"],
        "manifest_sha256": scoring._sha(manifest_path),
        "code_sha256": {"translation_scoring.py": scoring._sha(Path(scoring.__file__)),
                        "sol_translation_scoring.py": scoring._sha(Path(__file__))},
        "embedding_model": provenance, "cells": [{k: v for k, v in r.items() if k != "lines"} for r in reports],
    }
    summary_rows = [_flat_summary(r) for r in reports]
    line_rows = []
    for report in reports:
        for line in report["lines"]:
            row = {k: report[k] for k in ("cell_id", "seed", "condition", "protocol")}
            row.update({k: line[k] for k in ("id", "sender", "source", "reference", "hypothesis", "hypothesis_original",
                                            "reference_confidence", "prediction_status", "scorable", "excluded_reason")})
            row.update({key: (line["scores"] or {}).get(key) for key in ("bleu", "rouge1", "rouge2", "rougeL", "cosine")})
            row.update({f"embedding_{key}": line.get("embedding_tokens", {}).get(key)
                        for key in ("reference", "hypothesis", "max_seq_length", "reference_truncated", "hypothesis_truncated")})
            line_rows.append(row)
    output_dir.mkdir(parents=True, exist_ok=True)
    for report in reports:
        (output_dir / f"{report['cell_id']}.json").write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (output_dir / "summary.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    _write_csv(output_dir / "summary.csv", summary_rows)
    _write_csv(output_dir / "per_line.csv", line_rows)
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--models", action="store_true", help="include pinned MiniLM cosine; loads one model, no BERT")
    modes.add_argument("--no-models", action="store_true", help="offline BLEU/ROUGE only (default)")
    parser.add_argument("--model-revision", default=scoring.ST_MODEL_REVISION)
    args = parser.parse_args()
    summary = score_batch(args.manifest, args.output_dir, models=args.models, model_revision=args.model_revision)
    print(f"Wrote {len(summary['cells'])} cells to {args.output_dir}")


if __name__ == "__main__":
    main()
