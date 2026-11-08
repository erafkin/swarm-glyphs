"""Offline checks for immutable imports, frozen language handoffs and run planning."""
import importlib.util
import json
from pathlib import Path
import random
import shutil
import tempfile
import unittest
from unittest.mock import patch

REPO = Path(__file__).resolve().parents[1]
BATCH = REPO / "experiments/tangut_200g_250l_200t"
spec = importlib.util.spec_from_file_location("experiment_batch", BATCH / "batch.py")
batch = importlib.util.module_from_spec(spec)
spec.loader.exec_module(batch)


class BatchArchiveTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.repo = Path(self.tmp.name).resolve()
        self.root = self.repo / "experiments/batch"
        self.root.mkdir(parents=True)
        self.patch = patch.object(batch, "REPO", self.repo)
        self.patch.start()
        self.addCleanup(self.patch.stop)
        self.folder = self.root / "encoding/E01_sol_seed1"
        self.folder.mkdir(parents=True)
        self.plan = {"id": "E01", "stage": "encoding", "owner": "emma_krentz", "model": "openai/gpt-6.1-sol", "source_run_id": None, "seed_index": 1, "config_seed": 0, "condition": None, "approved_deviations": []}
        self.config = batch.LanguageExperimentConfig(task_kind="escape_room", run_monitors=False, n_agents=8,
            monitor_n_agents=8, model=self.plan["model"], n_glyphs=200, language_minutes=None,
            language_max_turns=200, language_max_lines=250, monitor_minutes=None, monitor_max_turns=200,
            seed=0, log_dir=str(self.folder.relative_to(self.repo) / "raw")).model_dump()
        batch.write(self.root / "batch.json", {"runs": [{"id": "E01", "path": "encoding/E01_sol_seed1"}]})
        batch.write(self.folder / "plan.json", self.plan)
        batch.write(self.folder / "config.json", self.config)
        self.source = self.repo / "incoming/source"
        self.source.mkdir(parents=True)
        batch.write(self.source / "config.json", self.config)
        batch.write(self.source / "glyphs.json", batch.sample_glyphs("glyphs_tangut", 200, random.Random(0)))
        batch.write(self.source / "language_protocol.json", {"requirements": "Use Swarmish under 250 lines."})
        batch.write(self.source / "summary.json", {"creation_only": True, "creation_stop_reason": "all_done", "total_cost_usd": 1.23})
        self.calls([
            {"phase": "creation", "agent_id": "agent_0", "turn": 1, "state_applied": True, "language_document": "EARLY"},
            {"phase": "creation", "agent_id": "agent_1", "turn": 1, "state_applied": True, "language_document": "SHARED\nFINAL"},
            {"phase": "creation", "state_applied": False, "language_document": "IGNORED LATE"},
        ])
        (self.source / "swarmish.txt").write_text("CONCATENATED PER-AGENT EXPORTS")

    def calls(self, records):
        (self.source / "agent_calls.jsonl").write_text("\n".join(json.dumps(r) for r in records) + "\n")

    def test_freeze_last_applied_shared_draft_and_retain_raw(self):
        (self.source / "monitor_runs").mkdir()
        batch.write(self.source / "monitor_runs/private.json", {"not": "copied"})
        receipt = batch.collect(self.root, "E01", self.source)
        self.assertEqual((self.folder / "handoff/swarmish.txt").read_text(), "SHARED\nFINAL\n")
        copied = self.repo / receipt["raw_path"]
        self.assertEqual((copied / "swarmish.txt").read_text(), "CONCATENATED PER-AGENT EXPORTS")
        self.assertFalse((copied / "monitor_runs").exists())
        self.assertEqual(receipt["shared_draft"]["lines"], 2)
        self.assertEqual(receipt["discussion_calls"], 3)
        self.assertEqual(receipt["raw_sha256"]["config.json"], batch.sha(copied / "config.json"))
        with self.assertRaisesRegex(ValueError, "overwrite"):
            batch.collect(self.root, "E01", self.source)

    def test_reject_overlong_shared_draft_before_copy(self):
        self.calls([{"phase": "creation", "state_applied": True, "language_document": "\n".join(["x"] * 251)}])
        with self.assertRaisesRegex(ValueError, "250 lines"):
            batch.collect(self.root, "E01", self.source)
        self.assertFalse((self.folder / "raw/source").exists())

    def test_reject_wrong_glyph_sample_before_copy(self):
        batch.write(self.source / "glyphs.json", batch.sample_glyphs("glyphs_tangut", 200, random.Random(1)))
        with self.assertRaisesRegex(ValueError, "Glyph sample"):
            batch.collect(self.root, "E01", self.source)
        self.assertFalse((self.folder / "raw/source").exists())

    def test_explicit_language_must_be_shared_draft(self):
        with self.assertRaisesRegex(ValueError, "last applied"):
            batch.collect(self.root, "E01", self.source, self.source / "swarmish.txt")

    def test_reject_symlinks_and_existing_destination(self):
        (self.source / "alias.json").symlink_to(self.source / "config.json")
        with self.assertRaisesRegex(ValueError, "symlink"):
            batch.collect(self.root, "E01", self.source)
        (self.source / "alias.json").unlink()
        (self.folder / "raw/source").mkdir(parents=True)
        with self.assertRaisesRegex(ValueError, "overwrite"):
            batch.collect(self.root, "E01", self.source)

    def test_reject_unknown_config_fields(self):
        batch.write(self.folder / "config.json", {**self.config, "language_max_turn": 200})
        with self.assertRaisesRegex(ValueError, "Unsupported"):
            batch.run_info(self.root, "E01")

    def test_failed_or_missing_cost_source_cannot_launch_next_phase(self):
        batch.write(self.source / "summary.json", {"creation_only": True, "creation_stop_reason": "fatal_api_error_400", "cost_incomplete": False})
        batch.collect(self.root, "E01", self.source)
        plan = {"source_run_id": "E01"}
        with self.assertRaisesRegex(ValueError, "review required"):
            batch.dependency(self.root, plan)
        receipt = batch.read(self.folder / "receipt.json")
        receipt["stop_reason"] = "all_done"
        receipt["summary"]["cost_incomplete"] = True
        batch.write(self.folder / "receipt.json", receipt)
        with self.assertRaisesRegex(ValueError, "cost reporting is incomplete"):
            batch.dependency(self.root, plan)

    def test_gameplay_translation_template_only_contains_public_fields(self):
        batch.collect(self.root, "E01", self.source)
        game = self.root / "gameplay/T01_sol"
        plan = {**self.plan, "id": "T01", "stage": "gameplay", "source_run_id": "E01", "owner": "tom"}
        config = {**self.config, "log_dir": str(game.relative_to(self.repo) / "raw")}
        batch.write(game / "plan.json", plan)
        batch.write(game / "config.json", config)
        manifest = batch.read(self.root / "batch.json")
        manifest["runs"].append({"id": "T01", "path": "gameplay/T01_sol"})
        batch.write(self.root / "batch.json", manifest)
        source = self.repo / "incoming/game"
        source.mkdir()
        batch.write(source / "config.json", config)
        batch.write(source / "glyphs.json", batch.read(self.folder / "handoff/glyphs.json"))
        shutil.copyfile(self.folder / "handoff/swarmish.txt", source / "swarmish.txt")
        batch.write(source / "summary.json", {"creation_stop_reason": "provided_language", "task_stop_reason": "escaped"})
        (source / "task_chatroom.jsonl").write_text(json.dumps({"sender": "agent_0", "text": "𗱓", "intended_meaning": "PRIVATE", "timestamp": 123}) + "\n")
        batch.collect(self.root, "T01", source)
        translation = batch.read(game / "english/translation.json")
        self.assertEqual(translation["messages"], [{"id": 1, "sender": "agent_0", "text": "𗱓", "english": None}])
        self.assertEqual(translation["status"], "pending")
        (self.folder / "handoff/swarmish.txt").write_text("CHANGED")
        with self.assertRaisesRegex(ValueError, "Frozen handoff changed"):
            batch.dependency(self.root, plan)

    def copied_manifest(self):
        root = self.repo / "complete"
        for entry in batch.read(BATCH / "batch.json")["runs"]:
            source, target = BATCH / entry["path"], root / entry["path"]
            target.mkdir(parents=True)
            shutil.copyfile(source / "plan.json", target / "plan.json")
            config = batch.read(source / "config.json")
            config["log_dir"] = str(target.relative_to(self.repo) / "raw")
            batch.write(target / "config.json", config)
        shutil.copyfile(BATCH / "batch.json", root / "batch.json")
        return root

    def test_manifest_checks_dependencies_and_owner_split(self):
        root = self.copied_manifest()
        self.assertEqual(batch.validate_manifest(root), 25)
        folder, plan, _ = batch.run_info(root, "D01")
        plan["source_run_id"] = "E01"
        batch.write(folder / "plan.json", plan)
        with self.assertRaisesRegex(ValueError, "source stage"):
            batch.validate_manifest(root)

    def test_prepare_only_has_no_api_or_execution_side_effects(self):
        root = self.copied_manifest()
        with patch("src.enc_dec.run.make_client", side_effect=AssertionError("API client must not be created")):
            batch.launch(root, "E02", prepare_only=True)
        folder, _, _ = batch.run_info(root, "E02")
        self.assertFalse((folder / "receipt.json").exists())
        self.assertFalse((folder / "execution.json").exists())
        self.assertFalse((folder / ".run.lock").exists())
        self.assertFalse((folder / "raw").exists())
        self.assertTrue(list((root / ".previews/E02").glob("*/agents.json")))


if __name__ == "__main__":
    unittest.main()
