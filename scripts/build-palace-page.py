#!/usr/bin/env python3
"""Build the Baraluga Mind artifact page: a wiki snapshot embedded into scripts/palace-page.html.

Usage: python3 scripts/build-palace-page.py OUTPUT.html
Then publish OUTPUT.html to the existing artifact URL (see wiki/projects/baraluga-mind.md).
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
TEMPLATE = Path(__file__).with_name("palace-page.html")
PERSONAL = {"job-search-2026", "game-price-tracker", "home-network", "thailand-2026"}
SYSTEM = {"baraluga-mind", "index", "aliases", "unclear-captures"}
LINK = re.compile(r"\[\[([^\]|#]+)")
HISTORY_ITEM = re.compile(r"^- (\d{4}-\d{2}(?:-\d{2})?)[^:\n]*:\s*(.+)$")
AS_OF = re.compile(r"As of (\d{4}-\d{2}-\d{2})")
UPDATED = re.compile(r"Last Updated:\s*(\d{4}-\d{2}-\d{2})")
SECTION = re.compile(r"^## (.+)$", re.M)


def section(text: str, name: str) -> str:
    parts = SECTION.split(text)
    for heading, body in zip(parts[1::2], parts[2::2]):
        if heading.strip() == name:
            return body
    return ""


def group(path: Path) -> str:
    if path.stem in SYSTEM:
        return "system"
    if path.stem in PERSONAL:
        return "personal"
    return "smp" if path.parent.name == "smp" else "work"


def page(path: Path) -> dict:
    text = path.read_text(errors="ignore")
    title = text.split("\n", 1)[0].removeprefix("# ").strip()
    updated = (UPDATED.search(text) or [None, None])[1]
    as_of = (AS_OF.search(text) or [None, updated])[1]
    history = [
        {"date": m.group(1), "text": m.group(2).strip()}
        for line in section(text, "History").splitlines()
        if (m := HISTORY_ITEM.match(line.strip()))
    ]
    sources = section(text, "Sources")
    body = text.split("\n## Sources", 1)[0]  # the ask box doesn't need the citation list
    return {
        "slug": path.stem,
        "title": title,
        "group": group(path),
        "folder": path.parent.name,
        "words": len(text.split()),
        "asOf": as_of,
        "updated": updated,
        "links": sorted({l.strip() for l in LINK.findall(text)} - {path.stem}),
        "history": history,
        "uncertain": text.count("UNCERTAIN"),
        "sources": sources.count("`sources/"),
        "text": body.strip(),
    }


def aliases() -> list[list[str]]:
    groups = []
    for line in (WIKI / "aliases.md").read_text().splitlines():
        m = re.match(r"- \*\*(.+?)\*\*(?: \([^)]*\))?: (.+?)(?:\. |\.$|$)", line)
        if m:
            groups.append([m.group(1)] + [v.strip() for v in m.group(2).split(",") if v.strip() and len(v.split()) <= 3])
    return groups


def main() -> None:
    out = Path(sys.argv[1])
    pages = [page(p) for p in sorted(WIKI.rglob("*.md")) if p.name not in ("AGENTS.md", "CLAUDE.md")]
    commit = subprocess.run(["git", "-C", ROOT, "log", "-1", "--format=%h %cs"], capture_output=True, text=True).stdout.split()
    data = {"snapshot": date.today().isoformat(), "commit": commit[0] if commit else "", "pages": pages, "aliases": aliases()}
    blob = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    html = TEMPLATE.read_text().replace("/*__DATA__*/null", blob)
    assert "/*__DATA__*/" not in html
    out.write_text(html)
    print(f"{out}: {len(pages)} pages, {sum(p['words'] for p in pages)} words, {len(html) // 1024} KB")


if __name__ == "__main__":
    main()
