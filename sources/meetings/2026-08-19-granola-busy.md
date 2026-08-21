# Granola Capture: Busy

- Date: 2026-08-19 14:15 GMT+8
- Meeting ID: `ad356008-6d3f-4f17-888f-fb5328d44f44`
- Title: Busy
- Participants: Brian Alexander Peralta (note creator) from Icloud <ba.peralta@icloud.com>
- Source: Granola

## Summary

# Bug Investigation: CSV Partial Intervals

- Root cause identified: DAG configured to skip any interval missing at least one minute of data
  - Explains gaps seen on August 14 (incomplete data)
  - Fix is straightforward: tweak DAG logic to handle partial intervals, then rerun reconciliation DAG
- Waiting on Matteo to confirm whether partial intervals are acceptable to process
  - His call on how to proceed

# Airflow Feature Spike

- Goal: explore underused Airflow features proactively
  - Not targeting a specific outcome; building awareness for future requests
- Deliverable: a table with columns for feature name, description, usefulness assessment, and applicable use cases
  - Could also surface refactoring opportunities where a feature should have been used earlier

# Jerome Overview Session (Later Today)

- Brian prepared short slides for the session
- Three-part structure, ~45 minutes total:
  1. SMP overview, business context, and demo
  2. Michael: infrastructure walkthrough (Kubernetes, pods, Airflow, India/Japan coexistence)
  3. Brian: code structure, CI/CD deployment, and interface creation
- Reusing the Iberia/UK presentation done with Bastian as the base
  - Faster-paced version; Jerome likely already familiar with Airflow and sign-ups

# Grooming and Task Sizing (After the Session)

- Will cover what is known from Matteo, with many unknowns still open
- Topics are identified; goal is to surface questions that need answering before tackling each one

# Next Steps

- **Confirm partial interval handling with Matteo**

  Once confirmed, tweak the DAG and rerun the reconciliation DAG to fill August 14 gaps.
- **Finalize slides for Jerome session** (Brian)

  Adapt the Iberia/UK deck to a faster 45-minute format covering code structure and CI/CD.

Last Updated: 2026-08-19
