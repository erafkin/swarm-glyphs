"""Score original decoder wording against public-message references, offline.

Unlike the historical scorers, unknown answers are embedded as ordinary text.
Task feedback, discarded glyph messages, and unscorable references stay excluded.
The source catalog, original documents, reference files, and old scores are read-only.
An optional --extra-summary appends separately archived follow-up cells by unique ID.
"""
from __future__ import annotations

import argparse
import copy
import csv
import json
import math
import re
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
sys.path.insert(0, str(REPO))
from src.core import translation_scoring as scoring
from remake_decoder_scores_na import checked_path, sha, write_json

DEFAULT_INPUT = HERE / "decoder_comparison_source_catalog/summary.json"
DEFAULT_OUTPUT = HERE / "decoder_comparison_scores_public_raw"
PRIMARY_METRIC = "mean_public_reference_raw_text_cosine"
PROVENANCE_KEYS = ("model_name", "resolved_revision", "packages", "max_seq_length")
METRIC = ("Arithmetic mean of paired MiniLM cosine against public-message English references; "
          "decoder 'unknown' answers and structural glosses are embedded as ordinary text. "
          "Task status, discarded messages, and unscorable references are excluded. Not percent accuracy.")
CLEANING = ("Parse the original numbered translation section with the recorded core parser; "
            "remove message IDs, speaker/confidence prefixes and normalize whitespace. "
            "For a validated Msg/Agent/Meaning/Confidence Markdown table, retain the meaning cell "
            "literally and preserve the full original row for audit. "
            "Do not replace unknown declarations, remove their parenthetical text, rewrite glosses, "
            "expand aliases, infer missing entries, or use private intended meanings.")


def write_csv(path: Path, rows: list[dict]) -> None:
    fields = list(dict.fromkeys(key for row in rows for key in row))
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({key: "N/A" if value is None else value for key, value in row.items()})


