# Ingest Workflow

Use this prompt with Codex, Claude Code, or another agent that can read and write this folder.

```text
Process the new material in `inbox/` and update this markdown second brain.

Follow `AGENTS.md`.

Goals:
- Preserve the raw inputs.
- Create or update durable wiki pages under `wiki/`.
- Prefer updating existing pages over creating duplicates.
- Link related pages with Obsidian-style links.
- Mark uncertainty explicitly.
- Give me a concise changelog when finished.

Do not move or delete files unless I explicitly ask.
```

## Manual Ingest Checklist

1. Read `AGENTS.md`.
2. List files in `inbox/`.
3. Search `wiki/` for related existing pages.
4. Create or update the smallest useful set of pages.
5. Add source references.
6. Report what changed.

## Optional Capture Prompts

For a messy voice note:

```text
Turn this into durable notes for my second brain. Extract projects, people, decisions, concepts, action items, and uncertainty. Preserve anything that sounds like a direct quote or strong preference.
```

For a meeting transcript:

```text
Extract decisions, action items, open questions, project context, people, and durable background. Update existing wiki pages instead of creating duplicates.
```

For an article:

```text
Extract the durable ideas, useful claims, examples, caveats, and related concepts. Do not summarize every paragraph. Add uncertainty where the source may be weak or time-sensitive.
```
