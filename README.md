# Baraluga Mind

This is a lightweight, AI-maintained second brain.

The goal is not to manually write perfect notes. The goal is to capture raw material with low friction, then have an AI maintain a clean markdown wiki from it.

## Workflow

1. Drop raw captures into `inbox/`.
2. Move source files into the right `sources/` folder when useful.
3. Ask an AI agent to run the ingest workflow in `scripts/ingest.md`.
4. Review the resulting wiki changes for accuracy.

## Folder Map

- `inbox/` - temporary landing zone for messy captures, pasted notes, transcripts, links, and voice dumps.
- `sources/articles/` - saved articles, web clips, and reading notes.
- `sources/meetings/` - meeting transcripts, summaries, agendas, and decisions.
- `sources/voice/` - dictated thoughts and voice-note transcripts.
- `sources/pdfs/` - PDFs and extracted PDF notes.
- `wiki/people/` - durable notes about people, teams, stakeholders, and relationships.
- `wiki/projects/` - durable notes about active or past projects.
- `wiki/concepts/` - durable notes about reusable ideas, patterns, topics, and frameworks.
- `wiki/decisions/` - durable records of decisions, rationale, tradeoffs, and open questions.
- `scripts/` - repeatable prompts and runbooks for maintaining the system.

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
