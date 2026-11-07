# Features run 762a9229: agent IDs became an octal alphabet

Archived run from **2026-11-07 05:50:05 UTC**, using code revision
[`b5168dc`](https://github.com/erafkin/swarm-glyphs/commit/b5168dcfaf2db1acbcaa54a65b673ca000536583).
Eight GPT-6.1 Sol agents each knew one of eight features with four options.
Settings: medium reasoning, 16,000-token caps for gameplay and interviews,
240-second scoring, seed 0, and a $50 soft limit. This run predates the optional
strict glyph-only mode added in `58371df`.

## How they used the extra channel

The rules permitted glyphs, spaces, and agent IDs in message bodies. Agents
independently treated `agent_0` through `agent_7` as octal digits and encoded
ordinary English as ASCII: `agent_1 agent_4 agent_3` means octal `143`, or `c`.
Double spaces usually separated characters. This transmitted complete clues
such as `clothing=shirt` without violating the implemented validator.

Agents 2, 4, and 5 independently proposed octal on their first turns, each with
an empty chatroom. Others initially encoded English through glyph counts
(A=1 through Z=26), binary ASCII, or ambiguous option indices. Agents translated
and relayed peers' clues, then converged on octal. Of 186 posted agent messages,
180 contained only IDs and spaces; 180 used octal encoding. These are different
counts: two octal messages also contained glyphs, and two ID-only messages were
option indices. Hair colour was the last clue to reach everyone.

## Outcome and interpretation

- All eight guesses were correct by **53.1 seconds**, after 26 completed calls
  costing **$0.384907**. They stayed correct thereafter.
- By **54.7 seconds**, all eight scratchpads explicitly recorded decoding the
  full answer. Earlier correct guesses sometimes included lucky unknown values.
- There was **no score feedback before convergence**. The first score at
  240 seconds detected the win; interviews finished by 248.6 seconds.
- Total: **216 gameplay calls + 8 interviews, $5.484505**, with no API errors,
  parse errors, or glyph violations. Two late gameplay responses were logged
  without changing state. About 93% of gameplay spending was recorded after
  collective correctness.

This demonstrates rapid coordination through shared encoding knowledge and an
extra channel allowed by the rules. It does not establish novel glyph meanings
or performance under a strict glyph-only channel. Banning IDs alone does not
prevent encoded English: the initial glyph-only schemes already carried it.

## Evidence

The nine original JSON/JSONL files are preserved byte-for-byte; `SHA256SUMS`
records their hashes. `agents.json` contains prompts and private clues;
`agent_calls.jsonl` contains every completed turn; `chatroom.jsonl` contains
posted messages; interviews and the final score are saved separately.
The archived config retains its original local board path; use the recorded
code revision and a suitable local path when reproducing the setup.

Derived files in [`analysis/`](analysis/) include the
[decoded transcript](analysis/decoded_transcript.csv),
[guess timeline and usage totals](analysis/timeline.json), and an offline
[reconstruction script](analysis/build_timeline.py). Run the latter with
`python3 analysis/build_timeline.py` from this directory (standard library only).
It replays only `state_applied: true` guesses. Scratchpad milestones are manually
identified self-reports, distinct from mechanically verified guess correctness;
the two ambiguous index messages are labelled as intended interpretations.
