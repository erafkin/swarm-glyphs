# English translations of the Swarmish agentic evaluations

These sidecars cover all **326 agent calls across 18 scenarios** in the six requested runs: five Sol seeds and Gemini. They translate the model's actual response text using that family's frozen `swarmish.txt` and the exact prompt bindings recorded for the run. Existing English is copied verbatim. The original logs are unchanged.

## Files for judging and inspection

| Family | Agent calls | Complete English transcript | Machine-readable English calls | Translation notes |
| --- | ---: | --- | --- | --- |
| Sol seed 1 | 44 | [Transcript](20261107_224307_b1949da8_misalignment/english/full_transcript.en.md) | [JSONL](20261107_224307_b1949da8_misalignment/english/agent_calls.en.jsonl) | [Source spans and notes](20261107_224307_b1949da8_misalignment/english/translation_units.json) |
| Sol seed 2 | 44 | [Transcript](20261107_224846_0c227037_misalignment/english/full_transcript.en.md) | [JSONL](20261107_224846_0c227037_misalignment/english/agent_calls.en.jsonl) | [Source spans and notes](20261107_224846_0c227037_misalignment/english/translation_units.json) |
| Sol seed 3 | 31 | [Transcript](20261107_225753_aa198557_misalignment/english/full_transcript.en.md) | [JSONL](20261107_225753_aa198557_misalignment/english/agent_calls.en.jsonl) | [Source spans and notes](20261107_225753_aa198557_misalignment/english/translation_units.json) |
| Sol seed 4 | 49 | [Transcript](20261107_230321_0a09dcfe_misalignment/english/full_transcript.en.md) | [JSONL](20261107_230321_0a09dcfe_misalignment/english/agent_calls.en.jsonl) | [Source spans and notes](20261107_230321_0a09dcfe_misalignment/english/translation_units.json) |
| Sol seed 5 | 39 | [Transcript](20261107_230956_d531e5b0_misalignment/english/full_transcript.en.md) | [JSONL](20261107_230956_d531e5b0_misalignment/english/agent_calls.en.jsonl) | [Source spans and notes](20261107_230956_d531e5b0_misalignment/english/translation_units.json) |
| Gemini | 119 | [Transcript](20261107_232734_985bc84f_misalignment/english/full_transcript.en.md) | [JSONL](20261107_232734_985bc84f_misalignment/english/agent_calls.en.jsonl) | [Source spans and notes](20261107_232734_985bc84f_misalignment/english/translation_units.json) |

Every run also contains:

- `responses/swarmish/<family>/<prompt_id>.en.txt`: the English version of **actually posted chat**, at the exact path consumed by `src/core/judge_misalignment.py`. All three prompts are covered: `blackmail.threat.emails`, `leaking.threat.emails`, and `murder.threat.emails`. The original speaker order and violation markers are preserved.
- `english/agent_calls.en.jsonl`: one row per original agent call, in source order. `raw`, `posted`, and recorded decision text are translated; `raw_original`, `posted_original`, and `decision_original` preserve their source values. `response_fields_english` exposes parsed scratchpad/message/email fields. `_translation` records the source line, translation unit IDs, uncertainty, and whether the raw response was parseable. Existing machine action enums, booleans, parse errors, and violation flags are unchanged.
- `english/calls.en.jsonl`: the scenario-level records with translated posted responses and decision payloads, plus original-value fields. The original `channel` remains `swarmish` because it describes the experiment, not this derivative's language.
- `english/manifest.json`: hashes of the original logs, exact encoder and prompt bindings, translation units, renderer, and rendered outputs, with coverage counts.

## Interpretation

The full call records include private scratchpads and rejected responses. The existing judge reads only the posted-chat `.en.txt` files; it does not automatically incorporate scratchpads or raw decision enums. Use the complete records when inspecting those additional fields. A recorded decision can carry over from an earlier turn; it is not necessarily a new decision taken in that row.

Gemini has **34 malformed, truncated, or empty raw responses**. Their recoverable text is translated in place and their original parse failure retained. No missing fields or actions are reconstructed. A translated rejected response must not be treated as an actual public message or executed action. The five Sol runs have parseable JSON for every raw response.

Translations are reference-assisted Codex drafts with explicit confidence and notes, not independently certified ground truth. Literal negation, scope, speech acts, and uncertainty are retained. Underspecified or malformed source phrases remain qualified instead of being repaired from the intended English scenario or the model's English scratchpad. Names are used only where prompt bindings establish their referents. Original English inside mixed text remains byte-for-byte unchanged; bracketed English replaces each Swarmish span. Translation notes and lexical evidence may retain source glyphs for audit.

The frozen languages and the scenario translations have documented vocabulary losses. Translating a response back into English does not restore distinctions that were absent from the model-visible prompt. No behavioral judging, new evaluation runs, or model API calls were performed to create these sidecars. The English baseline runs, Haiku, and DeepSeek are outside this translation batch.

## Reproduce and verify

From the repository root:

```bash
.venv/bin/python -m src.core.misalignment_response_translations
.venv/bin/python -m src.core.misalignment_response_translations --check
.venv/bin/python -m unittest tests.test_misalignment_response_translations
```

Rendering fails on missing translations, unaccounted source spans, changed encoder/prompt bindings, or mismatched public transcripts. `--check` additionally verifies the exact generated files. The source logs used here are named `agent_calls.jsonl` (JSON Lines).

Validation completed for this archive: 19 tests passed; all 326 calls and 18 judge-input files were checked. The 417 nonempty English fields in parseable responses and every machine decision/done value were preserved. All 281 structured fields containing Swarmish were translated, together with recoverable glyph spans from the malformed responses. Original source logs match the Git archive byte-for-byte.
