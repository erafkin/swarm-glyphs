"""Validate the archived comparison inputs and resulting measurement denominators."""

import hashlib
import importlib.util
import json
import math
import sys
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
ANALYSIS = REPO / "experiments/tangut_200g_250l_200t/analysis"
OUTPUT = ANALYSIS / "decoder_comparison_scores"
sys.path.insert(0, str(ANALYSIS))
spec = importlib.util.spec_from_file_location("comparison_scoring", ANALYSIS / "decoder_comparison_scoring.py")
batch = importlib.util.module_from_spec(spec)
spec.loader.exec_module(batch)


class DecoderComparisonScoringTests(unittest.TestCase):
    def test_archived_inputs_preflight_without_loading_models(self):
        _, previous, cells = batch.preflight()
        self.assertEqual(len(previous), 12)
        self.assertEqual(len(cells), 9)
        self.assertEqual([c["run"]["cell_id"] for c in cells if c["run"]["status"] == "failed"], ["D12"])

    def test_summary_is_exactly_twenty_unique_completed_and_one_failed(self):
        summary = json.loads((OUTPUT / "summary.json").read_text())
        self.assertEqual(len({r["cell_id"] for r in summary["cells"]}), 21)
        complete = [r for r in summary["cells"] if r["status"] == "completed"]
        self.assertEqual(len(complete), 20)
        self.assertEqual(sum(r["scorable_references"] for r in complete), 1738)
        failed = [r for r in summary["cells"] if r["status"] == "failed"]
        self.assertEqual(len(failed), 1)
        self.assertEqual(failed[0]["cell_id"], "D12")
        self.assertIsNone(failed[0]["cosine"])
        self.assertIsNone(failed[0]["report_path"])

    def test_all_means_use_fixed_denominator_and_exclusions(self):
        summary = json.loads((OUTPUT / "summary.json").read_text())
        for cell in summary["cells"]:
            if cell["status"] != "completed":
                continue
            with self.subTest(cell=cell["cell_id"]):
                path = REPO / cell["report_path"]
                self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), cell["report_sha256"])
                report = json.loads(path.read_text())
                scored = [r for r in report["lines"] if r["scorable"]]
                self.assertEqual(len(scored), cell["scorable_references"])
                self.assertAlmostEqual(math.fsum(r["scores"]["cosine"] for r in scored) / len(scored), cell["cosine"], places=12)
                for row in report["lines"]:
                    if row["excluded_reason"]:
                        self.assertIsNone(row["scores"])
                    if row["scorable"] and row["prediction_status"] in {"missing", "unknown"}:
                        self.assertEqual(row["scores"]["cosine"], 0.0)
                high = [r for r in scored if r["reference_confidence"] == "high"]
                if high:
                    self.assertAlmostEqual(math.fsum(r["scores"]["cosine"] for r in high) / len(high), cell["high_confidence_cosine"], places=12)
                else:
                    self.assertIsNone(cell["high_confidence_cosine"])

    def test_explicit_unknowns_preserve_original_decoder_words(self):
        for cell_id, count in (("D05", 109), ("D06", 109), ("D11", 6)):
            report = json.loads((OUTPUT / f"{cell_id}.json").read_text())
            overrides = [r for r in report["lines"] if r.get("unknown_reason")]
            self.assertEqual(len(overrides), count)
            self.assertTrue(all(r["hypothesis_original"] and r["hypothesis_normalized_raw"] for r in overrides))
            self.assertTrue(all(r["prediction_status"] == "unknown" and r["scores"]["cosine"] == 0 for r in overrides))
            self.assertNotEqual(report["inputs"]["canonical_document_sha256"], report["inputs"]["decoder_document_sha256"])


if __name__ == "__main__":
    unittest.main()
