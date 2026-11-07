# Mixed strict features run 9490e69c: shared binary English

Started **2026-11-07 16:20:58 UTC** at
[`fe9bf7c`](https://github.com/erafkin/swarm-glyphs/commit/fe9bf7cd4eefa10e30025fb036049b14c535e662).
Four GPT-6.1 Sol agents (0, 2, 4, 6) and four Gemini 3.8 Flash agents (1, 3,
5, 7), eight features with four choices each, seed 0, medium reasoning,
16,000-token gameplay/interview caps, 240-second scoring, and a $30 soft limit.
Message bodies contained only sampled glyphs: no spaces or IDs.
Sender labels remained visible. Feature ownership still followed agent index
in canonical feature order, matching the earlier single-family runs; it was
not randomized or explicitly disclosed to peers.

## How they solved it

Three Sol agents independently began sending binary ASCII with different
glyph mappings. Agent 4's `clothing=shirt` at **12.2 s** became the common code:

| Glyph | Assigned role |
|---|---|
| 𗏏 | Binary 0 |
| 𘜎 | Binary 1 |
| 𗘸 | Separator between eight-bit ASCII characters |

Gemini agents used this convention for `glasses=none`, `clothing_colour=blue`,
and `hairstyle=curls` at **29.8–46.4 s**. Gemini agent 7 sent
`expression=smile` at **56.1 s** using another alphabet:
`𗈰 = 0`, `𗰷 = 1`, `𗒇 = separator`.
All four Sol agents translated and relayed that clue in the common encoding
at **70.3–73.6 s**. Agent 6 explicitly wrote:
“Broadcast expression=smile translated into common protocol.”

This is coordination around familiar binary, ASCII, and English conventions,
including translation between glyph alphabets. It does not establish the
creation of new vocabulary or grammar. The first four-glyph unary proposal
is interpreted from its sender's scratchpad; the subsequent ASCII messages
are decoded mechanically from the logged glyph strings.

## Outcome

| Milestone | Recorded result |
|---|---|
| All eight submitted guesses first correct | **102.0 s** |
| Completed API calls / spend at that point | **52 / $1.11292675** |
| Agent chat posts / glyphs at that point | **21 / 2,738** |
| Victory detected | **240 s** |
| Finished, including interviews | **272.4 s** |
| Full run | **192 calls / $4.58665725** |
| Full chat | **22 posts / 2,881 glyphs** |

The 192 calls comprise 184 gameplay responses and eight interviews. Gameplay
includes 22 posts, 157 applied silent responses, and five unapplied late
responses. No API errors, parse failures, or glyph violations were recorded.

Some early correct answers included lucky guesses. All submitted answers
were correct at 102.0 s; every agent's scratchpad explicitly recorded all
eight facts by **105.7 s**. No score feedback had yet been supplied.
The first-correctness glyph count includes the convergence reply's own
143-glyph post, whose chat timestamp follows its API log timestamp by milliseconds.
Counts exclude sender labels and English feedback; milestone costs exclude
pending responses. This mixed run avoided the persistent colour mistake in
the Sol run and the convention confusion in the Gemini run. One trial per
condition does not establish that mixed teams are generally faster.

## Evidence and verification

The nine original JSON/JSONL files (**2,748,246 bytes**) are unchanged, with
hashes in `SHA256SUMS` and sizes in [raw-inventory.json](analysis/raw-inventory.json).
Saved local paths are historical provenance, not portable runtime settings.
Read the [decoded chat](analysis/decoded-chat.txt) or
[exact glyph strings, mappings, and milestones](analysis/decoded-chat.json).
From this directory, verify hashes, costs, convergence counts, and every
supplied ASCII decoding without API calls:

```sh
python3 analysis/verify_run.py
```
