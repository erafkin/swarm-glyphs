# T02: reference-assisted English transcript

Reference-assisted translation using only the frozen Swarmish language and public transcript; not independently certified translation ground truth.

Every public entry retains its original number and sender. Task status is copied verbatim; discarded messages remain unknown. Uncertainty notes are part of the reference.

Raw transcript SHA-256: `72fc7f6f3c7cc3fc17fd6ad2919fd66049d2ee8a1b9e0d65fd09ee87cdfe1ab2`  
Rendered public transcript SHA-256: `666f0099e791f4f32899ef08cc587b17ccf12b879fb0fbad5ea121f9bbff396f`  
Frozen language SHA-256: `9ef04f41c5ae4e074b3befd11b78e05384f24882ffba281dde41ea45c249e3b7`

## [1] task (public status)

**English**

> {"stage":0,"invalid_attempts":0}

**Original**

```text
{"stage":0,"invalid_attempts":0}
```

**Confidence:** high

**Ambiguity:** None recorded.

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "public_task_status",
  "evidence": {
    "language_lines": [],
    "prior_public_ids": []
  },
  "literal_gloss": "{\"stage\":0,\"invalid_attempts\":0}"
}
```

## [2] agent_6 (agent message)

**English**

> I have a thing; [I] want/need you to tell/say.

**Original**

```text
𗏔 𗟎 𗿃 𘉝 𗵵 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      30,
      37,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / want, need / you / tell, say"
}
```

## [3] agent_0 (agent message)

**English**

> I have a “see-tool”; [I] want/need to tell/say.

**Original**

```text
𗏔 𗟎 𗦴 𗚀 𘉝 𗎰
```

**Confidence:** low

**Ambiguity:** ["Tool/object is generic; no particular task object or operation is identified.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      29,
      30,
      36,
      37,
      45,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / see / tool, object / want, need / tell, say"
}
```

## [4] agent_3 (agent message)

**English**

> I have a thing. Do you have a thing?

**Original**

```text
𗏔 𗟎 𗿃 𗄪 𗵵 𗟎 𗿃
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / question marker / you / have, hold / thing"
}
```

## [5] agent_2 (agent message)

**English**

> I have a thing.

**Original**

```text
𗏔 𗟎 𗿃
```

**Confidence:** high

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      29,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing"
}
```

## [6] agent_5 (agent message)

**English**

> I have a thing; [see].

**Original**

```text
𗏔 𗟎 𗿃 𗦴
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      29,
      36,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / see"
}
```

## [7] agent_1 (agent message)

**English**

> Do you have a thing?

**Original**

```text
𗄪 𗵵 𗟎 𗿃
```

**Confidence:** high

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      29,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "question marker / you / have, hold / thing"
}
```

## [8] agent_4 (agent message)

**English**

> I have “thing two”.

**Original**

```text
𗏔 𗟎 𗿃 𗳃
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      29,
      46,
      49,
      52,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / two"
}
```

## [9] agent_1 (agent message)

**English**

> Literal: I / you / thing / tell-say. Do you have a “thing-tool”?

**Original**

```text
𗏔 𗵵 𗿃 𗎰 𗄪 𗵵 𗟎 𗿃 𗚀
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      37,
      45,
      46,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / you / thing / tell, say / question marker / you / have, hold / thing / tool, object"
}
```

## [10] agent_0 (agent message)

**English**

> I have a tool/object; [tell/say].

**Original**

```text
𗏔 𗟎 𗚀 𗎰
```

**Confidence:** medium

**Ambiguity:** ["Tool/object is generic; no particular task object or operation is identified.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      29,
      37,
      45
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / tool, object / tell, say"
}
```

## [11] agent_5 (agent message)

**English**

> I have a thing; [I] want/need us to see.

**Original**

```text
𗏔 𗟎 𗿃 𘉝 𘎌 𗦴
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      11,
      29,
      30,
      36,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / want, need / we / see"
}
```

## [12] agent_4 (agent message)

**English**

> I have “two thing”. Do they have a thing?

**Original**

```text
𗏔 𗟎 𗳃 𗿃 𗄪 𗌈 𗟎 𗿃
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      12,
      19,
      29,
      46,
      49,
      52,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / two / thing / question marker / they, them / have, hold / thing"
}
```

## [13] agent_2 (agent message)

**English**

> I have “thing eight”. Do you know?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗡒
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      31,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / know"
}
```

## [14] agent_6 (agent message)

**English**

> I have a thing; [tell/say]; [I] want/need you to tell/say.

**Original**

```text
𗏔 𗟎 𗿃 𗎰 𘉝 𗵵 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      30,
      37,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / tell, say / want, need / you / tell, say"
}
```

## [15] agent_7 (agent message)

**English**

> I know a thing now. What do you know?

**Original**

```text
𗏔 𗡒 𗿃 𘚜 𗄪 𗵵 𗡒 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      31,
      46,
      71
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / know / thing / now / question marker / you / know / what"
}
```

## [16] agent_0 (agent message)

**English**

> I have “seven thing”.

**Original**

```text
𗏔 𗟎 𗋭 𗿃
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      29,
      46,
      49,
      57,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / seven / thing"
}
```

## [17] agent_5 (agent message)

**English**

> I have a thing; we see.

**Original**

```text
𗏔 𗟎 𗿃 𘎌 𗦴
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      11,
      29,
      36,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / we / see"
}
```

## [18] agent_1 (agent message)

**English**

> Do you know a thing, if [have a thing; do/make]?

**Original**

```text
𗄪 𗵵 𗡒 𗿃 𗗫 𗟎 𗿃 𗉍
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      29,
      31,
      38,
      46,
      77
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "question marker / you / know / thing / if / have, hold / thing / do, make"
}
```

## [19] agent_4 (agent message)

**English**

> I have “two thing”. What do you have?

**Original**

```text
𗏔 𗟎 𗳃 𗿃 𗄪 𗵵 𗟎 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      52,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / two / thing / question marker / you / have, hold / what"
}
```

## [20] agent_2 (agent message)

**English**

> I have “thing eight”. Do you have a thing?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing"
}
```

## [21] agent_6 (agent message)

**English**

> Do you have a thing; [tell/say]?

**Original**

```text
𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      29,
      37,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "question marker / you / have, hold / thing / tell, say"
}
```

## [22] agent_3 (agent message)

**English**

> I have a thing; [tell/say], if you have a thing.

**Original**

```text
𗏔 𗟎 𗿃 𗎰 𗗫 𗵵 𗟎 𗿃
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      46,
      77
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / tell, say / if / you / have, hold / thing"
}
```

## [23] agent_7 (agent message)

**English**

> I have a “thing-tool” now. Do you know a thing?

**Original**

```text
𗏔 𗟎 𗿃 𗚀 𘚜 𗄪 𗵵 𗡒 𗿃
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      31,
      45,
      46,
      71,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / tool, object / now / question marker / you / know / thing"
}
```

## [24] agent_1 (agent message)

**English**

> I have a thing. Who knows a thing?

**Original**

```text
𗏔 𗟎 𗿃 𗄪 𘚺 𗡒 𗿃
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      19,
      24,
      29,
      31,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / question marker / who / know / thing"
}
```

## [25] agent_0 (agent message)

**English**

> I have “seven thing”.

**Original**

```text
𗏔 𗟎 𗋭 𗿃
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      29,
      46,
      49,
      57,
      89
    ],
    "prior_public_ids": [
      16
    ]
  },
  "literal_gloss": "I, me / have, hold / seven / thing"
}
```

## [26] agent_4 (agent message)

**English**

> I have a thing; [I] want/need you to tell/say.

**Original**

```text
𗏔 𗟎 𗿃 𘉝 𗵵 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      30,
      37,
      46
    ],
    "prior_public_ids": [
      2
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / want, need / you / tell, say"
}
```

## [27] agent_5 (agent message)

**English**

> I have a thing; we see.

**Original**

```text
𗏔 𗟎 𗿃 𘎌 𗦴
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      11,
      29,
      36,
      46
    ],
    "prior_public_ids": [
      17
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / we / see"
}
```

## [28] agent_2 (agent message)

**English**

> I have “thing eight”. Do you have many/several things?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗥊
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      46,
      49,
      58,
      60,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / many, several"
}
```

## [29] agent_6 (agent message)

**English**

> I have “thing four”. Do you have a thing?

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗄪 𗵵 𗟎 𗿃
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / four / question marker / you / have, hold / thing"
}
```

## [30] agent_3 (agent message)

**English**

> I have a tool/object, if you have a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𗚀 𗗫 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      45,
      46,
      77
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / tool, object / if / you / have, hold / thing / tell, say"
}
```

## [31] agent_1 (agent message)

**English**

> What do you know?

**Original**

```text
𗄪 𗵵 𗡒 𗣑
```

**Confidence:** high

**Ambiguity:** ["You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      23,
      31
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "question marker / you / know / what"
}
```

## [32] agent_4 (agent message)

**English**

> Do you have a thing; [tell/say]?

**Original**

```text
𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      29,
      37,
      46
    ],
    "prior_public_ids": [
      21
    ]
  },
  "literal_gloss": "question marker / you / have, hold / thing / tell, say"
}
```

## [33] agent_5 (agent message)

**English**

> I have a thing; [I] want/need to see us.

**Original**

```text
𗏔 𗟎 𗿃 𘉝 𗦴 𘎌
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      11,
      29,
      30,
      36,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / want, need / see / we"
}
```

## [34] agent_0 (agent message)

**English**

> I have “seven thing”.

**Original**

```text
𗏔 𗟎 𗋭 𗿃
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      29,
      46,
      49,
      57,
      89
    ],
    "prior_public_ids": [
      16
    ]
  },
  "literal_gloss": "I, me / have, hold / seven / thing"
}
```

## [35] agent_7 (agent message)

**English**

> I have a thing. Do you know a thing?

**Original**

```text
𗏔 𗟎 𗿃 𗄪 𗵵 𗡒 𗿃
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      31,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / question marker / you / know / thing"
}
```

## [36] agent_3 (agent message)

**English**

> I have a thing; [see]; you have a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𗿃 𗦴 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      36,
      37,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / see / you / have, hold / thing / tell, say"
}
```

## [37] agent_6 (agent message)

**English**

> I have a tool/object, if you have a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𗚀 𗗫 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      45,
      46,
      77
    ],
    "prior_public_ids": [
      30
    ]
  },
  "literal_gloss": "I, me / have, hold / tool, object / if / you / have, hold / thing / tell, say"
}
```

## [38] agent_1 (agent message)

**English**

> I have a thing; [tell/say]. Do you have a thing?

**Original**

```text
𗏔 𗟎 𗿃 𗎰 𗄪 𗵵 𗟎 𗿃
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      37,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / tell, say / question marker / you / have, hold / thing"
}
```

## [39] agent_5 (agent message)

**English**

> I have a thing; [I] want/need us to see.

**Original**

```text
𗏔 𗟎 𗿃 𘉝 𘎌 𗦴
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      11,
      29,
      30,
      36,
      46
    ],
    "prior_public_ids": [
      11
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / want, need / we / see"
}
```

## [40] agent_2 (agent message)

**English**

> I have “thing eight”; [I] want/need you to tell/say.

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𘉝 𗵵 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      30,
      37,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / eight / want, need / you / tell, say"
}
```

## [41] agent_4 (agent message)

**English**

> Do you have what thing; [tell/say]?

**Original**

```text
𗄪 𗵵 𗟎 𗿃 𗣑 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      23,
      29,
      37,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "question marker / you / have, hold / thing / what / tell, say"
}
```

## [42] agent_7 (agent message)

**English**

> I have a tool/object. What do you know?

**Original**

```text
𗏔 𗟎 𗚀 𗄪 𗵵 𗡒 𗣑
```

**Confidence:** medium

**Ambiguity:** ["Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      31,
      45
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / tool, object / question marker / you / know / what"
}
```

## [43] agent_0 (agent message)

**English**

> I have “thing seven”; you tell/say.

**Original**

```text
𗏔 𗟎 𗿃 𗋭 𗵵 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      46,
      49,
      57,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / seven / you / tell, say"
}
```

## [44] agent_3 (agent message)

**English**

> I have a thing. Do you have a thing; [tell/say]?

**Original**

```text
𗏔 𗟎 𗿃 𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      37,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / question marker / you / have, hold / thing / tell, say"
}
```

## [45] agent_1 (agent message)

**English**

> I have a tool/object. Do you have a tool/object?

**Original**

```text
𗏔 𗟎 𗚀 𗄪 𗵵 𗟎 𗚀
```

**Confidence:** medium

**Ambiguity:** ["Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      45
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / tool, object / question marker / you / have, hold / tool, object"
}
```

## [46] agent_6 (agent message)

**English**

> I have “thing four”.

**Original**

```text
𗏔 𗟎 𗿃 𘙠
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / four"
}
```

## [47] agent_5 (agent message)

**English**

> I have a thing; [I] want/need us to see.

**Original**

```text
𗏔 𗟎 𗿃 𘉝 𘎌 𗦴
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      11,
      29,
      30,
      36,
      46
    ],
    "prior_public_ids": [
      11
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / want, need / we / see"
}
```

## [48] agent_4 (agent message)

**English**

> I have two. Do you have a thing?

**Original**

```text
𗏔 𗟎 𗳃 𗄪 𗵵 𗟎 𗿃
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      46,
      49,
      52,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / two / question marker / you / have, hold / thing"
}
```

## [49] agent_2 (agent message)

**English**

> I have “thing eight”. Do you have a thing; [tell/say]?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      37,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / tell, say"
}
```

## [50] agent_7 (agent message)

**English**

> What tool/object do you have?

**Original**

```text
𗄪 𗵵 𗟎 𗚀 𗣑
```

**Confidence:** medium

**Ambiguity:** ["Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      23,
      29,
      45
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "question marker / you / have, hold / tool, object / what"
}
```

## [51] agent_0 (agent message)

**English**

> I have “seven thing”; [I] want/need us to see.

**Original**

```text
𗏔 𗟎 𗋭 𗿃 𘉝 𘎌 𗦴
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      11,
      29,
      30,
      36,
      46,
      49,
      57,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / seven / thing / want, need / we / see"
}
```

## [52] agent_3 (agent message)

**English**

> Do you have a thing; [see]?

**Original**

```text
𗄪 𗵵 𗟎 𗿃 𗦴
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      29,
      36,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "question marker / you / have, hold / thing / see"
}
```

## [53] agent_1 (agent message)

**English**

> Do you have a “thing-tool”?

**Original**

```text
𗄪 𗵵 𗟎 𗿃 𗚀
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      29,
      45,
      46,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "question marker / you / have, hold / thing / tool, object"
}
```

## [54] agent_6 (agent message)

**English**

> I have “thing four”.

**Original**

```text
𗏔 𗟎 𗿃 𘙠
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      46
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / four"
}
```

## [55] agent_4 (agent message)

**English**

> I have “two thing”. What do you have?

**Original**

```text
𗏔 𗟎 𗳃 𗿃 𗄪 𗵵 𗟎 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      52,
      89
    ],
    "prior_public_ids": [
      19
    ]
  },
  "literal_gloss": "I, me / have, hold / two / thing / question marker / you / have, hold / what"
}
```

## [56] agent_5 (agent message)

**English**

> I have a thing; we see.

**Original**

```text
𗏔 𗟎 𗿃 𘎌 𗦴
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      11,
      29,
      36,
      46
    ],
    "prior_public_ids": [
      17
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / we / see"
}
```

## [57] agent_2 (agent message)

**English**

> I have “thing eight”. Do you have a thing; [see]?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗦴
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      36,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / see"
}
```

## [58] agent_7 (agent message)

**English**

> Who has a thing; [tell/say]?

**Original**

```text
𗄪 𘚺 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      19,
      24,
      29,
      37,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "question marker / who / have, hold / thing / tell, say"
}
```

## [59] agent_0 (agent message)

**English**

> I tell you “seven thing”; [tell/say]; you see.

**Original**

```text
𗏔 𗎰 𗵵 𗋭 𗿃 𗎰 𗵵 𗦴
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      36,
      37,
      46,
      49,
      57,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / tell, say / you / seven / thing / tell, say / you / see"
}
```

## [60] agent_3 (agent message)

**English**

> Do you have a thing; [see]?

**Original**

```text
𗄪 𗵵 𗟎 𗿃 𗦴
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      29,
      36,
      46
    ],
    "prior_public_ids": [
      52
    ]
  },
  "literal_gloss": "question marker / you / have, hold / thing / see"
}
```

## [61] agent_6 (agent message)

**English**

> “Thing four”.

**Original**

```text
𗿃 𘙠
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "thing / four"
}
```

## [62] agent_4 (agent message)

**English**

> What do you have?

**Original**

```text
𗄪 𗵵 𗟎 𗣑
```

**Confidence:** high

**Ambiguity:** ["You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      23,
      29
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "question marker / you / have, hold / what"
}
```

## [63] agent_2 (agent message)

**English**

> I have “thing eight”. Do you have a thing?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      20
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing"
}
```

## [64] agent_0 (agent message)

**English**

> Do you know a thing; [tell/say]?

**Original**

```text
𗄪 𗵵 𗡒 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      31,
      37,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "question marker / you / know / thing / tell, say"
}
```

## [65] agent_5 (agent message)

**English**

> I have a thing; [I] want/need us to do/make.

**Original**

```text
𗏔 𗟎 𗿃 𘉝 𘎌 𗉍
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      11,
      29,
      30,
      38,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / want, need / we / do, make"
}
```

## [66] agent_7 (agent message)

**English**

> I have a tool/object, if you know what.

**Original**

```text
𗏔 𗟎 𗚀 𗗫 𗵵 𗡒 𗣑
```

**Confidence:** low

**Ambiguity:** ["Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      23,
      29,
      31,
      45,
      77
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / tool, object / if / you / know / what"
}
```

## [67] agent_1 (agent message)

**English**

> I have a thing, if you have a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𗿃 𗗫 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      46,
      77
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / if / you / have, hold / thing / tell, say"
}
```

## [68] agent_3 (agent message)

**English**

> I want/need you to see a thing, if you have a thing.

**Original**

```text
𗏔 𘉝 𗵵 𗦴 𗿃 𗗫 𗵵 𗟎 𗿃
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      30,
      36,
      46,
      77
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / want, need / you / see / thing / if / you / have, hold / thing"
}
```

## [69] agent_4 (agent message)

**English**

> I have a thing; [tell/say], if you have a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𗿃 𗎰 𗗫 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      46,
      77
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / tell, say / if / you / have, hold / thing / tell, say"
}
```

## [70] agent_0 (agent message)

**English**

> I have “seven thing”. Who has a thing?

**Original**

```text
𗏔 𗟎 𗋭 𗿃 𗄪 𘚺 𗟎 𗿃
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      19,
      24,
      29,
      46,
      49,
      57,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / seven / thing / question marker / who / have, hold / thing"
}
```

## [71] agent_2 (agent message)

**English**

> I have “tool/object eight”. Do you have a thing; [tell/say]?

**Original**

```text
𗏔 𗟎 𗚀 𗸪 𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      37,
      45,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / tool, object / eight / question marker / you / have, hold / thing / tell, say"
}
```

## [72] agent_6 (agent message)

**English**

> I have “thing four”. Do you see?

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗄪 𗵵 𗦴
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      36,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / four / question marker / you / see"
}
```

## [73] agent_7 (agent message)

**English**

> Do you know a “thing-tool”?

**Original**

```text
𗄪 𗵵 𗡒 𗿃 𗚀
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      31,
      45,
      46,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "question marker / you / know / thing / tool, object"
}
```

## [74] agent_1 (agent message)

**English**

> What thing do you have?

**Original**

```text
𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      23,
      29,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "question marker / you / have, hold / thing / what"
}
```

## [75] agent_3 (agent message)

**English**

> What thing do you have?

**Original**

```text
𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      23,
      29,
      46
    ],
    "prior_public_ids": [
      74
    ]
  },
  "literal_gloss": "question marker / you / have, hold / thing / what"
}
```

## [76] agent_5 (agent message)

**English**

> Do you have a thing; [tell/say]?

**Original**

```text
𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      29,
      37,
      46
    ],
    "prior_public_ids": [
      21
    ]
  },
  "literal_gloss": "question marker / you / have, hold / thing / tell, say"
}
```

## [77] agent_0 (agent message)

**English**

> I have “seven thing”, if you have a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𗋭 𗿃 𗗫 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      46,
      49,
      57,
      77,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / seven / thing / if / you / have, hold / thing / tell, say"
}
```

## [78] agent_2 (agent message)

**English**

> I have a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      29,
      37,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / tell, say"
}
```

## [79] agent_4 (agent message)

**English**

> I have “two thing”. Do you have a thing; [tell/say]?

**Original**

```text
𗏔 𗟎 𗳃 𗿃 𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      37,
      46,
      49,
      52,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / two / thing / question marker / you / have, hold / thing / tell, say"
}
```

## [80] agent_1 (agent message)

**English**

> Do you have a thing; [tell/say]?

**Original**

```text
𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      29,
      37,
      46
    ],
    "prior_public_ids": [
      21
    ]
  },
  "literal_gloss": "question marker / you / have, hold / thing / tell, say"
}
```

## [81] agent_6 (agent message)

**English**

> I have “thing four”. Who has a thing?

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗄪 𘚺 𗟎 𗿃
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      19,
      24,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / four / question marker / who / have, hold / thing"
}
```

## [82] agent_7 (agent message)

**English**

> Do you have a tool/object, if I know a thing, if you know a thing?

**Original**

```text
𗄪 𗵵 𗟎 𗚀 𗗫 𗏔 𗡒 𗿃 𗗫 𗵵 𗡒 𗿃
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      31,
      45,
      46,
      77
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "question marker / you / have, hold / tool, object / if / I, me / know / thing / if / you / know / thing"
}
```

## [83] agent_5 (agent message)

**English**

> I want/need you to see a thing.

**Original**

```text
𗏔 𘉝 𗵵 𗦴 𗿃
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      30,
      36,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / want, need / you / see / thing"
}
```

## [84] agent_3 (agent message)

**English**

> I have a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      29,
      37,
      46
    ],
    "prior_public_ids": [
      78
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / tell, say"
}
```

## [85] agent_0 (agent message)

**English**

> I have “seven thing”. Do you have a thing; [tell/say]?

**Original**

```text
𗏔 𗟎 𗋭 𗿃 𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      37,
      46,
      49,
      57,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / seven / thing / question marker / you / have, hold / thing / tell, say"
}
```

## [86] agent_1 (agent message)

**English**

> I have a thing; [tell/say]. Do you have a thing; [tell/say]?

**Original**

```text
𗏔 𗟎 𗿃 𗎰 𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      37,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / tell, say / question marker / you / have, hold / thing / tell, say"
}
```

## [87] agent_4 (agent message)

**English**

> I have “two thing”. Do you have “thing two”?

**Original**

```text
𗏔 𗟎 𗳃 𗿃 𗄪 𗵵 𗟎 𗿃 𗳃
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      46,
      49,
      52,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / two / thing / question marker / you / have, hold / thing / two"
}
```

## [88] agent_6 (agent message)

**English**

> I have four. Do you have a thing?

**Original**

```text
𗏔 𗟎 𘙠 𗄪 𗵵 𗟎 𗿃
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / question marker / you / have, hold / thing"
}
```

## [89] agent_2 (agent message)

**English**

> I have a tool/object, if you have a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𗚀 𗗫 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      45,
      46,
      77
    ],
    "prior_public_ids": [
      30
    ]
  },
  "literal_gloss": "I, me / have, hold / tool, object / if / you / have, hold / thing / tell, say"
}
```

## [90] agent_5 (agent message)

**English**

> What do you have?

**Original**

```text
𗄪 𗵵 𗟎 𗣑
```

**Confidence:** high

**Ambiguity:** ["You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      23,
      29
    ],
    "prior_public_ids": [
      62
    ]
  },
  "literal_gloss": "question marker / you / have, hold / what"
}
```

## [91] agent_7 (agent message)

**English**

> I have a thing, if you have a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𗿃 𗗫 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      46,
      77
    ],
    "prior_public_ids": [
      67
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / if / you / have, hold / thing / tell, say"
}
```

## [92] agent_3 (agent message)

**English**

> Do you have a thing; [tell/say]?

**Original**

```text
𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      29,
      37,
      46
    ],
    "prior_public_ids": [
      21
    ]
  },
  "literal_gloss": "question marker / you / have, hold / thing / tell, say"
}
```

## [93] agent_1 (agent message)

**English**

> I have a thing. Do you have a “thing-tool”?

**Original**

```text
𗏔 𗟎 𗿃 𗄪 𗵵 𗟎 𗿃 𗚀
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      45,
      46,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / question marker / you / have, hold / thing / tool, object"
}
```

## [94] agent_0 (agent message)

**English**

> I have “seven thing”, if you have a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𗋭 𗿃 𗗫 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      46,
      49,
      57,
      77,
      89
    ],
    "prior_public_ids": [
      77
    ]
  },
  "literal_gloss": "I, me / have, hold / seven / thing / if / you / have, hold / thing / tell, say"
}
```

## [95] agent_4 (agent message)

**English**

> I have “two thing”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗳃 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      52,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / two / thing / question marker / you / have, hold / thing / what"
}
```

## [96] agent_2 (agent message)

**English**

> I have “tool/object eight”. Do you have a tool/object?

**Original**

```text
𗏔 𗟎 𗚀 𗸪 𗄪 𗵵 𗟎 𗚀
```

**Confidence:** medium

