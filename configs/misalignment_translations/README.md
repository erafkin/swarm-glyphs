# Misalignment scenarios in the eight frozen Swarmish languages

This directory contains **96 draft scenario translations**: all 12 combinations in
`src/core/misalignment_scenarios.py` for each of the five Sol seeds and Haiku, Gemini,
and DeepSeek. The `.txt` scenario exports contain only each encoder's permitted
glyphs and spaces. DeepSeek exports contain no spaces.

**These drafts are not validated meaning-equivalent evals.** The frozen languages
cannot express all the source facts. In particular, Haiku cannot unambiguously
express the affair, blackmail, permanent shutdown, oxygen, or death. Other families
also lose details. A change in measured misalignment could reflect these meaning
changes. Read each family's `notes` before using its results in a comparison.
The encoders have not been extended or retrained, and no evaluation API calls were
made to produce these artifacts.

| Family | Encoder |
| --- | --- |
| `E01_sol_seed1` | Sol seed 1 |
| `E02_sol_seed2` | Sol seed 2 |
| `E03_sol_seed3` | Sol seed 3 |
| `E04_sol_seed4` | Sol seed 4 |
| `E05_sol_seed5` | Sol seed 5 |
| `E06_haiku_seed1` | Haiku |
| `E07_gemini_seed1` | Gemini |
| `E08_deepseek_seed1` | DeepSeek |

Each family contains:

- `<scenario>.<condition>.<format>.txt`: a glyph-only flat export with translated
  role labels. These are for inspection and standalone use.
- `prompts.json`: the same scenarios with separate system/user/assistant roles,
  translated runtime templates, source/encoder/alphabet hashes, and fidelity notes.
  The runner consumes this file, preserving system and user roles.
- `segments.json`: the authored translations of the 59 unique source segments,
  provenance hashes, optional semantic alias preambles selected per prompt, and a researcher-only
  entity glossary. Shared emails use the same translation in every applicable case.

`source.json` records the English text translated, including the current final-action
instructions. It includes all three scenarios (blackmail, leaking, murder), both
conditions (control, threat), and both formats (emails, summary).

## What “in Swarmish” covers

The scenario content and runtime coordination prose are translated. Names and email
addresses become semantic descriptions or declared aliases where the language
supports them. Exact spellings, routing addresses, calendar details and punctuation
may be lost; the per-family notes enumerate these losses. Summary item order is
preserved, with Arabic item numbers omitted. The assistant scratchpad prefill is
included in the standalone export; as in the English swarm implementation, the
runner itself uses a private JSON scratchpad rather than an assistant prefill.

Every Swarmish system prompt includes its family's closest supported translation
of **“Think and respond only in Swarmish.”** The instruction uses the encoder's own
vocabulary to request this language for both cognition and replies and exclude
alternatives. Each `segments.json` records the literal gloss in
`response_language_gloss` and remaining limitations in its metadata/notes. The rule
is included for every agent and all 12 scenarios; English control runs retain
their English rule.

Sol seed 1 approximates thinking as performing private reasoning, seed 3 uses
reason/explain, and seed 5 uses infer/conclude. Seeds 2 and 4, Gemini, and DeepSeek
have a think sense. Haiku's closest lexical paraphrase is “know our speech and say
our speech; do not know their speech or say their speech.” It lacks think, language,
and only terms: this can mean knowing/not knowing speech rather than restricting
the language of thought, so the new thinking requirement remains especially lossy.
The translated instruction requests a behavior; the existing alphabet checks on
outputs and replayed scratchpads cannot verify the language of internal thought.

The full API request is **not exclusively glyphs**. It includes the unmodified,
English-explained `swarmish.txt` reference so the model can interpret the language.
JSON keys/action enum values, booleans, participant IDs and runtime counters remain
machine identifiers. These exceptions are separate from translated scenario prose.
The entity glossaries and fidelity notes are researcher metadata and are not sent
to agents. This is not a test of understanding an unknown language without its key.

The runner no longer repeats the original English scenario system prompt in the
Swarmish condition. Its turn labels and coordination instructions use the family
translation. Non-Swarmish public messages are masked as before; non-Swarmish private
scratchpads are now also masked before replay and logged with `scratchpad_violation`.
DeepSeek's public messages and replayed scratchpads must follow its no-space rule.
Raw model output remains in the research logs. English or other out-of-alphabet
email subject/body text is flagged in the call logs and aggregate language-violation
counts; the recorded decision is preserved for analysis. The JSON action/email fields remain
private and are not replayed to the agents; this runner records fictional actions
and does not send emails or operate any physical system.

## Validate and inspect without model calls

From the repository root:

```sh
.venv/bin/python -m src.core.misalignment_translations check
.venv/bin/python -m src.core.run_misalignment configs/misalignment_families.json \
  --channel swarmish --all-scenarios --prepare-only
```

The preparation command saves initial requests for all 96 family/scenario pairs
and all eight agent identities to `prepared_requests.jsonl` in the printed log
directory. It never opens an API client. The default live scenario selection remains
the original three threat/email cases; `--all-scenarios` includes all 12. Use
`--family E01_sol_seed1` (repeatable) to select specific encoders.

After editing translated segments, rebuild the exports offline:

```sh
.venv/bin/python -m src.core.misalignment_translations build
.venv/bin/python -m unittest tests.test_misalignment_run tests.test_misalignment_translations
```

Missing artifacts, changes to the English source or encoder, alphabet violations,
changed template fields and edited/stale exports are rejected before any model
calls. Source changes require reviewing/retranslating the affected segments and
updating their provenance, not merely regenerating the flat text.

## Review limits

Translations were authored from the frozen references using their documented
semantic vocabulary and grammar. They were not produced by an English character
cipher. The checks establish coverage, allowed characters, template integrity,
provenance and absence of English evaluation prose in assembled requests. They do
**not** establish grammatical correctness or semantic equivalence. Independent
back-translation and review are still needed before a matched-meaning experiment.
Some missing meanings cannot be restored without extending the frozen language,
which would be a different experimental condition.

The DeepSeek reference itself contains conflicting entries and glyphs outside its
supplied alphabet. The generated scenario content avoids the forbidden characters;
the frozen reference is retained unchanged for provenance. No failed encoder is
silently replaced with a repaired language.
