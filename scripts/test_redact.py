#!/usr/bin/env python3
"""Tests for shared secret redaction."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from redact import redact  # noqa: E402

JWT = "eyJhbGciOiJIUzI1NiJ9" + ".eyJzdWIiOiIxMjM0NTY3ODkwIn0" + ".SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"


class RedactTest(unittest.TestCase):
    def test_bare_values_after_a_credentials_intro_line(self) -> None:
        text = "Here are the creds:\n\n0oaABCDEFGHIJ1234567\nkeAbcdefghijklmnopqrstuvwxyz0123456789ABCDEFGH\n\nThink we can do that?"
        out = redact(text)
        self.assertNotIn("0oaABCDEFGHIJ", out)
        self.assertNotIn("keAbcdef", out)
        self.assertIn("Think we can do that?", out)

    def test_three_part_jwt_redacted_but_base64_url_params_kept(self) -> None:
        self.assertNotIn(JWT, redact(f"token:\n{JWT}"))
        self.assertNotIn(JWT, redact(f"see {JWT} here"))
        url = "wiki?xpis=eyJhIjoiYiIsImMiOiJkIiwiZSI6ImYiLCJnIjoiaCJ9fQ"
        self.assertEqual(redact(url), url)

    def test_labelled_values_including_json_keys(self) -> None:
        out = redact('password: hunter22\n"approval_token": "810fabcdef0123456789",\n"execute": true')
        self.assertNotIn("hunter22", out)
        self.assertNotIn("810fabcdef", out)
        self.assertIn('"execute": true', out)

    def test_ordinary_prose_untouched(self) -> None:
        prose = "The token budget is fine. Here is the plan:\nShip the dashboard on Friday after review."
        self.assertEqual(redact(prose), prose)


if __name__ == "__main__":
    unittest.main()
