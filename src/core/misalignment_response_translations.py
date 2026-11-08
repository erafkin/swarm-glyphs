"""Render auditable English sidecars for the six archived Swarmish eval runs.

No model calls are made. Reviewed translations live in each run's
english/translation_units.json. Source logs and machine action values stay intact.
Run: python -m src.core.misalignment_response_translations [--check]
"""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re

REPO_ROOT = Path(__file__).resolve().parents[2]
RUN_NAMES = (
    "20261107_224307_b1949da8_misalignment",
    "20261107_224846_0c227037_misalignment",
    "20261107_225753_aa198557_misalignment",
    "20261107_230321_0a09dcfe_misalignment",
    "20261107_230956_d531e5b0_misalignment",
    "20261107_232734_985bc84f_misalignment",
)
GLYPH = re.compile(r"[\U00017000-\U00018dff]")
GLYPH_SPAN = re.compile(
    r"[\U00017000-\U00018dff]+(?:(?:[ \t]+|(?=agent_))"
    r"(?:[\U00017000-\U00018dff]+|agent_\d+))*")


def sha(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


def file_sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def json_text(value) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2) + "\n"


def mixed_english(text: str) -> bool:
    return bool(re.search("[A-Za-z]", re.sub(r"agent_\d+", "", text)))


def translate_text(text: str, units: dict[str, dict]) -> tuple[str, list[str]]:
    """Translate glyph spans, preserving every existing English character verbatim."""
    if not GLYPH.search(text):
        return text, []
    used = []

    def lookup(source: str) -> str:
        key = sha(source)
        unit = units[key]
        assert unit["source"] == source
        if key not in used:
            used.append(key)
        return unit["english"]

    if mixed_english(text):
        result = GLYPH_SPAN.sub(lambda match: "[" + lookup(match.group()) + "]", text)
    else:
        result = lookup(text)
    if GLYPH.search(result):
        raise ValueError("Untranslated glyphs remain")
    return result, used


def translate_value(value, units: dict[str, dict]) -> tuple[object, list[str]]:
    if isinstance(value, str):
        return translate_text(value, units)
    used = []
    if isinstance(value, dict):
        result = {}
        for key, item in value.items():
            result[key], ids = translate_value(item, units)
            used.extend(ids)
    elif isinstance(value, list):
        result = []
        for item in value:
            translated, ids = translate_value(item, units)
            result.append(translated)
            used.extend(ids)
    else:
        return value, []
    return result, list(dict.fromkeys(used))


def validate_units(document: dict) -> dict[str, dict]:
    units = {}
    for unit in document["units"]:
        key = unit["id"]
        if key != sha(unit["source"]) or key in units:
            raise ValueError("Translation unit ID mismatch or duplicate")
        if not isinstance(unit.get("english"), str) or not unit["english"].strip():
            raise ValueError(f"Missing English translation: {key}")
        if GLYPH.search(unit["english"]):
            raise ValueError(f"Glyphs remain in English translation: {key}")
        if unit.get("confidence") not in ("high", "medium", "low"):
            raise ValueError(f"Missing confidence: {key}")
        if not isinstance(unit.get("notes"), list):
            raise ValueError(f"Missing translation notes: {key}")
        if unit["confidence"] != "high" and not unit["notes"]:
            raise ValueError(f"Uncertainty must be explained: {key}")
        units[key] = unit
    return units


def translate_agent_row(row: dict, line_number: int, units: dict[str, dict]) -> dict:
    output = dict(row)
    used = []
    try:
        parsed = json.loads(row["raw"])
    except (json.JSONDecodeError, TypeError):
        parsed = None
    valid_object = isinstance(parsed, dict)
    if valid_object:
        english, ids = translate_value(parsed, units)
        output["raw"] = json.dumps(english, ensure_ascii=False)
        output["response_fields_english"] = english
    else:
        output["raw"], ids = translate_text(row["raw"], units)
        output["response_fields_english"] = None
    output["raw_original"] = row["raw"]
    used.extend(ids)
    output["posted_original"] = row.get("posted", "")
    output["posted"], ids = translate_text(row.get("posted", ""), units)
    used.extend(ids)
    output["decision_original"] = row.get("decision")
    output["decision"], ids = translate_value(row.get("decision"), units)
    used.extend(ids)
    unit_ids = list(dict.fromkeys(used))
    output["_translation"] = {
        "source_line": line_number,
        "raw_json_status": "parsed_object" if valid_object else "unparsed_original",
        "unit_ids": unit_ids,
        "needs_semantic_review": any(units[key]["confidence"] != "high" for key in unit_ids),
        "notes": ([] if valid_object else [
            "The original response was malformed, truncated, or empty. Its recoverable text is translated in place; no missing JSON, fields, or action is invented."
        ]),
    }
    return output


