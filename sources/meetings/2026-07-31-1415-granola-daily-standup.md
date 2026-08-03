# Daily Standup

Source Type: Granola meeting notes

Meeting ID: `243f9bed-4bde-4c2e-b5e2-3a30e1ebbad0`

Meeting Date/Time: Jul 31, 2026 2:15 PM GMT+8

Known Participants:

- Brian Alexander Peralta (note creator) from Icloud <ba.peralta@icloud.com>

Note: This capture preserves the available Granola-generated meeting notes and summary. It is not a verbatim transcript.

## Discussion Notes / Summary

### Ticket Status Updates

- Ticket 417: Carlos confirmed backfill to calendar year 2021
  - Capacity: available capacity first, then operational capacity for actual flow
  - FY2024+ data would come from Bloomberg (different TSDB setup)
  - Carlos opted to keep it simple with Octo
  - Actual flow fine if limited to FY2025 (Octo's current scope)
  - Flag removed; work starting once 1219 and 1216 are finalized
- Ticket 1219: ready for validation pending weekly capacity runs
  - No failures or errors on QA and prod required
  - Earlier QA prod runs checked and green (screenshot attached)
- Ticket 1216 (HJKS orchestrator DAG): monitored this morning and afternoon
  - Most recent run ~1 hour ago; no emails sent as expected
  - Email suppression scoped to specific types only: 2Y by region, bid stack, nuclear, energy availability analysis
  - Francois confirmed receiving mail at ~4:33 (3 hours prior); expects clean run by 10:00

### Ticket 1218 Spike (S3 Access)

- In progress alongside Michael
- Goal: verify cross-region S3 bucket access without additional changes
  - Bucket is on a different region but same premises
  - If access confirmed, no further action needed
  - If not, will pursue offline access request
- Michael handling git sync for the region across environments

### Budget and Steering Committee Prep

- Francois sent budget request to Adrian and Louis/Carlos
  - 15% increase for current sprint
  - Time-and-materials provision between mid-August and first steering committee
- Data type 3 inventory flagged to Adrian, Louis, and Carlos
  - Team offered to help bridge data gaps (provider details, frequency not visible from dashboard)
- Steering committee prep meeting scheduled today with Bong
  - Brought forward due to Fred's upcoming holiday and Francois's holiday last week of August

### Access and Housekeeping

- Michael granted access to Gird; team to flag any other projects needing access
- Call time discrepancy noted across devices (watches, laptop, cell phone showing different times)

## Next Steps / Action Items From Granola

- Finalize tickets 1219 and 1216, then set both to validation.
  - 1219 is straightforward once weekly capacity runs clean on all environments; 1216 pending confirmed email suppression by 10:00.
- Confirm S3 cross-region access for ticket 1218.
  - If access is confirmed without changes, spike is done; otherwise submit offline access request.
- Document data type 3 inventory gaps for Adrian, Louis, and Carlos.
  - Help bridge provider and frequency details not visible from the dashboard.

Last Updated: 2026-07-31
