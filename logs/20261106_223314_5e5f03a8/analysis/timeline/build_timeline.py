#!/usr/bin/env python3
"""Offline replay of run 5e5f03a8. Reads raw logs; writes derived JSON/CSV here."""
import csv
import json
import re
from collections import Counter
from copy import deepcopy
from pathlib import Path
from statistics import mean

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent

def read_jsonl(name):
    return [dict(json.loads(line), source_line=i) for i,line in enumerate((ROOT/name).read_text().splitlines(),1)]

calls = read_jsonl('agent_calls.jsonl')
interviews = read_jsonl('final_interviews.jsonl')
chat = read_jsonl('chatroom.jsonl')
scores = read_jsonl('scores.jsonl')
goal = json.loads((ROOT/'goal.json').read_text())['values']
agents = sorted({x['agent_id'] for x in calls})
features = list(goal)
initial = {}
for call in calls:
    if call['agent_id'] not in initial:
        initial[call['agent_id']] = json.JSONDecoder().raw_decode(call['turn_prompt'].split('YOUR CURRENT GUESS:\n',1)[1])[0]

def usage(rows):
    result = {'calls':len(rows),'cost_usd':0,'missing_cost_calls':0,'prompt_tokens':0,'completion_tokens':0,'total_tokens':0,'reasoning_tokens':0,'cached_prompt_tokens':0,'cache_write_tokens':0,'prompt_cost_usd':0,'completion_cost_usd':0}
    for row in rows:
        u=row.get('usage') or {}
        if u.get('cost') is None: result['missing_cost_calls']+=1
        else: result['cost_usd']+=u['cost']
        for key in ['prompt_tokens','completion_tokens','total_tokens']: result[key]+=u.get(key) or 0
        result['reasoning_tokens']+=(u.get('completion_tokens_details') or {}).get('reasoning_tokens') or 0
        for key,dest in [('cached_tokens','cached_prompt_tokens'),('cache_write_tokens','cache_write_tokens')]:
            result[dest]+=(u.get('prompt_tokens_details') or {}).get(key) or 0
        for key,dest in [('upstream_inference_prompt_cost','prompt_cost_usd'),('upstream_inference_completions_cost','completion_cost_usd')]:
            result[dest]+=(u.get('cost_details') or {}).get(key) or 0
    for k,v in result.items():
        if isinstance(v,float): result[k]=round(v,9)
    return result

state=deepcopy(initial)
changes=[]
events=[]
running_cost=0
def record(call=None):
    ca={a:sum(state[a][f]==goal[f] for f in features) for a in agents}
    cf={f:sum(state[a][f]==goal[f] for a in agents) for f in features}
    x={'elapsed_s':0 if call is None else call['elapsed_s'],'source_line':0 if call is None else call['source_line'],'agent_id':None if call is None else call['agent_id'],'turn':0 if call is None else call['turn'],'state_applied':True if call is None else call['state_applied'],'correct_by_agent':ca,'correct_by_feature':cf,'correct_cells':sum(ca.values()),'fully_correct_agents':sum(v==len(features) for v in ca.values()),'cumulative_gameplay_cost_usd':round(running_cost,9)}
    if call:
        x['input_elapsed_s']=int(re.search(r'Time since game start: (\d+)s',call['turn_prompt']).group(1))
        x['score_feedback_in_input']=any(line.startswith('[system] Score round') for line in call['turn_prompt'].splitlines())
        x['posted_message']=bool(call.get('message')) and call['state_applied']
    events.append(x)

record()
state_after_line={0:deepcopy(state)}
for call in calls:
    running_cost+=(call.get('usage') or {}).get('cost') or 0
    if call['state_applied']:
        previous=state[call['agent_id']]
        nxt=call['guess']
        for f in features:
            if previous[f]!=nxt[f]:
                changes.append({'elapsed_s':call['elapsed_s'],'source_line':call['source_line'],'agent_id':call['agent_id'],'turn':call['turn'],'feature':f,'before':previous[f],'after':nxt[f],'before_correct':previous[f]==goal[f],'after_correct':nxt[f]==goal[f]})
        state[call['agent_id']]=deepcopy(nxt)
    record(call)
    state_after_line[call['source_line']]=deepcopy(state)

