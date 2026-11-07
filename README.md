# Alignment Swarm Hackathon
Agents that each know one feature of a hidden goal object try to reach consensus on the full
object, communicating only through a chatroom of meaningless glyphs.

## Setup

```
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
echo "OPENROUTER_API_KEY=..." > .env
```

## Run

```
.venv/bin/python -m src.gameplay.play_game                              # defaults (src/config.py)
.venv/bin/python -m src.gameplay.play_game --config configs/dry_run.json        # per-feature feedback
.venv/bin/python -m src.gameplay.play_game --config configs/board_dry_run.json  # Guess Who board
```

First test runs (GPT-6.1 Sol, seed 0, stop at all-correct or $50):

```
.venv/bin/python -m src.scripts.run_board_seed0
.venv/bin/python -m src.scripts.run_board_seed0 src/scripts/board_seed0_no_spaces.json  # no spaces in chat
.venv/bin/python -m src.scripts.run_features_seed0
.venv/bin/python -m src.scripts.run_features_seed0 src/scripts/features_seed0_no_spaces.json  # glyphs only
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

## Random feature ownership: five Gemini runs

[`configs/gemini_random_features_5x60s`](configs/gemini_random_features_5x60s/README.md) contains
five independent eight-agent Gemini 3.8 Flash configurations, with seeds 0–4, 60-second feedback,
strict glyph-only messages, medium reasoning, and a **$20 soft cap per run**. Each run starts with
a fresh chatroom and scratchpads. Launch only run 1 initially; review it before starting runs 2–5.
There is no automatic batch continuation.

```sh
.venv/bin/python -m src.scripts.run_features_seed0 configs/gemini_random_features_5x60s/run_1_seed0.json
```

## Archived experiments

- [Gemini count encoding and glyph-choice follow-up interviews](logs/20261107_074528_12f02cc3/README.md)
- [Mixed Sol/Gemini binary ASCII and cross-model translation](logs/20261107_082059_9490e69c/README.md)
- [Strict Sol binary ASCII and Morse SOS](logs/20261106_223314_5e5f03a8/README.md)

Archives retain the exact settings used at the time, including four-minute scoring and fixed
feature ownership in these earlier runs. Current launch presets use the settings described above.

## Game and logs

Two modes (`mode` in the config):
- `features`: agents guess every feature; feedback is per-feature accuracy across agents.
- `board`: agents also see the board of 32 people (`src/game_object/board.json`, listed without
  identifiers) and guess every feature of the goal person; feedback is the % of agents with every
  feature right ("guessed the correct person").

In both modes the goal is a board person chosen by `seed`: seed 0 (the default) is person 22,
other seeds pick a different fixed person, and `goal_person` (a board.json number) overrides the seed.
Each game samples `n_glyphs` (default 18) glyphs from `glyph_dictionary` (`dictionary_a` (default) or
`dictionary_b`, the .txt files at the repo root), shared by all agents. Each agent sees the glyphs,
feature options, and board in its own random order.

Logs go to `logs/<timestamp>_<game_id>/`: `config.json`, `goal.json`, `glyphs.json`, `board.json` (board mode),
`agents.json` (system prompts), `chatroom.jsonl`, `agent_calls.jsonl` (every response, scratchpad,
and guess), `scores.jsonl`, `final_interviews.jsonl` (each agent's end-of-game explanation of its communication strategy),
`errors.jsonl`, `summary.json` (stop reason, final score, total cost).
Glyph dictionaries live under dictionary_n.txt. Each contains 50 symbols that should be sampled and randomly ordered when read into model context. dictionary_a.txt contains Tangut ideographs (https://en.wikipedia.org/wiki/Tangut_script) and dictionary_b.txt contains unassigned plane-4 Unicode characters (https://en.wikipedia.org/wiki/Plane_(Unicode)).
