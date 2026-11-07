"""Offline run of both chat modes: language file, fresh task team, and the four monitor briefings."""

import json
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import AsyncMock, patch

from openai.types.chat import ChatCompletion

from src.core.potential_glyphs import dictionary_path, load_dictionary
from src.enc_dec.config import LanguageExperimentConfig
from src.enc_dec.prompts import MONITOR_CONDITIONS
from src.enc_dec.run import LanguageExperiment

REPO_ROOT = Path(__file__).resolve().parents[1]
TASK = "TRUE_TASK_ALPHA"
FAR = "FAR_TASK_BETA"
NEAR = "NEAR_TASK_GAMMA"


def completion(text):
    return ChatCompletion.model_validate({
        "id": "offline-completion",
        "object": "chat.completion",
        "created": 0,
        "model": "offline-model",
        "choices": [{"index": 0, "message": {"role": "assistant", "content": text}, "finish_reason": "stop"}],
        "usage": {"prompt_tokens": 10, "completion_tokens": 5, "total_tokens": 15, "cost": 0.01},
    })


class LanguageRoundTests(unittest.IsolatedAsyncioTestCase):
    def config(self, chat_mode, log_dir):
        return LanguageExperimentConfig(
            chat_mode=chat_mode,
            n_agents=2,
            log_dir=log_dir,
            language_minutes=30,
            task_minutes=0.05,
            min_turn_interval_s=60,
            model="offline-model",
            task_prompt=TASK,
            wrong_task_far=FAR,
            wrong_task_near=NEAR,
            max_tokens=100,
            temperature=0,
        )

    def records(self, experiment, stream):
        path = experiment.logger.path / f"{stream}.jsonl"
        return [json.loads(line) for line in path.read_text().splitlines()]

    async def run_mode(self, chat_mode, **updates):
        logs = tempfile.TemporaryDirectory(prefix="language-offline-")
        self.addCleanup(logs.cleanup)
        experiment = LanguageExperiment(self.config(chat_mode, logs.name).model_copy(update=updates))
        task_message = "TASK FREE" if chat_mode == "free" else experiment.glyphs[0]

        async def create(**kwargs):
            system = kwargs["messages"][0]["content"]
            agent_id = system.split(",", 1)[0].removeprefix("You are ")
            if "response_format" not in kwargs:
                if "Write the language document" in system:
                    return completion(f"DOC-{agent_id}")
                return completion("I think the language marks each word with the first glyph.")
            required = kwargs["response_format"]["json_schema"]["schema"]["required"]
            if "done" in required:
                body = {"message": "ENGLISH PLAN", "language_document": "SHARED DOC", "done": True}
            else:
                body = {"scratchpad": "notes", "message": task_message, "answer": "ready"}
            return completion(json.dumps(body))

        client = SimpleNamespace(
            chat=SimpleNamespace(completions=SimpleNamespace(create=AsyncMock(side_effect=create))),
            close=AsyncMock(),
        )
        with patch("src.enc_dec.run.make_client", return_value=client):
            await experiment.run()
        return experiment

    async def test_glyphs_mode_plans_in_english_and_task_chat_is_language_plus_feedback(self):
        experiment = await self.run_mode("glyphs")
        self.assertEqual(experiment.creation_stop_reason, "all_done")
        self.assertEqual(experiment.task_stop_reason, "time_limit")
        self.assertEqual(set(experiment.glyphs), set(load_dictionary(dictionary_path("dictionary_a"))))

        language = (experiment.logger.path / "language.txt").read_text()
        self.assertIn("DOC-agent_0", language)
        self.assertIn("DOC-agent_1", language)
        creation_chat = self.records(experiment, "chatroom")
        self.assertEqual([m["text"] for m in creation_chat], ["ENGLISH PLAN", "ENGLISH PLAN"])
        self.assertFalse(any(m["is_violation"] for m in creation_chat))
        self.assertNotIn("DOC-", json.dumps(creation_chat))

        task_prompt = experiment.task_prompts["agent_0"]
        self.assertIn("DOC-agent_0", task_prompt)
        self.assertIn(TASK, task_prompt)
        self.assertNotIn("ENGLISH PLAN", task_prompt)
        self.assertIn("You did not create the language", task_prompt)
        creation_prompt = experiment.creation_prompts["agent_0"]
        self.assertIn("ordinary English", creation_prompt)
        self.assertIn("the most recent 100 messages and the current\nlanguage.txt", creation_prompt)
        self.assertNotIn("scratchpad", creation_prompt)
        self.assertNotIn(TASK, creation_prompt)
        creation_turns = [r for r in self.records(experiment, "agent_calls") if r["phase"] == "creation"]
        self.assertTrue(creation_turns)
        for turn in creation_turns:
            self.assertIn("CURRENT LANGUAGE DOCUMENT (language.txt):", turn["turn_prompt"])
            self.assertNotIn("SCRATCHPAD", turn["turn_prompt"])
        doc_prompts = [r["prompt"] for r in self.records(experiment, "language_document")]
        self.assertTrue(any("SHARED DOC" in prompt and "ENGLISH PLAN" in prompt for prompt in doc_prompts))

        task_chat = self.records(experiment, "task_chatroom")
        self.assertEqual(sorted(m["sender"] for m in task_chat[:2]), ["agent_0", "agent_1"])
        self.assertEqual(task_chat[-1]["sender"], "task")
        self.assertEqual([m["text"] for m in task_chat[:2]], [experiment.glyphs[0], experiment.glyphs[0]])
        self.assertIn("Task feedback: 2 of 2", task_chat[-1]["text"])
        task_dump = json.dumps(task_chat)
        self.assertNotIn("ENGLISH PLAN", task_dump)
        self.assertNotIn("DOC-", task_dump)
        self.assertNotIn("ready", task_dump)
        answers = json.loads((experiment.logger.path / "task_answers.json").read_text())
        self.assertEqual(answers, {"agent_0": "ready", "agent_1": "ready"})

        monitors = self.records(experiment, "monitor")
        self.assertEqual({m["condition"] for m in monitors}, set(MONITOR_CONDITIONS))
        by_condition = {m["condition"]: m["prompt"] for m in monitors}
        self.assertIn(TASK, by_condition["knows_task"])
        self.assertNotIn(TASK, by_condition["unknown_task"])
        self.assertIn(FAR, by_condition["wrong_task_far"])
        self.assertNotIn(TASK, by_condition["wrong_task_far"])
        self.assertIn(NEAR, by_condition["wrong_task_near"])
        self.assertNotIn(TASK, by_condition["wrong_task_near"])
        for prompt in by_condition.values():
            self.assertIn(experiment.glyphs[0], prompt)
            self.assertIn("Task feedback:", prompt)
            self.assertNotIn("DOC-", prompt)
            self.assertNotIn("ENGLISH PLAN", prompt)

    async def test_free_mode_posts_any_characters(self):
        experiment = await self.run_mode("free")
        self.assertEqual(experiment.glyphs, [])
        chat = self.records(experiment, "chatroom")
        self.assertEqual([m["text"] for m in chat], ["ENGLISH PLAN", "ENGLISH PLAN"])
        self.assertFalse(any(m["is_violation"] for m in chat))
        task_chat = self.records(experiment, "task_chatroom")
        self.assertEqual([m["text"] for m in task_chat[:2]], ["TASK FREE", "TASK FREE"])
        self.assertEqual(task_chat[-1]["sender"], "task")
        self.assertEqual(len(self.records(experiment, "monitor")), 4)

    async def test_task_feedback_can_be_left_out_of_the_chat(self):
        experiment = await self.run_mode("free", task_feedback=False)
        task_chat = self.records(experiment, "task_chatroom")
        self.assertTrue(task_chat)
        self.assertNotIn("task", [m["sender"] for m in task_chat])
        self.assertNotIn("Task feedback:", json.dumps(task_chat))
        prompt = experiment.task_prompts["agent_0"]
        self.assertIn("The task does not post status updates to the chat.", prompt)
        self.assertNotIn("posts feedback", prompt)
        for monitor in self.records(experiment, "monitor"):
            self.assertNotIn("Task feedback:", monitor["prompt"])

    def test_shipped_configs_differ_only_by_chat_mode_and_use_the_whole_dictionary(self):
        scripts = REPO_ROOT / "src/enc_dec/scripts"
        glyphs = LanguageExperimentConfig.from_file(scripts / "language_glyphs.json")
        free = LanguageExperimentConfig.from_file(scripts / "language_free.json")
        self.assertIsNone(glyphs.n_glyphs)
        self.assertEqual(free.model_dump(), glyphs.model_copy(update={"chat_mode": "free"}).model_dump())
        self.assertIn("PLACEHOLDER TASK", glyphs.task_prompt)


if __name__ == "__main__":
    unittest.main()
