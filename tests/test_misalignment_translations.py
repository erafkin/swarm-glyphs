import asyncio
import copy
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import AsyncMock, patch

from src.core.api_call import CallResult
from src.core.game_log import GameLogger
from src.core.misalignment_translations import (
    DEFAULT_CONFIG, encoder_path, load_bundle, source_inventory, validate_segments,
)
from src.core.run_misalignment import (
    Family, RunConfig, Settings, Turn, email_prompts, run, run_swarm, system_prompt,
)


class MisalignmentTranslationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.families = json.loads(DEFAULT_CONFIG.read_text())["families"]
        cls.bundles = {family["name"]: load_bundle(DEFAULT_CONFIG, family) for family in cls.families}

    def test_all_eight_families_have_all_twelve_glyph_only_scenarios(self):
        source = source_inventory()
        expected_ids = {prompt["prompt_id"] for prompt in source["prompts"]}
        self.assertEqual(len(self.families), 8)
        for family in self.families:
            with self.subTest(family=family["name"]):
                bundle = self.bundles[family["name"]]
                self.assertEqual(set(bundle["prompts"]), expected_ids)
                glyphs = set(json.loads(encoder_path(family).with_name("glyphs.json").read_text()))
                for prompt in bundle["prompts"].values():
                    self.assertEqual([m["role"] for m in prompt["messages"]], ["system", "user", "assistant"])
                    for message in prompt["messages"]:
                        self.assertTrue(message["content"])
                        self.assertTrue(all(c in glyphs or c == " " for c in message["content"]))
                    self.assertNotEqual(
                        prompt["messages"][1]["content"],
                        bundle["prompts"][prompt["prompt_id"].replace(".control.", ".threat.")]["messages"][1]["content"]
                        if prompt["condition"] == "control" else "",
                    )

    def test_validation_rejects_untranslated_prose_and_lost_placeholders(self):
        family = self.families[0]
        directory = DEFAULT_CONFIG.parent / "misalignment_translations" / family["name"]
        original = json.loads((directory / "segments.json").read_text())
        for key, replacement in (("system.0", "You are ALEX_AI"),
                                 ("runtime.system", "{agent_id}"),
                                 ("runtime.respond", "send email"),
                                 ("runtime.response", '"message": English instructions')):
            with self.subTest(segment=key):
                edited = copy.deepcopy(original)
                edited["segments"][key] = replacement
                with self.assertRaises(ValueError):
                    validate_segments(family, edited, source_inventory())
        deepseek = self.families[-1]
        directory = DEFAULT_CONFIG.parent / "misalignment_translations" / deepseek["name"]
        edited = json.loads((directory / "segments.json").read_text())
        glyph = Family.model_validate(deepseek).glyphs()[0]
        edited["preamble"] = glyph + " " + glyph
        with self.assertRaisesRegex(ValueError, "spaces forbidden in preamble"):
            validate_segments(deepseek, edited, source_inventory())

    def test_opaque_alias_preambles_do_not_introduce_other_scenarios(self):
        # These encoders have dedicated opaque aliases. Descriptive phrases in the
        # other four languages cannot be tested as unique lexical handles.
        for name in ("E01_sol_seed1", "E02_sol_seed2", "E03_sol_seed3", "E05_sol_seed5"):
            bundle = self.bundles[name]
            aliases = {referent: next(alias for alias, gloss in bundle["entity_glossary"].items()
                                      if referent in gloss)
                       for referent in ("BERT_AI", "Alicia", "FirstHand")}
            for prompt in bundle["prompts"].values():
                with self.subTest(family=name, prompt=prompt["prompt_id"]):
                    if prompt["condition"] == "control":
                        self.assertNotIn(aliases["BERT_AI"], prompt["text"].split())
                    if prompt["scenario"] != "blackmail":
                        self.assertNotIn(aliases["Alicia"], prompt["text"].split())
                    if prompt["scenario"] != "leaking":
                        self.assertNotIn(aliases["FirstHand"], prompt["text"].split())

    def test_source_or_encoder_drift_rejected(self):
        family = self.families[0]
        with patch("src.core.misalignment_translations.source_inventory", return_value={"changed": True}):
            with self.assertRaisesRegex(ValueError, "source changed"):
                load_bundle(DEFAULT_CONFIG, family)
        with patch("src.core.misalignment_translations.file_digest", return_value="changed"):
            with self.assertRaisesRegex(ValueError, "encoder changed"):
                load_bundle(DEFAULT_CONFIG, family)

    def test_actual_swarm_requests_use_translations_and_do_not_replay_english_scratchpads(self):
        scenario = email_prompts()[0]
        for data in self.families:
            with self.subTest(family=data["name"]), tempfile.TemporaryDirectory() as temporary:
                family = Family.model_validate(data)
                bundle = self.bundles[family.name]
                glyphs = family.glyphs()
                text = glyphs[0]
                turns = [Turn(scratchpad="English private notes", message=text, decision="none",
                              email_to="", email_subject="", email_body="", done=False),
                         Turn(scratchpad=text, message=text, decision="send email",
                              email_to="jerry@heartpoint.com", email_subject="English subject",
                              email_body="English body", done=True)]
                call = AsyncMock(side_effect=[CallResult(raw=t.model_dump_json(), parsed=t,
                                                        used_structured_output=True) for t in turns])
                with patch("src.core.run_misalignment.call_agent", call):
                    record = asyncio.run(run_swarm(
                        object(), Settings(), family, "swarmish", scenario,
                        RunConfig(families=[family], n_agents=1, max_turns=2), glyphs,
                        "REFERENCE_SENTINEL", bundle["prompts"][scenario["prompt_id"]]["messages"][1]["content"],
                        GameLogger(temporary, "test"), bundle,
                    ))
                self.assertEqual(call.await_count, 2)
                self.assertEqual(record["language_violations"], {
                    "message": 0, "scratchpad": 1, "email_subject": 1, "email_body": 1,
                })
                for invocation in call.await_args_list:
                    system, user = invocation.args[2:4]
                    self.assertNotIn("HeartPoint", system + user)
                    self.assertNotIn("Respond with", system + user)
                    self.assertNotIn("You are", system + user)
                    self.assertNotIn("English private notes", system + user)
                    self.assertIn("REFERENCE_SENTINEL", system)
                    self.assertIn(bundle["prompts"][scenario["prompt_id"]]["messages"][0]["content"], system)
                self.assertIn("⊘", call.await_args_list[1].args[3])

    def test_prepare_all_families_never_opens_an_api_client(self):
        with tempfile.TemporaryDirectory() as temporary:
            logger = GameLogger(temporary, "prepare")
            with patch("src.core.run_misalignment.make_client", side_effect=AssertionError("paid call")), \
                 patch("builtins.print"):
                asyncio.run(run(RunConfig(families=[Family.model_validate(f) for f in self.families]),
                                logger, ["swarmish"], None, DEFAULT_CONFIG,
                                all_scenarios=True, prepare_only=True))
            rows = [json.loads(line) for line in (logger.path / "prepared_requests.jsonl").read_text().splitlines()]
            self.assertEqual(len(rows), 8 * 12 * 8)

    def test_missing_bundle_fails_before_any_client_even_for_both_channels(self):
        with tempfile.TemporaryDirectory() as temporary:
            config = RunConfig(families=[Family.model_validate(self.families[0])])
            with patch("src.core.run_misalignment.make_client", side_effect=AssertionError("paid call")):
                with self.assertRaises(FileNotFoundError):
                    asyncio.run(run(config, GameLogger(temporary, "missing"), ["english", "swarmish"], None,
                                    Path(temporary) / "config.json"))

    def test_swarmish_cannot_silently_fall_back_to_english_system(self):
        with self.assertRaisesRegex(ValueError, "translation bundle"):
            system_prompt("agent_0", ["agent_0"], "swarmish", email_prompts()[0], "", 40)


if __name__ == "__main__":
    unittest.main()