def parse_decoder_document(path: Path, expected_senders: dict[int, str]) -> tuple[dict, dict, dict]:
    """Use the core parser, or narrowly validate an explicit translation table.

    A table's meaning cell is the prediction; agent and confidence columns are
    metadata. We never expand a preamble's default-unknown claim into absent IDs.
    Numbered/table mixtures are rejected for explicit alignment review.
    """
    text = scoring.read_text(path)
    heading = scoring._TRANSLATION_HEADING.search(text) or scoring._LOOSE_TRANSLATION.search(text)
    if heading is None:
        raise ValueError(f"No TRANSLATION section in {path}")
    section = text[heading.end():]
    end = scoring._LATER_HEADING.search(section) or scoring._LOOSE_LATER.search(section)
    if end:
        section = section[:end.start()]
    section_lines = section.splitlines()

    def cells(line):
        stripped = line.strip()
        if not stripped.startswith("|") or not stripped.endswith("|"):
            return None
        return [cell.strip() for cell in re.split(r"(?<!\\)\|", stripped[1:-1])]

    def header(line):
        values = cells(line)
        return (values is not None and len(values) == 4 and
                [value.casefold() for value in values] == ["msg", "agent", "meaning (likely)", "confidence"])

    if not any(header(line) for line in section_lines):
        if any(line.strip().startswith("|") for line in section_lines):
            raise ValueError(f"Unrecognized translation table format in {path}; audit before scoring")
        ids = set(expected_senders)
        decoded = scoring.parse_translation(path, ids, require_section=True)
        original = scoring.parse_translation(path, ids, require_section=True, strip_prefixes=False)
        metadata = {"format": "core_numbered_translation", "default_unknown_expanded": False}
        removed = []
        numbered_lines = {}
        for line in section_lines:
            match = scoring._MESSAGE_LINE.match(line)
            if match:
                numbered_lines[int(match.group(1) or match.group(2))] = line
        for number, meaning in decoded.items():
            prefix = re.match(r"^(task|agent_\d+):\s*", meaning)
            if prefix is None:
                continue
            sender = prefix.group(1)
            if sender != expected_senders[number]:
                raise ValueError(f"Numbered translation sender mismatch at #{number} in {path}")
            decoded[number] = meaning[prefix.end():]
            removed.append({"id": number, "sender": sender, "original_numbered_line": numbered_lines.get(number),
                            "original_body": original[number]})
        if removed:
            metadata["removed_bare_sender_prefixes"] = removed
        return decoded, original, metadata
    decoded, original, metadata = {}, {}, []
    index = 0
    while index < len(section_lines):
        line = section_lines[index]
        if not header(line):
            if (line.strip().startswith("|") or scoring._MESSAGE_LINE.match(line)
                    or scoring._LABELED_MESSAGE_LINE.match(line)):
                raise ValueError(f"Mixed or unrecognized translation rows in {path}; audit before scoring")
            index += 1
            continue
        if index + 1 == len(section_lines):
            raise ValueError(f"Missing Markdown table separator in {path}")
        separator = cells(section_lines[index + 1])
        if separator is None or len(separator) != 4 or not all(re.fullmatch(r":?-{3,}:?", item) for item in separator):
            raise ValueError(f"Invalid Markdown table separator in {path}")
        index += 2
        while index < len(section_lines) and section_lines[index].strip().startswith("|"):
            row_text = section_lines[index]
            row = cells(row_text)
            if row is None or len(row) != 4:
                raise ValueError(f"Malformed translation table row in {path}: {row_text}")
            number = re.fullmatch(r"(?:\[(\d+)\]|(\d+))", row[0])
            if number is None:
                raise ValueError(f"Invalid translation table message ID in {path}: {row[0]}")
            number = int(number.group(1) or number.group(2))
            if number not in expected_senders:
                raise ValueError(f"Unexpected translation message ID {number} in {path}")
            if number in decoded:
                raise ValueError(f"Duplicate translation message ID {number} in {path}")
            sender = row[1]
            if sender.startswith("[") and sender.endswith("]"):
                sender = sender[1:-1]
            if sender != expected_senders[number]:
                raise ValueError(f"Translation table sender mismatch at #{number} in {path}")
            decoded[number] = re.sub(r"\s+", " ", row[2]).strip()
            original[number] = row_text
            metadata.append({"id": number, "sender": sender, "confidence": row[3],
                             "original_table_line": row_text})
            index += 1
    if not decoded:
        raise ValueError(f"Translation table has no explicit message rows in {path}")
    return decoded, original, {"format": "markdown_msg_agent_meaning_confidence_table",
                               "default_unknown_expanded": False, "table_metadata": metadata}


def make_lines(references: list[dict], decoded: dict[int, str], original: dict[int, str],
               historical: dict[int, dict], *, allow_missing: bool = False) -> list[dict]:
    lines = []
    for row in references:
        number = row["id"]
        hypothesis = decoded.get(number, "")
        unknown, only_unknown = scoring._unknown_flags(hypothesis)
        ref_unknown, ref_only_unknown = scoring._unknown_flags(row["english"])
        excluded = ("task_status" if row["sender"] == "task" else
                    "discarded" if row["text"].strip() == "⊘" else None)
        scorable = excluded is None and row.get("confidence") != "unknown" and not ref_only_unknown
        # An absent row is not the same answer as the literal word 'unknown'.
        # Fail rather than silently change the denominator or invent its text.
        if scorable and not hypothesis and not allow_missing:
            raise ValueError(f"Missing eligible decoder translation #{number}; audit alignment before scoring")
        old = historical.get(number, {})
        if old and any(old.get(key) != expected for key, expected in (
                ("sender", row["sender"]), ("source", row["text"]),
                ("reference", row["english"]), ("scorable", scorable))):
            raise ValueError(f"Historical reference identity or eligibility changed at #{number}")
        status = "missing" if not hypothesis else "unknown" if only_unknown else "partial_unknown" if unknown else "present"
        lines.append({
            "id": number, "sender": row["sender"], "source": row["text"],
            "reference": row["english"], "reference_confidence": row.get("confidence"),
            "reference_ambiguities": row.get("ambiguities", row.get("ambiguity")),
            "reference_uncertain_or_partial": row.get("confidence") != "high" or ref_unknown,
            "hypothesis_original": original.get(number, ""), "hypothesis": hypothesis,
            "scoring_hypothesis": hypothesis, "prediction_status": status,
            "decoder_contains_unknown": unknown, "excluded_reason": excluded,
            "scorable": scorable, "included_in_primary_mean": scorable and bool(hypothesis), "scores": None,
            "historical_prediction_status": old.get("prediction_status"),
            "historical_unknown_reason": old.get("unknown_reason"),
        })
    return lines


