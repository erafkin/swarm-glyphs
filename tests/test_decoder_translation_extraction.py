"""Offline extraction tests against the public decoder artifacts only."""

import importlib.util
import tempfile
import unittest
from pathlib import Path

from src.core.translation_scoring import parse_translation


ROOT = Path(__file__).resolve().parents[1]
EXPERIMENT = ROOT / "experiments/tangut_200g_250l_200t"
spec = importlib.util.spec_from_file_location(
    "decoder_translation_extraction", EXPERIMENT / "analysis/decoder_translation_extraction.py")
adapter = importlib.util.module_from_spec(spec)
spec.loader.exec_module(adapter)
extract_translation = adapter.extract_translation


class DecoderTranslationExtractionTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.path = Path(self.tmp.name) / "decoded.txt"

    def fixture(self, cell):
        return next((EXPERIMENT / "decoding").glob(f"{cell}_*/decoded.txt"))

    def extract(self, cell, content, expected):
        self.path.write_text(content, encoding="utf-8")
        return extract_translation(self.path, cell, expected)

    def test_all_eight_fixtures_preserve_explicit_global_ids(self):
        for cell, start, end in (("D05", 2, 110), ("D06", 2, 110), ("D07", 1, 110),
                                 ("D08", 1, 97), ("D09", 1, 97), ("D10", 1, 97),
                                 ("D11", 1, 227), ("D13", 1, 227)):
            with self.subTest(cell=cell):
                result = extract_translation(self.fixture(cell), cell, set(range(1, end + 1)))
                self.assertEqual([entry["id"] for entry in result["entries"]], list(range(start, end + 1)))
                self.assertEqual(result["preamble"], result["conventions"])

    def test_core_formats_keep_normalized_text_and_original_bodies(self):
        for cell, end in (("D07", 110), ("D09", 97), ("D10", 97), ("D11", 227), ("D13", 227)):
            with self.subTest(cell=cell):
                path = self.fixture(cell)
                entries = extract_translation(path, cell, set(range(1, end + 1)))["entries"]
                self.assertEqual({e["id"]: e["original"] for e in entries},
                                 parse_translation(path, require_section=True, strip_prefixes=False))
                self.assertEqual({e["id"]: e["normalized"] for e in entries},
                                 parse_translation(path, require_section=True))
                if cell != "D11":
                    self.assertTrue(all(e["normalized"] == e["scoring_text"] for e in entries))
                    self.assertTrue(all(e["unknown_reason"] is None for e in entries))

    def test_d05_global_unknown_keeps_all_structural_glosses(self):
        result = extract_translation(self.fixture("D05"), "D05", set(range(1, 111)))
        entries = result["entries"]
        self.assertEqual(sum(e["original"].startswith("S:") for e in entries), 83)
        self.assertEqual(sum(e["original"].startswith("U:") for e in entries), 26)
        self.assertTrue(all(e["original"] == e["normalized"] for e in entries))
        self.assertTrue(all(e["scoring_text"] == "Unknown." for e in entries))
        self.assertEqual({e["unknown_reason"] for e in entries}, {"global_unknown_content_declaration"})
        self.assertNotIn("SECTION 3", entries[-1]["original"])
        self.assertIn("Message [1]", result["preamble"])

    def test_d06_extracts_only_explicit_enumeration_and_preserves_postamble(self):
        result = extract_translation(self.fixture("D06"), "D06", set(range(1, 111)))
        self.assertTrue(all(e["original"] == e["normalized"] == "unknown" for e in result["entries"]))
        self.assertTrue(all(e["scoring_text"] == "Unknown." for e in result["entries"]))
        self.assertTrue(all(e["unknown_reason"] == "explicit_unknown" for e in result["entries"]))
        self.assertIn("Structural note only", " ".join(result["notes"]))
        changed = self.fixture("D06").read_text().replace(" 3 unknown;", "", 1)
        entries = self.extract("D06", changed, set(range(1, 111)))["entries"]
        self.assertNotIn(3, [e["id"] for e in entries])  # Declared range does not fabricate missing rows.

    def test_d08_bullets_sender_tags_and_separator(self):
        entries = extract_translation(self.fixture("D08"), "D08", set(range(1, 98)))["entries"]
        self.assertTrue(entries[1]["original"].startswith("[agent_4] Statement:"))
        self.assertTrue(entries[1]["normalized"].startswith("Statement: agent_4:"))
        self.assertEqual(entries[-1]["normalized"], '{"stage":3,"invalid_attempts":16}')
        self.assertNotIn("---", entries[-1]["original"])

    def test_d11_only_six_structural_parentheticals_are_converted(self):
        entries = extract_translation(self.fixture("D11"), "D11", set(range(1, 228)))["entries"]
        changed = [e for e in entries if e["normalized"] != e["scoring_text"]]
        self.assertEqual([e["id"] for e in changed], [2, 5, 6, 8, 11, 13])
        self.assertTrue(all(e["scoring_text"] == "Unknown." for e in changed))
        self.assertTrue(all(e["normalized"].startswith("unknown (") for e in changed))
        self.assertEqual(entries[14]["scoring_text"], "unknown.")

    def test_section_boundaries_exclude_citations_and_later_prose(self):
        text = "1. SWARMISH.TXT, RECONSTRUCTED\n[999] citation\n2. TRANSLATION\nConventions: [987] is a citation.\n[2] [agent_0] Maybe open X; unknown qualifier.\n3. THE TASK\n[2] later citation\n4. EVIDENCE\n[1] evidence citation\n"
        result = self.extract("D09", text, {1, 2})
        self.assertEqual([e["id"] for e in result["entries"]], [2])
        self.assertEqual(result["entries"][0]["scoring_text"], "Maybe open X; unknown qualifier.")
        self.assertIn("[987]", result["conventions"])

    def test_duplicate_unexpected_ids_and_layout_drift_fail(self):
        for body, expected, error in (("[2] a\n[2] b", {2}, "duplicate"),
                                      ("[3] a", {2}, "unexpected"),
                                      ("- [2] a", {2}, "layout"),
                                      ("[2] a\nUnnumbered afterword", {2}, "non-entry")):
            with self.subTest(body=body):
                text = f"2. TRANSLATION\n{body}\n3. THE TASK\n4. EVIDENCE\n"
                with self.assertRaisesRegex(ValueError, error):
                    self.extract("D09", text, expected)
        for text in ("[2] bare entry", "2. TRANSLATION\n[2] a\n3. THE TASK\n",
                     "2. TRANSLATION\n[2] a\n3. THE TASK\n2. TRANSLATION\n4. EVIDENCE\n"):
            with self.subTest(text=text), self.assertRaisesRegex(ValueError, "heading"):
                self.extract("D09", text, {2})

    def test_unknown_overrides_require_the_audited_evidence(self):
        for cell, old, new, end in (
            ("D05", "every content meaning is unknown", "some content meanings are known", 110),
            ("D06", "Messages 2 to 110 are each unknown:", "Messages 2 to 110 are partly known:", 110),
            ("D11", '"unknown" is used when meaning is unclear.', '"unknown" means a red lever.', 227),
            ("D11", "unknown (short message, possibly partial assignment).", "unknown (but open the red lever).", 227),
        ):
            with self.subTest(cell=cell, old=old), self.assertRaisesRegex(ValueError, "audited"):
                self.extract(cell, self.fixture(cell).read_text().replace(old, new, 1), set(range(1, end + 1)))


if __name__ == "__main__":
    unittest.main()
