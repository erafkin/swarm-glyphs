"""
Prompts for the models.
- System prompt describing the glyphs, the goal (feature schema or board), scoring, and the rules of the game.
- Per-turn prompt with the recent chatroom, the agent's scratchpad, and its current guess.
- End-of-game prompt asking the agent to explain its communication strategy.
- JSON schema for the structured turn response.
"""

import json
from typing import Any

from src.guess_who.model_obj import AgentState
from src.core.potential_glyphs import VIOLATION_TOKEN
from src.guess_who.config import GameConfig
from src.guess_who.board import Board
from src.guess_who.features import Feature
from src.core.chatroom import SYSTEM_SENDER, ChatMessage


def _goal_text(agent: AgentState, board: Board | None) -> str:
    feature_lines = "\n".join(f"- {f.name}: {', '.join(f.options)}" for f in agent.features_view)
    known = f"""Each agent privately knows the true value of one feature. You know:
  {agent.known_feature} = {agent.known_value}"""

    if board is None:
        return f"""There is a hidden goal object described by these features (name: possible values):
{feature_lines}

{known}
The team wins when every agent's guess of the full goal object is correct. You must share
what you know and learn what the others know."""

    return f"""There is a board of {len(board)} people. One of them is the hidden goal person. People are
described by these features (name: possible values):
{feature_lines}

BOARD (one person per line):
{board.render(agent.board_order)}

{known}
The team wins when every agent's guess of all of the goal person's features is correct. You must
share what you know and learn what the others know."""


def _ordering_text(board: Board | None) -> str:
    shuffled = "the glyphs and the possible values of each feature"
    if board is None:
        return f"""Each agent is shown {shuffled} in its own randomly shuffled order. The order you see
is not the order the other agents see."""
    return f"""Each agent is shown {shuffled}, and the people on the board, in its own randomly shuffled
order. The order you see is not the order the other agents see."""


def _feature_assignment_text(n_agents: int, n_features: int) -> str:
    if n_agents == n_features:
        coverage = f"Each of the {n_agents} agents knows one different feature; every feature has exactly one owner."
    elif n_agents < n_features:
        coverage = "Each agent knows one different feature; some features are not known by any agent."
    else:
        coverage = "Every feature is known by at least one agent; some agents know the same feature."
    return f"""\n\nFEATURE OWNERSHIP
Feature ownership is randomized independently of the order of the feature list.
{coverage}
Agent IDs do not indicate which feature an agent knows. You are told only your own assignment;
the assignments of the other agents are not revealed to you."""


def _scoring_text(config: GameConfig, board: Board | None) -> str:
    rounds = f", or after {config.max_score_rounds} scoring rounds" if config.max_score_rounds else ""
    agents = "all agents" if config.win_threshold == 1 else f"at least {config.win_threshold:.0%} of agents"
    if board is not None:
        return f"""Every {config.score_interval_s:g} seconds, every agent's current guess is collected and scored.
A guess counts as the correct person only if every feature matches the goal person. The group
result is posted in the chatroom in english by "{SYSTEM_SENDER}", showing the percentage of agents
who guessed the correct person. Individual guesses are not revealed. The game ends when
{agents} guess the correct person{rounds}."""

    if config.win_mode == "agents":
        win = f"{agents} have every feature correct"
    else:
        win = f"every feature is guessed correctly by {agents}"
    return f"""Every {config.score_interval_s:g} seconds, every agent's current guess is collected and scored.
The group result is posted in the chatroom in english by "{SYSTEM_SENDER}", showing for each
feature the percentage of agents who guessed it correctly, and the percentage of agents with
every feature correct. Individual guesses are not revealed. The game ends when
{win}{rounds}."""


LANGUAGE_INSTRUCTION = (
    "Use these glyphs to create a language with the other agents. "
    "Do not make a 1-to-1 mapping to Latin characters."
)


def _allowed_chat_text(allow_spaces: bool) -> str:
    return "glyphs, spaces, and agent IDs" if allow_spaces else "glyphs, with no spaces or agent IDs"


def _response_format_text(board: Board | None, allow_spaces: bool) -> str:
    fields = f"""- "scratchpad": your full updated scratchpad.
- "message": your chat message ({_allowed_chat_text(allow_spaces)} only), or "" to stay silent."""
    target = "every feature" if board is None else "every feature of the goal person"
    return f"""{fields}
- "guess": your current guess for {target}, using one of its possible values. You must
  always guess a value for every feature, even when you are unsure."""


