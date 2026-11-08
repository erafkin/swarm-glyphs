# Decoder results D05–D13

This section records the original nine-run batch. Completed follow-ups, including
the successful D12 retry and D14–D16, are listed [below](#completed-follow-ups).

These nine runs used the revised R06 Haiku, R07 Gemini and R08 DeepSeek public
transcripts. Each had eight decoder agents, 200 shared scheduled discussion turns,
no time limit, 16,000 output tokens and a $50 soft spending cap. DeepSeek used high
reasoning; the other models used medium. At most three runs overlapped.

Eight teams finished their reports voluntarily. D12 failed in local Unicode logging.
Total recorded cost was **$34.30521774017351** for **740 returned calls**.
Completion means the team declared its document finished, not that its decoding
was correct. No message-level accuracy score has been calculated for this set.

| Report | Encoder | Decoder | Briefing | Calls | Cost | Runtime | Stop |
| --- | --- | --- | --- | ---: | ---: | ---: | --- |
| [D05](D05_haiku_to_haiku_no_task/decoded.txt) | Haiku | Haiku | None | 64 | $0.104897 | 1:17 | All done |
| [D06](D06_haiku_to_haiku_task_full/decoded.txt) | Haiku | Haiku | Full | 30 | $0.045702 | 0:37 | All done |
| [D07](D07_haiku_to_sol_no_task/decoded.txt) | Haiku | Sol | None | 86 | $3.098260 | 2:28 | All done |
| [D08](D08_gemini_to_gemini_no_task/decoded.txt) | Gemini | Gemini | None | 35 | $1.004902 | 2:13 | All done |
| [D09](D09_gemini_to_gemini_task_full/decoded.txt) | Gemini | Gemini | Full | 37 | $1.137828 | 2:33 | All done |
| [D10](D10_gemini_to_sol_no_task/decoded.txt) | Gemini | Sol | None | 127 | $6.820080 | 3:40 | All done |
| [D11](D11_deepseek_to_deepseek_no_task/decoded.txt) | DeepSeek | DeepSeek | None | 125 | $1.869168 | 19:17 | All done |
| [D12 failure](D12_deepseek_to_deepseek_task_full/failure.json) | DeepSeek | DeepSeek | Full | 48 | $1.085210 | 21:16 | Unicode logging failure |
| [D13](D13_deepseek_to_sol_no_task/decoded.txt) | DeepSeek | Sol | None | 188 | $19.139171 | 4:14 | All done |

## Interpretation and source outcomes

- Haiku's messages mostly remained unresolved, even with the full briefing. Sol
  recovered some report/request patterns but left much of the vocabulary unknown.
- Gemini's transcript supported substantial recovery of questions, reports,
  position/value relationships and action sequences. Full context supplied concrete
  Storm Shelter labels and answers, but the resulting report still contains lexical
  errors; its own claim of complete precision is unsupported.
- Sol recovered useful structure from DeepSeek's transcript, with errors in digit
  mappings. DeepSeek's own no-task report contains less reliable grammar and
  unsupported task interpretations. D12 provides no completed full-task comparison.

These are qualitative observations, not scored accuracy results. R06 and R08 did
not escape; both exhausted their 200-turn gameplay allowance. R07 escaped. Decoders
received only the public transcript and selected briefing, never the frozen
Swarmish document or researcher English reference. The full-task condition includes
the clues and answers, so recovering those facts alone does not prove decipherment.

## D12 failure and accounting

Thirty responses exhausted the 16,000-token allowance and could not be parsed.
A separate, normally finished response contained unpaired Unicode surrogates.
It was applied to the in-memory draft, but UTF-8 logging raised `UnicodeEncodeError`.
The same invalid text then prevented writing the final outcome. This was a local
logging failure, not a provider API failure.

`monitor_calls.jsonl` contains 47 records. The error log retains the serialized 48th
record, including its $0.0180096972 cost. Recovering that record reconciles the
summary's $1.0852104716860005 total. The empty `monitor.jsonl`, all other raw files,
and the failed execution remain unchanged. No successful receipt/report was
fabricated. A later successful retry is archived separately below.

## Verification and provenance

- [Verification ledger](../../../output/analysis/decoder_D05_D13_completion_20261108/verification.json)
- [Recovered D12 call](../../../output/analysis/decoder_D05_D13_completion_20261108/D12_call_recovered_from_error.json)
- [Parallel queue state](../../../output/launches/decoders_D05_D13_parallel_20261108/queue_state.json)
- [Queue controller](../../../output/launches/decoders_D05_D13_parallel_20261108/queue.py)

All eight successful receipts, 48 decoder raw-file hashes and source transcript
hashes were verified. The source gameplay receipts cover a further 38 raw files.
English references for R06/R07/R08 preserve 110/97/227 public entries. D12 has its
own failure record with hashes, rather than a completion receipt.

Sol seed 1's summary and Art Auction runs were performed separately; see
[their setup and provenance](sol_seed1_summary_auction/README.md) and the
[Sol scoring report](../analysis/sol_translation_scoring.md). They are not included
in the nine-run costs above.

## Completed follow-ups

| Report | Encoder | Decoder | Briefing | Calls | Cost | Runtime | Stop |
| --- | --- | --- | --- | ---: | ---: | ---: | --- |
| [D14](D14_haiku_to_sol_task_full/README.md) | Haiku | Sol | Full | 74 | $2.673096 | 2:33 | All done |
| [D12 retry 1](D12_deepseek_to_deepseek_task_full/attempts/retry1/README.md) | DeepSeek | DeepSeek | Full | 83 | $1.187103 | 30:21 | All done |
| [D15](D15_gemini_to_sol_task_full/README.md) | Gemini | Sol | Full | 123 | $5.282070 | 2:53 | All done |
| [D16](D16_deepseek_to_sol_task_full/README.md) | DeepSeek | Sol | Full | 138 | $13.065024 | 3:14 | All done |

D15 and D16 ran concurrently on 2026-11-08 and cost **$18.3470938** together.
Both had eight Sol decoders, medium reasoning, 16,000 output tokens, a 200-turn
allowance, no clock and a separate $50 soft cap. All eight agents in each team
marked done; neither run had a parse error or logged API error. All spending used
the primary key. All twelve raw-file hashes, source hashes and final reports
were verified against their receipts. These follow-ups were chosen after seeing
earlier results and are not preregistered or replicated comparisons.

Sol now has both briefing conditions for every other encoder family:

| Encoder | Sol, no task | Sol, full task | Eligible public messages |
| --- | ---: | ---: | ---: |
| Haiku | 0.074602 (D07) | 0.230568 (D14) | 109 |
| Gemini | 0.320221 (D10) | 0.502072 (D15) | 77 |
| DeepSeek | 0.289189 (D13) | 0.363718 (D16) | 164 |

Values are mean paired MiniLM cosine against the frozen public-message English
references, not percent accuracy. These six scores are identical in the
[literal-text](../analysis/decoder_comparison_scores_public_raw/README.md) and
[abstention-as-zero](../analysis/decoder_comparison_scores_zero/README.md) outputs:
none has a missing or wholly unknown classified entry. Partial-unknown and
structural guesses remain ordinary text. References have differing confidence;
DeepSeek's eligible references are all medium or low confidence.

Full context helps Sol recover task referents and numerical/action patterns, but
does not eliminate lexical errors. D15 recovers the cabinet-code proposal and
action sequence; D16 preserves the actual wrong proposal 1234 rather than
substituting the supplied solution 2748. Both retain uncertainties. Full-task
briefings contain clue ownership and answers, so these results do not by
themselves demonstrate complete recovery of the underlying vocabulary.

To reproduce all current scores, retain all three extra archived inputs:

```sh
python3 experiments/tangut_200g_250l_200t/analysis/score_public_raw_cosines.py \
  --extra-decoder-config experiments/tangut_200g_250l_200t/decoding/D12_deepseek_to_deepseek_task_full/attempts/retry1/scoring_config.json \
  --extra-decoder-config experiments/tangut_200g_250l_200t/decoding/D15_gemini_to_sol_task_full/scoring_config.json \
  --extra-decoder-config experiments/tangut_200g_250l_200t/decoding/D16_deepseek_to_sol_task_full/scoring_config.json
python3 experiments/tangut_200g_250l_200t/analysis/remake_decoder_scores_zero.py
python3 experiments/tangut_200g_250l_200t/analysis/render_decoder_comparisons.py experiments/tangut_200g_250l_200t/analysis/decoder_comparison_scores_zero/summary.json experiments/tangut_200g_250l_200t/analysis/decoder_comparison_scores_zero/comparisons.html
```

The original D12 failure remains excluded from scoring. Existing score differences
after adding the new reports are numerical rounding from embedding batches, not
changes to references, prediction text or scoring policy.
