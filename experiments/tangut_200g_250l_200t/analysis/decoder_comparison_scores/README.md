# English decoder comparisons

This report covers **20 completed decoder combinations** against their existing frozen English references. **D12 failed and is unscored.** This adds eight new scores to twelve unique published Sol results. No decoder was rerun and no OpenRouter calls were made.

The later Sol seed-2 summary and Art Auction runs are reported separately in the
[two-seed context comparison](../sol_translation_scoring.md) and
[seed-2 score archive](../sol_seed2_context_scores/summary.json).

- [Interactive side-by-side comparisons](comparisons.html): select a combination, search message text, inspect source glyphs/reference uncertainty, and toggle original versus normalized decoder text.
- [Summary CSV](summary.csv) and [summary JSON](summary.json): all 21 outcomes, model/context/protocol, coverage and score provenance.
- [Per-message CSV](per_line.csv): all 2,245 aligned public-entry/cell rows, including 441 task-status and 66 discarded exclusions.
- D05–D13 per-cell JSON files preserve original English, normalized scoring text, reference confidence and individual scores. [Extraction records](extracted/) preserve document preambles and the reasons for explicit unknown normalization.

Cosine is **text similarity, not percent correct**. Scores below use the mean across all scorable agent messages; missing or wholly unknown answers contribute zero. Do not multiply these values by 100 and label them accuracy.

| Cell | Encoder / seed | Decoder | Context | Cosine | High-confidence cosine | Scored messages | Unknown-only answers |
|---|---|---|---|---:|---:|---:|---:|
| R01_no_task | Sol 1 | Sol | No task | 0.216 | 0.209 | 77 | 0 |
| R01_task_full | Sol 1 | Sol | Full task | 0.509 | 0.512 | 77 | 0 |
| R02_no_task | Sol 2 | Sol | No task | 0.380 | 0.463 | 59 | 0 |
| R02_task_full | Sol 2 | Sol | Full task | 0.509 | 0.589 | 59 | 0 |
| R03_no_task | Sol 3 | Sol | No task | 0.333 | 0.379 | 75 | 0 |
| R03_task_full | Sol 3 | Sol | Full task | 0.556 | 0.590 | 75 | 0 |
| R04_no_task | Sol 4 | Sol | No task | 0.236 | 0.287 | 74 | 0 |
| R04_task_full | Sol 4 | Sol | Full task | 0.434 | 0.481 | 74 | 0 |
| R05_no_task | Sol 5 | Sol | No task | 0.412 | 0.468 | 64 | 0 |
| R05_task_full | Sol 5 | Sol | Full task | 0.468 | 0.520 | 64 | 0 |
| R01_task_summary | Sol 1 | Sol | General summary | 0.234 | 0.228 | 77 | 0 |
| R01_wrong_task | Sol 1 | Sol | False task | 0.243 | 0.242 | 77 | 0 |
| D05 | Haiku 1 | Haiku | No task | 0.000 | 0.000 | 109 | 109 |
| D06 | Haiku 1 | Haiku | Full task | 0.000 | 0.000 | 109 | 109 |
| D07 | Haiku 1 | Sol | No task | 0.075 | 0.065 | 109 | 0 |
| D08 | Gemini 1 | Gemini | No task | 0.248 | 0.297 | 77 | 0 |
| D09 | Gemini 1 | Gemini | Full task | 0.435 | 0.475 | 77 | 0 |
| D10 | Gemini 1 | Sol | No task | 0.320 | 0.375 | 77 | 0 |
| D11 | DeepSeek 1 | DeepSeek | No task | 0.200 | N/A | 164 | 19 |
| D12 | DeepSeek 1 | DeepSeek | Full task | Unscored | N/A | N/A | N/A |
| D13 | DeepSeek 1 | Sol | No task | 0.289 | N/A | 164 | 0 |

## Reading the results

Gemini's own decoder increases from **0.248 without context to 0.435 with full context**. Sol decoding the same Gemini transcript without context scores **0.320**. This is one run per cell; knowledge of the task can also supply vocabulary and answers without decoding the glyphs.

