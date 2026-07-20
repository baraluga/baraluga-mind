# TA Standup

Source type: Granola meeting notes

Meeting ID: `de3b871a-e8e6-413b-b2dd-6ddf3234d393`

Meeting date/time: 2026-07-20 16:45 GMT+8

Known participants:

- Brian Alexander Peralta (note creator) from Icloud <ba.peralta@icloud.com>

Note: This capture preserves the available Granola notes/summary. It is not a verbatim transcript.

## Discussion Notes

### Billing Issue (Hourly vs. Fixed)

- Customer wants to switch from hourly to fixed monthly/yearly billing.
- Bill page will show hourly amount minus savings, then total.
- Underlying engine still charges for subscription/savings plan at engine level.
- Root cause: accidental run of 1,000 instances for 6 days, not a billing system bug.
- Reply sent to ticket already; team to follow up with correct explanation.

### Pyrine Deployment

- Resumed debugging issues flagged by Nicola last week.
- Most issues tied to File Manager, which was deployed separately from Pyrine and is not yet integrated.
- Coordinating with Abraham on integration; info received, deployment update pending.
- Failing run reported on Abraham's side; unclear if related to deployment or expected behavior.
- Need to confirm with Abraham whether Pyrine runs are functional end-to-end.

### Model Runner Migration

- Updated ADO pipeline: Harbor not compatible with ADO, so images now pushed to MS accounts.
- Created additional pipeline to promote images between MS accounts, including dev to prod and hotfix flows.
- Previously all images pushed to a single ECR repo; new multi-repo process adds flexibility.
- Documentation task pending: how the new pipeline works, so team can use it properly.
- Migration status:
  - Alfred already migrated EFS; images migrated.
  - Database and file migration to happen when users cut over to prod.
  - At cutover: scale up cluster instances, not a redeploy.
- Pyrine pipelines being updated to match Model Runner setup; still in progress.

### Prosumer Data Migration

- David informed: data migration proceeds tomorrow.
- Permissions prep underway today:
  - Requested additional S3 buckets added to Azure admin role.
  - Buckets exist in both old Prosumer prod and DMS prod accounts.
  - Role needs read/list (`s3:GetObject`, `s3:ListBucket`) permissions on both.
- ABAC note: S3 buckets need cost center tags enabled for tag-based access control.
- Cross-account access: same role used, buckets added; existing access pattern already in place.
- Script created today: will reset/delete items in prod account before restoring data.
  - Using `s3 sync` with `--delete` flag to remove test-period additions.

### Wallet Migration (Brian)

- Migration going smoothly, no blockers.
- Three new repositories migrated for SFF:
  - `user-ms-client`
  - `user-microservice`
  - `web-colon`
- Naming convention cleanup:
  - Some repos were labeled with "tool" prefix, e.g. `SFF-tool-*`, but were not tools.
  - Pankaj created an Excel file with proposed naming convention based on README review.
  - Brian to review Excel file and flag any names that seem off.

## Next Steps

- Follow up on billing ticket with corrected explanation.
  - Clarify the 1,000-instance accidental run was a manual error, not a billing system issue.
- Update Pyrine deployment to integrate File Manager (Brian).
  - Info received from Abraham; apply integration and confirm runs are functional.
- Add S3 buckets to AWS role and enable ABAC tags.
  - Buckets in old Prosumer prod and DMS prod need cost center tags and cross-account read/list access before tomorrow's migration.
- Review Pankaj's naming convention Excel file (Brian).
  - Check proposed repo names against the SFF naming convention and flag any that look incorrect.
- Confirm Model Runner migration cutover date with Nick.
  - Identify when users stop using the old instance; database and file migration plus cluster scale-up happen at that point.

Last Updated: 2026-07-20
