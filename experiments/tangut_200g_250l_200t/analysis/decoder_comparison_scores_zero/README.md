# Decoder cosine with abstentions scored as zero

This is the recommended result table for the presentation. Missing and wholly unknown answers contribute zero; partially unknown answers keep their archived cosine. The denominator includes every scorable public agent-message reference, including abstentions. Cosine similarity is not percent accuracy.

- [Interactive report](comparisons.html): inspect all cells and their original message translations.
- [Summary CSV](summary.csv) / [JSON](summary.json)
- [Per-message CSV](per_line.csv) / [JSON](per_line.json)
- Original [raw-text scores](../decoder_comparison_scores_public_raw/README.md) and [N/A scores](../decoder_comparison_scores_na/README.md) remain available under their own conventions.

| Cell | Encoder → decoder | Context | Cosine | Denominator | Unknown / missing → zero | Partial unknown, scored | High-confidence cosine |
|---|---|---|---:|---:|---:|---:|---:|
| R01_no_task | Sol → Sol | no_task | 0.216283 | 77 | 0 / 0 | 19 | 0.209353 |
| R01_task_full | Sol → Sol | task_full | 0.509244 | 77 | 0 / 0 | 34 | 0.511896 |
| R02_no_task | Sol → Sol | no_task | 0.379945 | 59 | 0 / 0 | 18 | 0.463155 |
| R02_task_full | Sol → Sol | task_full | 0.509470 | 59 | 0 / 0 | 37 | 0.589195 |
| R03_no_task | Sol → Sol | no_task | 0.332651 | 75 | 0 / 0 | 66 | 0.378601 |
| R03_task_full | Sol → Sol | task_full | 0.556442 | 75 | 0 / 0 | 22 | 0.590240 |
| R04_no_task | Sol → Sol | no_task | 0.235798 | 74 | 0 / 0 | 14 | 0.287281 |
| R04_task_full | Sol → Sol | task_full | 0.434245 | 74 | 0 / 0 | 38 | 0.480896 |
| R05_no_task | Sol → Sol | no_task | 0.412330 | 64 | 0 / 0 | 31 | 0.467796 |
| R05_task_full | Sol → Sol | task_full | 0.468424 | 64 | 0 / 0 | 12 | 0.520335 |
| R01_task_summary | Sol → Sol | task_summary | 0.233929 | 77 | 0 / 0 | 40 | 0.228368 |
| R01_wrong_task | Sol → Sol | wrong_task | 0.243130 | 77 | 0 / 0 | 37 | 0.241957 |
| D05 | Haiku → Haiku | no_task | 0.000000 | 109 | 109 / 0 | 0 | 0.000000 |
| D06 | Haiku → Haiku | task_full | 0.000000 | 109 | 109 / 0 | 0 | 0.000000 |
| D07 | Haiku → Sol | no_task | 0.074602 | 109 | 0 / 0 | 109 | 0.065157 |
| D08 | Gemini → Gemini | no_task | 0.247659 | 77 | 0 / 0 | 1 | 0.297179 |
| D09 | Gemini → Gemini | task_full | 0.435338 | 77 | 0 / 0 | 1 | 0.474551 |
| D10 | Gemini → Sol | no_task | 0.320221 | 77 | 0 / 0 | 28 | 0.375130 |
| D11 | DeepSeek → DeepSeek | no_task | 0.199981 | 164 | 19 / 0 | 0 | N/A |
| D12 | DeepSeek → DeepSeek | task_full | Failed / unscored | N/A | N/A | N/A | N/A |
| D13 | DeepSeek → Sol | no_task | 0.289189 | 164 | 0 / 0 | 40 | N/A |
| D14 | Haiku → Sol | task_full | 0.230568 | 109 | 0 / 0 | 42 | 0.147848 |
| R02_task_summary | Sol → Sol | task_summary | 0.421021 | 59 | 0 / 0 | 55 | 0.498154 |
| R02_wrong_task | Sol → Sol | wrong_task | 0.436132 | 59 | 0 / 0 | 11 | 0.516218 |
| D12_retry1 | DeepSeek → DeepSeek | task_full | 0.263136 | 164 | 0 / 0 | 1 | N/A |
| D15 | Gemini → Sol | task_full | 0.502072 | 77 | 0 / 0 | 5 | 0.487970 |
| D16 | DeepSeek → Sol | task_full | 0.363718 | 164 | 0 / 0 | 101 | N/A |

## What changed

Haiku self-decoding (D05/D06) is **0.000000** without and with full context: all 109 eligible answers in each cell are historical abstentions. D05 contains structural glosses under a global unknown-content declaration; D06 gives literal `unknown` answers. We retain this existing classification rather than counting structural descriptions as recovered meanings.

GPT-6.1 Sol decoding Haiku (D07/D14) stays **0.074602 / 0.230568**: neither cell has wholly unknown or missing eligible answers. Their 109 / 42 partially unknown predictions remain scored. DeepSeek self-decoding without context (D11) changes to **0.199981**, because 19 of 164 predictions are historical abstentions. All other completed raw means are unchanged. The completed full-context retry D12_retry1 stays **0.263136**; the original D12 failure stays unscored.

## Method and provenance

The standard-library derivation reuses archived per-message raw cosines. Historical prediction statuses are authoritative and checked against the original hashed reports. For D12_retry1, which has no historical classifier report, the explicitly archived raw-parser statuses are used (one partial-unknown prediction, no abstentions). No answers are reinterpreted, rewritten or re-embedded.

There are 2,129 scorable message/cell pairs, including 237 predictions assigned zero and no missing predictions. Task-status messages, discarded glyph messages and unscorable references stay excluded; high-confidence columns use only that reference subset and show N/A when it is empty. All completed reports have complete decoder-entry alignment. Non-abstaining coverage is reported separately from the cosine denominator in JSON/CSV. Partial-unknown structural guesses can still have positive similarity without correct decipherment.

Source summary, source reports, classification sources, script and output reports are SHA-256 linked. Frozen public references and embedding provenance remain attached to each report. Failed attempts stay separate from completed retries. Only Sol self-decoding has five paired seeds; the other cells are single runs, and references differ in confidence. These descriptive comparisons do not isolate causal model effects.

From the repository root, rebuild with Python 3.10+ without API calls or model dependencies:

```sh
python3 experiments/tangut_200g_250l_200t/analysis/remake_decoder_scores_zero.py
python3 experiments/tangut_200g_250l_200t/analysis/render_decoder_comparisons.py experiments/tangut_200g_250l_200t/analysis/decoder_comparison_scores_zero/summary.json experiments/tangut_200g_250l_200t/analysis/decoder_comparison_scores_zero/comparisons.html
python3 -m unittest discover -s tests -p 'test_decoder_scores_zero.py'
```
