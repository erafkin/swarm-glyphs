"""Zero-abstention reporting keeps every eligible reference in the denominator."""
import copy
import importlib.util
import json
import math
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
ANALYSIS = REPO / "experiments/tangut_200g_250l_200t/analysis"
spec = importlib.util.spec_from_file_location("remake_decoder_scores_zero", ANALYSIS / "remake_decoder_scores_zero.py")
zero = importlib.util.module_from_spec(spec)
spec.loader.exec_module(zero)


def line(number, historical, raw_status, cosine, *, confidence="medium", scorable=True, excluded=None):
    return {
        "id": number, "sender": "task" if excluded else "agent_0", "source": "glyphs",
        "reference": "English reference", "reference_confidence": confidence,
        "hypothesis": "" if raw_status == "missing" else "English hypothesis",
        "prediction_status": raw_status, "historical_prediction_status": historical,
        "historical_unknown_reason": "global_unknown_content_declaration" if historical == "unknown" else None,
        "scorable": scorable, "excluded_reason": excluded,
        "scores": {"cosine": cosine} if cosine is not None else None,
    }


def raw_report(lines, kind="historical_source_report"):
    return {
        "primary_metric": zero.RAW_METRIC, "condition": "no_task", "lines": lines,
        "derived_from": {"kind": kind, "report_path": "historical/A.json", "report_sha256": "hash"},
        "coverage": {"public_messages": len(lines)},
        "summary": {"mean_per_line": {"cosine": 0.3}},
        "high_confidence": {"mean_per_line": {"cosine": None}},
    }


