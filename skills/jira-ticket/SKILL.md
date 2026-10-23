---
name: jira-ticket
description: Write, rewrite, or refine Jira (or other tracker) tickets in Brian's concise, AI-first format — user stories, technical tasks, and bug reports. Use for any ticket or backlog-item authoring, including turning rough notes or user reports into tickets and follow-up edits. Do not trigger for implementing or debugging the work itself, or for general explanations of agile/BDD.
---

# Jira Ticket

Write tickets that an AI agent can act on without guessing, and that a human can skim in seconds. Extremely concise, but sufficient: every line either removes ambiguity or gets cut. Follow explicit user or project templates when they differ.

This skill sets structure only. Apply `brian-voice` for tone. Where the ticket goes (Jira, markdown, elsewhere) is the calling session's job.

## Pick the type

- **Story**: a user-facing outcome with a real actor and benefit.
- **Task**: technical or internal work (refactor, infra, upgrade, spike, chore). Never force a fake persona onto it.
- **Bug**: existing behavior that differs from what's expected.

One ticket = one coherent outcome. If the request holds several, say so and propose a split; don't create extra tickets unless asked.

## Templates

Summary, plus the core sections, are required. Include optional sections only when they carry information; never write empty headings or "N/A".

### Story

```markdown
Summary: <user goal, action-first>

As a <specific role>, I want <capability>, so that <real benefit>.

Context: <optional — 1–2 lines on the current problem or why now>

Acceptance criteria
- <observable rule>
- <boundary / failure / permission case>

<optional Given/When/Then scenarios — see below>

Out of scope
- <plausible adjacent work that must not be done>

Open questions
- <unresolved decision that affects behavior>
```

### Task

```markdown
Summary: <verb> <thing>

Why: <1–2 lines: the problem or what this unblocks>

Done when
- <observable, verifiable outcome>

Constraints: <optional — must-keep behavior, compatibility, deadlines>

Out of scope
- ...

Open questions
- ...
```

### Bug

```markdown
Summary: <component> fails to <behavior> when <condition>

Reproduce
1. <starting state>
2. <triggering action>

Expected: <one sentence>
Actual: <one sentence, exact error or values if known>

Evidence: <optional — screenshot, exact error, log/run link>
Impact: <optional — who/how often, only if known>
```

Bugs skip personas and acceptance criteria by default; Expected is the verification target. Add criteria only if the fix must also guarantee extra behavior.

## Rules (AI-first)

- **Testable over descriptive.** Each criterion has an objective pass/fail. Replace adjectives with values: "fast" → "under 2s", "secure" → the specific rule.
- **State edge and failure cases explicitly.** Those are exactly what an agent will otherwise fill with plausible guesses. Cover them in proportion to the feature; no fixed quota.
- **Name what not to do.** Add Out of scope whenever an eager implementer could reasonably over-reach.
- **Behavior, not implementation.** No file paths, code design, selectors, or DB details unless they are the contract itself. Technical notes go in ticket comments, outside this skill.
- **Never invent.** Don't make up rules, limits, permissions, repro steps, or root causes. Ask about material gaps while drafting what's known, or list them under Open questions. Label proposals as proposals, never as agreed criteria. Mark unconfirmed repro and suspected causes as unverified.
- **No duplication.** Don't restate the story in the criteria or the Summary in the body. Keep Definition of Done items out unless the project requires them in tickets.
- **Editing an existing ticket:** read it first and keep its relevant decisions and references.

## Given/When/Then

Default to plain bullet criteria. Add scenarios only when branching, state, permissions, or calculations need a concrete example, and keep the general rule alongside them. One trigger per scenario, named by the behavior, concrete values that illustrate rather than add requirements. Use an outline or table when only data varies.

```gherkin
Scenario: Expired reset link
  Given my reset link is older than 30 minutes
  When I open it
  Then I see "This link has expired" with an option to request a new one
```

## Final check

Could an agent implement and verify this without asking anything the ticket could have answered? Are unknowns visible? Is every remaining line necessary? Cut what isn't.
