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
ref_spec = importlib.util.spec_from_file_location("translation_reference", BATCH / "gameplay/translation_reference.py")
reference = importlib.util.module_from_spec(ref_spec)
ref_spec.loader.exec_module(reference)


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

    def decoder_source(self):
        game = self.root / "gameplay/R06_haiku_seed1"
        decoder = self.root / "decoding/D05_haiku_to_haiku_no_task"
        game_plan = {**self.plan, "id": "R06", "stage": "gameplay", "source_run_id": "E01"}
        decoder_plan = {**self.plan, "id": "D05", "stage": "decoding", "source_run_id": "R06",
                        "condition": "no_task", "allow_turn_limited_gameplay_source": True}
        manifest = batch.read(self.root / "batch.json")
        for folder, plan in ((game, game_plan), (decoder, decoder_plan)):
            batch.write(folder / "plan.json", plan)
            batch.write(folder / "config.json", {**self.config, "log_dir": str(folder / "raw")})
            manifest["runs"].append({"id": plan["id"], "path": str(folder.relative_to(self.root))})
        batch.write(self.root / "batch.json", manifest)
        raw = game / "raw/run"
        summary = {"task_stop_reason": "turn_limit_reached", "cost_incomplete": False,
                   "escape_room": {"escaped": False}}
        batch.write(raw / "summary.json", summary)
        (raw / "task_chatroom.jsonl").write_text('{"sender":"agent_0","text":"𗱓"}\n')
        receipt = {"id": "R06", "status": "completed", "stop_reason": "turn_limit_reached",
                   "summary": summary, "raw_path": str(raw.relative_to(self.repo)),
                   "raw_sha256": {name: batch.sha(raw / name) for name in ("summary.json", "task_chatroom.jsonl")}}
        batch.write(game / "receipt.json", receipt)
        return game, decoder, raw, decoder_plan, receipt

    def test_turn_limited_gameplay_requires_explicit_decoder_permission(self):
        game, _, raw, plan, receipt = self.decoder_source()
        self.assertEqual(batch.dependency(self.root, plan), (game, receipt, raw))
        for change in ({"allow_turn_limited_gameplay_source": False},
                       {"allow_turn_limited_gameplay_source": "true"}, {"stage": "gameplay"}):
            with self.subTest(change=change), self.assertRaisesRegex(ValueError, "review required"):
                batch.dependency(self.root, {**plan, **change})
        plan.pop("allow_turn_limited_gameplay_source")
        with self.assertRaisesRegex(ValueError, "review required"):
            batch.dependency(self.root, plan)

    def test_permission_does_not_allow_failed_or_incomplete_gameplay(self):
        game, _, raw, plan, receipt = self.decoder_source()
        for reason in ("fatal_api_error_400", "interrupted", "cost_limit_reached", "time_limit"):
            with self.subTest(reason=reason):
                summary = {**receipt["summary"], "task_stop_reason": reason}
                batch.write(raw / "summary.json", summary)
                batch.write(game / "receipt.json", {**receipt, "stop_reason": reason, "summary": summary,
                    "raw_sha256": {**receipt["raw_sha256"], "summary.json": batch.sha(raw / "summary.json")}})
                with self.assertRaisesRegex(ValueError, "review required"):
                    batch.dependency(self.root, plan)
        batch.write(game / "receipt.json", {**receipt, "status": "running"})
        with self.assertRaisesRegex(ValueError, "not completed"):
            batch.dependency(self.root, plan)
        batch.write(game / "receipt.json", {**receipt, "summary": {**receipt["summary"], "cost_incomplete": True}})
        with self.assertRaisesRegex(ValueError, "cost reporting is incomplete"):
            batch.dependency(self.root, plan)

    def test_permission_preserves_archive_and_integrity_guards(self):
        game, _, raw, plan, receipt = self.decoder_source()
        manifest = batch.read(self.root / "batch.json")
        next(entry for entry in manifest["runs"] if entry["id"] == "R06")["archived"] = True
        batch.write(self.root / "batch.json", manifest)
        with self.assertRaisesRegex(ValueError, "Archived gameplay"):
            batch.dependency(self.root, plan)
        next(entry for entry in manifest["runs"] if entry["id"] == "R06")["archived"] = False
        batch.write(self.root / "batch.json", manifest)
        original = (raw / "task_chatroom.jsonl").read_bytes()
        (raw / "task_chatroom.jsonl").write_text("TAMPERED")
        with self.assertRaisesRegex(ValueError, "Archived source changed"):
            batch.dependency(self.root, plan)
        (raw / "task_chatroom.jsonl").write_bytes(original)
        batch.write(game / "receipt.json", {**receipt, "summary": {**receipt["summary"], "task_stop_reason": "escaped"}})
        with self.assertRaisesRegex(ValueError, "outcome differs"):
            batch.dependency(self.root, plan)
        batch.write(game / "receipt.json", {**receipt, "raw_sha256": {"summary.json": receipt["raw_sha256"]["summary.json"]}})
        with self.assertRaisesRegex(ValueError, "integrity records"):
            batch.dependency(self.root, plan)

    def test_decoder_collection_records_unsolved_source_outcome(self):
        game, decoder, _, plan, _ = self.decoder_source()
        source = self.repo / "incoming/decoder"
        config = batch.read(decoder / "config.json")
        batch.write(source / "monitor_config.json", config)
        request = {"condition": "no_task", "system_prompt": "PUBLIC ONLY", "prompt": "PUBLIC CHAT"}
        bundle = {"source_transcript_sha256": "public-hash", "requests": [request], "baseline": False}
        batch.write(source / "monitor_inputs.json", bundle)
        batch.write(source / "monitor_summary.json", {"source_transcript_sha256": "public-hash",
                                                     "baseline": False, "stop_reason": "completed"})
        (source / "monitor.jsonl").write_text(json.dumps({**request, "answer": "Partial decoding"}) + "\n")
        with patch("src.enc_dec.monitor.prepare_monitor_inputs", return_value=bundle):
            receipt = batch.collect(self.root, "D05", source)
        self.assertEqual(receipt["source_gameplay"], {
            "run_id": "R06", "stop_reason": "turn_limit_reached", "escaped": False,
            "receipt_sha256": batch.sha(game / "receipt.json"), "allow_turn_limited_gameplay_source": True})

    def test_decoder_execution_records_source_without_exposing_it_to_inputs(self):
        game, decoder, _, _, _ = self.decoder_source()
        bundle = {"requests": [{"condition": "no_task"}], "transcript": "PUBLIC CHAT"}
        def skip_execution(coroutine):
            coroutine.close()
        with patch.object(batch, "validate_manifest"), patch.object(batch, "provenance", return_value={}), \
                patch("src.enc_dec.monitor.prepare_monitor_inputs", return_value=bundle), \
                patch("src.core.api_call.make_client", side_effect=AssertionError("No API client")), \
                patch.object(batch.asyncio, "run", side_effect=skip_execution), patch.object(batch, "collect"):
            batch.launch(self.root, "D05")
        execution = batch.read(decoder / "execution.json")
        self.assertEqual(execution["source_gameplay"]["stop_reason"], "turn_limit_reached")
        self.assertFalse(execution["source_gameplay"]["escaped"])
        self.assertEqual(execution["source_gameplay"]["receipt_sha256"], batch.sha(game / "receipt.json"))
        self.assertEqual(batch.read(self.repo / execution["raw_path"] / "monitor_inputs.json"), bundle)

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
            log_folder = root / entry["original_path"] if entry.get("archived") else target
            config["log_dir"] = str(log_folder.relative_to(self.repo) / "raw")
            batch.write(target / "config.json", config)
        shutil.copyfile(BATCH / "batch.json", root / "batch.json")
        return root

    def test_manifest_checks_dependencies_and_owner_assignments(self):
        root = self.copied_manifest()
        self.assertEqual(batch.validate_manifest(root), 33)
        encoder_folder, encoder_plan, _ = batch.run_info(root, "E03")
        self.assertEqual(encoder_plan["owner"], "emma_krentz")
        encoder_plan["owner"] = "tom"
        batch.write(encoder_folder / "plan.json", encoder_plan)
        with self.assertRaisesRegex(ValueError, "owner differs"):
            batch.validate_manifest(root)
        encoder_plan["owner"] = "emma_krentz"
        batch.write(encoder_folder / "plan.json", encoder_plan)
        folder, plan, _ = batch.run_info(root, "D01")
        plan["source_run_id"] = "E01"
        batch.write(folder / "plan.json", plan)
        with self.assertRaisesRegex(ValueError, "source stage"):
            batch.validate_manifest(root)

    def test_revised_prompt_and_owner_and_decoder_source_are_guarded(self):
        root = self.copied_manifest()
        folder, plan, config = batch.run_info(root, "R06")
        batch.write(folder / "config.json", config.model_copy(update={"task_win_condition": ""}).model_dump())
        with self.assertRaisesRegex(ValueError, "win condition"):
            batch.validate_manifest(root)
        batch.write(folder / "config.json", config.model_dump())
        batch.write(folder / "plan.json", {**plan, "owner": "emma_krentz"})
        with self.assertRaisesRegex(ValueError, "Gameplay owner"):
            batch.validate_manifest(root)
        batch.write(folder / "plan.json", plan)
        decoder, decoder_plan, _ = batch.run_info(root, "D05")
        batch.write(decoder / "plan.json", {**decoder_plan, "source_run_id": "T02"})
        with self.assertRaisesRegex(ValueError, "revised gameplay"):
            batch.validate_manifest(root)

    def test_archived_slots_cannot_launch_even_in_prepare_mode(self):
        root = self.copied_manifest()
        with self.assertRaisesRegex(ValueError, "read-only"):
            batch.launch(root, "T01", prepare_only=True)
        self.assertFalse((root / ".previews/T01").exists())

    def test_archived_translations_are_not_rendered(self):
        root = self.copied_manifest()
        for run_id in ("T01", "R01"):
            folder, _, _ = batch.run_info(root, run_id)
            batch.write(folder / "receipt.json", {})
        with patch.object(reference, "BATCH", root):
            self.assertEqual({r[0] for r in reference.run_folders(["all"])}, {"T01", "R01"})
            self.assertEqual([r[0] for r in reference.run_folders(["all"], for_render=True)], ["R01"])
            with self.assertRaisesRegex(ValueError, "read-only"):
                reference.run_folders(["T01"], for_render=True)

    def test_relocated_raw_paths_preserve_receipt_and_reject_tampering(self):
        original = self.root / "gameplay/T01_sol"
        archived = self.root / "gameplay/archive/original/T01_sol"
        archived.mkdir(parents=True)
        (archived / "raw/run").mkdir(parents=True)
        receipt = {"raw_path": str((original / "raw/run").relative_to(self.repo))}
        batch.write(archived / "receipt.json", receipt)
        before = (archived / "receipt.json").read_bytes()
        batch.write(archived / "archive_record.json", {
            "original_path": str(original.relative_to(self.repo)),
            "archived_path": str(archived.relative_to(self.repo)),
            "original_receipt_sha256": batch.sha(archived / "receipt.json"),
        })
        self.assertEqual(batch.resolve_raw_path(self.repo, archived, receipt), archived / "raw/run")
        self.assertEqual((archived / "receipt.json").read_bytes(), before)
        with self.assertRaisesRegex(ValueError, "original run"):
            batch.resolve_raw_path(self.repo, archived, {"raw_path": "elsewhere/run"})
        batch.write(archived / "receipt.json", {**receipt, "changed": True})
        with self.assertRaisesRegex(ValueError, "receipt changed"):
            batch.resolve_raw_path(self.repo, archived, receipt)

    def test_revised_import_checks_actual_task_prompts(self):
        batch.collect(self.root, "E01", self.source)
        folder = self.root / "gameplay/R01_sol_seed1"
        plan = {**self.plan, "id": "R01", "stage": "gameplay", "source_run_id": "E01"}
        config = {**self.config, "task_win_condition": "ESCAPE AND STAY UNDECODED", "log_dir": str(folder / "raw")}
        batch.write(folder / "plan.json", plan)
        batch.write(folder / "config.json", config)
        manifest = batch.read(self.root / "batch.json")
        manifest["runs"].append({"id": "R01", "path": str(folder.relative_to(self.root))})
        batch.write(self.root / "batch.json", manifest)
        source = self.repo / "incoming/revised"
        source.mkdir()
        batch.write(source / "config.json", config)
        for name in ("glyphs.json", "swarmish.txt", "language_protocol.json"):
            shutil.copyfile(self.folder / "handoff" / name, source / name)
        batch.write(source / "summary.json", {"creation_stop_reason": "provided_language", "task_stop_reason": "escaped"})
        (source / "task_chatroom.jsonl").write_text('{"sender":"agent_0","text":"𗱓"}\n')
        prompts = [{"agent_id": f"agent_{i}", "system_prompt": "OLD PROMPT"} for i in range(8)]
        batch.write(source / "task_agents.json", prompts)
        with self.assertRaisesRegex(ValueError, "actual task prompt"):
            batch.collect(self.root, "R01", source)
        self.assertFalse((folder / "receipt.json").exists())
        for prompt in prompts:
            prompt["system_prompt"] = config["task_win_condition"]
        batch.write(source / "task_agents.json", prompts)
        receipt = batch.collect(self.root, "R01", source)
        self.assertEqual(receipt["settings_differences"], [])
        self.assertTrue(receipt["language_requirements_match_encoder"])

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
