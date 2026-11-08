# English reference: R07

Completed reference-assisted translation of all 97 public entries in the revised-prompt
Gemini Storm Shelter run: 77 agent messages, 20 task-status entries, and no discarded
messages. Every entry retains its original ID, sender and text. Task status is copied
verbatim. Agent-message confidence is 32 high, 44 medium and 1 low; all messages have
uncertainty annotations, and every agent message includes a literal gloss and frozen
language line references.

Translation evidence is restricted to E07's frozen `handoff/swarmish.txt` and R07's
public conversation preserved in `translation.json`. No private intended meanings,
scratchpads, room actions, task-agent files, room definition or answer key were used.
These are researcher references, not independently certified ground truth. A public
claim that an action was performed or completed is retained as a claim, even where
subsequent task status does not establish success.

Important limitations:

- Ad hoc symbol descriptions remain literal: `HOT`, `COLD LIGHT`, `BLUE MOVE`,
  `UP DOWN`, `SHAPE LIGHT`, and `SHAPE 5`. They are not replaced with presumed
  depicted symbols or silently identified with one another. The reference lists
  `LIGHT` as a descriptor opposite `HEAVY`, without separately defining illumination.
- The repeated digits `2 7 4 8` license decimal **2748** under the explicit base-10
  rule. The public box-position discussion also makes an ordered four-value sequence
  **(2, 7, 4, 8)** plausible. Both readings remain visible in messages 19, 23, 25, 27,
  29 and 33.
- Message 49 explicitly proposes remove, then repeat, then signal, then start.
  Messages 53, 56, 58 and 70 instead use `AFTER` (also glossed “later, next”);
  their annotations preserve both a forward sequence and a reversed dependency
  reading rather than imposing an unstated ordering rule.
- Message 37 is low confidence: its second clause says `SIGNAL COST` associated
  with `REMOVE DONE`. It is not repaired into `SIGNAL RULE`, a numeric cost or a
  definite prerequisite.
- Asserted actions, proposals, `DONE`, `FAIL`, and the agreement speech act remain
  distinct. Message 62 also uses the separate `AGREE_ACTION` verb, matching the
  frozen example. The language does not mark tense.
- Action labels such as `REMOVE`, `REPEAT`, `SIGNAL` and `START`, and compounds
  such as `NEW ADD`, remain generic when no precise referent or arithmetic target
  is expressed. Stage changes do not retrospectively correct the agents' messages.

`translation.json` is the annotated source. The shared offline reference utility
renders `transcript_english.md` from it and checks structural fidelity; it cannot
certify semantic accuracy. See [the reference method](../../english_reference_method.md).
Keep this folder and the frozen language out of decoder inputs.

Files: [English transcript](transcript_english.md), [annotated JSON](translation.json), [frozen Swarmish reference](../../../encoding/E07_gemini_seed1/handoff/swarmish.txt).
