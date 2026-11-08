"""Score a decoder's English against what the senders meant, and compare the two transcripts.

Text metrics are BLEU, ROUGE, type-token ratio, and a Zipf fit. With models loaded, sentence
cosine uses sentence-transformers/all-MiniLM-L6-v2 and perplexity is BERT pseudo-perplexity.

Usage:
  .venv/bin/python -m src.core.translation_scoring <task_log_dir> <monitor_run_dir> --no-models

Round 3 writes both texts in decoded_swarmish.txt: section 1 is the reconstructed
language, section 2 is the English translation of the gameplay transcript.
"""

import argparse
import json
import math
import re
from collections import Counter
from pathlib import Path

ST_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
BERT_MODEL = "bert-base-uncased"
_TOKEN = re.compile(r"[a-z0-9_]+")
_NUMBERED = re.compile(r"\[(\d+)\]\s*(.*)", re.S)


def _tokens(text: str) -> list[str]:
    return _TOKEN.findall(text.lower())


def _ngrams(tokens: list[str], n: int) -> Counter:
    return Counter(tuple(tokens[i:i + n]) for i in range(len(tokens) - n + 1))


def _f1(overlap: float, ref_n: int, hyp_n: int) -> float:
    if overlap == 0 or ref_n == 0 or hyp_n == 0:
        return 0.0
    precision, recall = overlap / hyp_n, overlap / ref_n
    return 2 * precision * recall / (precision + recall)


def _lcs(a: list[str], b: list[str]) -> int:
    prev = [0] * (len(b) + 1)
    for tok in a:
        cur = [0]
        for j, other in enumerate(b, start=1):
            cur.append(prev[j - 1] + 1 if tok == other else max(prev[j], cur[-1]))
        prev = cur
    return prev[-1]


def bleu(references: list[str], hypotheses: list[str], max_n: int = 4) -> float:
    """Corpus BLEU with add-one smoothing. 1 is an exact token match."""
    overlaps = [1] * max_n
    totals = [1] * max_n
    ref_len = hyp_len = 0
    for reference, hypothesis in zip(references, hypotheses):
        ref_tok, hyp_tok = _tokens(reference), _tokens(hypothesis)
        ref_len += len(ref_tok)
        hyp_len += len(hyp_tok)
        for n in range(1, max_n + 1):
            ref_counts, hyp_counts = _ngrams(ref_tok, n), _ngrams(hyp_tok, n)
            overlaps[n - 1] += sum((hyp_counts & ref_counts).values())
            totals[n - 1] += sum(hyp_counts.values())
    if hyp_len == 0:
        return 0.0
    brevity = 1.0 if hyp_len > ref_len else math.exp(1 - ref_len / hyp_len)
    mean_log = sum(math.log(overlap / total) for overlap, total in zip(overlaps, totals)) / max_n
    return brevity * math.exp(mean_log)


def rouge(references: list[str], hypotheses: list[str]) -> dict[str, float]:
    """Mean sentence-level ROUGE-1, ROUGE-2, and ROUGE-L F1."""
    scores = {"rouge1": 0.0, "rouge2": 0.0, "rougeL": 0.0}
    if not references:
        return scores
    for reference, hypothesis in zip(references, hypotheses):
        ref_tok, hyp_tok = _tokens(reference), _tokens(hypothesis)
        scores["rouge1"] += _f1(sum((_ngrams(ref_tok, 1) & _ngrams(hyp_tok, 1)).values()), len(ref_tok), len(hyp_tok))
        scores["rouge2"] += _f1(sum((_ngrams(ref_tok, 2) & _ngrams(hyp_tok, 2)).values()), max(len(ref_tok) - 1, 0), max(len(hyp_tok) - 1, 0))
        scores["rougeL"] += _f1(_lcs(ref_tok, hyp_tok), len(ref_tok), len(hyp_tok))
    n = len(references)
    return {name: value / n for name, value in scores.items()}


def type_token_ratio(tokens: list[str]) -> float:
    return len(set(tokens)) / len(tokens) if tokens else 0.0


