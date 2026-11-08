"""N/A reporting preserves source measurements and exposes answered coverage."""

import copy
import importlib.util
import json
import math
import sys
import tempfile
import unittest
from unittest.mock import patch
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
ANALYSIS = REPO / "experiments/tangut_200g_250l_200t/analysis"
sys.path.insert(0, str(ANALYSIS))
spec = importlib.util.spec_from_file_location("remake_decoder_scores_na", ANALYSIS / "remake_decoder_scores_na.py")
na = importlib.util.module_from_spec(spec)
spec.loader.exec_module(na)


def line(message_id, status, cosine, confidence="medium", *, scorable=True, excluded=None):
    return {
        "id": message_id, "sender": "task" if excluded else "agent_1", "source": "glyphs",
        "reference": "Reference English", "hypothesis": "Unknown." if status == "unknown" else "Tentative English",
        "hypothesis_original": "Original English", "scoring_hypothesis": "Tentative English",
        "reference_confidence": confidence, "reference_uncertain_or_partial": confidence != "high",
        "reference_ambiguities": [], "prediction_status": status, "scorable": scorable,
        "excluded_reason": excluded, "decoder_contains_unknown": status in {"unknown", "partial_unknown"},
        "scores": {"cosine": cosine, "bleu": 0.1} if scorable else None,
    }


def source_report(lines):
    return {
        "schema_version": 1, "condition": "no_task", "coverage": {"public_messages": len(lines)},
        "metric_definition": {"cosine": "Unknown and missing contribute zero"}, "lines": lines,
        "summary": {"mean_per_line": {"cosine": 0.3}, "valid_pair_mean": {"cosine": 0.6}},
        "high_confidence": {"mean_per_line": {"cosine": 0.0}},
    }


