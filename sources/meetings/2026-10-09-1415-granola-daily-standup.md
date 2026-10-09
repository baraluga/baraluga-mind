# Granola Capture: Daily Standup

Source Type: meeting
Source: Granola
Meeting Date: 2026-10-09 14:15 GMT+8
Meeting URL: https://notes.granola.ai/d/a17c2c46-2729-4161-9c65-294ab81f4905
Granola ID: a17c2c46-2729-4161-9c65-294ab81f4905

## Known Participants

- Brian Alexander Peralta (note creator) from Icloud <ba.peralta@icloud.com>

## Summary

### Sprint Blockers and Open Tickets

- Darwin API follow-up: no response from IT despite confirming the base URI is correct with the Darwin team.
- Adrian still has not created the needed resource; he will be bumped again.
- Bilateral contracts tickets: no meaningful feedback received, so the team agreed to close them.
  - The only feedback was late data delivery, which was not relevant to those tickets.
  - If action is needed later, open a support ticket.

### Sprint Process and Kanban Transition

- Burn rate line looks irregular because of mid-sprint ticket pulls.
  - Tickets are pulled because they are not clear enough at sprint start, or because the team runs out of work.
  - The team is completing work faster than closing tickets, hence the pulls.
- A break between sprints was proposed as a short-term fix, but was flagged as the wrong solution.
  - The problem recurs once the backlog is consumed.
- Kanban transition is seen as the more appropriate long-term fix.
  - Sprint reviews add little value: SMP India already sees changes in production and gives feedback in real time.
  - Reviews mainly serve budget tracking, which could be handled by email.
  - This should be discussed with Bang and Fred next week.

### Data Catalog and Process Documentation

- Ticket 1285 created a `data_catalog` file documenting all enabled DAGs.
  - Coverage includes what each DAG does, run frequency, data source, storage location (CDH or TSDB), time series IDs, and dataset names.
- A GitHub pipeline was added to validate documentation automatically against existing DAGs.
- Documentation is human-and-AI co-written; human familiarity still needs to be maintained.
  - At least one team member should be able to explain the processes to others.
- Aurora scraper lives in a separate repo, so excluding it from the catalog was the correct call.
- Kafka/Kaba collection was confirmed to be inside a DAG, so it is covered.

### IEX Real-Time Data Delay

- Ticket 1284 root cause: two separate scraping processes on different environments create an unavoidable gap.
  - APAC TSDB scraper handles IEX to TSDB outside Airflow control.
  - Airflow DAG handles TSDB to CDH internally.
  - Airflow runs on a fixed schedule with no signal that data has arrived, so data can be missed until the next interval, currently 30 minutes.
- Two proposals are under discussion with Adrian:
  - Decrease DAG and scraper intervals: reduces delay but does not eliminate it; the bottleneck remains.
  - Bypass APAC TSDB scraper for IEX RTM: Airflow writes directly to both TSDB and CDH in parallel, cutting delay to about 5 seconds.
- Option 2 is preferred if Adrian confirms a 2-3 minute delay is acceptable.
- If true real-time is required, scope expands to something closer to the Darwin solution.
- Key constraint: Airflow is schedule-based, not event-driven; it is not built for real-time or near-real-time operation.
  - Expectation management with Adrian's team is needed.
  - TSDB itself is likely not designed for real-time use either; no side-signaling is available.
- Action: gather timing evidence, including mean and standard deviation, for scraping time vs. TSDB injection time vs. CDH push time.
  - Use two sample time series: one from IEX and one from another source.
  - This evidence is needed to justify the TSDB bypass to the TSDB team.

### GDEM Gap Fix

- Ticket 1286 identified and fixed a data gap for October IEX day-ahead market prices (GDEM).
- Fix was pushed to the APAC TSDB Scraper repo with additional scraper optimizations.
- Lou confirmed the fix is working.
- Final review and ticket closure will be handled by the other participant.

## Next Steps Captured In Granola

- Bump Adrian on the pending resource creation, and include bilateral contracts in the follow-up to confirm no outstanding feedback before closing.
- Confirm acceptable delay threshold with Adrian for Ticket 1284. If a 2-3 minute delay is acceptable, proceed with Option 2; otherwise set expectations accordingly.
- Run timing inquiry on TSDB injection and CDH push latency. Measure mean and standard deviation for two time series, one IEX and one other, to justify the TSDB bypass with evidence.
- Discuss Kanban transition with Bang and Fred. Evaluate dropping sprint format in favor of Kanban because sprint reviews currently add little value beyond budget tracking.
- Do final check and close Ticket 1286. Lou confirmed the GDEM gap fix is working; close the ticket after final review.

Last Updated: 2026-10-10
