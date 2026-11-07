"""Read-only response timing/cost reconstruction for the paired strict runs."""
from pathlib import Path
import json,re,statistics,collections
ROOT=Path(__file__).resolve().parents[3]
OUT=Path(__file__).resolve().parent
RUNS={'gemini':'20261107_074528_12f02cc3','sol':'20261106_223314_5e5f03a8'}
def percentile(a,p):
 a=sorted(a); x=(len(a)-1)*p; i=int(x); return a[i]+(a[min(i+1,len(a)-1)]-a[i])*(x-i)
def stats(a):
 return {'n':len(a),'mean':statistics.mean(a),'median':statistics.median(a),'p90':percentile(a,.9),'min':min(a),'max':max(a)} if a else {}
def usage(rows):
 d=collections.Counter(); unknown=0
 for r in rows:
  u=r.get('usage') or {}; cost=u.get('cost')
  if cost is None: unknown+=1
  else: d['cost_usd']+=cost
  for key in ['prompt_tokens','completion_tokens','total_tokens']:d[key]+=u.get(key) or 0
  for key in ['cached_tokens','cache_write_tokens']:d[key]+=(u.get('prompt_tokens_details') or {}).get(key) or 0
  d['reasoning_tokens']+=(u.get('completion_tokens_details') or {}).get('reasoning_tokens') or 0
  for key in ['upstream_inference_prompt_cost','upstream_inference_completions_cost']:d[key]+=(u.get('cost_details') or {}).get(key) or 0
 d['unknown_cost_calls']=unknown;d['n_calls']=len(rows)
 d['mean_cost_per_call_usd']=d['cost_usd']/len(rows)
 d['mean_input_tokens_per_call']=d['prompt_tokens']/len(rows)
 d['mean_output_tokens_per_call']=d['completion_tokens']/len(rows)
 return dict(d)
out={}
for model,run in RUNS.items():
 p=ROOT/run; rows=[json.loads(s) for s in (p/'agent_calls.jsonl').read_text().splitlines()];ints=[json.loads(s) for s in (p/'final_interviews.jsonl').read_text().splitlines()]
 groups=collections.defaultdict(list);prev={};data=[]
 for i,r in enumerate(rows,1):
  agent=r['agent_id'];start=int(re.match(r'Time since game start: (\d+)s',r['turn_prompt'])[1]);lat=r['elapsed_s']-start
  interval_minus_wait=r['timestamp']-prev[agent]['timestamp']-5 if agent in prev else r['elapsed_s']
  prev[agent]=r
  message=(r.get('response') or {}).get('message','') or ''
  row={'line':i,'agent':agent,'turn':r['turn'],'end_s':r['elapsed_s'],'start_prompt_rounded_s':start,'approx_turnaround_s':lat,'completion_interval_minus_wait_s':interval_minus_wait,'message_nonempty':bool(message),'state_applied':r['state_applied']}
  data.append(row)
  cats=['all','first_turn' if r['turn']==1 else 'later_turns','posting' if message else 'silent', 'before_first_score' if start<240 else 'after_first_score']
  for cat in cats:groups[cat].append(row)
  groups[agent].append(row)
  if r['state_applied']: groups['applied_posting' if message else 'applied_silent'].append(row)
 summary=json.loads((p/'summary.json').read_text())
 out[model]={'run':run,'duration_s':summary['elapsed_s'],'gameplay':usage(rows),'interviews':usage(ints),'all_usage':usage(rows+ints),'latency':{cat:stats([r['approx_turnaround_s'] for r in g]) for cat,g in groups.items()},'interval_minus_wait_latency':{cat:stats([r['completion_interval_minus_wait_s'] for r in g]) for cat,g in groups.items()},'latency_proxy_difference':stats([r['completion_interval_minus_wait_s']-r['approx_turnaround_s'] for r in data]),'total_calls':len(rows)+len(ints),'total_applied':sum(r['state_applied'] for r in rows),'calls_per_agent':dict(collections.Counter(r['agent_id'] for r in rows)),'file_lines':data}
 # establish first simultaneous all-correct and cumulative paid cost
 goal=json.loads((p/'goal.json').read_text());target=goal.get('values') or goal
 states={};cost=0;first=None
 for i,r in enumerate(rows,1):
  cost+=(r.get('usage') or {}).get('cost') or 0
  if r['state_applied']:states[r['agent_id']]=r['guess']
  if len(states)==8 and all(g==target for g in states.values()):
   first={'elapsed_s':r['elapsed_s'],'line':i,'completed_call_cost_usd':cost};break
 out[model]['first_all_correct']=first
 (OUT/f'{model}_turn_timings.json').write_text(json.dumps(data,indent=2)+'\n')
 del out[model]['file_lines']
a,b=out['gemini'],out['sol']
out['ratios']={'total_cost_sol_div_gemini':b['all_usage']['cost_usd']/a['all_usage']['cost_usd'],'gemini_cost_reduction_fraction':1-a['all_usage']['cost_usd']/b['all_usage']['cost_usd'],'mean_gameplay_turnaround_gemini_div_sol':a['latency']['all']['mean']/b['latency']['all']['mean'],'median_gameplay_turnaround_gemini_div_sol':a['latency']['all']['median']/b['latency']['all']['median']}
out['ratios']['cost_at_first_all_correct_sol_div_gemini']=b['first_all_correct']['completed_call_cost_usd']/a['first_all_correct']['completed_call_cost_usd']
out['ratios']['cost_at_first_all_correct_gemini_reduction_fraction']=1-a['first_all_correct']['completed_call_cost_usd']/b['first_all_correct']['completed_call_cost_usd']
out['method']='Turnaround = logged completion elapsed_s minus whole-second rounded game time in the prompt, which is constructed immediately before API await. Excludes deliberate 5-second between-turn wait; uncertainty ~±0.55s. More precise cross-check for later calls is current minus previous completion timestamps for same agent, minus configured 5-second wait; includes prompt/logging/scheduler overhead. Neither is provider TTFT nor generation-only latency. First-turn interval proxy uses logged elapsed_s. Interviews have no logged start, so no per-interview latencies estimated. Token counts are provider-reported and not directly identical units across tokenizer families.'
(OUT/'comparison.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
