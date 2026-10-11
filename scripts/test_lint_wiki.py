#!/usr/bin/env python3
"""Tests for the wiki linter."""

from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path

SCRIPT_PATH = Path(__file__).with_name("lint-wiki.py")
SPEC = importlib.util.spec_from_file_location("lint_wiki", SCRIPT_PATH)
assert SPEC and SPEC.loader
LINT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(LINT)


class LintWikiTest(unittest.TestCase):
    def setUp(self) -> None:
        self.root = Path(tempfile.mkdtemp())
        (self.root / "sources" / "meetings").mkdir(parents=True)
        (self.root / "sources" / "meetings" / "m.md").write_text("x")
        self.write("index.md", "# Index\n\n- [[good]]\n- [[aliases]]\n")
        self.write("aliases.md", "# Aliases\n\n- **Khaba** (`k`): Kaba, KAVA. A site.\n")
        self.write("smp/good.md", "# Good\n\n## Current State\n\nSee [[aliases]]. Source: `sources/meetings/m.md`.\n")

    def write(self, rel: str, text: str) -> None:
        path = self.root / "wiki" / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)

    def test_clean_wiki_passes(self) -> None:
        self.assertEqual(LINT.lint(self.root), ([], []))

    def test_reports_each_error_kind(self) -> None:
        self.write("smp/bad.md", "# Bad\n\n[[nowhere]] `sources/meetings/gone.md`\n- [ ] todo\n")
        self.write("aliases.md", "# Aliases\n\n- **Broken** no colon\n")
        errors, warnings = LINT.lint(self.root)
        joined = "\n".join(errors)
        for expected in ("broken link [[nowhere]]", "gone.md", "checkbox", "page not listed: [[bad]]", "aliases.md:3"):
            self.assertIn(expected, joined)
        self.assertIn("wiki/smp/bad.md: not yet in current-state shape", warnings)

    def test_glob_citations_and_decision_pages_are_not_flagged(self) -> None:
        self.write("index.md", "# Index\n\n- [[good]]\n- [[aliases]]\n- [[2026-07-14-decision]]\n")
        self.write("decisions/2026-07-14-decision.md", "# Decision: X\n\nSee `sources/notes/*-clarifications.md`.\n")
        self.assertEqual(LINT.lint(self.root), ([], []))


if __name__ == "__main__":
    unittest.main()
