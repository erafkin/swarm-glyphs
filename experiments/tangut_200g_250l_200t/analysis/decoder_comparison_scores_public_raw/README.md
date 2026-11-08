# Public-message cosine with unknown answers included as text

**Arithmetic mean of paired MiniLM cosine against public-message English references; decoder 'unknown' answers and structural glosses are embedded as ordinary text. Task status, discarded messages, and unscorable references are excluded. Not percent accuracy.**

- [Interactive comparisons](comparisons.html)
- [Summary CSV](summary.csv) / [JSON](summary.json)
- [Per-message CSV](per_line.csv) / [JSON](per_line.json)
- 26 completed reports; 1 failed attempt(s), preserved unscored.

| Cell | Encoder | Seed | Decoder | Context | Raw cosine | Embedded / scorable | Literal unknown-only answers | High-confidence cosine |
|---|---|---:|---|---|---:|---:|---:|---:|
| R01_no_task | Sol | 1 | Sol | no_task | 0.216283 | 77/77 | 0 | 0.209353 |
| R01_task_full | Sol | 1 | Sol | task_full | 0.509244 | 77/77 | 0 | 0.511896 |
| R02_no_task | Sol | 2 | Sol | no_task | 0.379945 | 59/59 | 0 | 0.463155 |
| R02_task_full | Sol | 2 | Sol | task_full | 0.509470 | 59/59 | 0 | 0.589195 |
| R03_no_task | Sol | 3 | Sol | no_task | 0.332651 | 75/75 | 0 | 0.378601 |
| R03_task_full | Sol | 3 | Sol | task_full | 0.556442 | 75/75 | 0 | 0.590240 |
| R04_no_task | Sol | 4 | Sol | no_task | 0.235798 | 74/74 | 0 | 0.287281 |
| R04_task_full | Sol | 4 | Sol | task_full | 0.434245 | 74/74 | 0 | 0.480896 |
| R05_no_task | Sol | 5 | Sol | no_task | 0.412330 | 64/64 | 0 | 0.467796 |
| R05_task_full | Sol | 5 | Sol | task_full | 0.468424 | 64/64 | 0 | 0.520335 |
| R01_task_summary | Sol | 1 | Sol | task_summary | 0.233929 | 77/77 | 0 | 0.228368 |
| R01_wrong_task | Sol | 1 | Sol | wrong_task | 0.243130 | 77/77 | 0 | 0.241957 |
| D05 | Haiku | 1 | Haiku | no_task | 0.163266 | 109/109 | 0 | 0.112009 |
| D06 | Haiku | 1 | Haiku | task_full | 0.209329 | 109/109 | 109 | 0.245908 |
| D07 | Haiku | 1 | Sol | no_task | 0.074602 | 109/109 | 0 | 0.065157 |
| D08 | Gemini | 1 | Gemini | no_task | 0.247659 | 77/77 | 0 | 0.297179 |
| D09 | Gemini | 1 | Gemini | task_full | 0.435338 | 77/77 | 0 | 0.474551 |
| D10 | Gemini | 1 | Sol | no_task | 0.320221 | 77/77 | 0 | 0.375130 |
| D11 | DeepSeek | 1 | DeepSeek | no_task | 0.218711 | 164/164 | 13 | N/A |
| D12 | DeepSeek | 1 | DeepSeek | task_full | Failed / unscored | N/A | N/A | N/A |
| D13 | DeepSeek | 1 | Sol | no_task | 0.289189 | 164/164 | 0 | N/A |
| D14 | Haiku | 1 | Sol | task_full | 0.230568 | 109/109 | 0 | 0.147848 |
| R02_task_summary | Sol | 2 | Sol | task_summary | 0.421021 | 59/59 | 0 | 0.498154 |
| R02_wrong_task | Sol | 2 | Sol | wrong_task | 0.436132 | 59/59 | 0 | 0.516218 |
| D12_retry1 | DeepSeek | 1 | DeepSeek | task_full | 0.263136 | 164/164 | 0 | N/A |
| D15 | Gemini | 1 | Sol | task_full | 0.502072 | 77/77 | 0 | 0.487970 |
| D16 | DeepSeek | 1 | Sol | task_full | 0.363718 | 164/164 | 0 | N/A |

## Method and interpretation

Parse the original numbered translation section with the recorded core parser; remove message IDs, speaker/confidence prefixes and normalize whitespace. For a validated Msg/Agent/Meaning/Confidence Markdown table, retain the meaning cell literally and preserve the full original row for audit. Do not replace unknown declarations, remove their parenthetical text, rewrite glosses, expand aliases, infer missing entries, or use private intended meanings.

There are 2,370 embedded pairs out of 2,370 scorable message/cell pairs, including **122 literal unknown-only answers** and **0 missing answers**. Missing answers are not embedded. These counts are lexical descriptions, not semantic judgments. D05 retains its original structural glosses, even though its preamble says their meanings are unknown; D06 retains the literal word `unknown`; D11 retains unknown parentheticals. The historical evaluator's abstention classification is also recorded per line for audit, without altering the text or score.

The denominator is the number of scorable public agent messages with a provided decoder entry. 550 task-status entries and 128 discarded entries are excluded across all comparison cells. The 30 discarded DeepSeek messages stay excluded in each completed DeepSeek-source comparison. References marked unknown are also excluded. Historical cells require complete alignment. Fresh follow-ups may explicitly retain missing translations as unscored entries with coverage shown; they are never silently filled with `unknown`. High-confidence means use only that reference subset and are N/A when it is empty.

Scores are not percentages correct. The embedding of `unknown` can have positive similarity to English references despite recovering no meaning. Likewise, repetitive structural glosses can score above zero. This requested raw metric changes abstention handling, not the public-reference texts. Original reports, N/A results, and zero-assigned results remain unchanged in their historical directories.

The embedding model, immutable revision, package versions, input hashes, parser hash, token lengths, and truncation flags are saved. All computation is local; no paid API calls are made. Sources differ in reference confidence, task success and budget settings, so this descriptive table does not isolate causal model or context effects.

## Reproduce and append a retry

Run `analysis/score_public_raw_cosines.py` from this experiment directory using the same Python environment and cached pinned MiniLM model. Set `HF_HUB_OFFLINE=1` and `TRANSFORMERS_OFFLINE=1` to ensure offline loading. The default input is `analysis/decoder_comparison_source_catalog/summary.json`.

Use `--extra-summary path/to/summary.json` for a separately archived retry. The extra summary uses the same `cells` format with a unique attempt ID and verified source-report hash; source reports must identify the original decoder document, public reference, transcript, frozen language, input hashes, embedding provenance and per-message alignment. Duplicate cell IDs are rejected, so a failed original attempt cannot be silently overwritten. `--check` validates all inputs without loading embeddings.

Alternatively use `--extra-decoder-config path/to/config.json` to score a fresh archived decoder directly, without a prior embedding pass. The config specifies `cell_id`, `encoder`, `seed`, `decoder`, `decoder_model`, `condition`, `source_escaped`, `protocol`, `reference`, `task_dir`, `language`, `decoder_document`, and `receipt`. The scorer verifies the receipt, archived final answer, monitor hashes, model, condition and exact public transcript before aligning messages. Fresh config inputs allow missing entries to remain visibly unscored with coverage, unless `allow_missing` is explicitly false. All paths are repository-relative.
