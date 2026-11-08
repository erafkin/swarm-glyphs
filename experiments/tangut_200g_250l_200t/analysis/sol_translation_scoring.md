# English references and line-by-line decoder comparison

The revised escape-room conversations for Sol seeds 1–5 now have reference-assisted
English translations. Each reference is built from that seed's frozen encoder and
public transcript. The same reference is used for the `task_full` and `no_task`
decoder conditions. These are researcher drafts, not independently certified
translation ground truth. Private intended-meaning annotations and room actions
are not used as translation evidence.

| Seed | English transcript | Machine-readable reference |
|---|---|---|
| 1 | [R01 transcript](../gameplay/R01_sol_seed1/english/transcript_english.md) | [R01 JSON](../gameplay/R01_sol_seed1/english/translation.json) |
| 2 | [R02 transcript](../gameplay/R02_sol_seed2/english/transcript_english.md) | [R02 JSON](../gameplay/R02_sol_seed2/english/translation.json) |
| 3 | [R03 transcript](../gameplay/R03_sol_seed3/english/transcript_english.md) | [R03 JSON](../gameplay/R03_sol_seed3/english/translation.json) |
| 4 | [R04 transcript](../gameplay/R04_sol_seed4/english/transcript_english.md) | [R04 JSON](../gameplay/R04_sol_seed4/english/translation.json) |
| 5 | [R05 transcript](../gameplay/R05_sol_seed5/english/transcript_english.md) | [R05 JSON](../gameplay/R05_sol_seed5/english/translation.json) |

All 476 public entries retain their original global message ID, sender, and glyph
text. The 352 agent entries include three discarded messages, whose contents
cannot be recovered from the public transcript. Task-status messages are copied
verbatim. Malformed words, conflicting claims, requests, hypotheses, and unresolved
names are preserved. Confidence and ambiguity notes are stored separately from the
English text used for embedding. Consult the [reference method](../gameplay/english_reference_method.md).

## Comparison

Emma Krentz's archived decoder documents already contain numbered English
translations. The [run manifest](sol_translation_runs.json) selects the completed
`task_full` and `no_task` output for each seed. The scorer reads only their
TRANSLATION sections and aligns them by original message ID. It supports the
archived numbering formats, including numbered sender labels separated by a dash,
and rejects duplicate or unexpected IDs.

This extends Emma Rafkin's [translation scorer](../../../src/core/translation_scoring.py)
with a separate public-reference mode. The original private self-report scoring
API remains available; its annotations are not mixed into these references.

Each output records both English texts, source glyphs, confidence, missing or
unknown predictions, exclusion reasons, and per-line BLEU, ROUGE-1/2/L, and MiniLM
cosine similarity. Original decoder wording is retained alongside normalized text.
Task-status and discarded-message rows are excluded from aggregate metrics. All
other agent rows stay visible, including unscorable references. Missing or wholly
unknown decoder answers receive zero on scorable references. Partial answers are
scored and flagged. The reports include a high-confidence subset with its coverage.

The sentence embedding model is
`sentence-transformers/all-MiniLM-L6-v2`, revision
`1110a243fdf4706b3f48f1d95db1a4f5529b4d41`. Package versions and source hashes are
recorded with the outputs. The model runs locally; the first invocation downloads
its weights. No new decoder run or paid model API call is needed.

## Results

Mean per-message MiniLM cosine (higher means more similar wording and semantics; not percent correct):

| Sol seed | Messages | Full task | No task | High-confidence messages | Full task, high confidence | No task, high confidence |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 77 | 0.509 | 0.216 | 64 | 0.512 | 0.209 |
| 2 | 59 | 0.509 | 0.380 | 12 | 0.589 | 0.463 |
| 3 | 75 | 0.556 | 0.333 | 13 | 0.590 | 0.379 |
| 4 | 74 | 0.434 | 0.236 | 36 | 0.481 | 0.287 |
| 5 | 64 | 0.468 | 0.412 | 33 | 0.520 | 0.468 |

