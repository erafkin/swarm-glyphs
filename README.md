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

Two modes (`mode` in the config):
- `features`: agents guess every feature; feedback is per-feature accuracy across agents.
- `board`: agents see the board of 32 people (`src/game_object/board.json`) and guess the goal
  person's number (scored as % of agents correct).

In both modes the goal is a board person chosen by `seed`: seed 0 (the default) is person 22, other
seeds pick a different fixed person, and `goal_person` overrides the seed.
Glyphs are loaded from `src/agent_models/glyphs.txt` (`glyphs_path`); every non-whitespace character
is one glyph. Each agent sees the glyphs, feature options, and board in its own random order.

Logs go to `logs/<timestamp>_<game_id>/`: `config.json`, `goal.json`, `glyphs.json`, `board.json` (board mode),
`agents.json` (system prompts), `chatroom.jsonl`, `agent_calls.jsonl` (every response, scratchpad,
and guess), `scores.jsonl`, `final_interviews.jsonl` (each agent's end-of-game explanation of its communication strategy),
`errors.jsonl`, `summary.json` (stop reason, final score, total cost).