import json
import hashlib
import importlib.util
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from src.core.translation_scoring import (
    bleu, decoded_sections, load_reference, model_provenance, parse_numbered_translation,
    parse_translation, rouge, score_reference_run, score_run, type_token_ratio, zipf,
)


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

    def test_decoded_file_splits_language_and_translation(self):
        plain = "1. SWARMISH.TXT, RECONSTRUCTED\n\nglyph means word\n\n2. TRANSLATION\n\n1. first message\n2. second message\n\n3. THE TASK\n\nSee 1 again.\n"
        language, section = decoded_sections(plain)
        self.assertIn("glyph means word", language)
        self.assertNotIn("THE TASK", section)
        self.assertEqual(parse_numbered_translation(section), {1: "first message", 2: "second message"})
        marked = "# 1. SWARMISH.TXT, RECONSTRUCTED\n\nref\n\n# 2. TRANSLATION\n\n**1. [agent_0]** hello there\n\n# 3. THE TASK\n"
        self.assertEqual(parse_numbered_translation(decoded_sections(marked)[1]), {1: "hello there"})
        brackets = "1. SWARMISH.TXT, RECONSTRUCTED\n\nref\n\n2. TRANSLATION\n\n[1] status line\n[2] second line\n\n3. THE TASK\n"
        self.assertEqual(parse_numbered_translation(decoded_sections(brackets)[1]), {1: "status line", 2: "second line"})

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


class PublicReferenceScoringTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.transcript = self.root / "task_chatroom.jsonl"
        self.reference = self.root / "reference.json"
        self.language = self.root / "swarmish.txt"
        self.decoded = self.root / "decoded_swarmish.txt"

    def fixture(self):
        rows = [
            {"sender": "task", "text": "status is public", "english": "status is public", "confidence": "high"},
            {"sender": "agent_0", "text": "glyph-a", "english": "open the red door", "confidence": "high"},
            {"sender": "agent_1", "text": "⊘", "english": "Unknown: message discarded for using characters outside the permitted set.", "confidence": "unknown"},
            {"sender": "agent_0", "text": "glyph-b", "english": "move the blue lever", "confidence": "medium"},
            {"sender": "agent_0", "text": "glyph-c", "english": "Unknown.", "confidence": "unknown"},
            {"sender": "agent_1", "text": "glyph-d", "english": "close the left door", "confidence": "high"},
        ]
        self.transcript.write_text("\n".join(json.dumps({k: r[k] for k in ("sender", "text")}) for r in rows) + "\n")
        self.language.write_text("frozen glossary")
        rendered = "\n".join(f"[{i}] [{r['sender']}] {r['text']}" for i, r in enumerate(rows, 1))
        document = {
            "status": "draft_reference_translation", "private_annotations_used": False,
            "source_transcript_sha256": hashlib.sha256(self.transcript.read_bytes()).hexdigest(),
            "rendered_public_transcript_sha256": hashlib.sha256(rendered.encode()).hexdigest(),
            "language_sha256": hashlib.sha256(self.language.read_bytes()).hexdigest(),
            "messages": [{"id": i, **r} for i, r in enumerate(rows, 1)],
        }
        self.reference.write_text(json.dumps(document))
        self.decoded.write_text("1. LANGUAGE\nSee [999].\n2. TRANSLATION\n[1] status is public\n[2] open the red door\n[3] discarded\n[5] a guess about an unknown reference\n[6] Unknown.\n3. THE TASK\n[77] unrelated citation\n")
        return document

    def test_three_number_styles_and_section_boundaries(self):
        self.decoded.write_text("1. LANGUAGE\n[88] citation\n## 2. TRANSLATION\n[1] first line\ncontinued here\n2) second line\n**3. [agent_0]** third line\n**[4]** fourth line\n## 3. THE TASK\n[2] citation\n")
        self.assertEqual(parse_translation(self.decoded, {1, 2, 3, 4}, require_section=True), {
            1: "first line continued here", 2: "second line", 3: "third line", 4: "fourth line"})
        original = parse_translation(self.decoded, require_section=True, strip_prefixes=False)
        self.assertEqual(original[3], "[agent_0]** third line")

    def test_confidence_prefixes_require_explicit_definition(self):
        self.decoded.write_text("2. TRANSLATION\nConfidence applies per entry.\n1. H: open the door\n2. M, public: blue lever\n")
        self.assertEqual(parse_translation(self.decoded), {1: "open the door", 2: "blue lever"})
        self.decoded.write_text("2. TRANSLATION\n[1] H: structural frame\n[2] K: another frame\n")
        self.assertEqual(parse_translation(self.decoded)[1], "H: structural frame")

    def test_reject_duplicate_out_of_range_and_missing_section(self):
        for content in ("2. TRANSLATION\n[1] a\n1. b", "2. TRANSLATION\n[2] b", "2. TRANSLATION\n[0] a"):
            with self.subTest(content=content):
                self.decoded.write_text(content)
                with self.assertRaises(ValueError):
                    parse_translation(self.decoded, {1}, require_section=True)
        self.decoded.write_text("[1] a bare legacy translation")
        with self.assertRaisesRegex(ValueError, "No TRANSLATION"):
            parse_translation(self.decoded, require_section=True)

    def test_missing_unknown_and_exclusions_keep_global_ids(self):
        self.fixture()
        # A poisoned private log proves this mode does not read intended meanings.
        (self.root / "agent_calls.jsonl").write_text("not json; do not read private evidence")
        report = score_reference_run(self.reference, self.transcript, self.decoded, language_path=self.language)
        summary = report["summary"]
        self.assertEqual(summary["eligible"], 4)
        self.assertEqual(summary["scorable_references"], 3)
        self.assertEqual(summary["unknown_references"], 1)
        self.assertEqual(summary["missing_predictions"], 1)
        self.assertEqual(summary["unknown_only_predictions"], 1)
        self.assertEqual(summary["valid_pairs"], 1)
        self.assertAlmostEqual(summary["mean_per_line"]["rougeL"], 1 / 3)
        self.assertEqual(summary["valid_pair_mean"]["rougeL"], 1)
        self.assertEqual(report["high_confidence"]["prediction_coverage"], 0.5)
        self.assertEqual(report["coverage"]["high_confidence_reference_fraction"], 0.5)
        self.assertEqual([r["id"] for r in report["lines"]], list(range(1, 7)))
        self.assertEqual(report["lines"][0]["excluded_reason"], "task_status")
        self.assertEqual(report["lines"][2]["excluded_reason"], "discarded")
        self.assertIsNone(report["lines"][4]["scores"])
        self.assertEqual(report["lines"][3]["scores"]["bleu"], 0)

    def test_reference_identity_hashes_and_attestation_validated(self):
        original = self.fixture()
        for key, value in (("source_transcript_sha256", "wrong"), ("language_sha256", "wrong"),
                           ("rendered_public_transcript_sha256", "wrong"), ("private_annotations_used", True),
                           ("status", "pending")):
            with self.subTest(key=key):
                self.reference.write_text(json.dumps({**original, key: value}))
                with self.assertRaises(ValueError):
                    load_reference(self.reference, self.transcript, self.language)
        original["messages"][1]["id"] = 1
        self.reference.write_text(json.dumps(original))
        with self.assertRaisesRegex(ValueError, "identity/order"):
            load_reference(self.reference, self.transcript, self.language)

    def test_fake_embeddings_use_cleaned_line_pairs_and_report_truncation(self):
        self.fixture()
        self.decoded.write_text("2. TRANSLATION\nConfidence applies per entry.\n2. H: open the red door\n4. M: move the blue lever\n6. H: Unknown.\n")
        fake = FakeEmbedder()
        report = score_reference_run(self.reference, self.transcript, self.decoded, models=True, embedder=fake)
        self.assertEqual(len(fake.calls), 1)
        self.assertEqual(fake.calls[0], ["open the red door", "move the blue lever"] * 2)
        self.assertEqual(report["lines"][1]["hypothesis_original"], "H: open the red door")
        self.assertAlmostEqual(report["summary"]["mean_per_line"]["cosine"], 2 / 3)
        self.assertEqual(report["embedding_truncation"], {
            "measured_pairs": 2, "reference_lines_truncated": 2, "hypothesis_lines_truncated": 2})
        self.assertEqual(report["lines"][1]["embedding_tokens"]["reference"], 6)

    def test_batch_loads_model_once_and_writes_ten_cells(self):
        original = self.fixture()
        batch_path = Path(__file__).resolve().parents[1] / "experiments/tangut_200g_250l_200t/analysis/sol_translation_scoring.py"
        spec = importlib.util.spec_from_file_location("sol_scoring_test", batch_path)
        batch = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(batch)
        sources, runs = [], []
        for seed in range(1, 6):
            run_id = f"R{seed:02}"
            sources.append({"run_id": run_id, "seed": seed, "family": f"E{seed:02}_sol_seed{seed}",
                            "task_dir": ".", "reference": "reference.json", "language": "swarmish.txt"})
            for condition in ("task_full", "no_task"):
                cell = f"{run_id}_{condition}"
                monitor = self.root / cell
                monitor.mkdir()
                (monitor / "decoded_swarmish.txt").write_bytes(self.decoded.read_bytes())
                summary = {"source": str(self.root), "baseline": False,
                           "conditions_requested": [condition], "conditions_completed": [condition],
                           "transcript_sha256": original["rendered_public_transcript_sha256"],
                           "source_transcript_sha256": original["rendered_public_transcript_sha256"],
                           **batch.PROTOCOLS["legacy_10min_10usd"]}
                (monitor / "monitor_summary.json").write_text(json.dumps(summary))
                for filename in ("monitor_config.json", "monitor_inputs.json"):
                    (monitor / filename).write_text("{}")
                runs.append({"cell_id": cell, "source_run_id": run_id, "condition": condition,
                             "monitor_dir": cell, "protocol": "legacy_10min_10usd"})
        manifest = self.root / "manifest.json"
        manifest.write_text(json.dumps({"sources": sources, "runs": runs, "comparability_note": "test mixed budget caveat",
                                        "decoder_archive_commit": "archive"}))
        fake = FakeEmbedder()
        with patch.object(batch.scoring, "_sentence_model", return_value=fake) as loader:
            report = batch.score_batch(manifest, self.root / "scores", models=True, repo=self.root)
            loader.assert_called_once_with(batch.scoring.ST_MODEL_REVISION)
        self.assertEqual(len(report["cells"]), 10)
        self.assertEqual(len(fake.calls), 10)
        self.assertEqual(len(list((self.root / "scores").glob("R*.json"))), 10)
        self.assertTrue((self.root / "scores/per_line.csv").exists())
        self.assertTrue((self.root / "scores/summary.csv").exists())
        (self.root / runs[0]["monitor_dir"] / "monitor_summary.json").write_text("{}")
        with patch.object(batch.scoring, "_sentence_model") as loader:
            with self.assertRaisesRegex(ValueError, "context mismatch"):
                batch.score_batch(manifest, self.root / "bad-scores", models=True, repo=self.root)
            loader.assert_not_called()
        self.assertFalse((self.root / "bad-scores").exists())


class FakeEmbedder:
    max_seq_length = 5

    def __init__(self):
        self.calls = []

    def encode(self, texts, normalize_embeddings=True):
        self.calls.append(texts)
        return [[1.0, 0.0] for _ in texts]

    def tokenizer(self, texts, **kwargs):
        return {"input_ids": [list(range(len(t.split()) + 2)) for t in texts]}


if __name__ == "__main__":
    unittest.main()
