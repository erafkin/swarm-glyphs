"""Verify the three archived randomized-ownership runs using only the standard library.

Run from any directory: python3 /path/to/repo/results/randomized_features_seed0/verify_results.py
The default is read-only and compares recomputed results with metrics.json. Pass
--write-metrics to explicitly regenerate that derived file. No gameplay modules,
credentials, provider APIs, or absolute paths from archived configs are accessed.
"""

import argparse
from collections import Counter
from decimal import Decimal
import hashlib
import json
from pathlib import Path


REPO = Path(__file__).resolve().parents[2]
METRICS = Path(__file__).with_name("metrics.json")
RUNS = (
    ("gemini", "logs/20261107_085050_d116b353"),
    ("sol", "logs/20261107_102027_75544e8a"),
    ("mixed", "logs/20261107_103151_5e02de73"),
)
RAW_FILES = (
    "agent_calls.jsonl", "agents.json", "chatroom.jsonl", "config.json",
    "final_interviews.jsonl", "glyphs.json", "goal.json", "scores.jsonl", "summary.json",
)


def check(condition, message):
    if not condition:
        raise ValueError(message)


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def rows(path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def reported_cost(row):
    value = (row.get("usage") or {}).get("cost")
    check(value is not None, "A response has no provider-reported cost")
    return Decimal(str(value))


def inventory(run):
    result = []
    for name in RAW_FILES:
        payload = (run / name).read_bytes()
        result.append({"file": name, "bytes": len(payload), "sha256": hashlib.sha256(payload).hexdigest()})
    actual = {"files": result, "total_bytes": sum(item["bytes"] for item in result)}
    check(actual == read_json(run / "analysis/raw-inventory.json"), f"Inventory mismatch: {run.name}")
    hashes = {}
    for line in (run / "SHA256SUMS").read_text(encoding="utf-8").splitlines():
        expected, name = line.split("  ", 1)
        check(name not in hashes, f"Duplicate hash entry: {name}")
        hashes[name] = expected
    check(hashes == {item["file"]: item["sha256"] for item in result}, f"SHA256SUMS mismatch: {run.name}")
    # These runs had no logged API errors; any newly added error stream needs review.
    check(not (run / "errors.jsonl").exists(), f"Unexpected unhashed error stream: {run.name}")
    return actual


def initial_guesses(calls, agent_ids, goal):
    """Recover exact initial states from each agent's first recorded request."""
    initial = {}
    for call in calls:
        agent = call["agent_id"]
        if agent in initial:
            continue
        check(call["turn"] == 1, f"Missing first turn for {agent}")
        prompt = call["turn_prompt"]
        marker = "YOUR CURRENT GUESS:\n"
        check(marker in prompt, f"Missing initial guess in {agent}'s first request")
        guess, _ = json.JSONDecoder().raw_decode(prompt.split(marker, 1)[1].lstrip())
        check(set(guess) == set(goal), f"Initial feature set differs for {agent}")
        initial[agent] = guess
    check(set(initial) == set(agent_ids), "An agent has no recorded initial request")
    return initial


def score_key(score):
    return score["feature_accuracy"], score["fully_correct_rate"]


def verify_run(label, relative_path):
    run = REPO / relative_path
    raw = inventory(run)
    config = read_json(run / "config.json")
    goal_record = read_json(run / "goal.json")
    goal = goal_record["values"]
    agents = read_json(run / "agents.json")
    glyphs = read_json(run / "glyphs.json")
    summary = read_json(run / "summary.json")
    calls = rows(run / "agent_calls.jsonl")
    interviews = rows(run / "final_interviews.jsonl")
    chat = rows(run / "chatroom.jsonl")
    scores = rows(run / "scores.jsonl")
    ids = [agent["agent_id"] for agent in agents]
    check(len(ids) == len(set(ids)) == config["n_agents"] == 8, "Expected eight distinct agents")
    check(config["mode"] == "features" and config["allow_spaces"] is False, "Expected strict features mode")
    check(config["randomize_feature_assignment"] is True and config["score_interval_s"] == 60, "Wrong experiment settings")
    check(config["max_cost_usd"] == 20 and config["seed"] == 0, "Wrong budget or seed")
    check(run.name.endswith("_" + summary["game_id"]), "Run ID mismatch")
    check(summary["final_score"] == scores[-1], "Final score differs from the score stream")
    check(summary["score_rounds"] == len(scores), "Score count mismatch")
    check(dict(Counter(c["agent_id"] for c in calls)) == summary["turns_per_agent"], "Gameplay call count mismatch")
    check(Counter(i["agent_id"] for i in interviews) == Counter(ids), "Expected exactly one interview per agent")
    check(all(c["state_applied"] in (True, False) for c in calls), "Missing applied-state flags")
    check(all(a["timestamp"] <= b["timestamp"] for a, b in zip(calls, calls[1:])), "Call order is not chronological")

    initial = initial_guesses(calls, ids, goal)
    states = {agent: dict(guess) for agent, guess in initial.items()}
    first_correct = {agent: 0.0 if guess == goal else None for agent, guess in states.items()}
    first = None
    peak_correct = sum(g == goal for g in states.values())
    cost = Decimal(0)
    posted = []
    regressions = []
    last_guess_change = 0.0
    last_applied = 0.0

    def convergence(elapsed, call_count, last_agent):
        return {
            "elapsed_s": elapsed, "gameplay_calls": call_count,
            "reported_cost_usd": str(cost), "agent_posts": len(posted),
            "glyphs": sum(len(message[1]) for message in posted if not message[2]),
            "last_agent": last_agent,
        }

    if peak_correct == len(ids):
        first = convergence(0.0, 0, None)
    for number, call in enumerate(calls, 1):
        cost += reported_cost(call)
        agent = call["agent_id"]
        if call["state_applied"]:
            check(not call.get("parse_error"), "An unparsable response was applied")
            guess = call["guess"]
            check(set(guess) == set(goal), "Applied guess has a different feature set")
            if states[agent] != guess:
                last_guess_change = call["elapsed_s"]
            states[agent] = guess
            last_applied = call["elapsed_s"]
            if guess == goal and first_correct[agent] is None:
                first_correct[agent] = call["elapsed_s"]
            if call.get("message"):
                violation = bool(call.get("is_violation"))
                message = "⊘" if violation else call["message"]
                if not violation:
                    check(set(message) <= set(glyphs), "Non-glyph content in a valid posted message")
                posted.append((agent, message, violation))
        count = sum(guess == goal for guess in states.values())
        peak_correct = max(peak_correct, count)
        if first is None and count == len(ids):
            first = convergence(call["elapsed_s"], number, agent)
        elif first is not None and count < len(ids):
            regressions.append(number)

    public_posts = [entry for entry in chat if entry["sender"] != "system"]
    check(posted == [(entry["sender"], entry["text"], entry["is_violation"]) for entry in public_posts], "Applied messages differ from public chat")
    check(states == summary["final_score"]["guesses"], "Final applied guesses differ from final scored guesses")
    total = cost + sum((reported_cost(row) for row in interviews), Decimal(0))
    check(abs(total - Decimal(str(summary["total_cost_usd"]))) <= Decimal("0.0000005"), "Cost mismatch beyond summary rounding")
    final_correct = sum(guess == goal for guess in states.values())
    feature_correct = sum(guess[name] == value for guess in states.values() for name, value in goal.items())
    check(final_correct / len(ids) == summary["final_score"]["fully_correct_rate"], "Final agent accuracy mismatch")
    check(all(sum(guess[name] == value for guess in states.values()) / len(ids) == summary["final_score"]["feature_accuracy"][name] for name, value in goal.items()), "Final feature accuracy mismatch")
    index = len(scores) - 1
    while index and score_key(scores[index - 1]) == score_key(scores[-1]):
        index -= 1
    unapplied = Counter(c.get("ignored_reason") or "parse_error" for c in calls if not c["state_applied"])
    result = {
        "label": label, "run": relative_path, "game_id": summary["game_id"],
        "raw_files_verified": len(RAW_FILES), "raw_bytes": raw["total_bytes"],
        "models_by_agent": {agent["agent_id"]: agent["model"] for agent in agents},
        "stop_reason": summary["stop_reason"], "first_all_correct": first,
        "first_correct_by_agent_s": first_correct,
        "all_agents_ever_correct": all(value is not None for value in first_correct.values()),
        "peak_simultaneously_correct_agents": peak_correct,
        "regressions_after_first_all_correct": len(regressions),
        "victory_detected_s": scores[-1]["elapsed_s"] if summary["stop_reason"] == "win_threshold_reached" else None,
        "full_run": {
            "elapsed_s": summary["elapsed_s"], "gameplay_calls": len(calls),
            "interview_calls": len(interviews), "total_logged_calls": len(calls) + len(interviews),
            "gameplay_reported_cost_usd": str(cost), "reported_cost_usd": str(total),
            "summary_rounded_cost_usd": summary["total_cost_usd"],
            "agent_posts": len(posted), "glyphs": sum(len(p[1]) for p in posted if not p[2]),
            "system_posts": sum(entry["sender"] == "system" for entry in chat),
            "applied_silent_calls": sum(c["state_applied"] and not c.get("message") for c in calls),
            "unapplied_calls": sum(unapplied.values()), "unapplied_reasons": dict(sorted(unapplied.items())),
            "parse_errors": sum(bool(c.get("parse_error")) for c in calls),
            "glyph_violations": sum(bool(c.get("is_violation")) for c in calls),
            "logged_api_errors": 0,
        },
        "final_accuracy": {
            "fully_correct_agents": final_correct, "agents": len(ids),
            "correct_feature_guesses": feature_correct, "feature_guesses": len(ids) * len(goal),
            "feature_accuracy_percent": 100 * feature_correct / (len(ids) * len(goal)),
            "remaining_errors": {
                agent: {name: {"guess": guess[name], "correct": value} for name, value in goal.items() if guess[name] != value}
                for agent, guess in states.items() if guess != goal
            },
        },
        "last_guess_change_s": last_guess_change, "last_applied_response_s": last_applied,
        "final_score_unchanged_from_round": scores[index]["round"],
        "final_score_unchanged_from_s": scores[index]["elapsed_s"],
        "final_score_s": scores[-1]["elapsed_s"],
    }
    matching = {
        "config_except_models": {key: value for key, value in config.items() if key not in ("model", "agent_models")},
        "goal": goal_record, "glyphs": glyphs, "initial_guesses": initial,
        "agent_setup_except_models": [{key: value for key, value in agent.items() if key != "model"} for agent in agents],
    }
    return result, matching


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-metrics", action="store_true", help="Explicitly regenerate metrics.json after verification")
    args = parser.parse_args()
    verified = [verify_run(label, path) for label, path in RUNS]
    matching = verified[0][1]
    check(all(item[1] == matching for item in verified[1:]), "Runs differ in setup beyond model choices")
    result = {
        "schema_version": 1,
        "matched_setup_except_models": True,
        "runs": [item[0] for item in verified],
        "method": {
            "initial_state": "Exact initial guesses are parsed from each agent's first recorded request, without importing or rerunning gameplay.",
            "correctness": "Replay agent_calls.jsonl in log order; only state_applied=true changes a guess. First simultaneous correctness is not proof of explicit knowledge.",
            "cost": "Sum usage.cost for completed logged responses using Decimal. In-flight or hidden SDK retry charges unavailable in these records are not estimated. Summary costs are rounded to six decimal places.",
            "glyphs": "Unicode code points in valid agent message bodies, excluding sender labels, system feedback, and violation markers. Post counts include agent posts only.",
            "cutoff": "Includes the response and its own message that first makes all eight current guesses correct. Use log order rather than rounded timestamps to include that message consistently.",
            "errors": "Logged API errors and returned parse failures are counted separately; absence of logged API errors does not exclude hidden successful SDK retries.",
        },
    }
    if args.write_metrics:
        METRICS.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    else:
        check(result == read_json(METRICS), "metrics.json differs from recomputed results")
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
