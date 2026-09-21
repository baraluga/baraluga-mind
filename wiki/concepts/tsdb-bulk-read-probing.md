# TSDB Bulk Read Probing

## Standing preference

Brian explicitly requested on September 21, 2026: **always prefer bulk reads for TSDB value probing and audits**. Applies across SMP India, Japan, and other TSDB work; see [[smp-platform]] and [[apac-tsdb-scraper]].

- Pass all relevant series IDs together to the supported SDK read function. Avoid nested network calls per series per day; split and summarize the returned data locally.
- Bound the date range in sensible chunks. Seven-day chunks worked for the five-series KHABA minute audit; tune chunk size to row limits, revisions, memory, and backend constraints.
- Use the documented working storage access path. For KHABA on SDK 0.49.2, direct Athena reads avoided repeatedly failing API-only latest-value requests. Recheck SDK version/capabilities for other environments instead of assuming Athena is always necessary.
- Let the SDK handle query batching/parallelization; do not add a ThreadPool by default.
- Preserve correctness: partition latest-version selection by both series and application timestamp; use the correct revision axis; check truncation before collapsing versions; retain timezone-aware day boundaries; distinguish query errors from missing data.
- Show batch progress and elapsed time, and save completed results incrementally.

## Evidence

The five-series, 43-day KHABA audit completed in seven SDK calls, with approximately **53.5 seconds total query time** in Brian's supplied run. This is observed evidence, not a universal latency guarantee. Earlier serial day/series probing was slow enough that Brian aborted it.

## Sources

- `sources/notes/2026-09-21-tsdb-bulk-read-preference.md`
- [TSDB data-read and parallel-load guidance](https://pages.github.tools.digital.engie.com/Tsdb/engie-tsdb/data_read.html#parallel-load)

Last Updated: 2026-09-21