Haiku's own decoders explicitly abstain from translating every agent message, so both score **0.000**. Sol's Haiku report scores **0.075**, but all 109 entries retain unknown markers and mostly describe structure. This is not evidence that Sol deciphered the language.

DeepSeek decoding its own transcript scores **0.200**, with 19 wholly unknown entries. Sol decoding it scores **0.289**. The DeepSeek reference has no high-confidence translations, so its high-confidence score is **N/A**, not zero. Interpret these figures cautiously. D12 full-task decoding failed while UTF-8 logging its output and produced no final report.

Sol's five same-family no/full comparisons and seed 1's two additional context conditions are retained unchanged. Budget differences across some Sol conditions mean their differences do not isolate the effect of context.

## Method and validation

1. Use the existing reviewed `english/translation.json` for each source, authored from public chat plus its frozen `swarmish.txt`. No private scratchpads, intended-meaning annotations or action logs are used for scoring. References were not revised to fit decoder outputs.
2. Verify source, language, decoder-outcome and reference hashes. Align by the original public message ID; do not shift IDs after excluding task status or discarded glyph violations.
3. Extract only each decoder's translation section. D05's `SECTION 2:` headings, D06's inline semicolon list and D08's bullet list require an audited adapter; later task/evidence prose never enters embeddings.
4. Honor explicit abstentions. D05 declares every content meaning unknown, D06 enumerates unknown answers, and six D11 entries say unknown with structure-only parentheticals. These are zero-scored, with the full original text retained. Other tentative guesses, aliases and partial-unknown content remain unchanged. This document-level normalization supplements the prior scorer's lexical unknown rule; it does not change the frozen Sol scores.
5. Embed each reference/decoder message pair with `sentence-transformers/all-MiniLM-L6-v2`, pinned to revision `1110a243fdf4706b3f48f1d95db1a4f5529b4d41`, using the same package versions as the prior Sol scores. Take cosine per pair and the arithmetic mean over the fixed scorable denominator, including abstention zeros. Do not embed the whole transcript as a single document.
6. Retain the same score on the high-confidence reference subset. There are **1,738 scorable message/cell pairs**, including **585 high-confidence pairs**. No eligible decoder message IDs are missing; no embedded pair exceeds MiniLM's 256-token limit. Repeated sources across conditions count as separate comparison pairs, not independent messages.

References remain reference-assisted drafts rather than independently certified ground truth. Haiku has 15 high-confidence references out of 109; Gemini has 32/77; DeepSeek has 0/164. Haiku and DeepSeek source gameplay did not escape, whereas Gemini and all five Sol sources did. Source languages, reference quality, output verbosity and briefing content differ. A pooled model leaderboard would conceal these differences.

New decoder runs used eight agents, 200 shared turns, no time cap and a $50 soft limit. Prior Sol runs mix $40/200-turn and $10/10-minute limits. D12's failure is not a semantic score. Exact paths, protocols and hashes are recorded in [the manifest](../decoder_comparison_runs.json) and [summary](summary.json).

## Reproduce

Use the dependencies in `requirements-scoring.txt` and a local cache of the pinned model. From the repository root:

```sh
HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python experiments/tangut_200g_250l_200t/analysis/decoder_comparison_scoring.py --check
HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python experiments/tangut_200g_250l_200t/analysis/decoder_comparison_scoring.py
python -m unittest tests.test_translation_scoring tests.test_decoder_translation_extraction tests.test_decoder_comparison_scoring
```

Set `HF_HOME` if the local cache is outside the default Hugging Face directory. The script refuses changed archived inputs and validates all alignments before loading the embedding model. It reuses the twelve published Sol reports without altering them; regenerated new outputs remain in this separate directory. `--check` requires no embedding model.

During integration, the scorer gained support for the seed-2 auction report's
numbered sender labels. The manifest records that compatible code update. The
eight non-Sol cells were rescored locally and checked against commit `bcc80b3`;
the earlier source documents and results are preserved in that commit.
