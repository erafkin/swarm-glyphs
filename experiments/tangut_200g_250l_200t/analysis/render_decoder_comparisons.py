"""Render an offline, self-contained viewer for combined decoder score reports.

The renderer reads existing reports only. It performs no scoring or model calls.
Import ``render(summary, repo, output)`` or pass a summary JSON to the CLI.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def _report_path(repo: Path, value: str) -> Path:
    path = (repo / value).resolve()
    if not path.is_relative_to(repo):
        raise ValueError(f"Report path escapes repository: {value}")
    return path


def render(summary: dict, repo: Path, output: Path) -> None:
    """Embed the summary and completed report lines into one accessible HTML file.

    A completed cell must have a readable report. Failed cells never inherit lines
    from partial outputs. JSON is escaped for the HTML script-data context; all
    subsequent user-visible values are inserted with DOM textContent.
    """
    repo, output = Path(repo).resolve(), Path(output)
    cells = []
    seen = set()
    for cell in summary["cells"]:
        cell_id = str(cell["cell_id"])
        if cell_id in seen:
            raise ValueError(f"Duplicate cell ID: {cell_id}")
        seen.add(cell_id)
        status = cell.get("status")
        if status not in ("completed", "failed"):
            raise ValueError(f"Unexpected status for {cell_id}: {status}")
        record = dict(cell)
        record["lines"] = []
        if status == "completed":
            report = json.loads(_report_path(repo, cell["report_path"]).read_text(encoding="utf-8"))
            record["lines"] = report["lines"]
            record["report_summary"] = report.get("summary", {})
            record["high_confidence"] = report.get("high_confidence", {})
            record["coverage"] = report.get("coverage", {})
            record["embedding_truncation"] = report.get("embedding_truncation")
        cells.append(record)
    payload = json.dumps(
        {"cells": cells, "embedding_model": summary.get("embedding_model"),
         "primary_metric": summary.get("primary_metric")},
        ensure_ascii=False, allow_nan=False, separators=(",", ":"),
    )
    # Closing script tags and HTML entities must remain literal JSON data.
    for character, escaped in (("&", "\\u0026"), ("<", "\\u003c"), (">", "\\u003e"),
                               ("\u2028", "\\u2028"), ("\u2029", "\\u2029")):
        payload = payload.replace(character, escaped)
    document = _HTML.replace("__COMPARISON_DATA__", payload)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(document, encoding="utf-8")


_HTML = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Decoder translation comparisons</title>
<style>
:root { color-scheme:light; --ink:#252a2e; --muted:#596168; --line:#dce0e2; --paper:#fff; --wash:#f5f6f5; --accent:#235d68; }
* { box-sizing:border-box; }
body { margin:0; background:var(--wash); color:var(--ink); font:15px/1.55 system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif; }
main { max-width:1560px; margin:auto; padding:40px 28px 60px; }
h1 { font-size:clamp(1.8rem,3vw,2.7rem); line-height:1.15; letter-spacing:-.035em; margin:0 0 14px; font-weight:650; }
h2 { font-size:1.25rem; line-height:1.3; margin:0 0 16px; }
p { margin:0 0 12px; }
.eyebrow { color:var(--accent); font-size:.76rem; letter-spacing:.12em; text-transform:uppercase; font-weight:700; margin:0 0 10px; }
.intro { max-width:980px; color:var(--muted); }
.notice { background:#f0f4f3; border-left:3px solid #71958f; padding:12px 16px; max-width:1120px; margin:20px 0 26px; }
.notice p:last-child { margin-bottom:0; }
.panel { background:var(--paper); border:1px solid var(--line); border-radius:12px; padding:24px; margin:24px 0; }
.panel-top { display:flex; align-items:baseline; flex-wrap:wrap; gap:8px 20px; justify-content:space-between; }
.muted,small { color:var(--muted); }
.counts { color:var(--muted); font-variant-numeric:tabular-nums; }
.table-wrap { overflow:auto; border:1px solid var(--line); border-radius:7px; }
table { width:100%; border-collapse:collapse; text-align:left; }
caption { text-align:left; padding:12px; font-weight:600; }
th { font-size:.76rem; font-weight:650; color:var(--muted); background:#f7f8f7; }
th,td { border-bottom:1px solid #e7e9e9; padding:10px 12px; vertical-align:top; }
tbody tr:last-child td { border-bottom:0; }
.overview { font-size:.86rem; min-width:980px; }
.overview td { vertical-align:middle; }
.overview tr.selected { background:#eef5f5; }
.numeric { font-variant-numeric:tabular-nums; white-space:nowrap; text-align:right; }
button,select,input { font:inherit; }
button,select,input[type="search"] { border:1px solid #b9c2c5; border-radius:6px; background:white; color:var(--ink); padding:8px 10px; }
button { cursor:pointer; }
button.cell-button { padding:4px 9px; color:var(--accent); font-weight:650; }
button.cell-button[aria-pressed="true"] { background:var(--accent); border-color:var(--accent); color:white; }
:focus-visible { outline:3px solid #bc741d; outline-offset:3px; }
label { display:block; font-size:.82rem; font-weight:600; }
label select,label input[type="search"] { display:block; margin-top:5px; width:100%; font-size:.94rem; font-weight:400; }
.controls { display:grid; grid-template-columns:minmax(230px,1.2fr) minmax(230px,1.8fr) minmax(160px,1fr) minmax(150px,.8fr); gap:14px; margin:20px 0 14px; }
.check-row { display:flex; flex-wrap:wrap; align-items:center; gap:14px 26px; margin:10px 0 18px; }
.checkbox { font-size:.9rem; font-weight:400; display:flex; gap:8px; align-items:center; }
input[type="checkbox"] { width:17px; height:17px; accent-color:var(--accent); }
.stats { display:grid; grid-template-columns:repeat(4,minmax(140px,1fr)); gap:12px; margin:18px 0; }
.stat { padding:12px 15px; background:#f7f8f7; border-radius:7px; }
.stat strong { display:block; font-variant-numeric:tabular-nums; font-size:1.45rem; font-weight:650; }
.stat span { color:var(--muted); font-size:.8rem; }
.lines { table-layout:fixed; min-width:850px; }
.lines th:nth-child(1) { width:92px; }
.lines th:nth-child(2),.lines th:nth-child(3) { width:34%; }
.lines th:nth-child(4) { width:90px; }
.lines th:nth-child(5) { width:145px; }
.text { white-space:pre-wrap; overflow-wrap:anywhere; }
.badge { display:inline-block; padding:2px 7px; border:1px solid #d6dcde; border-radius:4px; background:#f5f6f6; font-size:.73rem; white-space:nowrap; margin:0 4px 5px 0; }
.badge.low,.badge.unknown,.badge.failed { background:#faf2e6; border-color:#e7d6bc; }
.badge.high { background:#eef4ef; border-color:#ceded1; }
.badge.medium { background:#f1f3f5; }
.line-note { font-size:.78rem; color:var(--muted); margin-top:7px; }
details { margin-top:10px; font-size:.8rem; color:var(--muted); }
summary { cursor:pointer; }
details p { margin:8px 0; }
.glyphs { font-size:1rem; line-height:1.7; word-break:break-word; }
.excluded { background:#fafafa; color:#656c70; }
.empty { padding:30px; text-align:center; color:var(--muted); border:1px dashed #c9d0d2; border-radius:7px; }
.footnote { max-width:1120px; font-size:.84rem; color:var(--muted); }
.path { overflow-wrap:anywhere; font-family:ui-monospace,SFMono-Regular,Consolas,monospace; font-size:.78rem; }
.sr-only { position:absolute; width:1px; height:1px; padding:0; margin:-1px; overflow:hidden; clip:rect(0,0,0,0); white-space:nowrap; border:0; }
[hidden] { display:none !important; }
@media(max-width:900px) { main { padding:26px 16px; } .panel { padding:18px; } .controls { grid-template-columns:1fr 1fr; } .stats { grid-template-columns:1fr 1fr; } }
@media(max-width:520px) { .controls { grid-template-columns:1fr; } .panel { padding:14px; } }
@media print { body { background:white; } main { padding:0; } .controls,.check-row { display:none; } .panel { break-inside:avoid; } .table-wrap { overflow:visible; } .lines { min-width:0; } }
</style>
</head>
<body>
<main>
<header>
  <p class="eyebrow">Storm Shelter · revised prompt</p>
  <h1>Decoder translation comparisons</h1>
  <p class="intro">Compare each decoder's English with the reference-assisted translation of the same public message. The overview preserves every completed cell and the failed attempt; the message table lets you inspect what lies behind each mean.</p>
  <div class="notice">
    <p><strong>Text similarity, not accuracy.</strong> MiniLM cosine measures resemblance between English texts. It can miss incorrect numbers, negation, roles, or actions. References retain uncertainty and are not certified ground truth.</p>
    <p id="metric-notice">Missing and wholly unknown decoder answers receive zero on scorable references. Partial unknown answers remain scored. Task status and discarded messages are excluded. High-confidence means cover only the reference subset shown.</p>
  </div>
</header>
<noscript><p class="notice">Enable JavaScript to view the locally embedded comparison data. This file makes no network requests.</p></noscript>
<section class="panel" aria-labelledby="overview-title">
  <div class="panel-top"><h2 id="overview-title">All decoder cells</h2><p id="counts" class="counts"></p></div>
  <div class="table-wrap" tabindex="0" role="region" aria-label="All decoder cells, horizontally scrollable">
    <table class="overview">
      <caption class="sr-only">Select a cell to inspect its original message translations.</caption>
      <thead><tr id="overview-head"><th scope="col">Cell</th><th scope="col">Encoder · seed</th><th scope="col">Decoder</th><th scope="col">Context</th><th scope="col">Status</th><th id="coverage-heading" scope="col" class="numeric">Eligible</th><th id="mean-heading" scope="col" class="numeric">Mean cosine</th><th scope="col" class="numeric">High confidence</th></tr></thead>
      <tbody id="overview-body"></tbody>
    </table>
  </div>
</section>
<section class="panel" aria-labelledby="detail-title">
  <h2 id="detail-title">Inspect translations</h2>
  <div class="controls">
    <label>Decoder cell<select id="cell-select"></select></label>
    <label>Search messages<input id="search" type="search" placeholder="English, glyphs, message ID, or sender" autocomplete="off"></label>
    <label>Decoder text<select id="text-mode"><option value="original">Original wording</option><option value="normalized">Normalized for scoring</option></select></label>
    <label>Reference confidence<select id="confidence"><option value="all">All confidence levels</option><option value="high">High</option><option value="medium">Medium</option><option value="low">Low</option><option value="unknown">Unknown</option></select></label>
  </div>
  <div class="check-row"><label class="checkbox"><input id="show-excluded" type="checkbox">Include task status and discarded messages</label><span id="visible-count" class="counts" role="status" aria-live="polite"></span></div>
  <div id="cell-description" class="muted"></div>
  <div id="stats" class="stats"></div>
  <p id="reference-note" class="footnote"></p>
  <p class="footnote">Filters change the visible rows only. All summary scores retain their original denominators. Normalized text is embedded literally; aliases and symbolic shorthand are not expanded into known meanings.</p>
  <div id="failed-note" class="empty" hidden></div>
  <div id="no-matches" class="empty" hidden>No messages match these filters.</div>
  <div id="line-table-wrap" class="table-wrap" tabindex="0" role="region" aria-label="Message comparisons, horizontally scrollable">
    <table class="lines">
      <caption id="line-caption" class="sr-only">Reference and decoder translations aligned by original message ID.</caption>
      <thead><tr><th scope="col">Message</th><th scope="col">Reference English</th><th scope="col" id="decoder-heading">Decoder · original wording</th><th scope="col" class="numeric">Cosine</th><th scope="col">Confidence / status</th></tr></thead>
      <tbody id="line-body"></tbody>
    </table>
  </div>
  <p id="report-path" class="path muted" style="margin-top:16px"></p>
</section>
<footer class="footnote">
  <p>One decoder run per cell. Languages, reference confidence, decoder models, briefing strength, and budget instructions differ. Haiku and DeepSeek gameplay stopped at the turn limit without escaping. These comparisons are descriptive and do not isolate a causal context or model effect.</p>
  <p id="model-note"></p>
  <p>All data is embedded in this file. Search and filtering run locally without external scripts, services, or network requests.</p>
</footer>
</main>
<script id="comparison-data" type="application/json">__COMPARISON_DATA__</script>
<script>
"use strict";
const data = JSON.parse(document.getElementById("comparison-data").textContent);
const naMode = data.primary_metric === "mean_cosine_over_valid_pairs";
const cells = data.cells;
const byId = new Map(cells.map(cell => [String(cell.cell_id), cell]));
const $ = id => document.getElementById(id);
const readable = value => value == null ? "—" : String(value).replaceAll("_", " ");
const format = value => typeof value === "number" && Number.isFinite(value) ? value.toFixed(3) : "N/A";
const count = value => typeof value === "number" ? value.toLocaleString("en-US") : "—";
const conditionNames = {task_full:"Full task", no_task:"No task", task_summary:"Task summary", wrong_task:"Art Auction"};
const context = value => conditionNames[value] || readable(value);
const text = value => value == null ? "" : String(value);
function node(tag, content, className) {
  const result = document.createElement(tag);
  if (content != null) result.textContent = String(content);
  if (className) result.className = className;
  return result;
}
function badge(content, kind) {
  const allowed = new Set(["high", "medium", "low", "unknown", "failed"]);
  return node("span", content, "badge" + (allowed.has(kind) ? " " + kind : ""));
}
function cellName(cell) {
  return `${cell.cell_id} · ${readable(cell.encoder)} → ${readable(cell.decoder)} · ${context(cell.condition)}`;
}
function stat(label, value, note) {
  const box = node("div", null, "stat");
  box.append(node("span", label), node("strong", value));
  if (note) box.append(node("span", note));
  return box;
}
function referenceDetails(line) {
  const details = node("details");
  details.append(node("summary", "Source glyphs and reference notes"));
  details.append(node("p", line.source || "Source text unavailable.", "glyphs text"));
  const notes = line.reference_ambiguities;
  if (Array.isArray(notes)) for (const note of notes) details.append(node("p", note, "text"));
  else if (notes) details.append(node("p", typeof notes === "object" ? JSON.stringify(notes) : notes, "text"));
  return details;
}
function decoderText(line, mode) {
  const value = mode === "original" ? (line.hypothesis_original ?? line.hypothesis) : line.hypothesis;
  return text(value).trim() ? text(value) : "No translation provided.";
}
function populateOverview() {
  if (naMode) {
    $("metric-notice").textContent = "Missing and wholly unknown answers are N/A and excluded from the primary cosine mean. Coverage is valid pairs / scorable references. Partial-unknown guesses remain scored and are flagged separately; no further semantic reclassification is applied. Tentative or structure-only glosses can receive nonzero cosine without establishing decipherment. Historical zero-inclusive means are supplementary. Task status and discarded messages remain excluded.";
    $("coverage-heading").textContent = "Coverage";
    $("mean-heading").textContent = "Primary cosine";
    for (const title of ["Unknown / missing", "Partial unknown", "Zero-inclusive (supp.)"]) {
      const heading = node("th", title, "numeric");
      heading.scope = "col";
      $("overview-head").append(heading);
    }
  }
  const completed = cells.filter(cell => cell.status === "completed").length;
  const failed = cells.filter(cell => cell.status === "failed").length;
  $("counts").textContent = `${completed} completed · ${failed} failed / unscored`;
  const rows = document.createDocumentFragment();
  for (const cell of cells) {
    const row = node("tr");
    row.dataset.cellId = String(cell.cell_id);
    const cellColumn = node("td");
    const button = node("button", cell.cell_id, "cell-button");
    button.type = "button";
    button.setAttribute("aria-label", "Inspect " + cellName(cell));
    button.setAttribute("aria-pressed", "false");
    button.addEventListener("click", () => {
      $("cell-select").value = String(cell.cell_id);
      update();
      $("detail-title").scrollIntoView({behavior:"smooth", block:"start"});
    });
    cellColumn.append(button);
    row.append(cellColumn, node("td", `${readable(cell.encoder)} · ${cell.seed ?? "—"}`), node("td", readable(cell.decoder)), node("td", context(cell.condition)));
    const status = node("td");
    status.append(badge(cell.status === "completed" ? "Completed" : "Failed · unscored", cell.status));
    const coverage = naMode ? `${count(cell.valid_pairs)}/${count(cell.scorable_references)}` : count(cell.eligible);
    const highValue = naMode ? `${format(cell.high_confidence_cosine)} (${count(cell.high_confidence_valid_pairs)}/${count(cell.high_confidence_references)})` : format(cell.high_confidence_cosine);
    row.append(status, node("td", cell.status === "completed" ? coverage : "—", "numeric"), node("td", cell.status === "completed" ? format(cell.cosine) : "N/A", "numeric"), node("td", cell.status === "completed" ? highValue : "N/A", "numeric"));
    if (naMode) row.append(
      node("td", cell.status === "completed" ? `${count(cell.unknown_only_predictions)} / ${count(cell.missing_predictions)}` : "—", "numeric"),
      node("td", cell.status === "completed" ? count(cell.partial_unknown_predictions) : "—", "numeric"),
      node("td", cell.status === "completed" ? format(cell.zero_inclusive_cosine) : "N/A", "numeric")
    );
    rows.append(row);
    const option = node("option", cellName(cell) + (cell.status === "failed" ? " · FAILED" : ""));
    option.value = String(cell.cell_id);
    $("cell-select").append(option);
  }
  $("overview-body").replaceChildren(rows);
  const model = data.embedding_model;
  $("model-note").textContent = model ? `Embedding model: ${model.model_name || "MiniLM"}. Revision: ${model.resolved_revision || model.requested_revision || "recorded in score report"}. Maximum input length: ${model.max_seq_length || 256} tokens. See per-row truncation notes when present.` : "Embedding model: sentence-transformers/all-MiniLM-L6-v2. Exact model and input provenance are retained in the canonical score reports.";
}
function update() {
  const cell = byId.get($("cell-select").value);
  if (!cell) return;
  for (const row of $("overview-body").children) {
    const selected = row.dataset.cellId === String(cell.cell_id);
    row.classList.toggle("selected", selected);
    row.querySelector("button").setAttribute("aria-pressed", String(selected));
  }
  const failed = cell.status !== "completed";
  $("failed-note").hidden = !failed;
  $("stats").hidden = failed;
  $("reference-note").hidden = failed;
  $("failed-note").textContent = `${cell.cell_id} failed before a completed decoder output was available. No translation lines or cosine score are assigned to this attempt.`;
  const escape = cell.source_escaped === true ? "escaped" : cell.source_escaped === false ? "did not escape" : "outcome recorded in source report";
  $("cell-description").textContent = `${cellName(cell)}. Source gameplay: ${escape}. Protocol: ${readable(cell.protocol)}.`;
  $("report-path").textContent = cell.report_path ? (naMode ? "Derived report: " : "Canonical report: ") + cell.report_path : "No completed score report.";
  const reportSummary = cell.report_summary || {};
  const high = cell.high_confidence || {};
  const highN = high.scorable_references ?? high.eligible ?? cell.lines.filter(line => !line.excluded_reason && line.scorable && line.reference_confidence === "high").length;
  const denominator = reportSummary.scorable_references ?? cell.eligible;
  const unknown = cell.unknown_only_predictions ?? reportSummary.unknown_only_predictions ?? 0;
  const missing = reportSummary.missing_predictions ?? cell.missing_predictions ?? 0;
  if (naMode) $("stats").replaceChildren(
    stat("Primary valid-pair cosine", format(cell.cosine), `${count(cell.valid_pairs)} answered, scorable pairs`),
    stat("Coverage", `${count(cell.valid_pairs)}/${count(denominator)}`, "valid pairs / scorable references"),
    stat("High-confidence cosine", format(cell.high_confidence_cosine), `${count(high.valid_pairs)} / ${count(highN)} valid / scorable pairs`),
    stat("N/A answers", count(unknown + missing), `${count(unknown)} wholly unknown · ${count(missing)} missing`),
    stat("Partial-unknown answers", count(cell.partial_unknown_predictions), "retained in the primary mean"),
    stat("Zero-inclusive cosine · supplementary", format(cell.zero_inclusive_cosine), `${count(denominator)} scorable references; historical mean`),
    stat("High-confidence zero-inclusive · supplementary", format(cell.zero_inclusive_high_confidence_cosine), `${count(highN)} scorable references; historical mean`)
  );
  else $("stats").replaceChildren(
    stat("Fixed-denominator cosine", format(cell.cosine), `${count(denominator)} scorable references`),
    stat("High-confidence cosine", format(cell.high_confidence_cosine), `${count(highN)} of ${count(cell.eligible)} eligible references`),
    stat("Nonempty, non-unknown pairs", count(cell.valid_pairs), `${count(cell.eligible)} eligible agent messages`),
    stat("Zero-scored answers", count(unknown + missing), `${count(unknown)} wholly unknown · ${count(missing)} missing`)
  );
  const uncertain = reportSummary.uncertain_or_partial_references ?? cell.lines.filter(line => !line.excluded_reason && (line.reference_confidence !== "high" || line.reference_uncertain_or_partial)).length;
  const excluded = cell.lines.filter(line => line.excluded_reason).length;
  $("reference-note").textContent = `${count(uncertain)} eligible references are uncertain or partial. ${count(excluded)} public status or discarded rows are excluded.${highN === 0 ? " No eligible high-confidence references exist for this source, so its high-confidence score is N/A." : naMode && high.valid_pairs === 0 ? " No valid high-confidence prediction pairs remain, so its high-confidence score is N/A." : ""}${naMode && cell.valid_pairs === 0 && !failed ? " No valid prediction pairs remain; the primary mean is N/A, not zero." : ""}`;
  const query = $("search").value.trim().toLocaleLowerCase();
  const confidence = $("confidence").value;
  const showExcluded = $("show-excluded").checked;
  const mode = $("text-mode").value;
  $("decoder-heading").textContent = "Decoder · " + (mode === "original" ? "original wording" : "normalized for scoring");
  const visible = cell.lines.filter(line => {
    if (!showExcluded && line.excluded_reason) return false;
    if (confidence !== "all" && line.reference_confidence !== confidence) return false;
    if (!query) return true;
    return [line.id, line.sender, line.source, line.reference, line.hypothesis, line.hypothesis_original, line.hypothesis_normalized_raw, line.unknown_reason].map(text).join("\n").toLocaleLowerCase().includes(query);
  });
  $("visible-count").textContent = failed ? "No scored rows" : `${count(visible.length)} of ${count(cell.lines.length)} public rows shown`;
  $("line-table-wrap").hidden = failed || visible.length === 0;
  $("no-matches").hidden = failed || visible.length > 0;
  $("line-caption").textContent = `${cell.cell_id}: reference and decoder translations aligned by original message ID.`;
  const fragment = document.createDocumentFragment();
  for (const line of visible) {
    const row = node("tr", null, line.excluded_reason ? "excluded" : "");
    const identity = node("td");
    identity.append(node("strong", "#" + line.id), node("div", line.sender, "line-note"));
    const reference = node("td");
    reference.append(node("div", line.reference, "text"), referenceDetails(line));
    const hypothesis = node("td");
    hypothesis.append(node("div", decoderText(line, mode), "text"));
    if (line.unknown_reason) hypothesis.append(node("p", "Unknown classification: " + line.unknown_reason, "line-note text"));
    if (line.hypothesis_normalized_raw != null && line.hypothesis_normalized_raw !== line.hypothesis) {
      const raw = node("details");
      raw.append(node("summary", "Normalized text before unknown classification"), node("p", line.hypothesis_normalized_raw, "text"));
      hypothesis.append(raw);
    }
    const tokens = line.embedding_tokens;
    if (tokens && (tokens.reference_truncated || tokens.hypothesis_truncated)) hypothesis.append(node("p", `Embedding input truncated at ${tokens.max_seq_length} tokens (${tokens.reference_truncated ? "reference" : ""}${tokens.reference_truncated && tokens.hypothesis_truncated ? " and " : ""}${tokens.hypothesis_truncated ? "decoder" : ""}).`, "line-note"));
    const cosine = node("td", format(line.scores?.cosine), "numeric");
    if (line.excluded_reason) cosine.append(node("div", "Excluded", "line-note"));
    else if (!line.scorable) cosine.append(node("div", "Unscorable reference", "line-note"));
    else if (line.prediction_status === "missing" || line.prediction_status === "unknown") cosine.append(node("div", naMode ? "N/A · excluded from mean" : "Assigned zero", "line-note"));
    const status = node("td");
    status.append(badge(readable(line.reference_confidence), line.reference_confidence));
    status.append(node("div", "Decoder: " + readable(line.prediction_status), "line-note"));
    if (naMode && line.prediction_status === "partial_unknown") status.append(node("div", "Tentative / partial: retained in mean", "line-note"));
    if (line.excluded_reason) status.append(node("div", "Excluded: " + readable(line.excluded_reason), "line-note"));
    row.append(identity, reference, hypothesis, cosine, status);
    fragment.append(row);
  }
  $("line-body").replaceChildren(fragment);
}
populateOverview();
for (const id of ["cell-select", "text-mode", "confidence", "show-excluded"]) $(id).addEventListener("change", update);
$("search").addEventListener("input", update);
update();
</script>
</body>
</html>
"""


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("summary", type=Path, help="combined summary JSON")
    parser.add_argument("output", type=Path, help="standalone HTML output")
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[3])
    args = parser.parse_args()
    render(json.loads(args.summary.read_text(encoding="utf-8")), args.repo, args.output)


if __name__ == "__main__":
    main()
