# DeepSeek full-task decoder retry

Fresh eight-agent retry of D12 after its malformed-Unicode logging crash. The original
failed attempt remains unchanged and unscored. The retry completed on 8 November 2026
at 09:45:28 UTC; all eight agents marked the report done.

| Measure | Result |
|---|---:|
| Mean public-reference cosine | 0.263136 |
| Corresponding no-task score, D11 | 0.218711 |
| Difference between these attempts | +0.044424 |
| Eligible messages scored | 164 / 164 |
| Public rows aligned | 227 / 227 |
| Excluded task-status rows | 33 |
| Excluded discarded messages | 30 |
| Returned API calls | 83 |
| Valid structured responses | 47 |
| Responses applied before stop | 40 |
| Valid responses ignored after stop | 7 |
| Parse errors, all token-limit truncations | 36 |
| Unicode parse errors / logged API errors | 0 / 0 |
| Runtime including drain | 30 minutes 20.6 seconds |
| Recorded cost | $1.18710330626 |
| Stop reason | all_done |

The retry retained the original prompts and public transcript, 200 shared-call limit,
no clock limit, $50 soft spending cap, high reasoning and 16,000 output tokens.
No output-token increase was applied. Malformed Unicode responses are now logged
losslessly and rejected before they can enter shared state.

## Evaluation

The final [decoder report](decoded.txt) explicitly translates every public row. Scoring
uses the frozen public-message English references, not private intended meanings.
Literal unknown text and structural glosses remain ordinary embedding inputs; task
feedback and discarded messages are excluded. Message numbers and validated sender
prefixes are removed. Parentheticals, including trailing confidence tags, remain literal.
There are no missing eligible entries, no unknown-only predictions and one prediction
containing the word unknown. No embedding inputs were truncated.

This is mean paired MiniLM cosine, not percent correct. The decoder correctly translates
some simple code proposals, including 1248 in message 110 and 1247 in message 170.
It makes task-consistent clue guesses, but many code translations remain wrong. For example, public message 226
translates as "I put/place 1728." in the frozen reference; the decoder gives
"(code:1,6,2?) (M)". Message 25 is largely questions about positions, but the decoder
calls it a code attempt. The +0.044424 difference from D11 is descriptive of these two
attempts, not a replicated causal estimate of context benefit. All 164 DeepSeek
references have medium or low confidence, so there is no high-confidence-only score.
The reconstructed language also contains inconsistent codepoint labels: for example,
it labels the displayed glyph `𘀝` as U+1800D, although the character is U+1801D.
Reconstructed lexicon correctness is separate from this translation-cosine score.

- [Scored message pairs](../../../../analysis/decoder_comparison_scores_public_raw/D12_retry1.json)
- [Full results index](../../../../analysis/decoder_comparison_scores_public_raw/README.md)
- [Receipt and archive hashes](receipt.json)
- [Execution provenance](execution.json)
- [Scoring inputs](scoring_config.json)

All six retry archive hashes and all seven original failure archive hashes were checked.
The final document matches the archived outcome, calls and costs reconcile with the
receipt, and the shared call cap was respected. Original N/A and zero-assigned score
histories remain intact. Scoring was performed locally without paid API calls.

To regenerate the current results, run the experiment's `analysis/score_public_raw_cosines.py`
with `--extra-decoder-config` pointing to this directory's `scoring_config.json`.
The default scorer input alone contains the historical reports and does not append this retry.
