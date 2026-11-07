"""
Board for the "Guess Who" game: a fixed set of people, each a full assignment of feature values.
Every agent sees the whole board (in its own shuffled order, with no person identifiers) and guesses
the goal person's features. The board also supplies the goal in both game modes.

board.json maps person number -> person, with features in one-hot (or label) form:
  {"22": {"number": 22, "hair_colour": {"black": 0, "brown": 1, ...}, ...}, ...}
Person numbers are internal (goal selection and logs); agents never see them.
"""

import json
import random
from pathlib import Path

from pydantic import BaseModel, model_validator

from src.guess_who.features import FEATURES, Feature, GoalObject, check_values, labels_from_one_hot

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
        """One line per person, in the given order (an agent's shuffled view), without identifiers."""
        features = [f.name for f in self.features]
        return "\n".join(
            "- " + ", ".join(f"{f}={self.people[n][f]}" for f in features) for n in (order or self.numbers)
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
