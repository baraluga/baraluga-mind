# YNAB Web App

## Current State

As of 2026-10-13, the only durable local evidence is a 2026-10-12 read-only Claude/REA-style exploration of Brian's logged-in YNAB web session. The investigation did not modify the budget except for Brian's own test memo edit, and it did not capture request bodies.

The useful takeaway is that YNAB's web app can be investigated from public static assets and browser-observed network traffic, but full REA runtime tracing needs a Chrome instance launched with a DevTools debugging port. The Codex in-app browser is useful for script and network inspection, but it cannot act as a REA browser target and did not expose upload payloads.

## Background

YNAB's web UI appeared to use Ember.js plus webpack-built assets. The observed app had Rails webpack files under `/assets/packs/js/` and larger Ember app chunks under `/assets/ynab_web/`. Source maps were not public in the checked session.

The sync path centered on an Ember `sync-control` service that delegates to `applicationService.syncManager` and a shared library. The observed and static evidence pointed to `POST /api/v1/catalog` as the main sync endpoint for catalog, family, and budget data, with operations such as `syncBudgetData`, `syncCatalogData`, and `syncFamilyData`.

Budget syncs used change counters: the browser's counter and the server's budget counter advanced when Brian edited a transaction memo. The server confirmed the edit with budget counter movement from 414 to 415, then another budget sync moved 415 to 416. Because the tool could not read request bodies, the exact uploaded `changed_entities` payload remains inferred rather than directly observed.

The live page's configuration reported an automatic sync rate of 180,000 milliseconds, interpreted as three minutes. A timed idle sync was not conclusively observed because page navigation and the memo edit also triggered syncs.

## Open Questions

- UNCERTAIN: Whether YNAB's web and mobile clients share the same compiled data-layer library; the source looked like shared TypeScript/Kotlin-derived code, but this was not confirmed.
- UNCERTAIN: Why two transfer payees came back in the server response after a memo edit; the source did not identify a reason.
- UNCERTAIN: Whether the three-minute timer fires independently during a quiet idle period; the observed traffic did not isolate it.

## Sources

- `sources/claude-conversations/2026-10-12-claude-scratch-3c479f77.txt`

Last Updated: 2026-10-13
