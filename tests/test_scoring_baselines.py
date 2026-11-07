"""Offline regression coverage for clue-conditioned random-guess baselines."""

import unittest

from src.agent_models.model_obj import AgentState, Guess
from src.config import GameConfig
from src.game_object.board import DEFAULT_GOAL_PERSON, Board, load_board
from src.game_object.features import Feature
from src.gameplay.scoring import format_score, is_won, score_round


def agent(agent_id, goal, known_feature, known_value=None, labels=None, person_guess=None):
    guess, rejected = Guess.empty(goal.features).updated(goal.features, labels or goal.values)
    assert not rejected
    return AgentState(
        agent_id=agent_id,
        model="unused-offline",
        known_feature=known_feature,
        known_value=goal.values[known_feature] if known_value is None else known_value,
        features_view=goal.features,
        glyphs_view=[],
        guess=guess,
        person_guess=person_guess,
    )


def small_board():
    return Board(
        features=[
            Feature(name="colour", options=["red", "blue"]),
            Feature(name="shape", options=["circle", "square", "triangle"]),
        ],
        people={
            "one": {"colour": "red", "shape": "circle"},
            "two": {"colour": "red", "shape": "square"},
            "three": {"colour": "blue", "shape": "circle"},
        },
    )


class ScoringBaselineTests(unittest.TestCase):
    def test_real_board_default_target_uses_each_agents_private_clue(self):
        board = load_board()
        goal = board.goal(DEFAULT_GOAL_PERSON)
        self.assertEqual(
            goal.values,
            {
                "hair_colour": "brown",
                "hairstyle": "curls",
                "facial_hair": "beard",
                "glasses": "none",
                "clothing": "shirt",
                "clothing_colour": "blue",
                "background": "green",
                "expression": "smile",
            },
        )
        agents = [agent(f"agent_{i}", goal, feature.name) for i, feature in enumerate(goal.features)]

        report = score_round(1, 240, agents, goal, DEFAULT_GOAL_PERSON, len(board), board=board)

        expected_counts = dict(zip((a.agent_id for a in agents), [9, 15, 6, 19, 8, 10, 9, 28]))
        self.assertEqual(report.person_candidate_counts, expected_counts)
        for agent_id, count in expected_counts.items():
            self.assertAlmostEqual(report.person_chance_by_agent[agent_id], 1 / count)
        self.assertAlmostEqual(report.person_chance, sum(1 / n for n in expected_counts.values()) / 8)
        self.assertEqual(report.feature_chance, {f.name: 0.34375 for f in goal.features})
        self.assertEqual(report.fully_correct_chance, 1 / 16384)
        self.assertEqual(report.blind_feature_chance, {f.name: 0.25 for f in goal.features})
        self.assertEqual(report.blind_fully_correct_chance, 1 / 65536)
        self.assertEqual(report.blind_person_chance, 1 / 32)

    def test_custom_board_counts_and_incompatible_or_empty_candidates(self):
        board = small_board()
        goal = board.goal("one")
        agents = [
            agent("red", goal, "colour"),
            agent("circle", goal, "shape"),
            agent("blue", goal, "colour", "blue"),
            agent("triangle", goal, "shape", "triangle"),
        ]
        report = score_round(1, 0, agents, goal, "one", len(board), board=board)
        self.assertEqual(report.person_candidate_counts, {"red": 2, "circle": 2, "blue": 1, "triangle": 0})
        self.assertEqual(report.person_chance_by_agent, {"red": 0.5, "circle": 0.5, "blue": 0, "triangle": 0})
        self.assertEqual(report.person_chance, 0.25)
        self.assertEqual(report.blind_person_chance, 1 / 3)

        reduced_board = Board(features=board.features, people={i: board.people[i] for i in ("one", "three")})
        reduced = score_round(1, 0, agents, goal, "one", len(reduced_board), board=reduced_board)
        self.assertEqual(reduced.person_candidate_counts, {"red": 1, "circle": 2, "blue": 1, "triangle": 0})
        self.assertEqual(reduced.person_chance, 0.375)
        self.assertEqual(reduced.blind_person_chance, 0.5)

    def test_uneven_assignments_and_option_counts_average_agent_probabilities(self):
        goal = small_board().goal("one")
        agents = [agent("a", goal, "colour"), agent("b", goal, "colour"), agent("c", goal, "shape")]
        report = score_round(1, 0, agents, goal)

        self.assertAlmostEqual(report.feature_chance["colour"], 5 / 6)
        self.assertAlmostEqual(report.feature_chance["shape"], 5 / 9)
        self.assertAlmostEqual(report.fully_correct_chance, 7 / 18)
        self.assertEqual(report.blind_feature_chance, {"colour": 0.5, "shape": 1 / 3})
        self.assertEqual(report.blind_fully_correct_chance, 1 / 6)
        self.assertIsNone(report.person_chance)
        self.assertIsNone(report.blind_person_chance)

        agents[0].known_value = "blue"
        wrong_clue = score_round(1, 0, agents, goal)
        self.assertAlmostEqual(wrong_clue.feature_chance["colour"], 0.5)
        self.assertAlmostEqual(wrong_clue.feature_chance["shape"], 5 / 9)
        self.assertAlmostEqual(wrong_clue.fully_correct_chance, 5 / 18)

    def test_actual_scores_win_checks_and_agent_feedback_are_unchanged(self):
        board = small_board()
        goal = board.goal("one")
        agents = [
            agent("a", goal, "colour", person_guess="one"),
            agent("b", goal, "shape", labels=board.people["three"], person_guess="three"),
        ]
        report = score_round(2, 240.24, agents, goal, "one", len(board), board=board)

        self.assertEqual(report.elapsed_s, 240.2)
        self.assertEqual(report.feature_accuracy, {"colour": 0.5, "shape": 1.0})
        self.assertEqual(report.fully_correct_rate, 0.5)
        self.assertEqual(report.guesses, {"a": board.people["one"], "b": board.people["three"]})
        self.assertEqual(report.person_correct, 1)
        self.assertEqual(report.person_accuracy, 0.5)
        self.assertEqual(report.person_guesses, {"a": "one", "b": "three"})
        for mode, win_mode in [("board", "agents"), ("features", "agents"), ("features", "features")]:
            with self.subTest(mode=mode, win_mode=win_mode):
                self.assertTrue(is_won(report, GameConfig(mode=mode, win_mode=win_mode, win_threshold=0.5)))
                self.assertFalse(is_won(report, GameConfig(mode=mode, win_mode=win_mode, win_threshold=0.75)))
        self.assertEqual(
            format_score(report, GameConfig(mode="board")),
            "Score round 2: 1 of 2 agents (50%) guessed the correct person.",
        )
        self.assertEqual(
            format_score(report, GameConfig(mode="features")),
            "Score round 2: colour 50%, shape 100%. Agents with every feature correct: 50%.",
        )

    def test_legacy_positional_board_size_does_not_claim_a_conditional_baseline(self):
        goal = small_board().goal("one")
        agents = [agent("a", goal, "colour", person_guess="one")]

        report = score_round(1, 0, agents, goal, "one", 3)

        self.assertIsNone(report.person_chance)
        self.assertIsNone(report.person_chance_by_agent)
        self.assertIsNone(report.person_candidate_counts)
        self.assertEqual(report.blind_person_chance, 1 / 3)
        self.assertEqual(report.person_accuracy, 1)


if __name__ == "__main__":
    unittest.main()
