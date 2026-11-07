"""
Scoring feedback for the game.
For each agent, pull its current guess and compare it to the true goal object.
- features mode: per-feature accuracy across agents, plus the fraction of agents with every feature correct.
- board mode: the fraction of agents who guessed the correct person.
The group-level result is posted to the chatroom in english. Feature accuracy is computed in both
modes so it's always in the logs, but in board mode it isn't shown to the agents.
Chance baselines (expected accuracy of uniform random guessing) are logged next to each score, not posted.
"""

import math

from pydantic import BaseModel

from src.agent_models.model_obj import AgentState
from src.config import GameConfig
from src.game_object.features import GoalObject


class ScoreReport(BaseModel):
    round: int
    elapsed_s: float
    feature_accuracy: dict[str, float]  # fraction of agents correct, per feature
    feature_chance: dict[str, float]  # 1 / number of options
    fully_correct_rate: float  # fraction of agents with every feature correct
    fully_correct_chance: float
    guesses: dict[str, dict[str, str | None]]  # agent_id -> labels, kept for the log only
    # board mode only
    person_correct: int | None = None  # number of agents who guessed the goal person
    person_accuracy: float | None = None
    person_chance: float | None = None  # 1 / board size
    person_guesses: dict[str, str | None] | None = None


def score_round(
    round_num: int,
    elapsed_s: float,
    agents: list[AgentState],
    goal: GoalObject,
    goal_person: str | None = None,
    board_size: int | None = None,
) -> ScoreReport:
    guesses = {a.agent_id: a.guess.to_labels(goal.features) for a in agents}
    n = len(agents)

    feature_accuracy = {
        name: sum(g[name] == goal.values[name] for g in guesses.values()) / n for name in goal.feature_names
    }
    fully_correct = sum(all(g[name] == goal.values[name] for name in goal.feature_names) for g in guesses.values())
    feature_chance = {f.name: 1 / len(f.options) for f in goal.features}

    report = ScoreReport(
        round=round_num,
        elapsed_s=round(elapsed_s, 1),
        feature_accuracy=feature_accuracy,
        feature_chance=feature_chance,
        fully_correct_rate=fully_correct / n,
        fully_correct_chance=math.prod(feature_chance.values()),
        guesses=guesses,
    )
    if goal_person is not None:
        report.person_guesses = {a.agent_id: a.person_guess for a in agents}
        report.person_correct = sum(a.person_guess == goal_person for a in agents)
        report.person_accuracy = report.person_correct / n
        report.person_chance = 1 / board_size
    return report


def is_won(report: ScoreReport, config: GameConfig) -> bool:
    if config.mode == "board":
        return report.person_accuracy >= config.win_threshold
    if config.win_mode == "agents":
        return report.fully_correct_rate >= config.win_threshold
    return all(acc >= config.win_threshold for acc in report.feature_accuracy.values())


def format_score(report: ScoreReport, config: GameConfig) -> str:
    if config.mode == "board":
        return (
            f"Score round {report.round}: {report.person_correct} of {len(report.person_guesses)} agents "
            f"({report.person_accuracy:.0%}) guessed the correct person."
        )
    per_feature = ", ".join(f"{name} {acc:.0%}" for name, acc in report.feature_accuracy.items())
    return (
        f"Score round {report.round}: {per_feature}. "
        f"Agents with every feature correct: {report.fully_correct_rate:.0%}."
    )
