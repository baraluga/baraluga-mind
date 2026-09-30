# Sprint Backlog Grooming

- Source: Granola
- Meeting ID: `675265db-d6c3-49c7-85ee-2f645122bec9`
- Date: 2026-09-30 15:30 Asia/Manila
- URL: https://notes.granola.ai/d/675265db-d6c3-49c7-85ee-2f645122bec9
- Captured by: Brian Alexander Peralta

## Summary

### Darwin Integration

- Meeting with Matteo planned (in ~3 hours at time of call) to discuss next steps on Darwin connection
- Almost at the finish line on Darwin connectivity; goal is to iron out remaining items with Matteo
- Tickets to be created once Matteo meeting concludes

### TSDB Time Series and Observability Backlog

- Question raised on insertion date vs. publication date for time series in the real-time N-minute DAG (ticket 1265)
  - Context from Guillaume Fontaine: trading desk in Belgium complained about TSDB insert wait times
  - Feedback promised by end of week (Monday)
- UAT injection bug (CDH and TSDB): fix pending support response, then revert to proper environment practices instead of targeting prod directly
- Observability stack (ticket 1254): agreed to split into user/pain-point-driven subtasks rather than copying Synapse's stack wholesale
  - Subtask 1: monitor Airflow CPU pressure
  - Subtask 2: monitor Airflow memory pressure
  - Subtask 3: investigate Grafana dashboard access errors (ref. Matteo's reported failures)
- Grafana usage monitoring: start with Okta connection logs as minimum-effort first step
  - If only 1-2 people are connecting, no need to go deeper
  - Deeper tracking (dashboard edits, zoom/refresh activity) may be limited by open-source Grafana version
  - Definition of done: report rough user behavior (avg. connections, editing activity)

### Grafana Geo-Map Feature (India Clearing Zones)

- Goal: display India clearing zones on a Grafana map, colored by time series values (heatmap style)
  - 3 sets of time series from Matteo, each driving a separate map
  - Merge condition: region name (N1, N2, N3, etc.)
- Two approaches under evaluation:
  - Plotly: working prototype exists; needs review for code quality and connection to correct time series
  - Grafana geomap (native): dynamic GeoJSON coloring not confirmed available; may be version-limited or require activation
- Key open point: color scale must be anchored to fixed bounds, not autoscaled per snapshot
  - Otherwise colors shift meaning day to day
  - Need to define min/max thresholds with Matteo
- Fallback to Plotly if native Grafana feature is unavailable or too costly to implement
- Grafana alerts to Teams: small ticket to be created and prioritized

### Next Steps

- **Clarify insertion date vs. publication date for TSDB time series** (Brian)

  Feedback due Monday (5th October); context from Guillaume Fontaine's trading desk complaint.
- **Check Okta connection logs for Grafana usage** (Brian)

  Minimum-effort first step; report rough user behavior (who connects, how often).
- **Assess Grafana native geomap vs. Plotly for India clearing zone map** (Brian)

  Check if dynamic GeoJSON coloring is available in current Grafana version; fall back to Plotly if not.
- **Review Plotly prototype with critical eye** (Brian)

  Connect correct time series per region and validate region naming with Matteo.
- **Clarify color scale bounds and thresholds with Matteo**

  Fixed min/max needed so heatmap colors remain consistent over time.
- **Create Darwin-related tickets after Matteo meeting**

  Ping Brian once created so they can be prioritized correctly.

Last Updated: 2026-10-01
