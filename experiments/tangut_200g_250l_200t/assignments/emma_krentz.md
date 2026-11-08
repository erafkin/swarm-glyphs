# Emma Krentz's assignments

Your four encoding slots are E01 (Sol seed 1), E02 (Sol seed 2), E06 (Haiku seed 1),
and E08 (DeepSeek seed 1). **E01 reuses your pushed 130-line shared draft; do not rerun it.**
Its original 500-line instruction/no turn-cap settings are retained as an accepted deviation.

Run E02, E06 and E08 sequentially in your checkout. Tom can run his separate queue
simultaneously. Each run has a unique configuration, raw output directory and receipt.

From the repository root:

```sh
# Offline checks.
.venv/bin/python experiments/tangut_200g_250l_200t/batch.py validate
.venv/bin/python experiments/tangut_200g_250l_200t/batch.py run E02 --prepare-only

# Separate paid runs; no automatic continuation.
.venv/bin/python experiments/tangut_200g_250l_200t/batch.py run E02
.venv/bin/python experiments/tangut_200g_250l_200t/batch.py run E06
.venv/bin/python experiments/tangut_200g_250l_200t/batch.py run E08
```

Commit and push only your assigned encoding directories when ready. Do not edit the
shared manifest for completion status; receipts belong inside each run's directory.
Tom will pull the frozen handoffs and run all four new Storm Shelter playthroughs.
Do not launch T01–T04 or any decoder as part of this encoding queue.

See [the shared protocol](../README.md) for all settings, including DeepSeek's high reasoning
setting, the 200-turn discussion cap and the additional final export calls.
