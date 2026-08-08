# SMP TSDB Explorer

## Summary

The SMP TSDB Explorer is a local-only, read-only diagnostic tool created on 2026-08-07 to inspect SMP TSDB series across UAT and production without changing TSDB data.

The V1 implementation lives at `/Users/qn5792/repos/smp/smp-tsdb-explorer` as a standalone sibling project. It was intentionally kept local: no remote repository, commit, push, deployment, hosting, or publication was authorized in the captured session.

## Details

- The tool combines a React diagnostic frontend with a FastAPI backend.
- It uses a static 49-series OCCTO preset, plus a legacy 35-series shortcut.
- Query behavior is read-only by construction: it imports reader/configuration paths only, isolates each TSDB query in a subprocess, runs one active query at a time, and supports cancellation, timeout, temporary result expiry, partial failures, gap detection, and coverage diagnostics.
- Frontend package management was switched from npm to `pnpm@10.14.0` after the initial implementation.
- Offline validation passed in the captured session: backend tests, frontend tests, lint/typecheck, production build, fake-gateway behavior, secret audit, write-capability audit, and sibling-repository no-change check.
- Live UAT/prod acceptance was not completed because TSDB credentials were unavailable. Fresh dependency synchronization also required ENGIE Artifactory connectivity.

## Open Questions

- UNCERTAIN: Whether live UAT/prod acceptance has since been run with valid local TSDB credentials and Artifactory connectivity.
- UNCERTAIN: Whether this should remain a private local utility or later become an ENGIE-hosted read-only gateway with hosted secrets.

## Sources

- `sources/codex-conversations/2026-08-07-codex-conversations.txt`

Last Updated: 2026-08-08
