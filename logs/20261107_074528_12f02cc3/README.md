# Gemini strict features run 12f02cc3: counting glyphs

Started **2026-11-07 15:45:27 UTC** at
[`fe9bf7c`](https://github.com/erafkin/swarm-glyphs/commit/fe9bf7cd4eefa10e30025fb036049b14c535e662).
Eight Gemini 3.8 Flash agents, eight features with four choices each, seed 0,
medium reasoning, 16,000-token gameplay/interview caps, 240-second scoring,
and a $20 soft limit. Message bodies allowed only sampled glyphs: no spaces
or IDs. **Sender labels remained visible, and feature ownership followed
agent index.** Each agent received only its own clue; the ownership mapping
was not explicitly supplied, but could be inferred from the canonical feature order.

## How they solved it

The eventual code used the **number of repeated glyphs** as the one-based index
of a value in an alphabetically sorted option list. Sender ID indicated the
feature. Glyph identity itself carried no necessary information:

| Sender | Feature | Settled message | Count | Meaning |
|---|---|---|---:|---|
| agent_0 | hair_colour | 𗮘𗮘𗮘 | 3 | brown |
| agent_1 | hairstyle | 𗰷𗰷 | 2 | curls |
| agent_2 | facial_hair | 𗾧 | 1 | beard |
| agent_3 | glasses | 𗄌 | 1 | none |
| agent_4 | clothing | 𗏏𗏏𗏏 | 3 | shirt |
| agent_5 | clothing_colour | 𗈰 | 1 | blue |
| agent_6 | background | 𗈰𗈰 | 2 | green |
| agent_7 | expression | 𗈰𗈰𗈰 | 3 | smile |

Agreement was gradual. Some early repeated messages were intended as personal
signatures or handshakes. Agent 1 changed three glyphs to two at **270.6 s**;
agent 2 changed three to one at **337.5 s**. Agent 0's initial three-glyph
signature happened to be the correct value count.

## Outcome

| Milestone | Recorded result |
|---|---|
| All eight submitted guesses first correct | **385.5 s** |
| Completed API calls / spend at that point | **184 / $1.307628** |
| Agent chat posts / glyphs at that point | **14 / 30** |
| Victory detected | **480 s** |
| Finished, including original interviews | **497.5 s** |
| Full run | **267 calls / $1.67423775** |
| Full chat | **71 posts / 140 glyphs** |

The 267 calls comprise 259 gameplay responses and eight original interviews.
Gameplay includes 71 posts, 185 applied silent responses, and three unapplied
late responses. No API errors, parse failures, or glyph violations were recorded.
The 57 posts after first correctness repeat earlier sender/message pairs.

Glyph totals exclude sender labels, English system feedback, answer JSON,
and private scratchpads. Costs sum completed logged responses; pending calls
are not included at the correctness milestone. Correct guesses do not prove
perfect protocol understanding: agent 5 swapped two feature owners whose
values both had index 3. One run cannot establish general model superiority.

## Follow-up: why different glyphs?

[Eight additional contextual interviews](analysis/followup-glyph-choices/interviews.txt)
cost **$0.1411005**, separate from the run totals above. Five agents used the
first glyph in their individually shuffled lists, and agent 1 used its second.
Early scratchpads support personal-signature intentions for agents 0–2;
agents 5–6 later described copying agent 7's glyph as plausible. All eight
predicted that one shared glyph would work with visible sender labels, but
that counterfactual was not tested. Some follow-ups corrected overly tidy
original interview accounts. These are retrospective explanations; original
messages and scratchpads are stronger evidence of the process.

## Evidence and verification

The nine original JSON/JSONL files (**1,368,832 bytes**) are unchanged, with
hashes in `SHA256SUMS` and sizes in [raw-inventory.json](analysis/raw-inventory.json).
Saved local paths are historical provenance, not portable runtime settings.
The complete follow-up requests, responses, source hashes, manifest, evidence,
and summary are under [analysis/followup-glyph-choices](analysis/followup-glyph-choices).

See the [compact chat image](analysis/transcript/gemini-groupchat-until-correct.png),
[full chat image](analysis/transcript/gemini-full-chat-transcript.png),
[verbatim transcript](analysis/transcript/full-chat-transcript.txt),
[timeline](analysis/timeline/gemini_replay.json), and
[Sol comparison](analysis/comparison/comparison.json).
From this directory, verify hashes, counts, costs, and convergence without API calls:

```sh
python3 analysis/verify_run.py
python3 analysis/comparison/compare_runs.py
```

The comparison script also needs the sibling archived Sol run `5e5f03a8`.
Latency estimates use rounded request-start times and are approximate, not
provider time-to-first-token measurements.