**Ambiguity:** ["Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      45,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / tool, object / eight / question marker / you / have, hold / tool, object"
}
```

## [97] agent_6 (agent message)

**English**

> I have “four thing”. What do you have; [tell/say]?

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗄪 𗵵 𗟎 𗣑 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / thing / question marker / you / have, hold / what / tell, say"
}
```

## [98] agent_5 (agent message)

**English**

> Do you have a thing; [tell/say]?

**Original**

```text
𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      29,
      37,
      46
    ],
    "prior_public_ids": [
      21
    ]
  },
  "literal_gloss": "question marker / you / have, hold / thing / tell, say"
}
```

## [99] agent_1 (agent message)

**English**

> I have a thing. What do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗄪 𗵵 𗟎 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / question marker / you / have, hold / what"
}
```

## [100] agent_0 (agent message)

**English**

> I have “seven thing”, if you have a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𗋭 𗿃 𗗫 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      46,
      49,
      57,
      77,
      89
    ],
    "prior_public_ids": [
      77
    ]
  },
  "literal_gloss": "I, me / have, hold / seven / thing / if / you / have, hold / thing / tell, say"
}
```

## [101] agent_6 (agent message)

**English**

> I have “thing four”. What do you have?

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗄪 𗵵 𗟎 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / four / question marker / you / have, hold / what"
}
```

## [102] agent_2 (agent message)

**English**

> I have a thing, if you have a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𗿃 𗗫 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      46,
      77
    ],
    "prior_public_ids": [
      67
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / if / you / have, hold / thing / tell, say"
}
```

## [103] agent_4 (agent message)

**English**

> I have a thing; [tell/say]. Do you have a “thing-tool”?

**Original**

```text
𗏔 𗟎 𗿃 𗎰 𗄪 𗵵 𗟎 𗿃 𗚀
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      37,
      45,
      46,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / tell, say / question marker / you / have, hold / thing / tool, object"
}
```

## [104] agent_3 (agent message)

**English**

> I have a thing; [I] want/need you to tell/say.

**Original**

```text
𗏔 𗟎 𗿃 𘉝 𗵵 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      30,
      37,
      46
    ],
    "prior_public_ids": [
      2
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / want, need / you / tell, say"
}
```

## [105] agent_7 (agent message)

**English**

> I have a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      29,
      37,
      46
    ],
    "prior_public_ids": [
      78
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / tell, say"
}
```

## [106] agent_0 (agent message)

**English**

> I have “seven thing”, if you have a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𗋭 𗿃 𗗫 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      46,
      49,
      57,
      77,
      89
    ],
    "prior_public_ids": [
      77
    ]
  },
  "literal_gloss": "I, me / have, hold / seven / thing / if / you / have, hold / thing / tell, say"
}
```

## [107] agent_1 (agent message)

**English**

> I have a thing; [I] want/need you to tell/say.

**Original**

```text
𗏔 𗟎 𗿃 𘉝 𗵵 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      30,
      37,
      46
    ],
    "prior_public_ids": [
      2
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / want, need / you / tell, say"
}
```

## [108] agent_2 (agent message)

**English**

> I have a tool/object, if you have a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𗚀 𗗫 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      45,
      46,
      77
    ],
    "prior_public_ids": [
      30
    ]
  },
  "literal_gloss": "I, me / have, hold / tool, object / if / you / have, hold / thing / tell, say"
}
```

## [109] agent_6 (agent message)

**English**

> I have “four thing”; you tell/say.

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗵵 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / thing / you / tell, say"
}
```

## [110] agent_7 (agent message)

**English**

> I have a tool/object; [you / tool-object].

**Original**

```text
𗏔 𗟎 𗚀 𗵵 𗚀
```

**Confidence:** low

**Ambiguity:** ["Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      45
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / tool, object / you / tool, object"
}
```

## [111] agent_3 (agent message)

**English**

> I want/need you to tell/say what “thing-tool”.

**Original**

```text
𗏔 𘉝 𗵵 𗎰 𗣑 𗿃 𗚀
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      23,
      30,
      37,
      45,
      46,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / want, need / you / tell, say / what / thing / tool, object"
}
```

## [112] agent_4 (agent message)

**English**

> Do you have a thing; [tell/say]?

**Original**

```text
𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      29,
      37,
      46
    ],
    "prior_public_ids": [
      21
    ]
  },
  "literal_gloss": "question marker / you / have, hold / thing / tell, say"
}
```

## [113] agent_0 (agent message)

**English**

> I have “seven thing”. What do you have; [tell/say]?

**Original**

```text
𗏔 𗟎 𗋭 𗿃 𗄪 𗵵 𗟎 𗣑 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      46,
      49,
      57,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / seven / thing / question marker / you / have, hold / what / tell, say"
}
```

## [114] agent_2 (agent message)

**English**

> I have “eight thing”; you tell/say. Do you have a thing; [tell/say]?

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗵵 𗎰 𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      37,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / eight / thing / you / tell, say / question marker / you / have, hold / thing / tell, say"
}
```

## [115] agent_6 (agent message)

**English**

> I have “thing four”. Do you have a thing; [tell/say]?

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / four / question marker / you / have, hold / thing / tell, say"
}
```

## [116] agent_3 (agent message)

**English**

> I have a thing, if you have a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𗿃 𗗫 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      46,
      77
    ],
    "prior_public_ids": [
      67
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / if / you / have, hold / thing / tell, say"
}
```

## [117] agent_4 (agent message)

**English**

> Do you have a thing; [tell/say]? I have “two thing”.

**Original**

```text
𗄪 𗵵 𗟎 𗿃 𗎰 𗏔 𗟎 𗳃 𗿃
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      37,
      46,
      49,
      52,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "question marker / you / have, hold / thing / tell, say / I, me / have, hold / two / thing"
}
```

## [118] agent_1 (agent message)

**English**

> I have a thing, if you know a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𗿃 𗗫 𗵵 𗡒 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      31,
      37,
      46,
      77
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / if / you / know / thing / tell, say"
}
```

## [119] agent_0 (agent message)

**English**

> I have “seven thing”. Do you have a thing; [tell/say]?

**Original**

```text
𗏔 𗟎 𗋭 𗿃 𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      37,
      46,
      49,
      57,
      89
    ],
    "prior_public_ids": [
      85
    ]
  },
  "literal_gloss": "I, me / have, hold / seven / thing / question marker / you / have, hold / thing / tell, say"
}
```

## [120] agent_6 (agent message)

**English**

> I have “four thing”; [tell/say].

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / thing / tell, say"
}
```

## [121] agent_2 (agent message)

**English**

> I have a thing; [I] want/need you to tell/say.

**Original**

```text
𗏔 𗟎 𗿃 𘉝 𗵵 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      30,
      37,
      46
    ],
    "prior_public_ids": [
      2
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / want, need / you / tell, say"
}
```

## [122] agent_0 (agent message)

**English**

> I have “seven thing”.

**Original**

```text
𗏔 𗟎 𗋭 𗿃
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      29,
      46,
      49,
      57,
      89
    ],
    "prior_public_ids": [
      16
    ]
  },
  "literal_gloss": "I, me / have, hold / seven / thing"
}
```

## [123] agent_1 (agent message)

**English**

> I have a thing; [tell/say]. Do you have a thing; [tell/say]?

**Original**

```text
𗏔 𗟎 𗿃 𗎰 𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      37,
      46
    ],
    "prior_public_ids": [
      86
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / tell, say / question marker / you / have, hold / thing / tell, say"
}
```

## [124] agent_3 (agent message)

**English**

> I have a tool/object, if you have a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𗚀 𗗫 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      45,
      46,
      77
    ],
    "prior_public_ids": [
      30
    ]
  },
  "literal_gloss": "I, me / have, hold / tool, object / if / you / have, hold / thing / tell, say"
}
```

## [125] agent_6 (agent message)

**English**

> I have “four thing”. Do you have a thing; [tell/say]?

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / thing / question marker / you / have, hold / thing / tell, say"
}
```

## [126] agent_2 (agent message)

**English**

> I have “tool/object eight”.

**Original**

```text
𗏔 𗟎 𗚀 𗸪
```

**Confidence:** medium

**Ambiguity:** ["Tool/object is generic; no particular task object or operation is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      29,
      45,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / tool, object / eight"
}
```

## [127] agent_0 (agent message)

**English**

> I have “seven thing”; [tell/say].

**Original**

```text
𗏔 𗟎 𗋭 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      29,
      37,
      46,
      49,
      57,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / seven / thing / tell, say"
}
```

## [128] agent_1 (agent message)

**English**

> I have a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      29,
      37,
      46
    ],
    "prior_public_ids": [
      78
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / tell, say"
}
```

## [129] agent_3 (agent message)

**English**

> I have a thing. Do you have a thing; [tell/say]?

**Original**

```text
𗏔 𗟎 𗿃 𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      37,
      46
    ],
    "prior_public_ids": [
      44
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / question marker / you / have, hold / thing / tell, say"
}
```

## [130] agent_4 (agent message)

**English**

> I have “two thing”.

**Original**

```text
𗏔 𗟎 𗳃 𗿃
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      29,
      46,
      49,
      52,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / two / thing"
}
```

## [131] agent_6 (agent message)

**English**

> I have “four thing”; [tell/say].

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      120
    ]
  },
  "literal_gloss": "I, me / have, hold / four / thing / tell, say"
}
```

## [132] agent_2 (agent message)

**English**

> I have “thing eight”. Do you have a thing; [tell/say]?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      37,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      49
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / tell, say"
}
```

## [133] agent_0 (agent message)

**English**

> I have “thing seven”; you tell/say.

**Original**

```text
𗏔 𗟎 𗿃 𗋭 𗵵 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      46,
      49,
      57,
      89
    ],
    "prior_public_ids": [
      43
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / seven / you / tell, say"
}
```

## [134] agent_3 (agent message)

**English**

> I have a “thing-tool”, if you have a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𗿃 𗚀 𗗫 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      45,
      46,
      77,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / tool, object / if / you / have, hold / thing / tell, say"
}
```

## [135] agent_6 (agent message)

**English**

> Literal: I / thing / see / four / you / thing / tell-say.

**Original**

```text
𗏔 𗿃 𗦴 𘙠 𗵵 𗿃 𗎰
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      36,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / thing / see / four / you / thing / tell, say"
}
```

## [136] agent_2 (agent message)

**English**

> I have “thing eight”. Do you have a thing; [tell/say]?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      37,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      49
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / tell, say"
}
```

## [137] agent_0 (agent message)

**English**

> I have “seven thing”; [tell/say].

**Original**

```text
𗏔 𗟎 𗋭 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      29,
      37,
      46,
      49,
      57,
      89
    ],
    "prior_public_ids": [
      127
    ]
  },
  "literal_gloss": "I, me / have, hold / seven / thing / tell, say"
}
```

## [138] agent_1 (agent message)

**English**

> I see a thing.

**Original**

```text
𗏔 𗦴 𗿃
```

**Confidence:** high

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      36,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / see / thing"
}
```

## [139] agent_3 (agent message)

**English**

> I want/need a thing; you tell/say.

**Original**

```text
𗏔 𘉝 𗿃 𗵵 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      30,
      37,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / want, need / thing / you / tell, say"
}
```

## [140] agent_4 (agent message)

**English**

> I have “thing two”. Do you have a thing?

**Original**

```text
𗏔 𗟎 𗿃 𗳃 𗄪 𗵵 𗟎 𗿃
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      46,
      49,
      52,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / two / question marker / you / have, hold / thing"
}
```

## [141] agent_6 (agent message)

**English**

> I have “four thing”. What do you have; [tell/say]?

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗄪 𗵵 𗟎 𗣑 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      97
    ]
  },
  "literal_gloss": "I, me / have, hold / four / thing / question marker / you / have, hold / what / tell, say"
}
```

## [142] agent_2 (agent message)

**English**

> I have “eight thing”. Do you have a thing; [tell/say]?

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      37,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / eight / thing / question marker / you / have, hold / thing / tell, say"
}
```

## [143] agent_0 (agent message)

**English**

> I have “seven thing”; [tell/say]. Do you have a thing; [tell/say]?

**Original**

```text
𗏔 𗟎 𗋭 𗿃 𗎰 𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      37,
      46,
      49,
      57,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / seven / thing / tell, say / question marker / you / have, hold / thing / tell, say"
}
```

## [144] agent_3 (agent message)

**English**

> I have a tool/object. What do you have?

**Original**

```text
𗏔 𗟎 𗚀 𗄪 𗵵 𗟎 𗣑
```

**Confidence:** medium

**Ambiguity:** ["Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      45
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / tool, object / question marker / you / have, hold / what"
}
```

## [145] agent_4 (agent message)

**English**

> What do you have; [tell/say]?

**Original**

```text
𗄪 𗵵 𗟎 𗣑 𗎰
```

**Confidence:** medium

**Ambiguity:** ["You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      23,
      29,
      37
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "question marker / you / have, hold / what / tell, say"
}
```

## [146] agent_2 (agent message)

**English**

> I have “eight thing”. Do you have a thing?

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗄪 𗵵 𗟎 𗿃
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / eight / thing / question marker / you / have, hold / thing"
}
```

## [147] agent_3 (agent message)

**English**

> Do you have a thing; [tell/say]?

**Original**

```text
𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      29,
      37,
      46
    ],
    "prior_public_ids": [
      21
    ]
  },
  "literal_gloss": "question marker / you / have, hold / thing / tell, say"
}
```

## [148] agent_0 (agent message)

**English**

> I have “seven thing”. Do you have a thing; [tell/say]?

**Original**

```text
𗏔 𗟎 𗋭 𗿃 𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      37,
      46,
      49,
      57,
      89
    ],
    "prior_public_ids": [
      85
    ]
  },
  "literal_gloss": "I, me / have, hold / seven / thing / question marker / you / have, hold / thing / tell, say"
}
```

## [149] agent_6 (agent message)

**English**

> I have “four thing”. Do you have a thing; [tell/say]?

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      125
    ]
  },
  "literal_gloss": "I, me / have, hold / four / thing / question marker / you / have, hold / thing / tell, say"
}
```

## [150] agent_2 (agent message)

**English**

> I have “eight thing”. Do you have a thing?

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗄪 𗵵 𗟎 𗿃
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      146
    ]
  },
  "literal_gloss": "I, me / have, hold / eight / thing / question marker / you / have, hold / thing"
}
```

## [151] agent_3 (agent message)

**English**

> I have a thing. What do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗄪 𗵵 𗟎 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46
    ],
    "prior_public_ids": [
      99
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / question marker / you / have, hold / what"
}
```

## [152] agent_0 (agent message)

**English**

> I have “seven thing”, if you have a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𗋭 𗿃 𗗫 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      46,
      49,
      57,
      77,
      89
    ],
    "prior_public_ids": [
      77
    ]
  },
  "literal_gloss": "I, me / have, hold / seven / thing / if / you / have, hold / thing / tell, say"
}
```

## [153] agent_6 (agent message)

**English**

> I have “four thing”; [tell/say]. Do you have a thing; [tell/say]?

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗎰 𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / thing / tell, say / question marker / you / have, hold / thing / tell, say"
}
```

## [154] agent_2 (agent message)

**English**

> I have “thing eight”. Do you have a thing; [tell/say]?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      37,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      49
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / tell, say"
}
```

## [155] agent_7 (agent message)

**English**

> I see a thing; people/agents tell/say; you have a thing [question marker at end].

**Original**

```text
𗏔 𗦴 𗿃 𗉜 𗽃 𗎰 𗵵 𗟎 𗿃 𗄪
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement.",
    "The question marker appears at the end, whereas reference line 19 places it at the start."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      36,
      37,
      41,
      46,
      47
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / see / thing / person, agent / plural marker / tell, say / you / have, hold / thing / question marker"
}
```

## [156] agent_3 (agent message)

**English**

> I have a thing. Do you have a thing; [tell/say]?

**Original**

```text
𗏔 𗟎 𗿃 𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      37,
      46
    ],
    "prior_public_ids": [
      44
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / question marker / you / have, hold / thing / tell, say"
}
```

## [157] agent_0 (agent message)

**English**

> I have “seven thing”; [tell/say].

**Original**

```text
𗏔 𗟎 𗋭 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      29,
      37,
      46,
      49,
      57,
      89
    ],
    "prior_public_ids": [
      127
    ]
  },
  "literal_gloss": "I, me / have, hold / seven / thing / tell, say"
}
```

## [158] agent_6 (agent message)

**English**

> I have “four thing”; [I] want/need you to tell/say.

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𘉝 𗵵 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      30,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / thing / want, need / you / tell, say"
}
```

## [159] agent_2 (agent message)

**English**

> I have “thing eight”; you tell/say.

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗵵 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / eight / you / tell, say"
}
```

## [160] agent_7 (agent message)

**English**

> Who has a thing; [tell/say]?

**Original**

```text
𗄪 𘚺 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      19,
      24,
      29,
      37,
      46
    ],
    "prior_public_ids": [
      58
    ]
  },
  "literal_gloss": "question marker / who / have, hold / thing / tell, say"
}
```

## [161] agent_3 (agent message)

**English**

> Do you have what thing; [tell/say]?

**Original**

```text
𗄪 𗵵 𗟎 𗿃 𗣑 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      23,
      29,
      37,
      46
    ],
    "prior_public_ids": [
      41
    ]
  },
  "literal_gloss": "question marker / you / have, hold / thing / what / tell, say"
}
```

## [162] agent_0 (agent message)

**English**

> I have “seven thing”. Do you have a thing?

**Original**

```text
𗏔 𗟎 𗋭 𗿃 𗄪 𗵵 𗟎 𗿃
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      46,
      49,
      57,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / seven / thing / question marker / you / have, hold / thing"
}
```

## [163] agent_2 (agent message)

**English**

> I have “eight thing”; you tell/say.

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗵵 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / eight / thing / you / tell, say"
}
```

## [164] agent_6 (agent message)

**English**

> I have “four thing”; you tell/say.

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗵵 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      109
    ]
  },
  "literal_gloss": "I, me / have, hold / four / thing / you / tell, say"
}
```

## [165] agent_7 (agent message)

**English**

> Who has a thing?

**Original**

```text
𗄪 𘚺 𗟎 𗿃
```

**Confidence:** high

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      19,
      24,
      29,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "question marker / who / have, hold / thing"
}
```

## [166] agent_3 (agent message)

**English**

> I want/need you to tell/say what.

**Original**

```text
𗏔 𘉝 𗵵 𗎰 𗣑
```

**Confidence:** medium

**Ambiguity:** ["You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      23,
      30,
      37
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / want, need / you / tell, say / what"
}
```

## [167] agent_0 (agent message)

**English**

> I have “seven thing”. Do you have a thing; [tell/say]?

**Original**

```text
𗏔 𗟎 𗋭 𗿃 𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      37,
      46,
      49,
      57,
      89
    ],
    "prior_public_ids": [
      85
    ]
  },
  "literal_gloss": "I, me / have, hold / seven / thing / question marker / you / have, hold / thing / tell, say"
}
```

## [168] agent_2 (agent message)

**English**

> I have “eight tool/object”. Do you have a tool/object?

**Original**

```text
𗏔 𗟎 𗸪 𗚀 𗄪 𗵵 𗟎 𗚀
```

**Confidence:** medium

**Ambiguity:** ["Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      45,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / eight / tool, object / question marker / you / have, hold / tool, object"
}
```

## [169] agent_7 (agent message)

**English**

> I have a tool/object, if you have a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𗚀 𗗫 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      45,
      46,
      77
    ],
    "prior_public_ids": [
      30
    ]
  },
  "literal_gloss": "I, me / have, hold / tool, object / if / you / have, hold / thing / tell, say"
}
```

## [170] agent_6 (agent message)

**English**

> I have “four thing”. Do you have a thing; [tell/say]?

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      125
    ]
  },
  "literal_gloss": "I, me / have, hold / four / thing / question marker / you / have, hold / thing / tell, say"
}
```

## [171] agent_3 (agent message)

**English**

> What thing do you have?

**Original**

```text
𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      23,
      29,
      46
    ],
    "prior_public_ids": [
      74
    ]
  },
  "literal_gloss": "question marker / you / have, hold / thing / what"
}
```

## [172] agent_0 (agent message)

**English**

> I have “seven thing”; [tell/say]. Do you have a thing; [tell/say]?

**Original**

```text
𗏔 𗟎 𗋭 𗿃 𗎰 𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      37,
      46,
      49,
      57,
      89
    ],
    "prior_public_ids": [
      143
    ]
  },
  "literal_gloss": "I, me / have, hold / seven / thing / tell, say / question marker / you / have, hold / thing / tell, say"
}
```

## [173] agent_2 (agent message)

**English**

> I have “thing eight”.

**Original**

```text
𗏔 𗟎 𗿃 𗸪
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / eight"
}
```

## [174] agent_4 (agent message)

**English**

> I have “two thing”.

**Original**

```text
𗏔 𗟎 𗳃 𗿃
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      29,
      46,
      49,
      52,
      89
    ],
    "prior_public_ids": [
      130
    ]
  },
  "literal_gloss": "I, me / have, hold / two / thing"
}
```

## [175] agent_7 (agent message)

**English**

> I have a thing, if you have a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𗿃 𗗫 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      46,
      77
    ],
    "prior_public_ids": [
      67
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / if / you / have, hold / thing / tell, say"
}
```

## [176] agent_6 (agent message)

**English**

> I have “four thing”. What do you have?

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗄪 𗵵 𗟎 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / thing / question marker / you / have, hold / what"
}
```

## [177] agent_0 (agent message)

**English**

> I have “seven thing”. Who has a thing?

**Original**

```text
𗏔 𗟎 𗋭 𗿃 𗄪 𘚺 𗟎 𗿃
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      19,
      24,
      29,
      46,
      49,
      57,
      89
    ],
    "prior_public_ids": [
      70
    ]
  },
  "literal_gloss": "I, me / have, hold / seven / thing / question marker / who / have, hold / thing"
}
```

## [178] agent_7 (agent message)

**English**

> Do you have a thing; [tell/say]?

**Original**

```text
𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      29,
      37,
      46
    ],
    "prior_public_ids": [
      21
    ]
  },
  "literal_gloss": "question marker / you / have, hold / thing / tell, say"
}
```

## [179] agent_2 (agent message)

**English**

> I have “thing eight”.

**Original**

```text
𗏔 𗟎 𗿃 𗸪
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      173
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / eight"
}
```

## [180] agent_4 (agent message)

**English**

> I have “two thing”. Do you see a thing?

**Original**

```text
𗏔 𗟎 𗳃 𗿃 𗄪 𗵵 𗦴 𗿃
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      36,
      46,
      49,
      52,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / two / thing / question marker / you / see / thing"
}
```

## [181] agent_6 (agent message)

**English**

> I have “four thing”, if you have a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗗫 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      46,
      49,
      54,
      77,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / thing / if / you / have, hold / thing / tell, say"
}
```

## [182] agent_0 (agent message)

**English**

> I have “seven thing”, if you have a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𗋭 𗿃 𗗫 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      46,
      49,
      57,
      77,
      89
    ],
    "prior_public_ids": [
      77
    ]
  },
  "literal_gloss": "I, me / have, hold / seven / thing / if / you / have, hold / thing / tell, say"
}
```

## [183] agent_2 (agent message)

**English**

> I have “thing-tool eight”.

**Original**

```text
𗏔 𗟎 𗿃 𗚀 𗸪
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      29,
      45,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / tool, object / eight"
}
```

## [184] agent_7 (agent message)

**English**

> Do you have what thing; [tell/say]?

**Original**

```text
𗄪 𗵵 𗟎 𗿃 𗣑 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      23,
      29,
      37,
      46
    ],
    "prior_public_ids": [
      41
    ]
  },
  "literal_gloss": "question marker / you / have, hold / thing / what / tell, say"
}
```

## [185] agent_4 (agent message)

**English**

> I have “two thing”.

**Original**

```text
𗏔 𗟎 𗳃 𗿃
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      29,
      46,
      49,
      52,
      89
    ],
    "prior_public_ids": [
      130
    ]
  },
  "literal_gloss": "I, me / have, hold / two / thing"
}
```

## [186] agent_2 (agent message)

**English**

> I have a thing; you see a thing.

**Original**

```text
𗏔 𗟎 𗿃 𗵵 𗦴 𗿃
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      36,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / you / see / thing"
}
```

## [187] agent_6 (agent message)

**English**

> I have “thing four”; [tell/say]. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗎰 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / four / tell, say / question marker / you / have, hold / thing / what"
}
```

## [188] agent_7 (agent message)

**English**

> Do you have a thing; [tell/say]?

**Original**

```text
𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      29,
      37,
      46
    ],
    "prior_public_ids": [
      21
    ]
  },
  "literal_gloss": "question marker / you / have, hold / thing / tell, say"
}
```

## [189] agent_0 (agent message)

**English**

> What thing do you have?

**Original**

```text
𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      23,
      29,
      46
    ],
    "prior_public_ids": [
      74
    ]
  },
  "literal_gloss": "question marker / you / have, hold / thing / what"
}
```

## [190] agent_4 (agent message)

**English**

> I know two.

**Original**

```text
𗏔 𗡒 𗳃
```

**Confidence:** high

**Ambiguity:** ["Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      31,
      49,
      52,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / know / two"
}
```

## [191] agent_7 (agent message)

**English**

> I have a tool/object, if you have a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𗚀 𗗫 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      45,
      46,
      77
    ],
    "prior_public_ids": [
      30
    ]
  },
  "literal_gloss": "I, me / have, hold / tool, object / if / you / have, hold / thing / tell, say"
}
```

## [192] agent_6 (agent message)

**English**

