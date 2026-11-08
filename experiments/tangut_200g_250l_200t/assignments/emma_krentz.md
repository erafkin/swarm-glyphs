# Emma Krentz's assignments

You own all five GPT/Sol encoding slots: E01–E05, corresponding to Sol seeds 1–5.
**E01 reuses your pushed 130-line shared draft; do not rerun it.**
Its original 500-line instruction/no turn-cap settings are retained as an accepted deviation.

Pull the latest main, preserving any local work, and read this file plus the shared README.
Use your local `.venv` and OpenRouter key; neither should be committed.

Run **E02, E03, E04 and E05 sequentially** in your checkout. Tom runs Haiku, Gemini and
DeepSeek in his separate queue
simultaneously. Each run has a unique configuration, raw output directory and receipt.

From the repository root:

```sh
# Offline checks.
.venv/bin/python experiments/tangut_200g_250l_200t/batch.py validate
.venv/bin/python experiments/tangut_200g_250l_200t/batch.py run E02 --prepare-only

# Separate paid runs; no automatic continuation.
.venv/bin/python experiments/tangut_200g_250l_200t/batch.py run E02
.venv/bin/python experiments/tangut_200g_250l_200t/batch.py run E03
.venv/bin/python experiments/tangut_200g_250l_200t/batch.py run E04
.venv/bin/python experiments/tangut_200g_250l_200t/batch.py run E05
```

Check each command succeeds and its receipt records a normal stop before starting the
next one. If a run fails or collection rejects its document, preserve the raw logs and
report the issue; do not silently overwrite or rerun that slot.

Commit and push only your assigned encoding directories when ready. Do not edit the
shared manifest for completion status; receipts belong inside each run's directory.
Tom will pull the frozen handoffs and run all four new Storm Shelter playthroughs.
Do not launch T01–T04 or any decoder as part of this encoding queue.

Your runs use Sol 6.1, medium reasoning, eight agents, 200 Tangut glyphs, 250-line
language instructions, 200 total discussion turns, and a $50 soft cap per run.
See [the shared protocol](../README.md) for final export calls and frozen-document selection.
