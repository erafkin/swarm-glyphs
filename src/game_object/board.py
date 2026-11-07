"""
Board for the "Guess Who" game: a fixed set of numbered people, each a full assignment of feature values.
Every agent sees the whole board. The board also supplies the default goal in both game modes.

board.json maps person number -> person, with features in one-hot (or label) form:
  {"22": {"number": 22, "hair_colour": {"black": 0, "brown": 1, ...}, ...}, ...}
"""

import json
import random
from pathlib import Path

from pydantic import BaseModel, model_validator

from src.game_object.features import FEATURES, Feature, GoalObject, check_values, labels_from_one_hot

DEFAULT_BOARD_PATH = Path(__file__).parent / "board.json"
DEFAULT_GOAL_PERSON = 22  # the goal for seed 0


class Board(BaseModel):
    features: list[Feature]
    people: dict[int, dict[str, str]]  # person number -> feature labels

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
    def numbers(self) -> list[int]:
        return sorted(self.people)

    def goal(self, number: int) -> GoalObject:
        return GoalObject(features=self.features, values=self.people[number])

    def render(self, order: list[int] | None = None) -> str:
        """One line per person. order changes only the listing order; person numbers stay fixed."""
        names = [f.name for f in self.features]
        return "\n".join(
            f"person {i}: " + ", ".join(f"{n}={self.people[i][n]}" for n in names) for i in (order or self.numbers)
        )


def goal_person_for_seed(seed: int | None, board: Board) -> int:
    """Seed 0 is always DEFAULT_GOAL_PERSON; other seeds pick a fixed person per seed; None is random."""
    if seed == 0:
        return DEFAULT_GOAL_PERSON
    # Separate RNG so the goal doesn't depend on (or shift) the game's other random draws.
    return random.Random(seed).choice(board.numbers)


def load_board(path: str | Path = DEFAULT_BOARD_PATH, features: list[Feature] = FEATURES) -> Board:
    people = {}
    for key, person in json.loads(Path(path).read_text()).items():
        number = person.pop("number", int(key))
        if number != int(key):
            raise ValueError(f"board key {key!r} doesn't match its number {number}")
        one_hot = isinstance(next(iter(person.values())), dict)
        people[number] = labels_from_one_hot(person) if one_hot else person
    return Board(features=features, people=people)
