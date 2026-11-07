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
.venv/bin/python -m src.scripts.run_features_seed0
```

Two modes (`mode` in the config):
- `features`: agents guess every feature; feedback is per-feature accuracy across agents.
- `board`: agents see the board of 32 people (`src/game_object/board.json`) and guess the goal
  person's name, a random UUID (scored as % of agents correct).

In both modes the goal is a board person chosen by `seed`: seed 0 (the default) is
`c5cfd9c46c6840e9bd503464fab926f0` (formerly person 22), other seeds pick a different fixed person,
and `goal_person` (a name) overrides the seed.
Each game samples `n_glyphs` (default 18) glyphs from `glyph_dictionary` (`dictionary_a` (default) or
`dictionary_b`, the .txt files at the repo root), shared by all agents. Each agent sees the glyphs,
feature options, and board in its own random order.

Logs go to `logs/<timestamp>_<game_id>/`: `config.json`, `goal.json`, `glyphs.json`, `board.json` (board mode),
`agents.json` (system prompts), `chatroom.jsonl`, `agent_calls.jsonl` (every response, scratchpad,
and guess), `scores.jsonl`, `final_interviews.jsonl` (each agent's end-of-game explanation of its communication strategy),
`errors.jsonl`, `summary.json` (stop reason, final score, total cost).
Glyph dictionaries live under dictionary_n.txt. Each contains 50 symbols that should be sampled and randomly ordered when read into model context. dictionary_a.txt contains Tangut ideographs (https://en.wikipedia.org/wiki/Tangut_script) and dictionary_b.txt contains unassigned plane-4 Unicode characters (https://en.wikipedia.org/wiki/Plane_(Unicode)).
