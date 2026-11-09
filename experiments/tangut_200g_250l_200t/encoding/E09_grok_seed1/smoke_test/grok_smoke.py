"""Grok 4.7 smoke test through the harness client: tokenizer rate on Tangut, copy fidelity,
reasoning volume and structured output on a real round 1 prompt. Four calls, a few cents."""
import asyncio, json, re, sys, time
from pathlib import Path
REPO = Path("/Users/emmakrentz/code/swarm-glyphs/erafkin-swarm-glyphs")
sys.path.insert(0, str(REPO))
from src.core.api_call import call_agent, make_client
from src.enc_dec.config import LanguageExperimentConfig
from src.enc_dec.models import CREATION_SCHEMA, CreationResponse

preview = Path(sys.argv[1]); out = Path(sys.argv[2])
config = LanguageExperimentConfig.from_file(REPO / "experiments/tangut_200g_250l_200t/encoding/E09_grok_seed1/config.json")
model = config.model
agents = json.loads((preview / "agents.json").read_text())
glyphs = json.loads((preview / "glyphs.json").read_text())
gset = set(glyphs)
system_full = agents[0]["system_prompt"]
TANGUT = re.compile(r"[\U00017000-\U000187F7]")
system_noglyph = TANGUT.sub("", system_full)
assert len(TANGUT.findall(system_full)) == 200 and not TANGUT.search(system_noglyph)

def usage_row(name, r, started):
    u = r.usage or {}
    return {"call": name, "latency_s": round(time.monotonic() - started, 2), "finish_reason": r.finish_reason,
            "prompt_tokens": u.get("prompt_tokens"), "completion_tokens": u.get("completion_tokens"),
            "reasoning_tokens": ((u.get("completion_tokens_details") or {}).get("reasoning_tokens")),
            "cached_tokens": ((u.get("prompt_tokens_details") or {}).get("cached_tokens")),
            "cost_usd": u.get("cost"), "structured": r.used_structured_output, "parse_error": r.parse_error}

try:
    import tiktoken
    o200k = tiktoken.get_encoding("o200k_base")
    o200k_full, o200k_noglyph = len(o200k.encode(system_full)), len(o200k.encode(system_noglyph))
except Exception as e:
    o200k_full = o200k_noglyph = None

async def main():
    client = make_client(config)
    rows, notes = [], {}
    try:
        t = time.monotonic()
        a = await call_agent(client, model, system_noglyph, "Ready? Reply with exactly OK.", None, None, config)
        rows.append(usage_row("A_system_without_glyphs", a, t)); notes["A_raw"] = a.raw[:200]
        t = time.monotonic()
        b = await call_agent(client, model, system_full, "Ready? Reply with exactly OK.", None, None, config)
        rows.append(usage_row("B_system_with_200_glyphs", b, t)); notes["B_raw"] = b.raw[:200]
        sample = glyphs[:20]
        t = time.monotonic()
        c = await call_agent(client, model, "You are testing exact character reproduction.",
                             "Repeat exactly these 20 characters, separated by single spaces, and nothing else:\n" + " ".join(sample),
                             None, None, config)
        rows.append(usage_row("C_copy_20_glyphs", c, t))
        got = c.raw.strip().split()
        notes["C_expected"] = sample; notes["C_got"] = got
        notes["C_exact_match"] = got == sample
        notes["C_matching_positions"] = sum(1 for x, y in zip(got, sample) if x == y)
        turn = ("Discussion turns scheduled so far: 1 of 200.\n\nRecent chat:\n(no messages yet)\n\n"
                "Current swarmish.txt:\n(empty)\n\nRespond with the JSON object described in your instructions.")
        t = time.monotonic()
        d = await call_agent(client, model, system_full, turn, CREATION_SCHEMA, CreationResponse, config)
        rows.append(usage_row("D_round1_turn_structured", d, t))
        notes["D_raw_head"] = d.raw[:1500]
        if d.parsed is not None:
            doc = d.parsed.language_document or ""
            used = TANGUT.findall(doc) + TANGUT.findall(d.parsed.message or "")
            notes["D_parsed"] = {"message_chars": len(d.parsed.message or ""), "document_lines": len(doc.splitlines()),
                                 "done": d.parsed.done, "glyphs_emitted": len(used),
                                 "glyphs_outside_sample": sorted({g for g in used if g not in gset})}
    finally:
        await client.close()
    pa, pb = rows[0]["prompt_tokens"], rows[1]["prompt_tokens"]
    summary = {"model": model, "reasoning_effort": config.reasoning_effort, "max_tokens": config.max_tokens,
               "grok_prompt_tokens_without_glyphs": pa, "grok_prompt_tokens_with_glyphs": pb,
               "grok_tokens_per_glyph": round((pb - pa) / 200, 2) if pa and pb else None,
               "o200k_prompt_tokens_without_glyphs": o200k_noglyph, "o200k_prompt_tokens_with_glyphs": o200k_full,
               "o200k_tokens_per_glyph": round((o200k_full - o200k_noglyph) / 200, 2) if o200k_full else None,
               "total_cost_usd": round(sum(r["cost_usd"] or 0 for r in rows), 5), "calls": rows, "notes": notes}
    out.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for r in rows:
        print(f"{r['call']:28} prompt={r['prompt_tokens']:>6} compl={r['completion_tokens']:>6} reason={r['reasoning_tokens']} cached={r['cached_tokens']} cost=${r['cost_usd']} finish={r['finish_reason']} structured={r['structured']} parse_error={r['parse_error']} latency={r['latency_s']}s")
    print("tokens/glyph grok:", summary["grok_tokens_per_glyph"], "| o200k:", summary["o200k_tokens_per_glyph"])
    print("copy exact:", notes.get("C_exact_match"), "| matching positions:", notes.get("C_matching_positions"), "/ 20")
    print("round1 parsed:", json.dumps(notes.get("D_parsed"), ensure_ascii=False))
    print("A/B replies:", repr(notes["A_raw"]), repr(notes["B_raw"]))
    print("TOTAL COST: $", summary["total_cost_usd"])
asyncio.run(main())
