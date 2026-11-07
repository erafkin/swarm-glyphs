"""Offline checks that random ownership hides the ID-to-feature shortcut without changing the task."""

from collections import Counter
import re
import tempfile
import unittest
from unittest.mock import patch

from src.config import GameConfig
from src.game_object.features import FEATURES
from src.gameplay.play_game import Game


class FeatureAssignmentTests(unittest.TestCase):
    def setUp(self):
        self.logs = tempfile.TemporaryDirectory(prefix="feature-assignment-")
        self.addCleanup(self.logs.cleanup)

    def game(self, **settings):
        return Game(GameConfig(log_dir=self.logs.name, **settings))

    @staticmethod
    def assignments(game):
        return [agent.known_feature for agent in game.agents]

    def test_randomized_eight_agent_assignment_is_bijective_with_true_clues(self):
        for seed in range(10):
            with self.subTest(seed=seed):
                game = self.game(seed=seed, randomize_feature_assignment=True)
                self.assertEqual(Counter(self.assignments(game)), Counter(game.goal.feature_names))
                for agent in game.agents:
                    self.assertEqual(agent.known_value, game.goal.values[agent.known_feature])

    def test_reproducible_for_same_seed_and_varies_across_seeds(self):
        permutations = set()
        for seed in range(10):
            first = self.game(seed=seed, randomize_feature_assignment=True)
            second = self.game(seed=seed, randomize_feature_assignment=True)
            self.assertEqual(first.agents, second.agents)
            self.assertEqual(first.system_prompts, second.system_prompts)
            permutations.add(tuple(self.assignments(first)))
        self.assertGreater(len(permutations), 1)

    def test_ownership_does_not_change_other_random_draws_or_public_schema(self):
        for mode in ("features", "board"):
            for seed in (0, 1, 98765):
                with self.subTest(mode=mode, seed=seed):
                    legacy = self.game(mode=mode, seed=seed)
                    shuffled = self.game(mode=mode, seed=seed, randomize_feature_assignment=True)
                    self.assertEqual(legacy.goal_person, shuffled.goal_person)
                    self.assertEqual(legacy.goal, shuffled.goal)
                    self.assertEqual(legacy.glyphs, shuffled.glyphs)
                    self.assertEqual(legacy.rng.getstate(), shuffled.rng.getstate())
                    self.assertEqual(legacy.json_schemas, shuffled.json_schemas)
                    for before, after in zip(legacy.agents, shuffled.agents):
                        self.assertEqual(
                            before.model_dump(exclude={"known_feature", "known_value"}),
                            after.model_dump(exclude={"known_feature", "known_value"}),
                        )
                        self.assertEqual([f.name for f in after.features_view], shuffled.goal.feature_names)
                    self.assertEqual(shuffled.goal.feature_names, [f.name for f in FEATURES])

    def test_prompt_explains_randomization_without_revealing_other_clues_or_seed(self):
        game = self.game(seed=98765, randomize_feature_assignment=True)
        self.assertNotEqual(self.assignments(game), game.goal.feature_names)
        for agent in game.agents:
            prompt = game.system_prompts[agent.agent_id]
            self.assertIn("Feature ownership is randomized independently of the order of the feature list.", prompt)
            self.assertIn("Each of the 8 agents knows one different feature", prompt)
            self.assertIn("Agent IDs do not indicate which feature an agent knows.", prompt)
            self.assertIn("the assignments of the other agents are not revealed to you.", prompt)
            private_clues = re.findall(r"^  (\w+) = (\w+)$", prompt, flags=re.MULTILINE)
            self.assertEqual(private_clues, [(agent.known_feature, agent.known_value)])
            self.assertNotIn("98765", prompt)
            self.assertNotIn("feature-assignment:v1", prompt)
            self.assertNotIn(str(self.assignments(game)), prompt)
            for other in game.agents:
                self.assertNotRegex(prompt, rf"{other.agent_id}\s*[:=]\s*{other.known_feature}")

    def test_legacy_config_uses_original_round_robin_and_prompt(self):
        for count in (3, 8, 11):
            with self.subTest(n_agents=count):
                game = self.game(n_agents=count)
                self.assertFalse(game.config.randomize_feature_assignment)
                expected = [game.goal.feature_names[i % len(FEATURES)] for i in range(count)]
                self.assertEqual(self.assignments(game), expected)
                for prompt in game.system_prompts.values():
                    self.assertNotIn("FEATURE OWNERSHIP", prompt)
                    self.assertNotIn("Feature ownership is randomized", prompt)

    def test_unequal_agent_counts_cycle_permutation_without_losing_coverage(self):
        complete = self.game(seed=123, randomize_feature_assignment=True)
        permutation = self.assignments(complete)
        for count in (1, 3, 11, 17):
            with self.subTest(n_agents=count):
                game = self.game(seed=123, n_agents=count, randomize_feature_assignment=True)
                self.assertEqual(self.assignments(game), [permutation[i % 8] for i in range(count)])
                if count < 8:
                    self.assertEqual(len(set(self.assignments(game))), count)
                    self.assertIn("some features are not known by any agent", game.system_prompts["agent_0"])
                else:
                    self.assertEqual(set(self.assignments(game)), set(permutation))
                    self.assertIn("some agents know the same feature", game.system_prompts["agent_0"])

    def test_none_seed_uses_system_entropy_for_assignment_rng(self):
        # Inspect the assignment RNG constructor without probabilistic assertions about its output.
        import random
        original_random = random.Random
        with patch("src.gameplay.play_game.random.Random", wraps=original_random) as rng:
            self.game(seed=None, randomize_feature_assignment=True)
        # The game, goal selection, and ownership each request independent entropy.
        self.assertEqual([call.args for call in rng.call_args_list], [(None,), (None,), (None,)])

    def test_default_score_interval_is_sixty_seconds(self):
        game = self.game(randomize_feature_assignment=True)
        self.assertEqual(game.config.score_interval_s, 60)
        self.assertIn("Every 60 seconds", game.system_prompts["agent_0"])


if __name__ == "__main__":
    unittest.main()
