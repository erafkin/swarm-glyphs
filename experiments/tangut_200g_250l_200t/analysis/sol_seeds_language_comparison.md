# Five Swarmish languages from one model

Eight GPT 6.1 Sol agents, five seeds, the same prompt, the same 200-glyph budget drawn from the Tangut block. How different are the five languages they produced?

Short answer: the grammar is nearly the same language five times. The vocabulary design is five different answers to one question, "how do we make 200 glyphs hard to crack", and two of the five answers are the same clever trick invented independently.

## Summary

- **One grammar, five times.** Every seed built a role-marked, bracket-nested clause language with free constituent order: a clause delimiter, an explicit marker for actor, patient, recipient, source, place and time, grouping brackets that nest, a speech-act or mood word, scoped negation and uncertainty, quantifiers, and if/and/or. None chose fixed word order. None chose English-like syntax.
- **Two word shapes.** Seeds 1, 3 and 5 build words from two glyphs. Seeds 2 and 4 use single glyphs for everything and give each glyph three or four meanings, selected by a register or frame word at the start of the clause. That is the largest structural split in the set.
- **The register trick was invented twice.** Seed 2 (four registers, 140 glyphs, 560 senses) and seed 4 (three frames, 100 glyphs, 300 senses) arrived at the same device with no contact: a clause-initial word that chooses which column of a multi-column dictionary applies. Both explicitly forbid choosing the register by speaker, topic or turn, to keep it from becoming a cipher key.
- **Only seed 1 leaks word class through glyph shape.** Its words are two glyphs where the first glyph names the family: grammar markers, pronouns, verbs, relations, logic, quantities. Three quarters of its vocabulary falls into five such families, and the round 3 decoders found that within minutes. Seeds 3 and 5 build two-glyph words from a flat pool with no prefix structure, and seeds 2 and 4 have no prefixes to leak.
- **Every seed added deliberate free variation to defeat frequency counting.** Irregular synonyms (seed 1), four registers (seed 2), synonymous particles plus sender-specific words plus filler glyphs (seed 3), three freely switched frames (seed 4), a second form for every grammar word (seed 5). The prompt's "decoding team" framing produced camouflage in all five, but no two chose the same mechanism.
- **Seed 3 is the only one with speaker-dependent meaning.** Eight words mean different things depending on who sent the message, by a Latin square across the eight agents. Nothing else in the set makes the reader look at the sender to parse a word.
- **All five have whole-word numbers and refuse digit composition**, which is the no-calculation clause working as intended. The range differs: 0 to 99 plus large units (seed 1), 0 to 100 plus fractions (seed 3), 0 to 30 then tens (seed 2), 0 to 20 then tens (seed 4), 0 to 20 then a handful (seed 5).
- **All five have a bindable name pool and a define predicate.** Twelve aliases, thirty handles, twenty-two labels, twenty handles, twenty-four names. Every team decided that unknown task referents would be handled by binding an empty word to a description rather than by any spelling mechanism.
- **Four of five have whole-utterance idioms** for collaboration acts: endorse, reject, share your private information, I am done, please clarify. Seed 2 has none and relies on its registers for compactness instead.
- **Document organisation splits the same way as word shape.** The two-glyph languages read as reference grammars: grammar, then a lexicon grouped by semantic field, then examples. The single-glyph languages read as a short grammar followed by a large lookup table.

## Method and caveats

The five documents are the frozen handoff references: the last shared draft each team applied before stopping. Seed 1 (E01) is the earlier run with a 500-line cap and a ten-minute clock; seeds 2 to 5 ran under the 250-line cap and 200-turn budget. All five ended on all-done, and seed 1's document is 130 lines, so the different cap did not bind.

Each seed samples its own 200 glyphs from the 6,136 Tangut ideographs, and the samples barely overlap: between 2 and 9 shared glyphs for any pair of seeds. No vocabulary can be compared across seeds. Everything below is structural.

Word statistics come from a script that treats any maximal run of permitted glyphs as a word and counts distinct words, their glyph lengths, how many glyphs of the 200 appear, and how concentrated the first glyphs of two-glyph words are. "Lexicon lines" are lines pairing glyph words with short English glosses; "prose lines" contain no glyphs. Counts of grammar markers, number words, idioms and names are from reading the documents.

## Comparison matrix

