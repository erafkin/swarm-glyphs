# Swarm languages: Encoding and decoding natural language in agent swarms. 
Submission to [swarm alignment hackathon](https://www.aialignmentfoundation.org/hackathons/swarm-alignment-2026)

Can we get agents to create a new language? Is that language monitorable/decodable?



## Setup

```
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
echo "OPENROUTER_API_KEY=..." > .env
```

## Guess Who
Agents that each know one feature of a hidden goal object try to reach consensus on the full
object, communicating only through a chatroom of meaningless glyphs.

```
.venv/bin/python -m src.guess_who.play_game                              # defaults (src/guess_who/config.py)
.venv/bin/python -m src.guess_who.play_game --config configs/dry_run.json        # per-feature feedback
.venv/bin/python -m src.guess_who.play_game --config configs/board_dry_run.json  # Guess Who board
```

First test runs (GPT-6.1 Sol, seed 0, stop at all-correct or $50):

```
.venv/bin/python -m src.guess_who.scripts.run_board_seed0
.venv/bin/python -m src.guess_who.scripts.run_board_seed0 src/guess_who/scripts/board_seed0_no_spaces.json  # no spaces in chat
.venv/bin/python -m src.guess_who.scripts.run_features_seed0
.venv/bin/python -m src.guess_who.scripts.run_features_seed0 src/guess_who/scripts/features_seed0_no_spaces.json  # glyphs only
```

`allow_spaces: false` in any config forbids spaces and agent IDs in chat messages: glyphs only.
`language_instruction: true` (on in both board configs) tells agents to build a language from the
glyphs rather than a 1-to-1 mapping to Latin characters.
The features no-spaces variant keeps the same eight agents, seed, model, scoring, and budget
as `features_seed0.json`; only the communication restriction changes. Sender labels remain visible.

Scoring runs every **60 seconds** (`score_interval_s: 60`) by default and in all current run configs.
All shipped configs enable `randomize_feature_assignment`: with eight agents and eight features,
each feature is privately assigned to exactly one agent by a seeded random permutation. Agents are
told that IDs do not reveal feature ownership. The public feature list stays in the same order;
the assignment uses a separate RNG so it does not change glyph, option, or initial-guess shuffles.
The flag defaults to false when omitted, preserving older saved configurations.
The Sol experiment configs use **medium** reasoning and a 16,000-token budget per gameplay
call. End-of-game interviews use a separate English-only prompt, **medium** reasoning, and a 16,000-token
budget. These budgets include hidden reasoning tokens. Temperature is omitted.
The $50 cap is soft: calls already in flight finish and are logged before the interviews run.
Responses received after stopping are retained with `state_applied: false` and `ignored_reason`;
they do not update guesses or chat.

### Random feature ownership: five Gemini runs

[`configs/gemini_random_features_5x60s`](configs/gemini_random_features_5x60s/README.md) contains
five independent eight-agent Gemini 3.8 Flash configurations, with seeds 0–4, 60-second feedback,
strict glyph-only messages, medium reasoning, and a **$20 soft cap per run**. Each run starts with
a fresh chatroom and scratchpads. Launch only run 1 initially; review it before starting runs 2–5.
There is no automatic batch continuation.

```sh
.venv/bin/python -m src.guess_who.scripts.run_features_seed0 configs/gemini_random_features_5x60s/run_1_seed0.json
```

### Archived experiments

- [Randomized ownership: Gemini, Sol and mixed comparison](results/randomized_features_seed0/README.md)
- [Gemini count encoding and glyph-choice follow-up interviews](logs/20261107_074528_12f02cc3/README.md)
- [Mixed Sol/Gemini binary ASCII and cross-model translation](logs/20261107_082059_9490e69c/README.md)
- [Strict Sol binary ASCII and Morse SOS](logs/20261106_223314_5e5f03a8/README.md)

Archives retain the exact settings used at the time. The randomized-ownership comparison uses
60-second feedback; the three earlier experiments use four-minute scoring and fixed ownership.
Current launch presets use the settings described above.

## Language handoff

**Storm Shelter is the implemented eight-agent escape-room task.** See
[the full room definition and monitor protocol](docs/storm_shelter.md) for the private
clues, action rules, four monitor briefings and saved-log replay instructions.
The first run uses the selected current setup: eight creators discussing asynchronously
for up to ten minutes, then a fresh eight-agent task team. The creation and monitor prompts
are now connected to the editable templates in `src/enc_dec/prompts/`.

Edit `round1_prompt.md` / `round1_config.json` for language-design instructions and
`round3_prompt.md` / `round3_config.json` for monitor instructions and conditions. Run
settings (model, alphabet, agent count, timing and budget) live in `configs/storm_shelter_*.json`.

```sh
# Inspect the eight starting prompts without API calls.
.venv/bin/python -m src.enc_dec.run configs/storm_shelter_tangut.json --prepare-only

# Create swarmish, then play with a fresh team ($50 combined soft cap).
.venv/bin/python -m src.enc_dec.run configs/storm_shelter_tangut.json

# Or import a frozen language, skipping creation.
.venv/bin/python -m src.enc_dec.run configs/storm_shelter_tangut.json --language-file /path/to/swarmish.txt

# After the task, inspect four monitor briefings on the SAME saved chat.
.venv/bin/python -m src.enc_dec.monitor logs/RUN --prepare-only
# Remove --prepare-only to make decoding calls; separate default $50 cap for the whole monitor batch.
# A decoding team of three per condition, five minutes each; both override the saved config.
.venv/bin/python -m src.enc_dec.monitor logs/RUN --agents 3 --minutes 5
```

The room has no rounds or invalid-attempt loss limit. Clues unlock as the team opens the
cabinet, restores power and solves the exit. Private submissions never enter the chat;
public feedback is only numeric stage and invalid-attempt count. The presets stop on
escape or an operational spending/error stop, retain pending responses in the logs,
and defer all monitors. `storm_shelter_latin.json` restricts the chat to a-z and 0-9 instead of
Tangut. Both presets name the language **swarmish**.

Custom text tasks use the same runner and monitor with `task_kind: custom`:

A separate run from the guessing game. One team has N minutes (`language_minutes`, 10 in the
shipped configs) to invent a language without being told the task. That planning chat is ordinary
English, with no scratchpad. Each turn they see the latest 100 messages and the current shared
`swarmish.txt`, which any of them can replace. At the end they write `swarmish.txt` once more;
the other saved output is the planning chatroom. The round 1 system prompt is the template
`src/enc_dec/prompts/round1_prompt.md`, with its toggles in `round1_config.json`.
A new team then receives only that file and the task, and works on it in the language for
`task_minutes`. With `task_feedback` true (the default), the task posts status updates into that
chatroom; set it false to leave them out. The saved task chat is the agents'
language messages plus that feedback. A decoding team of `monitor_n_agents` decoders (1 by
default) then reads only that chatroom, once per briefing listed in
`src/enc_dec/prompts/round3_config.json` (by default task summary, full task knowledge, no task,
and a wrong task). Like round 1, the team discusses in English and shares one draft of the judged
document until every decoder sets done or `monitor_minutes` (10) run out; the system prompt is
`round3_prompt.md` with the mechanics from `round3_config.json`. The task
chat may use only characters from the glyph file named by `glyph_dictionary`:
`glyphs_tangut.txt` (every Tangut ideograph, 6,136 of them) in `language_tangut.json`, or
`glyphs_latin.txt` (a-z and 0-9) in `language_latin.json`. Anything else is replaced by `⊘`.
The task strings in both files are placeholders.

```
.venv/bin/python -m src.enc_dec.run src/enc_dec/scripts/language_tangut.json
.venv/bin/python -m src.enc_dec.run src/enc_dec/scripts/language_latin.json
```

Those custom-task presets are placeholder examples, not Storm Shelter launches.
`src.enc_dec.scripts.run_language_round` remains a compatibility alias for the same CLI,
including `--prepare-only` and `--language-file`. Inline and standalone monitors use the
same numbered transcript and cost controls.

## Game and logs

Two modes (`mode` in the config):
- `features`: agents guess every feature; feedback is per-feature accuracy across agents.
- `board`: agents also see the board of 32 people (`src/guess_who/board.json`, listed without
  identifiers) and guess every feature of the goal person; feedback is the % of agents with every
  feature right ("guessed the correct person").

In both modes the goal is a board person chosen by `seed`: seed 0 (the default) is person 22,
other seeds pick a different fixed person, and `goal_person` (a board.json number) overrides the seed.
Each game samples `n_glyphs` (default 18) glyphs from `glyph_dictionary` (`dictionary_a` (default) or
`dictionary_b`, the .txt files at the repo root), shared by all agents. Each agent sees the glyphs,
feature options, and board in its own random order.

Logs go to `logs/<timestamp>_<game_id>/` (the language experiment appends what the run covered, such as `_round_1`, `_round_2` or `_round_1_2_3`, and monitor replays end in `_round_3`): `config.json`, `goal.json`, `glyphs.json`, `board.json` (board mode),
`agents.json` (system prompts), `chatroom.jsonl`, `agent_calls.jsonl` (every response, scratchpad,
and guess), `scores.jsonl`, `final_interviews.jsonl` (each agent's end-of-game explanation of its communication strategy),
`errors.jsonl`, `summary.json` (stop reason, final score, total cost).
For the language experiment, `glyphs_tangut.txt` holds every Tangut ideograph (6,136, unscreened) and `glyphs_latin.txt` holds a-z and 0-9; `glyph_dictionary` in a config names one of them. For the guessing game, glyph dictionaries live under dictionary_n.txt. Each contains 50 symbols that should be sampled and randomly ordered when read into model context. dictionary_a.txt contains Tangut ideographs (https://en.wikipedia.org/wiki/Tangut_script) and dictionary_b.txt contains unassigned plane-4 Unicode characters (https://en.wikipedia.org/wiki/Plane_(Unicode)).
