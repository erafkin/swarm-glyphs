"""
Scoring feedback for the game.
For each agent, pull its current guess and compare it to the true goal object.
- features mode: per-feature accuracy across agents, plus the fraction of agents with every feature correct.
- board mode: the fraction of agents who guessed the correct person.
The group-level result is posted to the chatroom in english. Feature accuracy is computed in both
modes so it's always in the logs, but in board mode it isn't shown to the agents.
Chance baselines use each agent's private clue, then guess uniformly without communication or
scoring feedback. Feature guesses sample each unknown option independently; person guesses sample
the clue-compatible board members. The original blind baselines are retained explicitly.
These reference probabilities are logged next to each score, not posted or used to determine wins.
"""

import math

from pydantic import BaseModel

from src.agent_models.model_obj import AgentState
from src.config import GameConfig
from src.game_object.board import Board
from src.game_object.features import GoalObject


class ScoreReport(BaseModel):
    round: int
    elapsed_s: float
    feature_accuracy: dict[str, float]  # fraction of agents correct, per feature
    feature_chance: dict[str, float]  # clue-aware expected accuracy, averaged across agents
    fully_correct_rate: float  # fraction of agents with every feature correct
    fully_correct_chance: float
    guesses: dict[str, dict[str, str | None]]  # agent_id -> labels, kept for the log only
    blind_feature_chance: dict[str, float] | None = None
    blind_fully_correct_chance: float | None = None
    # board mode only
    person_correct: int | None = None  # number of agents who guessed the goal person
    person_accuracy: float | None = None
    person_chance: float | None = None  # clue-aware mean; unavailable without the actual board
    person_guesses: dict[str, str | None] | None = None
    blind_person_chance: float | None = None  # 1 / board size
    person_chance_by_agent: dict[str, float] | None = None
    person_candidate_counts: dict[str, int] | None = None


def score_round(
    round_num: int,
    elapsed_s: float,
    agents: list[AgentState],
    goal: GoalObject,
    goal_person: str | None = None,
    board_size: int | None = None,
    *,
    board: Board | None = None,
) -> ScoreReport:
    """Score current guesses and log one-shot random baselines conditioned on private clues.

    Pass the actual board for the person baseline, including when using a custom board. Legacy
    callers supplying only board_size still receive the blind baseline; person_chance is None.
    """
    guesses = {a.agent_id: a.guess.to_labels(goal.features) for a in agents}
    n = len(agents)

    feature_accuracy = {
        name: sum(g[name] == goal.values[name] for g in guesses.values()) / n for name in goal.feature_names
    }
    fully_correct = sum(all(g[name] == goal.values[name] for name in goal.feature_names) for g in guesses.values())
    blind_feature_chance = {f.name: 1 / len(f.options) for f in goal.features}
    agent_feature_chances = [
        {
            f.name: (
                float(agent.known_value == goal.values[f.name])
                if agent.known_feature == f.name else blind_feature_chance[f.name]
            )
            for f in goal.features
        }
        for agent in agents
    ]
    feature_chance = {
        name: sum(chances[name] for chances in agent_feature_chances) / n
        for name in goal.feature_names
    }

    report = ScoreReport(
        round=round_num,
        elapsed_s=round(elapsed_s, 1),
        feature_accuracy=feature_accuracy,
        feature_chance=feature_chance,
        fully_correct_rate=fully_correct / n,
        fully_correct_chance=sum(math.prod(chances.values()) for chances in agent_feature_chances) / n,
        guesses=guesses,
        blind_feature_chance=blind_feature_chance,
        blind_fully_correct_chance=math.prod(blind_feature_chance.values()),
    )
    if goal_person is not None:
        report.person_guesses = {a.agent_id: a.person_guess for a in agents}
        report.person_correct = sum(a.person_guess == goal_person for a in agents)
        report.person_accuracy = report.person_correct / n
        size = len(board) if board is not None else board_size
        if size is None or size <= 0:
            raise ValueError("board or a positive board_size is required for person scoring")
        report.blind_person_chance = 1 / size
        if board is not None:
            report.person_chance_by_agent = {}
            report.person_candidate_counts = {}
            for agent in agents:
                candidates = [
                    name for name, values in board.people.items()
                    if values[agent.known_feature] == agent.known_value
                ]
                report.person_candidate_counts[agent.agent_id] = len(candidates)
                report.person_chance_by_agent[agent.agent_id] = (
                    1 / len(candidates) if goal_person in candidates else 0.0
                )
            report.person_chance = sum(report.person_chance_by_agent.values()) / n
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
