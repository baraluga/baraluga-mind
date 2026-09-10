# SMP Sprint Review

## Metadata

- Source: Granola
- Meeting ID: `5701c771-107d-4b41-a9d3-0fa243b946b4`
- Date: 2026-09-09 16:30 GMT+8
- Captured by: Brian Alexander Peralta
- Known participants:
  - Brian Alexander Peralta (note creator) from Icloud <ba.peralta@icloud.com>

## Summary

### Sprint 1 Overview: Period 3, Sep 1-9

- Brian presented the sprint review for Period 3, Sprint 1.
- Focus areas: S&P India, S&P Japan, and S&P Common platform.
- Several team members were absent: Carl on leave, Lou and India side participants Mateo and Francois uncertain.

### S&P India Deliverables

- IEX bid stack data implementation is underway.
- Kava generation dashboard improved.
  - Added day-ahead and intraday forecast alongside actual generation.
- Price history expanded across all three markets: day-ahead, G-DAM, and real-time.
  - Previously: rolling 30-90 day window.
  - Now: two-year coverage from Oct 2025 to date.
- Belarial contracts data was scraped and validated by Francois, and is now in CDH.
  - Next step pending: decide whether to create a new dashboard or push to TSDB.

### S&P Japan Deliverables

- TSDB production publishing finalized for interconnector time series.
  - Available capacity for all IC regions, operational capacity, actual flow, and JPX prices.
  - Historical data from 2021 to date confirmed available.
  - Provider: interconnector, owned by Carlos and Lona.
- Interconnector data for FY27 updated and reflected in the dashboard promptly.
  - Goal: reduce manual weekend data-gathering for Yuromishan.

### S&P Common: Airflow Assets Feature

- Explored Airflow Assets as an event-based DAG triggering mechanism.
  - Replaces arbitrary scheduling, such as noon, 1 PM, and 2 PM offsets, with asset-based triggers.
  - DAGs wait for upstream assets to be produced before running.
- High relevance for S&P Japan: HGKS scrapers all consume the same base data.
  - Nuclear by region, two-year and three-month datasets.
  - Pattern allows isolated scrapers to wait on a shared HGKS asset.
- Benefit: improved maintainability and robustness. This is not visible to stakeholders but reduces operational risk.

### Budget Update: Period 3

- Total budget: EUR 45,000, reduced from EUR 48,000 due to limited Japan scope.
- Distribution: Japan 10%, India 70%, Common 20%, with Common split equally between Japan and India.
- Consumed so far: about 20%, around EUR 9,000.
  - Japan: about EUR 1,800.
  - India: about EUR 7,500.
  - Covers support period from Aug 13-31 and Sprint 1 from Sep 1-9.
- Japan's 10% share was not strictly respected due to maintenance support weighting.

### Next Steps

- Confirm next steps for Belarial contracts data.
  - Data is in CDH and validated; decision needed on whether to build a new dashboard or push to TSDB.
- Evaluate Airflow Assets adoption across S&P Japan DAGs.
  - HGKS scraper pattern is a strong candidate; recommend to stakeholders if use cases are confirmed.

Last Updated: 2026-09-10
