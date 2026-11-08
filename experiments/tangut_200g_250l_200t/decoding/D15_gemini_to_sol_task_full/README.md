# D15: Gemini → Sol, full task knowledge

Completed on 2026-11-08. Eight fresh Sol decoders received R07's frozen public
transcript and the full Storm Shelter briefing, including clues, ownership and
worked solution. The input is byte-identical to D09's full-task input. Settings
match D10's no-task run: medium reasoning, 16,000 output tokens, 200 shared
scheduled turns, no clock and a $50 soft cap. The language document, English
reference and private logs were withheld.

| Result | Value |
| --- | ---: |
| Stop | All eight decoders done |
| Returned calls | 123 |
| Public decoder chat messages | 105 |
| Recorded spend | $5.2820695 |
| Runtime | 172.644 seconds |
| Parse / logged API errors | 0 / 0 |
| Public source entries | 97 |
| Eligible scored pairs | 77 |
| Excluded task-status entries | 20 |
| Missing / unknown-only predictions | 0 / 0 |
| Mean public-reference cosine | 0.502072 |
| Matching no-task cosine, D10 | 0.320221 |
| High-confidence reference cosine | 0.487970, 32 pairs |

Every public ID appears exactly once, with matching sender labels. Five eligible
entries retain partial-unknown markers. Both literal-text and abstention-as-zero
scoring give the same mean. Similarity is not accuracy.

The report correctly recovers message 19's proposal to submit cabinet code 2748
and message 49's action sequence as DRAIN → CRANK → SIGNAL → BOOT. Errors remain:
message 62's agreement and execution of “remove” becomes a speculative warning
about one actor, though DRAIN is retained. Task-specific labels can correctly
identify referents without reproducing the literal Swarmish vocabulary.

R07 escaped. D15 is a user-selected follow-up after prior results, with one run
in the cell. It overlapped D16, which matters for wall-clock comparisons.

- [Decoder report](decoded.txt)
- [Receipt, cost and hashes](receipt.json)
- [Settings](config.json), [launch provenance](execution.json), [input verification](input_verification.json)
- [Scoring input](scoring_config.json), [raw cosine pairs](../../analysis/decoder_comparison_scores_public_raw/D15.json)
- [All follow-up results and reproduction command](../README.md#completed-follow-ups)

The six raw logs are under `raw/`. Their hashes and the source transcript hash
match the receipt. All cost was recorded against the primary key.
