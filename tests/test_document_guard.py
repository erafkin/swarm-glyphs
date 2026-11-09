"""Round 1 refuses a document whose glyphs are mostly not the inventory's, and says so in the chat."""
import json
import tempfile
import unittest
from types import SimpleNamespace
from unittest.mock import AsyncMock, patch

from openai.types.chat import ChatCompletion

from src.core.potential_glyphs import glyph_report, is_corrupted_document
from src.enc_dec.config import LanguageExperimentConfig
from src.enc_dec.run import LanguageExperiment

TANGUT = [chr(0x17000 + i) for i in range(200)]
GARBAGE = " ".join(chr(0x0F10 + i) + chr(0x0F11 + i) for i in range(40))  # Tibetan, as Grok's escapes decoded


def completion(text):
    return ChatCompletion.model_validate({
        "id": "offline", "object": "chat.completion", "created": 0, "model": "offline-model",
        "choices": [{"index": 0, "message": {"role": "assistant", "content": text}, "finish_reason": "stop"}],
        "usage": {"prompt_tokens": 10, "completion_tokens": 5, "total_tokens": 15, "cost": 0.01},
    })


class GuardFunctionTests(unittest.TestCase):
    def test_all_glyphs_outside_inventory_is_corrupted(self):
        self.assertTrue(is_corrupted_document("WORDS\n" + GARBAGE, TANGUT))
        self.assertEqual(glyph_report(GARBAGE, TANGUT), (80, 0))

    def test_inventory_glyphs_with_a_few_strays_are_fine(self):
        doc = "WORDS\n" + " ".join(TANGUT[:60]) + " " + chr(0x18000) + chr(0x18001)
        self.assertFalse(is_corrupted_document(doc, TANGUT))
        self.assertEqual(glyph_report(doc, TANGUT), (62, 60))

    def test_prose_punctuation_and_replacement_char_do_not_count(self):
        doc = "Don’t “spell” English — use ⊘ for dropped text, → means next, and � marks a broken glyph." * 5
        self.assertEqual(glyph_report(doc, TANGUT)[0], 0)
        self.assertFalse(is_corrupted_document(doc, TANGUT))

    def test_unrepaired_mojibake_counts_as_corruption(self):
        mojibake = " ".join(TANGUT[:30]).encode("utf-8").decode("latin-1")
        self.assertTrue(is_corrupted_document("WORDS\n" + mojibake, TANGUT))

    def test_short_or_latin_documents_never_trigger(self):
        self.assertFalse(is_corrupted_document(chr(0x0F10) * 19, TANGUT))
        latin = [*"abcdefghijklmnopqrstuvwxyz0123456789"]
        self.assertFalse(is_corrupted_document("the quick brown fox " * 20, latin))


class GuardInRoundOneTests(unittest.IsolatedAsyncioTestCase):
    async def test_corrupted_edit_is_refused_and_announced(self):
        logs = tempfile.TemporaryDirectory(prefix="guard-offline-")
        self.addCleanup(logs.cleanup)
        config = LanguageExperimentConfig(glyph_dictionary="glyphs_tangut", n_glyphs=200, n_agents=2, log_dir=logs.name,
                                          language_minutes=30, task_minutes=0.05, min_turn_interval_s=60, model="offline-model",
                                          task_prompt="TASK", max_tokens=100, temperature=0)
        experiment = LanguageExperiment(config, creation_only=True)
        good = "WORDS\n" + " ".join(experiment.glyphs[:40])

        async def create(**kwargs):
            system = kwargs["messages"][0]["content"]
            agent_id = system.split(",", 1)[0].removeprefix("You are ")
            if "response_format" not in kwargs:
                return completion(f"DOC-{agent_id}")
            doc = GARBAGE if agent_id == "agent_0" else good
            return completion(json.dumps({"message": f"hello from {agent_id}", "language_document": doc, "done": True}))

        client = SimpleNamespace(chat=SimpleNamespace(completions=SimpleNamespace(create=AsyncMock(side_effect=create))), close=AsyncMock())
        with patch("src.enc_dec.run.make_client", return_value=client):
            await experiment.run()

        calls = [json.loads(l) for l in (experiment.logger.path / "agent_calls.jsonl").read_text().splitlines()]
        by_agent = {c["agent_id"]: c for c in calls if c["phase"] == "creation"}
        self.assertEqual(by_agent["agent_0"]["document_rejected"]["reason"], "glyphs_outside_inventory")
        self.assertEqual(by_agent["agent_0"]["document_rejected"]["inventory_glyphs"], 0)
        self.assertNotIn("document_rejected", by_agent["agent_1"])
        self.assertTrue(by_agent["agent_0"]["state_applied"] and by_agent["agent_0"]["done"])
        chat = [json.loads(l) for l in (experiment.logger.path / "chatroom.jsonl").read_text().splitlines()]
        notices = [m for m in chat if m["sender"] == "system"]
        self.assertEqual(len(notices), 1)
        self.assertIn("agent_0's edit to swarmish.txt was not applied: 80 of its 80 glyph characters", notices[0]["text"])
        self.assertEqual([m["text"] for m in chat if m["sender"] != "system"], ["hello from agent_0", "hello from agent_1"])
        applied = [c["language_document"] for c in calls if c["phase"] == "creation" and c.get("language_document")]
        self.assertTrue(all(doc == good for doc in applied), applied)
        self.assertEqual(experiment.creation_stop_reason, "all_done")


if __name__ == "__main__":
    unittest.main()
