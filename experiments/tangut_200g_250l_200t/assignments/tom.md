# Tom's assignments

Run **E06 (Haiku seed 1), E07 (Gemini seed 1), then E08 (DeepSeek seed 1)**.
Emma owns all five GPT/Sol seeds, with E01 already complete. She can run E02–E05
simultaneously with your queue in her own checkout. Run your queue sequentially.

From the repository root, first validate and inspect prompts:

```sh
.venv/bin/python experiments/tangut_200g_250l_200t/batch.py validate
.venv/bin/python experiments/tangut_200g_250l_200t/batch.py run E06 --prepare-only
```

Each command below is a separate paid run. Nothing chains automatically.

```sh
.venv/bin/python experiments/tangut_200g_250l_200t/batch.py run E06
.venv/bin/python experiments/tangut_200g_250l_200t/batch.py run E07
.venv/bin/python experiments/tangut_200g_250l_200t/batch.py run E08
```

Check each command succeeds and its receipt records a normal stop before starting the
next one. Preserve failed outputs for review rather than silently overwriting a slot.

Commit and push your three assigned encoding directories when ready. Pull Emma's results.
Once E01, E06, E07 and E08 have frozen handoffs, run T01, T02, T03 and T04 one at a time.
Codex will then fill each gameplay's `english/` directory from the matching frozen language.
D01–D13 are reserved for later decoder runs, with no language reference or English translation.

See [the shared protocol](../README.md) for limits, provenance and the complete matrix.
