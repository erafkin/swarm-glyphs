"""Audited extraction of the eight completed D05–D13 decoder documents.

This is an experiment adapter, not a general document parser. Layout drift is an
error. It reads only the supplied decoder document and preserves its entry bodies
before normalization and before the explicitly documented unknown conversions.
Missing IDs are left to the scoring wrapper's reference-aware preflight.
"""

import re
from pathlib import Path

from src.core.translation_scoring import parse_translation, read_text


_FORMATS = {
    "D05": "section_colon_structural_glosses",
    "D06": "inline_semicolon_unknowns",
    "D07": "numbered_translation_lines",
    "D08": "bulleted_bracket_translation_lines",
    "D09": "bracket_translation_lines",
    "D10": "bracket_translation_lines",
    "D11": "bracket_translation_lines",
    "D13": "numbered_translation_lines",
}
_D05_DECLARATION = (
    "Messages [2]-[110] are given structural glosses only; every content meaning "
    "is unknown. Labels: S = structural description of tokens, U = unknown content."
)
_D06_DECLARATION = (
    "Message 1 is public task status (stage 0, 0 invalid attempts), not Swarmish. "
    "Messages 2 to 110 are each unknown:"
)
_D11_DECLARATION = '"unknown" is used when meaning is unclear.'
# These six audited entries explicitly decline translation. Their parentheticals
# describe structure or repeat glyphs; they supply no translated proposition.
_D11_STRUCTURE_ONLY = {
    2: "unknown (short message, possibly partial assignment).",
    5: "unknown (sequence: 𗉞𘀝𘍂𗌈𘒳).",
    6: "unknown (𗒳𗟎𗢬𗉞𗽕𘅌𘂮𗕴𘂮𗃚𗉞𗁳).",
    8: "unknown (𘍂𗨥𗱑𘒳𗂱𗉞𗨥𘂮𗁳𗼛𗃚𗉞𘏉𗱑𗤄).",
    11: "unknown (𗯘𗃚𗉞𘅌𗤄 𘒳𗉞𘀝).",
    13: "unknown (𗉞𗨥𗇾𗟎𗉞𘊫𘆎𗇾𗉞𘀝𘆎𗇾𗉞𘔃𘆎𗇾).",
}


def _require(condition: bool, message: str) -> None:
    # Do not use assert: validation must also run with python -O.
    if not condition:
        raise ValueError(message)


def _section(text: str, cell_id: str) -> str:
    """Require unique, ordered translation/task/evidence headings."""
    headings = []
    for number, title in ((2, "TRANSLATION"), (3, "THE TASK"), (4, "EVIDENCE")):
        if cell_id == "D05":
            pattern = rf"(?m)^SECTION {number}: {title}\."
        elif cell_id == "D06":
            pattern = rf"(?<!\S){number}\. {title}\."
        else:
            pattern = rf"(?m)^[ \t]*#{{0,6}}[ \t]*{number}\. {title}[ \t]*$"
        matches = list(re.finditer(pattern, text))
        _require(len(matches) == 1,
                 f"{cell_id}: expected exactly one audited {title} heading; found {len(matches)}")
        headings.append(matches[0])
    _require(headings[0].end() < headings[1].start() < headings[2].start(),
             f"{cell_id}: section headings are out of order")
    return text[headings[0].end():headings[1].start()]


def _check_id(message_id: int, seen: set[int], expected_ids: set[int], cell_id: str) -> None:
    _require(message_id > 0 and message_id in expected_ids,
             f"{cell_id}: unexpected translation message ID {message_id}")
    _require(message_id not in seen,
             f"{cell_id}: duplicate translation message ID {message_id}")
    seen.add(message_id)


def _normalize(body: str, section: str) -> str:
    """Apply the core parser's normalization to the two extra list formats."""
    if re.search(r"Confidence applies per entry", section, re.I):
        body = re.sub(r"^(?:\*\*)?[HML](?:/[HML])*(?:,\s*public)?\s*:\s*(?:\*\*)?\s*", "", body)
    body = body.removeprefix("**").lstrip()
    body = re.sub(r"^\[(?:task|agent_\d+)\](?:\*\*)?\s*", "", body)
    return re.sub(r"\s+", " ", body).strip()


def _numbered_entries(section: str, cell_id: str, expected_ids: set[int]) -> tuple[str, list[dict], list[str]]:
    if cell_id == "D08":
        pattern = re.compile(r"^- \[(\d+)\]\s+(.+)$")
    elif cell_id in {"D07", "D13"}:
        pattern = re.compile(r"^(\d+)\.\s+(.+)$")
    else:
        pattern = re.compile(r"^\[(\d+)\]\s+(.+)$")
    entries, before, seen, notes = [], [], set(), []
    separator_seen = False
    for line in section.splitlines():
        if not line.strip():
            if not entries:
                before.append(line)
            continue
        match = pattern.fullmatch(line)
        if match:
            _require(not separator_seen, f"{cell_id}: numbered entry after closing separator")
            message_id, original = int(match[1]), match[2].strip()
            _check_id(message_id, seen, expected_ids, cell_id)
            normalized = _normalize(original, section)
            entries.append({"id": message_id, "original": original, "normalized": normalized,
                            "scoring_text": normalized, "unknown_reason": None})
        elif cell_id == "D08" and line == "---" and entries and not separator_seen:
            separator_seen = True
            notes.append("Trailing Markdown separator excluded from message 97 and scoring text.")
        else:
            _require(not entries, f"{cell_id}: unexpected non-entry text after numbered entries: {line!r}")
            _require(not re.match(r"\s*(?:[-*]\s*)?(?:\[\d+\]|\d+[.)])", line),
                     f"{cell_id}: unexpected numbered-entry layout: {line!r}")
            before.append(line)
    _require(bool(entries), f"{cell_id}: translation section contains no recognized entries")
    return "\n".join(before).strip(), entries, notes