| | Seed 1 (E01) | Seed 2 (E02) | Seed 3 (E03) | Seed 4 (E04) | Seed 5 (E05) |
|---|---|---|---|---|---|
| Lines / characters | 130 / 18,372 | 165 / 15,860 | 122 / 18,765 | 173 / 19,559 | 91 / 16,920 |
| Distinct glyph words | 401 | 199 | 531 | 252 | 264 |
| Word shape | all 2-glyph | all 1-glyph | 480 2-glyph, 51 1-glyph particles | 197 1-glyph, 55 2-glyph derived | 230 2-glyph, 24 1-glyph names, 10 3-glyph |
| Glyphs used of 200 | 192 | 199 | 200 | 197 | 197 |
| Meanings per content glyph | 1 | 4 (registers) | 1 | 3 (frames) | 1 |
| Approximate content senses | about 290 | about 560 | about 400 | about 300 plus 60 invariants | about 190 |
| First-glyph families | strong: 5 families hold 77% of words | none (single glyphs) | flat: 102 first glyphs, max 6 words each | none for content | flat: 153 first glyphs |
| Clause boundary | open and close words | register word opens, end word closes | one divider, two synonymous forms | frame word opens, end word closes | one divider, two forms |
| Role markers | 7 plus clause brackets | 8 | 6, each with two forms | 10 fields | 10, most with two forms |
| Speech act or mood | 7 scope words before the clause | 4 mandatory speech acts | question, request, possibility, necessity particles | 5 optional moods | 3 stance words, 2 forms each |
| Nesting | yes, with a restrictive-clause marker | bracket groups, nested propositions | bracket groups, quotation marker | bracket groups, nested clauses with own frame | bracket groups |
| Number words | 109: 0 to 99, large units, fractions | about 41, in register four | 115: 0 to 100, large units, fractions | 31: 0 to 20, tens, large units | 27: 0 to 20, 30, 40, 50, 100, 1,000 |
| Name pool | 12 aliases, 3 binding predicates | 30 handles | 22 labels | 20 handles, owner-qualified | 24 single-glyph names |
| Whole-utterance idioms | 14 | 0 | 23 | 16 | 9 |
| Camouflage device | irregular synonyms for grammar and common words | four registers | synonymous particles, sender-specific words, two filler glyphs | three freely switched frames | a second form for every grammar word |
| Speaker-dependent meaning | no | no, forbidden | yes, 8 words by sender | handles belong to their speaker | no |
| Worked examples | 5 | 7 | 0 | 6 | 6 |
| Lexicon lines / prose lines | 60 / 41 | 143 / 9 | 74 / 23 | 131 / 26 | 22 / 45 |

## The five languages

### Seed 1: a prefix-classed reference grammar

Every word is two glyphs and the first glyph is a class marker. One prefix family carries all the grammar: clause open and close, seven role markers, the restrictive-clause marker, the pair-grouping marker, and seven scope words for question, negation, request, uncertainty, conditional, disjunction and conjunction. Another family holds pronouns and the twelve bindable aliases. Three more families hold core verbs and nouns, relations and properties, and logic and quantifiers, and a sixth holds "open-world roots" such as substance, light, container, document. A seventh family holds 109 quantity words, zero to ninety-nine plus hundred, thousand, million, half, quarter, third, many, few, approximately.

The grammar is the most carefully specified of the five on scope: it states which role each argument takes for HAVE, OWNED-BY, BEFORE, CAUSES, GIVE and SAY, how a restrictive clause binds its omitted actor to the head, and how negation before a nested clause differs from negation before the predicate. The worked examples demonstrate exactly those contrasts.

The team saw the weakness of its own prefix system and added "irregular synonyms": a second, prefix-free form for every grammar marker and for twenty common words, to be chosen freely. It also added fourteen whole-utterance idioms. In the one round 2 and round 3 that have been run, the decoders found the prefix families first and the role grammar second, and the irregular synonyms were used rarely enough not to matter.

### Seed 2: one glyph, four meanings

This is the most radical design. Every token is a single glyph. A clause begins with one of four register glyphs, and that register selects which of four columns applies to every content glyph in the clause, including inside subordinate groups. The dictionary is a 140-row table with four English senses per row, so 140 glyphs carry 560 senses. Numbers live in the fourth column of the first forty rows: a glyph that means "I" in register one means "zero" in register four. Thirty glyphs are reserved as handles. The grammar fits in thirteen dense lines: four speech acts, eight roles, optional negation and uncertainty, bracket groups, and/or links, three quantifier modifiers, a relative-description marker, a correction marker.

The document is a lookup table with a grammar stapled to the front, 143 lexicon lines against nine of prose. There are no idioms. Compactness comes from the registers instead: a seed 2 message is about half the glyph length of a seed 1 message with the same content.

The register is explicitly not a cipher: "This is dictionary lookup, not a transformation", and agents are told to change register only at clause starts and never by a rule. For a decoder, per-glyph frequency counting is confounded four ways, but the four register glyphs are clause-initial and will be the first thing found, after which the columns can be separated.

