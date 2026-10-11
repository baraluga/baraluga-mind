# Ingest Workflow

Use this prompt with Codex, Claude Code, or another agent that can read and write this folder.

```text
Process the new material in `inbox/` and update this markdown second brain.

Follow `AGENTS.md`.

Goals:
- Preserve raw inputs during ingest.
- Apply an ingest-value gate before moving files: empty exports, scheduled-automation transcripts, capture bookkeeping, and repeated status-only records are no-ops.
- Ingest a conversation capture only when a user-initiated exchange adds a durable fact, decision, action, open question, or reusable context.
- Create or update durable wiki pages under `wiki/`. Rewrite each touched page's `Current State` instead of appending dated bullets, and update people pages for anyone mentioned.
- Do not touch `actions.md`; it is a frozen archive.
- Prefer updating existing pages over creating duplicates.
- Link related pages with Obsidian-style links.
- Mark uncertainty explicitly.
- Move processed `inbox/` files to the appropriate `sources/` folder when they remain useful as evidence.
- Treat `YYYY-MM-DD-codex-conversations.md` and its paired `.txt` transcript as one source: review the text evidence and move both files together without changing the transcript back to Markdown.
- Leave files in `inbox/` when they still need follow-up, review, or clarification.
- Give me a concise changelog when finished.
- If no inbox item passes the value gate, do not edit, move, commit, or push anything; report a clean no-op.
- End with a `Needs Confirmation` handover that lists only suspicious terms, ambiguous owners, uncertain claims, and other clarification items worth asking me about.

Do not delete files unless I explicitly ask.
```

## Manual Ingest Checklist

1. Read `AGENTS.md`.
2. List files in `inbox/`.
3. Apply the ingest-value gate and stop as a no-op when no item adds durable information.
4. Search `wiki/` for related existing pages.
5. Create or update the smallest useful set of pages.
6. Rewrite `Current State` on every touched page, including people pages; replace superseded claims.
7. Add source references.
8. Move processed `inbox/` files worth preserving to the right `sources/` folder. Keep Codex conversation `.md`/`.txt` pairs together.
9. Validate source references, wiki links, current `Last Updated` dates, and synthesized-file whitespace.
10. Commit and push only when at least one item passed the value gate and produced a durable source or wiki change.
11. Report what changed.
12. Include a `Needs Confirmation` handover:
    - group suspicious names, acronyms, systems, projects, jargon, ambiguous owners, and uncertain high-impact claims by durable area;
    - include why each item needs confirmation;
    - include the source path or related wiki page;
    - omit routine TODOs, low-priority maybe-later topics, `Open`, `Waiting`, and `Done` action lists unless explicitly requested.

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
