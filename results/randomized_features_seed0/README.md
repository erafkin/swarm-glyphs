# Randomized feature ownership: Gemini, Sol and mixed

Three sequential runs on 2026-11-07 at [`2464c36`](https://github.com/erafkin/swarm-glyphs/commit/2464c36b8759b6742ec7d9717cb879bba5db7d23).
Models: `google/gemini-3.8-flash` and `openai/gpt-6.1-sol`.
Each used eight agents, eight features with four choices, seed 0 (target 22),
the same randomized one-to-one private ownership and starting conditions,
60-second feedback, medium reasoning, 16,000-token gameplay/interview allowances,
and a **$20 soft cap**. Message bodies were glyph-only; sender labels remained
visible. Encoding existing text was not prohibited. The mixed run used Sol
on agents 0, 2, 4, 6 and Gemini on 1, 3, 5, 7.

| Result | 8 Gemini | 8 Sol | 4 Sol + 4 Gemini |
|---|---:|---:|---:|
| Everyone first correct | **Never; finished 7/8** | **75.1 s** | **235.5 s** |
| Spend at first full correctness | — | **$0.78** | **$4.62** |
| Gameplay calls at first full correctness | — | **36** | **112** |
| Total duration, including interviews | 86m 18s | 2m 7s | 4m 23s |
| Final cost, including interviews | **$20.10** | **$3.24** | **$5.44** |
| Gameplay calls + interviews | 3,248 + 8 | 81 + 8 | 119 + 8 |
| Main communication | Feature/value counts | Binary ASCII | Binary ASCII |
| Raw logs | [d116b353](../../logs/20261107_085050_d116b353/) | [75544e8a](../../logs/20261107_102027_75544e8a/) | [5e02de73](../../logs/20261107_103151_5e02de73/) |

- **Gemini:** repeated `𗄌` identified a feature; repeated `𗧽` identified its
  value. Agents confused alphabetical, prompt and individually shuffled orders.
  Agent 2 first got everything right at 835.2 s, then misread ranks as
  **red / none / yellow** instead of **brown / beard / green**. It treated 88%
  group accuracy as evidence someone else was wrong. Every agent was individually
  correct at some point, but never all together; no guesses changed during the
  final 49 minutes despite continued broadcasts.
- **Sol:** agent 2 introduced ASCII `clothing=shirt` at 16.2 s using
  `𗄌=0`, `𘞌=1`, `𘜎=byte separator`. Explicit words removed ownership and
  option-order ambiguity. All eight clues were available in recognizable ASCII
  by 44.1 s; agents repaired small encoding mistakes, relayed missing facts and
  retained confirmed answers. Seven first-correct responses used prompts with
  no score feedback.
- **Mixed:** Sol agent 4 introduced the same approach at 12.5 s with
  `𗄌=0`, `𗅋=1`, `𗏏=byte separator`; Gemini agents adopted it. Two long,
  malformed Gemini responses delayed the smile clue and its final reader.
  Both nearly exhausted the 16,000-token allowance, suggesting budget exhaustion;
  finish reasons were not logged. The last agent decoded the clue on its next
  valid response, so the delay does not demonstrate an inability to share the code.

These are one matched trial per condition, not a general model ranking. Sol and
mixed reused English/ASCII rather than establishing new vocabulary. Costs are
reported charges for completed logged calls; milestone spend excludes pending
requests. Final totals include interviews and can exceed the soft cap.

The 27 original JSON/JSONL files are unchanged. Each run includes `SHA256SUMS`
and `analysis/raw-inventory.json`; archived absolute paths are historical provenance.
[metrics.json](metrics.json) contains exact counts and costs. Verify all three
archives and replay applied guesses offline, from the repository root:

```sh
python3 results/randomized_features_seed0/verify_results.py
```

Gemini runs 2–5 remain unstarted. The queued Sol and mixed runs are complete.
