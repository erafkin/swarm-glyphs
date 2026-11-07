# Gemini: randomized feature ownership, 60-second scoring

Five independent configurations, each with eight `google/gemini-3.8-flash` agents and eight
features with four choices each. Feature ownership is a seeded one-to-one permutation.
Agents receive only their own private clue and are told that IDs do not reveal ownership.

All runs use glyph-only messages, 18 glyphs, medium reasoning, 16,000-token gameplay and
interview limits, 60-second feedback, and a **$20 soft cost limit per run**. In-flight calls
and end-of-game interviews can exceed the soft cap. Winning requires all eight agents to
guess every feature correctly.

| Run | Local seed | Config |
|---|---:|---|
| 1 | 0 | [run_1_seed0.json](run_1_seed0.json) |
| 2 | 1 | [run_2_seed1.json](run_2_seed1.json) |
| 3 | 2 | [run_3_seed2.json](run_3_seed2.json) |
| 4 | 3 | [run_4_seed3.json](run_4_seed3.json) |
| 5 | 4 | [run_5_seed4.json](run_5_seed4.json) |

Each run creates fresh agents, scratchpads and chat history. Seeds control the goal, glyph set,
private display order, initial guesses and feature assignment; model sampling is not seeded.
Seed 0 retains person 22 as the hidden goal for comparison with earlier runs. Subsequent seeds
also vary the goal and views. No previous game or interview context is supplied.

**Run 1 only, then pause for user review.** There is no automatic continuation to runs 2–5.
`batch.json` records the planned order and review requirement; it does not launch anything.

```sh
.venv/bin/python -m src.guess_who.scripts.run_features_seed0 configs/gemini_random_features_5x60s/run_1_seed0.json
```

Changing ownership removes the fixed agent-index-to-feature shortcut. Named-feature ASCII
encodings remain possible. Sixty-second feedback reduces the delay before the win check, and
also gives agents more frequent feedback; comparisons with four-minute runs change both factors.

Use each run's saved `agents.json` to recover the actual assignment, `config.json` for effective
settings, and `agent_calls.jsonl` to replay first correctness separately from the scoring check.
