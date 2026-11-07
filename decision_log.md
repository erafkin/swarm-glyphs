# Decision log

Design decisions for swarm-glyphs, newest last within each section. Add to this as decisions are made.

## Infrastructure

- **No orbit / Inspect AI.** One chatroom plus a scoring timer doesn't need a multi-agent framework;
  plain `asyncio` + the `openai` SDK pointed at OpenRouter keeps it simple.
- **Pydantic** for config, game objects, agent state, and model responses.
- **One model for all agents by default** (`model`), with optional per-agent override (`agent_models`)
  for comparing model families later.
- **Never push to GitHub.**

## Game loop

- **Real-time, not rounds.** Each agent runs its own async loop and calls the model whenever it's
  ready (throttled by `min_turn_interval_s`). A separate scorer wakes every `score_interval_s` (default 90).
- **A "try" is one scoring round.** The game ends at the win threshold or after `max_score_rounds`
  (default 100).
- **Features are assigned round-robin.** Agent *i* knows feature *i mod F*. Default `n_agents` is 8
  (= number of features) so every feature is known by someone; fewer agents prints a warning.
- **The system prompt tells agents scoring happens every N seconds**, plus the win condition and round limit.
- **Responses arriving after the game stops are discarded** (cost is still counted).

## Agent responses

- **One structured JSON response per turn** (`scratchpad`, `message`, `guess`, plus `person_guess` in
  board mode), schema-enforced via `response_format`, with a fallback to parsing JSON from plain text
  for models that don't support it. Unparseable responses are logged and skipped.
- **Scratchpad can be english or glyphs and is overwritten each turn.** Every version is preserved in
  `agent_calls.jsonl`.
- **Agents must always guess.** Every feature (and the person, in board mode) must be filled in; the
  schema has no `null`. If a null/invalid value still gets through, it's rejected and the previous
  guess is kept.
- **Guesses are stored as one-hot vectors** in the canonical option order from `features.py`. Models
  output labels; we convert.

## Glyphs

- **Each glyph is a single unicode character; spaces are allowed between glyphs.** Agent IDs are also
  allowed in messages so agents can address each other.
- **A message with anything else is replaced entirely** by the shared violation token `⊘`. Newlines
  count as violations.
- **Glyphs load from a .txt file** (`glyphs_path`, default `src/agent_models/glyphs.txt`). Every
  non-whitespace character is one glyph; duplicates and the violation token are rejected.
  We start with 18 glyphs. The current file is a placeholder until the real set is pasted in.
- **Glyph order is shuffled per agent** (`glyphs_view`), so each model sees a differently ordered list.

## Goal object and modes

- **Every agent sees all feature names and possible values**, but only the true value of its own feature.
- **Features** (`features.py`): hair_colour, hairstyle, facial_hair, glasses, clothing,
  clothing_colour, background, expression; 4 options each.
- **Two modes** (`mode` in config):
  - `features`: agents guess every feature; feedback is per-feature accuracy across agents.
    Win condition is configurable (`win_mode`): `agents` (default; ≥ threshold of agents have every
    feature right) or `features` (every feature right for ≥ threshold of agents).
  - `board` (Guess Who): agents see a board of 32 people and output the goal person's number. They
    still fill in per-feature guesses as notes (logged, not scored). Score is the fraction of agents
    who picked the right person; win when that's ≥ `win_threshold`.
- **One universal board** in `src/game_object/board.json`: 32 people numbered 1-32, features in
  one-hot form. People are referred to by these numbers everywhere (prompts, guesses, logs).
- **The goal is always a board person, chosen by seed, in both modes.** The default seed 0 is always
  person 22 (brown curls, beard, no glasses, blue shirt, green background, smile). Other seeds pick
  a fixed person per seed (separate RNG, so the same seed gives the same goal in both modes); seed
  `null` is random. `goal_person` overrides the seed. In features mode the board is only used to
  look up the goal's characteristics; it isn't shown to agents.
- **Seed also drives per-agent shuffles and starting guesses**, so the default config is fully reproducible.

## Scoring

- **Only group-level results are posted** to the chatroom, in english; individual guesses are never revealed.
- **Per-feature accuracy is logged in board mode too**, but not shown to agents.
- **Chance baselines are logged, not posted**: `feature_chance` (1/options), `fully_correct_chance`,
  and `person_chance` (1/board size) are in every `scores.jsonl` record.

## Bias mitigation

The first dry runs showed agents picking the first listed option when unsure (and person 0 in board
mode), which inflated scores for goals whose values happened to be listed first.

- **Option order is shuffled per agent** (`features_view`), in both the prompt and the response
  schema enum. Feature order is unchanged.
- **Board listing order is shuffled per agent** (`board_order`). Person numbers stay fixed across
  agents, so "person 23" means the same person to everyone; only the order they're listed in differs.
- **Agents start from a random guess** (and a random person in board mode) instead of an empty one.
  Since every response must fill in every guess, this only matters before an agent's first response.
- Per-agent views are recorded in `agents.json`.

## End-of-game interview

- After the game ends (not on Ctrl-C), each agent is asked, in parallel:
  **"Explain your communication strategy with the other agents"**. Free text, no schema. The agent's
  system prompt, recent chat, scratchpad, and current guess are included as context.
- Answers go to `final_interviews.jsonl`. Toggle with `final_interview` in config.
- Replaced an earlier per-glyph "what does each glyph mean" interview.

## Logging

Each game writes `logs/<timestamp>_<game_id>/`: `config.json`, `goal.json`, `glyphs.json`, `board.json` (board mode),
`agents.json` (system prompts and per-agent views), `chatroom.jsonl`, `agent_calls.jsonl`,
`scores.jsonl`, `final_interviews.jsonl`, `errors.jsonl`, `summary.json` (stop reason, final score,
total cost from OpenRouter usage accounting).