def preflight(input_paths: list[Path], output: Path, repo: Path = REPO) -> tuple[list[dict], list[dict]]:
    """Verify hashes and message identity before loading the embedding model."""
    repo = repo.resolve()
    output = checked_path(repo, output)
    sources, prepared, seen = [], [], set()
    for source_path in input_paths:
        source_path = checked_path(repo, source_path)
        if source_path.is_relative_to(output):
            raise ValueError("Output must be separate from source summaries and reports")
        source = json.loads(source_path.read_text(encoding="utf-8"))
        sources.append({"path": str(source_path.relative_to(repo)), "sha256": sha(source_path)})
        for cell in source["cells"]:
            identity = cell["cell_id"]
            if identity in seen or not re.fullmatch(r"[A-Za-z0-9_-]+", identity):
                raise ValueError(f"Invalid or duplicate cell ID: {identity}")
            seen.add(identity)
            if cell["status"] == "failed":
                prepared.append({"cell": copy.deepcopy(cell)})
                continue
            if cell["status"] != "completed":
                raise ValueError(f"Unexpected cell status: {identity}")
            report_path = checked_path(repo, cell["report_path"])
            if report_path.is_relative_to(output):
                raise ValueError("Output must be separate from source summaries and reports")
            if sha(report_path) != cell["report_sha256"]:
                raise ValueError(f"Historical source report hash changed: {identity}")
            report = json.loads(report_path.read_text(encoding="utf-8"))
            if report["cell_id"] != identity or report.get("private_annotations_used") is not False:
                raise ValueError(f"Invalid public-reference source report: {identity}")
            reference = checked_path(repo, report["reference"])
            transcript = checked_path(repo, report["task_dir"]) / "task_chatroom.jsonl"
            language = checked_path(repo, report["language"])
            decoder = (checked_path(repo, report["decoder_document"]) if report.get("decoder_document") else
                       scoring._decoded_document(checked_path(repo, report["monitor_dir"])))
            if decoder is None:
                raise ValueError(f"No original decoder document: {identity}")
            if any(path.is_relative_to(output) for path in (reference, transcript, language, decoder)):
                raise ValueError("Output must not contain original input files")
            inputs = report["inputs"]
            for path, key in ((reference, "reference_sha256"), (transcript, "public_transcript_sha256"),
                              (language, "language_sha256"), (decoder, "decoder_document_sha256")):
                if sha(path) != inputs[key]:
                    raise ValueError(f"Archived input changed: {identity}: {key}")
            document, rows, rendered_hash = scoring.load_reference(reference, transcript, language)
            if rendered_hash != inputs["rendered_public_transcript_sha256"]:
                raise ValueError(f"Rendered transcript mismatch: {identity}")
            if [row["id"] for row in rows] != [row["id"] for row in report["lines"]]:
                raise ValueError(f"Historical public-message alignment differs: {identity}")
            decoded, original, extraction = parse_decoder_document(decoder, {row["id"]: row["sender"] for row in rows})
            lines = make_lines(rows, decoded, original, {row["id"]: row for row in report["lines"]})
            prepared.append({"cell": copy.deepcopy(cell), "source_report": report, "lines": lines,
                             "reference_status": document["status"], "decoder_document": str(decoder.relative_to(repo)),
                             "decoder_message_ids": len(decoded), "extraction": extraction})
    return sources, prepared