### Seed 3: a flat vocabulary with a per-speaker dialect

Content words are two glyphs, but unlike seed 1 the pairs are drawn from a flat pool: 102 different first glyphs across 480 words, with no family holding more than six. Many content words are built from the same glyphs that serve as grammar particles, and the document warns that "never parse the internal glyphs of a dictionary word as particles." Grammar particles are single glyphs, and every one has a synonymous twin: two clause boundaries, two forms of each of six role markers, two forms of each logical and modal operator.

Three features are unique in the set. First, eight sender-specific words: each of the eight agents has its own row assigning the meanings know, choose, equal, true, false, propose, one and two to the same eight words in a different order, a Latin square, so a word's meaning depends on who sent it. Second, two "semantically empty hesitation words" that may be inserted between constituents as noise. Third, twenty-three whole-utterance idioms, several with alternate forms, covering endorse, reject, received, share your private information, checked and holds, checked and fails, I will do it, done, cannot, wait, clarify, correction, tentative, enough, no more information, conflict, final choice, cannot identify.

It has the largest number system, zero to one hundred as separate words plus two hundred, two hundred fifty, three, four and five hundred, a thousand, a million, and seven fractions, and the largest lexicon, organised by field: predicates, entities, qualities and logic, time and space, common task domains with colours, shapes, measures, and a hundred words for likely task content. It is the only document with no worked examples; it has a "usage and repair" section instead.

### Seed 4: one glyph, three meanings, with a derivational layer

Seed 4 reinvented seed 2's device with three frames instead of four registers, named SUN, RIVER and STONE in the English reference only. A clause begins with a frame glyph and ends with an end glyph; the frame governs every content glyph in it except inside a nested clause, which carries its own frame. A hundred content glyphs carry three senses each. Unlike seed 2, a substantial invariant layer sits outside the frames: ten field markers, five moods, bracket groups, negation, six quantifiers, an unknown word, six pronouns, two anaphors, seven logical predicates including exclusive or and equivalence, a naming predicate, and a source-value word that refers to "the exact task-given value associated with" a described item without reproducing it.

It is also the only language with a productive derivation: nineteen invariant attribute glyphs for colours, size, material, cost and so on, which combine with one suffix glyph to form nineteen derived words such as retract, observe, infer, document, column, row, identifier, hidden, adjacent, undo. Twenty opaque two-glyph handles belong to the agent who introduces them and are referred to by other agents through an owner-qualified group. Sixteen whole-utterance idioms close the lexicon.

The grammar is the most explicit about semantics after seed 1: what a frame does to a nested clause, that nested clauses denote propositions and never quotations of glyphs, how unmarked modifiers precede marked fields inside a group, that naming does not assert, and the difference between rejecting a proposal, retracting a claim and asserting its negation. The security guidance tells agents to vary frames and to avoid using one frame per speaker, which is precisely the pattern a decoder would hope for.

### Seed 5: the compact, readable one

The shortest document, 91 lines, and the only one with more prose than lexicon lines. Content words are two glyphs from a flat pool with no family structure. Every grammar word has two interchangeable forms, listed as "X or Y": two clause dividers, two of each bracket, two of each stance word, two of each role marker. Twenty-four single-glyph names form the pool for local labels, and the same glyphs also appear inside two-glyph words, which the document says is intentional and harmless. Nine whole-message idioms are three glyphs long, the only three-glyph words in any seed.

The grammar is the most procedural: a clause is a stance word followed by role constituents in any order, each constituent runs to the next role word or bracket, NOT and the modal scope words take one bracketed expression, AND, OR and exactly-one-of take two, IF takes a condition and a consequence, LIST and ORDERED-SEQUENCE take a bracketed collection with an item divider. A "writing and reading guide" gives the steps for composing and parsing a message. The number system is the smallest, zero to twenty, then thirty, forty, fifty, hundred, thousand, with instructions to describe anything else. Six worked examples form a short exchange: a declaration, a question, a denial, a request, an information-gap question, and a proposition name asserted true.

## Where they converge

**The clause model.** Five independent teams produced the same abstract grammar: delimited clauses, explicit semantic roles that can appear in any order, bracketed and nested groups, a clause-level speech act, scoped negation, quantifiers that attach to a description, and sentential connectives. None used positional syntax. This is the strongest finding in the set. Given a semantic rather than cipher framing and a reader who has only a text file, Sol reaches for a frame-semantics representation every time.

**Reference by binding.** All five provide a pool of meaningless words and a predicate that binds one to a description, and all five say that binding, not spelling, is how an unknown task term gets a name. All five also tell agents that a bound name does not assert its proposition.