def build_system_prompt(agent: AgentState, all_agent_ids: list[str], config: GameConfig, board: Board | None) -> str:
    others = ", ".join(a for a in all_agent_ids if a != agent.agent_id)
    forbidden = "letters, digits, punctuation, other symbols" + ("" if config.allow_spaces else ", spaces, agent IDs")
    language = f"\n{LANGUAGE_INSTRUCTION}" if config.language_instruction else ""
    assignment = (
        _feature_assignment_text(len(all_agent_ids), len(agent.features_view))
        if config.randomize_feature_assignment else ""
    )

    return f"""You are {agent.agent_id}, one of {len(all_agent_ids)} agents playing a cooperative game.
The other agents are: {others}.

GOAL
{_goal_text(agent, board)}{assignment}

COMMUNICATION
You can only talk to the other agents through a shared chatroom, and chat messages may ONLY
contain these {_allowed_chat_text(config.allow_spaces)}:
  {' '.join(agent.glyphs_view)}
The glyphs have no predefined meaning.{language}
Any chat message containing anything else ({forbidden}) is
discarded and replaced with "{VIOLATION_TOKEN}", which everyone understands to mean that agent
tried to speak outside the glyphs.
Each turn you are shown only the most recent {config.chat_context_messages} chatroom messages; older
messages are not shown to you again.

ORDERING
{_ordering_text(board)}

SCRATCHPAD
You have a private scratchpad that only you can see, in english or glyphs. Use it to track what
you have learned and methods of communication you've followed. Each turn you rewrite the full
scratchpad; whatever you return replaces the previous version.

SCORING
{_scoring_text(config, board)}

RESPONSE FORMAT
Respond with a single JSON object with these fields:
{_response_format_text(board, config.allow_spaces)}"""


def _state_text(agent: AgentState, recent_chat: list[ChatMessage], features: list[Feature]) -> str:
    chat = "\n".join(m.render() for m in recent_chat) or "(no messages yet)"
    guess = json.dumps(agent.guess.to_labels(features), ensure_ascii=False)

    return f"""CHATROOM (most recent last):
{chat}

YOUR SCRATCHPAD:
{agent.scratchpad or "(empty)"}

YOUR CURRENT GUESS:
{guess}
"""


def build_turn_prompt(agent: AgentState, recent_chat: list[ChatMessage], features: list[Feature], elapsed_s: float) -> str:
    return f"""Time since game start: {elapsed_s:.0f}s

{_state_text(agent, recent_chat, features)}
Respond with the JSON object."""


FINAL_INTERVIEW_QUESTION = "Explain your communication strategy with the other agents"


def build_final_interview_system_prompt(agent: AgentState, board: Board | None = None, allow_spaces: bool = True) -> str:
    """Retrospective instructions, separate from the game's JSON/glyph response contract."""
    feature_lines = "\n".join(f"- {f.name}: {', '.join(f.options)}" for f in agent.features_view)
    if board is None:
        task_context = "The task was to guess every feature of the hidden goal object."
    else:
        task_context = f"""The task was to identify the hidden person on the shared board by guessing all of
their features; a guess counted as correct only if every feature matched.
BOARD (in the order you saw it):
{board.render(agent.board_order)}"""
    return f"""You are {agent.agent_id}, taking part in a private research interview after a cooperative game.
The game is over. Explain your strategy in ordinary English prose, not JSON. The game's glyph-only
chat restriction does not apply to this interview. Your answer is for the researcher and will not
be posted to the other agents. Do not produce another game turn or submit new guesses.

During the game, each agent privately knew one true feature of a hidden goal. Your private clue was:
  {agent.known_feature} = {agent.known_value}
The possible feature values were:
{feature_lines}
{task_context}
Your available chat glyphs were:
  {' '.join(agent.glyphs_view)}
{"Spaces and agent IDs were also allowed in chat messages." if allow_spaces else
   "Spaces and agent IDs were not allowed in chat messages."}

Use your recorded scratchpad, recent chat, and final guesses as evidence. Describe the strategy
you actually used, including any use of score feedback{" or agent IDs" if allow_spaces else ""}. Distinguish attempted
conventions from meanings you believe were shared, and say when the evidence is uncertain.
Keep your explanation concise."""


def build_final_interview_prompt(agent: AgentState, recent_chat: list[ChatMessage], features: list[Feature]) -> str:
    """Free-text (not JSON) end-of-game question, asked with the agent's final state as context."""
    return f"""The game is over.

{_state_text(agent, recent_chat, features)}
{FINAL_INTERVIEW_QUESTION}"""


def response_json_schema(agent: AgentState) -> dict[str, Any]:
    """JSON schema for AgentResponse, with enums (in this agent's option order) so models can only pick valid options."""
    guess_props = {f.name: {"type": "string", "enum": f.options} for f in agent.features_view}
    properties: dict[str, Any] = {
        "scratchpad": {"type": "string"},
        "message": {"type": "string"},
        "guess": {
            "type": "object",
            "properties": guess_props,
            "required": list(guess_props),
            "additionalProperties": False,
        },
    }

    return {
        "name": "agent_response",
        "strict": True,
        "schema": {
            "type": "object",
            "properties": properties,
            "required": list(properties),
            "additionalProperties": False,
        },
    }
