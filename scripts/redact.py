"""Shared secret redaction for conversation captures (Codex exporter, Claude hook).

ponytail: pattern-based only; it catches labelled and obviously-shaped secrets. CI's gitleaks
scan is the backstop for anything that slips through.
"""

from __future__ import annotations

import re

REDACTIONS = [
    (re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----.*?-----END [A-Z ]*PRIVATE KEY-----", re.S), "[REDACTED: private key]"),
    # Real JWTs have three dot-separated parts; base64 URL params starting with eyJ do not.
    (re.compile(r"eyJ[A-Za-z0-9_\\-]{10,}\.[A-Za-z0-9_\\-]{10,}\.[A-Za-z0-9_\\-]{10,}"), "[REDACTED: JWT]"),
    (re.compile(r"(?i)\b(bearer)\s+[A-Za-z0-9._~+/=-]{16,}"), r"\1 [REDACTED]"),
    (re.compile(r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b"), "[REDACTED: aws key]"),
    (re.compile(r"\b(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,}|sk-[A-Za-z0-9_-]{20,}|xox[abpr]-[A-Za-z0-9-]{10,})"), "[REDACTED: token]"),
    # Labelled values, including JSON keys such as "approval_token": "...".
    (re.compile(r"(?i)\b([\w-]*(?:password|passwd|pwd|secret|api[_-]?key|token))(\"?\s*[:=]\s*[\"']?)([^\s\"',]{4,})"), r"\1\2[REDACTED]"),
]
# A line that announces credentials ("here are the creds:") followed by bare values on the next lines.
CRED_INTRO = re.compile(r"(?i)\b(creds?|credentials?|passwords?|secrets?|tokens?|api[ _-]?keys?|client[ _-]?secret)\b[^\n]*:\s*$")
BARE_VALUE = re.compile(r"^\s*\S{16,}\s*$")


def redact(text: str) -> str:
    for pattern, replacement in REDACTIONS:
        text = pattern.sub(replacement, text)
    lines = text.split("\n")
    for i, line in enumerate(lines):
        if CRED_INTRO.search(line):
            # Redact bare values on the following lines, skipping blanks, until prose resumes.
            for j in range(i + 1, min(i + 6, len(lines))):
                if not lines[j].strip():
                    continue
                if not BARE_VALUE.match(lines[j]):
                    break
                lines[j] = "[REDACTED: credential]"
    return "\n".join(lines)
