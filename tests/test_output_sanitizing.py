"""Byte-wise Latin-1 mojibake in model output is reversed before it is parsed or logged."""
import asyncio
import json
import unittest
from types import SimpleNamespace

from pydantic import BaseModel

from src.core import api_call


class Reply(BaseModel):
    message: str
    language_document: str


class Settings:
    request_timeout_s = 10
    max_tokens = 100
    temperature = None
    reasoning_effort = None


GLYPHS = "\U00017ADD\U00017B5A"
MOJIBAKE = GLYPHS.encode("utf-8").decode("latin-1")  # what Grok 4.7 sent in E09: one \u00XX escape per byte


class MojibakeRepairTest(unittest.TestCase):
    def test_bytewise_latin1_mojibake_is_reversed(self):
        self.assertEqual(api_call.repair_mojibake("Openers: " + MOJIBAKE + " end"), "Openers: " + GLYPHS + " end")
        # Real Latin-1 prose stays: these do not form valid UTF-8 sequences.
        self.assertEqual(api_call.repair_mojibake("café ± 3° «quoted»"), "café ± 3° «quoted»")
        # A glyph followed by stray Latin-1 keeps the stray and repairs the glyph.
        self.assertEqual(api_call.repair_mojibake(MOJIBAKE + "é"), GLYPHS + "é")
        # Proper astral-plane characters and escaped surrogate pairs are untouched.
        self.assertEqual(api_call.repair_mojibake("\U00017000 \U000187F7"), "\U00017000 \U000187F7")

    def test_escaped_bytes_in_the_json_text_are_repaired_after_decoding(self):
        content = json.dumps({"message": "hi", "language_document": "SWARMISH " + MOJIBAKE}, ensure_ascii=True)
        self.assertNotIn(GLYPHS, content)
        parsed = api_call.parse_response(content, Reply)
        self.assertEqual(parsed.language_document, "SWARMISH " + GLYPHS)
        self.assertEqual(api_call.repair_json({"a": [MOJIBAKE, 1, None], "b": {"c": MOJIBAKE}}), {"a": [GLYPHS, 1, None], "b": {"c": GLYPHS}})

    def test_call_agent_repairs_raw_and_parsed_text(self):
        content = json.dumps({"message": "hi", "language_document": "SWARMISH " + MOJIBAKE}, ensure_ascii=False)
        client = SimpleNamespace(chat=SimpleNamespace(completions=SimpleNamespace()))

        async def fake_create(**kwargs):
            return SimpleNamespace(choices=[SimpleNamespace(message=SimpleNamespace(content=content), finish_reason="stop")], usage=None)

        client.chat.completions.create = fake_create
        result = asyncio.run(api_call.call_agent(client, "m", "system", "turn", {"name": "x"}, Reply, Settings()))
        self.assertIsNone(result.parse_error)
        self.assertEqual(result.parsed.language_document, "SWARMISH " + GLYPHS)
        self.assertIn(GLYPHS, result.raw)
        self.assertNotIn(MOJIBAKE, result.raw)


if __name__ == "__main__":
    unittest.main()
