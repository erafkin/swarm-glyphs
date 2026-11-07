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
  ready (throttled by `min_turn_interval_s`). A separate scorer wakes every `score_interval_s` (default 240 seconds / 4 minutes).
- **A "try" is one scoring round.** The game ends at the win threshold or after `max_score_rounds`
  (default 100).
- **Features are assigned round-robin.** Agent *i* knows feature *i mod F*. Default `n_agents` is 8
  (= number of features) so every feature is known by someone; fewer agents prints a warning.
- **The system prompt tells agents scoring happens every N seconds**, plus the win condition and round limit.
- **Agents see only the most recent `chat_context_messages` (default 50) chat messages per turn**, and
  the system prompt tells them so (anything older has to be kept in their scratchpad).
- **Responses arriving at or after the stop are logged without changing game state.** This includes
  the response that reaches the cost cap. Logs preserve raw output, parsed `response`, and usage;
  `state_applied: false` and `ignored_reason` distinguish responses excluded from gameplay.
  `turns_per_agent` counts all returned gameplay calls, including these unapplied responses.
- **Normal shutdown drains in-flight calls** before interviews and the summary, so their usage and
  output are recorded. No new gameplay calls start after the stop. Ctrl-C and fatal API errors
  cancel pending calls instead; provider charges for cancelled requests may be unavailable locally.
- **Cost cap** (`max_cost_usd`): the game stops once total OpenRouter cost (from per-call usage
  accounting) reaches the cap. In-flight calls and the final interview still run, so the total can
  overshoot by roughly one call per agent for each. `max_score_rounds: null` disables the round limit.
- **Transient API errors are retried; fatal ones stop the game.** Rate limits, 5xx, and timeouts get
  the SDK's 2 retries, then per-agent exponential backoff (5s to 120s) with the error in `errors.jsonl`.
  401 (bad key), 402 (no credits), and 404 (unknown model) stop the game immediately with
  `stop_reason = fatal_api_error_<code>: <agent> (<model>)`, skipping the final interview, since a
  game where agents can't act isn't a valid run. 403 is not fatal (OpenRouter uses it for
  per-request moderation flags).

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
- **Optional language instruction** (`language_instruction`, default false): adds "Use these glyphs
  to create a language with the other agents. Do not make a 1-to-1 mapping to Latin characters."
  after "The glyphs have no predefined meaning." On in both board seed-0 configs (with and without
  spaces), off in features mode.
- **Spaces are configurable** (`allow_spaces`, default true). With `allow_spaces: false`, any space
  makes the message a violation, and the prompts say so. Agent IDs are not allowed in messages
  either (a brief prefix-only version was dropped), so IDs cannot stand in for spaces as
  delimiters; messages are glyphs only. Agents still see each message's sender in the chat log.
  With spaces on, IDs may appear anywhere.
  `src/scripts/board_seed0_no_spaces.json` and `src/scripts/features_seed0_no_spaces.json`
  are the board and features seed-0 runs with only this changed. Both launchers accept
  an optional config path; the original configs remain their defaults.
- **A message with anything else is replaced entirely** by the shared violation token `⊘`. Newlines
  count as violations.
- **Glyphs come from one of two dictionaries** (`glyph_dictionary`: `dictionary_a` (default) or
  `dictionary_b`, 50 glyphs each in `dictionary_a.txt` / `dictionary_b.txt` at the repo root). Every
  non-whitespace character is one glyph; duplicates and the violation token are rejected.
  Dictionary A is Tangut-block characters; dictionary B is unassigned code points (plane 4).
- **Each game samples `n_glyphs` (default 18) from the dictionary**, without replacement, using the
  game seed. All agents share that set; a dictionary glyph outside the sampled set is a violation.
- **Glyph order is shuffled per agent** (`glyphs_view`), so each model sees a differently ordered list.
  The sampled set is saved to `glyphs.json`; each agent's order is in `agents.json`.

## Goal object and modes

- **Every agent sees all feature names and possible values**, but only the true value of its own feature.
- **Features** (`features.py`): hair_colour, hairstyle, facial_hair, glasses, clothing,
  clothing_colour, background, expression; 4 options each.