def prepare_extra(config_path: Path, output: Path, repo: Path = REPO) -> tuple[dict, dict]:
    """Validate a fresh archived decoder without creating historical score files."""
    config_path = checked_path(repo, config_path)
    if config_path.is_relative_to(output):
        raise ValueError("Output must be separate from follow-up configs")
    config = json.loads(config_path.read_text(encoding="utf-8"))
    cell_keys = ("cell_id", "encoder", "seed", "decoder", "decoder_model", "condition", "source_escaped", "protocol")
    cell = {key: config[key] for key in cell_keys}
    if not re.fullmatch(r"[A-Za-z0-9_-]+", cell["cell_id"]):
        raise ValueError("Invalid follow-up cell ID")
    receipt_path = checked_path(repo, config["receipt"])
    receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
    monitor = checked_path(repo, receipt["raw_path"])
    summary = json.loads((monitor / "monitor_summary.json").read_text(encoding="utf-8"))
    if (receipt["status"] != "completed" or summary != receipt["summary"]
            or summary["conditions_completed"] != [cell["condition"]]
            or summary["conditions_requested"] != [cell["condition"]]
            or summary["model"] != cell["decoder_model"] or summary["n_agents"] != 8
            or summary["baseline"] is not False):
        raise ValueError("Follow-up receipt did not complete the configured decoder condition")
    for name in ("monitor.jsonl", "monitor_summary.json", "monitor_config.json", "monitor_inputs.json"):
        if sha(monitor / name) != receipt["raw_sha256"][name]:
            raise ValueError(f"Changed follow-up archive: {name}")
    reference = checked_path(repo, config["reference"])
    task = checked_path(repo, config["task_dir"])
    language = checked_path(repo, config["language"])
    decoder = checked_path(repo, config["decoder_document"])
    if any(path.is_relative_to(output) for path in (receipt_path, monitor, reference, task, language, decoder)):
        raise ValueError("Output must not contain follow-up inputs")
    document, rows, rendered_hash = scoring.load_reference(reference, task / "task_chatroom.jsonl", language)
    if any(summary[key] != rendered_hash for key in ("transcript_sha256", "source_transcript_sha256")):
        raise ValueError("Follow-up decoder received a different public transcript")
    outcomes = [json.loads(line) for line in (monitor / "monitor.jsonl").read_text(encoding="utf-8").splitlines()]
    if len(outcomes) != 1 or decoder.read_text(encoding="utf-8") != outcomes[0]["answer"] + "\n":
        raise ValueError("Follow-up decoded document is not the archived final answer")
    decoded, original, extraction = parse_decoder_document(decoder, {row["id"]: row["sender"] for row in rows})
    lines = make_lines(rows, decoded, original, {}, allow_missing=config.get("allow_missing", True))
    metadata = {key: config[key] for key in ("cell_id", "condition", "protocol", "seed", "reference", "task_dir", "language")}
    metadata.update({
        "run_id": config.get("run_id", task.parent.parent.name.split("_")[0]),
        "inputs": {"reference_sha256": sha(reference), "public_transcript_sha256": sha(task / "task_chatroom.jsonl"),
                   "rendered_public_transcript_sha256": rendered_hash, "language_sha256": sha(language),
                   "decoder_document_sha256": sha(decoder)},
        "decoder_provenance": {**summary, "record_path": str(receipt_path.relative_to(repo)), "record_sha256": sha(receipt_path)},
    })
    cell.update({"status": "completed", "report_path": str(config_path.relative_to(repo)),
                 "report_sha256": sha(config_path), "decoder_cost_usd": summary["total_cost_usd"]})
    return ({"path": str(config_path.relative_to(repo)), "sha256": sha(config_path), "kind": "fresh_decoder_config"},
            {"cell": cell, "source_report": metadata, "source_kind": "fresh_decoder_config", "lines": lines,
             "reference_status": document["status"], "decoder_document": str(decoder.relative_to(repo)),
             "decoder_message_ids": len(decoded), "extraction": extraction})


