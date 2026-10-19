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
- Do not create TODO checkboxes or `TODO:` items in wiki pages. Mention pending work once, dated, in `Current State`.
- Follow the root Current-State Rule: rewrite `Current State`, replace superseded claims, and keep `History` to turning points.
- If a page is mostly a bucket for unclear material, name it plainly, such as `unclear-captures.md`.
- Put every SMP page (platform, India, Japan, dashboards, ops, SMP tooling) in `wiki/smp/`. Other pages stay in `people/`, `projects/`, `concepts/`, or `decisions/`. Wiki-links resolve by page name, so moving a page never breaks links.
- Maintain `wiki/aliases.md`. Use the canonical name in pages. Add a variant to its line only when Brian confirms it or the evidence is unambiguous, and resolve any `UNCERTAIN:` line it settles. Leave unconfirmed matches as `UNCERTAIN:` and list them under `Needs Confirmation`.
- Keep `wiki/index.md` complete. When a page is created, renamed, split, or removed, update its entry under the right area with a one-line description.

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

## Feedback Notes

People pages may carry a `## Feedback Notes` section: observed behaviour Brian could give as feedback, written as a neutral third-party observer. Add to it during ingest when a source shows a concrete behaviour (what they did, its effect), never personality labels or hearsay presented as fact.

- Optional first line: `- **Headline**: one observer's line on the person, kind and specific.`
- One line per observation: `- **Strength** (YYYY-MM-DD): what happened and its effect. \`sources/...\``
- Growth items end with a concrete ask: `- **Growth** (YYYY-MM-DD): pattern with dated examples. Ask: one specific change. \`sources/...\``
- On `brian-peralta.md`, feedback Brian received uses `**Received strength**` / `**Received growth**` and names who gave it.
- Mark secondhand or unconfirmed items `UNCERTAIN:`. Replace an item when newer evidence supersedes it; this section is not append-only.
- The Feedback Ledger artifact renders these sections; keep the line format stable.
