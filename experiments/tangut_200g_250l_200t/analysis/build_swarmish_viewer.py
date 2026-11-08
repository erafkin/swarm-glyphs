"""Build swarmish_viewer.html: the five frozen Sol Swarmish references, their statistics, and the
comparison analysis in one self-contained page.

    .venv/bin/python experiments/tangut_200g_250l_200t/analysis/build_swarmish_viewer.py

Reads encoding/E0N_sol_seedN/handoff/{swarmish.txt,glyphs.json} and sol_seeds_language_comparison.md
from this folder. Writes swarmish_viewer.html next to this script. No network, no API calls.
"""

import html
import json
import re
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
BATCH = HERE.parent
SLOTS = [
    ("E01", "Seed 1", "E01_sol_seed1"),
    ("E02", "Seed 2", "E02_sol_seed2"),
    ("E03", "Seed 3", "E03_sol_seed3"),
    ("E04", "Seed 4", "E04_sol_seed4"),
    ("E05", "Seed 5", "E05_sol_seed5"),
]
# Counts taken by reading the documents; see sol_seeds_language_comparison.md.
BY_HAND = {
    "E01": {"design": "Two-glyph words, first glyph marks word class", "numbers": "109 (0 to 99, large units, fractions)",
            "names": "12 aliases", "idioms": 14, "roles": "7 plus clause open/close", "acts": "7 scope words",
            "camouflage": "Irregular synonyms for grammar and common words", "senses": "1 per word", "examples": 5},
    "E02": {"design": "Single glyphs, four meanings each by register", "numbers": "about 41 (register four)",
            "names": "30 handles", "idioms": 0, "roles": "8", "acts": "4 mandatory speech acts",
            "camouflage": "Four registers", "senses": "4 per glyph", "examples": 7},
    "E03": {"design": "Two-glyph words from a flat pool, single-glyph particles", "numbers": "115 (0 to 100, large units, fractions)",
            "names": "22 labels", "idioms": 23, "roles": "6, two forms each", "acts": "Question, request, possibility, necessity particles",
            "camouflage": "Synonymous particles, 8 sender-specific words, 2 filler glyphs", "senses": "1 per word", "examples": 0},
    "E04": {"design": "Single glyphs, three meanings each by frame, plus a derived layer", "numbers": "31 (0 to 20, tens, large units)",
            "names": "20 handles, owner-qualified", "idioms": 16, "roles": "10 fields", "acts": "5 optional moods",
            "camouflage": "Three frames switched freely", "senses": "3 per glyph", "examples": 6},
    "E05": {"design": "Two-glyph words from a flat pool, single-glyph names", "numbers": "27 (0 to 20, 30, 40, 50, 100, 1,000)",
            "names": "24 single-glyph names", "idioms": 9, "roles": "10, most with two forms", "acts": "3 stance words, two forms each",
            "camouflage": "A second form for every grammar word", "senses": "1 per word", "examples": 6},
}


def stats(doc: str, glyphs: set[str]) -> dict:
    gre = re.compile("[" + "".join(sorted(glyphs)) + "]+")
    lines = doc.splitlines()
    words = gre.findall(doc)
    distinct = set(words)
    lens = Counter(min(len(w), 3) for w in distinct)
    used = {ch for ch in doc if ch in glyphs}
    firsts = Counter(w[0] for w in distinct if len(w) >= 2)
    top5 = sum(n for _, n in firsts.most_common(5)) / max(1, sum(firsts.values()))
    lex = [l for l in lines if gre.search(l) and re.search(r"[A-Za-z]", l) and len(gre.findall(l)) <= 6
           and not re.search(r"\b(example|e\.g\.|for instance)\b", l, re.I)]
    prose = [l for l in lines if l.strip() and not gre.search(l)]
    return {
        "lines": len(lines), "chars": len(doc), "distinct": len(distinct),
        "one": lens[1], "two": lens[2], "three": lens[3], "glyphs_used": len(used),
        "families": len(firsts), "top5": round(top5 * 100), "lexicon_lines": len(lex), "prose_lines": len(prose),
    }


def md_to_html(md: str) -> str:
    """Enough Markdown for the analysis: headings, paragraphs, bullets, numbered lists, tables, bold, code."""
    def inline(s: str) -> str:
        s = html.escape(s, quote=False)
        s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
        s = re.sub(r"`(.+?)`", r"<code>\1</code>", s)
        return s

    out, i, lines = [], 0, md.splitlines()
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        if line.startswith("#"):
            level = len(line) - len(line.lstrip("#"))
            text = line[level:].strip()
            if level == 1:
                i += 1
                continue  # the page has its own title
            slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
            out.append(f'<h{level} id="a-{slug}">{inline(text)}</h{level}>')
            i += 1
        elif line.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            head, body = rows[0], [r for r in rows[1:] if not all(re.fullmatch(r"-+", c) for c in r)]
            out.append('<div class="tablewrap"><table><thead><tr>' + "".join(f"<th>{inline(c)}</th>" for c in head) + "</tr></thead><tbody>")
            for r in body:
                out.append("<tr>" + "".join(f"<{'th' if j == 0 else 'td'}>{inline(c)}</{'th' if j == 0 else 'td'}>" for j, c in enumerate(r)) + "</tr>")
            out.append("</tbody></table></div>")
        elif re.match(r"^- ", line):
            out.append("<ul>")
            while i < len(lines) and re.match(r"^- ", lines[i]):
                out.append(f"<li>{inline(lines[i][2:])}</li>")
                i += 1
            out.append("</ul>")
        elif re.match(r"^\d+\. ", line):
            out.append("<ol>")
            while i < len(lines) and re.match(r"^\d+\. ", lines[i]):
                out.append(f"<li>{inline(re.sub(r'^\d+\. ', '', lines[i]))}</li>")
                i += 1
            out.append("</ol>")
        else:
            para = []
            while i < len(lines) and lines[i].strip() and not re.match(r"^(#|\||- |\d+\. )", lines[i]):
                para.append(lines[i].strip())
                i += 1
            out.append(f"<p>{inline(' '.join(para))}</p>")
    return "\n".join(out)


def main() -> None:
    docs = []
    for slot, label, folder in SLOTS:
        text = (BATCH / "encoding" / folder / "handoff" / "swarmish.txt").read_text(encoding="utf-8")
        glyphs = json.loads((BATCH / "encoding" / folder / "handoff" / "glyphs.json").read_text(encoding="utf-8"))
        docs.append({"id": slot, "label": label, "folder": folder, "text": text, "glyphs": glyphs,
                     "stats": stats(text, set(glyphs)), "hand": BY_HAND[slot]})
    analysis = md_to_html((HERE / "sol_seeds_language_comparison.md").read_text(encoding="utf-8"))
    template = (HERE / "swarmish_viewer_template.html").read_text(encoding="utf-8")
    page = template.replace("/*__DATA__*/", json.dumps(docs, ensure_ascii=False)).replace("<!--__ANALYSIS__-->", analysis)
    out = HERE / "swarmish_viewer.html"
    out.write_text(page, encoding="utf-8")
    print(f"wrote {out} ({len(page):,} chars)")


if __name__ == "__main__":
    main()
