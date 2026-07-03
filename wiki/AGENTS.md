# Wiki Instructions

These rules apply to durable notes under `wiki/`.

The wiki is the synthesized memory layer. It should be more stable, more careful, and less noisy than `inbox/` or `sources/`.

## Durable Page Rules

- Do not create a wiki page just because a term appeared once.
- Prefer updating an existing page when the new material fits an existing topic.
- Create a new page only when the topic is likely to be useful again.
- Keep transcript-derived claims traceable to source files.
- Keep uncertain names, acronyms, and jargon out of page titles unless confirmed.
- Use `UNCERTAIN:` for important claims that depend on unclear transcript text.
- Do not create active TODO checkboxes or `TODO:` items in wiki pages.
- Put every active follow-up, task, owner commitment, or call to action in root `actions.md`.
- If a wiki page needs to mention active work, reference `[[actions]]` or describe the context without creating a separate TODO.
- If a page is mostly a bucket for unclear material, name it plainly, such as `unclear-captures.md`.

## Action References

When wiki content produces a follow-up:

- Add or update the task in root `actions.md`.
- Add new active tasks to `Open` by default, not `Today`.
- Move blocked tasks to `Waiting`.
- Move completed tasks to `Done`.
- Include `Context: [[page-name]]` linking back to the relevant wiki page.
- Include `Source: ` with the source file path that supports the action.
- Avoid duplicating existing open actions.
- Do not delete completed actions.

## Entity Pages

People, project, and concept pages have a higher bar than meeting source summaries.

Before creating one:

- Check whether a related page already exists.
- Confirm the name from an existing wiki page, repeated source usage, or clear source context.
- If the name is first-seen or possibly mistranscribed, flag it in review output instead of creating a new page.

## Page Titles

Use plain, durable titles:

- `# SMP Platform`
- `# Japan Interconnector Dashboard`
- `# AI Assisted Engineering`

Avoid titles that preserve obvious source typos or meeting-export artifacts:

- `# SMP Revie`
- `# New DAG Agent Meeting`

If the intended title is unclear, use the source title in `sources/` but avoid creating a durable wiki page with that title.

## Source References

Every durable page created from captured material should include:

```markdown
## Sources

- `sources/...`

Last Updated: YYYY-MM-DD
```
