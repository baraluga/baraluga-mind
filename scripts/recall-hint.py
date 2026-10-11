#!/usr/bin/env python3
"""Hint relevant Baraluga Mind pages when a prompt mentions something the wiki knows.

Runs as a Claude Code `UserPromptSubmit` hook. Matches the prompt (whole words,
case-insensitive) against wiki page titles/slugs and the confirmed names in
`wiki/aliases.md`. Prints nothing when nothing matches, so unmatched prompts cost
zero tokens. Each page is hinted at most once per session. Never fails the hook.
"""

from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path

WIKI = Path(os.environ.get("BARALUGA_WIKI", Path.home() / "baraluga-mind" / "wiki"))
STATE_DIR = Path(os.environ.get("BARALUGA_RECALL_STATE", Path.home() / ".cache" / "baraluga-mind" / "recall"))
MAX_PAGES = 4
SKIP_PAGES = {"index", "aliases", "AGENTS", "CLAUDE"}
AS_OF = re.compile(r"As of (\d{4}-\d{2}-\d{2})")


def pages() -> dict[str, Path]:
    return {p.stem: p for p in WIKI.rglob("*.md") if p.stem not in SKIP_PAGES}


def page_names(slug: str, path: Path) -> set[str]:
    title = path.read_text(errors="ignore").split("\n", 1)[0].removeprefix("# ").removeprefix("Decision: ")
    words = title.split()
    # Two-word pieces let "japan interconnector" find "Japan Interconnector Dashboard".
    names = {title, slug.replace("-", " "), *(" ".join(words[i:i + 2]) for i in range(len(words) - 1))}
    return {n.strip() for n in names if len(n.strip()) >= 4}


def alias_lines() -> list[list[str]]:
    """Each confirmed entity as [canonical, variant, ...]."""
    groups = []
    for line in (WIKI / "aliases.md").read_text(errors="ignore").splitlines():
        m = re.match(r"- \*\*(.+?)\*\*(?: \([^)]*\))?: (.+?)(?:\. |\.$|$)", line)
        if m:
            variants = [v.strip() for v in re.split(r",|\bbut\b", m.group(2)) if v.strip()]
            groups.append([m.group(1)] + [v for v in variants if len(v.split()) <= 3])
    return groups


def mentions(text: str, name: str) -> bool:
    return re.search(rf"(?<![\w-]){re.escape(name)}(?![\w-])", text, re.I) is not None


def match(prompt: str) -> list[str]:
    all_pages = pages()
    hits: dict[str, int] = {}
    for slug, path in all_pages.items():
        if any(mentions(prompt, n) for n in page_names(slug, path)):
            hits[slug] = hits.get(slug, 0) + 100  # a direct page-name mention ranks first
    for group in alias_lines():
        if any(mentions(prompt, n) for n in group):
            canonical = group[0]
            for slug, path in all_pages.items():
                count = len(re.findall(rf"(?<![\w-]){re.escape(canonical)}(?![\w-])", path.read_text(errors="ignore"), re.I))
                if count:
                    hits[slug] = hits.get(slug, 0) + count
    return sorted(hits, key=lambda s: -hits[s])[:MAX_PAGES]


def as_of(path: Path) -> str:
    m = AS_OF.search(path.read_text(errors="ignore"))
    return f" (as of {m.group(1)})" if m else ""


def hint(hook: dict) -> str | None:
    if hook.get("source") not in (None, "user"):
        return None
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    state_path = STATE_DIR / f"{hook['session_id']}.json"
    seen = set(json.loads(state_path.read_text())) if state_path.exists() else set()
    new = [s for s in match(hook.get("prompt", "")) if s not in seen]
    if not new:
        return None
    state_path.write_text(json.dumps(sorted(seen | set(new))))
    all_pages = pages()
    listed = ", ".join(f"[[{s}]]{as_of(all_pages[s])}" for s in new)
    return (f"Baraluga Mind has pages on this: {listed}. "
            "Consult them with the consult-mind-palace skill only if past context matters for the answer.")


def main() -> None:
    try:
        text = hint(json.load(sys.stdin))
        if text:
            print(json.dumps({"hookSpecificOutput": {"hookEventName": "UserPromptSubmit", "additionalContext": text}}))
    except Exception as exc:  # never block the user's prompt over a hint failure
        print(f"baraluga recall skipped: {exc}", file=sys.stderr)


if __name__ == "__main__":
    main()
