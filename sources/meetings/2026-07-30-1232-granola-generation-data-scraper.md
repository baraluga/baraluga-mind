# Generation Data Scraper

Source type: Granola meeting notes
Meeting ID: `25fd75cc-b7cc-4dfa-a07a-14ba38da5c3e`
Meeting date/time: Jul 30, 2026 12:32 PM GMT+8
Known participants:

- Brian Alexander Peralta (note creator) from Icloud <ba.peralta@icloud.com>

Note: This capture preserves Granola-provided notes and summaries. It is not a verbatim transcript.

## Private Notes

- File is being dumped in CDH S3.
- Every 15 minutes.
- We need access to this CDH dataset where the S3 bucket is bound to.
- What fields do we need?
  - Mateo will provide.
- Average the value for every 15 minute block.
- S3 is on a different region - what is the implication?
- Is the SMP AWS account used for S3 management tied to a specific region?

## Summary

### Data Source: CDH Generation File

- File dumped into CDH S3 bucket once per day, overwritten every 15 minutes with new data.
- Source: SFTP from asset server, pushing updates every 15 minutes.
- End-of-day file size: about 2.1 MB for the asset (Cabo generation).
- Overwrite model is convenient: missing data is recovered by the next update.

### Fields Required

- Active power (primary).
- Two topology values.
- GHI (Global Horizontal Irradiance).
- Ambient temperature (nice to have).
- Mateo to provide full list with time series IDs and names once TSDB entries are created.

### Aggregation Logic

- Only one value per 15-minute block needed in TSDB.
- Average all readings within each block:
  - 00:00 to 00:14
  - 00:15 to 00:29
  - 00:30 to 00:44, etc.
- This matches what Benny Khan's process already does.

### Access and Region

- S3 bucket is in Asia Pacific region (different from expected).
  - Implication unclear: need to confirm whether the SMP AWS account used for S3 management is tied to a specific region.
- CDH dataset: "Cabo Generation" (capital C, capital G, the larger one).
- Access group: EMI Analyst (prod).
  - Mateo added Brian to the group during the call.
  - Brian confirmed Cabo Generation is now visible in CDH.
- Next step: confirm console access and identify the correct project ID (likely India prod, but unconfirmed).
- CDH support may need to be contacted to clarify dataset/bucket binding.

## Open Questions

- What is the implication of the S3 bucket being in a different Asia Pacific region?
- Is the SMP AWS account for S3 management tied to a specific region?
- Correct project ID in CDH still needs to be confirmed.

## Next Steps

- **Get CDH project ID, data source, and dataset details from Mateo**

  Needed to configure the SMP connection to the Cabo Generation dataset in CDH.

- **Confirm console access to Cabo Generation dataset**

  Brian was added to the EMI Analyst prod group; verify access is active.

- **Clarify region implications for S3 bucket (Asia Pacific)**

  Check whether the SMP AWS account is region-locked and what that means for connectivity.

- **Create TSDB entries and share time series IDs (Mateo)**

  Mateo to send IDs and field names today or tomorrow at the latest.

Last Updated: 2026-07-30