def _inline_unknown_entries(section: str, expected_ids: set[int]) -> tuple[str, list[dict], list[str]]:
    section = section.strip()
    _require(section.startswith(_D06_DECLARATION), "D06: audited all-unknown declaration changed")
    rest = section[len(_D06_DECLARATION):].strip()
    marker = " Structural note only (low confidence):"
    _require(rest.count(marker) == 1, "D06: expected audited structural-note boundary")
    enumeration, postamble = rest.split(marker)
    _require(enumeration.endswith("."), "D06: unknown enumeration must end with a period")
    seen, entries = set(), []
    # Parse the explicit enumeration; never expand the declared 2–110 range.
    for index, part in enumerate(enumeration[:-1].split(";")):
        match = re.fullmatch(r"\s*(\d+) (unknown)\s*", part)
        _require(match is not None, f"D06: unexpected unknown enumeration item {index + 1}: {part!r}")
        message_id = int(match[1])
        _check_id(message_id, seen, expected_ids, "D06")
        entries.append({"id": message_id, "original": match[2], "normalized": match[2],
                        "scoring_text": "Unknown.", "unknown_reason": "explicit_unknown"})
    return _D06_DECLARATION, entries, [
        "Message 1 is described in prose only; no numbered task entry was fabricated.",
        "Only explicitly enumerated unknown entries were extracted; semicolon list punctuation was removed.",
        "Unscored postamble:" + marker + postamble,
    ]


def extract_translation(path: Path, cell_id: str, expected_ids: set[int]) -> dict:
    """Return audited entry bodies and scoring text without reading references.

    ``original`` is the entry body after its ID/list marker, retaining sender tags
    and wording. ``normalized`` follows core parser normalization. ``scoring_text``
    changes only explicit unknown-content cases documented by ``unknown_reason``.
    No source ID is inferred, renumbered, fabricated, or silently dropped.
    """
    _require(cell_id in _FORMATS, f"Unsupported decoder extraction cell: {cell_id}")
    text = read_text(Path(path))
    if cell_id == "D06":
        _require(len(text.splitlines()) == 1, "D06: expected the audited single-line document")
    section = _section(text, cell_id)
    if cell_id == "D06":
        preamble, entries, notes = _inline_unknown_entries(section, expected_ids)
    else:
        preamble, entries, notes = _numbered_entries(section, cell_id, expected_ids)
        if cell_id not in {"D05", "D08"}:
            # Keep normalization identical to the existing scorer, and reject any
            # discrepancy between its parsed bodies and our audited boundaries.
            originals = parse_translation(path, expected_ids, require_section=True, strip_prefixes=False)
            normalized = parse_translation(path, expected_ids, require_section=True)
            _require(originals == {entry["id"]: entry["original"] for entry in entries},
                     f"{cell_id}: audited extraction differs from core parser bodies")
            for entry in entries:
                entry["normalized"] = normalized[entry["id"]]
                entry["scoring_text"] = normalized[entry["id"]]
        if cell_id == "D05":
            _require(_D05_DECLARATION in preamble, "D05: audited global unknown-content declaration changed")
            for entry in entries:
                _require(re.fullmatch(r"[SU]: .+", entry["normalized"]) is not None,
                         f"D05: unexpected structural-gloss layout at ID {entry['id']}")
                entry["scoring_text"] = "Unknown."
                entry["unknown_reason"] = "global_unknown_content_declaration"
            notes.extend([
                "The translation preamble explicitly declares every content meaning unknown; S/U entries are structural glosses only.",
                "Message 1 is described in prose only; no numbered task entry was fabricated.",
            ])
        if cell_id == "D11":
            _require(_D11_DECLARATION in preamble, "D11: audited unknown convention changed")
            for entry in entries:
                if entry["id"] in _D11_STRUCTURE_ONLY:
                    _require(entry["normalized"] == _D11_STRUCTURE_ONLY[entry["id"]],
                             f"D11: audited unknown parenthetical changed at ID {entry['id']}")
                    entry["scoring_text"] = "Unknown."
                    entry["unknown_reason"] = "explicit_unknown_with_structural_commentary"
            notes.append("IDs 2, 5, 6, 8, 11, and 13 explicitly say unknown; parentheticals describe structure or repeat glyphs.")
    return {"format": _FORMATS[cell_id], "preamble": preamble, "conventions": preamble,
            "entries": entries, "notes": notes}
