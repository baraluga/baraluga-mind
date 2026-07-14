# Ingest Workflow

Use this prompt with Codex, Claude Code, or another agent that can read and write this folder.

```text
Process the new material in `inbox/` and update this markdown second brain.

Follow `AGENTS.md`.

Goals:
- Preserve raw inputs during ingest.
- Create or update durable wiki pages under `wiki/`.
- Add or update captured follow-up work in root `actions.md`.
- Put newly captured actions in `Open` by default; use `Waiting` only for blocked work and `Today` only when the user explicitly prioritizes it.
- Prefer updating existing pages over creating duplicates.
- Link related pages with Obsidian-style links.
- Mark uncertainty explicitly.
- Move processed `inbox/` files to the appropriate `sources/` folder when they remain useful as evidence.
- Leave files in `inbox/` when they still need follow-up, review, or clarification.
- Give me a concise changelog when finished.
- End with a `Needs Confirmation` handover that lists only suspicious terms, ambiguous owners, uncertain claims, and other clarification items worth asking me about.
- Do not surface the full `Open` action register as my assignment unless I explicitly ask for it.

Do not delete files unless I explicitly ask.
```

## Manual Ingest Checklist

1. Read `AGENTS.md`.
2. List files in `inbox/`.
3. Search `wiki/` for related existing pages.
4. Create or update the smallest useful set of pages.
5. Add or update active follow-up work in `actions.md`.
6. Add source references.
7. Move processed `inbox/` files worth preserving to the right `sources/` folder.
8. Validate source references, wiki links, action sections, duplicate actions, current `Last Updated` dates, and synthesized-file whitespace.
9. Report what changed.
10. Include a `Needs Confirmation` handover:
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