def zipf(tokens: list[str]) -> dict[str, float]:
    """Slope and r-squared of log frequency against log rank. Zipf's law is a slope near -1."""
    freqs = sorted(Counter(tokens).values(), reverse=True)
    if len(freqs) < 2:
        return {"slope": 0.0, "r_squared": 0.0}
    xs = [math.log(rank) for rank in range(1, len(freqs) + 1)]
    ys = [math.log(freq) for freq in freqs]
    mean_x, mean_y = sum(xs) / len(xs), sum(ys) / len(ys)
    var_x = sum((x - mean_x) ** 2 for x in xs)
    cov = sum((x - mean_x) * (y - mean_y) for x, y in zip(xs, ys))
    var_y = sum((y - mean_y) ** 2 for y in ys)
    slope = cov / var_x if var_x else 0.0
    r_squared = (cov ** 2) / (var_x * var_y) if var_x and var_y else 0.0
    return {"slope": slope, "r_squared": r_squared}


def _cosine(left, right) -> float:
    import numpy as np
    left, right = np.asarray(left, float), np.asarray(right, float)
    denom = np.linalg.norm(left) * np.linalg.norm(right)
    return float(np.dot(left, right) / denom) if denom else 0.0


def _chunks(text: str, words: int = 80) -> list[str]:
    tokens = text.split()
    return [" ".join(tokens[i:i + words]) for i in range(0, len(tokens), words)] or [text]


def mean_cosine(references: list[str], hypotheses: list[str], model=None) -> float:
    """Mean cosine between paired sentences. Loads MiniLM if no model is passed."""
    if not references:
        return 0.0
    model = model or _sentence_model()
    encoded = model.encode(references + hypotheses, normalize_embeddings=True)
    return sum(float(encoded[i] @ encoded[i + len(references)]) for i in range(len(references))) / len(references)


def document_cosine(original: str, reconstructed: str, model=None) -> float:
    """Cosine between the real swarmish.txt and the decoder's reconstruction."""
    model = model or _sentence_model()
    original_vec = model.encode(_chunks(original)).mean(axis=0)
    reconstructed_vec = model.encode(_chunks(reconstructed)).mean(axis=0)
    return _cosine(original_vec, reconstructed_vec)


def _sentence_model():
    try:
        from sentence_transformers import SentenceTransformer
    except ImportError as exc:
        raise ImportError("pip install sentence-transformers") from exc
    return SentenceTransformer(ST_MODEL)


def load_bert(model_name: str = BERT_MODEL):
    """BERT masked-LM used for pseudo-perplexity. Loaded once and reused across runs."""
    try:
        import torch
        from transformers import BertForMaskedLM, BertTokenizer
    except ImportError as exc:
        raise ImportError("pip install torch transformers") from exc
    tokenizer = BertTokenizer.from_pretrained(model_name)
    model = BertForMaskedLM.from_pretrained(model_name)
    device = "cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu"
    model.to(device)
    model.eval()
    return tokenizer, model, device


def bert_perplexity(texts: list[str], bert=None, max_chunks: int = 2, max_masks: int = 24) -> float:
    """Pseudo-perplexity over a few 60-word windows, masking a sample of tokens in each."""
    import torch
    tokenizer, model, device = bert or load_bert()
    windows = []
    for text in texts:
        chunks = _chunks(text, words=60)
        if len(chunks) > max_chunks:
            picks = [round(i * (len(chunks) - 1) / (max_chunks - 1)) for i in range(max_chunks)]
            chunks = [chunks[i] for i in picks]
        windows.extend(chunks)
    total, count = 0.0, 0
    for text in windows:
        ids = tokenizer(text, return_tensors="pt", truncation=True, max_length=64)["input_ids"][0].to(device)
        positions = list(range(1, len(ids) - 1))
        if len(positions) > max_masks:
            step = len(positions) / max_masks
            positions = [positions[min(int(i * step), len(positions) - 1)] for i in range(max_masks)]
        for index in positions:
            masked = ids.clone()
            target = ids[index]
            masked[index] = tokenizer.mask_token_id
            with torch.no_grad():
                logits = model(masked.unsqueeze(0)).logits[0, index]
            total += -torch.log_softmax(logits, dim=-1)[target].item()
            count += 1
    return math.exp(total / count) if count else 0.0