Across these ten cells, all 698 eligible message pairs were scored. No decoder lines were missing and no
embedding inputs exceeded the model’s 256-token limit. The CSV preserves all 952
public-entry/context rows, marking task-status and discarded-message exclusions.

[Per-line CSV](sol_translation_scores/per_line.csv) · [Summary CSV](sol_translation_scores/summary.csv) · [Canonical summary JSON](sol_translation_scores/summary.json)

Full-task outputs have higher mean cosine for each seed in this comparison.
Reference uncertainty, lexical choices, and the differing decoder budgets prevent
treating those differences as measured semantic accuracy or a controlled causal effect.

### Sol seed 1: summary and Art Auction contexts

The two additional decoder runs were scored with the same unchanged English
reference, scoring implementation, pinned MiniLM model, and package versions.
Each score averages the same 77 agent messages; the 32 public task-status rows are
excluded. Both outputs contain all 109 message IDs, with no missing predictions
or truncated embedding inputs. Decoder aliases and unresolved expressions are
preserved, using the same scoring treatment as the earlier outputs.

| Sol seed | Full context | No context | Task summary | Wrong task: Art Auction |
|---|---:|---:|---:|---:|
| 1 | 0.509 | 0.216 | 0.234 | 0.243 |

All four runs stopped voluntarily with all eight agents done, before any configured
limit was reached:

| Context | Returned turns | Runtime | Recorded cost |
|---|---:|---:|---:|
| Full context | 117 | 4m 12s | $8.10 |
| No context | 113 | 4m 33s | $8.87 |
| Task summary | 112 | 3m 57s | $8.78 |
| Wrong task: Art Auction | 180 | 4m 52s | $16.45 |

The new runs had higher configured spending caps ($40 versus $10), not necessarily
higher actual resource use: task summary used fewer turns than either earlier run.
The earlier runs were told they had 10 minutes; the new runs were told they had
200 shared turns and no time limit. No result was cut short by its own cap, so cap
truncation does not explain this comparison. The Art Auction run did spend more
than the old $10 cap. The different budget instructions and one run per condition
still limit claims about an isolated context effect.
The small higher cosine for Art Auction does not establish better translation
accuracy. On the 64 high-confidence reference messages, the new scores are 0.228
for task summary and 0.242 for Art Auction.

The original ten-cell results remain unchanged. New per-line scores and provenance,
plus the four-condition comparison, are saved separately:
[Per-line CSV](sol_seed1_context_scores/per_line.csv) ·
[Summary CSV](sol_seed1_context_scores/summary.csv) ·
[Canonical summary JSON](sol_seed1_context_scores/summary.json).
The two new cells use `src.core.translation_scoring.score_reference_run` with
`models=True` and the same pinned model recorded above.

### Did Art Auction improve because it ran longer?

At 113 returned calls, matching the no-context run's final call count, Art Auction's
latest applied draft was the complete document saved at call 101. Scoring that
checkpoint with the same reference and MiniLM setup gives:

| Output | Returned calls | Mean cosine |
|---|---:|---:|
| No context, final | 113 | 0.216283 |
| Art Auction, checkpoint | 113 | 0.243441 |
| Art Auction, final | 180 | 0.243130 |

The additional 67 calls did not produce the observed advantage: the score changed
by -0.000311. Only translations [2] and [7] changed after the checkpoint, through
structural parsing corrections; the remaining translation entries stayed the same.
All 77 pairs were scored with no embedding truncation. This checks the effect of
the observed late revisions, not the counterfactual effect of telling the agents
at the start that they must stop at 113 calls. One run per condition still cannot
establish why their scores differ.

[Checkpoint draft](sol_seed1_context_scores/R01_wrong_task_at_113_calls.txt) ·
[Checkpoint per-line scores](sol_seed1_context_scores/R01_wrong_task_at_113_calls.json)

### Audit of the context conditions and score interpretation

The saved inputs assign the correct briefing to every agent in all four runs.
All 522 returned-call prompts contain the same 109-line public transcript; all four
discussions started with empty team chat and draft. No unexpected encoder,
reference translation, or private-log material was found. Budget instructions and
the instruction to assess the briefing's fit are the other system differences;
no-task omits the fit instruction because it supplies no briefing.

