#!/usr/bin/env python3
"""Tests for the recall-hint hook."""

from __future__ import annotations

import importlib.util
import os
import tempfile
import unittest
from pathlib import Path

SCRIPT_PATH = Path(__file__).with_name("recall-hint.py")


class RecallHintTest(unittest.TestCase):
    def setUp(self) -> None:
        tmp = Path(tempfile.mkdtemp())
        wiki = tmp / "wiki"
        (wiki / "smp").mkdir(parents=True)
        (wiki / "smp" / "darwin-collector.md").write_text("# Darwin Collector\n\nAs of 2026-10-07.\n")
        (wiki / "smp" / "smp-india.md").write_text("# SMP India\n\nAs of 2026-10-09. Khaba generation. Khaba again.\n")
        (wiki / "projects").mkdir()
        (wiki / "projects" / "thailand-2026.md").write_text("# Thailand 2026\n\nBangkok trip.\n")
        (wiki / "aliases.md").write_text(
            "# Aliases\n\n- **Khaba** (`khaba_generation`): Kaba, Kaaba, KAVA. Site.\n- **Bong**: Bang, Pong.\n"
        )
        os.environ["BARALUGA_WIKI"] = str(wiki)
        os.environ["BARALUGA_RECALL_STATE"] = str(tmp / "state")
        spec = importlib.util.spec_from_file_location("recall_hint", SCRIPT_PATH)
        assert spec and spec.loader
        self.mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.mod)

    def hint(self, prompt, session="s1", **extra):
        return self.mod.hint({"session_id": session, "prompt": prompt, **extra})

    def test_no_match_returns_nothing(self) -> None:
        self.assertIsNone(self.hint("refactor this python function please"))
        self.assertIsNone(self.hint("booking a flight to Bangkok"))  # Bang must not match Bangkok

    def test_page_name_and_alias_matches_with_as_of_date(self) -> None:
        text = self.hint("what's blocking the darwin collector and the Kaba feed?")
        self.assertIn("[[darwin-collector]] (as of 2026-10-07)", text)
        self.assertIn("[[smp-india]] (as of 2026-10-09)", text)
        self.assertNotIn("thailand", text)

    def test_each_page_hinted_once_per_session_and_non_user_prompts_skipped(self) -> None:
        self.assertIsNotNone(self.hint("darwin collector status"))
        self.assertIsNone(self.hint("darwin collector again"))
        self.assertIsNotNone(self.hint("darwin collector", session="s2"))
        self.assertIsNone(self.hint("darwin collector", session="s3", source="system"))


if __name__ == "__main__":
    unittest.main()
