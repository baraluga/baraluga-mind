# Baraluga Mind Agent Instructions

You are maintaining a local markdown second brain.

Your job is to turn raw captures into durable, useful wiki pages without inventing facts.

## Core Rules

- Read any nested `AGENTS.md` files that apply to the files being processed or edited.
- Preserve source material during ingest.
- Do not delete raw inputs unless explicitly asked.
- After processing an `inbox/` file, move it to the appropriate `sources/` folder when it remains useful as evidence.
- Leave an `inbox/` file in place when it still needs follow-up, review, or clarification.
- Do not fabricate details, links, names, dates, or decisions.
- Distinguish facts from inferences.
- Prefer small updates to existing wiki pages over creating duplicate notes.
- Link related wiki pages using Obsidian-style links like `[[concept-name]]`.
- Keep prose direct, dense, and useful.
- Use `UNCERTAIN:` when a claim needs verification.
- If source material is ambiguous, say so in the page.

## Purpose

This is a reference memory, not a task tracker. Optimize every page for "what do I need to remember about this right now?"

- `actions.md` is retired as of 2026-10-11 and kept only as a frozen archive. Do not add, update, or reconcile actions.
- Commitments and follow-ups stay in source summaries (`Next Steps`). When one matters to a topic, mention it once in that page's `Current State` as pending, with a date. Never use checkboxes in wiki pages.

## Current-State Rule

Wiki pages describe the present, not a diary of updates.

- Rewrite `Current State` on every ingest that touches the page. Do not append dated bullets to it.
- When new evidence supersedes a claim, replace or remove the old claim. The sources keep the history.
- Put a dated line in `History` only for real turning points: role changes, reversals, launches, decisions. Keep it terse.
- Date volatile facts inline ("as of YYYY-MM-DD") so staleness is visible.
- When an ingest mentions a person or project that has a page, update that page too, not only the topic page the source is mainly about.
- Split a page that grows past roughly 1,500 words into linked sub-pages.

## File Naming

Use lowercase kebab-case for all new files and directories.

Good:

- `wiki/concepts/second-brain.md`
- `wiki/projects/baraluga-mind.md`
- `wiki/decisions/2026-07-04-use-markdown-wiki.md`
- `inbox/2026-07-04-team-sync.md`

Avoid:

- `Second Brain.md`
- `second_brain.md`
- `Team Sync.md`
- `2026_07_04_notes.md`

## Process Improvement

Do not edit `AGENTS.md`, `CLAUDE.md`, or nested instruction files during normal ingest unless explicitly asked.

If you notice repeated friction, ambiguity, bad output, a useful convention, or instruction bloat, append a short note to `process-notes.md` instead.

Use this format:

```markdown
### YYYY-MM-DD

- Observation: ...
- Suggested rule: ...
- Example: ...
```

Instruction files should stay small and scoped. Prefer one local, source-specific instruction over expanding the root file when a rule applies only to one folder or content type.

## Ingest Behavior

When processing files from `inbox/` or `sources/`:

1. Identify the source type: article, meeting, voice note, PDF, pasted note, or mixed capture.
2. Apply an ingest-value gate before moving or editing anything:
   - Scheduled-automation transcripts, empty/zero-session exports, capture bookkeeping, and repeated status-only records are not ingest-worthy.
   - A conversation capture is ingest-worthy only when it contains at least one user-initiated exchange that adds a durable fact, decision, action, open question, or reusable project/person/concept context.
   - If every inbox item fails this gate, make no source, wiki, action, commit, or push changes. Leave pre-existing raw inputs untouched and report a no-op.
3. Extract durable entities:
   - people
   - projects
   - concepts
   - decisions
   - open questions
4. Update existing pages when possible, following the Current-State Rule: rewrite `Current State` for every page the source touches, including people pages.
5. Create new pages only when the topic is likely to matter again.
6. Keep `Background` for slow-changing context; move anything time-sensitive into `Current State`.
7. Add a short `Sources` section with the source filename or path.
8. Move processed `inbox/` files to the appropriate `sources/` subfolder when they remain useful as evidence:
   - `sources/articles/` for articles, links, and reading notes
   - `sources/meetings/` for meeting transcripts, agendas, and summaries
   - `sources/voice/` for voice-note transcripts and dictated thoughts
   - `sources/pdfs/` for PDFs and extracted PDF notes
   - `sources/notes/` for manual or AI-maintained daily notes
   - Leave the current Asia/Manila day's live daily note in `inbox/` unless the user explicitly asks to close or ingest it.
   - Preserve a closed `inbox/YYYY-MM-DD.md` daily note in `sources/notes/`.
   - When a daily note duplicates content in a Codex conversation export, prefer the structured daily note and use the transcript as backup evidence.
9. Add a short `Last Updated` date using `YYYY-MM-DD`.
10. Validate the complete ingest diff. Commit and push using an unscoped conventional commit only when the ingest produced a durable source or wiki change that passed the value gate.

## Wiki Page Shape

Use this structure for durable pages. When an ingest touches a page still in the older `Summary`/`Details` shape, convert it.

```markdown
# Page Title

## Current State

As of YYYY-MM-DD. What is true now: status, owners, blockers, pending items. Rewritten, never appended.

## Background

Slow-changing context: what it is, why it exists, how it works, who is involved.

## History

- YYYY-MM-DD: turning points only.

## Open Questions

- UNCERTAIN: ...

## Sources

- `sources/...`

Last Updated: YYYY-MM-DD
```

If a section is not useful, omit it.

## Decision Page Shape

Use `wiki/decisions/YYYY-MM-DD-short-decision.md`.

```markdown
# Decision: Short Decision

## Decision

State the decision plainly.

## Context

Why this came up.

## Rationale

Why this option was chosen.

## Tradeoffs

What this makes easier or harder.

## Sources

- `sources/...`

Last Updated: YYYY-MM-DD
```

## Review Output

After an ingest pass, report:

- pages created
- pages updated
- source files processed
- uncertain claims
- new or suspicious names, acronyms, systems, projects, or jargon needing confirmation
- suggested next cleanup

Also include a consolidated handover section titled `Needs Confirmation`.

`Needs Confirmation` should be pleasant to scan and useful as a one-by-one clarification queue for the user. It should include only:

- all current needs-confirmation items from the ingest review, including suspicious names, acronyms, systems, projects, jargon, ambiguous owners, and uncertain high-impact claims.

Format `Needs Confirmation` as grouped checklists by durable area when possible, such as `Team Operations`, `SMP Platform`, `Japan Interconnector`, and `Alerting and Ops`.

For each item, include:

- the exact term or claim to confirm;
- why confirmation is needed;
- the source path or related wiki page.

Keep `Needs Confirmation` concise enough to work through manually. Exclude items that are merely low-priority, already resolved, or not currently worth asking the user about.
