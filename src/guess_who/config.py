"""
Game configuration. Every tunable knob lives here so runs are reproducible from config.json.
"""

import json
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, Field, model_validator

from src.core.types import ReasoningEffort
from src.guess_who.board import DEFAULT_BOARD_PATH


class GameConfig(BaseModel):
    # "features": agents guess every feature and get per-feature feedback.
    # "board": agents also see a board of people (Guess Who) and guess the goal person's features;
    #   a guess counts as correct only if every feature matches.
    mode: Literal["features", "board"] = "features"
    board_path: str = str(DEFAULT_BOARD_PATH)
    # The goal is a person from the board in both modes (by its internal number in board.json).
    # None derives it from seed: seed 0 -> person 22, other seeds -> a fixed person per seed.
    goal_person: int | None = None
    # Glyphs: n_glyphs sampled from this dictionary file (repo root), shared by all agents.
    glyph_dictionary: Literal["dictionary_a", "dictionary_b"] = "dictionary_a"
    n_glyphs: int = Field(default=18, ge=1)
    allow_spaces: bool = True  # False: chat messages may contain only glyphs (no spaces or agent IDs)
    # True adds "use these glyphs to create a language ... no 1-to-1 mapping to Latin characters".
    language_instruction: bool = False

    # Features cycle across agents, so n_agents >= number of features covers every feature.
    n_agents: int = Field(default=8, ge=1)
    # Shuffle private ownership independently of public feature order and all other random draws.
    # False preserves legacy runs whose agent index identifies the feature.
    randomize_feature_assignment: bool = False

    # Default model for every agent; agent_models (if set) overrides per agent, by index.
    model: str = "openai/gpt-4o-mini"
    agent_models: list[str] | None = None

    # Stop conditions besides winning; None disables that limit.
    score_interval_s: float = Field(default=60, gt=0)
    max_score_rounds: int | None = Field(default=100, ge=1)
    max_cost_usd: float | None = Field(default=None, gt=0)  # total OpenRouter cost for the run

    # Features mode only ("board" mode wins when win_threshold of agents have every feature right):
    # "agents": fraction of agents with every feature correct must reach win_threshold.
    # "features": every feature must be guessed correctly by at least win_threshold of agents.
    win_mode: Literal["agents", "features"] = "agents"
    win_threshold: float = Field(default=0.9, gt=0, le=1)

    chat_context_messages: int = Field(default=50, ge=0)
    min_turn_interval_s: float = Field(default=5, ge=0)
    temperature: float | None = 1.0  # None omits it (some reasoning models don't accept it)
    reasoning_effort: ReasoningEffort | None = None  # None uses the model default
    max_tokens: int = 1500  # includes hidden reasoning tokens on reasoning models
    request_timeout_s: float = 120

    final_interview: bool = True  # after the game, ask each agent to explain its communication strategy
    final_interview_max_tokens: int = Field(default=16000, ge=1)  # also bounded by gameplay max_tokens
    final_interview_reasoning_effort: ReasoningEffort | None = None  # None inherits gameplay effort

    seed: int | None = 0  # also drives per-agent shuffles and starting guesses; None is fully random
    log_dir: str = "logs"

    @model_validator(mode="after")
    def _check_agent_models(self) -> "GameConfig":
        if self.agent_models is not None and len(self.agent_models) != self.n_agents:
            raise ValueError("agent_models must have exactly n_agents entries")
        return self

    def model_for(self, agent_index: int) -> str:
        if self.agent_models is not None:
            return self.agent_models[agent_index]
        return self.model

    @classmethod
    def from_file(cls, path: str | Path) -> "GameConfig":
        return cls.model_validate(json.loads(Path(path).read_text()))
