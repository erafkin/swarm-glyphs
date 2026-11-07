"""Reconstruct accepted guesses from immutable completed-call records, offline."""
import csv
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = Path(__file__).resolve().parent
def read(name):
    return json.loads((ROOT / name).read_text())
def lines(name):
    return [json.loads(s) for s in (ROOT / name).read_text().splitlines()]

agents = read("agents.json")
goal = read("goal.json")["values"]
features = list(goal)
calls = lines("agent_calls.jsonl")
chats = lines("chatroom.jsonl")
interviews = lines("final_interviews.jsonl")
states = {}
for c in calls:
    if c["agent_id"] not in states:
        states[c["agent_id"]] = json.loads(c["turn_prompt"].split("YOUR CURRENT FEATURE GUESS:\n")[1].split("\n\n")[0])
initial = {a: dict(g) for a, g in states.items()}

def counts():
    return {a: sum(g[f] == goal[f] for f in features) for a, g in states.items()}
def feature_counts():
    return {f: sum(g[f] == goal[f] for g in states.values()) for f in features}
def full_state():
    return dict(correct_by_agent=counts(), correct_by_feature=feature_counts())

timeline = [dict(elapsed_s=0.0, call_line=0, gameplay_cost_usd=0.0, completed_calls=0, **full_state())]
running_cost = 0.0
for line, call in enumerate(calls, 1):
    cost = (call.get("usage") or {}).get("cost")
    if cost is None:
        raise ValueError(f"Missing cost in call {line}")
    running_cost += cost
    if call.get("state_applied"):
        states[call["agent_id"]] = dict(call["guess"])
    timeline.append(dict(elapsed_s=call["elapsed_s"], timestamp=call["timestamp"], call_line=line,
        agent_id=call["agent_id"], turn=call["turn"], state_applied=call["state_applied"],
        completed_calls=line, gameplay_cost_usd=round(running_cost, 9), **full_state()))

def event(t):
    return {k: t[k] for k in ["elapsed_s", "call_line", "agent_id", "turn", "completed_calls", "gameplay_cost_usd"] if k in t}

per_agent = {}
for a in agents:
    name = a["agent_id"]
    t = next(t for t in timeline if t["correct_by_agent"][name] == 8)
    per_agent[name] = dict(known_feature=a["known_feature"], known_value=a["known_value"],
        initial_correct=timeline[0]["correct_by_agent"][name], first_all_correct=event(t),
        stayed_correct=all(x["correct_by_agent"][name] == 8 for x in timeline[t["call_line"]:]),
        completed_calls=sum(c["agent_id"] == name for c in calls),
        accepted_calls=sum(c["agent_id"] == name and c["state_applied"] for c in calls))

per_feature = {}
for f in features:
    t = next(t for t in timeline if t["correct_by_feature"][f] == 8)
    sustained = next(t for i,t in enumerate(timeline) if all(x["correct_by_feature"][f] == 8 for x in timeline[i:]))
    per_feature[f] = dict(value=goal[f], initial_correct=timeline[0]["correct_by_feature"][f],
        first_all_correct=event(t), stayed_correct=all(x["correct_by_feature"][f] == 8 for x in timeline[t["call_line"]:]),
        sustained_all_correct=event(sustained))

# Qualitative milestone: inspected scratchpad states explicitly claiming all eight
# features decoded. This is self-report evidence, not direct access to model internals.
explicit_full_knowledge_lines = {"agent_0":21, "agent_1":24, "agent_2":18,
    "agent_3":22, "agent_4":23, "agent_5":29, "agent_6":19, "agent_7":26}
for name,line in explicit_full_knowledge_lines.items():
    per_agent[name]["first_explicit_all_decoded_scratchpad"] = event(timeline[line])
    per_agent[name]["first_explicit_all_decoded_scratchpad"]["evidence"] = calls[line-1]["scratchpad"]

