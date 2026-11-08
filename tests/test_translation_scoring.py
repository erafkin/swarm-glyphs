import json
import tempfile
import unittest
from pathlib import Path

from src.core.translation_scoring import bleu, parse_translation, rouge, score_run, type_token_ratio, zipf


class TranslationScoringTests(unittest.TestCase):
    def test_exact_translation_scores_one(self):
        text = ["the four positions have values two seven four eight"]
        self.assertAlmostEqual(bleu(text, text), 1.0, places=6)
        scores = rouge(text, text)
        self.assertEqual(scores, {"rouge1": 1.0, "rouge2": 1.0, "rougeL": 1.0})

    def test_transcript_stats(self):
        tokens = ["du"] * 3 + ["ud"] * 2 + ["zux"]
        self.assertAlmostEqual(type_token_ratio(tokens), 0.5)
        fit = zipf(tokens)
        self.assertLess(fit["slope"], 0)
        self.assertGreaterEqual(fit["r_squared"], 0)

    def test_translation_section_stops_before_later_citations(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "translation.txt"
            path.write_text("[1] hello there\\n[2] second line\\n\\n3. THE TASK\\n\\nSee [1] again.\\n")
            self.assertEqual(parse_translation(path), {1: "hello there", 2: "second line"})

    def test_score_run_pairs_intended_meaning_with_translation(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            task, monitor = root / "task", root / "monitor"
            task.mkdir()
            monitor.mkdir()
            (task / "task_chatroom.jsonl").write_text("\n".join([
                json.dumps({"sender": "task", "text": "{\"stage\":0}"}),
                json.dumps({"sender": "agent_0", "text": "zux du ud"}),
            ]) + "\n")
            (task / "agent_calls.jsonl").write_text(json.dumps({
                "public_message_id": 2, "intended_meaning": "I define the symbol.",
            }) + "\n")
            (task / "swarmish.txt").write_text("zux means a header\n")
            (monitor / "translation.txt").write_text("[1] status\\n[2] I define the symbol.\\n\\n3. THE TASK\\n\\n")
            (monitor / "reconstructed_swarmish.txt").write_text("zux means a header\n")
            report = score_run(task, monitor, models=False)
        self.assertEqual(report["n_paired"], 1)
        self.assertAlmostEqual(report["translation"]["bleu"], 1.0, places=6)
        self.assertEqual(report["swarmish"]["tokens"], 3)
        self.assertNotIn("bert_perplexity", report["swarmish"])


if __name__ == "__main__":
    unittest.main()