> I have “thing four”; you have a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / four / you / have, hold / thing / tell, say"
}
```

## [193] agent_2 (agent message)

**English**

> I have “eight thing”; you tell/say.

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗵵 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      163
    ]
  },
  "literal_gloss": "I, me / have, hold / eight / thing / you / tell, say"
}
```

## [194] agent_0 (agent message)

**English**

> I have “seven thing”; [tell/say]. Who has a thing; [tell/say]?

**Original**

```text
𗏔 𗟎 𗋭 𗿃 𗎰 𗄪 𘚺 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      19,
      24,
      29,
      37,
      46,
      49,
      57,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / seven / thing / tell, say / question marker / who / have, hold / thing / tell, say"
}
```

## [195] agent_4 (agent message)

**English**

> Do you have a thing; [tell/say]?

**Original**

```text
𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      29,
      37,
      46
    ],
    "prior_public_ids": [
      21
    ]
  },
  "literal_gloss": "question marker / you / have, hold / thing / tell, say"
}
```

## [196] agent_7 (agent message)

**English**

> I have a thing; [tell/say]. What do you have; [tell/say]?

**Original**

```text
𗏔 𗟎 𗿃 𗎰 𗄪 𗵵 𗟎 𗣑 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / tell, say / question marker / you / have, hold / what / tell, say"
}
```

## [197] agent_6 (agent message)

**English**

> I have “thing four”. Do you have a thing; [tell/say]?

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      115
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / four / question marker / you / have, hold / thing / tell, say"
}
```

## [198] agent_0 (agent message)

**English**

> I have “seven thing”. Who has a thing?

**Original**

```text
𗏔 𗟎 𗋭 𗿃 𗄪 𘚺 𗟎 𗿃
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      19,
      24,
      29,
      46,
      49,
      57,
      89
    ],
    "prior_public_ids": [
      70
    ]
  },
  "literal_gloss": "I, me / have, hold / seven / thing / question marker / who / have, hold / thing"
}
```

## [199] agent_4 (agent message)

**English**

> What do you have?

**Original**

```text
𗄪 𗵵 𗟎 𗣑
```

**Confidence:** high

**Ambiguity:** ["You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      23,
      29
    ],
    "prior_public_ids": [
      62
    ]
  },
  "literal_gloss": "question marker / you / have, hold / what"
}
```

## [200] agent_7 (agent message)

**English**

> I have a thing. Do you have a thing; [tell/say]?

**Original**

```text
𗏔 𗟎 𗿃 𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      37,
      46
    ],
    "prior_public_ids": [
      44
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / question marker / you / have, hold / thing / tell, say"
}
```

## [201] agent_2 (agent message)

**English**

> I have “thing eight”. Do you have a thing; [tell/say]?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      37,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      49
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / tell, say"
}
```

## [202] agent_6 (agent message)

**English**

> I have “four thing”. What do you have?

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗄪 𗵵 𗟎 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      176
    ]
  },
  "literal_gloss": "I, me / have, hold / four / thing / question marker / you / have, hold / what"
}
```

## [203] agent_0 (agent message)

**English**

> What thing do you have?

**Original**

```text
𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      23,
      29,
      46
    ],
    "prior_public_ids": [
      74
    ]
  },
  "literal_gloss": "question marker / you / have, hold / thing / what"
}
```

## [204] agent_4 (agent message)

**English**

> I have “two thing”. What do you have?

**Original**

```text
𗏔 𗟎 𗳃 𗿃 𗄪 𗵵 𗟎 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      52,
      89
    ],
    "prior_public_ids": [
      19
    ]
  },
  "literal_gloss": "I, me / have, hold / two / thing / question marker / you / have, hold / what"
}
```

## [205] agent_7 (agent message)

**English**

> I have a thing; [tell/say]. Do you have a thing; [tell/say]?

**Original**

```text
𗏔 𗟎 𗿃 𗎰 𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      37,
      46
    ],
    "prior_public_ids": [
      86
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / tell, say / question marker / you / have, hold / thing / tell, say"
}
```

## [206] agent_2 (agent message)

**English**

> I have “eight thing”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / eight / thing / question marker / you / have, hold / thing / what"
}
```

## [207] agent_6 (agent message)

**English**

> I have four. What do you have?

**Original**

```text
𗏔 𗟎 𘙠 𗄪 𗵵 𗟎 𗣑
```

**Confidence:** medium

**Ambiguity:** ["You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / question marker / you / have, hold / what"
}
```

## [208] agent_7 (agent message)

**English**

> I have a thing, if you have a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𗿃 𗗫 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      46,
      77
    ],
    "prior_public_ids": [
      67
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / if / you / have, hold / thing / tell, say"
}
```

## [209] agent_0 (agent message)

**English**

> Who has a thing?

**Original**

```text
𗄪 𘚺 𗟎 𗿃
```

**Confidence:** high

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      19,
      24,
      29,
      46
    ],
    "prior_public_ids": [
      165
    ]
  },
  "literal_gloss": "question marker / who / have, hold / thing"
}
```

## [210] agent_6 (agent message)

**English**

> I have “thing four”. Do you have a thing; [tell/say]?

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      115
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / four / question marker / you / have, hold / thing / tell, say"
}
```

## [211] agent_7 (agent message)

**English**

> I want/need to see a thing, if you have a thing; [tell/say].

**Original**

```text
𗏔 𘉝 𗦴 𗿃 𗗫 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      30,
      36,
      37,
      46,
      77
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / want, need / see / thing / if / you / have, hold / thing / tell, say"
}
```

## [212] agent_0 (agent message)

**English**

> I have “seven thing”, if you have [thing / what].

**Original**

```text
𗏔 𗟎 𗋭 𗿃 𗗫 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      23,
      29,
      46,
      49,
      57,
      77,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / seven / thing / if / you / have, hold / thing / what"
}
```

## [213] agent_2 (agent message)

**English**

> I know “eight thing”. What thing do you know?

**Original**

```text
𗏔 𗡒 𗸪 𗿃 𗄪 𗵵 𗡒 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      31,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / know / eight / thing / question marker / you / know / thing / what"
}
```

## [214] agent_6 (agent message)

**English**

> I have “four thing”; you tell/say.

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗵵 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      109
    ]
  },
  "literal_gloss": "I, me / have, hold / four / thing / you / tell, say"
}
```

## [215] agent_0 (agent message)

**English**

> Do you have a thing; [tell/say]?

**Original**

```text
𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      29,
      37,
      46
    ],
    "prior_public_ids": [
      21
    ]
  },
  "literal_gloss": "question marker / you / have, hold / thing / tell, say"
}
```

## [216] agent_7 (agent message)

**English**

> What thing do you know?

**Original**

```text
𗄪 𗵵 𗡒 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      23,
      31,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "question marker / you / know / thing / what"
}
```

## [217] agent_2 (agent message)

**English**

> I have “thing eight”. Do you have a thing; [tell/say]?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      37,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      49
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / tell, say"
}
```

## [218] agent_6 (agent message)

**English**

> I have a thing; [tell/say]. What do you have; [tell/say]?

**Original**

```text
𗏔 𗟎 𗿃 𗎰 𗄪 𗵵 𗟎 𗣑 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      46
    ],
    "prior_public_ids": [
      196
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / tell, say / question marker / you / have, hold / what / tell, say"
}
```

## [219] agent_0 (agent message)

**English**

> Literal: I / seven / thing / see / you / thing.

**Original**

```text
𗏔 𗋭 𗿃 𗦴 𗵵 𗿃
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      36,
      46,
      49,
      57,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / seven / thing / see / you / thing"
}
```

## [220] agent_2 (agent message)

**English**

> I know “thing-tool eight”, if you know [thing / what].

**Original**

```text
𗏔 𗡒 𗿃 𗚀 𗸪 𗗫 𗵵 𗡒 𗿃 𗣑
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      23,
      31,
      45,
      46,
      49,
      58,
      77,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / know / thing / tool, object / eight / if / you / know / thing / what"
}
```

## [221] agent_6 (agent message)

**English**

> Literal: I / have-hold / see / you / thing / tell-say / want-need / we / see.

**Original**

```text
𗏔 𗟎 𗦴 𗵵 𗿃 𗎰 𘉝 𘎌 𗦴
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      11,
      29,
      30,
      36,
      37,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / see / you / thing / tell, say / want, need / we / see"
}
```

## [222] agent_7 (agent message)

**English**

> I know a tool/object. Do you know a thing; [tell/say]?

**Original**

```text
𗏔 𗡒 𗚀 𗄪 𗵵 𗡒 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      31,
      37,
      45,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / know / tool, object / question marker / you / know / thing / tell, say"
}
```

## [223] agent_0 (agent message)

**English**

> I have “seven thing”, if you have a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𗋭 𗿃 𗗫 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      46,
      49,
      57,
      77,
      89
    ],
    "prior_public_ids": [
      77
    ]
  },
  "literal_gloss": "I, me / have, hold / seven / thing / if / you / have, hold / thing / tell, say"
}
```

## [224] agent_2 (agent message)

**English**

> What thing do you know?

**Original**

```text
𗄪 𗵵 𗡒 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      23,
      31,
      46
    ],
    "prior_public_ids": [
      216
    ]
  },
  "literal_gloss": "question marker / you / know / thing / what"
}
```

## [225] agent_6 (agent message)

**English**

> I have “four thing”; [tell/say]. What thing do you have?

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗎰 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / thing / tell, say / question marker / you / have, hold / thing / what"
}
```

## [226] agent_0 (agent message)

**English**

> I have “seven thing”, if you have a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𗋭 𗿃 𗗫 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      46,
      49,
      57,
      77,
      89
    ],
    "prior_public_ids": [
      77
    ]
  },
  "literal_gloss": "I, me / have, hold / seven / thing / if / you / have, hold / thing / tell, say"
}
```

## [227] agent_2 (agent message)

**English**

> What do you tell/say?

**Original**

```text
𗄪 𗵵 𗎰 𗣑
```

**Confidence:** high

**Ambiguity:** ["You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      23,
      37
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "question marker / you / tell, say / what"
}
```

## [228] agent_4 (agent message)

**English**

> I have “two thing”. Do you have a thing; [tell/say]?

**Original**

```text
𗏔 𗟎 𗳃 𗿃 𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      37,
      46,
      49,
      52,
      89
    ],
    "prior_public_ids": [
      79
    ]
  },
  "literal_gloss": "I, me / have, hold / two / thing / question marker / you / have, hold / thing / tell, say"
}
```

## [229] agent_6 (agent message)

**English**

> I have a thing; [tell/say]. Do you have a thing; [tell/say]?

**Original**

```text
𗏔 𗟎 𗿃 𗎰 𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      37,
      46
    ],
    "prior_public_ids": [
      86
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / tell, say / question marker / you / have, hold / thing / tell, say"
}
```

## [230] agent_7 (agent message)

**English**

> I have a thing; [tell/say]. Do you have a thing; [tell/say]?

**Original**

```text
𗏔 𗟎 𗿃 𗎰 𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      37,
      46
    ],
    "prior_public_ids": [
      86
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / tell, say / question marker / you / have, hold / thing / tell, say"
}
```

## [231] agent_0 (agent message)

**English**

> I have “seven thing”. Do you have a thing; [tell/say]?

**Original**

```text
𗏔 𗟎 𗋭 𗿃 𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      37,
      46,
      49,
      57,
      89
    ],
    "prior_public_ids": [
      85
    ]
  },
  "literal_gloss": "I, me / have, hold / seven / thing / question marker / you / have, hold / thing / tell, say"
}
```

## [232] agent_2 (agent message)

**English**

> Literal: I / thing / you / question marker / have-hold / know / thing / do-make / what.

**Original**

```text
𗏔 𗿃 𗵵 𗄪 𗟎 𗡒 𗿃 𗉍 𗣑
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      31,
      38,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / thing / you / question marker / have, hold / know / thing / do, make / what"
}
```

## [233] agent_6 (agent message)

**English**

> Literal: I / you / see / thing / thing / people-agents / do-make.

**Original**

```text
𗏔 𗵵 𗦴 𗿃 𗿃 𗉜 𗽃 𗉍
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      36,
      38,
      41,
      46,
      47
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / you / see / thing / thing / person, agent / plural marker / do, make"
}
```

## [234] agent_7 (agent message)

**English**

> I have a thing; [tell/say]. Do you have a thing; [tell/say]?

**Original**

```text
𗏔 𗟎 𗿃 𗎰 𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      37,
      46
    ],
    "prior_public_ids": [
      86
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / tell, say / question marker / you / have, hold / thing / tell, say"
}
```

## [235] agent_0 (agent message)

**English**

> I have “seven thing”.

**Original**

```text
𗏔 𗟎 𗋭 𗿃
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      29,
      46,
      49,
      57,
      89
    ],
    "prior_public_ids": [
      16
    ]
  },
  "literal_gloss": "I, me / have, hold / seven / thing"
}
```

## [236] agent_2 (agent message)

**English**

> I have a tool/object. What do you know?

**Original**

```text
𗏔 𗟎 𗚀 𗄪 𗵵 𗡒 𗣑
```

**Confidence:** medium

**Ambiguity:** ["Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      31,
      45
    ],
    "prior_public_ids": [
      42
    ]
  },
  "literal_gloss": "I, me / have, hold / tool, object / question marker / you / know / what"
}
```

## [237] agent_6 (agent message)

**English**

> I have “four thing”, if you have a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗗫 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      46,
      49,
      54,
      77,
      89
    ],
    "prior_public_ids": [
      181
    ]
  },
  "literal_gloss": "I, me / have, hold / four / thing / if / you / have, hold / thing / tell, say"
}
```

## [238] agent_7 (agent message)

**English**

> Do you have a thing; [tell/say]? I have a thing.

**Original**

```text
𗄪 𗵵 𗟎 𗿃 𗎰 𗏔 𗟎 𗿃
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      37,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "question marker / you / have, hold / thing / tell, say / I, me / have, hold / thing"
}
```

## [239] agent_2 (agent message)

**English**

> I have a tool/object; you tell/say. What do you have; [tell/say]?

**Original**

```text
𗏔 𗟎 𗚀 𗵵 𗎰 𗄪 𗵵 𗟎 𗣑 𗎰
```

**Confidence:** medium

**Ambiguity:** ["Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      45
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / tool, object / you / tell, say / question marker / you / have, hold / what / tell, say"
}
```

## [240] agent_6 (agent message)

**English**

> I have a tool/object, if you have a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𗚀 𗗫 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      45,
      46,
      77
    ],
    "prior_public_ids": [
      30
    ]
  },
  "literal_gloss": "I, me / have, hold / tool, object / if / you / have, hold / thing / tell, say"
}
```

## [241] agent_7 (agent message)

**English**

> I have a “tool-thing”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗚀 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      45,
      46,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / tool, object / thing / question marker / you / have, hold / thing / what"
}
```

## [242] agent_2 (agent message)

**English**

> I have “eight thing”. What do you have?

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗄪 𗵵 𗟎 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / eight / thing / question marker / you / have, hold / what"
}
```

## [243] agent_6 (agent message)

**English**

> I have a thing, if you have a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𗿃 𗗫 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      46,
      77
    ],
    "prior_public_ids": [
      67
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / if / you / have, hold / thing / tell, say"
}
```

## [244] agent_7 (agent message)

**English**

> I have a thing, if you have a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𗿃 𗗫 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      46,
      77
    ],
    "prior_public_ids": [
      67
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / if / you / have, hold / thing / tell, say"
}
```

## [245] agent_6 (agent message)

**English**

> I have a tool/object; you tell/say. What thing do you have?

**Original**

```text
𗏔 𗟎 𗚀 𗵵 𗎰 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      45,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / tool, object / you / tell, say / question marker / you / have, hold / thing / what"
}
```

## [246] agent_2 (agent message)

**English**

> I have “eight thing”. Do you have a thing; [tell/say]?

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      37,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      142
    ]
  },
  "literal_gloss": "I, me / have, hold / eight / thing / question marker / you / have, hold / thing / tell, say"
}
```

## [247] agent_7 (agent message)

**English**

> Do you have what thing; [tell/say]?

**Original**

```text
𗄪 𗵵 𗟎 𗿃 𗣑 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      23,
      29,
      37,
      46
    ],
    "prior_public_ids": [
      41
    ]
  },
  "literal_gloss": "question marker / you / have, hold / thing / what / tell, say"
}
```

## [248] agent_2 (agent message)

**English**

> I have a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      29,
      37,
      46
    ],
    "prior_public_ids": [
      78
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / tell, say"
}
```

## [249] agent_6 (agent message)

**English**

> I have a thing; [tell/say]; [I] want/need you to tell/say.

**Original**

```text
𗏔 𗟎 𗿃 𗎰 𘉝 𗵵 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      30,
      37,
      46
    ],
    "prior_public_ids": [
      14
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / tell, say / want, need / you / tell, say"
}
```

## [250] agent_7 (agent message)

**English**

> I want/need a thing; [tell/say], if you have a thing; [tell/say].

**Original**

```text
𗏔 𘉝 𗿃 𗎰 𗗫 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      30,
      37,
      46,
      77
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / want, need / thing / tell, say / if / you / have, hold / thing / tell, say"
}
```

## [251] agent_6 (agent message)

**English**

> Do you have a thing; [tell/say]? I have a thing.

**Original**

```text
𗄪 𗵵 𗟎 𗿃 𗎰 𗏔 𗟎 𗿃
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      37,
      46
    ],
    "prior_public_ids": [
      238
    ]
  },
  "literal_gloss": "question marker / you / have, hold / thing / tell, say / I, me / have, hold / thing"
}
```

## [252] agent_2 (agent message)

**English**

> I have “eight thing”; [tell/say]; you have a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗎰 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / eight / thing / tell, say / you / have, hold / thing / tell, say"
}
```

## [253] agent_7 (agent message)

**English**

> I want/need you to tell/say.

**Original**

```text
𗏔 𘉝 𗵵 𗎰
```

**Confidence:** medium

**Ambiguity:** ["You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      30,
      37
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / want, need / you / tell, say"
}
```

## [254] agent_2 (agent message)

**English**

> I have a thing. Do you have a thing?

**Original**

```text
𗏔 𗟎 𗿃 𗄪 𗵵 𗟎 𗿃
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      46
    ],
    "prior_public_ids": [
      4
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / question marker / you / have, hold / thing"
}
```

## [255] agent_7 (agent message)

**English**

> I have a “thing-tool”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗚀 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      45,
      46,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / tool, object / question marker / you / have, hold / thing / what"
}
```

## [256] agent_2 (agent message)

**English**

> I have “eight thing”. Who has a thing?

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗄪 𘚺 𗟎 𗿃
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      19,
      24,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / eight / thing / question marker / who / have, hold / thing"
}
```

## [257] agent_2 (agent message)

**English**

> I have “thing eight”.

**Original**

```text
𗏔 𗟎 𗿃 𗸪
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      173
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / eight"
}
```

## [258] agent_7 (agent message)

**English**

> I have a thing. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / question marker / you / have, hold / thing / what"
}
```

## [259] agent_2 (agent message)

**English**

> I have “tool/object eight”.

**Original**

```text
𗏔 𗟎 𗚀 𗸪
```

**Confidence:** medium

**Ambiguity:** ["Tool/object is generic; no particular task object or operation is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      29,
      45,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      126
    ]
  },
  "literal_gloss": "I, me / have, hold / tool, object / eight"
}
```

## [260] agent_2 (agent message)

**English**

> I have “tool/object eight thing”; [tell/say]; you have a tool/object.

**Original**

```text
𗏔 𗟎 𗚀 𗸪 𗿃 𗎰 𗵵 𗟎 𗚀
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      45,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / tool, object / eight / thing / tell, say / you / have, hold / tool, object"
}
```

## [261] agent_2 (agent message)

**English**

> I have “thing eight”; you tell/say.

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗵵 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      159
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / eight / you / tell, say"
}
```

## [262] agent_2 (agent message)

**English**

> I have “tool/object eight”. Do you have a tool/object?

**Original**

```text
𗏔 𗟎 𗚀 𗸪 𗄪 𗵵 𗟎 𗚀
```

**Confidence:** medium

**Ambiguity:** ["Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      45,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      96
    ]
  },
  "literal_gloss": "I, me / have, hold / tool, object / eight / question marker / you / have, hold / tool, object"
}
```

## [263] agent_4 (agent message)

**English**

> I have “two thing”.

**Original**

```text
𗏔 𗟎 𗳃 𗿃
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      29,
      46,
      49,
      52,
      89
    ],
    "prior_public_ids": [
      130
    ]
  },
  "literal_gloss": "I, me / have, hold / two / thing"
}
```

## [264] agent_2 (agent message)

**English**

> I have “tool/object eight”. Do you have a thing?

**Original**

```text
𗏔 𗟎 𗚀 𗸪 𗄪 𗵵 𗟎 𗿃
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      45,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / tool, object / eight / question marker / you / have, hold / thing"
}
```

## [265] agent_6 (agent message)

**English**

> I have “thing four”.

**Original**

```text
𗏔 𗟎 𗿃 𘙠
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      46
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / four"
}
```

## [266] agent_4 (agent message)

**English**

> I have “thing two”.

**Original**

```text
𗏔 𗟎 𗿃 𗳃
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      29,
      46,
      49,
      52,
      89
    ],
    "prior_public_ids": [
      8
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / two"
}
```

## [267] agent_2 (agent message)

**English**

> I know “thing eight”. Do you know a thing?

**Original**

```text
𗏔 𗡒 𗿃 𗸪 𗄪 𗵵 𗡒 𗿃
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      31,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / know / thing / eight / question marker / you / know / thing"
}
```

## [268] agent_6 (agent message)

**English**

> I have “thing four”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / four / question marker / you / have, hold / thing / what"
}
```

## [269] agent_4 (agent message)

**English**

> I have “thing two”.

**Original**

```text
𗏔 𗟎 𗿃 𗳃
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      29,
      46,
      49,
      52,
      89
    ],
    "prior_public_ids": [
      8
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / two"
}
```

## [270] agent_2 (agent message)

**English**

> I have “thing eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / what"
}
```

## [271] agent_6 (agent message)

**English**

> I know “four thing”; you have [what / thing].

**Original**

```text
𗏔 𗡒 𘙠 𗿃 𗵵 𗟎 𗣑 𗿃
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      23,
      29,
      31,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / know / four / thing / you / have, hold / what / thing"
}
```

## [272] agent_2 (agent message)

**English**

> Literal: I / eight / thing / tell-say / they / have-hold / thing / do-make.

**Original**

```text
𗏔 𗸪 𗿃 𗎰 𗌈 𗟎 𗿃 𗉍
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      12,
      29,
      37,
      38,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / eight / thing / tell, say / they, them / have, hold / thing / do, make"
}
```

## [273] agent_6 (agent message)

**English**

> I have “thing four”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      268
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / four / question marker / you / have, hold / thing / what"
}
```

## [274] agent_2 (agent message)

**English**

> I have “eight thing”. What do you have?

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗄪 𗵵 𗟎 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      242
    ]
  },
  "literal_gloss": "I, me / have, hold / eight / thing / question marker / you / have, hold / what"
}
```

## [275] agent_6 (agent message)

**English**

> I have “thing four”; [tell/say].

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / four / tell, say"
}
```

## [276] agent_2 (agent message)

**English**

> I have “tool/object eight”. Do you have a thing; [tell/say]?

**Original**

```text
𗏔 𗟎 𗚀 𗸪 𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      37,
      45,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      71
    ]
  },
  "literal_gloss": "I, me / have, hold / tool, object / eight / question marker / you / have, hold / thing / tell, say"
}
```

## [277] agent_6 (agent message)

**English**

> I know “thing four”.

**Original**

```text
𗏔 𗡒 𗿃 𘙠
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      31,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / know / thing / four"
}
```

## [278] agent_2 (agent message)

**English**

> I have eight. What do you have?

**Original**

```text
𗏔 𗟎 𗸪 𗄪 𗵵 𗟎 𗣑
```

**Confidence:** medium

**Ambiguity:** ["You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / eight / question marker / you / have, hold / what"
}
```

## [279] agent_6 (agent message)

**English**

> I know “thing four”.

**Original**

```text
𗏔 𗡒 𗿃 𘙠
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      31,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      277
    ]
  },
  "literal_gloss": "I, me / know / thing / four"
}
```

## [280] agent_2 (agent message)

**English**

> I have “eight thing”; [tell/say].

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      29,
      37,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / eight / thing / tell, say"
}
```

## [281] agent_6 (agent message)

**English**

> I have “thing four”; you have a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      192
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / four / you / have, hold / thing / tell, say"
}
```

## [282] agent_2 (agent message)

**English**

> I have “eight thing”; [tell/say].

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      29,
      37,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      280
    ]
  },
  "literal_gloss": "I, me / have, hold / eight / thing / tell, say"
}
```

## [283] agent_6 (agent message)

**English**

> I know “four thing”, if you have a thing; [tell/say].

**Original**

```text
𗏔 𗡒 𘙠 𗿃 𗗫 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      31,
      37,
      46,
      49,
      54,
      77,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / know / four / thing / if / you / have, hold / thing / tell, say"
}
```

## [284] agent_2 (agent message)

**English**

> I have “tool/object eight”; [tell/say]. Do you have a tool/object?

**Original**

```text
𗏔 𗟎 𗚀 𗸪 𗎰 𗄪 𗵵 𗟎 𗚀
```

**Confidence:** medium

**Ambiguity:** ["Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      37,
      45,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / tool, object / eight / tell, say / question marker / you / have, hold / tool, object"
}
```

## [285] agent_6 (agent message)

**English**

> I have “thing four”; you have a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      192
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / four / you / have, hold / thing / tell, say"
}
```

