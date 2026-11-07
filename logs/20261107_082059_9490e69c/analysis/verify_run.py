"""Read-only verification of an archived strict features run (standard library only).

Run from anywhere: python3 /path/to/archive/analysis/verify_run.py
It never imports gameplay, loads API credentials, or makes network requests.
"""
from decimal import Decimal
import hashlib
import json
from pathlib import Path

RUN = Path(__file__).resolve().parents[1]


def rows(name):
    return [json.loads(line) for line in (RUN / name).read_text().splitlines() if line.strip()]


def cost(row):
    value = (row.get('usage') or {}).get('cost')
    assert value is not None, 'Missing provider-reported cost'
    return Decimal(str(value))


for line in (RUN / 'SHA256SUMS').read_text().splitlines():
    expected, name = line.split('  ', 1)
    assert hashlib.sha256((RUN / name).read_bytes()).hexdigest() == expected, name

calls = rows('agent_calls.jsonl')
interviews = rows('final_interviews.jsonl')
chat = rows('chatroom.jsonl')
goal = json.loads((RUN / 'goal.json').read_text())['values']
config = json.loads((RUN / 'config.json').read_text())
summary = json.loads((RUN / 'summary.json').read_text())
states = {}
first = None
paid = Decimal(0)
for i, call in enumerate(calls, 1):
    paid += cost(call)
    if call.get('state_applied'):
        states[call['agent_id']] = call['guess']
    if first is None and len(states) == config['n_agents'] and all(g == goal for g in states.values()):
        first = {'elapsed_s': call['elapsed_s'], 'timestamp': call['timestamp'],
                 'api_calls': i, 'reported_cost_usd': str(paid)}
assert first is not None

posted_calls = [c for c in calls if c.get('state_applied') and c.get('message')]
posted_chat = [e for e in chat if e['sender'] != 'system']
assert [(c['agent_id'], c['message']) for c in posted_calls] == [(e['sender'], e['text']) for e in posted_chat]
assert not any(c.get('error') or c.get('parse_error') or c.get('is_violation') for c in calls)
# Posting happens just after response logging; include the convergence reply's own post.
post_count_at_cutoff = sum(bool(c.get('state_applied') and c.get('message')) for c in calls[:first['api_calls']])
before = posted_chat[:post_count_at_cutoff]
first.update(chat_messages=len(before), glyphs=sum(len(e['text']) for e in before))

transcript = RUN / 'analysis/transcript/transcript-verified.json'
if transcript.exists():
    recorded = json.loads(transcript.read_text())
    assert [(e['sender'], e['text'], e['timestamp']) for e in recorded['chat']] == [(e['sender'], e['text'], e['timestamp']) for e in chat]
    assert recorded['before_correct_posts'] == len(before)
    assert recorded['before_correct_glyphs'] == first['glyphs']
    assert recorded['total_posts'] == len(posted_chat)
    assert recorded['total_glyphs'] == sum(len(e['text']) for e in posted_chat)

# Every supplied ASCII decoding is checked against the original glyph bytes.
decoded = RUN / 'analysis/decoded-chat.json'
if decoded.exists():
    recorded = json.loads(decoded.read_text())
    assert len(recorded['chat']) == len(posted_chat)
    for entry, original in zip(recorded['chat'], posted_chat):
        assert (entry['agent_id'], entry['message']) == (original['sender'], original['text'])
        mapping = entry['decoding']
        if mapping is None:
            continue  # Initial unary proposal is explicitly interpretive.
        chunks = entry['message'].split(mapping['separator'])
        assert all(len(chunk) == 8 for chunk in chunks)
        plain = ''.join(chr(int(''.join('0' if g == mapping['zero'] else '1' if g == mapping['one'] else '?' for g in chunk), 2)) for chunk in chunks)
        assert plain == mapping['text']

followup = RUN / 'analysis/followup-glyph-choices'
followup_report = None
if followup.exists():
    manifest = json.loads((followup / 'manifest.json').read_text())
    for name, expected in manifest['source_sha256'].items():
        assert hashlib.sha256((RUN / name).read_bytes()).hexdigest() == expected
    response_rows = [json.loads(line) for line in (followup / 'responses.jsonl').read_text().splitlines() if line.strip()]
    followup_summary = json.loads((followup / 'summary.json').read_text())
    assert len(response_rows) == followup_summary['successful_calls'] == 8
    followup_cost = sum((cost(r) for r in response_rows), Decimal(0))
    assert followup_cost == Decimal(str(followup_summary['total_reported_cost_usd']))
    followup_report = {'api_calls': len(response_rows), 'reported_cost_usd': str(followup_cost)}

result = {
    'run': RUN.name,
    'raw_sha256_matches': 9,
    'first_all_correct': first,
    'victory_detected_s': summary['final_score']['elapsed_s'],
    'full_run': {'elapsed_s': summary['elapsed_s'], 'gameplay_calls': len(calls),
                 'interview_calls': len(interviews), 'api_calls': len(calls) + len(interviews),
                 'reported_cost_usd': str(sum((cost(r) for r in calls + interviews), Decimal(0))),
                 'chat_messages': len(posted_chat), 'glyphs': sum(len(e['text']) for e in posted_chat),
                 'applied_silent_calls': sum(bool(c.get('state_applied')) and not c.get('message') for c in calls),
                 'unapplied_calls': sum(not c.get('state_applied') for c in calls)},
    'followup_interviews_separate': followup_report,
    'errors_or_parse_failures_or_glyph_violations': 0,
    'method': 'Costs sum completed logged responses. Glyph counts are Unicode code points in agent message bodies, excluding sender labels/system feedback. Cutoff includes the reply that first makes all submitted guesses correct; this does not establish every agent had correctly decoded every clue.'
}
print(json.dumps(result, indent=2))
