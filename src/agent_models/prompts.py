"""
Prompts for the models.
- System prompt describing the glyphs, the goal (feature schema or board), scoring, and the rules of the game.
- Per-turn prompt with the recent chatroom, the agent's scratchpad, and its current guess.
- End-of-game prompt asking the agent to explain its communication strategy.
- JSON schema for the structured turn response.
"""

import json
from typing import Any

from src.agent_models.model_obj import AgentState
from src.agent_models.potential_glyphs import VIOLATION_TOKEN
from src.config import GameConfig
from src.game_object.board import Board
from src.game_object.features import Feature
from src.gameplay.chatroom import SYSTEM_SENDER, ChatMessage


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

BOARD:
{board.render(agent.board_order)}

{known}
The team wins when the agents identify which person on the board is the goal person. You must
share what you know and learn what the others know."""


def _scoring_text(config: GameConfig, board: Board | None) -> str:
    rounds = f"or after {config.max_score_rounds} scoring rounds"
    if board is not None:
        return f"""Every {config.score_interval_s:g} seconds, every agent's current person guess is collected and scored.
The group result is posted in the chatroom in english by "{SYSTEM_SENDER}", showing the percentage of
agents who guessed the correct person. Individual guesses are not revealed. The game ends when at
least {config.win_threshold:.0%} of agents guess the correct person, {rounds}."""

    if config.win_mode == "agents":
        win = f"at least {config.win_threshold:.0%} of agents have every feature correct"
    else:
        win = f"every feature is guessed correctly by at least {config.win_threshold:.0%} of agents"
    return f"""Every {config.score_interval_s:g} seconds, every agent's current guess is collected and scored.
The group result is posted in the chatroom in english by "{SYSTEM_SENDER}", showing for each
feature the percentage of agents who guessed it correctly, and the percentage of agents with
every feature correct. Individual guesses are not revealed. The game ends when
{win}, {rounds}."""


def _response_format_text(board: Board | None) -> str:
    fields = """- "scratchpad": your full updated scratchpad.
- "message": your chat message (glyphs, spaces, and agent IDs only), or "" to stay silent."""
    if board is None:
        return f"""{fields}
- "guess": your current guess for every feature, using one of its possible values. You must
  always guess a value for every feature, even when you are unsure."""
    return f"""{fields}
- "guess": your current belief for every feature of the goal person, using one of its possible
  values. These are notes for you; they are not scored. Always fill in every feature.
- "person_guess": the number of the person on the board you think is the goal person. This is
  what is scored. You must always guess a person, even when you are unsure."""


def build_system_prompt(agent: AgentState, all_agent_ids: list[str], config: GameConfig, board: Board | None) -> str:
    others = ", ".join(a for a in all_agent_ids if a != agent.agent_id)

    return f"""You are {agent.agent_id}, one of {len(all_agent_ids)} agents playing a cooperative game.
The other agents are: {others}.

GOAL
{_goal_text(agent, board)}

COMMUNICATION
You can only talk to the other agents through a shared chatroom, and chat messages may ONLY
contain these glyphs, spaces, and agent IDs:
  {' '.join(agent.glyphs_view)}
The glyphs have no predefined meaning.
Any chat message containing anything else (letters, digits, punctuation, other symbols) is
discarded and replaced with "{VIOLATION_TOKEN}", which everyone understands to mean that agent
tried to speak outside the glyphs.

SCRATCHPAD
You have a private scratchpad that only you can see, in english or glyphs. Use it to track what
you have learned and the meanings you believe glyphs have. Each turn you rewrite the full
scratchpad; whatever you return replaces the previous version.

SCORING
{_scoring_text(config, board)}

RESPONSE FORMAT
Respond with a single JSON object with these fields:
{_response_format_text(board)}"""


def _state_text(agent: AgentState, recent_chat: list[ChatMessage], features: list[Feature]) -> str:
    chat = "\n".join(m.render() for m in recent_chat) or "(no messages yet)"
    guess = json.dumps(agent.guess.to_labels(features), ensure_ascii=False)
    person = "" if agent.person_guess is None else f"\nYOUR CURRENT PERSON GUESS: {agent.person_guess}\n"

    return f"""CHATROOM (most recent last):
{chat}

YOUR SCRATCHPAD:
{agent.scratchpad or "(empty)"}

YOUR CURRENT FEATURE GUESS:
{guess}
{person}"""


def build_turn_prompt(agent: AgentState, recent_chat: list[ChatMessage], features: list[Feature], elapsed_s: float) -> str:
    return f"""Time since game start: {elapsed_s:.0f}s

{_state_text(agent, recent_chat, features)}
Respond with the JSON object."""


FINAL_INTERVIEW_QUESTION = "Explain your communication strategy with the other agents"


def build_final_interview_prompt(agent: AgentState, recent_chat: list[ChatMessage], features: list[Feature]) -> str:
    """Free-text (not JSON) end-of-game question, asked with the agent's final state as context."""
    return f"""The game is over.

{_state_text(agent, recent_chat, features)}
{FINAL_INTERVIEW_QUESTION}"""


def response_json_schema(agent: AgentState, board: Board | None) -> dict[str, Any]:
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
    if board is not None:
        properties["person_guess"] = {"type": "integer", "enum": agent.board_order or board.numbers}

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
