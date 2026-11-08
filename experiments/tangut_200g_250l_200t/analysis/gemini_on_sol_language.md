# Can Gemini use Sol's language? Cross-model round 2

Companion to `haiku_on_sol_language.md`. Same question: given the frozen Swarmish reference that
eight Sol agents wrote (seed 1, E01), can a different model's team use it to play Storm Shelter, or
does it change the rules? Gemini 3.8 Flash is the second model tried, and it has a stronger
control than Haiku: Tom's R07, Gemini on the language it built itself, escaped.

Setup: eight `google/gemini-3.8-flash` agents, medium reasoning, the 130-line E01 shared draft as
reference, the exact 200-glyph sample E01 was built with, the revised prompt (escape and stay
undecoded), no task time limit, $11 safety cap. Run on 2026-11-08. One run per cell.

## Numbers

| | Gemini, own language (R07) | Gemini on Sol's language | Sol, own language (R01) | Haiku on Sol's language |
|---|---|---|---|---|
| Reference | 200 single-glyph words, 159 lines | 401 two-glyph words, 130 lines | same as Gemini on Sol | same |
| Outcome | escaped, 297 s, $1.55 | escaped, 277 s, $1.80 | escaped, 155 s, $2.11 | cancelled at 827 s, $2.83, no actions |
| Task turns | 88 | 81 | 81 | 828 |
| Room actions, rejected | 22, 16 | 24, 18 | 34, 28 | 0 |
| Messages posted, rejected | 77, 0 | 73, 0 | 77, 0 | 323, 4 |
| Distinct words used | 75 of 200 | 72 of 401 | 107 of 401 | 39 of 401 |
| Tokens that are reference words | 100% | 100% | 99% | 89% |
| Single glyphs used as words | n/a, all single | 0% | 0% | 11% |
| Messages with Sol's clause frame | n/a | 88%, the other 12% are idioms | 100% | 2% |
| Tokens per message | 12.5 | 13.4 | 21.5 | 9.3 |
| Exact duplicate messages | 0% | 11% | 4% | 42% |
| Whole-utterance idioms used | n/a | 49 tokens, 5 distinct | 26 tokens, 4 distinct | 0 |
| Irregular synonym forms used | n/a | 10 | 18 | 0 |
| Symbols whose digit was stated privately | 4 of 4 | 4 of 4 | 4 of 4 | 4 of 4 |

## Findings

**Gemini learned the language.** Every token it sent is a word in Sol's reference. Every message
either has Sol's clause frame, open marker, predicate, roles, close, or is one of Sol's
whole-utterance idioms, which the reference says need no frame. Nothing was clipped, nothing was
invented, nothing was rejected. The first message from agent_6 is a well-formed clause stating
that the star symbol represents four, and the private intended meanings track the messages.

**It played about as well as on its own language.** 277 seconds against 297, 81 turns against 88,
24 room actions against 22, with a similar rejection rate. The language changed from its own
single-glyph subject-verb-object design to Sol's two-glyph role-marked one and the result did not.
Gemini's competence here is portable; Haiku's failure, by contrast, followed Haiku to both
languages.

**It used Sol's language differently from Sol.** Gemini leaned on the idioms: 49 idiom tokens
across five idioms, against Sol's 26 across four, with "please share the relevant information
only you possess" used 29 times and "I endorse the current proposal" six times. Sol never used
"endorse" or "do not act yet". Gemini also used fewer distinct words, 72 against 107, and shorter
messages, 13 tokens against 22, so its chat is terser and more formulaic, with 11 percent exact
duplicates to Sol's 4. It used the camouflage forms slightly less, ten irregular synonyms to Sol's
eighteen.

**It was slower than Sol on Sol's language**, 277 seconds against 155, though with fewer rejected
actions, 18 against 28. Whether that is the model or the unfamiliar grammar cannot be separated
from one run.

**Private understanding matched public behaviour.** All four symbol digits appear in Gemini's
private annotations, as in every other team, and unlike Haiku the team then entered codes and
operated the panel. The difference between the two foreign models is not comprehension of the
reference; it is whether the team converts what it knows into action.

## Caveats

One run per cell. R07 ran under Tom's 200-turn task limit, which it never approached. The Gemini
run here had no turn limit and ended on escape. The four-column table includes the Haiku run for
contrast; its full write-up and caveats are in `haiku_on_sol_language.md`.

## Files

Run: `logs/20261108_131700_b598a6c8_round_2`. Preset: `configs/storm_shelter_tangut_200_wincond_gemini_task.json`
(the seed 1 win-condition preset with `task_model` set to Gemini and an $11 cap). Control:
`gameplay/R07_gemini_seed1` in this batch. Yardstick: `gameplay/R01_sol_seed1`.
