# Tom's revised Storm Shelter assignments

Encoding is complete. Prepare **R06 Haiku, R07 Gemini, R08 DeepSeek** using the existing
E06/E07/E08 frozen handoffs and Emma's revised escape-and-secrecy instruction.
Emma owns all five revised Sol slots R01–R05 and is already running them.

Tom authorized these three runs sequentially with **200 task turns shared across all eight
agents per run**. Each also has a $50 soft cap, no time cap, and 16,000 output tokens. Preserve medium reasoning for Haiku/Gemini and high for DeepSeek.

```sh
# Offline: inspect these first.
.venv/bin/python experiments/tangut_200g_250l_200t/batch.py validate
.venv/bin/python experiments/tangut_200g_250l_200t/batch.py run R06 --prepare-only
.venv/bin/python experiments/tangut_200g_250l_200t/batch.py run R07 --prepare-only
.venv/bin/python experiments/tangut_200g_250l_200t/batch.py run R08 --prepare-only

# Paid: only after the requested launch.
.venv/bin/python experiments/tangut_200g_250l_200t/batch.py run R06
.venv/bin/python experiments/tangut_200g_250l_200t/batch.py run R07
.venv/bin/python experiments/tangut_200g_250l_200t/batch.py run R08
```

The helper does not chain runs. A started/collected slot cannot be overwritten. Preserve
failures and any operator stopping decision. Commit only each assigned R folder and its
reviewed English reference, then push. No new encoders or decoders are part of this queue.
Do not repair the frozen languages; the original failures
remain under `gameplay/archive/original_prompt_20261107/`.

See [the shared protocol](../README.md).