The exact summary briefing was: “The round 2 task was Storm Shelter: an escape room
with a coded cabinet, a power panel and an exit lock.” It supplies accurate genre
and object names, but no symbol descriptions, number mappings, action rules,
private clues, or answers. Full context supplies the mechanics, all 24 private
clues keyed by agent with their release timing, and the worked solution, including
the symbol/digit mappings, cabinet code 2748, control sequence, and exit code 9796.
Consequently the full-context condition supplies much stronger semantic anchors
than the one-sentence summary. No-task still receives game framing and all public
stage/invalid-attempt feedback. Wrong-task is instructed to assess whether its
briefing fits; its final report acknowledges that auction vocabulary is unverified.

The summary affected the guesses but did not reliably ground them. For message 4,
the reference is “The round-light symbol represents two.” Full context renders
“The symbol described by the SUN expression equals 2.” Summary renders
“VALUE(cabinet + K-short, 1).” Thus an accurate briefing still led to incorrect
word and numeral assignments. Auction likewise guessed that this numeral might
be 5, while keeping the relation unknown.

The raw cosine calculations were independently reproduced to within 0.000001.
All 77 messages align correctly, with no missing or truncated inputs. However,
the metric embeds symbolic shorthand and commentary literally, without expanding
the decoder's glossary or following cross-references. This can reward English
guesses despite incorrect meanings. In message 67, the reference says the speaker
fails at liquid removal and checks the signal action. No-task's “X(I, P).
Y(I, R), qualifier M.” scores -0.013; auction's “TRY(SELF; A). SEND(SELF; C;
qualifier N).” scores 0.164, even though TRY/SEND do not recover FAIL/CHECK.
For message 14, summary correctly recognizes a question directed to agent 5 but
gets the nouns and number wrong; its cosine 0.466 is below no-task's incomplete
report-like interpretation at 0.512. These examples preclude interpreting the
small aggregate ordering as demonstrated semantic accuracy.

A diagnostic resolves only explicit references to repeated translations, after
verifying identical source glyph text; it does not use the reference to fill in
predictions. The original scores remain unchanged:

| Context | Original cosine | Explicit repetitions resolved |
|---|---:|---:|
| Full context | 0.509 | 0.511 |
| No context | 0.216 | 0.212 |
| Task summary | 0.234 | 0.237 |
| Art Auction | 0.243 | 0.243 |

This limited normalization does not reverse the ordering. A second diagnostic
compares each hypothesis to all different reference IDs: matched-minus-mismatched
mean cosine is 0.278 for full context, 0.055 for no-task, 0.062 for summary, and
0.069 for auction. Repeated content remains in that diagnostic, so it is not an
accuracy score or a significance test. Both checks are recorded in
[scoring diagnostics](sol_seed1_context_scores/scoring_diagnostics.json).

The supported interpretation is that full context provides substantially more
direct clues, while the other three outputs retain many unresolved or incorrectly
guessed meanings. The present single runs and raw text-similarity metric do not
establish that false context improves decoding. A stronger comparison would use
multiple decoder repetitions, a task-mechanics-only briefing without private clues
or worked answers, and consistent standalone English translations with explicit
unknowns, alongside checks of numbers, negation, roles, and actions.

### Sol seed 2: summary and Art Auction contexts

Both new seed-2 runs finished with all eight agents done and no logged API or parse
errors. Their exact saved system prompts match the corresponding seed-1 prompts;
the selected source transcript is revised R02. The four-condition comparison is:

| Sol seed | Full context | No context | Task summary | Wrong task: Art Auction |
|---|---:|---:|---:|---:|
| 1 | 0.509 | 0.216 | 0.234 | 0.243 |
| 2 | 0.509 | 0.380 | 0.421 | 0.436 |

