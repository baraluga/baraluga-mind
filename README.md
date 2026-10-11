# Baraluga Mind

This is a lightweight, AI-maintained second brain.

The goal is not to manually write perfect notes. The goal is to capture raw material with low friction, then have an AI maintain a clean markdown wiki from it.

## Workflow

Everything runs on a schedule, with no manual step required:

1. At 00:10 Asia/Manila, capture automations export the previous day's Codex, GitHub Copilot, and Granola material into `inbox/`.
2. At 00:30, the ingest automation follows `scripts/ingest.md`: it gates for durable value, moves evidence to `sources/`, rewrites the affected wiki pages, then commits and pushes.
3. Skim the ingest report and diff for accuracy when convenient.

Claude Code conversations are captured continuously instead. A `Stop` hook in `~/.claude/settings.json` runs `scripts/capture-claude-conversation.py` after every turn, appending new messages to `inbox/YYYY-MM-DD-claude-<project>-<session8>.txt`.

Anything else can be dropped into `inbox/` by hand, and the next run picks it up.

## Folder Map

- `inbox/` - temporary landing zone for automated exports and anything dropped in by hand.
- `sources/articles/` - saved articles, web clips, and reading notes.
- `sources/meetings/` - meeting transcripts, summaries, agendas, and decisions.
- `sources/voice/` - dictated thoughts and voice-note transcripts.
- `sources/notes/` - manual notes and historical daily notes preserved as source evidence.
- `sources/pdfs/` - PDFs and extracted PDF notes.
- `sources/codex-conversations/` - small Markdown indexes paired with complete raw `.txt` transcripts so Obsidian does not parse oversized conversation exports.
- `wiki/index.md` - every page, grouped by area. Start here.
- `wiki/smp/` - all SMP pages (platform, India, Japan, dashboards, ops, tooling), kept together because SMP dominates the captures.
- `wiki/people/` - durable notes about people, teams, stakeholders, and relationships.
- `wiki/projects/` - durable notes about active or past projects.
- `wiki/concepts/` - durable notes about reusable ideas, patterns, topics, and frameworks.
- `wiki/decisions/` - durable records of decisions, rationale, tradeoffs, and open questions.
- `scripts/` - repeatable prompts and runbooks for maintaining the system.
- `skills/` - agent skills shared by Codex and Claude Code. Each skill is symlinked from `~/.codex/skills/<name>` and `~/.claude/skills/<name>`. To set one up on a new machine:

  ```bash
  for d in ~/.codex/skills ~/.claude/skills; do ln -s ~/baraluga-mind/skills/consult-mind-palace "$d/consult-mind-palace"; done
  ```

## Naming

Use lowercase, hyphenated filenames:

```text
wiki/projects/example-project.md
wiki/concepts/second-brain.md
wiki/decisions/2026-07-03-use-markdown-wiki.md
```

Prefer stable topic names over dates, except for decisions and time-bound logs.

## Maintenance Rule

Raw material can be messy. Wiki pages should be useful.

Every wiki page should make it clear what is known, what is inferred, what is uncertain, and where the information came from.

Codex conversation captures are emitted as a pair: an Obsidian-safe Markdown index and a raw text transcript. Keep and move both files together during ingest; do not rename a large transcript to `.md`.
