# Strict features run 5e5f03a8: binary English and a Morse SOS

Started **2026-11-07 06:33:14 UTC** at code revision
[`c939c1d`](https://github.com/erafkin/swarm-glyphs/commit/c939c1de1e15c7011453568a374b95f0913e530e).
Eight agents, eight features with four choices each, GPT-6.1 Sol on medium,
16,000-token gameplay/interview caps, seed 0, 240-second scoring, $50 soft limit.
`allow_spaces: false`: message bodies contained only sampled glyphs, with no
spaces or agent IDs. Sender labels remained visible.

## How the shared code emerged

Agents proposed encodings without prior negotiation: every first turn saw an
empty chatroom. Five independently chose binary ASCII. Agents 3 and 7 chose
the same three glyphs by Unicode order; agent 5 chose the same bits but initially
omitted separators. Peers decoded these proposals and adopted the common code.
All eight had sent in it by **44.7 seconds**.

| Glyph | Assigned role | Unicode |
|---|---|---|
| 𗄌 | Binary 0 | U+1710C |
| 𗅋 | Binary 1 | U+1714B |
| 𗈰 | Separator between eight-bit characters | U+17230 |

Each eight-bit number is an ASCII character. For example, `blue`:

| Character | Binary | Recorded glyph sequence |
|---|---|---|
| b | `01100010` | 𗄌𗅋𗅋𗄌𗄌𗄌𗅋𗄌 |
| l | `01101100` | 𗄌𗅋𗅋𗄌𗅋𗅋𗄌𗄌 |
| u | `01110101` | 𗄌𗅋𗅋𗅋𗄌𗅋𗄌𗅋 |
| e | `01100101` | 𗄌𗅋𗅋𗄌𗄌𗅋𗄌𗅋 |

Joining these rows with `𗈰` reproduces agent 6's message at 257.0 seconds.
The glyph roles were newly assigned; binary, ASCII, and English meanings were
reused. This demonstrates spontaneous protocol coordination, not new vocabulary
or grammar. The logs establish proposals and successful decoding, not the
models' unrecorded internal recognition algorithms.

## The Morse detour

At 19.0 seconds, agent 6 sent **SOS BACKGROUND GREEN** using `𘑻` for dot,
`𗰷` for dash, `𗏠` between letters, and `𗡝` between words. Its scratchpad
explicitly hoped peers would recognize SOS (`... --- ...`). Agents 0, 1, 2, 4,
and 3 recorded decoding this message from inputs predating its binary
retransmission. Agents 1 and 4 relayed `background=green` in the shared binary
code. The Morse message used 66 glyphs; that binary clue used 143.

## Outcome and remaining error

- **56.2 s:** seven agents fully correct; 63/64 feature guesses correct.
- Agent 6 falsely decoded blue as yellow and preserved an identical wrong
  scratchpad for 27 turns despite the correct messages remaining visible.
  Agent 2 made the same initial error but corrected it at 44.7 s. Neither
  broadcast yellow; agent 5's original and clarified messages both encode blue.
- **240 s:** the first score identified clothing colour as the only imperfect
  feature. On its first score-aware turn, agent 6 re-read the original bytes.
- **257.0 s:** everyone correct. Agent 6's correction input contained no new
  post-score peer reminders, so the observed repair followed score feedback
  and re-reading old evidence.
- **480 s:** win detected; interviews finished by **489.8 s**.

Total: **$18.889641**, 476 gameplay calls plus 8 interviews. Only 36 agent
messages were posted; there were 436 applied silent responses and 4 late
unapplied responses. No API errors, parse failures, or glyph violations.

## Evidence and reproduction

The nine original JSON/JSONL files are unchanged; `SHA256SUMS` records their
hashes. The saved config retains its original local board path. This archive
describes the recorded revision, not later prompt changes on main.

See the [decoded chat](analysis/protocol/decoded_compact.csv),
[exact glyphs and bits](analysis/protocol/decoded_transcript.json),
[convergence analysis](analysis/timeline/timeline.json), and
[interview cross-checks](analysis/behavior/behavior_findings.json).
From this directory, reproduce the derived data with standard-library Python:

```sh
python3 analysis/protocol/decode_protocol.py
python3 analysis/timeline/build_timeline.py
```

Mappings and qualitative milestones come from contemporaneous scratchpads;
message bytes and accepted guess changes are checked mechanically. The initial
two-glyph index proposal is marked interpretive, not a negotiated convention.
