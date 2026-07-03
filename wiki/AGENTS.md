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
- Do not turn every action item into a durable TODO. Only keep TODOs that still matter outside the meeting.
- If a page is mostly a bucket for unclear material, name it plainly, such as `unclear-captures.md`.

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
