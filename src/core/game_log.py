"""
Per-game log folder. Each stream (chatroom, agent_calls, scores) is an append-only JSONL file;
one-off artifacts (config, goal, summary) are plain JSON.
"""

import json
import time
import uuid
from pathlib import Path
from typing import Any


class GameLogger:
    def __init__(self, log_dir: str):
        self.game_id = uuid.uuid4().hex[:8]
        self.path = Path(log_dir) / f"{time.strftime('%Y%m%d_%H%M%S')}_{self.game_id}"
        self.path.mkdir(parents=True, exist_ok=True)

    def log(self, stream: str, record: dict[str, Any]) -> None:
        with open(self.path / f"{stream}.jsonl", "a", encoding="utf-8") as f:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")

    def write_json(self, name: str, data: Any) -> None:
        (self.path / f"{name}.json").write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
