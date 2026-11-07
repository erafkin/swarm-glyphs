"""
Potential glyphs for the game. The models can only use these glyphs (plus spaces and
agent IDs) in chatroom messages to communicate with other agents.

Glyphs are loaded from a .txt file (config.glyphs_path). Every non-whitespace character in the
file is one glyph, so one-per-line or space-separated both work.
Each agent is shown the glyphs in its own random order.
"""

import re
from pathlib import Path

DEFAULT_GLYPHS_PATH = Path(__file__).parent / "glyphs.txt"

# Posted in place of any message that contains something other than glyphs, spaces, and agent IDs.
VIOLATION_TOKEN = "⊘"


def load_glyphs(path: str | Path = DEFAULT_GLYPHS_PATH) -> list[str]:
    glyphs = [ch for ch in Path(path).read_text(encoding="utf-8") if not ch.isspace()]
    if len(set(glyphs)) != len(glyphs):
        raise ValueError(f"duplicate glyphs in {path}")
    if VIOLATION_TOKEN in glyphs:
        raise ValueError(f"the violation token {VIOLATION_TOKEN!r} can't be a glyph")
    return glyphs


def is_glyph_only(text: str, agent_ids: list[str], glyphs: list[str]) -> bool:
    """True if text consists only of glyphs, spaces, and agent IDs."""
    # Longest IDs first so e.g. "agent_10" isn't partially matched as "agent_1".
    for agent_id in sorted(agent_ids, key=len, reverse=True):
        text = re.sub(rf"(?<!\w){re.escape(agent_id)}(?!\w)", " ", text)
    allowed = set(glyphs) | {" "}
    return all(ch in allowed for ch in text)
