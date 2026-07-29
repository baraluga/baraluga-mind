# Declic Sharing

Source type: Granola meeting notes
Meeting ID: `7715f598-f100-4a49-9d7c-3b72bbd3f1f4`
Meeting date/time: Jul 28, 2026 10:50 AM GMT+8

## Known Participants

- Brian Alexander Peralta (note creator) from Icloud <ba.peralta@icloud.com>

## Capture Note

These are Granola meeting notes/summaries, not a verbatim transcript.

## Discussion Notes / Summary

### CI/CD Pipeline Architecture

- Discussion centered on migrating/converting pipeline to GitHub Actions.
- Reusable workflow pattern identified as the target approach.
- Custom orchestrator agent proposed as the abstraction layer.
- Goal: standardized, publishable, granular actions package.

### AWS and Credentials Setup

- AWS resources and credential rows under review.
- IAM role as the underlying base for environment access.
- Credentials for CDH to be manually screened via GitHub.
- Environment variables, including deployment environment, need verification.

### Declic Sharing and Dependencies

- Library dependency calculator referenced as part of the pipeline.
- Services discussed: notification, MS client, service desk client, user MS client, web common, calculator, image service lambda, SQL checker.
- Currency backend also sent for review.

## Next Steps / Action Items Present in Granola

- Verify credentials and environment variables in pipeline.
  - Confirm IAM role, CDH credentials, and deployment environment variables are correctly configured in GitHub.
- Define reusable workflow pattern for GitHub Actions migration.
  - Standardize as a publishable, granular actions package using the custom orchestrator agent.

Last Updated: 2026-07-28