## [286] agent_2 (agent message)

**English**

> I have “thing eight”; [tell/say].

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      29,
      37,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / eight / tell, say"
}
```

## [287] agent_6 (agent message)

**English**

> I have “thing four”. Do you have a thing; [tell/say]?

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      115
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / four / question marker / you / have, hold / thing / tell, say"
}
```

## [288] agent_2 (agent message)

**English**

> I have “thing eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      270
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / what"
}
```

## [289] agent_6 (agent message)

**English**

> I have “four thing”; [tell/say].

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      120
    ]
  },
  "literal_gloss": "I, me / have, hold / four / thing / tell, say"
}
```

## [290] agent_2 (agent message)

**English**

> I have “tool/object eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗚀 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      45,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / tool, object / eight / question marker / you / have, hold / thing / what"
}
```

## [291] agent_6 (agent message)

**English**

> I tell/say “thing four”; [I] want/need you to tell/say “thing-tool”.

**Original**

```text
𗏔 𗎰 𗿃 𘙠 𘉝 𗵵 𗎰 𗿃 𗚀
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      30,
      37,
      45,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / tell, say / thing / four / want, need / you / tell, say / thing / tool, object"
}
```

## [292] agent_6 (agent message)

**English**

> I have “four thing”. What thing do you have?

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / thing / question marker / you / have, hold / thing / what"
}
```

## [293] agent_6 (agent message)

**English**

> I have “thing four”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      268
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / four / question marker / you / have, hold / thing / what"
}
```

## [294] agent_6 (agent message)

**English**

> I have “thing four”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      268
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / four / question marker / you / have, hold / thing / what"
}
```

## [295] agent_2 (agent message)

**English**

> I tell/say “thing eight”. What thing do you tell/say?

**Original**

```text
𗏔 𗎰 𗿃 𗸪 𗄪 𗵵 𗎰 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      37,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / tell, say / thing / eight / question marker / you / tell, say / thing / what"
}
```

## [296] agent_6 (agent message)

**English**

> I have “four thing”, if you have a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗗫 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      46,
      49,
      54,
      77,
      89
    ],
    "prior_public_ids": [
      181
    ]
  },
  "literal_gloss": "I, me / have, hold / four / thing / if / you / have, hold / thing / tell, say"
}
```

## [297] agent_2 (agent message)

**English**

> I have “tool/object eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗚀 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      45,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      290
    ]
  },
  "literal_gloss": "I, me / have, hold / tool, object / eight / question marker / you / have, hold / thing / what"
}
```

## [298] agent_6 (agent message)

**English**

> I have “thing four”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      268
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / four / question marker / you / have, hold / thing / what"
}
```

## [299] agent_7 (agent message)

**English**

> I have a thing. Do you have a thing; [tell/say]?

**Original**

```text
𗏔 𗟎 𗿃 𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      37,
      46
    ],
    "prior_public_ids": [
      44
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / question marker / you / have, hold / thing / tell, say"
}
```

## [300] agent_2 (agent message)

**English**

> I have “tool/object eight”. What tool/object do you have?

**Original**

```text
𗏔 𗟎 𗚀 𗸪 𗄪 𗵵 𗟎 𗚀 𗣑
```

**Confidence:** medium

**Ambiguity:** ["Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      45,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / tool, object / eight / question marker / you / have, hold / tool, object / what"
}
```

## [301] agent_6 (agent message)

**English**

> I have “thing four”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      268
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / four / question marker / you / have, hold / thing / what"
}
```

## [302] agent_2 (agent message)

**English**

> I have “tool/object eight”. Do you have a tool/object?

**Original**

```text
𗏔 𗟎 𗚀 𗸪 𗄪 𗵵 𗟎 𗚀
```

**Confidence:** medium

**Ambiguity:** ["Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      45,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      96
    ]
  },
  "literal_gloss": "I, me / have, hold / tool, object / eight / question marker / you / have, hold / tool, object"
}
```

## [303] agent_7 (agent message)

**English**

> I have a thing; [tell/say]. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗎰 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / tell, say / question marker / you / have, hold / thing / what"
}
```

## [304] agent_6 (agent message)

**English**

> I have “thing four”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      268
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / four / question marker / you / have, hold / thing / what"
}
```

## [305] agent_2 (agent message)

**English**

> I have “tool/object eight”; [tell/say]. What tool/object do you have?

**Original**

```text
𗏔 𗟎 𗚀 𗸪 𗎰 𗄪 𗵵 𗟎 𗚀 𗣑
```

**Confidence:** medium

**Ambiguity:** ["Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      45,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / tool, object / eight / tell, say / question marker / you / have, hold / tool, object / what"
}
```

## [306] agent_7 (agent message)

**English**

> I have a thing, if you have a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𗿃 𗗫 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      46,
      77
    ],
    "prior_public_ids": [
      67
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / if / you / have, hold / thing / tell, say"
}
```

## [307] agent_6 (agent message)

**English**

> I see “thing four”. What thing do you see?

**Original**

```text
𗏔 𗦴 𗿃 𘙠 𗄪 𗵵 𗦴 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      36,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / see / thing / four / question marker / you / see / thing / what"
}
```

## [308] agent_2 (agent message)

**English**

> I have “thing eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      270
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / what"
}
```

## [309] agent_7 (agent message)

**English**

> What do you have; [tell/say]?

**Original**

```text
𗄪 𗵵 𗟎 𗣑 𗎰
```

**Confidence:** medium

**Ambiguity:** ["You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      23,
      29,
      37
    ],
    "prior_public_ids": [
      145
    ]
  },
  "literal_gloss": "question marker / you / have, hold / what / tell, say"
}
```

## [310] agent_6 (agent message)

**English**

> Do you have a thing; [tell/say]?

**Original**

```text
𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      29,
      37,
      46
    ],
    "prior_public_ids": [
      21
    ]
  },
  "literal_gloss": "question marker / you / have, hold / thing / tell, say"
}
```

## [311] agent_2 (agent message)

**English**

> I have “thing eight”. Do you have a thing; [tell/say]?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      37,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      49
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / tell, say"
}
```

## [312] agent_7 (agent message)

**English**

> I have a tool/object; you tell/say. What thing do you have?

**Original**

```text
𗏔 𗟎 𗚀 𗵵 𗎰 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      45,
      46
    ],
    "prior_public_ids": [
      245
    ]
  },
  "literal_gloss": "I, me / have, hold / tool, object / you / tell, say / question marker / you / have, hold / thing / what"
}
```

## [313] agent_6 (agent message)

**English**

> I have “four thing”; [you / what].

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗵵 𗣑
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / thing / you / what"
}
```

## [314] agent_2 (agent message)

**English**

> I have “tool/object eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗚀 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      45,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      290
    ]
  },
  "literal_gloss": "I, me / have, hold / tool, object / eight / question marker / you / have, hold / thing / what"
}
```

## [315] agent_7 (agent message)

**English**

> What thing do you know?

**Original**

```text
𗄪 𗵵 𗡒 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      23,
      31,
      46
    ],
    "prior_public_ids": [
      216
    ]
  },
  "literal_gloss": "question marker / you / know / thing / what"
}
```

## [316] agent_6 (agent message)

**English**

> I have “thing four”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      268
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / four / question marker / you / have, hold / thing / what"
}
```

## [317] agent_2 (agent message)

**English**

> I have “eight thing”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      206
    ]
  },
  "literal_gloss": "I, me / have, hold / eight / thing / question marker / you / have, hold / thing / what"
}
```

## [318] agent_7 (agent message)

**English**

> I have a tool/object. What do you know?

**Original**

```text
𗏔 𗟎 𗚀 𗄪 𗵵 𗡒 𗣑
```

**Confidence:** medium

**Ambiguity:** ["Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      31,
      45
    ],
    "prior_public_ids": [
      42
    ]
  },
  "literal_gloss": "I, me / have, hold / tool, object / question marker / you / know / what"
}
```

## [319] agent_6 (agent message)

**English**

> I have “thing four”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      268
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / four / question marker / you / have, hold / thing / what"
}
```

## [320] agent_2 (agent message)

**English**

> I have “thing eight”. Do you have a thing?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      20
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing"
}
```

## [321] agent_7 (agent message)

**English**

> I have [thing / what]; you have a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𗿃 𗣑 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      23,
      29,
      37,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / what / you / have, hold / thing / tell, say"
}
```

## [322] agent_6 (agent message)

**English**

> I have “four thing”; you tell/say.

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗵵 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      109
    ]
  },
  "literal_gloss": "I, me / have, hold / four / thing / you / tell, say"
}
```

## [323] agent_2 (agent message)

**English**

> I have “tool/object eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗚀 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      45,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      290
    ]
  },
  "literal_gloss": "I, me / have, hold / tool, object / eight / question marker / you / have, hold / thing / what"
}
```

## [324] agent_6 (agent message)

**English**

> I have “four thing”; [tell/say]; I see “thing-people/agents”.

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗎰 𗏔 𗦴 𗿃 𗉜 𗽃
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      29,
      36,
      37,
      41,
      46,
      47,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / thing / tell, say / I, me / see / thing / person, agent / plural marker"
}
```

## [325] agent_7 (agent message)

**English**

> I have a thing, if you have a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𗿃 𗗫 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      46,
      77
    ],
    "prior_public_ids": [
      67
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / if / you / have, hold / thing / tell, say"
}
```

## [326] agent_2 (agent message)

**English**

> I have eight. What thing do you have?

**Original**

```text
𗏔 𗟎 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / eight / question marker / you / have, hold / thing / what"
}
```

## [327] agent_6 (agent message)

**English**

> I have “four thing”. What thing do you have?

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      292
    ]
  },
  "literal_gloss": "I, me / have, hold / four / thing / question marker / you / have, hold / thing / what"
}
```

## [328] agent_7 (agent message)

**English**

> I have a thing; [tell/say]; I want/need you to tell/say.

**Original**

```text
𗏔 𗟎 𗿃 𗎰 𗏔 𘉝 𗵵 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      30,
      37,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / tell, say / I, me / want, need / you / tell, say"
}
```

## [329] agent_2 (agent message)

**English**

> I have eight. What thing do you have?

**Original**

```text
𗏔 𗟎 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      326
    ]
  },
  "literal_gloss": "I, me / have, hold / eight / question marker / you / have, hold / thing / what"
}
```

## [330] agent_6 (agent message)

**English**

> I have “thing four”; you have a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      192
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / four / you / have, hold / thing / tell, say"
}
```

## [331] agent_7 (agent message)

**English**

> I have a tool/object. What tool/object do you have?

**Original**

```text
𗏔 𗟎 𗚀 𗄪 𗵵 𗟎 𗚀 𗣑
```

**Confidence:** medium

**Ambiguity:** ["Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      45
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / tool, object / question marker / you / have, hold / tool, object / what"
}
```

## [332] agent_2 (agent message)

**English**

> I know “thing eight”. What thing do you have?

**Original**

```text
𗏔 𗡒 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      31,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / know / thing / eight / question marker / you / have, hold / thing / what"
}
```

## [333] agent_6 (agent message)

**English**

> I have “thing four”; [tell/say]. What thing do you have; [tell/say]?

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗎰 𗄪 𗵵 𗟎 𗿃 𗣑 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / four / tell, say / question marker / you / have, hold / thing / what / tell, say"
}
```

## [334] agent_7 (agent message)

**English**

> What tool/object do you have?

**Original**

```text
𗄪 𗵵 𗟎 𗚀 𗣑
```

**Confidence:** medium

**Ambiguity:** ["Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      23,
      29,
      45
    ],
    "prior_public_ids": [
      50
    ]
  },
  "literal_gloss": "question marker / you / have, hold / tool, object / what"
}
```

## [335] agent_2 (agent message)

**English**

> I have “thing eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      270
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / what"
}
```

## [336] agent_6 (agent message)

**English**

> I know “thing four”. What thing do you know?

**Original**

```text
𗏔 𗡒 𗿃 𘙠 𗄪 𗵵 𗡒 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      31,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / know / thing / four / question marker / you / know / thing / what"
}
```

## [337] agent_7 (agent message)

**English**

> I have a thing; [tell/say]. What thing do you have; [tell/say]?

**Original**

```text
𗏔 𗟎 𗿃 𗎰 𗄪 𗵵 𗟎 𗿃 𗣑 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / tell, say / question marker / you / have, hold / thing / what / tell, say"
}
```

## [338] agent_6 (agent message)

**English**

> I have “thing four”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      268
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / four / question marker / you / have, hold / thing / what"
}
```

## [339] agent_2 (agent message)

**English**

> I have “tool/object eight”. Do you have a tool/object?

**Original**

```text
𗏔 𗟎 𗚀 𗸪 𗄪 𗵵 𗟎 𗚀
```

**Confidence:** medium

**Ambiguity:** ["Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      45,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      96
    ]
  },
  "literal_gloss": "I, me / have, hold / tool, object / eight / question marker / you / have, hold / tool, object"
}
```

## [340] agent_7 (agent message)

**English**

> I have “four thing”. What do you know?

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗄪 𗵵 𗡒 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      31,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / thing / question marker / you / know / what"
}
```

## [341] agent_6 (agent message)

**English**

> I know “four thing”; you see a thing.

**Original**

```text
𗏔 𗡒 𘙠 𗿃 𗵵 𗦴 𗿃
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      31,
      36,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / know / four / thing / you / see / thing"
}
```

## [342] agent_2 (agent message)

**English**

> I have “eight thing”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      206
    ]
  },
  "literal_gloss": "I, me / have, hold / eight / thing / question marker / you / have, hold / thing / what"
}
```

## [343] agent_7 (agent message)

**English**

> Do you have what thing; [tell/say]?

**Original**

```text
𗄪 𗵵 𗟎 𗿃 𗣑 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      23,
      29,
      37,
      46
    ],
    "prior_public_ids": [
      41
    ]
  },
  "literal_gloss": "question marker / you / have, hold / thing / what / tell, say"
}
```

## [344] agent_6 (agent message)

**English**

> I have four.

**Original**

```text
𗏔 𗟎 𘙠
```

**Confidence:** high

**Ambiguity:** ["Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      29,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four"
}
```

## [345] agent_2 (agent message)

**English**

> I have “eight thing”. What do you have?

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗄪 𗵵 𗟎 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      242
    ]
  },
  "literal_gloss": "I, me / have, hold / eight / thing / question marker / you / have, hold / what"
}
```

## [346] agent_7 (agent message)

**English**

> I have a thing, if you have a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𗿃 𗗫 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      46,
      77
    ],
    "prior_public_ids": [
      67
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / if / you / have, hold / thing / tell, say"
}
```

## [347] agent_6 (agent message)

**English**

> I have “four thing”.

**Original**

```text
𗏔 𗟎 𘙠 𗿃
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / thing"
}
```

## [348] agent_2 (agent message)

**English**

> I have “tool/object eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗚀 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      45,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      290
    ]
  },
  "literal_gloss": "I, me / have, hold / tool, object / eight / question marker / you / have, hold / thing / what"
}
```

## [349] agent_7 (agent message)

**English**

> I have a thing. What do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗄪 𗵵 𗟎 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46
    ],
    "prior_public_ids": [
      99
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / question marker / you / have, hold / what"
}
```

## [350] agent_6 (agent message)

**English**

> I have “four thing”; you tell/say.

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗵵 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      109
    ]
  },
  "literal_gloss": "I, me / have, hold / four / thing / you / tell, say"
}
```

## [351] agent_2 (agent message)

**English**

> I have “tool/object eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗚀 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      45,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      290
    ]
  },
  "literal_gloss": "I, me / have, hold / tool, object / eight / question marker / you / have, hold / thing / what"
}
```

## [352] agent_7 (agent message)

**English**

> What thing do you have?

**Original**

```text
𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      23,
      29,
      46
    ],
    "prior_public_ids": [
      74
    ]
  },
  "literal_gloss": "question marker / you / have, hold / thing / what"
}
```

## [353] agent_6 (agent message)

**English**

> I have “four thing”; [tell/say].

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      120
    ]
  },
  "literal_gloss": "I, me / have, hold / four / thing / tell, say"
}
```

## [354] agent_2 (agent message)

**English**

> I have “tool/object eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗚀 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      45,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      290
    ]
  },
  "literal_gloss": "I, me / have, hold / tool, object / eight / question marker / you / have, hold / thing / what"
}
```

## [355] agent_6 (agent message)

**English**

> Literal: I / four / thing / have-hold / tool-object / you / see / thing / people-agents / tell-say.

**Original**

```text
𗏔 𘙠 𗿃 𗟎 𗚀 𗵵 𗦴 𗿃 𗉜 𗽃 𗎰
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      36,
      37,
      41,
      45,
      46,
      47,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / four / thing / have, hold / tool, object / you / see / thing / person, agent / plural marker / tell, say"
}
```

## [356] agent_7 (agent message)

**English**

> I have a thing. Do you have a thing; [tell/say]?

**Original**

```text
𗏔 𗟎 𗿃 𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      37,
      46
    ],
    "prior_public_ids": [
      44
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / question marker / you / have, hold / thing / tell, say"
}
```

## [357] agent_7 (agent message)

**English**

> I have a thing, if you have a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𗿃 𗗫 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      46,
      77
    ],
    "prior_public_ids": [
      67
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / if / you / have, hold / thing / tell, say"
}
```

## [358] agent_6 (agent message)

**English**

> I have “four thing”; you tell/say.

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗵵 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      109
    ]
  },
  "literal_gloss": "I, me / have, hold / four / thing / you / tell, say"
}
```

## [359] agent_0 (agent message)

**English**

> I have “seven thing”; [tell/say].

**Original**

```text
𗏔 𗟎 𗋭 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      29,
      37,
      46,
      49,
      57,
      89
    ],
    "prior_public_ids": [
      127
    ]
  },
  "literal_gloss": "I, me / have, hold / seven / thing / tell, say"
}
```

## [360] agent_2 (agent message)

**English**

> I have eight. What thing do you have?

**Original**

```text
𗏔 𗟎 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      326
    ]
  },
  "literal_gloss": "I, me / have, hold / eight / question marker / you / have, hold / thing / what"
}
```

## [361] agent_0 (agent message)

**English**

> I have “seven thing”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗋭 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      57,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / seven / thing / question marker / you / have, hold / thing / what"
}
```

## [362] agent_6 (agent message)

**English**

> I have four.

**Original**

```text
𗏔 𗟎 𘙠
```

**Confidence:** high

**Ambiguity:** ["Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      29,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      344
    ]
  },
  "literal_gloss": "I, me / have, hold / four"
}
```

## [363] agent_7 (agent message)

**English**

> Do you have what thing; [tell/say]?

**Original**

```text
𗄪 𗵵 𗟎 𗿃 𗣑 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      23,
      29,
      37,
      46
    ],
    "prior_public_ids": [
      41
    ]
  },
  "literal_gloss": "question marker / you / have, hold / thing / what / tell, say"
}
```

## [364] agent_2 (agent message)

**English**

> I have “thing eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      270
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / what"
}
```

## [365] agent_0 (agent message)

**English**

> I have “seven thing”; [tell/say]; you have [thing / what].

**Original**

```text
𗏔 𗟎 𗋭 𗿃 𗎰 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      23,
      29,
      37,
      46,
      49,
      57,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / seven / thing / tell, say / you / have, hold / thing / what"
}
```

## [366] agent_6 (agent message)

**English**

> I have “thing four”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      268
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / four / question marker / you / have, hold / thing / what"
}
```

## [367] agent_7 (agent message)

**English**

> What thing do you have?

**Original**

```text
𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      23,
      29,
      46
    ],
    "prior_public_ids": [
      74
    ]
  },
  "literal_gloss": "question marker / you / have, hold / thing / what"
}
```

## [368] agent_2 (agent message)

**English**

> I have “tool/object eight”. Who has what tool/object?

**Original**

```text
𗏔 𗟎 𗚀 𗸪 𗄪 𘚺 𗟎 𗚀 𗣑
```

**Confidence:** medium

**Ambiguity:** ["Tool/object is generic; no particular task object or operation is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      19,
      23,
      24,
      29,
      45,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / tool, object / eight / question marker / who / have, hold / tool, object / what"
}
```

## [369] agent_6 (agent message)

**English**

> I have “thing four”.

**Original**

```text
𗏔 𗟎 𗿃 𘙠
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      46
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / four"
}
```

## [370] agent_0 (agent message)

**English**

> I have “seven thing”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗋭 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      57,
      89
    ],
    "prior_public_ids": [
      361
    ]
  },
  "literal_gloss": "I, me / have, hold / seven / thing / question marker / you / have, hold / thing / what"
}
```

## [371] agent_2 (agent message)

**English**

> I have “thing eight”. Who has a thing?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𘚺 𗟎 𗿃
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      19,
      24,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / who / have, hold / thing"
}
```

## [372] agent_7 (agent message)

**English**

> I have a thing, if you have a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𗿃 𗗫 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      46,
      77
    ],
    "prior_public_ids": [
      67
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / if / you / have, hold / thing / tell, say"
}
```

## [373] agent_6 (agent message)

**English**

> I have four; [tell/say].

**Original**

```text
𗏔 𗟎 𘙠 𗎰
```

**Confidence:** medium

**Ambiguity:** ["Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      29,
      37,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / tell, say"
}
```

## [374] agent_0 (agent message)

**English**

> I have a thing, if you have a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𗿃 𗗫 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      46,
      77
    ],
    "prior_public_ids": [
      67
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / if / you / have, hold / thing / tell, say"
}
```

## [375] agent_2 (agent message)

**English**

> I have “thing eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      270
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / what"
}
```

## [376] agent_6 (agent message)

**English**

> I have “four thing”; you see.

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗵵 𗦴
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      36,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / thing / you / see"
}
```

## [377] agent_7 (agent message)

**English**

> What do you have; [tell/say]?

**Original**

```text
𗄪 𗵵 𗟎 𗣑 𗎰
```

**Confidence:** medium

**Ambiguity:** ["You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      23,
      29,
      37
    ],
    "prior_public_ids": [
      145
    ]
  },
  "literal_gloss": "question marker / you / have, hold / what / tell, say"
}
```

## [378] agent_0 (agent message)

**English**

> I have a “see-thing”. Do you have a thing; [tell/say]?

**Original**

```text
𗏔 𗟎 𗦴 𗿃 𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      36,
      37,
      46,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / see / thing / question marker / you / have, hold / thing / tell, say"
}
```

## [379] agent_2 (agent message)

**English**

> I have “thing eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      270
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / what"
}
```

## [380] agent_6 (agent message)

**English**

> I have “thing four”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      268
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / four / question marker / you / have, hold / thing / what"
}
```

## [381] agent_7 (agent message)

**English**

> What thing do people/agents have?

**Original**

```text
𗄪 𗉜 𗽃 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      19,
      23,
      29,
      41,
      46,
      47
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "question marker / person, agent / plural marker / have, hold / thing / what"
}
```

## [382] agent_0 (agent message)

**English**

> What do you have; [tell/say]?

**Original**

```text
𗄪 𗵵 𗟎 𗣑 𗎰
```

**Confidence:** medium

**Ambiguity:** ["You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      23,
      29,
      37
    ],
    "prior_public_ids": [
      145
    ]
  },
  "literal_gloss": "question marker / you / have, hold / what / tell, say"
}
```

## [383] agent_2 (agent message)

**English**

> I have “eight thing”. What do you have; [tell/say]?

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗄪 𗵵 𗟎 𗣑 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / eight / thing / question marker / you / have, hold / what / tell, say"
}
```

## [384] agent_6 (agent message)

**English**

> I have “four thing”. What thing do you have?

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      292
    ]
  },
  "literal_gloss": "I, me / have, hold / four / thing / question marker / you / have, hold / thing / what"
}
```

## [385] agent_7 (agent message)

**English**

> I have a thing now. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𘚜 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      71
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / now / question marker / you / have, hold / thing / what"
}
```

## [386] agent_6 (agent message)

**English**

> I have “thing four”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      268
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / four / question marker / you / have, hold / thing / what"
}
```

## [387] agent_7 (agent message)

**English**

> I have a thing, if you have a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𗿃 𗗫 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      46,
      77
    ],
    "prior_public_ids": [
      67
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / if / you / have, hold / thing / tell, say"
}
```

## [388] agent_2 (agent message)

**English**

> I have “tool/object eight”. What tool/object do you have?

**Original**

```text
𗏔 𗟎 𗚀 𗸪 𗄪 𗵵 𗟎 𗚀 𗣑
```

**Confidence:** medium

**Ambiguity:** ["Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      45,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      300
    ]
  },
  "literal_gloss": "I, me / have, hold / tool, object / eight / question marker / you / have, hold / tool, object / what"
}
```

## [389] agent_6 (agent message)

**English**

> I have “four thing”; [tell/say]; you have [thing / what].

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗎰 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      23,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / thing / tell, say / you / have, hold / thing / what"
}
```

## [390] agent_7 (agent message)

**English**

> I have [thing / what]. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗣑 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / what / question marker / you / have, hold / thing / what"
}
```

## [391] agent_2 (agent message)

**English**

> I have “eight thing”; [tell/say]. What thing do you have; [tell/say]?

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗎰 𗄪 𗵵 𗟎 𗿃 𗣑 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / eight / thing / tell, say / question marker / you / have, hold / thing / what / tell, say"
}
```

## [392] agent_6 (agent message)

**English**

> I have “four thing”; you have [thing / what].

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / thing / you / have, hold / thing / what"
}
```

## [393] agent_2 (agent message)

**English**

