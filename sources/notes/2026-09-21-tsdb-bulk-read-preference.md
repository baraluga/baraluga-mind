# TSDB probing preference — Brian, September 21, 2026

Brian explicitly requested persistent memory after the KHABA audit completed:

> Please, keep this in memory when doing any probing in TSDB values. Always prefer bulk read, or whatever it is that you did!

The provided terminal output showed seven batches covering August 5–September 16, 2026, across five one-minute KHABA series. Batch read durations were 9.9, 6.0, 8.0, 8.0, 8.0, 8.1, and 5.5 seconds (53.5 seconds summed read time, excluding local reporting overhead).

Implementation: `smp-india/scripts/audit_khaba_minute_tsdb.py` called `engie_tsdb.data.read_ts` with all five series IDs, seven-day date chunks, `read_data_methods=["athena"]`, and a bounded row limit. Latest publication was selected independently by series ID and application timestamp; daily IST coverage was calculated locally.

The prior approach issued one query per series per day (215 queries for 43 days), plus API-only latest-version attempts that failed. SDK 0.49.2 forced API-only latest-version access; the published documentation describes broader support from 0.50.0. This version detail is contextual, not a permanent requirement to use Athena for every series.

Evidence: user-provided terminal output `/Users/qn5792/.codex/attachments/cbc03a9d-2912-44f5-aa89-a6742768e69a/pasted-text.txt` and direct request in the SMP conversation.

Last Updated: 2026-09-21
