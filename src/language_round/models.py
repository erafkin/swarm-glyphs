"""Agent state and the two turn schemas. The private answer is logged, not posted."""

from typing import Any

from pydantic import BaseModel


class RoundAgent(BaseModel):
    agent_id: str
    model: str
    glyphs_view: list[str] = []
    scratchpad: str = ""
    answer: str = ""  # phase 2: private solution, in English; the task feedback may count these
    done: bool = False
    turn_count: int = 0


class CreationResponse(BaseModel):
    message: str = ""
    language_document: str = ""  # full shared language.txt; empty leaves the current file unchanged
    done: bool = False


class TaskResponse(BaseModel):
    scratchpad: str = ""
    message: str = ""
    answer: str = ""


def _schema(name: str, fields: list[str]) -> dict[str, Any]:
    properties = {field: {"type": "string"} for field in fields}
    if "done" in properties:
        properties["done"] = {"type": "boolean"}
    return {
        "name": name,
        "strict": True,
        "schema": {
            "type": "object",
            "properties": properties,
            "required": list(properties),
            "additionalProperties": False,
        },
    }


CREATION_SCHEMA = _schema("creation_turn", ["message", "language_document", "done"])
TASK_SCHEMA = _schema("task_turn", ["scratchpad", "message", "answer"])
