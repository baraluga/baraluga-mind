# Granola: Atlas Checkpoint

Date: 2026-09-17 16:30 GMT+8
Source: Granola
Meeting ID: 99a839d8-c362-4f30-b143-a1a565bbf47c
Captured By: Brian Alexander Peralta <ba.peralta@icloud.com>

## Summary

### CI/CD Deployment Workflow Redesign

- Deployment is now manual and interactive instead of auto-triggering on push to dev or prod.
- It is triggered via the "Run Workflow" button in GitHub Actions, available after DM898 merges to main.
- The workflow prompts for three inputs: target environment (`dev` or `prod`), action (`deploy` or `refresh data`), and data version.
- Merge to main is blocked by current Git conflicts.
- Brian will resolve the conflicts offline and notify once merged.
- Risk is low because the changes are additive only.

### Data Versioning via CDH and S3

- CDH for the Atlas project can upload datasets as "stages," which auto-copy to S3.
- There are two datasets: master upstream and master downstream.
- One stage represents one period, such as one month.
- Re-uploads for the same period should replace prior data rather than stack.
- The pipeline will be updated to point to the CDH Atlas S3 folder and download all stages.
- Latest-file logic should use last-modified date, not folder or file name, to identify current data.
- Historical stages will be retained to support period comparison in the dashboard.
- The PowerShell upload script is no longer needed because CDH handles S3 uploads natively.

### Pipeline Behavior: Data Retention and Fetching

- If no new data is found in S3, the pipeline retains previously downloaded files.
- All CSV stages are downloaded at deploy time, with one CSV per stage.
- A performance concern was flagged for when stage count grows to one or two years of data.
- The group agreed to revisit that later; it is not a current blocker.

### Dash Expert Agent

- A new agent entry was added: "Dash Expert Atlas-Dash Expert."
- It includes Dash-specific instructions.
- It cannot be tested yet because Brian's API credits are exhausted for the month.
- It will be available to test after merge to main.

## Next Steps

- Resolve Git conflicts and merge DM898 to main. Owner: Brian. Notify once merged so deployment testing can begin.
- Update the pipeline to fetch all stages from the CDH Atlas S3 folder. Owner: Brian. Use last-modified date to identify the latest file and download all stages for period comparison.
- Upload latest data stages to CDH. Owner: Principal. Add June 2026 master upstream and downstream before deploying to dev.
- Test dev deployment and Dash Expert agent. Owner: Principal. Do this once Brian confirms the merge is done and the pipeline is updated.
