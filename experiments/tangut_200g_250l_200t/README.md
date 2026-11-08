# Tangut language and decoder batch

Eight encoding runs, four fresh Storm Shelter playthroughs, thirteen decoder runs.
This is the initial matrix agreed by Tom; a complete cross-family matrix can be added later.

## Completed Storm Shelter playthroughs

All four gameplay attempts are archived. English links below include aligned JSON alongside
the readable transcript. No decoder runs were launched as part of these playthroughs.

| Model | Outcome | Run elapsed | Returned API calls | Public agent messages | Recorded cost | English reference |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| Sol | Escaped | 2m 58s | 75 | 72 | $2.007253 | [T01](gameplay/T01_sol/english/transcript_english.md) |
| Haiku | Stopped at requested $10 limit; no room actions | 60m 29s | 3,496 | 864 | $10.002707 | [T02](gameplay/T02_haiku/english/transcript_english.md) |
| Gemini | Escaped | 5m 55s | 95 | 80 | $1.801470 | [T03](gameplay/T03_gemini/english/transcript_english.md) |
| DeepSeek | Stopped at user request; six rejected first-lock attempts | 13m 51s | 53 | 50 | $0.416546 | [T04](gameplay/T04_deepseek/english/transcript_english.md) |

**Total recorded gameplay cost: $14.227976 across 3,719 returned calls.** Elapsed time is
the runner's duration. Calls and costs include returned responses ignored after escape
(three for Sol, seven for Gemini). Public agent-message counts include discarded-message
placeholders but exclude task status updates. Haiku and DeepSeek were interrupted, so
cancelled in-flight requests may have additional provider charges absent from the logs.
Their per-run stop notes preserve this distinction; original raw configs and logs are unchanged.

Sol and Gemini used compositional symbol descriptions, numbers and action coordination to
escape. Haiku's mostly generic messages did not produce any room action. DeepSeek remained
at the first lock; 15 of its 50 public messages were discarded for forbidden characters,
and three additional replies reached the token limit and failed to parse. Its frozen language
also contains conflicting numeric definitions and uses glyphs outside the sampled alphabet.
These are observed limitations, not proof of the sole cause of failure or that eventual escape
was impossible. This is one playthrough per language with different stopping rules, not a
controlled ranking of model families. Runtime source and prompt hashes match across all four.

All English references were made from the frozen language and public transcript, then
independently reviewed. They preserve mistakes and uncertainty; they are not certified scoring
ground truth. DeepSeek's 35 surviving messages have 33 low-confidence and two medium-confidence
readings. Compare decoder outputs by original message ID and score already-English status
entries and discarded placeholders separately. See the [reference method](gameplay/english_reference_method.md)
and [machine-readable results](gameplay/results.json) for definitions and provenance.

## Operators and sequence

| Operator | Encoding assignments | Remaining new creations |
| --- | --- | --- |
| Emma Krentz | All Sol seeds: E01–E05 | E02, E03, E04, E05 |
| Tom Taylor | E06 Haiku, E07 Gemini, E08 DeepSeek | E06, E07, E08 |

E01 reuses Emma's pushed run `logs/20261107_181546_5949aefe` at commit
`ce8dc324a83946b670348725dbcb3a7283cf41e1`. Its **130-line final shared draft** is the selected
language, not the 1,393-line concatenation of final exports. It stopped at all-done after
136 discussion calls. The original instruction allowed 500 lines and had a ten-minute
deadline with no enforced turn cap; Tom explicitly approved reuse because the actual
document and discussion are within 250 lines and 200 turns. Preserve these differences
in E01's plan and receipt.

After pulling this setup from main, read your assignment: [Emma](assignments/emma_krentz.md)
or [Tom](assignments/tom.md). Emma owns all GPT/Sol seeds; Tom owns all other encoder families.

The two operators can work simultaneously in separate checkouts. Within each operator's
list, run one experiment at a time. This keeps log ownership disjoint and limits API
contention. No run edits another run's configuration, result or receipt. Do not edit
the shared batch manifest while collecting results.

