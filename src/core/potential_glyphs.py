"""
Potential glyphs for the game. The models can only use these glyphs (plus spaces and agent IDs,
unless config.allow_spaces is off) in chatroom messages to communicate with other agents.

Glyphs come from a dictionary file (dictionary_a.txt .. dictionary_d.txt at the repo root, chosen
in config). Every non-whitespace character in the file is one glyph. Each game samples
config.n_glyphs of them, shared by all agents; each agent is shown that set in its own random order.
"""

import random
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]

# Posted in place of any message that contains something other than the allowed characters.
VIOLATION_TOKEN = "⊘"


def dictionary_path(name: str) -> Path:
    return REPO_ROOT / f"{name}.txt"


def load_dictionary(path: str | Path) -> list[str]:
    glyphs = [ch for ch in Path(path).read_text(encoding="utf-8") if not ch.isspace()]
    if len(set(glyphs)) != len(glyphs):
        raise ValueError(f"duplicate glyphs in {path}")
    if VIOLATION_TOKEN in glyphs:
        raise ValueError(f"the violation token {VIOLATION_TOKEN!r} can't be a glyph")
    return glyphs


def sample_glyphs(name: str, n: int, rng: random.Random) -> list[str]:
    """The game's shared glyph set: n glyphs sampled without replacement from the named dictionary."""
    dictionary = load_dictionary(dictionary_path(name))
    if n > len(dictionary):
        raise ValueError(f"n_glyphs={n} but {name} only has {len(dictionary)} glyphs")
    return rng.sample(dictionary, n)


# Characters prose may use beside the inventory: combining marks, general punctuation (typographic quotes
# and dashes), arrows, mathematical operators (the violation token ⊘) and the replacement character the
# client substitutes for broken surrogates. Latin-1 and C1 characters are not excluded: in these English
# documents a run of them is byte-wise mojibake of glyphs, which the client repairs when it is reversible.
_PROSE_RANGES = ((0x0300, 0x036F), (0x2000, 0x206F), (0x2190, 0x21FF), (0x2200, 0x22FF), (0xFFFD, 0xFFFD))
CORRUPTION_MIN_GLYPH_CHARS = 20
CORRUPTION_MAX_INVENTORY_SHARE = 0.5


def glyph_report(text: str, glyphs: list[str] | set[str]) -> tuple[int, int]:
    """(glyph-like characters, how many of them are inventory glyphs).

    Glyph-like means outside ASCII and not whitespace or common prose punctuation. For a Latin alphabet
    nothing counts, so the corruption guard below never fires there.
    """
    inventory = set(glyphs)
    attempts = hits = 0
    for ch in text:
        code = ord(ch)
        if code < 0x80 or ch.isspace() or any(lo <= code <= hi for lo, hi in _PROSE_RANGES):
            continue
        attempts += 1
        if ch in inventory:
            hits += 1
    return attempts, hits


def is_corrupted_document(text: str, glyphs: list[str] | set[str]) -> bool:
    """A document that writes glyphs, but mostly glyphs that are not in the inventory.

    Seen with Grok 4.7, which sometimes writes astral-plane glyphs as JSON escapes numbered from an arbitrary
    base, so every glyph decodes to some other script. A valid draft with a few stray glyphs is not corrupted.
    """
    attempts, hits = glyph_report(text, glyphs)
    return attempts >= CORRUPTION_MIN_GLYPH_CHARS and hits < attempts * CORRUPTION_MAX_INVENTORY_SHARE


def is_glyph_only(text: str, agent_ids: list[str], glyphs: list[str], allow_spaces: bool = True) -> bool:
    """
    With spaces: text is only glyphs, spaces, and agent IDs.
    Without spaces: text is only glyphs (no agent IDs either, so nothing can act as a delimiter).
    """
    if not allow_spaces:
        return all(ch in set(glyphs) for ch in text)
    # Longest first so e.g. "agent_10" isn't partially matched as "agent_1". IDs may touch
    # glyphs directly, but not other ASCII word characters.
    ids = "|".join(re.escape(a) for a in sorted(agent_ids, key=len, reverse=True)) or r"(?!)"
    text = re.sub(rf"(?<![A-Za-z0-9_])(?:{ids})(?![A-Za-z0-9_])", "", text)
    return all(ch in set(glyphs) | {" "} for ch in text)
