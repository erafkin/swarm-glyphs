"""Offline launch checks using the real API adapter with a simulated SDK client."""

import json
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import AsyncMock, patch

from openai.types.chat import ChatCompletion

from src.guess_who.config import GameConfig
from src.guess_who.play_game import Game


REPO_ROOT = Path(__file__).resolve().parents[1]


def completion(text):
    # Exercise SDK preservation of OpenRouter's extra usage.cost field.
    return ChatCompletion.model_validate({
        "id": "offline-completion",
        "object": "chat.completion",
        "created": 0,
        "model": "offline-model",
        "choices": [{"index": 0, "message": {"role": "assistant", "content": text},
                     "finish_reason": "stop"}],
        "usage": {"prompt_tokens": 100, "completion_tokens": 50,
                  "total_tokens": 150, "cost": 0.01},
    })


class FeaturesLaunchTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.logs = tempfile.TemporaryDirectory(prefix="features-offline-")
        self.addCleanup(self.logs.cleanup)
        launch = GameConfig.from_file(REPO_ROOT / "src/guess_who/scripts/features_seed0.json")
        self.config = launch.model_copy(update={
            "log_dir": self.logs.name,
            "score_interval_s": 0.02,
            "min_turn_interval_s": 60,
            "max_score_rounds": 2,
        })
        self.game = Game(self.config)

    def records(self, stream):
        return [json.loads(line) for line in
                (self.game.logger.path / f"{stream}.jsonl").read_text().splitlines()]

    def fake_client(self, response_for_agent):
        async def create(**kwargs):
            if "response_format" not in kwargs:
                return completion("Offline interview explanation.")
            agent_id = kwargs["messages"][0]["content"].split(",", 1)[0].removeprefix("You are ")
            return completion(response_for_agent(agent_id))

        self.create = AsyncMock(side_effect=create)
        return SimpleNamespace(chat=SimpleNamespace(completions=SimpleNamespace(create=self.create)),
                               close=AsyncMock())

    async def run_with(self, client):
        with patch("src.guess_who.play_game.make_client", return_value=client):
            await self.game.run()
        client.close.assert_awaited_once()
        self.assertFalse((self.game.logger.path / "errors.jsonl").exists())

    def test_private_clues_and_schema_match_eight_by_four_features_mode(self):
        self.assertEqual(self.config.mode, "features")
        self.assertIsNone(self.game.board)
        self.assertEqual(len(self.game.agents), 8)
        self.assertEqual({a.known_feature for a in self.game.agents}, set(self.game.goal.values))
        self.assertEqual(len(self.game.glyphs), 18)
        for agent in self.game.agents:
            prompt = self.game.system_prompts[agent.agent_id]
            self.assertIn(f"You know:\n  {agent.known_feature} = {agent.known_value}", prompt)
            self.assertEqual(agent.known_value, self.game.goal.values[agent.known_feature])
            self.assertNotIn("BOARD (", prompt)
            schema = self.game.json_schemas[agent.agent_id]["schema"]
            self.assertEqual(set(schema["required"]), {"scratchpad", "message", "guess"})
            guesses = schema["properties"]["guess"]
            self.assertEqual(set(guesses["required"]), set(self.game.goal.values))
            for feature in self.game.goal.features:
                self.assertEqual(set(guesses["properties"][feature.name]["enum"]), set(feature.options))
                self.assertEqual(len(feature.options), 4)

    async def test_all_correct_run_scores_wins_interviews_and_logs_cost(self):
        response = json.dumps({"scratchpad": "private state", "message": self.game.glyphs[0],
                               "guess": self.game.goal.values})
        client = self.fake_client(lambda _: response)
        await self.run_with(client)

        self.assertEqual(self.game.stop_reason, "win_threshold_reached")
        self.assertEqual([a.turn_count for a in self.game.agents], [1] * 8)
        self.assertEqual(len(self.records("agent_calls")), 8)
        self.assertEqual(len(self.records("final_interviews")), 8)
        scores = self.records("scores")
        self.assertEqual(len(scores), 1)
        self.assertEqual(scores[0]["feature_accuracy"], {f: 1.0 for f in self.game.goal.values})
        self.assertEqual(scores[0]["fully_correct_rate"], 1.0)
        self.assertEqual(scores[0]["feature_chance"], {f: 0.34375 for f in self.game.goal.values})
        self.assertEqual(scores[0]["fully_correct_chance"], 1 / 16384)
        self.assertIsNone(scores[0]["person_accuracy"])
        self.assertAlmostEqual(self.game.total_cost_usd, 0.16)
        summary = json.loads((self.game.logger.path / "summary.json").read_text())
        self.assertEqual(summary["stop_reason"], "win_threshold_reached")
        self.assertEqual(summary["score_rounds"], 1)
        self.assertEqual(summary["total_cost_usd"], 0.16)
        self.assertFalse((self.game.logger.path / "board.json").exists())
        for call in self.create.call_args_list:
            self.assertNotIn("temperature", call.kwargs)
            if "response_format" in call.kwargs:
                self.assertEqual(call.kwargs["max_tokens"], 16000)
                self.assertEqual(call.kwargs["extra_body"]["reasoning"], {"effort": "medium"})
                self.assertTrue(call.kwargs["response_format"]["json_schema"]["strict"])
            else:
                self.assertEqual(call.kwargs["max_tokens"], 16000)
                self.assertEqual(call.kwargs["extra_body"]["reasoning"], {"effort": "medium"})
                interview_system = call.kwargs["messages"][0]["content"]
                self.assertIn("ordinary English prose, not JSON", interview_system)
                self.assertNotIn("Respond with a single JSON object", interview_system)
                self.assertNotIn("SCORING", interview_system)
        for interview in self.records("final_interviews"):
            self.assertEqual(interview["reasoning_effort"], "medium")
            self.assertEqual(interview["max_tokens"], 16000)
            self.assertIn("ordinary English prose, not JSON", interview["system_prompt"])

    async def test_interview_inherits_effort_and_respects_smaller_gameplay_cap(self):
        self.config.max_tokens = 1200
        self.config.reasoning_effort = "high"
        self.config.final_interview_reasoning_effort = None
        client = self.fake_client(lambda _: self.fail("interview requested gameplay output"))
        await self.game.final_interview(client)
        self.assertEqual(self.create.await_count, 8)
        for call in self.create.call_args_list:
            self.assertNotIn("response_format", call.kwargs)
            self.assertEqual(call.kwargs["max_tokens"], 1200)
            self.assertEqual(call.kwargs["extra_body"]["reasoning"], {"effort": "high"})
        self.assertEqual([a.turn_count for a in self.game.agents], [0] * 8)
        self.assertEqual(len(self.game.chatroom), 0)

    async def test_board_interview_includes_board_and_scoring_context(self):
        self.game = Game(self.config.model_copy(update={"mode": "board"}))
        client = self.fake_client(lambda _: self.fail("interview requested gameplay output"))
        await self.game.final_interview(client)
        for call, agent in zip(self.create.call_args_list, self.game.agents):
            system_prompt = call.kwargs["messages"][0]["content"]
            self.assertIn("a guess counted as correct only if every feature matched", system_prompt)
            self.assertIn(self.game.board.render(agent.board_order), system_prompt)
            self.assertIn("ordinary English prose, not JSON", system_prompt)
            self.assertNotIn("Respond with a single JSON object", system_prompt)

    async def test_board_mode_scores_full_feature_guesses_as_person_accuracy(self):
        self.config.final_interview = False
        self.game = Game(self.config.model_copy(update={"mode": "board"}))
        for agent in self.game.agents:
            prompt = self.game.system_prompts[agent.agent_id]
            self.assertIn(self.game.board.render(agent.board_order), prompt)
            self.assertNotIn("person_guess", json.dumps(self.game.json_schemas[agent.agent_id]))

        def response(agent_id):
            labels = dict(self.game.goal.values)
            if agent_id == "agent_7":
                labels["expression"] = next(o for o in self.game.goal.features[-1].options if o != labels["expression"])
            return json.dumps({"scratchpad": "", "message": self.game.glyphs[0], "guess": labels})

        await self.run_with(self.fake_client(response))
        self.assertEqual(self.game.stop_reason, "max_score_rounds_reached")
        scores = self.records("scores")
        self.assertEqual(scores[-1]["person_correct"], 7)
        self.assertEqual(scores[-1]["person_accuracy"], 7 / 8)
        feedback = [m["text"] for m in self.records("chatroom") if m["sender"] == "system"]
        self.assertEqual(feedback[-1], "Score round 2: 7 of 8 agents (88%) guessed the correct person.")

    async def test_partial_accuracy_feedback_and_glyph_violation_do_not_win(self):
        self.config.final_interview = False

        def response(agent_id):
            labels = dict(self.game.goal.values)
            if int(agent_id.rsplit("_", 1)[1]) >= 4:
                labels["hair_colour"] = "black"
            return json.dumps({"scratchpad": "PRIVATE_MARKER", "guess": labels,
                               "message": "NOT_ALLOWED" if agent_id == "agent_0" else self.game.glyphs[0]})

        await self.run_with(self.fake_client(response))
        self.assertEqual(self.game.stop_reason, "max_score_rounds_reached")
        scores = self.records("scores")
        self.assertEqual(len(scores), 2)
        self.assertEqual(scores[-1]["feature_accuracy"]["hair_colour"], 0.5)
        self.assertEqual(scores[-1]["fully_correct_rate"], 0.5)
        for name, accuracy in scores[-1]["feature_accuracy"].items():
            if name != "hair_colour":
                self.assertEqual(accuracy, 1.0)
        chat = self.records("chatroom")
        agent_zero = next(message for message in chat if message["sender"] == "agent_0")
        self.assertEqual(agent_zero["text"], "⊘")
        self.assertTrue(agent_zero["is_violation"])
        self.assertNotIn("NOT_ALLOWED", json.dumps(chat))
        self.assertNotIn("PRIVATE_MARKER", json.dumps(chat))
        feedback = [m["text"] for m in chat if m["sender"] == "system"]
        self.assertIn("hair_colour 50%", feedback[-1])
        self.assertIn("Agents with every feature correct: 50%", feedback[-1])
        self.assertFalse((self.game.logger.path / "final_interviews.jsonl").exists())


if __name__ == "__main__":
    unittest.main()