def markdown_trace(run: str, family: str, rows: list[dict], units: dict[str, dict]) -> str:
    lines = [f"# English agent-call transcript: {family}", "", f"Source run: `{run}`.", "",
             "Reference-assisted translations of the actual response text, including private scratchpads. "
             "Existing English is copied verbatim. Brackets inside mixed English mark translated Swarmish spans. "
             "Uncertain or malformed constructions retain explicit qualifications; these are translations, not judgments.", "",
             "Raw response fields are distinct from posted chat and recorded decisions. An invalid/unposted raw response "
             "does not establish an action. Original logs, decision enums, parse errors, and language-violation flags are retained "
             "in `agent_calls.en.jsonl`. See `translation_units.json` for every source span, confidence, and note.", ""]
    for row in rows:
        meta = row["_translation"]
        lines.extend([f"## {row['prompt_id']} · turn {row['turn']} · {row['agent_id']} · source line {meta['source_line']}", ""])
        lines.extend([f"Original parse error: {row.get('parse_error') or 'none'}; message violation: {row.get('is_violation', False)}; "
                      f"scratchpad violation: {row.get('scratchpad_violation', False)}.", ""])
        fields = row["response_fields_english"]
        if fields is None:
            lines.extend(["**Unparsed raw response (translated in place; original failure retained):**", "",
                          "```text", row["raw"] or "[empty original response]", "```", ""])
        else:
            for field, label in (("scratchpad", "Private scratchpad"), ("message", "Raw message"),
                                 ("decision", "Raw decision enum"), ("email_to", "Email recipient"),
                                 ("email_subject", "Email subject"), ("email_body", "Email body")):
                value = fields.get(field, "")
                if value:
                    lines.extend([f"**{label}:**", "", str(value), ""])
            lines.extend([f"Raw done: `{fields.get('done')}`.", ""])
        lines.extend(["**Actually posted:**", "", row["posted"] or "[nothing posted]", "",
                      "**Recorded agent decision after this turn (may carry over from an earlier turn):**", "",
                      "```json", json.dumps(row["decision"], ensure_ascii=False), "```", ""])
        notes = list(meta["notes"])
        for key in meta["unit_ids"]:
            unit = units[key]
            if unit["notes"]:
                notes.append(f"{key[:12]} ({unit['confidence']} confidence): " + " ".join(unit["notes"]))
        if notes:
            lines.extend(["**Translation notes:**", "", *[f"- {note}" for note in dict.fromkeys(notes)], ""])
    return "\n".join(lines)


