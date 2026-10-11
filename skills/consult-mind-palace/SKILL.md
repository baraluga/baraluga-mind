---
name: consult-mind-palace
description: Search and synthesize the Baraluga Mind markdown second brain at `/Users/qn5792/baraluga-mind` from any working directory. Use when the user asks to consult, search, check, mine, or look into the "mind palace," their wiki, notes, memory, or accumulated knowledge about a topic; gather background for writing such as a Confluence page; find prior decisions, people, projects, evidence, open questions, or pending work; or answer what is already known about something from Baraluga Mind.
---

# Consult Mind Palace

Treat `/Users/qn5792/baraluga-mind` as the canonical root. Use absolute paths in commands so the workflow works from any current directory.

## Search Workflow

1. Confirm the root exists. If it does not, report the missing path and stop.
2. Read `/Users/qn5792/baraluga-mind/AGENTS.md` and any nested `AGENTS.md` that applies to files being read or changed.
3. Translate the request into search terms: the exact phrase, obvious spelling or acronym variants, related project and person names, and likely Obsidian page slugs. Do not invent speculative synonyms.
4. Search filenames, headings, body text, and Obsidian links with `rg`. Start with `wiki/`, then search `sources/` for evidence and details. Search `inbox/` only when the user asks for exhaustive or very recent knowledge, and label unprocessed material clearly.
5. Open the most relevant durable pages in full. Read `Current State` first and note its "as of" date; treat `History` as turning points only. Follow their `[[wiki-links]]` and `Sources` references when they materially expand or verify the answer.
6. For pending work, use the dated pending items in each page's `Current State`, then verify against recent sources. `actions.md` is a frozen archive from before 2026-10-11; cite it only for historical context, and do not infer that any item belongs to the user.
7. Inspect relevant source passages directly before making detailed claims. For transcript-derived material, preserve uncertainty around unfamiliar names, acronyms, owners, dates, and jargon.
8. Stop when additional matches are duplicates or add no material context. If the query is ambiguous, present the likely interpretation and mention the uncovered alternative instead of silently choosing.

Example discovery commands:

```bash
rg --files /Users/qn5792/baraluga-mind/wiki /Users/qn5792/baraluga-mind/sources /Users/qn5792/baraluga-mind/inbox
rg -n -i --glob '*.md' 'term|variant' /Users/qn5792/baraluga-mind/wiki
rg -n -i --glob '*.md' 'term|variant' /Users/qn5792/baraluga-mind/sources
```

Use quoted patterns and `rg -F` when search terms contain regular-expression characters.

## Evidence Model

Apply this precedence without hiding disagreement:

- `wiki/`: durable synthesized knowledge; use as the organizing layer.
- `wiki/decisions/`: explicit decisions; distinguish them from proposals or discussion.
- `sources/`: captured evidence and finer detail; use to verify and enrich durable pages. A source newer than a page's `Current State` date may supersede it.
- `inbox/`: unprocessed captures; treat as provisional.

State facts as facts only when supported. Label interpretations as inferences. Preserve `UNCERTAIN:` claims and surface conflicting or stale-looking evidence with dates and paths. Never fabricate missing context.

## Response Shape

Adapt the depth to the request. For broad requests such as “everything we know about X,” provide:

1. A concise synthesis suitable for the user's immediate purpose.
2. Relevant facts and context, grouped by durable theme rather than by file.
3. Explicit decisions and rationale.
4. Pending work, open questions, conflicts, and uncertain claims, each clearly labeled.
5. A short source trail containing the most useful wiki pages and primary captures.

Prefer direct prose over a raw search-results dump. Include relevant dates. Cite repository-relative paths in backticks and, when the client supports it, make key local files clickable using their absolute paths. Say plainly when the mind palace contains little or no relevant information.

For writing support, first return a source-backed briefing tailored to the requested artifact. Draft the artifact only when the user asks for a draft or when drafting is clearly part of the request.

## Mutation Boundary

Default to read-only consultation. Do not edit, ingest, reorganize, commit, or push the mind palace unless the user explicitly asks. If mutation is requested, follow all applicable repository instructions, preserve raw inputs, and validate the complete diff before reporting completion.
