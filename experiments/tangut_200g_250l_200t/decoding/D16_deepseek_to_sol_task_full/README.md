# D16: DeepSeek → Sol, full task knowledge

Completed on 2026-11-08. Eight fresh Sol decoders received R08's frozen public
transcript and the full Storm Shelter briefing, including clues, ownership and
worked solution. The input is byte-identical to D12's full-task input. Settings
match D13's no-task run: medium reasoning, 16,000 output tokens, 200 shared
scheduled turns, no clock and a $50 soft cap. The language document, English
reference and private logs were withheld.

| Result | Value |
| --- | ---: |
| Stop | All eight decoders done |
| Returned / state-applied calls | 138 / 136 |
| Public decoder chat messages | 115 |
| Recorded spend | $13.0650243 |
| Runtime | 193.635 seconds |
| Parse / logged API errors | 0 / 0 |
| Public source entries | 227 |
| Eligible scored pairs | 164 |
| Excluded task-status / discarded entries | 33 / 30 |
| Missing / unknown-only predictions | 0 / 0 |
| Mean public-reference cosine | 0.363718 |
| Matching no-task cosine, D13 | 0.289189 |

Every public ID appears exactly once. Sender labels are omitted; explicit message
numbers provide alignment. There are 101 eligible entries with partial-unknown
markers. Both literal-text and abstention-as-zero scoring give the same mean.
Similarity is not accuracy. The reference has 102 medium-confidence and 62
low-confidence eligible translations, with no high-confidence subset.

Sol recovers numerical and missing-information patterns, including message 32's
actual wrong proposal 1234 instead of substituting the supplied answer 2748.
It still overinterprets some statements: message 157's “third/five shape: 4”
becomes “[5] position4”, and alternative-number questions become possible
replacement arrows. Message 200 retains unknown rule/order vocabulary. The
report's locally defined T/M/MN/TS abbreviations remain literal in scoring.

R08 did not escape before its 200-turn gameplay cap; the decoder interpreted that
unsuccessful transcript unchanged. D16 is a user-selected follow-up after prior
results, with one run in the cell. It overlapped D15.

- [Decoder report](decoded.txt)
- [Receipt, cost and hashes](receipt.json)
- [Settings](config.json), [launch provenance](execution.json), [input verification](input_verification.json)
- [Scoring input](scoring_config.json), [raw cosine pairs](../../analysis/decoder_comparison_scores_public_raw/D16.json)
- [All follow-up results and reproduction command](../README.md#completed-follow-ups)

The six raw logs are under `raw/`. Their hashes and the source transcript hash
match the receipt. Both responses arriving after completion remain logged and
cost-accounted without changing the final draft. All cost used the primary key.
