# D14: Haiku → Sol, full task knowledge

User-authorized follow-up to D07, selected after observing its no-task result.
Eight fresh `openai/gpt-6.1-sol` decoders received the same frozen R06 public
transcript and the full Storm Shelter briefing, including clue ownership and the
worked solution. They did not receive the language file, English reference,
creation conversation, private scratchpads or private action records.

The system prompts and user briefing are byte-identical to D06 (Haiku decoding
the same transcript with full task knowledge). Settings match D07: medium
reasoning, 16,000 output tokens, 200 shared scheduled turns, no clock, $50 soft cap.

| Result | Value |
|---|---:|
| Stop | All eight decoders marked done |
| Returned calls | 74 |
| Decoder elapsed time | 153.4 seconds |
| Recorded spend | $2.6730956 |
| Parse errors | 0 |
| Public source entries | 110, including one excluded task-status entry |
| Mean cosine, unknown answers N/A | 0.230568 |
| Included/scorable pairs | 109/109 |
| Per-line partial-unknown flags | 42 |
| High-confidence reference cosine | 0.147848, 15/15 pairs |

For the matching no-task run D07, mean cosine was 0.074602. Both runs retain
tentative/structural guesses in the measured pairs; 109/109 coverage is not 109
correct translations. Per-line unknown-marker counts do not capture every global
uncertainty convention in the report. D14's document explicitly describes its
reconstruction as partial, with uncertain word meanings.

## What the full briefing helped recover

The six proposed numeral mappings are correct against the frozen language:

| Glyph | D14 proposal | Frozen language |
|---|---:|---:|
| 𗛽 | 1 | 1 |
| 𗳃 | 2 | 2 |
| 𗸽 | 3 | 3 |
| 𘙠 | 4 | 4 |
| 𗋭 | 7 | 7 |
| 𗸪 | 8 | 8 |

D14 labels these medium confidence. It connects each speaker's recurring glyph
to the numbers in that speaker's known clue, with additional evidence from
different speakers sharing the glyphs for 2 and 4. D07 lacked that briefing and
had considered the same speaker-associated payloads possible agent IDs.

The decoder also proposes I/my, you/your, self-reports and inquiries, but does not
recover the full have/know/thing vocabulary or the missing task-symbol names. It
correctly separates the supplied solution from anything established by the chat.
This is improved partial recovery using task knowledge, not a fully decoded
language. Because this follow-up was chosen after reviewing D07 and contains one
run, it is descriptive evidence rather than a preregistered or replicated effect.

## Artifacts

- [Final decoder report](decoded.txt)
- [Receipt, timing, cost and archive hashes](receipt.json)
- [Run configuration](config.json) and [launch provenance](execution.json)
- [Current comparisons and N/A scoring method](../../analysis/decoder_comparison_scores_na/README.md)
- [Underlying D14 score report](../../analysis/haiku_to_sol_full_task_scores/D14.json)

English comparison pairs use the previously frozen public-only reference. No
reference text or old decoder scores were changed after inspecting this run.
The new primary N/A summaries preserve old zero-inclusive means as supplementary
metrics. Raw logs are kept under this slot's `raw/` directory.