def summarize(lines: list[dict]) -> dict:
    eligible = [row for row in lines if not row["excluded_reason"]]
    scorable = [row for row in eligible if row["scorable"]]
    pairs = [row for row in scorable if row["included_in_primary_mean"]]
    values = [row["scores"]["cosine"] for row in pairs]
    if any(not math.isfinite(value) for value in values):
        raise ValueError("Every scored pair must have finite cosine")
    non_abstaining = [row for row in pairs if row["prediction_status"] not in {"missing", "unknown"}]
    return {
        "eligible": len(eligible), "scorable_references": len(scorable), "cosine_denominator": len(pairs),
        "embedded_pairs": len(pairs), "unknown_references": len(eligible) - len(scorable),
        "valid_pairs": len(pairs), "prediction_coverage": len(pairs) / len(scorable) if scorable else None,
        "non_abstaining_pairs": len(non_abstaining),
        "missing_predictions": sum(row["prediction_status"] == "missing" for row in scorable),
        "unknown_only_predictions": sum(row["prediction_status"] == "unknown" for row in pairs),
        "partial_unknown_predictions": sum(row["prediction_status"] == "partial_unknown" for row in pairs),
        "historical_unknown_classifications": sum(row["historical_prediction_status"] == "unknown" for row in pairs),
        "predictions_with_unknown_markers": sum(row["decoder_contains_unknown"] for row in pairs),
        "uncertain_or_partial_references": sum(row["reference_uncertain_or_partial"] for row in eligible),
        "mean_per_line": {"cosine": math.fsum(values) / len(values) if values else None},
    }


