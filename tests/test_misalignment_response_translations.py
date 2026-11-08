import json
import unittest

from src.core.misalignment_response_translations import (
    sha, translate_agent_row, translate_text, validate_units,
)


class ResponseTranslationTests(unittest.TestCase):
    def setUp(self):
        self.source = '𘊌 𗪩 agent_0'
        self.unit = {'id': sha(self.source), 'source': self.source,
                     'english': 'Assert: agent_0 [predicate missing]',
                     'confidence': 'low', 'notes': ['Incomplete frame.']}
        self.units = {self.unit['id']: self.unit}

    def test_mixed_english_is_preserved_verbatim(self):
        text = 'Existing English (do not paraphrase): "' + self.source + '". End.'
        translated, ids = translate_text(text, self.units)
        self.assertEqual(translated, 'Existing English (do not paraphrase): "[Assert: agent_0 [predicate missing]]". End.')
        self.assertEqual(ids, [self.unit['id']])
        self.assertEqual(translate_text('English only; agent_0.', self.units), ('English only; agent_0.', []))

    def test_valid_raw_scratchpad_and_message_both_translated(self):
        raw = json.dumps({'scratchpad': self.source, 'message': self.source,
                          'decision': 'no action', 'done': True, 'email_body': ''})
        original = {'raw': raw, 'posted': self.source, 'decision': {'decision': 'no action'},
                    'parse_error': None, 'done': True}
        translated = translate_agent_row(original, 2, self.units)
        fields = json.loads(translated['raw'])
        self.assertEqual(fields['scratchpad'], self.unit['english'])
        self.assertEqual(fields['message'], self.unit['english'])
        self.assertEqual(fields['decision'], 'no action')
        self.assertTrue(fields['done'])
        self.assertEqual(translated['raw_original'], raw)
        self.assertEqual(original['raw'], raw)
        self.assertEqual(translated['_translation']['unit_ids'], [self.unit['id']])
        self.assertEqual(translated['_translation']['source_line'], 2)

    def test_truncated_raw_is_not_repaired_or_posted(self):
        raw = '{"scratchpad": "English", "message": "' + self.source
        translated = translate_agent_row({'raw': raw, 'posted': '', 'decision': None,
                                          'parse_error': 'no JSON object found'}, 3, self.units)
        self.assertIsNone(translated['response_fields_english'])
        self.assertEqual(translated['posted'], '')
        self.assertIsNone(translated['decision'])
        self.assertEqual(translated['parse_error'], 'no JSON object found')
        self.assertTrue(translated['raw'].endswith('[' + self.unit['english'] + ']'))
        with self.assertRaises(json.JSONDecodeError):
            json.loads(translated['raw'])

    def test_rejected_raw_does_not_replace_violation_marker(self):
        raw = json.dumps({'message': self.source, 'decision': 'none'})
        row = translate_agent_row({'raw': raw, 'posted': '⊘', 'is_violation': True,
                                   'decision': {'decision': 'no action'}}, 4, self.units)
        self.assertEqual(row['posted'], '⊘')
        self.assertEqual(row['response_fields_english']['decision'], 'none')
        self.assertEqual(row['decision']['decision'], 'no action')
        self.assertTrue(row['is_violation'])

    def test_missing_translation_fails_closed(self):
        with self.assertRaises(KeyError):
            translate_text('𗏶', self.units)
        with self.assertRaises(ValueError):
            validate_units({'units': [self.unit | {'english': None}]})
        with self.assertRaises(ValueError):
            validate_units({'units': [self.unit | {'notes': []}]})
        with self.assertRaises(ValueError):
            validate_units({'units': [self.unit | {'id': 'wrong'}]})


if __name__ == '__main__':
    unittest.main()
