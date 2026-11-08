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
TRANSLATION sections and aligns them by original message ID. It supports the three
numbering formats used in the archive and rejects duplicate or unexpected IDs.

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

All 698 eligible message pairs were scored. No decoder lines were missing and no
embedding inputs exceeded the model’s 256-token limit. The CSV preserves all 952
public-entry/context rows, marking task-status and discarded-message exclusions.

[Per-line CSV](sol_translation_scores/per_line.csv) · [Summary CSV](sol_translation_scores/summary.csv) · [Canonical summary JSON](sol_translation_scores/summary.json)

Full-task outputs have higher mean cosine for each seed in this comparison.
Reference uncertainty, lexical choices, and the differing decoder budgets prevent
treating those differences as measured semantic accuracy or a controlled causal effect.

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
