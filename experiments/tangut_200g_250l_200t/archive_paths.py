"""Resolve relocated artifacts without rewriting historical receipts or raw logs."""
import hashlib
import json
from pathlib import Path


def resolve_raw_path(repo, folder, receipt):
    repo, folder = Path(repo).resolve(), Path(folder).resolve()
    recorded = Path(receipt["raw_path"])
    record_path = folder / "archive_record.json"
    if record_path.exists():
        record = json.loads(record_path.read_text())
        digest = hashlib.sha256((folder / "receipt.json").read_bytes()).hexdigest()
        if digest != record["original_receipt_sha256"]:
            raise ValueError("Historical receipt changed after relocation")
        if (repo / record["archived_path"]).resolve() != folder:
            raise ValueError("Archive folder differs from relocation record")
        original = Path(record["original_path"])
        if recorded.is_absolute() or not recorded.is_relative_to(original / "raw"):
            raise ValueError("Historical raw path is outside its original run")
        raw = (folder / recorded.relative_to(original)).resolve()
        if not raw.is_relative_to(folder / "raw"):
            raise ValueError("Relocated raw path escapes its run")
    else:
        raw = (repo / recorded).resolve()
    if not raw.is_relative_to(repo):
        raise ValueError("Raw path escapes repository")
    return raw
