"""
Configuration for the language handoff experiment. The task text is supplied here; the code
doesn't score it. Replace task_prompt and the two wrong-task briefings before a real run.
"""

import json
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, Field, model_validator

from src.config import ReasoningEffort


class LanguageExperimentConfig(BaseModel):
    # Applies to the task chat, not the planning chat (that one is English).
    # "glyphs": task chat may use only the sampled dictionary characters.
    # "free": task chat may use any characters.
    chat_mode: Literal["glyphs", "free"] = "glyphs"
    glyph_dictionary: Literal["dictionary_a", "dictionary_b"] = "dictionary_a"
    n_glyphs: int | None = Field(default=None, ge=1)  # glyphs mode only; None uses the whole dictionary
    allow_spaces: bool = True  # glyphs mode only

    n_agents: int = Field(default=8, ge=1)
    model: str = "openai/gpt-4o-mini"
    agent_models: list[str] | None = None  # per creation-team agent, by index; length must be n_agents
    task_model: str | None = None  # phase-2 team; None uses model
    task_n_agents: int | None = Field(default=None, ge=1)  # None uses n_agents
    monitor_model: str | None = None  # None uses model

    language_minutes: float = Field(default=10, gt=0)  # planning ends at this time, or sooner if every agent is done
    task_minutes: float = Field(default=10, gt=0)
    task_feedback: bool = True  # False: phase 2 chat gets no task status updates
    task_feedback_interval_s: float = Field(default=60, gt=0)  # how often updates are posted when task_feedback is on

    max_cost_usd: float | None = Field(default=None, gt=0)
    chat_context_messages: int = Field(default=50, ge=0)  # task round
    language_context_messages: int = Field(default=100, ge=0)  # encoding round
    min_turn_interval_s: float = Field(default=5, ge=0)
    temperature: float | None = 1.0
    reasoning_effort: ReasoningEffort | None = None
    max_tokens: int = 1500
    request_timeout_s: float = 120
    monitor_max_tokens: int = Field(default=16000, ge=1)
    monitor_reasoning_effort: ReasoningEffort | None = None  # None inherits reasoning_effort

    # What the phase-2 team is asked to do. The monitor's four briefings are this text,
    # no task, wrong_task_far, and wrong_task_near.
    task_prompt: str
    wrong_task_far: str
    wrong_task_near: str

    seed: int | None = 0
    log_dir: str = "logs"

    @model_validator(mode="after")
    def _check(self) -> "LanguageExperimentConfig":
        if self.agent_models is not None and len(self.agent_models) != self.n_agents:
            raise ValueError("agent_models must have exactly n_agents entries")
        for name in ("task_prompt", "wrong_task_far", "wrong_task_near"):
            if not getattr(self, name).strip():
                raise ValueError(f"{name} is empty")
        return self

    def model_for(self, agent_index: int, phase: str) -> str:
        if phase == "task":
            return self.task_model or self.model
        if phase == "monitor":
            return self.monitor_model or self.model
        if self.agent_models is not None:
            return self.agent_models[agent_index]
        return self.model

    @classmethod
    def from_file(cls, path: str | Path) -> "LanguageExperimentConfig":
        return cls.model_validate(json.loads(Path(path).read_text()))
