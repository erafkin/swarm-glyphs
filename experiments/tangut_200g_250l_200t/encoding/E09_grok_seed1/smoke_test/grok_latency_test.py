"""Latency test: the same real E09 turn at low effort and at medium with a reasoning budget."""
import asyncio, json, re, sys, time
from pathlib import Path
REPO = Path("/Users/emmakrentz/code/swarm-glyphs/erafkin-swarm-glyphs"); sys.path.insert(0, str(REPO))
from src.core import api_call
from src.enc_dec.config import LanguageExperimentConfig
from src.enc_dec.models import CREATION_SCHEMA, CreationResponse

raw = Path(sys.argv[1]); out = Path(sys.argv[2])
config = LanguageExperimentConfig.from_file(REPO / "experiments/tangut_200g_250l_200t/encoding/E09_grok_seed1/config.json")
calls = [json.loads(l) for l in (raw / "agent_calls.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
agents = {a["agent_id"]: a for a in json.loads((raw / "agents.json").read_text())}
inv = set(json.loads((raw / "glyphs.json").read_text()))
TANGUT = re.compile(r"[\U00017000-\U000187F7]")
# Baseline: a logged medium-effort turn with a non-empty draft in its prompt and reasoning near the run mean.
cands = [c for c in calls if "(empty)" not in c["turn_prompt"] and c.get("usage")]
mean = sum(c["usage"]["completion_tokens_details"]["reasoning_tokens"] for c in cands) / len(cands)
base = min(cands, key=lambda c: abs(c["usage"]["completion_tokens_details"]["reasoning_tokens"] - mean))
system, turn = agents[base["agent_id"]]["system_prompt"], base["turn_prompt"]

def row(name, usage, latency, finish, structured, parsed_doc):
    g = [ch for ch in parsed_doc if ord(ch) > 0x7F and not ch.isspace()]
    return {"variant": name, "reasoning_tokens": (usage.get("completion_tokens_details") or {}).get("reasoning_tokens"),
            "completion_tokens": usage.get("completion_tokens"), "prompt_tokens": usage.get("prompt_tokens"),
            "latency_s": round(latency), "cost_usd": usage.get("cost"), "finish_reason": finish, "structured": structured,
            "doc_lines": len(parsed_doc.splitlines()), "glyph_chars": len(g), "inventory_glyphs": sum(1 for ch in g if ch in inv),
            "garbage_chars": sum(1 for ch in g if not TANGUT.match(ch))}

async def one(client, name, reasoning):
    kwargs = dict(model=config.model, messages=[{"role": "system", "content": system}, {"role": "user", "content": turn}],
                  max_tokens=config.max_tokens, extra_body={"usage": {"include": True}, "reasoning": reasoning},
                  response_format={"type": "json_schema", "json_schema": CREATION_SCHEMA})
    t = time.monotonic()
    completion = await api_call._create(client, **kwargs)
    latency = time.monotonic() - t
    text = api_call.sanitize_text(completion.choices[0].message.content or "")
    try:
        parsed = api_call.parse_response(text, CreationResponse); doc = parsed.language_document or ""; ok = True
    except Exception as e:
        doc = ""; ok = f"parse failed: {e}"[:120]
    return row(name, completion.usage.model_dump(), latency, completion.choices[0].finish_reason, ok, doc)

async def main():
    client = api_call.make_client(config)
    try:
        results = [row("medium (logged baseline, same prompt)", base["usage"], base["latency_s"], base["finish_reason"], True, base.get("language_document") or "")]
        results[0]["agent_turn"] = f"{base['agent_id']} t{base['turn']}"
        for name, reasoning in (("low effort", {"effort": "low"}), ("reasoning max_tokens 8000 (no effort)", {"max_tokens": 8000})):
            try:
                results.append(await one(client, name, reasoning))
            except Exception as e:
                results.append({"variant": name, "error": repr(e)[:300], "reasoning_tokens": None, "completion_tokens": None, "latency_s": None, "cost_usd": 0, "finish_reason": None, "structured": None, "doc_lines": 0, "glyph_chars": 0, "inventory_glyphs": 0, "garbage_chars": 0})
            out.write_text(json.dumps({"run_mean_reasoning_tokens": round(mean), "results": results}, ensure_ascii=False, indent=2) + "\n")
    finally:
        await client.close()
    out.write_text(json.dumps({"run_mean_reasoning_tokens": round(mean), "results": results}, ensure_ascii=False, indent=2) + "\n")
    print(f"baseline prompt: {results[0]['agent_turn']} (run mean reasoning {mean:.0f})")
    for r in results:
        if r.get("error"):
            print(f"{r['variant']:44} ERROR {r['error']}"); continue
        print(f"{r['variant']:44} reasoning={r['reasoning_tokens']:>6} compl={r['completion_tokens']:>6} latency={r['latency_s']:>4}s cost=${r['cost_usd']:.3f} finish={r['finish_reason']} structured={r['structured']} doc_lines={r['doc_lines']} glyphs={r['glyph_chars']} in_inventory={r['inventory_glyphs']} garbage={r['garbage_chars']}")
    print("test cost: $%.3f" % sum(r["cost_usd"] or 0 for r in results[1:]))
asyncio.run(main())