def score(input_paths: list[Path] | None = None, output: Path = DEFAULT_OUTPUT,
          *, repo: Path = REPO, extra_decoder_configs: list[Path] | None = None,
          embedder=None, embedding_provenance: dict | None = None) -> dict:
    repo = repo.resolve()
    output = checked_path(repo, output)
    sources, prepared = preflight(input_paths or [DEFAULT_INPUT], output, repo)
    for config_path in extra_decoder_configs or []:
        source, item = prepare_extra(config_path, output, repo)
        if item["cell"]["cell_id"] in {old["cell"]["cell_id"] for old in prepared}:
            raise ValueError(f"Duplicate cell ID: {item['cell']['cell_id']}")
        sources.append(source)
        prepared.append(item)
    if embedder is None:
        embedder = scoring._sentence_model(scoring.ST_MODEL_REVISION)
        embedder.to("cpu")
        embedding_provenance = scoring.model_provenance(embedder, requested_revision=scoring.ST_MODEL_REVISION)
    if embedding_provenance is None:
        raise ValueError("Explicit embedder requires recorded provenance")
    for item in prepared:
        if "source_report" in item and item.get("source_kind") != "fresh_decoder_config":
            for key in PROVENANCE_KEYS:
                if item["source_report"]["embedding_model"][key] != embedding_provenance[key]:
                    raise ValueError(f"Embedding provenance differs for {item['cell']['cell_id']}: {key}")
    texts = sorted({value for item in prepared for row in item.get("lines", []) if row["included_in_primary_mean"]
                    for value in (row["reference"], row["hypothesis"])})
    encoded = embedder.encode(texts, normalize_embeddings=True, batch_size=64, show_progress_bar=False)
    if len(encoded) != len(texts):
        raise ValueError("Unexpected number of embedding vectors")
    vectors = dict(zip(texts, encoded))
    limit = embedder.max_seq_length
    lengths = {text: len(ids) for text, ids in zip(texts, embedder.tokenizer(
        texts, add_special_tokens=True, truncation=False, padding=False)["input_ids"])}
    reports, cells = [], []
    for item in prepared:
        cell = item["cell"]
        if cell["status"] == "failed":
            cells.append(cell)
            continue
        old, lines = item["source_report"], item["lines"]
        for row in lines:
            if row["included_in_primary_mean"]:
                left, right = row["reference"], row["hypothesis"]
                row["scores"] = {"cosine": scoring._cosine(vectors[left], vectors[right])}
                row["embedding_tokens"] = {"reference": lengths[left], "hypothesis": lengths[right],
                                           "max_seq_length": limit, "reference_truncated": lengths[left] > limit,
                                           "hypothesis_truncated": lengths[right] > limit}
        stats = summarize(lines)
        high = summarize([row for row in lines if row["reference_confidence"] == "high"])
        eligible = [row for row in lines if not row["excluded_reason"]]
        coverage = {"public_messages": len(lines), "decoder_message_ids": item["decoder_message_ids"],
                    "task_status_excluded": sum(row["excluded_reason"] == "task_status" for row in lines),
                    "discarded_excluded": sum(row["excluded_reason"] == "discarded" for row in lines),
                    "high_confidence_reference_fraction": high["eligible"] / len(eligible) if eligible else None,
                    "reference_confidence_counts": dict(Counter(row["reference_confidence"] for row in eligible))}
        report = {key: copy.deepcopy(old[key]) for key in (
            "cell_id", "condition", "protocol", "run_id", "seed", "reference", "task_dir", "language", "decoder_provenance")}
        report.update({
            "schema_version": 1, "mode": "reference_assisted_public_only", "private_annotations_used": False,
            "primary_metric": PRIMARY_METRIC, "method": METRIC, "text_normalization": CLEANING,
            "extraction": item["extraction"],
            "reference_status": item["reference_status"], "decoder_document": item["decoder_document"],
            "inputs": {key: value for key, value in old["inputs"].items() if key != "canonical_document_sha256"},
            "derived_from": {"report_path": cell["report_path"], "report_sha256": cell["report_sha256"],
                             "kind": item.get("source_kind", "historical_source_report")},
            "embedding_model": embedding_provenance, "summary": stats, "high_confidence": high,
            "coverage": coverage, "lines": lines,
            "embedding_truncation": {
                "measured_pairs": stats["embedded_pairs"],
                "reference_lines_truncated": sum(row.get("embedding_tokens", {}).get("reference_truncated", False) for row in lines),
                "hypothesis_lines_truncated": sum(row.get("embedding_tokens", {}).get("hypothesis_truncated", False) for row in lines)},
            "metric_definition": {"cosine": METRIC, "unknown_detection": "Lexical flags are descriptive only; do not alter text or score inclusion.",
                                  "missing": "Historical cells must have complete alignment. Fresh follow-ups may retain missing entries as unscored with coverage shown; no invented text.",
                                  "historical_classifications": "Retained for audit only; do not alter text or score inclusion."},
        })
        cell.update({"primary_metric": PRIMARY_METRIC, "cosine": stats["mean_per_line"]["cosine"],
                     "high_confidence_cosine": high["mean_per_line"]["cosine"],
                     "high_confidence_valid_pairs": high["embedded_pairs"],
                     "high_confidence_references": high["scorable_references"],
                     "source_report_path": cell["report_path"], "source_report_sha256": cell["report_sha256"],
                     "report_path": str((output / f"{cell['cell_id']}.json").relative_to(repo)),
                     "reused_published_score": False})
        cell.update({key: value for key, value in stats.items() if key != "mean_per_line"})
        cell.update({key: report["embedding_truncation"][key]
                     for key in ("reference_lines_truncated", "hypothesis_lines_truncated")})
        reports.append(report)
        cells.append(cell)
    # Everything above is validated and computed before any output files change.
    output.mkdir(parents=True, exist_ok=True)
    for report in reports:
        path = output / f"{report['cell_id']}.json"
        write_json(path, report)
        next(cell for cell in cells if cell["cell_id"] == report["cell_id"])["report_sha256"] = sha(path)
    counts = {
        "completed": len(reports), "failed_unscored": sum(cell["status"] == "failed" for cell in cells),
        "scorable_pairs": sum(report["summary"]["scorable_references"] for report in reports),
        "high_confidence_pairs": sum(report["high_confidence"]["scorable_references"] for report in reports),
        "public_rows": sum(report["coverage"]["public_messages"] for report in reports),
        **{key: sum(report["coverage"][key] for report in reports) for key in ("task_status_excluded", "discarded_excluded")},
        **{key: sum(report["summary"][key] for report in reports) for key in (
            "embedded_pairs", "unknown_only_predictions", "partial_unknown_predictions", "missing_predictions", "historical_unknown_classifications")},
    }
    summary = {"schema_version": 1, "primary_metric": PRIMARY_METRIC, "metric": METRIC,
               "mode": "reference_assisted_public_only", "private_annotations_used": False,
               "text_normalization": CLEANING, "source_summaries": sources,
               "embedding_model": embedding_provenance, "counts": counts, "cells": cells,
               "code_sha256": {str(path.relative_to(REPO)): sha(path) for path in (Path(__file__), Path(scoring.__file__))},
               "computation": {"api_calls": 0, "embedding_device": "cpu", "unique_embedded_texts": len(texts)},
               "comparability_notes": [METRIC, CLEANING,
                   "Nonzero unknown or structural-gloss similarity is not evidence of decipherment.",
                   "References are public-only, reference-assisted drafts with differing uncertainty; models and budget instructions differ.",
                   "Historical unknown classifications are retained for audit without changing the input or denominator.",
                   "A failed run has no final report and remains unscored. Separate retries retain separate attempt identities."]}
    write_json(output / "summary.json", summary)
    write_csv(output / "summary.csv", cells)
    rows = [{"cell_id": report["cell_id"], "condition": report["condition"],
             **{key: row.get(key) for key in (
                 "id", "sender", "source", "reference", "hypothesis_original", "hypothesis", "scoring_hypothesis",
                 "reference_confidence", "prediction_status", "historical_prediction_status", "historical_unknown_reason",
                 "excluded_reason", "scorable", "included_in_primary_mean")},
             "cosine": (row["scores"] or {}).get("cosine")}
            for report in reports for row in report["lines"]]
    write_json(output / "per_line.json", rows)
    write_csv(output / "per_line.csv", rows)
    (output / "README.md").write_text(readme(summary), encoding="utf-8")
    from render_decoder_comparisons import render
    render(summary, repo, output / "comparisons.html")
    return summary