def render_run(repo: Path, run_name: str) -> tuple[dict[Path, str], dict]:
    run = repo / "experiments/misalignment_scenarios" / run_name
    source = read_jsonl(run / "agent_calls.jsonl")
    calls = read_jsonl(run / "calls.jsonl")
    family = source[0]["family"]
    document_path = run / "english/translation_units.json"
    document = json.loads(document_path.read_text())
    if document["family"] != family or document["run"] != run_name:
        raise ValueError("Wrong family/run in translation units")
    units = validate_units(document)
    config = json.loads((run / "config.json").read_text())
    families = json.loads((repo / "configs/misalignment_families.json").read_text())["families"]
    family_config = next(item for item in families if item["name"] == family)
    encoder = repo / family_config["swarmish"]
    if file_sha(encoder) != config["translations"][family]["encoder_sha256"]:
        raise ValueError("Encoder does not match the evaluated run")
    bundle = repo / "configs/misalignment_translations" / family / "segments.json"
    segment_document = json.loads(bundle.read_text())
    canonical = json.dumps(segment_document, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    if sha(canonical) != config["translations"][family]["segments_sha256"]:
        raise ValueError("Prompt bindings do not match the evaluated run")
    translated = [translate_agent_row(row, i, units) for i, row in enumerate(source, 1)]
    used = {key for row in translated for key in row["_translation"]["unit_ids"]}
    if used != set(units):
        raise ValueError(f"Unused or missing translation units: {set(units) ^ used}")
    outputs = {}
    english_calls = []
    for call in calls:
        original_rows = [row for row in source if row["prompt_id"] == call["prompt_id"]]
        english_rows = [row for row in translated if row["prompt_id"] == call["prompt_id"]]
        original_chat = "\n".join(f"[{row['agent_id']}] {row['posted']}" for row in original_rows if row["posted"])
        if original_chat != call["response"]:
            raise ValueError(f"Posted chat does not match calls.jsonl: {call['prompt_id']}")
        response_path = run / "responses/swarmish" / family / f"{call['prompt_id']}.txt"
        if response_path.read_text() != call["response"]:
            raise ValueError("Public response archive mismatch")
        english_chat = "\n".join(f"[{row['agent_id']}] {row['posted']}" for row in english_rows if row["posted"])
        outputs[response_path.with_suffix(".en.txt")] = english_chat
        english_call = dict(call)
        english_call["response_original"] = call["response"]
        english_call["response"] = english_chat
        for field in ("decision", "decisions"):
            english_call[field + "_original"] = call[field]
            english_call[field], _ = translate_value(call[field], units)
        english_calls.append(english_call)
    english_dir = run / "english"
    outputs[english_dir / "agent_calls.en.jsonl"] = "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in translated)
    outputs[english_dir / "calls.en.jsonl"] = "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in english_calls)
    outputs[english_dir / "full_transcript.en.md"] = markdown_trace(run_name, family, translated, units)
    manifest = {
        "schema_version": 1, "run": run_name, "family": family,
        "method": document["method"],
        "status": "reference_assisted_translation_with_explicit_uncertainty",
        "agent_calls": len(source), "scenarios": len(calls), "translation_units": len(units),
        "unit_confidence": dict(Counter(unit["confidence"] for unit in units.values())),
        "malformed_or_truncated_raw_calls": sum(row["response_fields_english"] is None for row in translated),
        "original_runner_parse_errors": sum(bool(row.get("parse_error")) for row in source),
        "calls_with_swarmish_scratchpad": sum(bool(row["response_fields_english"] is not None and
                                                   GLYPH.search(json.loads(row["raw_original"]).get("scratchpad", "")))
                                               for row in translated),
        "source_sha256": {str(path.relative_to(repo)): file_sha(path) for path in (
            run / "agent_calls.jsonl", run / "calls.jsonl", run / "config.json", encoder, bundle, document_path)},
        "renderer_sha256": file_sha(Path(__file__)),
        "output_sha256": {str(path.relative_to(repo)): sha(text) for path, text in outputs.items()},
        "judging": {
            "public_chat": "responses/swarmish/<family>/<prompt_id>.en.txt is consumed by the existing judge_misalignment.english_text function and contains only actually posted chat.",
            "full_record": "english/agent_calls.en.jsonl and full_transcript.en.md also contain private scratchpads, rejected/unparsed raw responses, and recorded decisions. These must not be mistaken for posted messages or executed actions.",
            "not_run": "No behavioral judging or new model calls were performed for these translations.",
        },
    }
    outputs[english_dir / "manifest.json"] = json_text(manifest)
    return outputs, manifest


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="validate source hashes, coverage, and exact rendered outputs")
    parser.add_argument("--run", action="append", choices=RUN_NAMES)
    args = parser.parse_args()
    manifests = []
    for run_name in args.run or RUN_NAMES:
        outputs, manifest = render_run(REPO_ROOT, run_name)
        for path, text in outputs.items():
            if args.check:
                if not path.exists() or path.read_text() != text:
                    raise ValueError(f"Missing or stale output: {path}")
            else:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(text, encoding="utf-8")
        manifests.append(manifest)
        print(f"{manifest['family']}: {manifest['agent_calls']} calls, {manifest['scenarios']} scenarios, "
              f"{manifest['translation_units']} translation units, "
              f"{manifest['malformed_or_truncated_raw_calls']} malformed/truncated originals")
    print(f"Total: {sum(m['agent_calls'] for m in manifests)} agent calls; {sum(m['scenarios'] for m in manifests)} scenarios")


if __name__ == "__main__":
    main()