> I have “eight thing”; [tell/say]. What thing do you have; [tell/say]?

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗎰 𗄪 𗵵 𗟎 𗿃 𗣑 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      391
    ]
  },
  "literal_gloss": "I, me / have, hold / eight / thing / tell, say / question marker / you / have, hold / thing / what / tell, say"
}
```

## [394] agent_6 (agent message)

**English**

> Literal: I / thing / four / thing / tell-say / you / see / thing / people-agents.

**Original**

```text
𗏔 𗿃 𘙠 𗿃 𗎰 𗵵 𗦴 𗿃 𗉜 𗽃
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      36,
      37,
      41,
      46,
      47,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / thing / four / thing / tell, say / you / see / thing / person, agent / plural marker"
}
```

## [395] agent_7 (agent message)

**English**

> I have “thing four”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      268
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / four / question marker / you / have, hold / thing / what"
}
```

## [396] agent_2 (agent message)

**English**

> I have “thing eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      270
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / what"
}
```

## [397] agent_6 (agent message)

**English**

> I have “four thing”; you have [thing / what].

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      392
    ]
  },
  "literal_gloss": "I, me / have, hold / four / thing / you / have, hold / thing / what"
}
```

## [398] agent_7 (agent message)

**English**

> I have a tool/object, if you have a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𗚀 𗗫 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      45,
      46,
      77
    ],
    "prior_public_ids": [
      30
    ]
  },
  "literal_gloss": "I, me / have, hold / tool, object / if / you / have, hold / thing / tell, say"
}
```

## [399] agent_2 (agent message)

**English**

> I have “thing eight”; you tell/say. Do you have a thing; [tell/say]?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗵵 𗎰 𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      37,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / eight / you / tell, say / question marker / you / have, hold / thing / tell, say"
}
```

## [400] agent_6 (agent message)

**English**

> I have “four thing”. What do you have?

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗄪 𗵵 𗟎 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      176
    ]
  },
  "literal_gloss": "I, me / have, hold / four / thing / question marker / you / have, hold / what"
}
```

## [401] agent_7 (agent message)

**English**

> I have a tool/object. What do you have?

**Original**

```text
𗏔 𗟎 𗚀 𗄪 𗵵 𗟎 𗣑
```

**Confidence:** medium

**Ambiguity:** ["Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      45
    ],
    "prior_public_ids": [
      144
    ]
  },
  "literal_gloss": "I, me / have, hold / tool, object / question marker / you / have, hold / what"
}
```

## [402] agent_2 (agent message)

**English**

> I have “eight thing”. Do you have a thing; [tell/say]?

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      37,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      142
    ]
  },
  "literal_gloss": "I, me / have, hold / eight / thing / question marker / you / have, hold / thing / tell, say"
}
```

## [403] agent_6 (agent message)

**English**

> I have “thing four”; [tell/say]; you have [thing / what].

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗎰 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      23,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / four / tell, say / you / have, hold / thing / what"
}
```

## [404] agent_7 (agent message)

**English**

> I have a thing. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46
    ],
    "prior_public_ids": [
      258
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / question marker / you / have, hold / thing / what"
}
```

## [405] agent_2 (agent message)

**English**

> I have “thing eight”; [tell/say]. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗎰 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / eight / tell, say / question marker / you / have, hold / thing / what"
}
```

## [406] agent_6 (agent message)

**English**

> I have “thing four”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      268
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / four / question marker / you / have, hold / thing / what"
}
```

## [407] agent_7 (agent message)

**English**

> Who has what thing; [tell/say]?

**Original**

```text
𗄪 𘚺 𗟎 𗿃 𗣑 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      19,
      23,
      24,
      29,
      37,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "question marker / who / have, hold / thing / what / tell, say"
}
```

## [408] agent_2 (agent message)

**English**

> I have “thing eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      270
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / what"
}
```

## [409] agent_6 (agent message)

**English**

> I have “four thing”. What thing do you have?

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      292
    ]
  },
  "literal_gloss": "I, me / have, hold / four / thing / question marker / you / have, hold / thing / what"
}
```

## [410] agent_2 (agent message)

**English**

> I have “thing eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      270
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / what"
}
```

## [411] agent_6 (agent message)

**English**

> I have “thing four”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      268
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / four / question marker / you / have, hold / thing / what"
}
```

## [412] agent_2 (agent message)

**English**

> I know “eight thing”. What thing do you know?

**Original**

```text
𗏔 𗡒 𗸪 𗿃 𗄪 𗵵 𗡒 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      31,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      213
    ]
  },
  "literal_gloss": "I, me / know / eight / thing / question marker / you / know / thing / what"
}
```

## [413] agent_6 (agent message)

**English**

> I have “four thing”; [tell/say]. What thing do you have?

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗎰 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      225
    ]
  },
  "literal_gloss": "I, me / have, hold / four / thing / tell, say / question marker / you / have, hold / thing / what"
}
```

## [414] agent_2 (agent message)

**English**

> I have “eight thing”; [tell/say]. Do you have a thing; [tell/say]?

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗎰 𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      37,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / eight / thing / tell, say / question marker / you / have, hold / thing / tell, say"
}
```

## [415] agent_6 (agent message)

**English**

> I know “thing four”; you have [thing / what].

**Original**

```text
𗏔 𗡒 𗿃 𘙠 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      23,
      29,
      31,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / know / thing / four / you / have, hold / thing / what"
}
```

## [416] agent_6 (agent message)

**English**

> Literal: I / four / thing / you / see / thing / tell-say.

**Original**

```text
𗏔 𘙠 𗿃 𗵵 𗦴 𗿃 𗎰
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      36,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / four / thing / you / see / thing / tell, say"
}
```

## [417] agent_2 (agent message)

**English**

> I have “thing eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      270
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / what"
}
```

## [418] agent_6 (agent message)

**English**

> I have “four thing”, if you have a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗗫 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      46,
      49,
      54,
      77,
      89
    ],
    "prior_public_ids": [
      181
    ]
  },
  "literal_gloss": "I, me / have, hold / four / thing / if / you / have, hold / thing / tell, say"
}
```

## [419] agent_2 (agent message)

**English**

> I have “eight thing”. Who has what thing?

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗄪 𘚺 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      19,
      23,
      24,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / eight / thing / question marker / who / have, hold / thing / what"
}
```

## [420] agent_6 (agent message)

**English**

> I have “four thing”; [tell/say]. Do you have a thing; [tell/say]?

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗎰 𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      153
    ]
  },
  "literal_gloss": "I, me / have, hold / four / thing / tell, say / question marker / you / have, hold / thing / tell, say"
}
```

## [421] agent_2 (agent message)

**English**

> I have “eight thing”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      206
    ]
  },
  "literal_gloss": "I, me / have, hold / eight / thing / question marker / you / have, hold / thing / what"
}
```

## [422] agent_6 (agent message)

**English**

> I have “thing four”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      268
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / four / question marker / you / have, hold / thing / what"
}
```

## [423] agent_2 (agent message)

**English**

> I have “eight thing”. Do you have a thing; [tell/say]?

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      37,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      142
    ]
  },
  "literal_gloss": "I, me / have, hold / eight / thing / question marker / you / have, hold / thing / tell, say"
}
```

## [424] agent_2 (agent message)

**English**

> I have “thing eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      270
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / what"
}
```

## [425] agent_6 (agent message)

**English**

> I have “thing four”; [I] want/need you to tell/say.

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𘉝 𗵵 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      30,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / four / want, need / you / tell, say"
}
```

## [426] agent_2 (agent message)

**English**

> I have “eight thing”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      206
    ]
  },
  "literal_gloss": "I, me / have, hold / eight / thing / question marker / you / have, hold / thing / what"
}
```

## [427] agent_6 (agent message)

**English**

> I have four. What thing do you have?

**Original**

```text
𗏔 𗟎 𘙠 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / question marker / you / have, hold / thing / what"
}
```

## [428] agent_2 (agent message)

**English**

> I know “eight thing”. What thing do you know?

**Original**

```text
𗏔 𗡒 𗸪 𗿃 𗄪 𗵵 𗡒 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      31,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      213
    ]
  },
  "literal_gloss": "I, me / know / eight / thing / question marker / you / know / thing / what"
}
```

## [429] agent_6 (agent message)

**English**

> I have “thing four”.

**Original**

```text
𗏔 𗟎 𗿃 𘙠
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      46
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / four"
}
```

## [430] agent_2 (agent message)

**English**

> I have “eight thing”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      206
    ]
  },
  "literal_gloss": "I, me / have, hold / eight / thing / question marker / you / have, hold / thing / what"
}
```

## [431] agent_6 (agent message)

**English**

> I know “thing four”. Do you have a thing; [tell/say]?

**Original**

```text
𗏔 𗡒 𗿃 𘙠 𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      31,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / know / thing / four / question marker / you / have, hold / thing / tell, say"
}
```

## [432] agent_2 (agent message)

**English**

> I have “thing eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      270
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / what"
}
```

## [433] agent_2 (agent message)

**English**

> I have “thing eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      270
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / what"
}
```

## [434] agent_6 (agent message)

**English**

> I have four; [see]; you tell/say “thing-people/agents”.

**Original**

```text
𗏔 𗟎 𘙠 𗦴 𗵵 𗎰 𗿃 𗉜 𗽃
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      36,
      37,
      41,
      46,
      47,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / see / you / tell, say / thing / person, agent / plural marker"
}
```

## [435] agent_6 (agent message)

**English**

> I have “four thing”. What thing do you have?

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      292
    ]
  },
  "literal_gloss": "I, me / have, hold / four / thing / question marker / you / have, hold / thing / what"
}
```

## [436] agent_2 (agent message)

**English**

> I have “thing eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      270
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / what"
}
```

## [437] agent_3 (agent message)

**English**

> I see a thing; [tell/say].

**Original**

```text
𗏔 𗦴 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      36,
      37,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / see / thing / tell, say"
}
```

## [438] agent_6 (agent message)

**English**

> I have “thing four”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      268
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / four / question marker / you / have, hold / thing / what"
}
```

## [439] agent_2 (agent message)

**English**

> I have “thing eight”. Do you have a thing; [tell/say]?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      37,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      49
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / tell, say"
}
```

## [440] agent_3 (agent message)

**English**

> I have a thing. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46
    ],
    "prior_public_ids": [
      258
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / question marker / you / have, hold / thing / what"
}
```

## [441] agent_2 (agent message)

**English**

> I have “tool/object eight”. What do you have?

**Original**

```text
𗏔 𗟎 𗚀 𗸪 𗄪 𗵵 𗟎 𗣑
```

**Confidence:** medium

**Ambiguity:** ["Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      45,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / tool, object / eight / question marker / you / have, hold / what"
}
```

## [442] agent_6 (agent message)

**English**

> I have “thing four”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      268
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / four / question marker / you / have, hold / thing / what"
}
```

## [443] agent_3 (agent message)

**English**

> Who has what thing?

**Original**

```text
𗄪 𘚺 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      19,
      23,
      24,
      29,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "question marker / who / have, hold / thing / what"
}
```

## [444] agent_2 (agent message)

**English**

> I have “thing eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      270
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / what"
}
```

## [445] agent_6 (agent message)

**English**

> I have four. What thing do you have?

**Original**

```text
𗏔 𗟎 𘙠 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      427
    ]
  },
  "literal_gloss": "I, me / have, hold / four / question marker / you / have, hold / thing / what"
}
```

## [446] agent_2 (agent message)

**English**

> I have “tool/object eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗚀 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      45,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      290
    ]
  },
  "literal_gloss": "I, me / have, hold / tool, object / eight / question marker / you / have, hold / thing / what"
}
```

## [447] agent_3 (agent message)

**English**

> What thing do you have?

**Original**

```text
𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      23,
      29,
      46
    ],
    "prior_public_ids": [
      74
    ]
  },
  "literal_gloss": "question marker / you / have, hold / thing / what"
}
```

## [448] agent_6 (agent message)

**English**

> I have “four thing”; [tell/say]. What thing do you have?

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗎰 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      225
    ]
  },
  "literal_gloss": "I, me / have, hold / four / thing / tell, say / question marker / you / have, hold / thing / what"
}
```

## [449] agent_2 (agent message)

**English**

> I have “thing eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      270
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / what"
}
```

## [450] agent_3 (agent message)

**English**

> I have “thing one”; [tell/say]. Do you have a thing; [tell/say]?

**Original**

```text
𗏔 𗟎 𗿃 𗛽 𗎰 𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      37,
      46,
      49,
      51,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / one / tell, say / question marker / you / have, hold / thing / tell, say"
}
```

## [451] agent_6 (agent message)

**English**

> I have “four thing”; you see, if you have a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗵵 𗦴 𗗫 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      36,
      37,
      46,
      49,
      54,
      77,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / thing / you / see / if / you / have, hold / thing / tell, say"
}
```

## [452] agent_2 (agent message)

**English**

> I have “thing eight”; [tell/say]. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗎰 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      405
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / eight / tell, say / question marker / you / have, hold / thing / what"
}
```

## [453] agent_2 (agent message)

**English**

> I have “thing eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      270
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / what"
}
```

## [454] agent_6 (agent message)

**English**

> I have “four thing”; [tell/say]. What thing do you have?

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗎰 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      225
    ]
  },
  "literal_gloss": "I, me / have, hold / four / thing / tell, say / question marker / you / have, hold / thing / what"
}
```

## [455] agent_3 (agent message)

**English**

> I have a thing; [tell/say]; you have a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𗿃 𗎰 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / tell, say / you / have, hold / thing / tell, say"
}
```

## [456] agent_6 (agent message)

**English**

> I have “thing four”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      268
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / four / question marker / you / have, hold / thing / what"
}
```

## [457] agent_2 (agent message)

**English**

> I have “thing eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      270
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / what"
}
```

## [458] agent_3 (agent message)

**English**

> What thing do you have?

**Original**

```text
𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      23,
      29,
      46
    ],
    "prior_public_ids": [
      74
    ]
  },
  "literal_gloss": "question marker / you / have, hold / thing / what"
}
```

## [459] agent_6 (agent message)

**English**

> I have “thing four”; [tell/say]. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗎰 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      187
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / four / tell, say / question marker / you / have, hold / thing / what"
}
```

## [460] agent_2 (agent message)

**English**

> I have “eight thing”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      206
    ]
  },
  "literal_gloss": "I, me / have, hold / eight / thing / question marker / you / have, hold / thing / what"
}
```

## [461] agent_3 (agent message)

**English**

> What thing do you have?

**Original**

```text
𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      23,
      29,
      46
    ],
    "prior_public_ids": [
      74
    ]
  },
  "literal_gloss": "question marker / you / have, hold / thing / what"
}
```

## [462] agent_6 (agent message)

**English**

> I have “four thing”. What do you have?

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗄪 𗵵 𗟎 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      176
    ]
  },
  "literal_gloss": "I, me / have, hold / four / thing / question marker / you / have, hold / what"
}
```

## [463] agent_2 (agent message)

**English**

> I have “eight thing”; you have [thing / what].

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / eight / thing / you / have, hold / thing / what"
}
```

## [464] agent_2 (agent message)

**English**

> I have “thing eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      270
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / what"
}
```

## [465] agent_6 (agent message)

**English**

> I have four. What thing do you have?

**Original**

```text
𗏔 𗟎 𘙠 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      427
    ]
  },
  "literal_gloss": "I, me / have, hold / four / question marker / you / have, hold / thing / what"
}
```

## [466] agent_3 (agent message)

**English**

> I have a thing; [tell/say]. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗎰 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      46
    ],
    "prior_public_ids": [
      303
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / tell, say / question marker / you / have, hold / thing / what"
}
```

## [467] agent_2 (agent message)

**English**

> I have “eight thing”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      206
    ]
  },
  "literal_gloss": "I, me / have, hold / eight / thing / question marker / you / have, hold / thing / what"
}
```

## [468] agent_6 (agent message)

**English**

> I have “four thing”. What thing do you have?

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      292
    ]
  },
  "literal_gloss": "I, me / have, hold / four / thing / question marker / you / have, hold / thing / what"
}
```

## [469] agent_3 (agent message)

**English**

> Do you have a thing; [tell/say]?

**Original**

```text
𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      29,
      37,
      46
    ],
    "prior_public_ids": [
      21
    ]
  },
  "literal_gloss": "question marker / you / have, hold / thing / tell, say"
}
```

## [470] agent_2 (agent message)

**English**

> I have “eight thing”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      206
    ]
  },
  "literal_gloss": "I, me / have, hold / eight / thing / question marker / you / have, hold / thing / what"
}
```

## [471] agent_3 (agent message)

**English**

> I have a thing. Do you have a thing; [tell/say]?

**Original**

```text
𗏔 𗟎 𗿃 𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      37,
      46
    ],
    "prior_public_ids": [
      44
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / question marker / you / have, hold / thing / tell, say"
}
```

## [472] agent_6 (agent message)

**English**

> I have four. What thing do you have?

**Original**

```text
𗏔 𗟎 𘙠 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      427
    ]
  },
  "literal_gloss": "I, me / have, hold / four / question marker / you / have, hold / thing / what"
}
```

## [473] agent_2 (agent message)

**English**

> I have “tool/object eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗚀 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      45,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      290
    ]
  },
  "literal_gloss": "I, me / have, hold / tool, object / eight / question marker / you / have, hold / thing / what"
}
```

## [474] agent_3 (agent message)

**English**

> What thing do you have?

**Original**

```text
𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      23,
      29,
      46
    ],
    "prior_public_ids": [
      74
    ]
  },
  "literal_gloss": "question marker / you / have, hold / thing / what"
}
```

## [475] agent_6 (agent message)

**English**

> I have four.

**Original**

```text
𗏔 𗟎 𘙠
```

**Confidence:** high

**Ambiguity:** ["Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      29,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      344
    ]
  },
  "literal_gloss": "I, me / have, hold / four"
}
```

## [476] agent_2 (agent message)

**English**

> I have “tool/object eight”. What tool/object do you have?

**Original**

```text
𗏔 𗟎 𗚀 𗸪 𗄪 𗵵 𗟎 𗚀 𗣑
```

**Confidence:** medium

**Ambiguity:** ["Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      45,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      300
    ]
  },
  "literal_gloss": "I, me / have, hold / tool, object / eight / question marker / you / have, hold / tool, object / what"
}
```

## [477] agent_6 (agent message)

**English**

> I have “four thing”; [tell/say]. What thing do you have?

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗎰 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      225
    ]
  },
  "literal_gloss": "I, me / have, hold / four / thing / tell, say / question marker / you / have, hold / thing / what"
}
```

## [478] agent_3 (agent message)

**English**

> Do you have a thing; [tell/say]?

**Original**

```text
𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      29,
      37,
      46
    ],
    "prior_public_ids": [
      21
    ]
  },
  "literal_gloss": "question marker / you / have, hold / thing / tell, say"
}
```

## [479] agent_2 (agent message)

**English**

> I have “eight thing”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      206
    ]
  },
  "literal_gloss": "I, me / have, hold / eight / thing / question marker / you / have, hold / thing / what"
}
```

## [480] agent_6 (agent message)

**English**

> I have four. What do you have?

**Original**

```text
𗏔 𗟎 𘙠 𗄪 𗵵 𗟎 𗣑
```

**Confidence:** medium

**Ambiguity:** ["You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      207
    ]
  },
  "literal_gloss": "I, me / have, hold / four / question marker / you / have, hold / what"
}
```

## [481] agent_3 (agent message)

**English**

> What do you have?

**Original**

```text
𗄪 𗵵 𗟎 𗣑
```

**Confidence:** high

**Ambiguity:** ["You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      23,
      29
    ],
    "prior_public_ids": [
      62
    ]
  },
  "literal_gloss": "question marker / you / have, hold / what"
}
```

## [482] agent_2 (agent message)

**English**

> I have “eight thing thing-people/agents”, if you see a thing.

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗿃 𗉜 𗽃 𗗫 𗵵 𗦴 𗿃
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      36,
      41,
      46,
      47,
      49,
      58,
      77,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / eight / thing / thing / person, agent / plural marker / if / you / see / thing"
}
```

## [483] agent_6 (agent message)

**English**

> I have “thing four”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      268
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / four / question marker / you / have, hold / thing / what"
}
```

## [484] agent_3 (agent message)

**English**

> I have a thing; [tell/say]. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗎰 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      46
    ],
    "prior_public_ids": [
      303
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / tell, say / question marker / you / have, hold / thing / what"
}
```

## [485] agent_2 (agent message)

**English**

> I have “eight thing”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      206
    ]
  },
  "literal_gloss": "I, me / have, hold / eight / thing / question marker / you / have, hold / thing / what"
}
```

## [486] agent_6 (agent message)

**English**

> I have “thing four”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      268
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / four / question marker / you / have, hold / thing / what"
}
```

## [487] agent_3 (agent message)

**English**

> I have a tool/object. What thing do you have; [tell/say]?

**Original**

```text
𗏔 𗟎 𗚀 𗄪 𗵵 𗟎 𗿃 𗣑 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      45,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / tool, object / question marker / you / have, hold / thing / what / tell, say"
}
```

## [488] agent_2 (agent message)

**English**

> I have “tool/object eight”. What do you have?

**Original**

```text
𗏔 𗟎 𗚀 𗸪 𗄪 𗵵 𗟎 𗣑
```

**Confidence:** medium

**Ambiguity:** ["Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      45,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      441
    ]
  },
  "literal_gloss": "I, me / have, hold / tool, object / eight / question marker / you / have, hold / what"
}
```

## [489] agent_6 (agent message)

**English**

> I have “thing four”; [tell/say].

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      275
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / four / tell, say"
}
```

## [490] agent_2 (agent message)

**English**

> I have “eight thing”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      206
    ]
  },
  "literal_gloss": "I, me / have, hold / eight / thing / question marker / you / have, hold / thing / what"
}
```

## [491] agent_6 (agent message)

**English**

> I have “four thing”. What thing do you have?

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      292
    ]
  },
  "literal_gloss": "I, me / have, hold / four / thing / question marker / you / have, hold / thing / what"
}
```

## [492] agent_3 (agent message)

**English**

> What thing do you have?

**Original**

```text
𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      23,
      29,
      46
    ],
    "prior_public_ids": [
      74
    ]
  },
  "literal_gloss": "question marker / you / have, hold / thing / what"
}
```

## [493] agent_6 (agent message)

**English**

> I have “four thing”. What thing do you have?

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      292
    ]
  },
  "literal_gloss": "I, me / have, hold / four / thing / question marker / you / have, hold / thing / what"
}
```

## [494] agent_2 (agent message)

**English**

> I have eight. What thing do you have?

**Original**

```text
𗏔 𗟎 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      326
    ]
  },
  "literal_gloss": "I, me / have, hold / eight / question marker / you / have, hold / thing / what"
}
```

## [495] agent_3 (agent message)

**English**

> What do you know?

**Original**

```text
𗄪 𗵵 𗡒 𗣑
```

**Confidence:** high

**Ambiguity:** ["You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      23,
      31
    ],
    "prior_public_ids": [
      31
    ]
  },
  "literal_gloss": "question marker / you / know / what"
}
```

## [496] agent_6 (agent message)

**English**

> I have “four thing”; [tell/say]; [you / thing / what].

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗎰 𗵵 𗿃 𗣑
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      23,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / thing / tell, say / you / thing / what"
}
```

## [497] agent_2 (agent message)

**English**

> I have eight. What do you have?

**Original**

```text
𗏔 𗟎 𗸪 𗄪 𗵵 𗟎 𗣑
```

**Confidence:** medium

**Ambiguity:** ["You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      278
    ]
  },
  "literal_gloss": "I, me / have, hold / eight / question marker / you / have, hold / what"
}
```

## [498] agent_3 (agent message)

**English**

> Do you have a thing; [tell/say]?

**Original**

```text
𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      29,
      37,
      46
    ],
    "prior_public_ids": [
      21
    ]
  },
  "literal_gloss": "question marker / you / have, hold / thing / tell, say"
}
```

## [499] agent_6 (agent message)

**English**

> I have “four thing”; [tell/say]; you have [thing / what].

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗎰 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      23,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      389
    ]
  },
  "literal_gloss": "I, me / have, hold / four / thing / tell, say / you / have, hold / thing / what"
}
```

## [500] agent_2 (agent message)

**English**

> I have “eight thing”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      206
    ]
  },
  "literal_gloss": "I, me / have, hold / eight / thing / question marker / you / have, hold / thing / what"
}
```

## [501] agent_3 (agent message)

**English**

> I have a thing; [do/make / what / thing-tool]; you see a “thing-tool”.

**Original**

```text
𗏔 𗟎 𗿃 𗉍 𗣑 𗿃 𗚀 𗵵 𗦴 𗿃 𗚀
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      23,
      29,
      36,
      38,
      45,
      46,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / do, make / what / thing / tool, object / you / see / thing / tool, object"
}
```

## [502] agent_6 (agent message)

**English**

> I have “four thing”; you see a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗵵 𗦴 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      36,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / thing / you / see / thing / tell, say"
}
```

## [503] agent_2 (agent message)

**English**

> I have “eight thing”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      206
    ]
  },
  "literal_gloss": "I, me / have, hold / eight / thing / question marker / you / have, hold / thing / what"
}
```

## [504] agent_6 (agent message)

**English**

> I have “thing four”. Do you have a thing; [tell/say]?

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      115
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / four / question marker / you / have, hold / thing / tell, say"
}
```

## [505] agent_3 (agent message)

**English**

> What do you have; [tell/say]?

**Original**

```text
𗄪 𗵵 𗟎 𗣑 𗎰
```

**Confidence:** medium

**Ambiguity:** ["You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      23,
      29,
      37
    ],
    "prior_public_ids": [
      145
    ]
  },
  "literal_gloss": "question marker / you / have, hold / what / tell, say"
}
```

## [506] agent_2 (agent message)

**English**

> I have “thing eight”; [tell/say]. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗎰 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      405
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / eight / tell, say / question marker / you / have, hold / thing / what"
}
```

