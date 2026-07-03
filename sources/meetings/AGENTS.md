# Meeting Source Instructions

These rules apply to meeting notes, meeting summaries, Granola exports, and transcript-derived files in this folder.

## Transcript Accuracy

Meeting notes and transcripts may contain incorrect speaker names, product names, acronyms, dates, and domain jargon.

When processing meeting sources:

- Treat unfamiliar names, acronyms, systems, project names, and domain jargon as provisional.
- Treat terms that appear for the first time as provisional unless they match an existing wiki page or another reliable source.
- Cross-check names and terms against existing `wiki/` pages before normalizing them.
- Do not silently correct a suspicious term unless the correction is obvious from nearby context.
- Do not create new people, project, or concept pages from low-confidence transcript text.
- Preserve uncertain terms with `UNCERTAIN:` instead of guessing the intended meaning.
- If a term affects a decision, action item, owner, or durable project context, flag it in the ingest review output for confirmation.
- Prefer quoting a short source phrase around an uncertain term over replacing it with a guess.

## Action Capture

Meeting sources can contain `Next Steps` as part of the source summary, but active task tracking belongs in root `actions.md`.

When a meeting contains a follow-up, owner commitment, or call to action:

- Add or update the action in root `actions.md`.
- Link `Context` to the relevant wiki page when one exists.
- Link `Source` to the meeting source file.
- Do not create active TODOs only in meeting source files or wiki pages.
- If the owner, term, or task wording is uncertain because of transcript quality, flag it for confirmation in the ingest review output before creating a high-confidence action.

## First-Time Term Review

Flag first-time terms when they look like:

- people
- teams
- projects
- systems
- products
- acronyms
- domain-specific jargon
- action owners
- possible transcription artifacts

Ignore common words, generic meeting phrases, and obvious one-off wording.

Use this review shape:

```markdown
## Names Or Terms Needing Confirmation

- `Term` - first seen in `sources/meetings/file-name.md`; why it may need confirmation.
```

## Meeting Source Shape

Meeting source files should stay close to the source evidence. Summarize lightly, but do not over-synthesize here. Durable synthesis belongs under `wiki/`.

Use this structure when normalizing a new meeting source:

```markdown
# Meeting Title

Source type: Granola meeting notes
Meeting ID: `...`
Date: YYYY-MM-DD HH:MM timezone
Participants known to source: ...

Note: This is from meeting notes or transcript-derived material and may contain transcription errors.

## Discussed

- ...

## Decisions

- ...

## Next Steps

- ...

## Open Questions

- UNCERTAIN: ...

Last Updated: YYYY-MM-DD
```

Omit empty sections.