def first_and_sustained(test):
    matching=[i for i,e in enumerate(events) if test(e)]
    first=events[matching[0]] if matching else None
    last_false=max([i for i,e in enumerate(events) if not test(e)],default=-1)
    sustained=events[last_false+1] if last_false+1<len(events) else None
    keep=['elapsed_s','source_line','agent_id','turn','cumulative_gameplay_cost_usd','correct_cells','fully_correct_agents']
    return {key:None if value is None else {k:value[k] for k in keep} for key,value in [('first',first),('sustained',sustained)]}

global_conv=first_and_sustained(lambda e:e['fully_correct_agents']==len(agents))
seven=first_and_sustained(lambda e:e['fully_correct_agents']>=7)
conv_line=global_conv['first']['source_line']
conv_time=global_conv['first']['elapsed_s']
score_checks=[]
for score in scores:
    prior=[e for e in events if e['elapsed_s']<=score['elapsed_s']][-1]
    snapshot=state_after_line[prior['source_line']]
    score_checks.append({'round':score['round'],'elapsed_s':score['elapsed_s'],'last_completed_call_line':prior['source_line'],'guesses_match_replay':snapshot==score['guesses'],'accuracy_matches_replay':all(score['feature_accuracy'][f]==prior['correct_by_feature'][f]/len(agents) for f in features),'fully_correct_rate_matches':score['fully_correct_rate']==prior['fully_correct_agents']/len(agents)})

post_calls=[x for x in calls if x['state_applied'] and x.get('message')]
last_post=post_calls[-1]
last_change_line=changes[-1]['source_line']
first_score_inputs={}
for call in calls:
    lines=[z for z in call['turn_prompt'].splitlines() if z.startswith('[system] Score round')]
    if lines and call['agent_id'] not in first_score_inputs:
        first_score_inputs[call['agent_id']]={'source_line':call['source_line'],'elapsed_s':call['elapsed_s'],'turn':call['turn'],'input_elapsed_s':events[call['source_line']]['input_elapsed_s'],'score_lines':lines}
first_score_chat_inputs=[calls[x['source_line']-1]['turn_prompt'].split('CHATROOM (most recent last):\n',1)[1].split('\nYOUR SCRATCHPAD:',1)[0] for x in first_score_inputs.values()]
claimed_full_correct_lines={'agent_0':26,'agent_1':16,'agent_2':17,'agent_3':31,'agent_4':19,'agent_5':18,'agent_6':234,'agent_7':22}

