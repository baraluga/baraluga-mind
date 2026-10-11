#!/usr/bin/env python3
"""Lint the Baraluga Mind wiki. Exits 1 on errors; warnings never fail.

Errors (CI fails):
  - broken [[wiki-links]]
  - cited `sources/...` paths that don't exist
  - pages missing from wiki/index.md, or index links to missing pages
  - unparseable entries in wiki/aliases.md
  - checkboxes in wiki pages (pending work belongs in `Current State` prose)
Warnings:
  - pages over 1,500 words (split candidates)
  - pages not yet in the current-state shape

Usage: python scripts/lint-wiki.py [repo_root]
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

LINK = re.compile(r"\[\[([^\]|#]+)")
SOURCE = re.compile(r"sources/[a-z-]+/[^\s`;),*]+")
CHECKBOX = re.compile(r"^\s*- \[[ xX]\]", re.M)
ALIAS = re.compile(r"- \*\*.+?\*\*(?: \([^)]*\))?: .+")
INSTRUCTION_FILES = {"AGENTS.md", "CLAUDE.md"}
MAX_WORDS = 1500


def lint(root: Path) -> tuple[list[str], list[str]]:
    wiki = root / "wiki"
    pages = {p.stem: p for p in wiki.rglob("*.md") if p.name not in INSTRUCTION_FILES}
    valid = set(pages) | {"actions"}  # root actions.md is a frozen archive still linked from old text
    errors, warnings = [], []

    for slug, path in sorted(pages.items()):
        rel = path.relative_to(root)
        text = path.read_text(errors="ignore")
        for target in sorted({t.strip() for t in LINK.findall(text)} - valid):
            errors.append(f"{rel}: broken link [[{target}]]")
        for cited in sorted(set(SOURCE.findall(text))):
            if not (root / cited.rstrip(".")).exists():
                errors.append(f"{rel}: cited source does not exist: {cited}")
        if CHECKBOX.search(text):
            errors.append(f"{rel}: checkbox found; mention pending work in Current State instead")
        if slug not in ("index", "aliases"):
            if len(text.split()) > MAX_WORDS:
                warnings.append(f"{rel}: {len(text.split())} words; consider splitting")
            if "## Current State" not in text and not slug[:4].isdigit():
                warnings.append(f"{rel}: not yet in current-state shape")

    index = pages.get("index")
    if index is None:
        errors.append("wiki/index.md is missing")
    else:
        listed = {t.strip() for t in LINK.findall(index.read_text())}
        for slug in sorted(set(pages) - listed - {"index"}):
            errors.append(f"wiki/index.md: page not listed: [[{slug}]]")

    aliases = pages.get("aliases")
    if aliases is not None:
        for n, line in enumerate(aliases.read_text().splitlines(), 1):
            if line.startswith("- **") and not ALIAS.fullmatch(line):
                errors.append(f"wiki/aliases.md:{n}: entry does not match '- **Canonical**: variant, variant'")
    return errors, warnings


def main() -> None:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent
    errors, warnings = lint(root)
    for w in warnings:
        print(f"warning: {w}")
    for e in errors:
        print(f"error: {e}")
    print(f"{len(errors)} error(s), {len(warnings)} warning(s)")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
