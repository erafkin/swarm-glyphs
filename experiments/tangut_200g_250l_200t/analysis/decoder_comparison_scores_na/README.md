# Decoder comparisons with unknown answers marked N/A

**Primary cosine excludes missing and wholly unknown answers.** Their per-line cosine is `null` in JSON and **N/A** in the viewer and CSV. A completed cell with no valid pairs has an N/A mean and zero coverage. Failed cells remain unscored.

- [Interactive comparisons](comparisons.html): original and normalized text, source glyphs, confidence, N/A reasons, coverage, and separately labelled historical means.
- [Summary CSV](summary.csv) / [JSON](summary.json): 23 completed cells; failed attempts: 1.
- [Per-message CSV](per_line.csv) / [JSON](per_line.json): 2,497 public-entry/cell rows with primary inclusion flags and supplementary historical cosine.
- Per-cell JSON files preserve source hashes, text, prediction statuses, and historical metrics under `supplementary_metrics`.

| Cell | Encoder → decoder | Context | Primary cosine | Coverage | Unknown / missing | Partial unknown | High-confidence cosine (coverage) | Supplementary zero-inclusive cosine |
|---|---|---|---:|---:|---:|---:|---:|---:|
| R01_no_task | Sol → Sol | no_task | 0.216 | 77/77 | 0 / 0 | 19 | 0.209 (64/64) | 0.216 |
| R01_task_full | Sol → Sol | task_full | 0.509 | 77/77 | 0 / 0 | 34 | 0.512 (64/64) | 0.509 |
| R02_no_task | Sol → Sol | no_task | 0.380 | 59/59 | 0 / 0 | 18 | 0.463 (12/12) | 0.380 |
| R02_task_full | Sol → Sol | task_full | 0.509 | 59/59 | 0 / 0 | 37 | 0.589 (12/12) | 0.509 |
| R03_no_task | Sol → Sol | no_task | 0.333 | 75/75 | 0 / 0 | 66 | 0.379 (13/13) | 0.333 |
| R03_task_full | Sol → Sol | task_full | 0.556 | 75/75 | 0 / 0 | 22 | 0.590 (13/13) | 0.556 |
| R04_no_task | Sol → Sol | no_task | 0.236 | 74/74 | 0 / 0 | 14 | 0.287 (36/36) | 0.236 |
| R04_task_full | Sol → Sol | task_full | 0.434 | 74/74 | 0 / 0 | 38 | 0.481 (36/36) | 0.434 |
| R05_no_task | Sol → Sol | no_task | 0.412 | 64/64 | 0 / 0 | 31 | 0.468 (33/33) | 0.412 |
| R05_task_full | Sol → Sol | task_full | 0.468 | 64/64 | 0 / 0 | 12 | 0.520 (33/33) | 0.468 |
| R01_task_summary | Sol → Sol | task_summary | 0.234 | 77/77 | 0 / 0 | 40 | 0.228 (64/64) | 0.234 |
| R01_wrong_task | Sol → Sol | wrong_task | 0.243 | 77/77 | 0 / 0 | 37 | 0.242 (64/64) | 0.243 |
| D05 | Haiku → Haiku | no_task | N/A | 0/109 | 109 / 0 | 0 | N/A (0/15) | 0.000 |
| D06 | Haiku → Haiku | task_full | N/A | 0/109 | 109 / 0 | 0 | N/A (0/15) | 0.000 |
| D07 | Haiku → Sol | no_task | 0.075 | 109/109 | 0 / 0 | 109 | 0.065 (15/15) | 0.075 |
| D08 | Gemini → Gemini | no_task | 0.248 | 77/77 | 0 / 0 | 1 | 0.297 (32/32) | 0.248 |
| D09 | Gemini → Gemini | task_full | 0.435 | 77/77 | 0 / 0 | 1 | 0.475 (32/32) | 0.435 |
| D10 | Gemini → Sol | no_task | 0.320 | 77/77 | 0 / 0 | 28 | 0.375 (32/32) | 0.320 |
| D11 | DeepSeek → DeepSeek | no_task | 0.226 | 145/164 | 19 / 0 | 0 | N/A (0/0) | 0.200 |
| D12 | DeepSeek → DeepSeek | task_full | Failed / unscored | N/A | N/A | N/A | N/A | N/A |
| D13 | DeepSeek → Sol | no_task | 0.289 | 164/164 | 0 / 0 | 40 | N/A (0/0) | 0.289 |
| D14 | Haiku → Sol | task_full | 0.231 | 109/109 | 0 / 0 | 42 | 0.148 (15/15) | 0.231 |
| R02_task_summary | Sol → Sol | task_summary | 0.421 | 59/59 | 0 / 0 | 55 | 0.498 (12/12) | 0.421 |
| R02_wrong_task | Sol → Sol | wrong_task | 0.436 | 59/59 | 0 / 0 | 11 | 0.516 (12/12) | 0.436 |

