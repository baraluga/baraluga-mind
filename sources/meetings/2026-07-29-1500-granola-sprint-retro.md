# Sprint Retro

Source type: Granola meeting notes

Meeting ID: `9293458e-7921-41ad-893a-7c7f2416664f`

Meeting date/time: Jul 29, 2026 3:00 PM GMT+8

Known participants:

- Brian Alexander Peralta (note creator) from Icloud <ba.peralta@icloud.com>

Note: This capture preserves Granola-provided meeting notes and summaries. It is not a verbatim transcript.

## Discussion Notes / Summary

### Sprint Retrospective and Budget Status

- Sprint 3 (Period 2, Sprint 25 in rolling count) reviewed.
- Budget: 39,000 total; around 98% consumed this sprint.
- Two out-of-scope items identified:
  - Lookback function added to Japan dashboards (new scope).
  - Darwin scrapper troubleshooting for India (minor effort).
- Projected 15% overshoot, around 5,900 EUR, to finish the full phase.
- Options discussed for Brian's allocation:
  1. Keep full capacity: 15% overshoot.
  2. Stop work: no Sprint 4.
  3. Half capacity: around 7% overshoot.
- Decision: push full-time through end of August, present overshoot as driven by additional scope; reduce capacity only if client rejects.

### Sprint Goals and Burndown

- TSDB interconnector data upload: done, confirmed via local script fetching time series.
  - Validated data matches expectations; accessible through Grafana.
  - Debate on whether operational capacity should be included: not yet confirmed with Carlos or Laurent.
- TSDB catalog in Octo: marked done; scope change (nominal vs. operational capacity) noted.
- Lookback functionality added to three dashboards in one sprint: standardized pattern established.
  - Japan tickets set to "done" with user acceptance confirmed.
  - India comparison: Material handled TSDB approval internally, likely an owner/approver, making it far smoother.
- Japan TSDB path required briefing Carlos and Laurent from scratch; they had little awareness of the plan.
  - Brian flagged this as a significant source of red tape vs. the India experience.

### Retro Themes and Next Steps

- What went well: TSDB data upload finally complete; lookback dashboards delivered and accepted.
- Bloopers / friction:
  - Low visibility on incoming tasks; Louis flagged his data need the day before sprint end.
  - Japan TSDB approval process far more manual than India; Carlos needs to be looped in earlier.
  - Concern raised: too much effort spent solving problems not yet confirmed as problems.
- Stop doing: proactive scope-finding when budget is constrained; better to be reactive until pain points are explicit.
- Jupyter notebook vs. Git-based contribution: original assumption was non-technical users; advanced users (Carlos, Singapore) now want more control.
  - No implementation yet; decision deferred to next steering committee with user feedback.
- Louis's data access: grant Grafana dashboard access (free); point to existing SharePoint folder; TSDB push or direct parquet connector to be discussed in tomorrow's review.
- UK and Iberia follow-up: Bastian confirmed contact with Iberia next week to check for further questions.

## Next Steps / Action Items Present in Granola

- Discuss Louis's data access and TSDB push decision in sprint review: determine whether to push data to TSDB or set up direct parquet connector; present budget overshoot as scope-driven.
- Confirm Brian's capacity allocation after tomorrow's planning session: full-time through August is the current plan; adjust if planning reveals otherwise.
- Contact Iberia next week to follow up on UK and Iberia meetings: Bastian confirmed this is the right next move; check for further questions or interest in SMP.

Last Updated: 2026-07-29