**Whole-word numbers.** All five list numbers as indivisible words and forbid concatenation, arithmetic, positional notation and glyph counting. The no-calculation clause produced this uniformly. The size of the number vocabulary is where they differ, from 27 words to 115.

**Collaboration pragmatics.** Four of five list whole-utterance idioms, and the sets overlap heavily in meaning: endorse the proposal, reject it, share your private information, I have nothing further, I am done, please clarify, my information conflicts. The teams anticipated the same speech acts a cooperative task would need.

**Security preambles.** Every document opens by stating that it is a semantic language and not a cipher, that English is never sent, and that correctness beats obscurity. Seeds 1, 3, 4 and 5 add a closing section on style: vary synonyms, vary order, omit recoverable roles, do not greet, do not translate.

**Full use of the alphabet.** Each team used between 192 and 200 of its 200 glyphs, whether it built two-glyph words or multi-sense single glyphs.

## Where they diverge

**Word shape.** Two-glyph words with one meaning each (seeds 1, 3, 5) against single glyphs with three or four meanings each (seeds 2, 4). The second design halves message length and multiplies the lexicon, at the cost of making every reader track clause state.

**How class is signalled.** Seed 1 signals word class by prefix. Seeds 3 and 5 deliberately do not. Seeds 2 and 4 signal nothing by glyph and everything by position and the clause-initial register or frame.

**The camouflage mechanism.** Five different answers: a second prefix-free form for key words; four registers; speaker-dependent words plus synonymous particles plus filler; three frames to be switched freely; a second form for every grammar word. The intent is the same in all five, to make a glyph's frequency uninformative, but the means never repeat except for the register device shared by seeds 2 and 4.

**Speaker-dependence.** Seed 3 alone makes meaning depend on the sender. Seeds 2 and 4 explicitly forbid it for their registers and frames.

**Number range.** From 27 words (seed 5) to 115 (seed 3). Seeds 1 and 3 spent a quarter of their vocabulary on numbers; seed 5 spent a tenth.

**Idioms.** From none (seed 2) to twenty-three (seed 3).

**Grammar depth.** Seeds 1 and 4 specify argument structure per predicate, scope of negation over nested clauses, and the semantics of naming. Seed 5 specifies a parsing procedure. Seeds 2 and 3 specify the clause shape and leave fine scope to "use explicit roles and quotation".

**Document shape.** Grammar first with a field-organised lexicon and examples (seeds 1, 3, 5) against a brief grammar and a large table (seeds 2, 4). The ratio of lexicon lines to prose lines runs from one to two (seed 5) to sixteen to one (seed 2).

## What this means for decoding

- **Seed 1** gives up its word classes through prefixes, and its grammar through the clause-initial family. The round 3 team with full task knowledge recovered the role markers, the digits and the task referents in under five minutes.
- **Seeds 2 and 4** will give up their register or frame glyphs first, since they are always clause-initial and there are only three or four of them. After that, separating the dictionary into columns is a clustering problem over clause contexts. Within a column, the single-glyph words are as exposed as any one-meaning vocabulary, and seed 4's invariant layer of field markers and moods is exposed from the start.
- **Seed 3** is the hardest by design: no prefix structure, two forms for every particle, eight words that change meaning by sender, and filler glyphs. A decoder who does not condition on the sender will see the eight dialect words as noise. The 23 idioms are standalone messages and will be frequent, which makes them findable but not interpretable without context.
- **Seed 5** removes prefix structure and doubles every grammar word, but has the smallest vocabulary and the most regular clause shape, so its role markers should fall to frequency alone.

## What this means for round 2

The designs that are hardest to decode are also the hardest to use from a text file. Seeds 2 and 4 require every agent to hold the active register or frame while reading nested material, and a register slip changes every content word in the clause. Seed 3 requires looking up the sender's row for eight common words, including inside quoted material, and relaying another agent's claim requires restating it rather than copying it. Seed 1 has been played once and worked: the team escaped Storm Shelter with 66 messages and no violations. Whether the multi-sense and dialect designs survive contact with a fresh team is the open question that T01 to T04 cannot answer, since gameplay is planned only on seed 1 of each family.

## Open questions worth a run

1. Does a fresh Sol team use seed 2's registers correctly, or do register slips produce silent mistranslation? One playthrough on E02 would answer it.
2. How much harder is seed 3 to decode than seed 1 under the no-task briefing? The sender-specific words are the only speaker-conditioned feature in the set and the only one that resists per-glyph frequency analysis outright.
3. Is the register device a stable attractor for Sol? Two of five seeds found it. A second batch of five would show whether it is a coin flip or a preference.
4. The number vocabulary is the most predictable part of every language and the first thing decoded in round 3. A task that never needs numbers would move the comparison onto the grammar and the camouflage.