class ZeroAbstentionTests(unittest.TestCase):
    def test_historical_abstentions_zero_even_when_raw_parser_calls_them_present(self):
        source = raw_report([
            line(1, "present", "present", 0.8),
            line(2, "partial_unknown", "partial_unknown", 0.4),
            line(3, "unknown", "present", 0.3, confidence="high"),
            line(4, "missing", "missing", None, confidence="high"),
            line(5, "present", "present", None, scorable=False, confidence="unknown"),
            line(6, "present", "present", None, scorable=False, excluded="task_status"),
        ])
        original = copy.deepcopy(source)
        report = zero.transform_report(source, source_path="raw.json", source_sha256="digest")
        self.assertEqual(source, original)
        stats = report["summary"]
        self.assertAlmostEqual(stats["mean_per_line"]["cosine"], 0.3)
        self.assertEqual(stats["cosine_denominator"], 4)
        self.assertEqual(stats["valid_pairs"], 2)
        self.assertEqual(stats["prediction_coverage"], 0.5)
        self.assertEqual(stats["zero_assigned_predictions"], 2)
        self.assertEqual(stats["partial_unknown_predictions"], 1)
        self.assertEqual(report["lines"][2]["raw_text_cosine"], 0.3)
        self.assertEqual(report["lines"][2]["raw_prediction_status"], "present")
        self.assertEqual(report["lines"][2]["prediction_status"], "unknown")
        self.assertEqual(report["high_confidence"]["mean_per_line"]["cosine"], 0.0)
        for row in report["lines"][4:]:
            self.assertIsNone(row["scores"]["cosine"])
            self.assertFalse(row["included_in_primary_mean"])

    def test_empty_reference_subset_is_na_but_all_abstentions_is_zero(self):
        source = raw_report([line(1, "unknown", "unknown", 0.5)])
        report = zero.transform_report(source, source_path="raw.json", source_sha256="digest")
        self.assertEqual(report["summary"]["mean_per_line"]["cosine"], 0.0)
        self.assertIsNone(report["high_confidence"]["mean_per_line"]["cosine"])
        self.assertEqual(report["high_confidence"]["cosine_denominator"], 0)

    def test_fresh_decoder_uses_archived_parser_and_retains_partial_unknown(self):
        source = raw_report([line(1, None, "partial_unknown", -0.1),
                             line(2, None, "unknown", 0.4)], kind="fresh_decoder_config")
        report = zero.transform_report(source, source_path="raw.json", source_sha256="digest")
        self.assertEqual(report["summary"]["mean_per_line"]["cosine"], -0.05)
        self.assertEqual(report["summary"]["raw_parser_classifications"], 2)
        source["derived_from"]["kind"] = "historical_source_report"
        with self.assertRaisesRegex(ValueError, "classification"):
            zero.transform_report(source, source_path="raw.json", source_sha256="digest")

    def test_nonabstaining_scores_must_be_finite_and_duplicate_ids_rejected(self):
        for invalid in (None, math.nan, math.inf):
            with self.subTest(cosine=invalid), self.assertRaisesRegex(ValueError, "finite cosine"):
                zero.transform_report(raw_report([line(1, "present", "present", invalid)]),
                                      source_path="raw.json", source_sha256="digest")
        with self.assertRaisesRegex(ValueError, "Duplicate message IDs"):
            zero.transform_report(raw_report([line(1, "present", "present", 0.2)] * 2),
                                  source_path="raw.json", source_sha256="digest")

    def test_classification_provenance_rejects_tampering_and_missing_alignment(self):
        with tempfile.TemporaryDirectory() as temporary:
            repo = Path(temporary)
            row = line(1, "unknown", "present", 0.2)
            raw = raw_report([row])
            old = copy.deepcopy(row)
            old["prediction_status"] = "unknown"
            path = repo / "historical/A.json"
            zero.write_json(path, {"lines": [old]})
            raw["derived_from"]["report_sha256"] = zero.sha(path)
            zero.verify_classifications(raw, repo)
            raw["lines"][0]["historical_prediction_status"] = "present"
            with self.assertRaisesRegex(ValueError, "status changed"):
                zero.verify_classifications(raw, repo)
            raw["lines"][0]["historical_prediction_status"] = "unknown"
            raw["lines"][0]["reference"] = "Different reference"
            with self.assertRaisesRegex(ValueError, "identity changed"):
                zero.verify_classifications(raw, repo)
            raw["lines"] = []
            with self.assertRaisesRegex(ValueError, "ID alignment"):
                zero.verify_classifications(raw, repo)
            path.write_text("{}")
            with self.assertRaisesRegex(ValueError, "hash mismatch"):
                zero.verify_classifications(raw, repo)

    def test_archived_results_regression_source_preservation_and_reproducibility(self):
        source = json.loads(zero.DEFAULT_INPUT.read_text())
        paths = {zero.DEFAULT_INPUT}
        for cell in source["cells"]:
            if cell["status"] == "completed":
                path = REPO / cell["report_path"]
                paths.add(path)
                paths.add(REPO / json.loads(path.read_text())["derived_from"]["report_path"])
        before = {path: zero.sha(path) for path in paths}
        with tempfile.TemporaryDirectory(dir=REPO) as temporary:
            output = Path(temporary) / "derived"
            rebuilt = zero.remake(output=output)
            cells = {cell["cell_id"]: cell for cell in rebuilt["cells"]}
            self.assertEqual(rebuilt["counts"]["completed"], 24)
            self.assertEqual(rebuilt["counts"]["failed_unscored"], 1)
            self.assertEqual(rebuilt["counts"]["cosine_denominator"], 2129)
            self.assertEqual(rebuilt["counts"]["zero_assigned_predictions"], 237)
            expected = {"D05": 0.0, "D06": 0.0, "D07": 0.07460178752815685,
                        "D14": 0.23056829007874746, "D11": 0.19998121883599781,
                        "D12_retry1": 0.2631357143604035}
            for identity, value in expected.items():
                self.assertAlmostEqual(cells[identity]["cosine"], value, places=14)
            for identity in ("D05", "D06"):
                self.assertEqual(cells[identity]["cosine_denominator"], 109)
                self.assertEqual(cells[identity]["valid_pairs"], 0)
            self.assertEqual(cells["D07"]["partial_unknown_predictions"], 109)
            self.assertEqual(cells["D14"]["partial_unknown_predictions"], 42)
            self.assertEqual(cells["D11"]["unknown_only_predictions"], 19)
            failure = next(cell for cell in source["cells"] if cell["cell_id"] == "D12")
            self.assertEqual(cells["D12"], failure)
            self.assertFalse((output / "D12.json").exists())
            for cell in rebuilt["cells"]:
                if cell["status"] == "completed":
                    self.assertEqual(zero.sha(REPO / cell["report_path"]), cell["report_sha256"])
            first_build = {path.name: zero.sha(path) for path in output.iterdir()}
            zero.remake(output=output)
            self.assertEqual(first_build, {path.name: zero.sha(path) for path in output.iterdir()})
            self.assertEqual(before, {path: zero.sha(path) for path in paths})
        with self.assertRaisesRegex(ValueError, "separate"):
            zero.remake(output=zero.DEFAULT_INPUT.parent)


if __name__ == "__main__":
    unittest.main()