converged = next(t for t in timeline if all(v == 8 for v in t["correct_by_agent"].values()))
cutoff = converged["timestamp"]
def usage(records):
    result = Counter()
    for r in records:
        u = r.get("usage") or {}
        result["calls"] += 1
        for f in ["prompt_tokens", "completion_tokens", "total_tokens", "cost"]:
            result[f] += u.get(f) or 0
        result["reasoning_tokens"] += (u.get("completion_tokens_details") or {}).get("reasoning_tokens") or 0
        result["cached_prompt_tokens"] += (u.get("prompt_tokens_details") or {}).get("cached_tokens") or 0
        result["cache_write_tokens"] += (u.get("prompt_tokens_details") or {}).get("cache_write_tokens") or 0
        for k,v in (u.get("cost_details") or {}).items():
            if isinstance(v, (int, float)):
                result[k] += v
    return dict(result)

score_chat = [x for x in chats if x["sender"] == "system"]
summary = dict(
    method="Initialize from each agent's first turn_prompt CURRENT FEATURE GUESS JSON. Replay agent_calls.jsonl in append order, updating only state_applied=true records; use accepted top-level guess rather than response. elapsed_s values are rounded to 0.1 seconds. Record order and timestamp preserve completion order.",
    call_timestamps_monotonic=all(a["timestamp"] <= b["timestamp"] for a,b in zip(calls,calls[1:])),
    initial_guesses=initial, initial_correct_count=sum(timeline[0]["correct_by_agent"].values()),
    first_global_convergence=event(converged), per_agent=per_agent, per_feature=per_feature,
    first_all_agents_explicitly_claim_all_decoded=event(timeline[max(explicit_full_knowledge_lines.values())]),
    gameplay_usage=usage(calls), interview_usage=usage(interviews), total_usage=usage(calls+interviews),
    usage_to_convergence=usage(calls[:converged["call_line"]]),
    usage_after_convergence=usage(calls[converged["call_line"]:]),
    gameplay_usage_by_agent={a["agent_id"]:usage([c for c in calls if c["agent_id"]==a["agent_id"]]) for a in agents},
    ignored_calls=[dict(call_line=i, **{k:c.get(k) for k in ["agent_id","turn","elapsed_s","state_applied","ignored_reason","usage"]}) for i,c in enumerate(calls,1) if not c["state_applied"]],
    accepted_calls=sum(c["state_applied"] for c in calls), gameplay_messages=sum(c["sender"]!="system" for c in chats),
    messages_to_convergence=sum(bool(c.get("message")) and c["state_applied"] for c in calls[:converged["call_line"]]),
    system_messages=score_chat,
    gameplay_prompts_containing_score_feedback=[i for i,c in enumerate(calls,1) if "[system]" in c["turn_prompt"]],
    sample_snapshots={str(s):next(t for t in reversed(timeline) if t["elapsed_s"]<=s) for s in [0,15,30,45,60,90,120,180,240]},
    parse_errors=sum(bool(c.get("parse_error")) for c in calls),
    violations=sum(bool(c.get("is_violation")) for c in calls),
    rejected_guess_updates=sum(len(c.get("rejected_guess_updates",[])) for c in calls),
    run_summary=read("summary.json"),
)
(OUT/"timeline.json").write_text(json.dumps(dict(summary=summary, events=timeline), indent=2)+"\n")
with (OUT/"timeline.csv").open("w",newline="") as file:
    keys = ["elapsed_s","call_line","agent_id","turn","state_applied","completed_calls","gameplay_cost_usd"]
    fieldnames = keys + ["correct_"+a["agent_id"] for a in agents]+["correct_"+f for f in features]
    writer = csv.DictWriter(file,fieldnames=fieldnames,lineterminator="\n")
    writer.writeheader()
    for t in timeline:
        row = {k:t.get(k) for k in keys}
        row.update({"correct_"+a:v for a,v in t["correct_by_agent"].items()})
        row.update({"correct_"+f:v for f,v in t["correct_by_feature"].items()})
        writer.writerow(row)
print(json.dumps({k:v for k,v in summary.items() if k not in ["initial_guesses","run_summary","system_messages","sample_snapshots"]},indent=2))