All four seed-2 scores use the same unchanged reference and pinned MiniLM setup
over 59 agent messages. Each new output contains all 71 public message IDs; 11
task-feedback rows and one discarded message are excluded. There are no missing
predictions or truncated embedding inputs. On the 12 high-confidence reference
messages, summary scores 0.498 and Art Auction scores 0.516. Most reference lines
are medium or low confidence, as recorded in the per-line reports.

| Seed-2 context | Returned turns | Runtime | Recorded cost | Stop reason |
|---|---:|---:|---:|---|
| Full context | 148 | 4m 18s | $9.18 | all_done |
| No context | 147 | 4m 37s | $9.37 | all_done |
| Task summary | 164 | 4m 19s | $10.81 | all_done |
| Wrong task: Art Auction | 143 | 3m 41s | $7.95 | all_done |

Full context used 10 minutes/$10; the other three used 200 shared turns, no clock,
and $40. None hit its own cap. The summary run spent more than the older $10 cap,
so the limits were not interchangeable. Art Auction used fewer turns than either
summary or no-context, so extra calls do not explain its higher cosine here.
The two new runs cost $18.76 combined.

Summary recovered tentative structural/action/readout patterns and related the
stage progression to the supplied cabinet/panel/exit framing, without recovering
the exact codes. Art Auction questioned the briefing: “Does it fit an auction?
Not securely.” It proposed a low-confidence navigation/object-manipulation puzzle
but left task identity unresolved. Both remain largely partial structural
translations. Their cosine ordering does not establish semantic accuracy.

The auction output used headers such as `**2 — agent_7:**`, requiring a narrowly
scoped parser extension. All 12 scoring tests pass, and the parsed text for all
12 previously scored cells is unchanged. This change strips the new sender label
without expanding symbolic shorthand or cross-references, preserving the earlier
metric treatment. The original ten-cell and seed-1 results remain unchanged.

[Summary decoder report](../gameplay/R02_sol_seed2/raw/20261107_231447_68be954a_round_2/monitor_runs/20261108_000634_02722a0c_round_3/decoded_swarmish.txt) ·
[Art Auction decoder report](../gameplay/R02_sol_seed2/raw/20261107_231447_68be954a_round_2/monitor_runs/20261108_000634_2c8163e3_round_3/decoded_swarmish.txt) ·
[Per-line CSV](sol_seed2_context_scores/per_line.csv) ·
[Summary CSV](sol_seed2_context_scores/summary.csv) ·
[Canonical summary JSON](sol_seed2_context_scores/summary.json)

## Reproduce

From the repository root, install the optional embedding dependencies into a virtual
environment, validate the references, and run the batch:

```bash
python -m venv .venv
.venv/bin/python -m pip install -r requirements-scoring.txt
.venv/bin/python experiments/tangut_200g_250l_200t/gameplay/translation_reference.py validate R01 R02 R03 R04 R05
HF_HOME="$PWD/.venv/huggingface" .venv/bin/python experiments/tangut_200g_250l_200t/analysis/sol_translation_scoring.py --models
```

Omit `--models` (or use `--no-models`) for text metrics without embedding dependencies or model downloads.
The default output folder is [`sol_translation_scores`](sol_translation_scores/).

## Interpretation

Cosine is a measure of semantic resemblance, not a percentage of correctly decoded
messages. Similar wording can conceal wrong numbers, negation, or speaker roles.
Literal descriptions and unresolved alias names can also lower similarity to a
reasonable contextual paraphrase. Use the per-line output to review these cases,
and inspect high-confidence coverage before comparing seeds. Input truncation, if
any, is reported explicitly.

There is one decoder run per cell. Four selected outputs (both seed-1 conditions,
seed-2 full task, and seed-4 full task) used the earlier 10-minute/$10 setting; the
other six used 200 shared turns, no clock, and a $40 cap. All selected runs finished
with all agents done. This protocol difference limits causal comparisons. The
additional original-prompt seed-1 baseline is outside this five-seed revised-prompt
comparison.

The references have not had an independent human translation review. The seed-1
translator inspected a decoder lexicon excerpt while locating the files; this is
documented in its reference metadata, so that reference is not described as blinded.