summary={
    'method':'Replay full applied guess snapshots in JSONL completion order, starting from first-turn YOUR CURRENT GUESS for each agent. Ignore four state_applied:false late responses. Rounded elapsed timestamps; source lines are authoritative ordering. Cost is recorded completed-response cost, not counterfactual savings.',
    'initial_guesses':initial,
    'initial_correct_cells':events[0]['correct_cells'],
    'call_timestamps_monotonic':all(a['timestamp']<=b['timestamp'] for a,b in zip(calls,calls[1:])),
    'global_convergence':global_conv,
    'seven_agents_correct':seven,
    'per_agent_convergence':{a:first_and_sustained(lambda e,a=a:e['correct_by_agent'][a]==len(features)) for a in agents},
    'per_feature_convergence':{f:first_and_sustained(lambda e,f=f:e['correct_by_feature'][f]==len(agents)) for f in features},
    'regressions':[c for c in changes if c['before_correct'] and not c['after_correct']],
    'guess_change_count':len(changes),
    'last_guess_change':changes[-1],
    'score_checks':score_checks,
    'first_score_in_inputs':first_score_inputs,
    'first_score_aware_chat_inputs_identical':len(set(first_score_chat_inputs))==1,
    'first_score_aware_agent_message_count':sum(line.startswith('[agent_') for line in first_score_chat_inputs[0].splitlines()),
    'first_explicit_full_correct_decoding_claim':{a:{'source_line':line,'elapsed_s':calls[line-1]['elapsed_s'],'turn':calls[line-1]['turn'],'scratchpad':calls[line-1]['scratchpad']} for a,line in claimed_full_correct_lines.items()},
    'claim_caveat':'Explicit full-decoding milestones are manually identified model-written scratchpad claims, corroborated with correct guesses; these are not access to hidden reasoning. Agent3 happened to guess shirt correctly before decoding it. Agent6 falsely claimed all decoded from48.8s while yellow was wrong.',
    'gameplay_usage':usage(calls),
    'interview_usage':usage(interviews),
    'total_usage':usage(calls+interviews),
    'usage_to_seven_agents_correct':usage(calls[:seven['first']['source_line']]),
    'usage_to_first_score':usage([c for c in calls if c['elapsed_s']<=240]),
    'usage_to_convergence':usage(calls[:conv_line]),
    'usage_after_convergence':usage(calls[conv_line:]),
    'usage_after_last_post':usage(calls[last_post['source_line']:]),
    'usage_by_agent':{a:usage([c for c in calls if c['agent_id']==a]) for a in agents},
    'applied_calls':sum(c['state_applied'] for c in calls),
    'silences':sum(c['state_applied'] and not c.get('message') for c in calls),
    'posted_messages':len(post_calls),
    'posted_messages_before_first_score':sum(c['elapsed_s']<240 for c in post_calls),
    'last_post_before_first_score':{k:[c for c in post_calls if c['elapsed_s']<240][-1][k] for k in ['agent_id','turn','elapsed_s','source_line']},
    'posted_messages_by_agent':dict(Counter(c['agent_id'] for c in post_calls)),
    'last_posted_message':{k:last_post[k] for k in ['agent_id','turn','elapsed_s','source_line','message']},
    'system_messages':[{k:x[k] for k in ['source_line','timestamp','text']} for x in chat if x['sender']=='system'],
    'chat_matches_posts':len(chat)==len(post_calls)+sum(x['sender']=='system' for x in chat),
    'parse_errors':sum(bool(c.get('parse_error')) for c in calls),
    'violations':sum(bool(c.get('is_violation')) for c in calls),
    'rejected_guess_updates':sum(len(c.get('rejected_guess_updates',[])) for c in calls),
    'all_calls_used_structured_output':all(c['used_structured_output'] for c in calls),
    'agent6_evidence':{
        'first_misdecode':{'source_line':14,'elapsed_s':36.8,'turn':2},
        'false_full_decoding_claim':{'source_line':20,'elapsed_s':48.8,'turn':3},
        'last_wrong_response':{'source_line':226,'elapsed_s':242.5,'turn':30,'input_elapsed_s':240,'score_feedback_present':False},
        'repair':{'source_line':234,'elapsed_s':257.0,'turn':31,'input_elapsed_s':247,'score_feedback_present':True,'new_postscore_peer_messages_seen':0},
        'inference':'First score identified clothing_colour as only imperfect feature. Agent6 explicitly re-decoded original agent5 binary into blue in first score-aware call. Seven peers independently rebroadcast blue, but those replies had not appeared in this call input. Whole conversation fit within50messagewindow, so original clue was never truncated.'
    },
    'ignored_calls':[{k:c[k] for k in ['agent_id','turn','elapsed_s','source_line','ignored_reason']} for c in calls if not c['state_applied']],
    'gameplay_token_stats':{k:{'mean':mean(c['usage'][k] for c in calls),'min':min(c['usage'][k] for c in calls),'max':max(c['usage'][k] for c in calls)} for k in ['prompt_tokens','completion_tokens']},
    'snapshots':{str(t):[e for e in events if e['elapsed_s']<=t][-1] for t in [0,20,30,40,50,60,90,120,240,257,300,480]},
    'raw_folder_bytes':sum(f.stat().st_size for f in ROOT.iterdir() if f.is_file() and f.suffix in {'.json', '.jsonl'}),
}
OUT.mkdir(parents=True,exist_ok=True)
(OUT/'timeline.json').write_text(json.dumps({'summary':summary,'events':events,'guess_changes':changes},ensure_ascii=False,indent=2)+'\n')
with (OUT/'timeline.csv').open('w',newline='') as f:
    fields=['elapsed_s','source_line','agent_id','turn','state_applied','input_elapsed_s','score_feedback_in_input','posted_message','correct_cells','fully_correct_agents','cumulative_gameplay_cost_usd']+[a+'_correct' for a in agents]+[f+'_correct_agents' for f in features]
    w=csv.DictWriter(f,fieldnames=fields,lineterminator='\n');w.writeheader()
    for e in events:
        row={k:e.get(k) for k in fields}
        row.update({a+'_correct':e['correct_by_agent'][a] for a in agents});row.update({f+'_correct_agents':e['correct_by_feature'][f] for f in features});w.writerow(row)
with (OUT/'guess_changes.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(changes[0]),lineterminator='\n');w.writeheader();w.writerows(changes)
(OUT/'summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(summary,ensure_ascii=False,indent=2))
