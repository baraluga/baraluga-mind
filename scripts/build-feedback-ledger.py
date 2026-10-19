"""Build the Feedback Ledger page from the `## Feedback Notes` sections of wiki/people/*.md.

Usage: python3 -B scripts/build-feedback-ledger.py [out.html]
Default output: outputs/feedback-ledger.html. Republish the output to the Feedback Ledger artifact URL to refresh it.
"""

import datetime
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ITEM = re.compile(
    r"^- \*\*(Strength|Growth|Received strength|Received growth)\*\* \((\d{4}-\d{2}-\d{2})\)(?:, from ([^:]+))?: (.*)$"
)
SOURCE = re.compile(r"\s*`(sources/[^`]+)`\s*$")


def section(text: str, heading: str) -> str:
    m = re.search(rf"^## {heading}\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    return m.group(1) if m else ""


def parse(path: Path) -> dict | None:
    text = path.read_text()
    notes = section(text, "Feedback Notes")
    if not notes:
        return None
    state = re.sub(r"^\s*As of [\d-]+\.\s*", "", section(text, "Current State").strip())
    person = {
        "slug": path.stem,
        "name": text.splitlines()[0].lstrip("# ").strip(),
        "role": state.split("\n")[0],
        "items": [],
        "caveats": [],
    }
    for line in notes.splitlines():
        if line.startswith("- UNCERTAIN:"):
            person["caveats"].append(line[2:].strip())
            continue
        m = ITEM.match(line)
        if not m:
            continue
        kind, date, giver, body = m.groups()
        src = SOURCE.search(body)
        body = SOURCE.sub("", body).strip()
        ask = None
        if " Ask: " in body:
            body, ask = body.split(" Ask: ", 1)
        person["items"].append(
            {"kind": kind.lower(), "date": date, "from": giver, "text": body, "ask": ask, "source": src.group(1) if src else None}
        )
    return person


def build() -> dict:
    people = [p for f in sorted((ROOT / "wiki/people").glob("*.md")) if (p := parse(f))]
    return {"built": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), "people": people}


if __name__ == "__main__":
    data = build()
    sample = parse(ROOT / "wiki/people/michael.md")
    assert sample and any(i["ask"] for i in sample["items"]), "parser lost growth asks"
    assert all(i["source"] for p in data["people"] for i in p["items"]), "item without a source"
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "outputs/feedback-ledger.html"
    template = (ROOT / "scripts/feedback-ledger.html").read_text()
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(template.replace("/*DATA*/null", json.dumps(data, ensure_ascii=False).replace("</", "<\\/")))
    print(f"{out}: {len(data['people'])} people, {sum(len(p['items']) for p in data['people'])} notes")
