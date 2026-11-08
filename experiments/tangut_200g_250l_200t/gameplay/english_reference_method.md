# English reference transcripts

These translations are researcher references made from each run's frozen `swarmish.txt`
and its public conversation. They are **reference-assisted, not independently certified
ground truth**. Private scratchpads, intended-meaning self-reports and private actions are
not translation evidence. The correct task solution must not replace what the glyphs say.
Keep these files and the language references out of every decoder's inputs.

Each run has `english/translation.json` and a matching `english/transcript_english.md`.
The JSON keeps every public entry's original one-based `id`, `sender` and `text`, including
task status entries. Add `english`, `confidence` (high, medium, low or unknown),
`ambiguities`, and, where useful, a literal gloss, alternative readings,
`departures_from_reference`, and evidence with language line numbers or prior public
message IDs. Preserve errors, questions, proposals and unresolved referents. Use explicit
`unknown` or `undecipherable` text for unknown parts, rather than an empty string.

Public `task` entries must have `english` identical to `text`. A `⊘` entry must use exactly:

> Unknown: message discarded for using characters outside the permitted set.

The discarded content is unavailable in the public transcript. Do not reconstruct it from
private logs. Arbitrary extra annotations remain in JSON and are included in the rendered
Markdown. The utility checks structural fidelity; it cannot certify semantic correctness
or whether a translator actually followed the evidence restrictions.

## Offline validation and rendering

From the repository root, using its existing virtualenv:

```bash
.venv/bin/python experiments/tangut_200g_250l_200t/gameplay/translation_reference.py validate T01
.venv/bin/python experiments/tangut_200g_250l_200t/gameplay/translation_reference.py render T01 --update-metadata
.venv/bin/python experiments/tangut_200g_250l_200t/gameplay/translation_reference.py validate all
```

Omitted IDs or `all` select collected gameplay runs, including unsuccessful completed
attempts; they do not silently skip pending translations. Validation includes archived T
runs. Rendering selects only current R runs and rejects explicit archived T IDs, preserving
historical references byte-for-byte. Validation is read-only and
fails if any English field is empty. Rendering validates all selected runs first and
deterministically writes their Markdown. Only `render --update-metadata` also changes
top-level JSON method/hash metadata; that flag attests to the public-only method.
It preserves all message annotations and does not change raw logs, receipts or configs.
No API keys, network access or model calls are used.

The hashes distinguish three different artifacts:

- `source_transcript_sha256` hashes the raw `task_chatroom.jsonl` bytes and must match
  the immutable collection receipt and existing translation template.
- `rendered_public_transcript_sha256` hashes the UTF-8 output of the monitor's own
  `render_public_messages(read_public_messages(...))`. This is the transcript hash to
  match against an unmasked decoder run. It differs from the raw JSONL hash.
- `language_sha256` hashes the frozen encoder handoff. Both its receipt and gameplay's
  archived copy must agree.

## Comparing decoder outputs

Align the decoder document's TRANSLATION section by original message ID. Score agent
speech separately from already-English task status and discarded-message placeholders;
otherwise copying progress entries can inflate decoding accuracy. Report the number of
agent messages eligible for comparison, uncertain/partial reference translations, and
unknown decoder answers. Do not silently drop hard messages or treat missing translations
as correct. Any stricter score restricted to high-confidence reference spans should be
reported alongside its coverage. Exact phrasing need not match when the semantics do.

No automatic percentage is produced here. Specify a scoring rubric before inspecting
decoder results, and adjudicate ambiguous references separately. A correct room answer
alone is not evidence that the decoder recovered the communication. If private intended
meanings are compared later, preserve that as a separate self-report analysis.

## Frozen-language caveats

Line numbers below refer to the exact encoder `handoff/swarmish.txt`, whose hash is in
each translation. These defects or restrictions are observations, not instructions to
repair a language after a run.

- **E01 Sol:** Words are indivisible lexical entries (line 4). Clause boundaries,
  roles and scope are significant (7–30); aliases have explicit declarations (35–38).
  Numeric quantity words are whole meanings, not decimal digits (80–93). Keep contextual
  descriptions and undeclared aliases distinguishable from literal dictionary meanings.
- **E06 Haiku:** Modifier order and head-final compounds share an underspecified rule
  (line 6). Its small lexicon has numbers zero to nine (49–60), but no explicit rule for
  decimal concatenation. Unknown task concepts must use compounds (89). Mark expansions
  such as a generic "tool" becoming a particular control as contextual interpretations.
- **E07 Gemini:** Speech acts, interchangeable role markers and digit strings are
  explicit (7–13, 16–49). Distinguish an agreement speech act from its separate
  `AGREE_ACTION` verb (102). Decimal number readings are licensed by the document.
- **E08 DeepSeek:** The document asks for continuous strings with polysemy and ignored
  noise (3, 38–47). Its dedicated numeric table (33–36) conflicts with later general
  number entries (95–98); questions and pronouns also have overlapping definitions.
  Examples introduce meanings not transparently licensed by the lexicon (104–117).
  Fifteen referenced Tangut glyphs are outside the sampled allowed 200, including all
  three suggested noise glyphs: `𗊣𗒀𗖸𗧎𗫍𗳶𘄔𘆀𘊓𘎶𘔗𘖈𘖺𘗺𘜀`.
  Preserve resulting violations, ambiguity and departures from the reference rather
  than declaring one convenient reading certain.