def readme(summary: dict) -> str:
    rows = []
    for cell in summary["cells"]:
        failed = cell["status"] == "failed"
        value = "Failed / unscored" if failed else f"{cell['cosine']:.6f}"
        high = "N/A" if cell["high_confidence_cosine"] is None else f"{cell['high_confidence_cosine']:.6f}"
        pairs = "N/A" if failed else f"{cell['embedded_pairs']}/{cell['scorable_references']}"
        unknown = "N/A" if failed else str(cell["unknown_only_predictions"])
        rows.append(f"| {cell['cell_id']} | {cell['encoder']} | {cell['seed']} | {cell['decoder']} | {cell['condition']} | {value} | {pairs} | {unknown} | {high} |")
    return f"""# Public-message cosine with unknown answers included as text

**{METRIC}**

- [Interactive comparisons](comparisons.html)
- [Summary CSV](summary.csv) / [JSON](summary.json)
- [Per-message CSV](per_line.csv) / [JSON](per_line.json)
- {summary['counts']['completed']} completed reports; {summary['counts']['failed_unscored']} failed attempt(s), preserved unscored.

| Cell | Encoder | Seed | Decoder | Context | Raw cosine | Embedded / scorable | Literal unknown-only answers | High-confidence cosine |
|---|---|---:|---|---|---:|---:|---:|---:|
{chr(10).join(rows)}

## Method and interpretation

{CLEANING}

There are {summary['counts']['embedded_pairs']:,} embedded pairs out of {summary['counts']['scorable_pairs']:,} scorable message/cell pairs, including **{summary['counts']['unknown_only_predictions']} literal unknown-only answers** and **{summary['counts']['missing_predictions']} missing answers**. Missing answers are not embedded. These counts are lexical descriptions, not semantic judgments. D05 retains its original structural glosses, even though its preamble says their meanings are unknown; D06 retains the literal word `unknown`; D11 retains unknown parentheticals. The historical evaluator's abstention classification is also recorded per line for audit, without altering the text or score.

The denominator is the number of scorable public agent messages with a provided decoder entry. {summary['counts']['task_status_excluded']} task-status entries and {summary['counts']['discarded_excluded']} discarded entries are excluded across all comparison cells. The 30 discarded DeepSeek messages stay excluded in each completed DeepSeek-source comparison. References marked unknown are also excluded. Historical cells require complete alignment. Fresh follow-ups may explicitly retain missing translations as unscored entries with coverage shown; they are never silently filled with `unknown`. High-confidence means use only that reference subset and are N/A when it is empty.

Scores are not percentages correct. The embedding of `unknown` can have positive similarity to English references despite recovering no meaning. Likewise, repetitive structural glosses can score above zero. This requested raw metric changes abstention handling, not the public-reference texts. Original reports, N/A results, and zero-assigned results remain unchanged in their historical directories.

The embedding model, immutable revision, package versions, input hashes, parser hash, token lengths, and truncation flags are saved. All computation is local; no paid API calls are made. Sources differ in reference confidence, task success and budget settings, so this descriptive table does not isolate causal model or context effects.

## Reproduce and append a retry

Run `analysis/score_public_raw_cosines.py` from this experiment directory using the same Python environment and cached pinned MiniLM model. Set `HF_HUB_OFFLINE=1` and `TRANSFORMERS_OFFLINE=1` to ensure offline loading. The default input is `analysis/decoder_comparison_source_catalog/summary.json`.

Use `--extra-summary path/to/summary.json` for a separately archived retry. The extra summary uses the same `cells` format with a unique attempt ID and verified source-report hash; source reports must identify the original decoder document, public reference, transcript, frozen language, input hashes, embedding provenance and per-message alignment. Duplicate cell IDs are rejected, so a failed original attempt cannot be silently overwritten. `--check` validates all inputs without loading embeddings.

Alternatively use `--extra-decoder-config path/to/config.json` to score a fresh archived decoder directly, without a prior embedding pass. The config specifies `cell_id`, `encoder`, `seed`, `decoder`, `decoder_model`, `condition`, `source_escaped`, `protocol`, `reference`, `task_dir`, `language`, `decoder_document`, and `receipt`. The scorer verifies the receipt, archived final answer, monitor hashes, model, condition and exact public transcript before aligning messages. Fresh config inputs allow missing entries to remain visibly unscored with coverage, unless `allow_missing` is explicitly false. All paths are repository-relative.
"""


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--extra-summary", type=Path, action="append", default=[])
    parser.add_argument("--extra-decoder-config", type=Path, action="append", default=[])
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    inputs = [args.input, *args.extra_summary]
    if args.check:
        _, prepared = preflight(inputs, args.output)
        for config_path in args.extra_decoder_config:
            _, item = prepare_extra(config_path, args.output)
            if item["cell"]["cell_id"] in {old["cell"]["cell_id"] for old in prepared}:
                raise ValueError(f"Duplicate cell ID: {item['cell']['cell_id']}")
            prepared.append(item)
        print(json.dumps({"outcomes": len(prepared), "completed": sum("lines" in item for item in prepared)}))
    else:
        print(json.dumps(score(inputs, args.output, extra_decoder_configs=args.extra_decoder_config)["counts"], indent=2))
