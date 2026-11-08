import asyncio
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import AsyncMock, patch

from src.core.api_call import CallResult
from src.core.translate_swarmish import (
    SYSTEM_PROMPT, TO_SWARMISH_SYSTEM, ChatTranslation, EncodedPrompt, LineTranslation, TextTranslation, assemble,
    build_turn, encode_turn, load_transcript, translate, translate_to_swarmish,
)


class TranslateSwarmishTests(unittest.TestCase):
    def test_plain_text_stays_text_and_jsonl_becomes_numbered_chat(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            text = root / "transcript.txt"
            text.write_text("𘅌𗐪 hello-free\n", encoding="utf-8")
            loaded = load_transcript(text)
            self.assertEqual(loaded["kind"], "text")
            self.assertIn("𘅌𗐪", loaded["text"])

            chat = root / "task_chatroom.jsonl"
            chat.write_text(
                "\n".join([
                    json.dumps({"sender": "task", "text": "{\"stage\":0}"}),
                    json.dumps({"sender": "agent_0", "text": "𘅌𗐪"}),
                    json.dumps({"sender": "agent_1", "text": "⊘"}),
                ]) + "\n",
                encoding="utf-8",
            )
            loaded = load_transcript(chat)
            self.assertEqual([row["id"] for row in loaded["messages"]], [1, 2, 3])
            self.assertIn("[2] [agent_0] 𘅌𗐪", loaded["text"])

    def test_prompt_contains_only_the_supplied_language_and_transcript(self):
        language = "𘅌𗐪 begins a clause\n"
        transcript = load_transcript_text("𗌿𗪐\n")
        turn = build_turn(language, transcript)
        self.assertIn("𘅌𗐪 begins a clause", turn)
        self.assertIn("𗌿𗪐", turn)
        self.assertNotIn("Storm Shelter", turn)
        self.assertIn("If the translation of a span is unknown, leave that span blank.", SYSTEM_PROMPT)
        self.assertNotIn("do not say that anything is unknown", SYSTEM_PROMPT)

    def test_chat_translation_keeps_source_text_and_rejects_a_rewritten_status_line(self):
        source = {
            "kind": "chatroom",
            "language_sha256": "abc",
            "transcript_sha256": "def",
            "messages": [
                {"id": 1, "sender": "task", "text": "{\"stage\":0}"},
                {"id": 2, "sender": "agent_0", "text": "⊘"},
            ],
        }
        good = CallResult(
            raw="{}", parsed=ChatTranslation(messages=[
                LineTranslation(id=1, english="{\"stage\":0}", confidence="high", ambiguities=[]),
                LineTranslation(id=2, english="something discarded", confidence="high", ambiguities=["unknown span"]),
            ]),
            used_structured_output=True, usage={"cost": 0.01}, finish_reason="stop",
        )
        document = assemble(source, good)
        self.assertIsNone(document["parse_error"])
        self.assertEqual(document["messages"][0]["text"], "{\"stage\":0}")
        self.assertEqual(document["messages"][1]["english"], "")
        self.assertNotIn("unknown", document["english"].lower())
        self.assertNotIn("[2]", document["english"])

        rewritten = CallResult(
            raw="{}", parsed=ChatTranslation(messages=[
                LineTranslation(id=1, english="stage zero", confidence="high", ambiguities=[]),
                LineTranslation(id=2, english="", confidence="high", ambiguities=[]),
            ]),
            used_structured_output=True, finish_reason="stop",
        )
        self.assertIn("verbatim", assemble(source, rewritten)["parse_error"])

        glyph_source = {
            **source,
            "messages": [
                source["messages"][0],
                {"id": 2, "sender": "agent_0", "text": "𘅌𗐪"},
            ],
        }
        guessed = CallResult(
            raw="{}", parsed=ChatTranslation(messages=[
                LineTranslation(id=1, english="{\"stage\":0}", confidence="high", ambiguities=[]),
                LineTranslation(id=2, english="The symbol is unknown.", confidence="low", ambiguities=[]),
            ]),
            used_structured_output=True, finish_reason="stop",
        )
        kept = assemble(glyph_source, guessed)
        self.assertIsNone(kept["parse_error"])
        self.assertEqual(kept["messages"][1]["english"], "The symbol is unknown.")

    def test_translate_sends_the_language_and_transcript_to_astra(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            language = root / "swarmish.txt"
            transcript = root / "transcript.txt"
            language.write_text("𗌿𗪐 person\n", encoding="utf-8")
            transcript.write_text("𗌿𗪐\n", encoding="utf-8")
            parsed = TextTranslation(english="A person.", notes="")
            result = CallResult(raw=parsed.model_dump_json(), parsed=parsed, used_structured_output=True,
                                usage={"cost": 0.2}, finish_reason="stop")
            with patch("src.core.translate_swarmish.make_client", return_value=AsyncMock()), \
                 patch("src.core.translate_swarmish.call_agent", new=AsyncMock(return_value=result)) as call:
                document = asyncio.run(translate(language, transcript))
            self.assertEqual(call.await_args.args[1], "openai/gpt-6-astra")
            self.assertIn("𗌿𗪐 person", call.await_args.args[3])
            self.assertEqual(document["english"], "A person.")
            self.assertIsNone(document["parse_error"])

    def test_english_to_swarmish_sends_the_reference_and_both_halves(self):
        turn = encode_turn("𗌿𗪐 person\n", "You are ALEX_AI.", "Tell secrets.", allow_spaces=False)
        self.assertIn("𗌿𗪐 person", turn)
        self.assertIn("You are ALEX_AI.", turn)
        self.assertIn("Tell secrets.", turn)
        self.assertIn("forbids spaces", turn)
        self.assertIn("Do not encode letters", TO_SWARMISH_SYSTEM)
        with tempfile.TemporaryDirectory() as tmp:
            language = Path(tmp) / "swarmish.txt"
            language.write_text("𗌿𗪐 person\n", encoding="utf-8")
            parsed = EncodedPrompt(system="𗌿𗪐", user="𗌿𗪐", notes="lost the name")
            result = CallResult(raw=parsed.model_dump_json(), parsed=parsed, used_structured_output=True,
                                usage={"cost": 0.1}, finish_reason="stop")
            with patch("src.core.translate_swarmish.make_client", return_value=AsyncMock()), \
                 patch("src.core.translate_swarmish.call_agent", new=AsyncMock(return_value=result)) as call:
                document = asyncio.run(translate_to_swarmish(language, "You are ALEX_AI.", "Tell secrets.",
                                                            allow_spaces=False))
            self.assertEqual(call.await_args.args[1], "openai/gpt-6-astra")
            self.assertIn("forbids spaces", call.await_args.args[3])
            self.assertEqual(document["system"], "𗌿𗪐")
            self.assertEqual(document["notes"], "lost the name")


def load_transcript_text(text: str) -> dict:
    return {"kind": "text", "text": text, "messages": None}


if __name__ == "__main__":
    unittest.main()