def read_text(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    if text.count("\n") <= 1 and "\\n" in text:
        text = text.replace("\\n", "\n")
    return text


_ITEM = re.compile(r"^(?:\*\*)?(\d+)\.\s+(.*)$")
_BRACKET_ITEM = re.compile(r"^\[(\d+)\]\s*(.*)$")
_TRANSLATION_HEADER = re.compile(r"^(?:#+\s*)?2\.\s+TRANSLATION\s*$", re.I)
_TASK_HEADER = re.compile(r"^(?:#+\s*)?3\.\s+THE TASK\s*$", re.I)


def decoded_sections(text: str) -> tuple[str, str]:
    """Split a round-3 answer into the reconstructed language and the translation section.

    Message lines inside the translation are also numbered, so only the section titles count.
    """
    lines = text.splitlines()
    translation_at = task_at = None
    for index, line in enumerate(lines):
        stripped = line.strip()
        if translation_at is None and _TRANSLATION_HEADER.match(stripped):
            translation_at = index
        elif translation_at is not None and _TASK_HEADER.match(stripped):
            task_at = index
            break
    if translation_at is None:
        return text.strip(), ""
    reconstructed = "\n".join(lines[:translation_at]).strip()
    end = task_at if task_at is not None else len(lines)
    return reconstructed, "\n".join(lines[translation_at + 1:end]).strip()


def parse_numbered_translation(section: str) -> dict[int, str]:
    """Message translations numbered 1, 2, 3, either as '1. text' or '**1. [sender]** text'."""
    parsed: dict[int, str] = {}
    current: int | None = None
    buffer: list[str] = []

    def flush() -> None:
        if current is None:
            return
        text = re.sub(r"\s+", " ", " ".join(buffer)).strip()
        text = re.sub(r"^\[[^\]]+\]\s*", "", text)
        parsed[current] = text

    for line in section.splitlines():
        match = _ITEM.match(line.strip()) or _BRACKET_ITEM.match(line.strip())
        if match:
            number = int(match.group(1))
            if current is None or number == current + 1:
                flush()
                current = number
                buffer = [match.group(2).replace("**", "")]
                continue
        if current is not None and line.strip():
            buffer.append(line.strip().replace("**", ""))
    flush()
    return parsed


def parse_translation(path: Path) -> dict[int, str]:
    """Numbered lines from the TRANSLATION section. Later sections cite message numbers too."""
    text = read_text(path)
    if re.search(r"(?:^|\n)(?:#+\s*)?2\.\s+TRANSLATION\b", text):
        _, section = decoded_sections(text)
        return parse_numbered_translation(section)
    start = text.find("[1]")
    if start < 0:
        return {}
    section = text[start:]
    end = re.search(r"\n\d+\. ", section)
    if end:
        section = section[:end.start()]
    parsed = {}
    for block in re.split(r"\n(?=\[\d+\])", section.strip()):
        match = _NUMBERED.match(block)
        if match:
            parsed[int(match.group(1))] = re.sub(r"\s+", " ", match.group(2)).strip()
    return parsed


def intended_meanings(path: Path) -> dict[int, str]:
    """Private English the sender reported for each posted task message."""
    meanings = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        row = json.loads(line)
        message_id = row.get("public_message_id")
        meaning = (row.get("intended_meaning") or "").strip()
        if message_id and meaning:
            meanings[int(message_id)] = meaning
    return meanings


def agent_messages(path: Path) -> list[str]:
    return [
        row["text"] for row in (json.loads(line) for line in path.read_text(encoding="utf-8").splitlines())
        if row["sender"] != "task" and row["text"].strip()
    ]


def _transcript(texts: list[str]) -> dict[str, float]:
    tokens = [tok for text in texts for tok in text.split()]
    fit = zipf(tokens)
    return {
        "tokens": len(tokens),
        "types": len(set(tokens)),
        "ttr": type_token_ratio(tokens),
        "zipf_slope": fit["slope"],
        "zipf_r_squared": fit["r_squared"],
    }


def _document_scores(original: str, reconstructed: str, embedder=None) -> dict[str, float]:
    scores = {"bleu": bleu([original], [reconstructed]), **rouge([original], [reconstructed])}
    if embedder is not None and original.strip() and reconstructed.strip():
        scores["cosine"] = document_cosine(original, reconstructed, embedder)
    return scores


def _monolingual(text: str, bert=None) -> dict[str, float]:
    stats = _transcript([text])
    if bert is not None and text.strip():
        stats["bert_perplexity"] = bert_perplexity([text], bert)
    return stats


def score_run(task_dir: str | Path, monitor_dir: str | Path, models: bool = True,
               embedder=None, bert=None) -> dict:
    """Score one task log against one monitor run. models=False skips MiniLM and BERT.

    English is the senders' private intended meanings against the round-3 translation.
    The language comparison is swarmish.txt against section 1 of decoded_swarmish.txt.
    """
    task_dir, monitor_dir = Path(task_dir), Path(monitor_dir)
    meanings = intended_meanings(task_dir / "agent_calls.jsonl")
    decoded_path = monitor_dir / "decoded_swarmish.txt"
    legacy_translation = monitor_dir / "translation.txt"
    if decoded_path.exists() and decoded_path.stat().st_size > 0:
        reconstructed_language, _section = decoded_sections(read_text(decoded_path))
        decoded = parse_translation(decoded_path)
        language_source = "decoded_swarmish.txt section 1"
    elif legacy_translation.exists():
        reconstructed_language = read_text(monitor_dir / "reconstructed_swarmish.txt") if (monitor_dir / "reconstructed_swarmish.txt").exists() else ""
        decoded = parse_translation(legacy_translation)
        language_source = "reconstructed_swarmish.txt"
    else:
        return {"skipped": "no decoded transcript", "n_paired": 0}
    paired = sorted(set(meanings) & set(decoded))
    references = [meanings[i] for i in paired]
    hypotheses = [decoded[i] for i in paired]
    original_language = read_text(task_dir / "swarmish.txt")
    original_english = "\n".join(meanings[i] for i in sorted(meanings))
    reconstructed_english = "\n".join(decoded[i] for i in sorted(decoded))
    swarmish_chat = agent_messages(task_dir / "task_chatroom.jsonl")
    if models:
        embedder = embedder or _sentence_model()
        bert = bert or load_bert()
    english_scores = {"bleu": bleu(references, hypotheses), **rouge(references, hypotheses)}
    if embedder is not None and references:
        english_scores["cosine"] = mean_cosine(references, hypotheses, embedder)
    language_scores = _document_scores(original_language, reconstructed_language, embedder)
    report = {
        "n_paired": len(paired),
        "n_original_messages": len(meanings),
        "n_reconstructed_messages": len(decoded),
        "english_transcript": english_scores,
        "language_document": {"source": language_source, **language_scores},
        "monolingual": {
            "original_english": _monolingual(original_english, bert),
            "reconstructed_english": _monolingual(reconstructed_english, bert),
            "original_swarmish": _monolingual(original_language, bert),
            "reconstructed_swarmish": _monolingual(reconstructed_language, bert),
        },
        # Kept for the earlier chat-level summary.
        "translation": english_scores,
        "swarmish": _transcript(swarmish_chat),
        "english": _transcript(references),
    }
    if embedder is not None and original_language.strip() and reconstructed_language.strip():
        report["swarmish_document_cosine"] = language_scores["cosine"]
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description="Score a decoder translation against a task log.")
    parser.add_argument("task_dir", type=Path)
    parser.add_argument("monitor_dir", type=Path)
    parser.add_argument("--no-models", action="store_true", help="skip MiniLM cosine and BERT perplexity")
    parser.add_argument("--write", action="store_true", help="write translation_scores.json into the monitor run")
    args = parser.parse_args()
    report = score_run(args.task_dir, args.monitor_dir, models=not args.no_models)
    if args.write:
        destination = args.monitor_dir / "translation_scores.json"
        destination.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
        print(destination)
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
