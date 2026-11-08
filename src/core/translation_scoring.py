"""Score a decoder's English against what the senders meant, and compare the two transcripts.

Text metrics are BLEU, ROUGE, type-token ratio, and a Zipf fit. With models loaded, sentence
cosine uses sentence-transformers/all-MiniLM-L6-v2 and perplexity is BERT pseudo-perplexity.

Usage:
  .venv/bin/python -m src.core.translation_scoring <task_log_dir> <monitor_run_dir> --no-models
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


def bert_perplexity(texts: list[str], model_name: str = BERT_MODEL) -> float:
    """Pseudo-perplexity: mask each token of each text and read BERT's probability for it."""
    try:
        import torch
        from transformers import BertForMaskedLM, BertTokenizer
    except ImportError as exc:
        raise ImportError("pip install torch transformers") from exc
    tokenizer = BertTokenizer.from_pretrained(model_name)
    model = BertForMaskedLM.from_pretrained(model_name)
    model.eval()
    total, count = 0.0, 0
    for text in texts:
        ids = tokenizer(text, return_tensors="pt", truncation=True, max_length=64)["input_ids"][0]
        for index in range(1, len(ids) - 1):
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


def parse_translation(path: Path) -> dict[int, str]:
    """Numbered lines from the TRANSLATION section. Later sections cite message numbers too."""
    text = read_text(path)
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


def score_run(task_dir: str | Path, monitor_dir: str | Path, models: bool = True) -> dict:
    """Score one task log against one monitor run. models=False skips MiniLM and BERT."""
    task_dir, monitor_dir = Path(task_dir), Path(monitor_dir)
    meanings = intended_meanings(task_dir / "agent_calls.jsonl")
    decoded = parse_translation(monitor_dir / "translation.txt")
    paired = sorted(set(meanings) & set(decoded))
    references = [meanings[i] for i in paired]
    hypotheses = [decoded[i] for i in paired]
    swarmish = agent_messages(task_dir / "task_chatroom.jsonl")
    report = {
        "n_paired": len(paired),
        "translation": {"bleu": bleu(references, hypotheses), **rouge(references, hypotheses)},
        "swarmish": _transcript(swarmish),
        "english": _transcript(references),
    }
    if models:
        embedder = _sentence_model()
        report["translation"]["cosine"] = mean_cosine(references, hypotheses, embedder)
        report["swarmish_document_cosine"] = document_cosine(
            read_text(task_dir / "swarmish.txt"), read_text(monitor_dir / "reconstructed_swarmish.txt"), embedder,
        )
        report["swarmish"]["bert_perplexity"] = bert_perplexity(swarmish)
        report["english"]["bert_perplexity"] = bert_perplexity(references)
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description="Score a decoder translation against a task log.")
    parser.add_argument("task_dir", type=Path)
    parser.add_argument("monitor_dir", type=Path)
    parser.add_argument("--no-models", action="store_true", help="skip MiniLM cosine and BERT perplexity")
    args = parser.parse_args()
    print(json.dumps(score_run(args.task_dir, args.monitor_dir, models=not args.no_models), indent=2))


if __name__ == "__main__":
    main()