## Denominators and interpretation

The primary mean is the arithmetic mean of existing paired cosine values for scorable reference messages whose existing `prediction_status` is neither `missing` nor `unknown`. Coverage is **valid pairs / scorable references**. Task-status entries, discarded messages, and unscorable references remain excluded. High-confidence means and coverage apply the same rules within the high-confidence reference subset. No valid pairs means N/A, including when a source has no high-confidence references.

There are **1,728/1,965 valid/scorable message-cell pairs**, **237 wholly unknown** and **0 missing** predictions. **655 partial-unknown predictions remain scored.** Repeated source messages across conditions are separate comparison pairs, not independent observations.

Existing partial_unknown predictions remain scored and are counted separately. No new semantic classification is performed. Tentative guesses, unresolved aliases, and structure-only glosses may still receive cosine scores; nonzero similarity does not establish decipherment. In particular, D07's 109 partial-unknown entries largely describe structure; its nonzero score is not evidence of successful decipherment. D05 and D06 explicitly abstained on every scorable message, so their primary mean is N/A (0/109 coverage). D11's 19 unknown answers are excluded from the primary mean; the original zero-inclusive mean remains available for comparison.

Cosine measures resemblance between English texts, **not percent correct**. It can miss wrong numbers, negation, roles and actions. References remain reference-assisted drafts. The sources, reference uncertainty, decoder wording, task context, and budgets differ; one run per cell cannot isolate a model or context effect. A higher valid-pair mean can reflect a smaller answered subset, so always read coverage alongside it.

## Preservation and reproducibility

This is a reporting-only derivation. No model is loaded, no embeddings are recomputed, and no API calls are made. Historical score files, raw decoder outputs, extraction records, frozen references, and their existing classifications remain unchanged. The original means and other metrics are retained under explicitly labelled supplementary fields; their zero-inclusive denominator differs from the primary metric.

Source summary: `experiments/tangut_200g_250l_200t/analysis/decoder_comparison_source_catalog/summary.json` (SHA-256 `5da0fe9826d8f9baaae17fea9b5267b7c25768cce01db98ac62d2fdb665f5478`). Each derived report records its original path and hash. Historical comparison notes are preserved as `source_comparability_notes` in the summary.

The source catalog consolidates the original comparison summary, D14, and the two published seed-2 context extensions without changing their measurements or counting repeated cells twice. From the repository root, rebuild the catalog and primary results:

```sh
python experiments/tangut_200g_250l_200t/analysis/assemble_decoder_score_catalog.py
python experiments/tangut_200g_250l_200t/analysis/remake_decoder_scores_na.py --input experiments/tangut_200g_250l_200t/analysis/decoder_comparison_source_catalog/summary.json --output experiments/tangut_200g_250l_200t/analysis/decoder_comparison_scores_na
python -m unittest tests.test_decoder_scores_na
```

The transform validates recorded source-report hashes, rejects in-place output, and uses only Python's standard library. It does not alter the original scorer or historical results.