- **Two modes** (`mode` in config):
  - `features`: agents guess every feature; feedback is per-feature accuracy across agents.
    Win condition is configurable (`win_mode`): `agents` (default; ≥ threshold of agents have every
    feature right) or `features` (every feature right for ≥ threshold of agents).
  - `board` (Guess Who): agents see a board of 32 people and guess every feature of the goal person,
    same output as features mode. A guess counts as the correct person only if every feature
    matches. Score is the fraction of agents who guessed the correct person; win when that's
    ≥ `win_threshold`.
- **One universal board** in `src/game_object/board.json`: 32 people numbered 1-32, features in one-hot form.
- **Agents never see a person identifier.** The board is listed without numbers or names, in a
  different shuffled order per agent. Earlier versions had agents guess a person number, then a
  random UUID name; both were replaced by guessing the features directly, which removes any shared
  identifier order to enumerate through the scoreboard. Numbers are only used internally (goal
  selection, logs, `board_order` in `agents.json`).
- **Remaining scoreboard probing is accepted.** Agents could still enumerate guesses via the score
  posts, but that takes enough coordination to be acceptable.
  No guess-consistency restriction, guess-change budget, or coarser feedback for now.
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
  and `person_chance` (board mode) are in every `scores.jsonl` record.

## Bias mitigation

The first dry runs showed agents picking the first listed option when unsure (and person 0 in board
mode), which inflated scores for goals whose values happened to be listed first.

- **Option order is shuffled per agent** (`features_view`), in both the prompt and the response
  schema enum. Feature order is unchanged.
- **Board listing order is shuffled per agent** (`board_order`).
- **Agents start from a random guess** instead of an empty one.
  Since every response must fill in every guess, this only matters before an agent's first response.
- Per-agent views are recorded in `agents.json`.
- **Agents are told the order is shuffled per agent** (ORDERING section of the system prompt). Added after a GPT-6.1 Sol test turn proposed a protocol based on
  "listed order", which can't work when every agent's lists are ordered differently. The prompt
  states the fact only; it doesn't suggest a protocol.

## End-of-game interview

- After the game ends (not on Ctrl-C), each agent is asked, in parallel:
  **"Explain your communication strategy with the other agents"**. Free text, no schema. A separate
  interview system prompt requests concise English rather than another JSON gameplay turn. It
  includes the agent's identity, private clue, feature options, glyphs, and board in board mode; the user prompt includes
  recent chat, scratchpad, and current guesses. It asks for evidence and uncertainty, including
  any use of score feedback or agent IDs. Answers are private to the researcher.
- **Interview settings are separate.** `final_interview_max_tokens` defaults to 16000, capped by the
  gameplay `max_tokens`; `final_interview_reasoning_effort` defaults to inheriting gameplay effort.
  The two Sol experiment configs explicitly use medium effort and a 16000-token cap for both phases.
  Interview tokens include hidden reasoning. Interviews still run past the soft cost limit.
- Answers, system/user prompts, effective token/effort settings, and usage go to
  `final_interviews.jsonl`. Toggle with `final_interview` in config.
- Replaced an earlier per-glyph "what does each glyph mean" interview.

## First test runs (`src/scripts/`)

- Two runs, seed 0 (goal person 22), 8 agents on `openai/gpt-6.1-sol`, `dictionary_a`, 18 glyphs,
  scoring every 4 minutes (240 seconds): `run_board_seed0.py` and `run_features_seed0.py`, each with a JSON config next to it.
  `run_board_seed0.py` takes an optional config path (default `board_seed0.json`).
- **Stop only when every agent is right or the run's cost hits $50**: `win_threshold: 1.0`
  (features mode: `win_mode: agents`, i.e. every agent has every feature right), `max_cost_usd: 50`,
  no round limit.
- GPT-6.1 Sol is a reasoning model that doesn't list `temperature` as supported, so `temperature` is
  omitted and `max_tokens` is raised to 16000 (it includes hidden reasoning tokens). Request timeout
  raised to 300s. Gameplay reasoning effort is explicitly `medium`, matching the current model
  default; interview effort is also `medium` with a 16000-token cap. The game seed controls local setup,
  not the model's sampling, so repeated runs can produce different conversations.

## Logging

Each game writes `logs/<timestamp>_<game_id>/`: `config.json`, `goal.json`, `glyphs.json`, `board.json` (board mode),
`agents.json` (system prompts and per-agent views), `chatroom.jsonl`, `agent_calls.jsonl`,
`scores.jsonl`, `final_interviews.jsonl`, `errors.jsonl`, `summary.json` (stop reason, final score,
total cost from OpenRouter usage accounting).
