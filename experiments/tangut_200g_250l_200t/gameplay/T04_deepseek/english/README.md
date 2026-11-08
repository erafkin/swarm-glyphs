# Reference-assisted English translation: T04

Status: waiting for gameplay. This folder is not a decoder result.

After collecting the completed gameplay, `translation.json` will contain every public
message in its original order with a stable one-based message ID and a pending English field.
Codex will translate each Swarmish message using the exact frozen `swarmish.txt` used by
this run. Preserve sender IDs, original glyphs, questions/assertions, mistakes and ambiguity.
Copy public numeric status entries verbatim and mark them as status, not translated speech.

Keep the raw transcript and frozen language unchanged. Record their SHA-256 hashes.
Mark uncertain interpretations explicitly; do not silently replace a message with the known
room answer. Any comparison with private intended meanings or actions is a separate
researcher annotation, not evidence silently substituted for the language reference.

Final outputs here: `translation.json` (one row per public entry) and
`transcript_english.md` (readable group chat with matching message IDs).
Do not supply these translations, the language document, or private logs to decoder swarms.