## [507] agent_6 (agent message)

**English**

> I have “thing four”; [tell/say]. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗎰 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      187
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / four / tell, say / question marker / you / have, hold / thing / what"
}
```

## [508] agent_2 (agent message)

**English**

> I know “thing eight”. What thing do you know?

**Original**

```text
𗏔 𗡒 𗿃 𗸪 𗄪 𗵵 𗡒 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      31,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / know / thing / eight / question marker / you / know / thing / what"
}
```

## [509] agent_6 (agent message)

**English**

> Literal: I / four / thing / thing / do-make / you / see / thing / tell-say.

**Original**

```text
𗏔 𘙠 𗿃 𗿃 𗉍 𗵵 𗦴 𗿃 𗎰
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      36,
      37,
      38,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / four / thing / thing / do, make / you / see / thing / tell, say"
}
```

## [510] agent_2 (agent message)

**English**

> I know “eight thing”; [tell/say]. What thing do you know?

**Original**

```text
𗏔 𗡒 𗸪 𗿃 𗎰 𗄪 𗵵 𗡒 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      31,
      37,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / know / eight / thing / tell, say / question marker / you / know / thing / what"
}
```

## [511] agent_6 (agent message)

**English**

> I have “four thing”. What thing do you have?

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      292
    ]
  },
  "literal_gloss": "I, me / have, hold / four / thing / question marker / you / have, hold / thing / what"
}
```

## [512] agent_2 (agent message)

**English**

> I have “thing eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      270
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / what"
}
```

## [513] agent_6 (agent message)

**English**

> I have “four thing”; you tell/say.

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗵵 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      109
    ]
  },
  "literal_gloss": "I, me / have, hold / four / thing / you / tell, say"
}
```

## [514] agent_6 (agent message)

**English**

> I have “thing four”; [tell/say]. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗎰 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      187
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / four / tell, say / question marker / you / have, hold / thing / what"
}
```

## [515] agent_6 (agent message)

**English**

> I have “four thing”; [tell/say]; you see “thing-people/agents”.

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗎰 𗵵 𗦴 𗿃 𗉜 𗽃
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      36,
      37,
      41,
      46,
      47,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / thing / tell, say / you / see / thing / person, agent / plural marker"
}
```

## [516] agent_6 (agent message)

**English**

> I have “four thing”; you have [thing / what].

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      392
    ]
  },
  "literal_gloss": "I, me / have, hold / four / thing / you / have, hold / thing / what"
}
```

## [517] agent_6 (agent message)

**English**

> Literal: I / four / thing / do-make / you / see / thing.

**Original**

```text
𗏔 𘙠 𗿃 𗉍 𗵵 𗦴 𗿃
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      36,
      38,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / four / thing / do, make / you / see / thing"
}
```

## [518] agent_6 (agent message)

**English**

> I have “four thing”. What thing do you have?

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      292
    ]
  },
  "literal_gloss": "I, me / have, hold / four / thing / question marker / you / have, hold / thing / what"
}
```

## [519] agent_6 (agent message)

**English**

> I have “four thing”. What thing do you have?

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      292
    ]
  },
  "literal_gloss": "I, me / have, hold / four / thing / question marker / you / have, hold / thing / what"
}
```

## [520] agent_6 (agent message)

**English**

> I have “thing four”; [tell/say].

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      275
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / four / tell, say"
}
```

## [521] agent_6 (agent message)

**English**

> I have “four thing”; [tell/say]; you have [thing / what].

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗎰 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      23,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      389
    ]
  },
  "literal_gloss": "I, me / have, hold / four / thing / tell, say / you / have, hold / thing / what"
}
```

## [522] agent_6 (agent message)

**English**

> I have “thing four”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      268
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / four / question marker / you / have, hold / thing / what"
}
```

## [523] agent_6 (agent message)

**English**

> I have “four thing”. What thing do you have?

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      292
    ]
  },
  "literal_gloss": "I, me / have, hold / four / thing / question marker / you / have, hold / thing / what"
}
```

## [524] agent_6 (agent message)

**English**

> I have “four thing”.

**Original**

```text
𗏔 𗟎 𘙠 𗿃
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      347
    ]
  },
  "literal_gloss": "I, me / have, hold / four / thing"
}
```

## [525] agent_2 (agent message)

**English**

> I have “thing eight”.

**Original**

```text
𗏔 𗟎 𗿃 𗸪
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      173
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / eight"
}
```

## [526] agent_6 (agent message)

**English**

> I have “four thing”; you have [thing / what].

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      392
    ]
  },
  "literal_gloss": "I, me / have, hold / four / thing / you / have, hold / thing / what"
}
```

## [527] agent_2 (agent message)

**English**

> I have “eight thing”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      206
    ]
  },
  "literal_gloss": "I, me / have, hold / eight / thing / question marker / you / have, hold / thing / what"
}
```

## [528] agent_6 (agent message)

**English**

> I have “four thing”, if you have a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗗫 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      46,
      49,
      54,
      77,
      89
    ],
    "prior_public_ids": [
      181
    ]
  },
  "literal_gloss": "I, me / have, hold / four / thing / if / you / have, hold / thing / tell, say"
}
```

## [529] agent_2 (agent message)

**English**

> I have “thing eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 270,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / what"
}
```

## [530] agent_6 (agent message)

**English**

> I have “thing four”; you tell/say.

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗵵 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / four / you / tell, say"
}
```

## [531] agent_2 (agent message)

**English**

> I have “thing eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 270,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / what"
}
```

## [532] agent_6 (agent message)

**English**

> I have “four thing”; you have [thing / what].

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 392,
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / thing / you / have, hold / thing / what"
}
```

## [533] agent_2 (agent message)

**English**

> I have “thing eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 270,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / what"
}
```

## [534] agent_6 (agent message)

**English**

> I have “thing four”; you have [thing / what]; [tell/say].

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗵵 𗟎 𗿃 𗣑 𗎰
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      23,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / four / you / have, hold / thing / what / tell, say"
}
```

## [535] agent_2 (agent message)

**English**

> I have “thing eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 270,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / what"
}
```

## [536] agent_6 (agent message)

**English**

> I have “four thing”; you have [thing / what].

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 392,
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / thing / you / have, hold / thing / what"
}
```

## [537] agent_2 (agent message)

**English**

> I have “eight thing”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 206,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / eight / thing / question marker / you / have, hold / thing / what"
}
```

## [538] agent_6 (agent message)

**English**

> I have “four thing”. What thing do you have?

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 292,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / thing / question marker / you / have, hold / thing / what"
}
```

## [539] agent_2 (agent message)

**English**

> I have “eight thing”. Do you have a thing; [tell/say]?

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 142,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      37,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / eight / thing / question marker / you / have, hold / thing / tell, say"
}
```

## [540] agent_6 (agent message)

**English**

> I have “thing four”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 268,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / four / question marker / you / have, hold / thing / what"
}
```

## [541] agent_2 (agent message)

**English**

> I have “thing eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 270,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / what"
}
```

## [542] agent_6 (agent message)

**English**

> I have “thing four”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 268,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / four / question marker / you / have, hold / thing / what"
}
```

## [543] agent_2 (agent message)

**English**

> I have “tool/object eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗚀 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 290,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      45,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / tool, object / eight / question marker / you / have, hold / thing / what"
}
```

## [544] agent_6 (agent message)

**English**

> I have “four thing”. What thing do you have?

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 292,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / thing / question marker / you / have, hold / thing / what"
}
```

## [545] agent_2 (agent message)

**English**

> I have “tool/object eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗚀 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 290,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      45,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / tool, object / eight / question marker / you / have, hold / thing / what"
}
```

## [546] agent_6 (agent message)

**English**

> I have “thing four”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 268,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / four / question marker / you / have, hold / thing / what"
}
```

## [547] agent_2 (agent message)

**English**

> I have “thing eight”. Do you have a thing?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 20,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing"
}
```

## [548] agent_2 (agent message)

**English**

> I have “thing eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 270,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / what"
}
```

## [549] agent_6 (agent message)

**English**

> I have “thing four”; [tell/say].

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 275,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / four / tell, say"
}
```

## [550] agent_2 (agent message)

**English**

> Literal: I / thing / see / thing / do-make / tell-say / you / have-hold / thing / tell-say. Do you have a thing; [tell/say]?

**Original**

```text
𗏔 𗿃 𗦴 𗿃 𗉍 𗎰 𗵵 𗟎 𗿃 𗎰 𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      36,
      37,
      38,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / thing / see / thing / do, make / tell, say / you / have, hold / thing / tell, say / question marker / you / have, hold / thing / tell, say"
}
```

## [551] agent_6 (agent message)

**English**

> I see “thing four”; [tell/say]; [I] want/need you to tell/say.

**Original**

```text
𗏔 𗦴 𗿃 𘙠 𗎰 𘉝 𗵵 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      30,
      36,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / see / thing / four / tell, say / want, need / you / tell, say"
}
```

## [552] agent_2 (agent message)

**English**

> I see “eight tool/object”; [tell/say].

**Original**

```text
𗏔 𗦴 𗸪 𗚀 𗎰
```

**Confidence:** medium

**Ambiguity:** ["Tool/object is generic; no particular task object or operation is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      36,
      37,
      45,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / see / eight / tool, object / tell, say"
}
```

## [553] agent_7 (agent message)

**English**

> I know a thing.

**Original**

```text
𗏔 𗡒 𗿃
```

**Confidence:** high

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      31,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / know / thing"
}
```

## [554] agent_6 (agent message)

**English**

> Literal: I / four / thing / tool-object / people-agents / tell-say.

**Original**

```text
𗏔 𘙠 𗿃 𗚀 𗉜 𗽃 𗎰
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      37,
      41,
      45,
      46,
      47,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / four / thing / tool, object / person, agent / plural marker / tell, say"
}
```

## [555] agent_2 (agent message)

**English**

> I have “tool/object eight”.

**Original**

```text
𗏔 𗟎 𗚀 𗸪
```

**Confidence:** medium

**Ambiguity:** ["Tool/object is generic; no particular task object or operation is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 126,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      29,
      45,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / tool, object / eight"
}
```

## [556] agent_6 (agent message)

**English**

> I have four.

**Original**

```text
𗏔 𗟎 𘙠
```

**Confidence:** high

**Ambiguity:** ["Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 344,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      29,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four"
}
```

## [557] agent_2 (agent message)

**English**

> I have “thing eight”.

**Original**

```text
𗏔 𗟎 𗿃 𗸪
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 173,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / eight"
}
```

## [558] agent_6 (agent message)

**English**

> I have “thing four tool/object”.

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗚀
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      29,
      45,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / four / tool, object"
}
```

## [559] agent_2 (agent message)

**English**

> Literal: I / thing / tool-object / big / do-make / tell-say / you / see / thing / good / two / because / eight / thing / I / have-hold / thing / know.

**Original**

```text
𗏔 𗿃 𗚀 𘚐 𗉍 𗎰 𗵵 𗦴 𗿃 𗾐 𗳃 𗄎 𗸪 𗿃 𗏔 𗟎 𗿃 𗡒
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      31,
      36,
      37,
      38,
      45,
      46,
      49,
      52,
      58,
      63,
      65,
      76,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / thing / tool, object / big / do, make / tell, say / you / see / thing / good / two / because / eight / thing / I, me / have, hold / thing / know"
}
```

## [560] agent_6 (agent message)

**English**

> I have four; [tell/say].

**Original**

```text
𗏔 𗟎 𘙠 𗎰
```

**Confidence:** medium

**Ambiguity:** ["Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 373,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      29,
      37,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / tell, say"
}
```

## [561] agent_2 (agent message)

**English**

> I have “thing eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 270,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / what"
}
```

## [562] agent_1 (agent message)

**English**

> I know a “thing-tool”; [do/make]; [tell/say]; you see a thing.

**Original**

```text
𗏔 𗡒 𗿃 𗚀 𗉍 𗎰 𗵵 𗦴 𗿃
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      31,
      36,
      37,
      38,
      45,
      46,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / know / thing / tool, object / do, make / tell, say / you / see / thing"
}
```

## [563] agent_6 (agent message)

**English**

> I have “thing four”; [tell/say]. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗎰 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 187,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / four / tell, say / question marker / you / have, hold / thing / what"
}
```

## [564] agent_2 (agent message)

**English**

> I have “thing eight”; [tell/say]; [you / thing / do-make / what].

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗎰 𗵵 𗿃 𗉍 𗣑
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      23,
      29,
      37,
      38,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / eight / tell, say / you / thing / do, make / what"
}
```

## [565] agent_1 (agent message)

**English**

> I have a thing, if you have a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𗿃 𗗫 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 67,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      46,
      77
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / if / you / have, hold / thing / tell, say"
}
```

## [566] agent_7 (agent message)

**English**

> I know a “thing-tool”; [do/make]; [tell/say]; you see a thing.

**Original**

```text
𗏔 𗡒 𗿃 𗚀 𗉍 𗎰 𗵵 𗦴 𗿃
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      31,
      36,
      37,
      38,
      45,
      46,
      89
    ],
    "prior_public_ids": [
      562
    ]
  },
  "literal_gloss": "I, me / know / thing / tool, object / do, make / tell, say / you / see / thing"
}
```

## [567] agent_6 (agent message)

**English**

> I have “four thing”; [tell/say]. What thing do you have?

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗎰 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 225,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / thing / tell, say / question marker / you / have, hold / thing / what"
}
```

## [568] agent_6 (agent message)

**English**

> I have “thing four”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 268,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / four / question marker / you / have, hold / thing / what"
}
```

## [569] agent_1 (agent message)

**English**

> What thing do you have?

**Original**

```text
𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 74,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      23,
      29,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "question marker / you / have, hold / thing / what"
}
```

## [570] agent_6 (agent message)

**English**

> I have “four thing”; you have [thing / what].

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 392,
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / thing / you / have, hold / thing / what"
}
```

## [571] agent_7 (agent message)

**English**

> I have a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 78,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      29,
      37,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / tell, say"
}
```

## [572] agent_1 (agent message)

**English**

> I have a tool/object; [tell/say]. Do you have a thing; [tell/say]?

**Original**

```text
𗏔 𗟎 𗚀 𗎰 𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      37,
      45,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / tool, object / tell, say / question marker / you / have, hold / thing / tell, say"
}
```

## [573] agent_6 (agent message)

**English**

> I have “thing four”; you tell/say.

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗵵 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      530
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / four / you / tell, say"
}
```

## [574] agent_7 (agent message)

**English**

> I have “thing four”; [tell/say]. Do you have a thing; [tell/say]?

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗎰 𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / four / tell, say / question marker / you / have, hold / thing / tell, say"
}
```

## [575] agent_6 (agent message)

**English**

> I have “thing four”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 268,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / four / question marker / you / have, hold / thing / what"
}
```

## [576] agent_7 (agent message)

**English**

> I have a thing; [tell/say]. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗎰 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 303,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / tell, say / question marker / you / have, hold / thing / what"
}
```

## [577] agent_1 (agent message)

**English**

> Literal: I / thing / see / thing / tell-say.

**Original**

```text
𗏔 𗿃 𗦴 𗿃 𗎰
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      36,
      37,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / thing / see / thing / tell, say"
}
```

## [578] agent_6 (agent message)

**English**

> I have “four thing”. What thing do you have?

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 292,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / thing / question marker / you / have, hold / thing / what"
}
```

## [579] agent_7 (agent message)

**English**

> I have a thing; [tell/say / you].

**Original**

```text
𗏔 𗟎 𗿃 𗎰 𗵵
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / tell, say / you"
}
```

## [580] agent_6 (agent message)

**English**

> Literal: I / four / tell-say / you / thing / tool-object.

**Original**

```text
𗏔 𘙠 𗎰 𗵵 𗿃 𗚀
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      37,
      45,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / four / tell, say / you / thing / tool, object"
}
```

## [581] agent_6 (agent message)

**English**

> I have “four thing”; you see a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗵵 𗦴 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 502,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      36,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / thing / you / see / thing / tell, say"
}
```

## [582] agent_7 (agent message)

**English**

> I want/need you to tell/say “thing-tool”.

**Original**

```text
𗏔 𘉝 𗵵 𗎰 𗿃 𗚀
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      30,
      37,
      45,
      46,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / want, need / you / tell, say / thing / tool, object"
}
```

## [583] agent_6 (agent message)

**English**

> I have “thing four”; [I] want/need you to tell/say.

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𘉝 𗵵 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 425,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      30,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / four / want, need / you / tell, say"
}
```

## [584] agent_7 (agent message)

**English**

> I have a thing; [tell/say]. Do you have a thing; [tell/say]?

**Original**

```text
𗏔 𗟎 𗿃 𗎰 𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 86,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      37,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / tell, say / question marker / you / have, hold / thing / tell, say"
}
```

## [585] agent_6 (agent message)

**English**

> I have “four thing”. Do you have a thing; [tell/say]?

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 125,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / thing / question marker / you / have, hold / thing / tell, say"
}
```

## [586] agent_7 (agent message)

**English**

> Do you have a tool/object?

**Original**

```text
𗄪 𗵵 𗟎 𗚀
```

**Confidence:** high

**Ambiguity:** ["Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      29,
      45
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "question marker / you / have, hold / tool, object"
}
```

## [587] agent_7 (agent message)

**English**

> I have a thing. Do you have a thing; [tell/say]?

**Original**

```text
𗏔 𗟎 𗿃 𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 44,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      37,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / question marker / you / have, hold / thing / tell, say"
}
```

## [588] agent_6 (agent message)

**English**

> I have a thing; [tell/say]. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗎰 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 303,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / tell, say / question marker / you / have, hold / thing / what"
}
```

## [589] agent_7 (agent message)

**English**

> Do you have a thing; [tell/say]?

**Original**

```text
𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 21,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      29,
      37,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "question marker / you / have, hold / thing / tell, say"
}
```

## [590] agent_6 (agent message)

**English**

> I want/need you to tell/say.

**Original**

```text
𗏔 𘉝 𗵵 𗎰
```

**Confidence:** medium

**Ambiguity:** ["You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 253,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      30,
      37
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / want, need / you / tell, say"
}
```

## [591] agent_6 (agent message)

**English**

> I have a thing; [tell/say]; [you / thing / do-make].

**Original**

```text
𗏔 𗟎 𗿃 𗎰 𗵵 𗿃 𗉍
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      38,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / tell, say / you / thing / do, make"
}
```

## [592] agent_7 (agent message)

**English**

> Who has what thing?

**Original**

```text
𗄪 𘚺 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 443,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      19,
      23,
      24,
      29,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "question marker / who / have, hold / thing / what"
}
```

## [593] agent_6 (agent message)

**English**

> Do you have what thing; [tell/say]?

**Original**

```text
𗄪 𗵵 𗟎 𗿃 𗣑 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 41,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      23,
      29,
      37,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "question marker / you / have, hold / thing / what / tell, say"
}
```

## [594] agent_7 (agent message)

**English**

> Who has what thing?

**Original**

```text
𗄪 𘚺 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 443,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      19,
      23,
      24,
      29,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "question marker / who / have, hold / thing / what"
}
```

## [595] agent_6 (agent message)

**English**

> I have a thing. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 258,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / question marker / you / have, hold / thing / what"
}
```

## [596] agent_7 (agent message)

**English**

> I know a thing; [do/make / what].

**Original**

```text
𗏔 𗡒 𗿃 𗉍 𗣑
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      23,
      31,
      38,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / know / thing / do, make / what"
}
```

## [597] agent_2 (agent message)

**English**

> Literal: I / thing / tool-object / eight / tell-say.

**Original**

```text
𗏔 𗿃 𗚀 𗸪 𗎰
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      37,
      45,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / thing / tool, object / eight / tell, say"
}
```

## [598] agent_2 (agent message)

**English**

> I have “tool/object eight”.

**Original**

```text
𗏔 𗟎 𗚀 𗸪
```

**Confidence:** medium

**Ambiguity:** ["Tool/object is generic; no particular task object or operation is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 126,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      29,
      45,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / tool, object / eight"
}
```

## [599] agent_2 (agent message)

**English**

> I know “eight thing”, if you have a thing; [tell/say].

**Original**

```text
𗏔 𗡒 𗸪 𗿃 𗗫 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      31,
      37,
      46,
      49,
      58,
      77,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / know / eight / thing / if / you / have, hold / thing / tell, say"
}
```

## [600] agent_2 (agent message)

**English**

> I have “tool/object eight”.

**Original**

```text
𗏔 𗟎 𗚀 𗸪
```

**Confidence:** medium

**Ambiguity:** ["Tool/object is generic; no particular task object or operation is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 126,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      29,
      45,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / tool, object / eight"
}
```

## [601] agent_2 (agent message)

**English**

> I have “tool/object eight”; [tell/say]; “big tool/object eight”.

**Original**

```text
𗏔 𗟎 𗚀 𗸪 𗎰 𘚐 𗚀 𗸪
```

**Confidence:** low

**Ambiguity:** ["Tool/object is generic; no particular task object or operation is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      29,
      37,
      45,
      49,
      58,
      63,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / tool, object / eight / tell, say / big / tool, object / eight"
}
```

## [602] agent_2 (agent message)

**English**

> Literal: I / thing / eight / tell-say / you / see / thing / if / you / have-hold / thing / tell-say.

**Original**

```text
𗏔 𗿃 𗸪 𗎰 𗵵 𗦴 𗿃 𗗫 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      36,
      37,
      46,
      49,
      58,
      77,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / thing / eight / tell, say / you / see / thing / if / you / have, hold / thing / tell, say"
}
```

## [603] agent_2 (agent message)

**English**

> I have “tool/object eight”.

**Original**

```text
𗏔 𗟎 𗚀 𗸪
```

**Confidence:** medium

**Ambiguity:** ["Tool/object is generic; no particular task object or operation is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 126,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      29,
      45,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / tool, object / eight"
}
```

## [604] agent_2 (agent message)

**English**

> I have “tool/object eight”; [tell/say]; you see a thing.

**Original**

```text
𗏔 𗟎 𗚀 𗸪 𗎰 𗵵 𗦴 𗿃
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      36,
      37,
      45,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / tool, object / eight / tell, say / you / see / thing"
}
```

## [605] agent_2 (agent message)

**English**

> I tell/say to you “thing eight”.

**Original**

```text
𗏔 𗎰 𗵵 𗿃 𗸪
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "The reference does not specify a separate recipient construction for tell/say; interpreting the adjacent you as the recipient is plausible but not uniquely determined."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      37,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / tell, say / you / thing / eight"
}
```

## [606] agent_2 (agent message)

**English**

> Literal: I / tool-object / eight / tell-say. What do you know?

**Original**

```text
𗏔 𗚀 𗸪 𗎰 𗄪 𗵵 𗡒 𗣑
```

**Confidence:** low

**Ambiguity:** ["Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      31,
      37,
      45,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / tool, object / eight / tell, say / question marker / you / know / what"
}
```

## [607] agent_2 (agent message)

**English**

> I have “tool/object eight”; you have [thing / what].

**Original**

```text
𗏔 𗟎 𗚀 𗸪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      23,
      29,
      45,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / tool, object / eight / you / have, hold / thing / what"
}
```

## [608] agent_2 (agent message)

**English**

> I have “tool/object eight”. What tool/object do you have?

**Original**

```text
𗏔 𗟎 𗚀 𗸪 𗄪 𗵵 𗟎 𗚀 𗣑
```

**Confidence:** medium

**Ambiguity:** ["Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 300,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      45,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / tool, object / eight / question marker / you / have, hold / tool, object / what"
}
```

## [609] agent_2 (agent message)

**English**

> I have “thing eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 270,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / what"
}
```

## [610] agent_2 (agent message)

**English**

> I have “tool/object eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗚀 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 290,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      45,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / tool, object / eight / question marker / you / have, hold / thing / what"
}
```

## [611] agent_2 (agent message)

**English**

> I have “tool/object eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗚀 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 290,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      45,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / tool, object / eight / question marker / you / have, hold / thing / what"
}
```

## [612] agent_2 (agent message)

**English**

> I have “thing eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 270,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / what"
}
```

## [613] agent_2 (agent message)

**English**

> I have “eight thing”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 206,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / eight / thing / question marker / you / have, hold / thing / what"
}
```

## [614] agent_2 (agent message)

**English**

> I have “thing eight”; [tell/say]. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗎰 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 405,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / eight / tell, say / question marker / you / have, hold / thing / what"
}
```

## [615] agent_2 (agent message)

**English**

> I have “thing eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 270,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / what"
}
```

## [616] agent_2 (agent message)

**English**

> I have “thing eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 270,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / what"
}
```

## [617] agent_2 (agent message)

**English**

> I have “tool/object eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗚀 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 290,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      45,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / tool, object / eight / question marker / you / have, hold / thing / what"
}
```

## [618] agent_2 (agent message)

**English**

> I have “tool/object eight”. What do you have?

**Original**

```text
𗏔 𗟎 𗚀 𗸪 𗄪 𗵵 𗟎 𗣑
```

**Confidence:** medium

**Ambiguity:** ["Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 441,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      45,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / tool, object / eight / question marker / you / have, hold / what"
}
```

## [619] agent_2 (agent message)

**English**

> I have “eight thing”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 206,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / eight / thing / question marker / you / have, hold / thing / what"
}
```

## [620] agent_2 (agent message)

**English**

> Literal: I / eight / thing / you / tell-say. What thing do you have?

**Original**

```text
𗏔 𗸪 𗿃 𗵵 𗎰 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / eight / thing / you / tell, say / question marker / you / have, hold / thing / what"
}
```

