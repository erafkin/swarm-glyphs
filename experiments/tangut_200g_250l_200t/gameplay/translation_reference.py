"""Offline validation and deterministic rendering of public-only English references.

Use the repository virtualenv. This module never calls a model or reads private
gameplay annotations. ``validate`` never writes; ``render --update-metadata``
also records the translator's attestation to the method documented beside it.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys

REPO = Path(__file__).resolve().parents[3]
BATCH = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))

from src.enc_dec.monitor import read_public_messages, render_public_messages
from experiments.tangut_200g_250l_200t.archive_paths import resolve_raw_path

DISCARDED = "Unknown: message discarded for using characters outside the permitted set."
METHOD = (
    "Reference-assisted translation using only the frozen Swarmish language and "
    "public transcript; not independently certified translation ground truth."
)


def read(path):
    return json.loads(path.read_text(encoding="utf-8"))


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def inside(path, base):
    path = path.resolve()
    require(path.is_relative_to(base.resolve()), f"Path escapes {base}: {path}")
    return path


def run_folders(run_ids, for_render=False):
    manifest = read(BATCH / "batch.json")["runs"]
    archived = {r["id"] for r in manifest if r.get("archived")}
    entries = {r["id"]: inside(BATCH / r["path"], BATCH) for r in manifest}
    gameplay = {key: folder for key, folder in entries.items() if key.startswith(("T", "R"))}
    if not run_ids or run_ids == ["all"]:
        selected = [key for key, folder in gameplay.items() if (folder / "receipt.json").exists()
                    and not (for_render and key in archived)]
        require(selected, "No collected gameplay runs exist")
    else:
        require("all" not in run_ids, "Use 'all' alone or supply explicit run IDs")
        require(len(set(run_ids)) == len(run_ids), "Duplicate run IDs")
        require(all(key in gameplay for key in run_ids), "Expected gameplay IDs such as R06 or archived T01")
        selected = run_ids
    require(not for_render or not any(key in archived for key in selected),
            "Archived English references are read-only; validate them instead of rendering")
    return [(key, gameplay[key], entries) for key in selected]


def validate(run_id, folder, entries):
    """Verify immutable public data and translations without changing any file."""
    receipt = read(folder / "receipt.json")
    plan = read(folder / "plan.json")
    require(receipt.get("status") == "completed", f"{run_id}: receipt is not completed")
    require(receipt.get("id") == plan.get("id") == run_id, "Run identity mismatch")
    source_id = plan["source_run_id"]
    require(receipt.get("source_run_id") == source_id, "Source run mismatch")
    source = entries[source_id]
    source_receipt = read(source / "receipt.json")
    language = source / "handoff/swarmish.txt"
    raw = inside(resolve_raw_path(REPO, folder, receipt), folder / "raw")
    transcript = raw / "task_chatroom.jsonl"
    raw_hash, language_hash = sha(transcript), sha(language)
    require(raw_hash == receipt["raw_sha256"]["task_chatroom.jsonl"], "Archived public transcript changed")
    require(language_hash == source_receipt["handoff_sha256"]["swarmish.txt"], "Frozen language changed")
    require(sha(raw / "swarmish.txt") == language_hash == receipt["raw_sha256"]["swarmish.txt"],
            "Gameplay language differs from frozen reference")
    messages = read_public_messages(transcript, 8)
    rendered_hash = hashlib.sha256(render_public_messages(messages).encode("utf-8")).hexdigest()
    document = read(folder / "english/translation.json")
    require(document.get("source_transcript_sha256") == raw_hash, "Translation raw transcript hash differs")
    require(document.get("language_sha256") == language_hash, "Translation language hash differs")
    require(document.get("rendered_public_transcript_sha256", rendered_hash) == rendered_hash,
            "Translation rendered public transcript hash differs")
    require(document.get("private_annotations_used", False) is False,
            "This public-only reference must not incorporate private annotations")
    translated = document.get("messages")
    require(isinstance(translated, list) and len(translated) == len(messages), "Message count differs")
    for expected, row in zip(messages, translated):
        require(isinstance(row, dict), f"Message {expected['id']}: expected an object")
        require({key: row.get(key) for key in ("id", "sender", "text")} == expected,
                f"Message {expected['id']}: original ID, sender, text or order changed")
        english = row.get("english")
        require(isinstance(english, str) and bool(english.strip()),
                f"Message {expected['id']}: English must be nonempty; write 'unknown' when undecipherable")
        if expected["sender"] == "task":
            require(english == expected["text"], f"Message {expected['id']}: public status must be verbatim")
        elif expected["text"].strip() == "⊘":
            require(english == DISCARDED, f"Message {expected['id']}: discarded message must use {DISCARDED!r}")
    metadata = {
        "method": METHOD,
        "private_annotations_used": False,
        "reference_source_run_id": source_id,
        "source_transcript_sha256": raw_hash,
        "rendered_public_transcript_sha256": rendered_hash,
        "language_sha256": language_hash,
        "methodology_file": "../../english_reference_method.md",
    }
    return document, metadata


def fenced(text, label="text"):
    """Keep even arbitrary source text inside a literal Markdown fence."""
    longest = max((len(match) for match in re.findall(r"`+", text)), default=0)
    fence = "`" * max(3, longest + 1)
    return f"{fence}{label}\n{text}\n{fence}"


def display(value):
    if value is None or value == "" or value == []:
        return "None recorded."
    if isinstance(value, str):
        return value
    return json.dumps(value, ensure_ascii=False, sort_keys=True)


def render(run_id, document, metadata):
    lines = [f"# {run_id}: reference-assisted English transcript", "", METHOD, "",
             "Every public entry retains its original number and sender. Task status is copied "
             "verbatim; discarded messages remain unknown. Uncertainty notes are part of the reference.", "",
             f"Raw transcript SHA-256: `{metadata['source_transcript_sha256']}`  ",
             f"Rendered public transcript SHA-256: `{metadata['rendered_public_transcript_sha256']}`  ",
             f"Frozen language SHA-256: `{metadata['language_sha256']}`", ""]
    for row in document["messages"]:
        kind = "public status" if row["sender"] == "task" else "discarded message" if row["text"].strip() == "⊘" else "agent message"
        ambiguity = row.get("ambiguities", row.get("ambiguity"))
        lines.extend([f"## [{row['id']}] {row['sender']} ({kind})", "", "**English**", "",
                      *["> " + line for line in row["english"].splitlines()], "",
                      "**Original**", "", fenced(row["text"]), "",
                      f"**Confidence:** {display(row.get('confidence', 'Not recorded.'))}", "",
                      f"**Ambiguity:** {display(ambiguity)}", ""])
        # Preserve and expose all additional annotations, including alternate readings.
        reserved = {"id", "sender", "text", "english", "confidence", "ambiguity", "ambiguities"}
        annotations = {key: value for key, value in row.items() if key not in reserved}
        if annotations:
            lines.extend(["**Annotations**", "", fenced(json.dumps(annotations, ensure_ascii=False, indent=2, sort_keys=True), "json"), ""])
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("validate", "render"))
    parser.add_argument("run_ids", nargs="*", help="R06, T01 etc.; omitted or 'all' selects collected gameplay runs")
    parser.add_argument("--update-metadata", action="store_true",
                        help="render only: attest to public-only method and save method/hash metadata in JSON")
    args = parser.parse_args()
    parser.error("--update-metadata requires render") if args.update_metadata and args.command != "render" else None
    try:
        # Validate every selected run before writing any output.
        checked = [(run_id, folder, *validate(run_id, folder, entries))
                   for run_id, folder, entries in run_folders(args.run_ids, for_render=args.command == "render")]
        for run_id, folder, document, metadata in checked:
            if args.command == "render":
                if args.update_metadata:
                    document.update(metadata)
                    (folder / "english/translation.json").write_text(
                        json.dumps(document, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
                (folder / "english/transcript_english.md").write_text(render(run_id, document, metadata), encoding="utf-8")
            print(f"{run_id}: {len(document['messages'])} public entries verified; {args.command} complete")
    except (OSError, ValueError, KeyError, TypeError) as exc:
        parser.exit(1, f"Reference validation failed: {exc}\n")


if __name__ == "__main__":
    main()