class DecoderScoresNATests(unittest.TestCase):
    def test_unknown_and_missing_null_with_valid_pair_denominator(self):
        lines = [line(1, "present", 0.8), line(2, "partial_unknown", 0.4),
                 line(3, "unknown", 0.0, "high"), line(4, "missing", 0.0, "high"),
                 line(5, "present", None, "unknown", scorable=False),
                 line(6, "present", None, "high", scorable=False, excluded="task_status")]
        source = source_report(lines)
        original = copy.deepcopy(source)
        result = na.transform_report(source, source_path="original.json", source_sha256="hash")
        stats = result["summary"]
        self.assertEqual(source, original)
        self.assertEqual(stats["scorable_references"], 4)
        self.assertEqual(stats["valid_pairs"], 2)
        self.assertEqual(stats["cosine_denominator"], 2)
        self.assertAlmostEqual(stats["mean_per_line"]["cosine"], 0.6)
        self.assertEqual(stats["prediction_coverage"], 0.5)
        self.assertEqual(stats["unknown_only_predictions"], 1)
        self.assertEqual(stats["missing_predictions"], 1)
        self.assertEqual(stats["partial_unknown_predictions"], 1)
        self.assertEqual(result["lines"][1]["scores"]["cosine"], 0.4)
        self.assertTrue(result["lines"][1]["partial_unknown_prediction"])
        for entry in result["lines"][2:4]:
            self.assertIsNone(entry["scores"]["cosine"])
            self.assertFalse(entry["included_in_primary_mean"])
            self.assertEqual(entry["supplementary_metrics"]["zero_inclusive_scores"]["cosine"], 0.0)
        self.assertIsNone(result["high_confidence"]["mean_per_line"]["cosine"])
        self.assertEqual(result["high_confidence"]["prediction_coverage"], 0)
        self.assertEqual(result["supplementary_metrics"]["summary"], original["summary"])

    def test_all_unknown_and_absent_high_confidence_means_are_none(self):
        result = na.transform_report(source_report([line(1, "unknown", 0), line(2, "missing", 0)]),
                                     source_path="original.json", source_sha256="hash")
        self.assertIsNone(result["summary"]["mean_per_line"]["cosine"])
        self.assertEqual(result["summary"]["prediction_coverage"], 0)
        self.assertEqual(result["summary"]["valid_pairs"], 0)
        self.assertIsNone(result["high_confidence"]["mean_per_line"]["cosine"])
        self.assertIsNone(result["high_confidence"]["prediction_coverage"])

    def test_rebuild_preserves_inputs_failures_and_supplementary_means(self):
        with tempfile.TemporaryDirectory() as temporary:
            repo = Path(temporary)
            original = repo / "original"
            output = repo / "derived"
            report = source_report([line(1, "unknown", 0, "high")])
            report["summary"]["mean_per_line"]["cosine"] = 0.0
            na.write_json(original / "A.json", report)
            cell = {"cell_id": "A", "encoder": "Haiku", "decoder": "Haiku", "condition": "no_task",
                    "status": "completed", "cosine": 0.0, "high_confidence_cosine": 0.0,
                    "report_path": "original/A.json", "report_sha256": na.sha(original / "A.json")}
            failure = {"cell_id": "D12", "encoder": "DeepSeek", "decoder": "DeepSeek", "condition": "task_full",
                       "status": "failed", "cosine": None, "high_confidence_cosine": None,
                       "report_path": None, "reason": "logging failure", "failure_record": "receipt.json"}
            summary = {"schema_version": 1, "cells": [cell, failure],
                       "counts": {"completed": 1, "failed_unscored": 1, "public_rows": 1, "scorable_pairs": 1}}
            na.write_json(original / "summary.json", summary)
            before = {path: path.read_bytes() for path in original.iterdir()}
            result = na.remake(original / "summary.json", output, repo=repo)
            for path, content in before.items():
                self.assertEqual(path.read_bytes(), content)
            self.assertEqual(result["cells"][1], failure)
            self.assertIsNone(result["cells"][0]["cosine"])
            self.assertEqual(result["cells"][0]["zero_inclusive_cosine"], 0.0)
            self.assertEqual(result["cells"][0]["report_sha256"], na.sha(output / "A.json"))
            self.assertIsNone(json.loads((output / "per_line.json").read_text())[0]["cosine"])
            self.assertIn("N/A", (output / "per_line.csv").read_text())
            html = (output / "comparisons.html").read_text()
            payload = html.split('<script id="comparison-data" type="application/json">', 1)[1].split("</script>", 1)[0]
            self.assertEqual(json.loads(payload)["primary_metric"], na.PRIMARY_METRIC)
            self.assertEqual(json.loads(payload)["cells"][1]["lines"], [])
            with self.assertRaisesRegex(ValueError, "separate"):
                na.remake(original / "summary.json", original, repo=repo)

    def test_archived_cells_match_existing_valid_pairs_without_reclassification(self):
        summary = json.loads(na.DEFAULT_INPUT.read_text())
        self.assertEqual(len(summary["cells"]), 24)
        self.assertTrue({"D14", "R02_task_summary", "R02_wrong_task"} <= {cell["cell_id"] for cell in summary["cells"]})
        for cell in summary["cells"]:
            if cell["status"] != "completed":
                continue
            with self.subTest(cell=cell["cell_id"]):
                path = REPO / cell["report_path"]
                source = json.loads(path.read_text())
                report = na.transform_report(source, source_path=cell["report_path"], source_sha256=na.sha(path))
                valid = [entry for entry in source["lines"] if entry["scorable"] and entry["prediction_status"] not in na.ABSTENTIONS]
                self.assertEqual(report["summary"]["valid_pairs"], len(valid))
                expected = math.fsum(entry["scores"]["cosine"] for entry in valid) / len(valid) if valid else None
                self.assertEqual(report["summary"]["mean_per_line"]["cosine"], expected)
                self.assertEqual(report["summary"]["scorable_references"], cell["scorable_references"])
                for old, new in zip(source["lines"], report["lines"]):
                    for key in ("id", "hypothesis", "hypothesis_original", "prediction_status", "reference", "reference_confidence"):
                        self.assertEqual(new.get(key), old.get(key))
                if cell["cell_id"] in {"D05", "D06"}:
                    self.assertIsNone(expected)
                    self.assertEqual(report["summary"]["prediction_coverage"], 0.0)
                if cell["cell_id"] == "D11":
                    self.assertEqual(report["summary"]["valid_pairs"], 145)
                    self.assertAlmostEqual(expected, 0.22618565278781963)
                    self.assertIsNone(report["high_confidence"]["mean_per_line"]["cosine"])

    def test_catalog_rebuild_preserves_sources_and_deduplicates_existing_cells(self):
        import assemble_decoder_score_catalog as catalog
        sources = [catalog.BASE, catalog.FOLLOWUP, catalog.SEED2]
        saved = json.loads(na.DEFAULT_INPUT.read_text())
        sources.extend(REPO / cell["report_path"] for cell in saved["cells"] if cell["status"] == "completed")
        before = {path: na.sha(path) for path in sources}
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / "summary.json"
            with patch.object(catalog, "OUTPUT", output):
                rebuilt = catalog.assemble()
            self.assertEqual(rebuilt, saved)
            self.assertEqual(len(rebuilt["cells"]), len({cell["cell_id"] for cell in rebuilt["cells"]}))
            self.assertEqual(rebuilt["counts"]["completed"], 23)
            self.assertEqual(rebuilt["counts"]["failed_unscored"], 1)
            self.assertEqual(rebuilt["source_catalog"]["model_calls"], 0)
            self.assertEqual(rebuilt["source_catalog"]["api_calls"], 0)
        self.assertEqual({path: na.sha(path) for path in sources}, before)

    def test_legacy_renderer_keeps_default_zero_inclusive_mode(self):
        from render_decoder_comparisons import render
        summary = json.loads((ANALYSIS / "decoder_comparison_scores/summary.json").read_text())
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "legacy.html"
            render(summary, REPO, path)
            payload = path.read_text().split('<script id="comparison-data" type="application/json">', 1)[1].split("</script>", 1)[0]
            embedded = json.loads(payload)
            self.assertIsNone(embedded["primary_metric"])
            d05 = next(cell for cell in embedded["cells"] if cell["cell_id"] == "D05")
            self.assertEqual(d05["cosine"], 0.0)
            self.assertTrue(all(entry["scores"]["cosine"] == 0 for entry in d05["lines"] if entry["scorable"]))


if __name__ == "__main__":
    unittest.main()
