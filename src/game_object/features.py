"""
Goal object definition: the feature schema and the hidden true values.
Prompts, guesses, and scoring all read FEATURES dynamically.
"""

import random

from pydantic import BaseModel, model_validator


class Feature(BaseModel):
    name: str
    options: list[str]

    @model_validator(mode="after")
    def _check_options(self) -> "Feature":
        if len(set(self.options)) != len(self.options) or not self.options:
            raise ValueError(f"feature {self.name!r} needs non-empty, unique options")
        return self


class GoalObject(BaseModel):
    features: list[Feature]
    values: dict[str, str]

    @model_validator(mode="after")
    def _check_values(self) -> "GoalObject":
        check_values(self.features, self.values)
        return self

    @property
    def feature_names(self) -> list[str]:
        return [f.name for f in self.features]


FEATURES: list[Feature] = [
    Feature(name="hair_colour", options=["black", "brown", "blonde", "red"]),
    Feature(name="hairstyle", options=["bob", "curls", "spikes", "ponytail"]),
    Feature(name="facial_hair", options=["none", "moustache", "goatee", "beard"]),
    Feature(name="glasses", options=["none", "round", "square", "sunglasses"]),
    Feature(name="clothing", options=["shirt", "sweater", "hoodie", "jacket"]),
    Feature(name="clothing_colour", options=["red", "blue", "green", "yellow"]),
    Feature(name="background", options=["green", "blue", "yellow", "purple"]),
    Feature(name="expression", options=["neutral", "smile", "frown", "surprised"]),
]


def check_values(features: list[Feature], values: dict[str, str]) -> None:
    """Raise if values doesn't assign exactly one valid option to every feature."""
    if set(values) != {f.name for f in features}:
        raise ValueError(f"values must cover exactly the features {[f.name for f in features]}, got {list(values)}")
    for feature in features:
        if values[feature.name] not in feature.options:
            raise ValueError(f"{values[feature.name]!r} is not a valid option for {feature.name!r}")


def labels_from_one_hot(one_hot: dict[str, dict[str, int]]) -> dict[str, str]:
    """Convert {"hair_colour": {"black": 0, "blonde": 1, ...}, ...} to {"hair_colour": "blonde", ...}."""
    labels = {}
    for name, options in one_hot.items():
        chosen = [opt for opt, v in options.items() if v == 1]
        if len(chosen) != 1:
            raise ValueError(f"{name!r} must have exactly one option set to 1, got {options}")
        labels[name] = chosen[0]
    return labels


def shuffle_options(features: list[Feature], rng: random.Random) -> list[Feature]:
    """Copy of features with each feature's options in a random order (feature order unchanged)."""
    return [Feature(name=f.name, options=rng.sample(f.options, len(f.options))) for f in features]
