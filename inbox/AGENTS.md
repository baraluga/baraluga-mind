# Daily Capture Instructions

These rules apply to live daily notes in `inbox/`.

## Live Note Shape

Use `YYYY-MM-DD.md` for the current Asia/Manila date:

```markdown
# YYYY-MM-DD

## Today

## Notes

## Timeline

Last Updated: YYYY-MM-DD
```

- `Today` is a provisional, stateful view of inferred tasks and status changes.
- `Notes` contains non-actionable observations, ideas, decisions, and reflections.
- `Timeline` preserves each raw chat dump once under a local-time heading.

## Stateful Updates

- Add inferred tasks as unchecked checkboxes.
- When later evidence completes a task, change it to `[x]`, strike through its text, and add a timestamped completion annotation.
- Preserve cancelled and superseded tasks with a struck-through entry and source-backed reason.
- Keep blocked or waiting tasks unchecked and annotate their state.
- Update existing entries instead of adding semantic duplicates.
- Do not delete raw timeline entries.
- Use `UNCERTAIN:` for ambiguous owners, names, acronyms, dates, or high-impact interpretations.

## Ingest Handoff

- Daily-note tasks are provisional capture, not the canonical action register.
- Leave the current Asia/Manila day's live note in `inbox/` unless the user explicitly asks to close or ingest it.
- During ingest, reconcile unresolved and completed items with root `actions.md`.
- Move the processed note to `sources/notes/YYYY-MM-DD.md`.
- When the same dump also appears in a Codex conversation export, prefer this daily note as the structured source and use the transcript only as backup evidence. Do not duplicate actions or durable claims.
