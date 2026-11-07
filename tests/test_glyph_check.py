"""Offline checks for the chat glyph filter and the no-spaces variant."""

import tempfile
import unittest
from pathlib import Path

from src.agent_models.potential_glyphs import is_glyph_only
from src.agent_models.prompts import LANGUAGE_INSTRUCTION, build_final_interview_system_prompt
from src.config import GameConfig
from src.gameplay.play_game import Game

REPO_ROOT = Path(__file__).resolve().parents[1]
GLYPHS = ["𘜎", "𗄌"]
IDS = [f"agent_{i}" for i in range(11)]


class GlyphCheckTests(unittest.TestCase):
    def test_spaces_allowed_by_default(self):
        self.assertTrue(is_glyph_only("𘜎 𗄌 agent_1", IDS, GLYPHS))
        self.assertTrue(is_glyph_only("𘜎agent_10𗄌", IDS, GLYPHS))
        self.assertFalse(is_glyph_only("𘜎 a", IDS, GLYPHS))
        self.assertFalse(is_glyph_only("𘜎\n𗄌", IDS, GLYPHS))

    def test_no_spaces_allows_only_glyphs(self):
        self.assertTrue(is_glyph_only("𘜎𗄌", IDS, GLYPHS, allow_spaces=False))
        for text in ["𘜎 𗄌", "agent_1𘜎𗄌", "𘜎agent_1𗄌", "agent_3", "𘜎a"]:
            with self.subTest(text=text):
                self.assertFalse(is_glyph_only(text, IDS, GLYPHS, allow_spaces=False))

    def test_language_instruction_is_off_by_default_and_on_for_board_runs(self):
        scripts = REPO_ROOT / "src/scripts"
        self.assertFalse(GameConfig().language_instruction)
        self.assertFalse(GameConfig.from_file(scripts / "features_seed0.json").language_instruction)
        with tempfile.TemporaryDirectory() as logs:
            for name, expected in [("board_seed0.json", True), ("features_seed0.json", False)]:
                config = GameConfig.from_file(scripts / name).model_copy(update={"log_dir": logs})
                prompt = Game(config).system_prompts["agent_0"]
                self.assertEqual(LANGUAGE_INSTRUCTION in prompt, expected, name)

    def test_no_spaces_board_config_only_changes_spaces_and_prompts_say_so(self):
        scripts = REPO_ROOT / "src/scripts"
        base = GameConfig.from_file(scripts / "board_seed0.json")
        no_spaces = GameConfig.from_file(scripts / "board_seed0_no_spaces.json")
        self.assertTrue(base.allow_spaces)
        self.assertEqual(no_spaces.model_dump(), base.model_copy(update={"allow_spaces": False}).model_dump())

        with tempfile.TemporaryDirectory() as logs:
            game = Game(no_spaces.model_copy(update={"log_dir": logs}))
            prompt = game.system_prompts["agent_0"]
            self.assertIn("contain these glyphs, with no spaces or agent IDs:", prompt)
            self.assertIn("(letters, digits, punctuation, other symbols, spaces, agent IDs)", prompt)
            self.assertNotIn("spaces, and agent IDs", prompt)
            self.assertIn("The glyphs have no predefined meaning.\n" + LANGUAGE_INSTRUCTION, prompt)
            interview = build_final_interview_system_prompt(game.agents[0], game.board, allow_spaces=False)
            self.assertIn("Spaces and agent IDs were not allowed", interview)
            self.assertNotIn("or agent IDs", interview)


if __name__ == "__main__":
    unittest.main()