After collecting and exchanging the encoding results, **Tom runs T01–T04**. These are four
new playthroughs; Emma's already archived gameplay and decoder runs remain historical
results and are not silently substituted. Codex then writes one reference-assisted English
transcript for each new playthrough. Decoders run separately afterwards.

## Settings

| Setting | Value |
| --- | --- |
| Creation / decoder team size | 8 |
| Alphabet | 200 Tangut glyphs sampled without replacement, same set for all eight agents |
| Language document | At most 250 lines at frozen handoff |
| Creation / decoder discussion limit | 200 total scheduled agent turns per run, across the team |
| Time limit for new creation / decoding | None; all-done, turn cap, cost or fatal error stops the run |
| End-of-creation exports | Up to eight additional calls, outside the discussion-turn budget |
| Handoff selection | Last nonempty shared draft applied before creation stops |
| Reply token cap | 16,000, including reasoning |
| Reasoning | Medium for Sol, Haiku and Gemini; high for DeepSeek V4-Pro 0423 |
| Spaces and agent IDs | Allowed, matching the existing language experiment |
| Gameplay | Eight fresh agents of the encoder model; stop on escape or operational cap/error |
| Per-run spending safeguard | Existing $50 soft cap; pending/export calls may overshoot |

DeepSeek uses exact OpenRouter ID `deepseek/deepseek-v4-pro` (0423).
Its documented reasoning settings are high/xhigh, so this batch uses high rather than
assuming medium is supported. This is a recorded model-setting difference, not a claim
of matched compute. [Model documentation](https://openrouter.ai/deepseek/deepseek-v4-pro)

Human seed labels 1–5 correspond to config seeds 0–4. Config seeds control glyph sampling
and agent ordering, not API randomness. The four primary languages use config seed 0,
so their alphabet samples match when using the same dictionary and sampler. Later gameplay
must use the exact frozen sample; the helper checks it before making API calls.

The 250-line instruction is per config. The shared prompt template remains unchanged for
other experiments. The collector refuses a longer frozen reference; it does not truncate
or silently choose an earlier, shorter draft. Keep failed/over-limit runs and review them.

## Files and ownership

```
batch.json                          fixed plan and dependency graph
assignments/                        instructions for each operator
encoding/E01_sol_seed1/              one directory per creation
  plan.json                         assigned model, seed, owner and approved deviations
  config.json                       prospective settings, not a rewritten historical config
  raw/<timestamp_id_round_1>/        newly created raw logs
  handoff/swarmish.txt               frozen shared reference
  handoff/glyphs.json                exact sampled characters
  handoff/config.json               original run settings
  handoff/language_protocol.json     original requirements
  receipt.json                      provenance, hashes, calls, cost and outcome
gameplay/T01_sol/
  raw/<timestamp_id_round_2>/        raw chat, actions, private clues and model calls
  english/                          reference-assisted translation, separate from raw logs
decoding/D01_sol_to_sol_no_task/
  raw/<timestamp_id_round_3>/        independent decoder discussion and calls
  decoded.txt                       decoder's final answer
```

Existing tracked archives can be referenced in a receipt rather than duplicated; E01 uses
that approach. Raw logs retain private scratchpads and clues for researcher analysis.
The decoder input builder supplies only the public transcript and the selected briefing.
The language file and English translations are never supplied to decoder agents.

Every completed run gets its own receipt. This avoids both operators updating a shared
results spreadsheet and creates a checkable link from a language to gameplay to decoding.
Generate the current overview with `status`; do not hand-edit receipts to conceal failures.

## Commands

Run from the repository root after installing `requirements.txt` into `.venv`.
Keep `OPENROUTER_API_KEY` in the local ignored `.env`, never inside this batch.

```sh
# Offline: validate all configurations and dependencies; no API calls.
.venv/bin/python experiments/tangut_200g_250l_200t/batch.py validate
.venv/bin/python experiments/tangut_200g_250l_200t/batch.py status

# Offline: prepare E03's exact prompts in the ignored .previews directory.
.venv/bin/python experiments/tangut_200g_250l_200t/batch.py run E03 --prepare-only

# PAID: run only E03, then collect its outputs and frozen shared draft.
.venv/bin/python experiments/tangut_200g_250l_200t/batch.py run E03
```

The helper never advances automatically to another run. Each live invocation reserves its
own directory and refuses to rerun a completed slot. Run it from the same reviewed checkout
on both computers; it records revision/config/prompt provenance. A shared API key still
shares account limits. Record concurrency when interpreting wall-clock latency.

If a run already exists elsewhere, collect it without running it again:

```sh
.venv/bin/python experiments/tangut_200g_250l_200t/batch.py collect E02 /path/to/completed_round_1
```

Do not run E01 again. Its accepted import uses this source:

```sh
.venv/bin/python experiments/tangut_200g_250l_200t/batch.py collect E01 \
  logs/20261107_181546_5949aefe \
  --language-file logs/20261107_181546_5949aefe/swarmish_shared_draft.txt \
  --reference-existing
```

After all four primary handoffs are available, Tom can prepare or run `T01`, `T02`,
`T03`, and `T04` with the same `run ID [--prepare-only]` interface. Dependency and
glyph checks happen before the paid calls. Decoders use the same interface with `D01`
through `D13`, one condition per invocation, so their budget is not shared with another
condition.

## Gameplay and decoder mapping

| Gameplay | Primary language | Gameplay owner |
| --- | --- | --- |
| T01 | E01 Sol seed 1 | Tom |
| T02 | E06 Haiku seed 1 | Tom |
| T03 | E07 Gemini seed 1 | Tom |
| T04 | E08 DeepSeek seed 1 | Tom |

| Decoder run | Gameplay | Decoder | Briefing |
| --- | --- | --- | --- |
| D01 | T01 | Sol | No task |
| D02 | T01 | Sol | Some task (`task_summary`) |
| D03 | T01 | Sol | Full task |
| D04 | T01 | Sol | Lie about task (`wrong_task`) |
| D05 | T02 | Haiku | No task |
| D06 | T02 | Haiku | Full task |
| D07 | T02 | Sol | No task |
| D08 | T03 | Gemini | No task |
| D09 | T03 | Gemini | Full task |
| D10 | T03 | Sol | No task |
| D11 | T04 | DeepSeek | No task |
| D12 | T04 | DeepSeek | Full task |
| D13 | T04 | Sol | No task |

## English translations and evaluation

Codex translates each completed gameplay from its **frozen Swarmish reference**, retaining
the original public message IDs, order, sender and glyph text. Status entries remain
verbatim. Store structured translations in `english/translation.json` and the readable
group chat in `english/transcript_english.md`. Record reference/transcript hashes, ambiguity,
confidence and any departures from the reference. Preserve erroneous statements as errors;
do not rewrite them into the correct task solution.

Private intended meanings are self-reports. If inspected later, keep that comparison in
separate annotations. These reference-assisted translations are researcher artifacts,
not blind decoder outputs and not automatically a validated scoring ground truth.

## Git handoff and budget

The batch lives outside the ignored `logs/` tree, so new raw files can be added normally.
Each operator should commit their assigned run directories, not shared status files or
the other operator's work. Pull each other's completed commits before starting dependent
gameplay. Do not commit `.env`, credentials or local preview/lock files. New timestamped
raw directories and per-run receipts prevent routine filename conflicts; they do not
replace Git's normal merge checks.

There is no auto-push, background scheduler or paid run started by creating these files.
The original all-new estimate was approximately $225; E01 is now reused. The $350 budget
is a planning envelope, not an aggregate runtime limiter. The per-run $50 caps are
independent across machines. Check both operators' recorded spend before adding work.
