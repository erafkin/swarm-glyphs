# Can Haiku use Sol's language? Cross-model round 2

Question: given the frozen Swarmish reference that eight Sol agents wrote (seed 1, E01), can a team
of a different model use it to play Storm Shelter, or does it start changing the rules? Haiku 5.5
was chosen because its own round 2, Tom's R06, had already failed, which makes R06 the natural
control: the same model on the language it built itself.

Setup: eight `anthropic/claude-haiku-5.5` agents, medium reasoning, the 130-line E01 shared draft
as reference, the exact 200-glyph sample E01 was built with, the revised prompt (escape and stay
undecoded), no task time limit, $12 safety cap. Run on 2026-11-08 and cancelled by hand after
828 turns when it had made no progress; the summary was written on interruption. Tom's R06 used
the same prompt on the E06 Haiku reference (51 single-glyph words, 89 lines) and was stopped by
the batch's 200-turn task limit, so the Haiku-on-Sol run is also shown sliced to its first 200
turns. Sol's own R01 on the same E01 reference is the yardstick. One run per cell.

## Numbers

| | Haiku, own language (R06) | Haiku on Sol, first 200 turns | Haiku on Sol, full run | Sol, own language (R01) |
|---|---|---|---|---|
| Reference | 51 words | 401 words | 401 words | 401 words |
| Stop | turn_limit_reached | interrupted | interrupted | escaped |
| Task turns | 200 | 200 | 828 | 81 |
| Room actions | 0 | 0 | 0 | 38 |
| Room stage reached | cabinet | cabinet | cabinet | escaped |
| Messages posted | 109 | 145 | 323 | 77 |
| Messages rejected for illegal characters | 0 | 3 | 4 | 0 |
| Distinct words used | 27 | 35 | 39 | 107 |
| Tokens that are reference words | 100% | 88% | 89% | 99% |
| Single glyphs used as words | 100% | 12% | 11% | 0% |
| Exact duplicate messages | 35% | 27% | 42% | 4% |
| Tokens per message | 6.6 | 8.4 | 9.3 | 21.5 |
| Symbols whose digit was stated privately | 3 of 4 | 4 of 4 | 4 of 4 | 4 of 4 |
| Spend | $0.18 | $0.45 | $2.83 | $2.11 |

Single glyphs are not words in Sol's language, where every word is two glyphs; in Haiku's own
language every word is a single glyph, so that row does not apply to R06. "Stated privately"
counts the private intended-meaning annotations, which the teammates never see.

## Findings

**The failure is the model's, not the language's.** On its own language and on Sol's, Haiku did
the same thing for the whole run: each agent announced that it held a clue and asked the others
to share theirs, then chose to wait. Across 1,028 Haiku turns in the two runs, no agent ever
submitted a cabinet code. Sol's team on the identical reference and prompt entered the correct
code by its fifth action and escaped in 155 seconds.

**The clues were understood.** The Haiku-on-Sol team stated a digit for all four cabinet symbols
in its private annotations, exactly as Sol's team did; R06 stated three of four. Haiku holds the
pieces and never assembles them: it waits for a complete mapping to arrive rather than
contributing its part to a shared code.

**On Sol's language, Haiku bends the grammar toward its own.** The first message from agent_3 is
a correct Sol clause with opener, predicate marker, role markers and closer. From the second turn
on the frame is gone: two percent of messages have it. The team also clipped two-glyph words to
their second glyph, with 𗣎 for 𗌿𗣎 "ask" and 𗗢 for 𗌿𗗢 "include" accounting for about an eighth
of all tokens. What they wrote, pronoun first then bare content words with no markers, has the
shape of Haiku's own E06 design: single glyphs in subject-verb-object order. Given a richer
grammar, Haiku regressed to the grammar it would have built.

**On its own language there was nothing to bend**, and it did not: R06 is 100 percent reference
words with no rejections. A single-glyph vocabulary cannot be clipped and a grammar without
clause markers cannot lose them. That makes the clean R06 figures a floor, not a sign of
competence.

**Repetition rose over time.** Exact duplicates ran at 27 percent in the first 200 turns and 41
percent by turn 614; the last sixty turns before cancellation used ten distinct words. Varying the
wording of the same request was the only change in behaviour over fourteen minutes.

## Caveats

One run per cell. R06 ended at Tom's 200-turn limit; the Sol-language run had no turn limit and
was cancelled, so its full-run column is longer but not different in kind. A first attempt with
the baseline prompt was stopped after eight calls and 16 cents when the revised prompt was chosen
instead; it is not archived. Haiku's reasoning was medium, as in Tom's encoder and R06 settings.

## Files

Run: `logs/20261108_115614_3b302c39_round_2`. Preset: `configs/storm_shelter_tangut_200_wincond_haiku_task.json`
(the seed 1 win-condition preset with `task_model` set to Haiku and a $12 cap). Control: `gameplay/R06_haiku_seed1`
in this batch. Yardstick: `gameplay/R01_sol_seed1`.
