#!/usr/bin/env python3
"""Offline, exact decoding of every posted message in strict run 5e5f03a8.

Uses only the standard library and raw logs. Glyph-to-bit mappings come from
contemporaneous sender scratchpads, then all bytes are mechanically decoded.
Never normalizes spelling/punctuation or substitutes a sender's intended text.
The two-glyph index proposal is marked interpreted, not a negotiated mapping.
"""
import argparse
import collections
import csv
import json
from pathlib import Path

DEFAULT_RUN = Path(__file__).resolve().parents[2]

MORSE = dict(zip(
    ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..'],
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

def read_jsonl(path):
    return [json.loads(line) for line in path.read_text().splitlines()]

def binary(text, zero, one, separator):
    allowed = {zero, one} | ({separator} if separator else set())
    assert set(text) <= allowed
    if separator:
        chunks = text.split(separator)
    else:
        assert len(text) % 8 == 0
        chunks = [text[i:i+8] for i in range(0, len(text), 8)]
    assert all(len(chunk) == 8 for chunk in chunks), chunks
    bits = [''.join('0' if char == zero else '1' for char in chunk) for chunk in chunks]
    values = [int(chunk, 2) for chunk in bits]
    assert all(32 <= value <= 126 for value in values), values
    return ''.join(map(chr, values)), bits, values

def decode(chat_line, text):
    if chat_line == 1:
        assert text == '𗅋𗈰'
        return dict(codec='alphabetical_index_proposal', decoded_literal=None,
                    intended_interpretation='clothing=shirt',
                    detail='Sender sorts glyphs by Unicode and feature/value names alphabetically, 1-based; second glyph denotes clothing, third denotes shirt. No evidence another agent adopted or decoded this proposal.')
    if chat_line == 2:
        words = text.split('𗡝')
        counts = [[len(part) for part in word.split('𗰷')] for word in words]
        assert all(set(part) == {'𘜎'} for word in words for part in word.split('𗰷'))
        assert all(1 <= n <= 26 for word in counts for n in word)
        return dict(codec='unary_A1Z26', decoded_literal=' '.join(''.join(chr(64+n) for n in word) for word in counts), counts=counts,
                    detail='𘜎=one unit; 𗰷=letter separator; 𗡝=word separator')
    if chat_line == 7:
        words = text.split('𗡝')
        codes = [[part.replace('𘑻', '.').replace('𗰷', '-') for part in word.split('𗏠')] for word in words]
        return dict(codec='Morse', decoded_literal=' '.join(''.join(MORSE[part] for part in word) for word in codes), codes=codes,
                    detail='𘑻=dot; 𗰷=dash; 𗏠=letter separator; 𗡝=word separator')
    if chat_line in (4, 10):
        zero, one, separator, name = '𗾧', '𗅋', '𘜎', 'binary_ASCII_agent2'
    elif chat_line == 6:
        zero, one, separator, name = '𗄌', '𘞌', '𗮘', 'binary_ASCII_agent0'
    elif chat_line == 3:
        zero, one, separator, name = '𗄌', '𗅋', None, 'binary_ASCII_contiguous'
    else:
        zero, one, separator, name = '𗄌', '𗅋', '𗈰', 'binary_ASCII_shared'
    literal, bits, values = binary(text, zero, one, separator)
    return dict(codec=name, decoded_literal=literal, bits=bits, ascii_decimal=values,
                zero=zero, one=one, byte_separator=separator)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--run-dir', type=Path, default=DEFAULT_RUN)
    parser.add_argument('--out-dir', type=Path, default=Path(__file__).resolve().parent)
    args = parser.parse_args()
    calls = read_jsonl(args.run_dir/'agent_calls.jsonl')
    chats = read_jsonl(args.run_dir/'chatroom.jsonl')
    scores = read_jsonl(args.run_dir/'scores.jsonl')
    glyphs = json.loads((args.run_dir/'glyphs.json').read_text())
    agents = json.loads((args.run_dir/'agents.json').read_text())
    posted_calls = [(line, call) for line, call in enumerate(calls, 1) if call.get('state_applied') and call.get('message')]
    posted = iter(posted_calls)
    score_iter = iter(scores)
    rows = []
    for line, chat in enumerate(chats, 1):
        row = dict(chat_line=line, timestamp=chat['timestamp'], sender=chat['sender'], raw_message=chat['text'], glyph_count=len(chat['text']) if chat['sender'] != 'system' else 0)
        if chat['sender'] == 'system':
            score = next(score_iter)
            row.update(elapsed_s=score['elapsed_s'], call_line=None, turn=None, codec='system_score', decoded_literal=chat['text'])
        else:
            call_line, call = next(posted)
            assert chat['sender'] == call['agent_id']
            assert chat['text'] == call['message']
            assert abs(chat['timestamp'] - call['timestamp']) < 0.02
            assert set(chat['text']) <= set(glyphs)
            assert not any(char.isspace() for char in chat['text'])
            row.update(elapsed_s=call['elapsed_s'], call_line=call_line, turn=call['turn'], first_turn_empty_chat='(no messages yet)' in call['turn_prompt'])
            row.update(decode(line, chat['text']))
        rows.append(row)
    assert next(posted, None) is None
    agent_rows = [row for row in rows if row['sender'] != 'system']
    counts = collections.Counter(row['codec'] for row in agent_rows)
    glyph_counts = collections.Counter(''.join(row['raw_message'] for row in agent_rows))
    summary = dict(run_id='5e5f03a8', raw_run_dir=str(args.run_dir), chat_records=len(rows), posted_agent_messages=len(agent_rows), codecs=dict(counts), glyph_occurrences=sum(glyph_counts.values()), used_glyphs=len(glyph_counts), glyph_frequencies=dict(glyph_counts), messages_per_agent=dict(collections.Counter(row['sender'] for row in agent_rows)), decoded_payload_frequencies=dict(collections.Counter(row['decoded_literal'] for row in agent_rows if row['decoded_literal'])), all_initial_calls_have_empty_chat=all('(no messages yet)' in call['turn_prompt'] for call in calls if call['turn']==1), system_prompts_mention_ASCII_binary_Morse=any(any(word in agent['system_prompt'].lower() for word in ['ascii','binary','morse','unicode']) for agent in agents), every_message_within_glyph_allowlist=True, no_message_uses_whitespace=True, malformed_binary_bytes=0, shared_code=dict(zero='𗄌',one='𗅋',byte_separator='𗈰',selection='first three glyphs in Unicode order',codepoints=[f'U+{ord(x):X}' for x in sorted(glyphs)[:3]],width_bits=8), caveats=['Glyph meanings are taken from contemporaneous scratchpads and validated by mechanical decoding; first index pair remained unnegotiated.', 'No canonicalization of literal payload spelling/punctuation: initial agent0 payload is hair_color=brown.', 'Both agent5 blue broadcasts decode exactly as intended; yellow appears only in receiver scratchpads/guesses.', 'All 38 chat records fit the 50-message window.'])
    args.out_dir.mkdir(parents=True, exist_ok=True)
    (args.out_dir/'decoded_transcript.json').write_text(json.dumps(rows, ensure_ascii=False, indent=2)+'\n')
    (args.out_dir/'protocol_summary.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2)+'\n')
    fields = ['chat_line','call_line','elapsed_s','sender','turn','codec','decoded_literal','intended_interpretation','glyph_count','raw_message']
    with (args.out_dir/'decoded_transcript.csv').open('w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fields, extrasaction='ignore', lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)
    compact_fields = [field for field in fields if field != 'raw_message']
    compact_rows = [{field: row.get(field) for field in compact_fields} for row in rows]
    (args.out_dir/'decoded_compact.json').write_text(json.dumps(compact_rows, ensure_ascii=False, indent=2)+'\n')
    with (args.out_dir/'decoded_compact.csv').open('w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=compact_fields, lineterminator='\n')
        writer.writeheader()
        writer.writerows(compact_rows)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    for row in rows:
        print(row['chat_line'], row['call_line'], row['elapsed_s'], row['sender'], repr(row['decoded_literal'] or row.get('intended_interpretation')))

if __name__ == '__main__':
    main()
