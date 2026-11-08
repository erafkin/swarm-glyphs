"""Raw public cosine includes literal abstentions without inventing translations."""
import copy
import importlib.util
import json
import math
from pathlib import Path
import sys
import tempfile
import unittest

REPO = Path(__file__).resolve().parents[1]
ANALYSIS = REPO / "experiments/tangut_200g_250l_200t/analysis"
sys.path.insert(0, str(ANALYSIS))
spec = importlib.util.spec_from_file_location("score_public_raw_cosines", ANALYSIS / "score_public_raw_cosines.py")
raw = importlib.util.module_from_spec(spec)
spec.loader.exec_module(raw)


def reference(number, text="glyph", confidence="medium", sender="agent_1", english="I have two."):
    return {"id": number, "text": text, "sender": sender, "english": english, "confidence": confidence}


class PublicRawCosineTests(unittest.TestCase):
    def test_unknown_text_and_structural_glosses_stay_literal(self):
        references = [reference(1), reference(2), reference(3), reference(4, text="⊘"),
                      reference(5, sender="task"), reference(6, confidence="unknown", english="Unknown.")]
        decoded = {1: "unknown", 2: "unknown (a repeated question)", 3: "S: 𗏔 𗟎 template", 4: "Two", 5: "Feedback", 6: "Two"}
        historical = {3: {"sender": "agent_1", "source": "glyph", "reference": "I have two.",
                          "scorable": True, "prediction_status": "unknown", "unknown_reason": "global_declaration"}}
        before = copy.deepcopy(decoded)
        lines = raw.make_lines(references, decoded, decoded, historical)
        self.assertEqual(decoded, before)
        self.assertEqual([line["hypothesis"] for line in lines[:3]], list(decoded.values())[:3])
        self.assertTrue(all(line["included_in_primary_mean"] for line in lines[:3]))
        self.assertEqual([line["prediction_status"] for line in lines[:3]], ["unknown", "partial_unknown", "present"])
        self.assertEqual(lines[2]["historical_prediction_status"], "unknown")
        self.assertEqual([line["excluded_reason"] for line in lines[3:5]], ["discarded", "task_status"])
        self.assertTrue(all(not line["included_in_primary_mean"] for line in lines[3:]))
        for line, value in zip(lines[:3], (0.3, 0.6, 0.9)):
            line["scores"] = {"cosine": value}
        stats = raw.summarize(lines)
        self.assertAlmostEqual(stats["mean_per_line"]["cosine"], 0.6)
        self.assertEqual(stats["cosine_denominator"], 3)
        self.assertEqual(stats["unknown_only_predictions"], 1)
        self.assertEqual(stats["historical_unknown_classifications"], 1)

    def test_missing_is_not_replaced_with_unknown_or_included_as_text(self):
        references = [reference(1), reference(2)]
        with self.assertRaisesRegex(ValueError, "Missing eligible"):
            raw.make_lines(references, {1: "unknown"}, {1: "unknown"}, {})
        lines = raw.make_lines(references, {1: "unknown"}, {1: "unknown"}, {}, allow_missing=True)
        lines[0]["scores"] = {"cosine": 0.25}
        stats = raw.summarize(lines)
        self.assertEqual(stats["mean_per_line"]["cosine"], 0.25)
        self.assertEqual(stats["scorable_references"], 2)
        self.assertEqual(stats["embedded_pairs"], 1)
        self.assertEqual(stats["missing_predictions"], 1)
        self.assertEqual(stats["prediction_coverage"], 0.5)
        self.assertEqual(lines[1]["hypothesis"], "")
        self.assertIsNone(lines[1]["scores"])

    def test_all_archived_original_inputs_align_and_keep_deepseek_discards_excluded(self):
        _, prepared = raw.preflight([raw.DEFAULT_INPUT], raw.DEFAULT_OUTPUT)
        self.assertEqual(len(prepared), 24)
        self.assertEqual(sum("lines" in item for item in prepared), 23)
        cells = {item["cell"]["cell_id"]: item for item in prepared}
        self.assertEqual(cells["D12"]["cell"]["status"], "failed")
        for cell_id in ("D11", "D13"):
            lines = cells[cell_id]["lines"]
            self.assertEqual(sum(line["excluded_reason"] == "discarded" for line in lines), 30)
            self.assertEqual(sum(line["included_in_primary_mean"] for line in lines), 164)
        d05 = [line for line in cells["D05"]["lines"] if line["scorable"]]
        self.assertTrue(all(line["historical_prediction_status"] == "unknown" for line in d05))
        self.assertTrue(any(line["hypothesis"].startswith("S:") for line in d05))
        d06 = [line for line in cells["D06"]["lines"] if line["scorable"]]
        self.assertTrue(all(line["hypothesis"] == "unknown" and line["included_in_primary_mean"] for line in d06))
        with self.assertRaisesRegex(ValueError, "duplicate cell ID"):
            raw.preflight([raw.DEFAULT_INPUT, raw.DEFAULT_INPUT], raw.DEFAULT_OUTPUT)

    def test_fresh_decoder_config_validates_receipt_and_final_answer_without_embeddings(self):
        summary = json.loads(raw.DEFAULT_INPUT.read_text())
        cell = next(row for row in summary["cells"] if row["cell_id"] == "D14")
        report = json.loads((REPO / cell["report_path"]).read_text())
        config = {key: cell[key] for key in ("cell_id", "encoder", "seed", "decoder", "decoder_model", "condition", "source_escaped", "protocol")}
        config.update({key: report[key] for key in ("reference", "task_dir", "language", "decoder_document")})
        config["receipt"] = report["decoder_provenance"]["record_path"]
        with tempfile.TemporaryDirectory(dir=REPO) as temporary:
            path = Path(temporary) / "config.json"
            path.write_text(json.dumps(config))
            _, item = raw.prepare_extra(path, raw.DEFAULT_OUTPUT)
            self.assertEqual(item["source_kind"], "fresh_decoder_config")
            self.assertEqual(sum(row["scorable"] for row in item["lines"]), 109)
            self.assertNotIn("embedding_model", item["source_report"])
            config["decoder_model"] = "incorrect/model"
            path.write_text(json.dumps(config))
            with self.assertRaisesRegex(ValueError, "configured decoder"):
                raw.prepare_extra(path, raw.DEFAULT_OUTPUT)

    def test_saved_raw_reports_match_paired_means_and_original_parser(self):
        summary = json.loads((raw.DEFAULT_OUTPUT / "summary.json").read_text())
        self.assertEqual(summary["primary_metric"], raw.PRIMARY_METRIC)
        _, prepared = raw.preflight([raw.DEFAULT_INPUT], raw.DEFAULT_OUTPUT)
        original = {item["cell"]["cell_id"]: item for item in prepared}
        for cell in summary["cells"]:
            if cell["status"] != "completed":
                continue
            report_path = REPO / cell["report_path"]
            report = json.loads(report_path.read_text())
            self.assertEqual(raw.sha(report_path), cell["report_sha256"])
            included = [line for line in report["lines"] if line["included_in_primary_mean"]]
            expected = math.fsum(line["scores"]["cosine"] for line in included) / len(included)
            self.assertEqual(cell["cosine"], expected)
            if cell["cell_id"] in original:
                self.assertEqual([line["hypothesis"] for line in report["lines"]],
                                 [line["hypothesis"] for line in original[cell["cell_id"]]["lines"]])
        by_id = {cell["cell_id"]: cell for cell in summary["cells"]}
        self.assertAlmostEqual(by_id["D05"]["cosine"], 0.1632656084, places=6)
        self.assertAlmostEqual(by_id["D06"]["cosine"], 0.2093293225, places=6)
        self.assertEqual(by_id["D11"]["cosine_denominator"], 164)
        self.assertEqual(by_id["D12"]["status"], "failed")
        html = (raw.DEFAULT_OUTPUT / "comparisons.html").read_text()
        payload = html.split('<script id="comparison-data" type="application/json">', 1)[1].split("</script>", 1)[0]
        self.assertEqual(json.loads(payload)["primary_metric"], raw.PRIMARY_METRIC)
        self.assertIn("Embedded as ordinary text", html)


if __name__ == "__main__":
    unittest.main()
