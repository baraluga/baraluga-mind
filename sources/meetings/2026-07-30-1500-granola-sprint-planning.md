# Sprint Planning

Source type: Granola meeting notes
Meeting ID: `6c4f38ea-4935-4380-ac90-f794394a12bc`
Meeting date/time: Jul 30, 2026 3:00 PM GMT+8
Known participants:

- Brian Alexander Peralta (note creator) from Icloud <ba.peralta@icloud.com>

Note: This capture preserves Granola-provided notes and summaries. It is not a verbatim transcript.

## Summary

### Sprint 25 Closeout

- Sprint 25 closed; all remaining effort set to zero, carried-over tickets treated as formalities.
- Tickets needing validation: 1206, FIL-07, 1208, 1058.
  - Mate to lead validation; has questions on the process, call scheduled post-planning.
  - Tickets currently assigned to Brian and Bong for unclear reasons.

### Sprint 26 Commitments

- Brian and Michael committing 9 points across 4 stories + 1 bug.
- Key stories:
  - **1216**: Activation of automatic email report disabling for specific tags (1 pt); already in progress, bug found during QA testing.
  - **Backfilling 35 time series** from last sprint for operational capacity (already in UAT, pending prod approval).
  - **India spike (1209-related)**: Prove cross-account S3 access from a different region/project/dataset; result determines fate of 1209 (CSV parsing, DAG setup, TSDB publish).
  - **Critical bug**: Weekly interconnector capacity failing on all environments including prod; daily granularity fine, weekly not; 1-2 pts estimated.

### TSDB Strategy and Japan Data

- Decision: hold off on backfilling operational capacity time series until Japan data scope is confirmed.
  - Agreed that TSDB changes should be owned by the TSDB admins (they design, provide IDs; team implements).
  - Louis initiated the discussion; working closely with Carlos, who should be looped in.
  - Alex from their team already requesting creation of a big provider tool, suggesting movement on their side.
- Prod push for the 35 backfilled time series:
  - Awaiting approval from Sandrine and Alexander Hinen (metadata admins).
  - Laurent to approve the 35 time series changes once cleared.
  - All steps (backfill + push) captured under ticket 2017.

### India Integration Spike

- CTH dataset: one CSV file per day in S3, updated every 15 minutes (overrides same file).
- Goal: ingest every 15 min and push to TSDB; 4 time series identified by Mateo (one per needed column).
- Cross-account S3 access: requires configuring trust relationship for cross-account role; Michael confirmed feasible.
- Scheduling the DAG:
  - Coordinate with Mateo on exact file push timing; add a small offset (not 5 min, check S3 logs empirically).
  - Avoid over-engineering with S3 event listeners; keep it simple.
  - Build in a backfill mechanism to target specific files/time slots in case of data gaps or provider errors.

### Budget and Period End

- Sprint 26 is the 4th (final committed) sprint of the current period; agreement ends late August.
- Steering committee moved beyond the period end, leaving about 2 weeks uncovered.
- Plan: request time-and-material coverage for those 2 weeks (minimal effort, Brian only).
  - Email to Mateo and Euro Mission to confirm T&M continuation.
  - Reinforce in Sprint Review that remaining items still exist.
  - Note in the email that the budget has already been exceeded (as declared in yesterday's Sprint Review).

## Next Steps

- **Validate carried-over tickets 1206, FIL-07, 1208, 1058** (Mate)

  Mate to take the lead; call with Brian post-planning to clarify the process.

- **Reach out to Sandrine and Alexander Hinen for TSDB prod approval** (Brian)

  Approval unblocks Laurent's sign-off and the backfill push under ticket 2017.

- **Coordinate with Mateo on S3 file push timing** (Brian)

  Check S3 logs empirically to determine reliable offset before scheduling the DAG.

- **Send T&M extension request email to Mateo and Euro Mission**

  Cover the 2 weeks post-period; note budget already exceeded and remaining backlog items.

- **Work with Louis on TSDB data catalog**

  Louis and the dashboard team to identify and document all required time series with correct metadata before next sprint.

Last Updated: 2026-07-30