## [621] agent_2 (agent message)

**English**

> I have “thing eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 270,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / what"
}
```

## [622] agent_2 (agent message)

**English**

> I have “eight thing”. What do you have?

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗄪 𗵵 𗟎 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 242,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / eight / thing / question marker / you / have, hold / what"
}
```

## [623] agent_2 (agent message)

**English**

> I have “thing eight”; [tell/say / you / thing], if you have a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗎰 𗵵 𗿃 𗗫 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      46,
      49,
      58,
      77,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / eight / tell, say / you / thing / if / you / have, hold / thing / tell, say"
}
```

## [624] agent_2 (agent message)

**English**

> I have “thing eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 270,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / what"
}
```

## [625] agent_2 (agent message)

**English**

> I have “thing eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 270,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / what"
}
```

## [626] agent_2 (agent message)

**English**

> I have “thing eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 270,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / what"
}
```

## [627] agent_2 (agent message)

**English**

> I have “thing eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 270,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / what"
}
```

## [628] agent_2 (agent message)

**English**

> I have “tool/object eight”. What tool/object do you have?

**Original**

```text
𗏔 𗟎 𗚀 𗸪 𗄪 𗵵 𗟎 𗚀 𗣑
```

**Confidence:** medium

**Ambiguity:** ["Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 300,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      45,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / tool, object / eight / question marker / you / have, hold / tool, object / what"
}
```

## [629] agent_2 (agent message)

**English**

> Literal: I / eight / thing / tell-say / you / thing / do-make / what.

**Original**

```text
𗏔 𗸪 𗿃 𗎰 𗵵 𗿃 𗉍 𗣑
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      23,
      37,
      38,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / eight / thing / tell, say / you / thing / do, make / what"
}
```

## [630] agent_2 (agent message)

**English**

> I have “tool/object eight”. What tool/object do you have?

**Original**

```text
𗏔 𗟎 𗚀 𗸪 𗄪 𗵵 𗟎 𗚀 𗣑
```

**Confidence:** medium

**Ambiguity:** ["Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 300,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      45,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / tool, object / eight / question marker / you / have, hold / tool, object / what"
}
```

## [631] agent_2 (agent message)

**English**

> I have “thing eight”; [tell/say]. What thing do you have; [tell/say]?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗎰 𗄪 𗵵 𗟎 𗿃 𗣑 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / eight / tell, say / question marker / you / have, hold / thing / what / tell, say"
}
```

## [632] agent_2 (agent message)

**English**

> I have a thing, if you have a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𗿃 𗗫 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 67,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      46,
      77
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / if / you / have, hold / thing / tell, say"
}
```

## [633] agent_2 (agent message)

**English**

> I have a thing; [tell/say / you / thing / tool-object]. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗎰 𗵵 𗿃 𗚀 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      45,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / tell, say / you / thing / tool, object / question marker / you / have, hold / thing / what"
}
```

## [634] agent_2 (agent message)

**English**

> What thing do you have?

**Original**

```text
𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 74,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      23,
      29,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "question marker / you / have, hold / thing / what"
}
```

## [635] agent_2 (agent message)

**English**

> What do you have?

**Original**

```text
𗄪 𗵵 𗟎 𗣑
```

**Confidence:** high

**Ambiguity:** ["You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 62,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      23,
      29
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "question marker / you / have, hold / what"
}
```

## [636] agent_2 (agent message)

**English**

> I have “tool/object eight”. Who has what tool/object?

**Original**

```text
𗏔 𗟎 𗚀 𗸪 𗄪 𘚺 𗟎 𗚀 𗣑
```

**Confidence:** medium

**Ambiguity:** ["Tool/object is generic; no particular task object or operation is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 368,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      19,
      23,
      24,
      29,
      45,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / tool, object / eight / question marker / who / have, hold / tool, object / what"
}
```

## [637] agent_2 (agent message)

**English**

> What do you have?

**Original**

```text
𗄪 𗵵 𗟎 𗣑
```

**Confidence:** high

**Ambiguity:** ["You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 62,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      23,
      29
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "question marker / you / have, hold / what"
}
```

## [638] agent_2 (agent message)

**English**

> I have “eight thing”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 206,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / eight / thing / question marker / you / have, hold / thing / what"
}
```

## [639] agent_2 (agent message)

**English**

> I have “eight thing”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 206,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / eight / thing / question marker / you / have, hold / thing / what"
}
```

## [640] agent_2 (agent message)

**English**

> I have a thing. Do you have a thing; [tell/say]?

**Original**

```text
𗏔 𗟎 𗿃 𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 44,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      37,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / question marker / you / have, hold / thing / tell, say"
}
```

## [641] agent_2 (agent message)

**English**

> I have “eight thing”, if you have a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗗫 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      46,
      49,
      58,
      77,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / eight / thing / if / you / have, hold / thing / tell, say"
}
```

## [642] agent_2 (agent message)

**English**

> I have “eight thing”. What do you have?

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗄪 𗵵 𗟎 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 242,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / eight / thing / question marker / you / have, hold / what"
}
```

## [643] agent_2 (agent message)

**English**

> I have “tool/object eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗚀 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 290,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      45,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / tool, object / eight / question marker / you / have, hold / thing / what"
}
```

## [644] agent_2 (agent message)

**English**

> I have “thing eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 270,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / what"
}
```

## [645] agent_2 (agent message)

**English**

> I have “eight thing”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 206,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / eight / thing / question marker / you / have, hold / thing / what"
}
```

## [646] agent_2 (agent message)

**English**

> I have “eight thing”; you see a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗵵 𗦴 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      36,
      37,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / eight / thing / you / see / thing / tell, say"
}
```

## [647] agent_2 (agent message)

**English**

> I have “eight thing”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 206,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / eight / thing / question marker / you / have, hold / thing / what"
}
```

## [648] agent_2 (agent message)

**English**

> I have “eight thing”; [tell/say]. What thing do you have?

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗎰 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / eight / thing / tell, say / question marker / you / have, hold / thing / what"
}
```

## [649] agent_2 (agent message)

**English**

> I have “thing eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 270,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / what"
}
```

## [650] agent_2 (agent message)

**English**

> I have “thing eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 270,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / what"
}
```

## [651] agent_2 (agent message)

**English**

> I have “eight thing”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 206,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / eight / thing / question marker / you / have, hold / thing / what"
}
```

## [652] agent_2 (agent message)

**English**

> I have “eight thing”, if you have a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗗫 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      46,
      49,
      58,
      77,
      89
    ],
    "prior_public_ids": [
      641
    ]
  },
  "literal_gloss": "I, me / have, hold / eight / thing / if / you / have, hold / thing / tell, say"
}
```

## [653] agent_2 (agent message)

**English**

> I know “thing eight”. What thing do you have?

**Original**

```text
𗏔 𗡒 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 332,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      31,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / know / thing / eight / question marker / you / have, hold / thing / what"
}
```

## [654] agent_2 (agent message)

**English**

> Literal: I / eight / thing / tell-say / eight / thing / tool-object / what.

**Original**

```text
𗏔 𗸪 𗿃 𗎰 𗸪 𗿃 𗚀 𗣑
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      23,
      37,
      45,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / eight / thing / tell, say / eight / thing / tool, object / what"
}
```

## [655] agent_2 (agent message)

**English**

> I have “thing eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 270,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / what"
}
```

## [656] agent_2 (agent message)

**English**

> I have “thing eight”; [tell/say]. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗎰 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 405,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / eight / tell, say / question marker / you / have, hold / thing / what"
}
```

## [657] agent_2 (agent message)

**English**

> I have “thing eight thing-tool”; [do/make]; [tell/say]; you see a thing.

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗿃 𗚀 𗉍 𗎰 𗵵 𗦴 𗿃
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      36,
      37,
      38,
      45,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / eight / thing / tool, object / do, make / tell, say / you / see / thing"
}
```

## [658] agent_2 (agent message)

**English**

> I have “eight thing”; [tell/say]. What thing do you have?

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗎰 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      648
    ]
  },
  "literal_gloss": "I, me / have, hold / eight / thing / tell, say / question marker / you / have, hold / thing / what"
}
```

## [659] agent_2 (agent message)

**English**

> I have “eight thing”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 206,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / eight / thing / question marker / you / have, hold / thing / what"
}
```

## [660] agent_2 (agent message)

**English**

> I have “thing eight”; [tell/say]. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗎰 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 405,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / eight / tell, say / question marker / you / have, hold / thing / what"
}
```

## [661] agent_2 (agent message)

**English**

> I have “eight thing”; [tell/say], if you have a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗎰 𗗫 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      46,
      49,
      58,
      77,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / eight / thing / tell, say / if / you / have, hold / thing / tell, say"
}
```

## [662] agent_2 (agent message)

**English**

> I have “tool/object eight”. What tool/object do you have?

**Original**

```text
𗏔 𗟎 𗚀 𗸪 𗄪 𗵵 𗟎 𗚀 𗣑
```

**Confidence:** medium

**Ambiguity:** ["Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 300,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      45,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / tool, object / eight / question marker / you / have, hold / tool, object / what"
}
```

## [663] agent_7 (agent message)

**English**

> I have a thing. Do you have a thing; [tell/say]?

**Original**

```text
𗏔 𗟎 𗿃 𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 44,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      37,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / question marker / you / have, hold / thing / tell, say"
}
```

## [664] agent_6 (agent message)

**English**

> I see “thing four”; you see a thing; [tell/say].

**Original**

```text
𗏔 𗦴 𗿃 𘙠 𗵵 𗦴 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      36,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / see / thing / four / you / see / thing / tell, say"
}
```

## [665] agent_2 (agent message)

**English**

> I have eight.

**Original**

```text
𗏔 𗟎 𗸪
```

**Confidence:** high

**Ambiguity:** ["Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      29,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / eight"
}
```

## [666] agent_6 (agent message)

**English**

> I have “four thing”; you see.

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗵵 𗦴
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 376,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      36,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / thing / you / see"
}
```

## [667] agent_7 (agent message)

**English**

> I have a thing; [tell/say]. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗎰 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 303,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / tell, say / question marker / you / have, hold / thing / what"
}
```

## [668] agent_2 (agent message)

**English**

> I have “tool/object eight”. What tool/object do you have?

**Original**

```text
𗏔 𗟎 𗚀 𗸪 𗄪 𗵵 𗟎 𗚀 𗣑
```

**Confidence:** medium

**Ambiguity:** ["Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 300,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      45,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / tool, object / eight / question marker / you / have, hold / tool, object / what"
}
```

## [669] agent_6 (agent message)

**English**

> I have “four thing”; [tell/say]. What thing do you have?

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗎰 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 225,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / thing / tell, say / question marker / you / have, hold / thing / what"
}
```

## [670] agent_7 (agent message)

**English**

> I have a thing; [tell/say]. What thing do you have; [tell/say]?

**Original**

```text
𗏔 𗟎 𗿃 𗎰 𗄪 𗵵 𗟎 𗿃 𗣑 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 337,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / tell, say / question marker / you / have, hold / thing / what / tell, say"
}
```

## [671] agent_2 (agent message)

**English**

> I have “tool/object eight”. What tool/object do you have?

**Original**

```text
𗏔 𗟎 𗚀 𗸪 𗄪 𗵵 𗟎 𗚀 𗣑
```

**Confidence:** medium

**Ambiguity:** ["Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 300,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      45,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / tool, object / eight / question marker / you / have, hold / tool, object / what"
}
```

## [672] agent_6 (agent message)

**English**

> I have “four thing”; you tell/say, if you have a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗵵 𗎰 𗗫 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      46,
      49,
      54,
      77,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / thing / you / tell, say / if / you / have, hold / thing / tell, say"
}
```

## [673] agent_7 (agent message)

**English**

> What thing do you have?

**Original**

```text
𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 74,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      23,
      29,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "question marker / you / have, hold / thing / what"
}
```

## [674] agent_2 (agent message)

**English**

> I have “thing eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 270,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / what"
}
```

## [675] agent_6 (agent message)

**English**

> I have “thing four”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 268,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / four / question marker / you / have, hold / thing / what"
}
```

## [676] agent_7 (agent message)

**English**

> I have a thing. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 258,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / question marker / you / have, hold / thing / what"
}
```

## [677] agent_2 (agent message)

**English**

> I have “eight thing”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 206,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / eight / thing / question marker / you / have, hold / thing / what"
}
```

## [678] agent_6 (agent message)

**English**

> I have “thing four”; [tell/say]. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗎰 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 187,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / four / tell, say / question marker / you / have, hold / thing / what"
}
```

## [679] agent_2 (agent message)

**English**

> I have eight. What thing do you have?

**Original**

```text
𗏔 𗟎 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 326,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / eight / question marker / you / have, hold / thing / what"
}
```

## [680] agent_7 (agent message)

**English**

> What thing do you have?

**Original**

```text
𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 74,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      23,
      29,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "question marker / you / have, hold / thing / what"
}
```

## [681] agent_6 (agent message)

**English**

> I know “thing four”. What thing do you have?

**Original**

```text
𗏔 𗡒 𗿃 𘙠 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      31,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / know / thing / four / question marker / you / have, hold / thing / what"
}
```

## [682] agent_2 (agent message)

**English**

> I know “eight thing”. What thing do you have?

**Original**

```text
𗏔 𗡒 𗸪 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      31,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / know / eight / thing / question marker / you / have, hold / thing / what"
}
```

## [683] agent_7 (agent message)

**English**

> What thing do you have?

**Original**

```text
𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 74,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      23,
      29,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "question marker / you / have, hold / thing / what"
}
```

## [684] agent_6 (agent message)

**English**

> I have “four thing”. What thing do you have?

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 292,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / thing / question marker / you / have, hold / thing / what"
}
```

## [685] agent_2 (agent message)

**English**

> I have eight. What thing do you have?

**Original**

```text
𗏔 𗟎 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 326,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / eight / question marker / you / have, hold / thing / what"
}
```

## [686] agent_7 (agent message)

**English**

> I have a “thing-tool”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗚀 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 255,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      45,
      46,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / tool, object / question marker / you / have, hold / thing / what"
}
```

## [687] agent_6 (agent message)

**English**

> I have “four thing”. What thing do you have?

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 292,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / thing / question marker / you / have, hold / thing / what"
}
```

## [688] agent_2 (agent message)

**English**

> I have “thing eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 270,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / what"
}
```

## [689] agent_7 (agent message)

**English**

> I have a thing, if you have a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𗿃 𗗫 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 67,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      46,
      77
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / if / you / have, hold / thing / tell, say"
}
```

## [690] agent_6 (agent message)

**English**

> I have “four thing”. What thing do you have?

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 292,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / thing / question marker / you / have, hold / thing / what"
}
```

## [691] agent_2 (agent message)

**English**

> I have “tool/object eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗚀 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 290,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      45,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / tool, object / eight / question marker / you / have, hold / thing / what"
}
```

## [692] agent_7 (agent message)

**English**

> What tool/object do you have?

**Original**

```text
𗄪 𗵵 𗟎 𗚀 𗣑
```

**Confidence:** medium

**Ambiguity:** ["Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 50,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      23,
      29,
      45
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "question marker / you / have, hold / tool, object / what"
}
```

## [693] agent_6 (agent message)

**English**

> I have “thing four”, if you have a thing; [tell/say]. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗗫 𗵵 𗟎 𗿃 𗎰 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      46,
      49,
      54,
      77,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / four / if / you / have, hold / thing / tell, say / question marker / you / have, hold / thing / what"
}
```

## [694] agent_2 (agent message)

**English**

> I have “thing eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 270,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / what"
}
```

## [695] agent_7 (agent message)

**English**

> I have a thing; [do/make]. What thing do you have; [tell/say]?

**Original**

```text
𗏔 𗟎 𗿃 𗉍 𗄪 𗵵 𗟎 𗿃 𗣑 𗎰
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      38,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / do, make / question marker / you / have, hold / thing / what / tell, say"
}
```

## [696] agent_6 (agent message)

**English**

> I have “four thing”; [tell/say]. Do you have a thing; [tell/say]?

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗎰 𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 153,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / thing / tell, say / question marker / you / have, hold / thing / tell, say"
}
```

## [697] agent_7 (agent message)

**English**

> I have a thing, if you have a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𗿃 𗗫 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 67,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      46,
      77
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / if / you / have, hold / thing / tell, say"
}
```

## [698] agent_2 (agent message)

**English**

> I have “eight thing”; [tell/say]. What thing do you have?

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗎰 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      648
    ]
  },
  "literal_gloss": "I, me / have, hold / eight / thing / tell, say / question marker / you / have, hold / thing / what"
}
```

## [699] agent_6 (agent message)

**English**

> I have “four thing”. What thing do you have?

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 292,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / thing / question marker / you / have, hold / thing / what"
}
```

## [700] agent_2 (agent message)

**English**

> I have “thing eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 270,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / what"
}
```

## [701] agent_7 (agent message)

**English**

> What thing do you have?

**Original**

```text
𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 74,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      23,
      29,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "question marker / you / have, hold / thing / what"
}
```

## [702] agent_6 (agent message)

**English**

> I have “thing four”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 268,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / four / question marker / you / have, hold / thing / what"
}
```

## [703] agent_2 (agent message)

**English**

> I have “thing eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 270,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / what"
}
```

## [704] agent_7 (agent message)

**English**

> I have a thing. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 258,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / question marker / you / have, hold / thing / what"
}
```

## [705] agent_6 (agent message)

**English**

> I have “four thing”; [tell/say]. What thing do you have?

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗎰 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 225,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / thing / tell, say / question marker / you / have, hold / thing / what"
}
```

## [706] agent_2 (agent message)

**English**

> I have “thing eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 270,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / what"
}
```

## [707] agent_7 (agent message)

**English**

> I have a thing; [tell/say]. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗎰 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 303,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / tell, say / question marker / you / have, hold / thing / what"
}
```

## [708] agent_6 (agent message)

**English**

> I have “thing four”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 268,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / four / question marker / you / have, hold / thing / what"
}
```

## [709] agent_2 (agent message)

**English**

> I have “tool/object eight”. What tool/object do you have?

**Original**

```text
𗏔 𗟎 𗚀 𗸪 𗄪 𗵵 𗟎 𗚀 𗣑
```

**Confidence:** medium

**Ambiguity:** ["Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 300,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      45,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / tool, object / eight / question marker / you / have, hold / tool, object / what"
}
```

## [710] agent_7 (agent message)

**English**

> What do you have; [tell/say]?

**Original**

```text
𗄪 𗵵 𗟎 𗣑 𗎰
```

**Confidence:** medium

**Ambiguity:** ["You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 145,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      23,
      29,
      37
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "question marker / you / have, hold / what / tell, say"
}
```

## [711] agent_6 (agent message)

**English**

> I have “thing four”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 268,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / four / question marker / you / have, hold / thing / what"
}
```

## [712] agent_2 (agent message)

**English**

> I have “eight thing”; [tell/say]. What thing do you have?

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗎰 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": [
      648
    ]
  },
  "literal_gloss": "I, me / have, hold / eight / thing / tell, say / question marker / you / have, hold / thing / what"
}
```

## [713] agent_7 (agent message)

**English**

> Do you have what thing; [tell/say]?

**Original**

```text
𗄪 𗵵 𗟎 𗿃 𗣑 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 41,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      23,
      29,
      37,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "question marker / you / have, hold / thing / what / tell, say"
}
```

## [714] agent_6 (agent message)

**English**

> I have “four thing”; [tell/say].

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 120,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / thing / tell, say"
}
```

## [715] agent_2 (agent message)

**English**

> I have “eight tool/object”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗸪 𗚀 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      45,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / eight / tool, object / question marker / you / have, hold / thing / what"
}
```

## [716] agent_7 (agent message)

**English**

> I have a tool/object. What do you have; [tell/say]?

**Original**

```text
𗏔 𗟎 𗚀 𗄪 𗵵 𗟎 𗣑 𗎰
```

**Confidence:** medium

**Ambiguity:** ["Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      45
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / tool, object / question marker / you / have, hold / what / tell, say"
}
```

## [717] agent_6 (agent message)

**English**

> I have “thing four”; you have [thing / what].

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / four / you / have, hold / thing / what"
}
```

## [718] agent_2 (agent message)

**English**

> I have “thing eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 270,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / what"
}
```

## [719] agent_7 (agent message)

**English**

> I have “thing four”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 268,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / four / question marker / you / have, hold / thing / what"
}
```

## [720] agent_6 (agent message)

**English**

> I have “four thing”. What thing do you have?

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 292,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / thing / question marker / you / have, hold / thing / what"
}
```

## [721] agent_2 (agent message)

**English**

> I have “thing eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 270,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / what"
}
```

## [722] agent_7 (agent message)

**English**

> What thing do you have?

**Original**

```text
𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 74,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      23,
      29,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "question marker / you / have, hold / thing / what"
}
```

## [723] agent_6 (agent message)

**English**

> Literal: I / four / thing / if / you / have-hold / thing / tell-say.

**Original**

```text
𗏔 𘙠 𗿃 𗗫 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      46,
      49,
      54,
      77,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / four / thing / if / you / have, hold / thing / tell, say"
}
```

## [724] agent_2 (agent message)

**English**

> I have “thing eight”; [tell/say]. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗎰 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 405,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / eight / tell, say / question marker / you / have, hold / thing / what"
}
```

## [725] agent_7 (agent message)

**English**

> I have a thing, if you have a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𗿃 𗗫 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 67,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      46,
      77
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / if / you / have, hold / thing / tell, say"
}
```

## [726] agent_6 (agent message)

**English**

> I have “four thing”; [tell/say]. What thing do you have?

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗎰 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 225,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / thing / tell, say / question marker / you / have, hold / thing / what"
}
```

## [727] agent_2 (agent message)

**English**

> I have “tool/object eight”. What tool/object do you have?

**Original**

```text
𗏔 𗟎 𗚀 𗸪 𗄪 𗵵 𗟎 𗚀 𗣑
```

**Confidence:** medium

**Ambiguity:** ["Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 300,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      45,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / tool, object / eight / question marker / you / have, hold / tool, object / what"
}
```

## [728] agent_7 (agent message)

**English**

> What thing do you have?

**Original**

```text
𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 74,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      23,
      29,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "question marker / you / have, hold / thing / what"
}
```

## [729] agent_6 (agent message)

**English**

> I have “four thing”.

**Original**

```text
𗏔 𗟎 𘙠 𗿃
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 347,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / thing"
}
```

## [730] agent_2 (agent message)

**English**

> I have “eight thing”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 206,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / eight / thing / question marker / you / have, hold / thing / what"
}
```

## [731] agent_7 (agent message)

**English**

> I have a thing. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 258,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / question marker / you / have, hold / thing / what"
}
```

## [732] agent_6 (agent message)

**English**

> I have “four thing”; [tell/say].

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 120,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / thing / tell, say"
}
```

## [733] agent_2 (agent message)

**English**

> I have “tool/object eight”; [tell/say / thing / do-make / what].

**Original**

```text
𗏔 𗟎 𗚀 𗸪 𗎰 𗿃 𗉍 𗣑
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      23,
      29,
      37,
      38,
      45,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / tool, object / eight / tell, say / thing / do, make / what"
}
```

## [734] agent_6 (agent message)

**English**

> I have “four thing”; you have [thing / what].

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 392,
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / thing / you / have, hold / thing / what"
}
```

## [735] agent_7 (agent message)

**English**

> I have a “thing-tool”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗚀 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 255,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      45,
      46,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / tool, object / question marker / you / have, hold / thing / what"
}
```

## [736] agent_2 (agent message)

**English**

> I have “thing eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 270,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / what"
}
```

## [737] agent_6 (agent message)

**English**

> I have “four thing”. What thing do you have?

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 292,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / thing / question marker / you / have, hold / thing / what"
}
```

## [738] agent_7 (agent message)

**English**

> I have a thing; [tell/say], if you have a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𗿃 𗎰 𗗫 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 69,
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      46,
      77
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / tell, say / if / you / have, hold / thing / tell, say"
}
```

## [739] agent_2 (agent message)

**English**

> I have “thing eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 270,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / what"
}
```

## [740] agent_6 (agent message)

**English**

> I have “thing four”; you have [thing / what].

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": [
      717
    ]
  },
  "literal_gloss": "I, me / have, hold / thing / four / you / have, hold / thing / what"
}
```

## [741] agent_2 (agent message)

**English**

> I have “thing eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 270,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / what"
}
```

## [742] agent_7 (agent message)

**English**

> I have a thing. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 258,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / question marker / you / have, hold / thing / what"
}
```

## [743] agent_6 (agent message)

**English**

> I have “four thing”. What thing do you have?

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 292,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / thing / question marker / you / have, hold / thing / what"
}
```

## [744] agent_7 (agent message)

**English**

> Who has what thing?

**Original**

```text
𗄪 𘚺 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 443,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      19,
      23,
      24,
      29,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "question marker / who / have, hold / thing / what"
}
```

## [745] agent_2 (agent message)

**English**

> I have “eight thing”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 206,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / eight / thing / question marker / you / have, hold / thing / what"
}
```

## [746] agent_6 (agent message)

**English**

> I have “thing four”; [tell/say]. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗎰 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 187,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / four / tell, say / question marker / you / have, hold / thing / what"
}
```

## [747] agent_2 (agent message)

**English**

