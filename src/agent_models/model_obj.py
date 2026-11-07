"""
Model objects for agents.

- AgentState: an agent's identity, the one feature it knows, its scratchpad, and its current guess.
- Guess: the agent's current belief about the goal object, stored as one-hot encodings per feature.
- AgentResponse: the structured output each game turn must return.

The scratchpad can be in english or in glyphs and is overwritten every turn
(every version is preserved in the agent call log).
"""

import random

from pydantic import BaseModel, Field, model_validator

from src.game_object.features import Feature


class Guess(BaseModel):
    # feature name -> one-hot vector over that feature's options; all zeros means "no guess yet"
    one_hot: dict[str, list[int]]

    @model_validator(mode="after")
    def _check_one_hot(self) -> "Guess":
        for name, vec in self.one_hot.items():
            if any(v not in (0, 1) for v in vec) or sum(vec) > 1:
                raise ValueError(f"guess for {name!r} is not a valid one-hot vector: {vec}")
        return self

    @classmethod
    def empty(cls, features: list[Feature]) -> "Guess":
        return cls(one_hot={f.name: [0] * len(f.options) for f in features})

    @classmethod
    def random(cls, features: list[Feature], rng: random.Random) -> "Guess":
        guess, _ = cls.empty(features).updated(features, {f.name: rng.choice(f.options) for f in features})
        return guess

    def to_labels(self, features: list[Feature]) -> dict[str, str | None]:
        labels = {}
        for f in features:
            vec = self.one_hot[f.name]
            labels[f.name] = f.options[vec.index(1)] if 1 in vec else None
        return labels

    def updated(self, features: list[Feature], labels: dict[str, str | None]) -> tuple["Guess", list[str]]:
        """
        Return a new Guess with the given label updates applied, plus a list of rejected updates.
        Agents must always guess, so None and unknown labels are rejected and the previous value is kept.
        """
        one_hot = {name: vec.copy() for name, vec in self.one_hot.items()}
        rejected = []
        by_name = {f.name: f for f in features}
        for name, label in labels.items():
            feature = by_name.get(name)
            if feature is None or label not in feature.options:
                rejected.append(f"{name}={label}")
                continue
            one_hot[name] = [int(opt == label) for opt in feature.options]
        return Guess(one_hot=one_hot), rejected


class AgentState(BaseModel):
    agent_id: str
    model: str
    known_feature: str
    known_value: str
    # This agent's view of the game, shuffled per agent to counter order effects.
    # Guess one-hot vectors always use the canonical option order from features.py.
    features_view: list[Feature]
    glyphs_view: list[str]
    board_order: list[int] | None = None  # board mode only: order the person numbers are listed in
    scratchpad: str = ""
    guess: Guess  # per-feature beliefs; scored in features mode, notes only in board mode
    person_guess: int | None = None  # board mode only: person number on the board
    turn_count: int = 0


class AgentResponse(BaseModel):
    scratchpad: str = ""
    message: str = ""
    guess: dict[str, str | None] = Field(default_factory=dict)
    person_guess: int | None = None
