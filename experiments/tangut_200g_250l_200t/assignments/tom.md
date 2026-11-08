# Tom's assignments

Run E03 (Sol seed 3), E04 (Sol seed 4), E05 (Sol seed 5), then E07 (Gemini seed 1).
Emma can run her queue simultaneously in her own checkout. Run your queue sequentially.

From the repository root, first validate and inspect prompts:

```sh
.venv/bin/python experiments/tangut_200g_250l_200t/batch.py validate
.venv/bin/python experiments/tangut_200g_250l_200t/batch.py run E03 --prepare-only
```

Each command below is a separate paid run. Nothing chains automatically.

```sh
.venv/bin/python experiments/tangut_200g_250l_200t/batch.py run E03
.venv/bin/python experiments/tangut_200g_250l_200t/batch.py run E04
.venv/bin/python experiments/tangut_200g_250l_200t/batch.py run E05
.venv/bin/python experiments/tangut_200g_250l_200t/batch.py run E07
```

Commit and push your four assigned encoding directories when ready. Pull Emma's results.
Once E01, E06, E07 and E08 have frozen handoffs, run T01, T02, T03 and T04 one at a time.
Codex will then fill each gameplay's `english/` directory from the matching frozen language.
D01–D13 are reserved for later decoder runs, with no language reference or English translation.

See [the shared protocol](../README.md) for limits, provenance and the complete matrix.
