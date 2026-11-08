"""
Per-game log folder, <log_dir>/<timestamp>_<id>[_<label>]. The label names what the run covers
(round_1, round_2, round_1_2_3, round_3). Each stream (chatroom, agent_calls, scores) is an
append-only JSONL file; one-off artifacts (config, goal, summary) are plain JSON.
"""

import json
import re
import time
import uuid
from pathlib import Path
from typing import Any


def _json_text(data: Any, *, indent: int | None = None) -> str:
    """Keep ordinary Unicode readable, but escape malformed provider surrogate text.

    Lone UTF-16 surrogates can arrive in API strings or escaped JSON fields. They
    cannot be written as UTF-8; JSON escapes retain them in the raw log instead.
    """
    text = json.dumps(data, ensure_ascii=False, indent=indent)
    return re.sub(r"[\ud800-\udfff]", lambda match: f"\\u{ord(match[0]):04x}", text)


class GameLogger:
    def __init__(self, log_dir: str, label: str = ""):
        self.game_id = uuid.uuid4().hex[:8]
        name = f"{time.strftime('%Y%m%d_%H%M%S')}_{self.game_id}"
        if label:
            name += f"_{label}"
        self.path = Path(log_dir) / name
        self.path.mkdir(parents=True, exist_ok=True)

    def log(self, stream: str, record: dict[str, Any]) -> None:
        with open(self.path / f"{stream}.jsonl", "a", encoding="utf-8") as f:
            f.write(_json_text(record) + "\n")

    def write_json(self, name: str, data: Any) -> None:
        (self.path / f"{name}.json").write_text(_json_text(data, indent=2), encoding="utf-8")
