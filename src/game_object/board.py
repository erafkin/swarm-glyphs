"""
Board for the "Guess Who" game: a fixed set of people, each identified by a random ID ("name") and
a full assignment of feature values. Every agent sees the whole board (in its own shuffled order)
and guesses by name. The board also supplies the goal in both game modes.

board.json maps name -> person, with features in one-hot (or label) form:
  {"c5cf...": {"name": "c5cf...", "hair_colour": {"black": 0, "brown": 1, ...}, ...}, ...}
"""

import json
import random
from pathlib import Path

from pydantic import BaseModel, model_validator

from src.game_object.features import FEATURES, Feature, GoalObject, check_values, labels_from_one_hot

DEFAULT_BOARD_PATH = Path(__file__).parent / "board.json"
DEFAULT_GOAL_PERSON = "c5cfd9c46c6840e9bd503464fab926f0"  # the goal for seed 0 (formerly person 22)


class Board(BaseModel):
    features: list[Feature]
    people: dict[str, dict[str, str]]  # name -> feature labels

    @model_validator(mode="after")
    def _check_people(self) -> "Board":
        for person in self.people.values():
            check_values(self.features, person)
        keys = [tuple(sorted(p.items())) for p in self.people.values()]
        if len(set(keys)) != len(keys):
            raise ValueError("board contains duplicate people")
        return self

    def __len__(self) -> int:
        return len(self.people)

    @property
    def names(self) -> list[str]:
        return sorted(self.people)

    def goal(self, name: str) -> GoalObject:
        return GoalObject(features=self.features, values=self.people[name])

    def render(self, order: list[str] | None = None) -> str:
        """One line per person, in the given order (an agent's shuffled view)."""
        features = [f.name for f in self.features]
        return "\n".join(
            f"person {n}: " + ", ".join(f"{f}={self.people[n][f]}" for f in features) for n in (order or self.names)
        )


def goal_person_for_seed(seed: int | None, board: Board) -> str:
    """Seed 0 is always DEFAULT_GOAL_PERSON; other seeds pick a fixed person per seed; None is random."""
    if seed == 0:
        return DEFAULT_GOAL_PERSON
    # Separate RNG so the goal doesn't depend on (or shift) the game's other random draws.
    return random.Random(seed).choice(board.names)


def load_board(path: str | Path = DEFAULT_BOARD_PATH, features: list[Feature] = FEATURES) -> Board:
    people = {}
    for key, person in json.loads(Path(path).read_text()).items():
        name = person.pop("name", key)
        if name != key:
            raise ValueError(f"board key {key!r} doesn't match its name {name!r}")
        one_hot = isinstance(next(iter(person.values())), dict)
        people[name] = labels_from_one_hot(person) if one_hot else person
    return Board(features=features, people=people)