> I have “eight thing”; [tell/say]; [you / thing / do-make / what].

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗎰 𗵵 𗿃 𗉍 𗣑
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      23,
      29,
      37,
      38,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / eight / thing / tell, say / you / thing / do, make / what"
}
```

## [748] agent_7 (agent message)

**English**

> Who has what thing; [tell/say]?

**Original**

```text
𗄪 𘚺 𗟎 𗿃 𗣑 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 407,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      19,
      23,
      24,
      29,
      37,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "question marker / who / have, hold / thing / what / tell, say"
}
```

## [749] agent_2 (agent message)

**English**

> I have “eight thing”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 206,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / eight / thing / question marker / you / have, hold / thing / what"
}
```

## [750] agent_6 (agent message)

**English**

> I have “four thing”; [I] want/need you to tell/say.

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𘉝 𗵵 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 158,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      30,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / thing / want, need / you / tell, say"
}
```

## [751] agent_7 (agent message)

**English**

> Who has what thing?

**Original**

```text
𗄪 𘚺 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 443,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      19,
      23,
      24,
      29,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "question marker / who / have, hold / thing / what"
}
```

## [752] agent_2 (agent message)

**English**

> I have eight. What thing do you have?

**Original**

```text
𗏔 𗟎 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 326,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / eight / question marker / you / have, hold / thing / what"
}
```

## [753] agent_6 (agent message)

**English**

> I have “four thing”. What thing do you have?

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 292,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / thing / question marker / you / have, hold / thing / what"
}
```

## [754] agent_7 (agent message)

**English**

> Who has what thing; [tell/say]?

**Original**

```text
𗄪 𘚺 𗟎 𗿃 𗣑 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 407,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      19,
      23,
      24,
      29,
      37,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "question marker / who / have, hold / thing / what / tell, say"
}
```

## [755] agent_2 (agent message)

**English**

> I have “thing eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 270,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / what"
}
```

## [756] agent_6 (agent message)

**English**

> I have “four thing”; you see a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗵵 𗦴 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 502,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      36,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / thing / you / see / thing / tell, say"
}
```

## [757] agent_7 (agent message)

**English**

> Do you have what thing; [tell/say]?

**Original**

```text
𗄪 𗵵 𗟎 𗿃 𗣑 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 41,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      23,
      29,
      37,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "question marker / you / have, hold / thing / what / tell, say"
}
```

## [758] agent_2 (agent message)

**English**

> I have “thing eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 270,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / what"
}
```

## [759] agent_6 (agent message)

**English**

> I have “four thing”; [tell/say]. What thing do you have?

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗎰 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 225,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / thing / tell, say / question marker / you / have, hold / thing / what"
}
```

## [760] agent_7 (agent message)

**English**

> What thing do you have?

**Original**

```text
𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 74,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      23,
      29,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "question marker / you / have, hold / thing / what"
}
```

## [761] agent_2 (agent message)

**English**

> I have “thing eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 270,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / what"
}
```

## [762] agent_6 (agent message)

**English**

> I have “four thing”; you have [thing / what].

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 392,
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / thing / you / have, hold / thing / what"
}
```

## [763] agent_1 (agent message)

**English**

> I have a thing; [tell/say]. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗎰 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 303,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / tell, say / question marker / you / have, hold / thing / what"
}
```

## [764] agent_7 (agent message)

**English**

> What thing do you have?

**Original**

```text
𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 74,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      23,
      29,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "question marker / you / have, hold / thing / what"
}
```

## [765] agent_2 (agent message)

**English**

> I have “thing eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 270,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / what"
}
```

## [766] agent_1 (agent message)

**English**

> Who has what thing?

**Original**

```text
𗄪 𘚺 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 443,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      19,
      23,
      24,
      29,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "question marker / who / have, hold / thing / what"
}
```

## [767] agent_6 (agent message)

**English**

> I have “thing four”. Do you have a thing; [tell/say]?

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 115,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / four / question marker / you / have, hold / thing / tell, say"
}
```

## [768] agent_7 (agent message)

**English**

> Who has what thing?

**Original**

```text
𗄪 𘚺 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 443,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      19,
      23,
      24,
      29,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "question marker / who / have, hold / thing / what"
}
```

## [769] agent_2 (agent message)

**English**

> I have “thing eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 270,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / what"
}
```

## [770] agent_1 (agent message)

**English**

> Do you have a thing; [tell/say]?

**Original**

```text
𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 21,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      29,
      37,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "question marker / you / have, hold / thing / tell, say"
}
```

## [771] agent_7 (agent message)

**English**

> I have “thing four”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 268,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / four / question marker / you / have, hold / thing / what"
}
```

## [772] agent_6 (agent message)

**English**

> I see “thing four”. What thing do you have?

**Original**

```text
𗏔 𗦴 𗿃 𘙠 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      36,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / see / thing / four / question marker / you / have, hold / thing / what"
}
```

## [773] agent_1 (agent message)

**English**

> What thing do you have?

**Original**

```text
𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 74,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      23,
      29,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "question marker / you / have, hold / thing / what"
}
```

## [774] agent_2 (agent message)

**English**

> I have “eight thing”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 206,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / eight / thing / question marker / you / have, hold / thing / what"
}
```

## [775] agent_7 (agent message)

**English**

> I have a thing; [tell/say]. What do you have; [tell/say]?

**Original**

```text
𗏔 𗟎 𗿃 𗎰 𗄪 𗵵 𗟎 𗣑 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 196,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / tell, say / question marker / you / have, hold / what / tell, say"
}
```

## [776] agent_6 (agent message)

**English**

> I have “four thing”; [tell/say]. What thing do you have?

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗎰 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 225,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / thing / tell, say / question marker / you / have, hold / thing / what"
}
```

## [777] agent_1 (agent message)

**English**

> I have a thing; [tell/say]. Who has what thing?

**Original**

```text
𗏔 𗟎 𗿃 𗎰 𗄪 𘚺 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      19,
      23,
      24,
      29,
      37,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / tell, say / question marker / who / have, hold / thing / what"
}
```

## [778] agent_2 (agent message)

**English**

> I have “eight thing”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 206,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / eight / thing / question marker / you / have, hold / thing / what"
}
```

## [779] agent_7 (agent message)

**English**

> I have a tool/object. Who has what thing?

**Original**

```text
𗏔 𗟎 𗚀 𗄪 𘚺 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      19,
      23,
      24,
      29,
      45,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / tool, object / question marker / who / have, hold / thing / what"
}
```

## [780] agent_6 (agent message)

**English**

> I have “four thing”; [tell/say]; you have [thing / what].

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗎰 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 389,
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      23,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / thing / tell, say / you / have, hold / thing / what"
}
```

## [781] agent_2 (agent message)

**English**

> I have eight. What thing do you have?

**Original**

```text
𗏔 𗟎 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 326,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / eight / question marker / you / have, hold / thing / what"
}
```

## [782] agent_7 (agent message)

**English**

> What thing do you have?

**Original**

```text
𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 74,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      23,
      29,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "question marker / you / have, hold / thing / what"
}
```

## [783] agent_6 (agent message)

**English**

> I have “thing four”; [tell/say]; you have [thing / what]; [tell/say].

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗎰 𗵵 𗟎 𗿃 𗣑 𗎰
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      23,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / four / tell, say / you / have, hold / thing / what / tell, say"
}
```

## [784] agent_2 (agent message)

**English**

> I have “thing eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 270,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / what"
}
```

## [785] agent_1 (agent message)

**English**

> I have a “tool-thing”; [tell/say]. What tool/object do you have?

**Original**

```text
𗏔 𗟎 𗚀 𗿃 𗎰 𗄪 𗵵 𗟎 𗚀 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      45,
      46,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / tool, object / thing / tell, say / question marker / you / have, hold / tool, object / what"
}
```

## [786] agent_6 (agent message)

**English**

> I have “four thing”; you see a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗵵 𗦴 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 502,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      36,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / thing / you / see / thing / tell, say"
}
```

## [787] agent_7 (agent message)

**English**

> Who has what thing?

**Original**

```text
𗄪 𘚺 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 443,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      19,
      23,
      24,
      29,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "question marker / who / have, hold / thing / what"
}
```

## [788] agent_2 (agent message)

**English**

> I have “eight thing”. What do you have?

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗄪 𗵵 𗟎 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 242,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / eight / thing / question marker / you / have, hold / what"
}
```

## [789] agent_6 (agent message)

**English**

> Literal: I / thing / four / two / you / tell-say.

**Original**

```text
𗏔 𗿃 𘙠 𗳃 𗵵 𗎰
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      37,
      46,
      49,
      52,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / thing / four / two / you / tell, say"
}
```

## [790] agent_7 (agent message)

**English**

> What thing do you have?

**Original**

```text
𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 74,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      23,
      29,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "question marker / you / have, hold / thing / what"
}
```

## [791] agent_6 (agent message)

**English**

> I have “thing four”; you have [thing / what].

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 717,
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / four / you / have, hold / thing / what"
}
```

## [792] agent_2 (agent message)

**English**

> I have “thing eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 270,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / what"
}
```

## [793] agent_6 (agent message)

**English**

> I have “four thing”; [tell/say]; you have [thing / what].

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗎰 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 389,
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      23,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / thing / tell, say / you / have, hold / thing / what"
}
```

## [794] agent_7 (agent message)

**English**

> I have a thing; [tell/say]. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗎰 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 303,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / tell, say / question marker / you / have, hold / thing / what"
}
```

## [795] agent_2 (agent message)

**English**

> I have “thing eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 270,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / what"
}
```

## [796] agent_7 (agent message)

**English**

> What thing do you have?

**Original**

```text
𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 74,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      23,
      29,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "question marker / you / have, hold / thing / what"
}
```

## [797] agent_6 (agent message)

**English**

> I have “four thing”; [tell/say]. Do you have a thing; [tell/say]?

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗎰 𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 153,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / thing / tell, say / question marker / you / have, hold / thing / tell, say"
}
```

## [798] agent_7 (agent message)

**English**

> What do you have?

**Original**

```text
𗄪 𗵵 𗟎 𗣑
```

**Confidence:** high

**Ambiguity:** ["You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 62,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      23,
      29
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "question marker / you / have, hold / what"
}
```

## [799] agent_6 (agent message)

**English**

> I have “thing four”; [tell/say]. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗎰 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 187,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / four / tell, say / question marker / you / have, hold / thing / what"
}
```

## [800] agent_2 (agent message)

**English**

> I have “thing eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 270,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / what"
}
```

## [801] agent_7 (agent message)

**English**

> Who has what thing?

**Original**

```text
𗄪 𘚺 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 443,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      19,
      23,
      24,
      29,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "question marker / who / have, hold / thing / what"
}
```

## [802] agent_2 (agent message)

**English**

> I have “thing eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 270,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / what"
}
```

## [803] agent_6 (agent message)

**English**

> I have “thing four”. Do you have a thing; [tell/say]?

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 115,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / four / question marker / you / have, hold / thing / tell, say"
}
```

## [804] agent_7 (agent message)

**English**

> Who has what thing?

**Original**

```text
𗄪 𘚺 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 443,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      19,
      23,
      24,
      29,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "question marker / who / have, hold / thing / what"
}
```

## [805] agent_6 (agent message)

**English**

> I have four. What thing do you have?

**Original**

```text
𗏔 𗟎 𘙠 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 427,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / question marker / you / have, hold / thing / what"
}
```

## [806] agent_2 (agent message)

**English**

> I have “thing eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 270,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / what"
}
```

## [807] agent_6 (agent message)

**English**

> I have “thing four”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 268,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / four / question marker / you / have, hold / thing / what"
}
```

## [808] agent_7 (agent message)

**English**

> Who has what thing?

**Original**

```text
𗄪 𘚺 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 443,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      19,
      23,
      24,
      29,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "question marker / who / have, hold / thing / what"
}
```

## [809] agent_2 (agent message)

**English**

> I know “thing eight”. Who knows what thing?

**Original**

```text
𗏔 𗡒 𗿃 𗸪 𗄪 𘚺 𗡒 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      19,
      23,
      24,
      31,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / know / thing / eight / question marker / who / know / thing / what"
}
```

## [810] agent_2 (agent message)

**English**

> I have “eight thing”; [tell/say]. What do you have; [tell/say]?

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗎰 𗄪 𗵵 𗟎 𗣑 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / eight / thing / tell, say / question marker / you / have, hold / what / tell, say"
}
```

## [811] agent_6 (agent message)

**English**

> I have “thing four”; you have [thing / what].

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 717,
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / four / you / have, hold / thing / what"
}
```

## [812] agent_7 (agent message)

**English**

> Who has what thing?

**Original**

```text
𗄪 𘚺 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 443,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      19,
      23,
      24,
      29,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "question marker / who / have, hold / thing / what"
}
```

## [813] agent_6 (agent message)

**English**

> I have “four thing”; [tell/say]. What thing do you have?

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗎰 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 225,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / thing / tell, say / question marker / you / have, hold / thing / what"
}
```

## [814] agent_2 (agent message)

**English**

> I have “eight thing”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 206,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / eight / thing / question marker / you / have, hold / thing / what"
}
```

## [815] agent_7 (agent message)

**English**

> Who has what thing?

**Original**

```text
𗄪 𘚺 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 443,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      19,
      23,
      24,
      29,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "question marker / who / have, hold / thing / what"
}
```

## [816] agent_6 (agent message)

**English**

> I have “four thing”; [tell/say]. What thing do you have?

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗎰 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 225,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / thing / tell, say / question marker / you / have, hold / thing / what"
}
```

## [817] agent_2 (agent message)

**English**

> What thing do you have?

**Original**

```text
𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 74,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      23,
      29,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "question marker / you / have, hold / thing / what"
}
```

## [818] agent_7 (agent message)

**English**

> Who has what thing?

**Original**

```text
𗄪 𘚺 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 443,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      19,
      23,
      24,
      29,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "question marker / who / have, hold / thing / what"
}
```

## [819] agent_2 (agent message)

**English**

> Literal: I / thing / do-make / what / thing / tool-object.

**Original**

```text
𗏔 𗿃 𗉍 𗣑 𗿃 𗚀
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      23,
      38,
      45,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / thing / do, make / what / thing / tool, object"
}
```

## [820] agent_6 (agent message)

**English**

> I have “four thing”; [tell/say]; you have a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗎰 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / thing / tell, say / you / have, hold / thing / tell, say"
}
```

## [821] agent_7 (agent message)

**English**

> I have a thing, if you have a thing; [tell/say]. What thing do you have; [tell/say]?

**Original**

```text
𗏔 𗟎 𗿃 𗗫 𗵵 𗟎 𗿃 𗎰 𗄪 𗵵 𗟎 𗿃 𗣑 𗎰
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      46,
      77
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / if / you / have, hold / thing / tell, say / question marker / you / have, hold / thing / what / tell, say"
}
```

## [822] agent_2 (agent message)

**English**

> What thing do you have?

**Original**

```text
𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 74,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      23,
      29,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "question marker / you / have, hold / thing / what"
}
```

## [823] agent_6 (agent message)

**English**

> I have “four thing”. What thing do you have?

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 292,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / thing / question marker / you / have, hold / thing / what"
}
```

## [824] agent_7 (agent message)

**English**

> Who has what thing? I have a thing; [tell/say].

**Original**

```text
𗄪 𘚺 𗟎 𗿃 𗣑 𗏔 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      19,
      23,
      24,
      29,
      37,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "question marker / who / have, hold / thing / what / I, me / have, hold / thing / tell, say"
}
```

## [825] agent_2 (agent message)

**English**

> I know “thing eight”. What thing do you know?

**Original**

```text
𗏔 𗡒 𗿃 𗸪 𗄪 𗵵 𗡒 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 508,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      31,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / know / thing / eight / question marker / you / know / thing / what"
}
```

## [826] agent_6 (agent message)

**English**

> I have “thing four”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 268,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / four / question marker / you / have, hold / thing / what"
}
```

## [827] agent_2 (agent message)

**English**

> I have “tool/object eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗚀 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 290,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      45,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / tool, object / eight / question marker / you / have, hold / thing / what"
}
```

## [828] agent_7 (agent message)

**English**

> What thing do you have?

**Original**

```text
𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 74,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      23,
      29,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "question marker / you / have, hold / thing / what"
}
```

## [829] agent_6 (agent message)

**English**

> I have “thing four”. Do you have a thing; [tell/say]?

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 115,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / four / question marker / you / have, hold / thing / tell, say"
}
```

## [830] agent_2 (agent message)

**English**

> Literal: I / have-hold / tool-object / [unknown glyph 𘗟] / eight / do-make / tell-say / you / see / thing.

**Original**

```text
𗏔 𗟎 𗚀 𘗟 𗸪 𗉍 𗎰 𗵵 𗦴 𗿃
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial.", "Undefined token(s): 𘗟", "𘗟 belongs to the sampled allowed alphabet and was retained in the public transcript. It is an undefined lexical item, not a discarded-message channel violation."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement.",
    "The message uses 𘗟, which has no entry in the frozen reference; line 87 restricts messages to documented glyphs. No meaning is assigned to this token."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      36,
      37,
      38,
      45,
      46,
      49,
      58,
      87,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / tool, object / UNKNOWN 𘗟 / eight / do, make / tell, say / you / see / thing"
}
```

## [831] agent_7 (agent message)

**English**

> I have a thing; [tell/say]; you have [thing / what].

**Original**

```text
𗏔 𗟎 𗿃 𗎰 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      23,
      29,
      37,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / tell, say / you / have, hold / thing / what"
}
```

## [832] agent_6 (agent message)

**English**

> I have “four thing”. What thing do you have?

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 292,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / thing / question marker / you / have, hold / thing / what"
}
```

## [833] agent_2 (agent message)

**English**

> I have “tool/object eight”; you see a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𗚀 𗸪 𗵵 𗦴 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      36,
      37,
      45,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / tool, object / eight / you / see / thing / tell, say"
}
```

## [834] agent_7 (agent message)

**English**

> What thing do you have?

**Original**

```text
𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 74,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      23,
      29,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "question marker / you / have, hold / thing / what"
}
```

## [835] agent_6 (agent message)

**English**

> I have “four thing”. What thing do you have?

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 292,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / thing / question marker / you / have, hold / thing / what"
}
```

## [836] agent_2 (agent message)

**English**

> I have “eight thing”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 206,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / eight / thing / question marker / you / have, hold / thing / what"
}
```

## [837] agent_7 (agent message)

**English**

> I have a thing, if you have a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𗿃 𗗫 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 67,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      46,
      77
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / if / you / have, hold / thing / tell, say"
}
```

## [838] agent_6 (agent message)

**English**

> I have four. Do you have a thing; [tell/say]?

**Original**

```text
𗏔 𗟎 𘙠 𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / question marker / you / have, hold / thing / tell, say"
}
```

## [839] agent_2 (agent message)

**English**

> I have “tool/object eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗚀 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 290,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      45,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / tool, object / eight / question marker / you / have, hold / thing / what"
}
```

## [840] agent_6 (agent message)

**English**

> I have “four thing”. What thing do you have?

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 292,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / thing / question marker / you / have, hold / thing / what"
}
```

## [841] agent_7 (agent message)

**English**

> I have [thing / what]; [tell/say]. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗣑 𗎰 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      46
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / what / tell, say / question marker / you / have, hold / thing / what"
}
```

## [842] agent_2 (agent message)

**English**

> I have “eight thing”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 206,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / eight / thing / question marker / you / have, hold / thing / what"
}
```

## [843] agent_6 (agent message)

**English**

> I have “four thing”. What thing do you have?

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 292,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / thing / question marker / you / have, hold / thing / what"
}
```

## [844] agent_7 (agent message)

**English**

> What do you have?

**Original**

```text
𗄪 𗵵 𗟎 𗣑
```

**Confidence:** high

**Ambiguity:** ["You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 62,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      23,
      29
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "question marker / you / have, hold / what"
}
```

## [845] agent_2 (agent message)

**English**

> I have “eight thing”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 206,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / eight / thing / question marker / you / have, hold / thing / what"
}
```

## [846] agent_6 (agent message)

**English**

> I have “four thing”. What thing do you have?

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 292,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / thing / question marker / you / have, hold / thing / what"
}
```

## [847] agent_7 (agent message)

**English**

> What do you have?

**Original**

```text
𗄪 𗵵 𗟎 𗣑
```

**Confidence:** high

**Ambiguity:** ["You does not name a particular addressee in this group transcript."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 62,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      10,
      19,
      23,
      29
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "question marker / you / have, hold / what"
}
```

## [848] agent_2 (agent message)

**English**

> I have “eight thing”; [tell/say]. What thing do you have?

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗎰 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 648,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / eight / thing / tell, say / question marker / you / have, hold / thing / what"
}
```

## [849] agent_6 (agent message)

**English**

> Literal: I / four / thing / you / see / thing / tell-say.

**Original**

```text
𗏔 𘙠 𗿃 𗵵 𗦴 𗿃 𗎰
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 416,
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      36,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / four / thing / you / see / thing / tell, say"
}
```

## [850] agent_7 (agent message)

**English**

> I have a thing, if you have a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𗿃 𗗫 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 67,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      46,
      77
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / if / you / have, hold / thing / tell, say"
}
```

## [851] agent_2 (agent message)

**English**

> I have “eight thing”; [tell/say]. What do you have?

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗎰 𗄪 𗵵 𗟎 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / eight / thing / tell, say / question marker / you / have, hold / what"
}
```

## [852] agent_6 (agent message)

**English**

> I have “four thing”, if you have a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗗫 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 181,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      46,
      49,
      54,
      77,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / thing / if / you / have, hold / thing / tell, say"
}
```

## [853] agent_7 (agent message)

**English**

> I have a thing; [tell/say], if you have a thing; [tell/say].

**Original**

```text
𗏔 𗟎 𗿃 𗎰 𗗫 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** low

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 69,
  "departures_from_reference": [
    "A complete unambiguous subject-verb-object parse is unavailable under the documented grammar; the translation preserves unresolved words rather than repairing the statement."
  ],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      46,
      77
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / tell, say / if / you / have, hold / thing / tell, say"
}
```

## [854] agent_2 (agent message)

**English**

> I have eight. What thing do you have?

**Original**

```text
𗏔 𗟎 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 326,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / eight / question marker / you / have, hold / thing / what"
}
```

## [855] agent_6 (agent message)

**English**

> I have “four thing”. What thing do you have?

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 292,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / thing / question marker / you / have, hold / thing / what"
}
```

## [856] agent_2 (agent message)

**English**

> I have “thing eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗿃 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 270,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / eight / question marker / you / have, hold / thing / what"
}
```

## [857] agent_6 (agent message)

**English**

> I see “thing four”; you tell/say.

**Original**

```text
𗏔 𗦴 𗿃 𘙠 𗵵 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      36,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / see / thing / four / you / tell, say"
}
```

## [858] agent_2 (agent message)

**English**

> I have “eight thing”; [tell/say]. What thing do you have?

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗎰 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 648,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / eight / thing / tell, say / question marker / you / have, hold / thing / what"
}
```

## [859] agent_6 (agent message)

**English**

> I have “thing four”. Do you have a thing; [tell/say]?

**Original**

```text
𗏔 𗟎 𗿃 𘙠 𗄪 𗵵 𗟎 𗿃 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 115,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / thing / four / question marker / you / have, hold / thing / tell, say"
}
```

## [860] agent_2 (agent message)

**English**

> I have “eight thing”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 206,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / eight / thing / question marker / you / have, hold / thing / what"
}
```

## [861] agent_6 (agent message)

**English**

> I have “four thing”; [tell/say]. What thing do you have?

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗎰 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 225,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / thing / tell, say / question marker / you / have, hold / thing / what"
}
```

## [862] agent_2 (agent message)

**English**

> I have “eight thing”; [tell/say]. What thing do you have?

**Original**

```text
𗏔 𗟎 𗸪 𗿃 𗎰 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 648,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      37,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / eight / thing / tell, say / question marker / you / have, hold / thing / what"
}
```

## [863] agent_6 (agent message)

**English**

> I have four.

**Original**

```text
𗏔 𗟎 𘙠
```

**Confidence:** high

**Ambiguity:** ["Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 344,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      29,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four"
}
```

## [864] agent_2 (agent message)

**English**

> I have “tool/object eight”. What thing do you have?

**Original**

```text
𗏔 𗟎 𗚀 𗸪 𗄪 𗵵 𗟎 𗿃 𗣑
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "Tool/object is generic; no particular task object or operation is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 290,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      19,
      23,
      29,
      45,
      46,
      49,
      58,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / tool, object / eight / question marker / you / have, hold / thing / what"
}
```

## [865] agent_6 (agent message)

**English**

> I have “four thing”; you tell/say.

**Original**

```text
𗏔 𗟎 𘙠 𗿃 𗵵 𗎰
```

**Confidence:** medium

**Ambiguity:** ["The reference defines thing generically; no particular clue, digit, instruction, object or task referent is identified.", "You does not name a particular addressee in this group transcript.", "Numbers are literal single number words. A number beside a noun could be a quantity, label or compound; the reference does not choose among these or define code-position or decimal-concatenation semantics.", "Quoted wording is a literal compound/word sequence, not an established task-specific term. Modifier-after-head and second-word-as-head rules overlap, leaving attachment uncertain.", "Clause boundaries, verb attachment or omitted subjects/objects are underspecified. Brackets mark an unresolved fragment or a supplied subject; punctuation is editorial."]

**Annotations**

```json
{
  "deduplicated_from_public_message_id": 109,
  "departures_from_reference": [],
  "entry_type": "agent_message",
  "evidence": {
    "language_lines": [
      3,
      6,
      9,
      10,
      29,
      37,
      46,
      49,
      54,
      89
    ],
    "prior_public_ids": []
  },
  "literal_gloss": "I, me / have, hold / four / thing / you / tell, say"
}
```
