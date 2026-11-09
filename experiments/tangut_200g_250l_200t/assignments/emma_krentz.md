# Emma Krentz's revised Storm Shelter assignments

All Sol encoders E01–E05 are complete. You own **R01–R05**, one Storm Shelter playthrough
per frozen Sol language, with your revised escape-and-secrecy instruction. Tom owns R06–R08
for Haiku, Gemini and DeepSeek. Each slot has a distinct output folder to avoid overlap.

**Your runs are already in progress. Do not restart them just because these slots are new.**
When you finish and push, import the matching existing raw directories without API calls:

```sh
.venv/bin/python experiments/tangut_200g_250l_200t/batch.py collect R01 /absolute/path/to/sol_seed1_round_2
.venv/bin/python experiments/tangut_200g_250l_200t/batch.py collect R02 /absolute/path/to/sol_seed2_round_2
.venv/bin/python experiments/tangut_200g_250l_200t/batch.py collect R03 /absolute/path/to/sol_seed3_round_2
.venv/bin/python experiments/tangut_200g_250l_200t/batch.py collect R04 /absolute/path/to/sol_seed4_round_2
.venv/bin/python experiments/tangut_200g_250l_200t/batch.py collect R05 /absolute/path/to/sol_seed5_round_2
```

R01–R05 correspond to E01–E05 and config seeds 0–4. Collection verifies the exact frozen
language, glyph sample, model, seed and revised goal in all eight task prompts. Other setting
differences and language-requirement differences are recorded in the receipt for review.
Use a matching original raw folder; never alter it to make a validation check pass.

If a particular seed truly has not started, inspect `run R0N --prepare-only`, then use
`run R0N` for that seed only. The helper uses the frozen language-design requirements and
checks hashes before making calls. Default settings are eight Sol agents, medium reasoning,
16,000 tokens, a $50 soft cap and no gameplay turn/time deadline. Do not duplicate an
existing run. No encoders or decoders need to launch as part of this phase.

Pull the setup while preserving local work. Commit only your assigned R folders (or push
existing logs and identify their seed mapping for import). Keep `.env`, previews and locks
local. Do not edit the shared manifest to report completion; each receipt records its outcome.
The original T01–T04 results are archived separately and are not substitutes for these reruns.

See [the shared protocol](../README.md).

## Grok 4.7 extension (added 2026-11-08)

You also own **E09, R09 and D17–D20**, one Grok 4.7 family on config seed 0. Run them in
order and only after the key has been topped up; nothing launches automatically:

```sh
.venv/bin/python experiments/tangut_200g_250l_200t/batch.py validate
.venv/bin/python experiments/tangut_200g_250l_200t/batch.py run E09 --prepare-only
.venv/bin/python experiments/tangut_200g_250l_200t/batch.py run E09
.venv/bin/python experiments/tangut_200g_250l_200t/batch.py run R09 --prepare-only
.venv/bin/python experiments/tangut_200g_250l_200t/batch.py run R09
.venv/bin/python experiments/tangut_200g_250l_200t/batch.py run D17
.venv/bin/python experiments/tangut_200g_250l_200t/batch.py run D18
.venv/bin/python experiments/tangut_200g_250l_200t/batch.py run D19
.venv/bin/python experiments/tangut_200g_250l_200t/batch.py run D20
```

All six Grok slots were collected on 2026-11-08 (see the batch README's Grok 4.7 section and
`decoding/README.md`); only the R09 English reference remains open.

Review the frozen `encoding/E09_grok_seed1/handoff/swarmish.txt` before R09, and write the R09
English reference before the decoders. If R09 ends on the turn cap instead of escaping, the
decoder plans need `allow_turn_limited_gameplay_source: true`, as D05–D07 and D11–D13 did.
Read the smoke-test note in the [shared protocol](../README.md#grok-47-extension-2026-11-08)
before launching E09.
