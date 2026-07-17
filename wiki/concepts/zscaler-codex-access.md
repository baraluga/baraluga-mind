# Zscaler Codex Access

## Summary

July 17 diagnostics tested whether Codex could control private corporate websites while Zscaler was connected. The result was mixed: browser access to private Airflow sites worked through Zscaler after the network handoff settled, but fresh Codex/OpenAI requests received 403 responses through the Zscaler path.

The practical conclusion is to avoid reverse-engineering or bypassing Zscaler locally. The clean path is an IT-managed process or destination policy that lets ChatGPT/Codex traffic reach OpenAI while Chrome and private corporate sites continue to use approved Zscaler access.

## Details

- While Zscaler was connected, routing moved through a `utun` interface with a `100.64.0.1` gateway and private Airflow sites loaded to Okta sign-in pages.
- A live Codex thread could temporarily keep exchanging messages because an already-open response stream survived the network transition.
- New Codex requests failed with HTTP 403 through the Zscaler path. The source notes mention `gateway.zscloud.net`, Zscaler challenge parameters, `Server: Zscaler/6.2`, and a Hong Kong Cloudflare edge in the failure path.
- After Zscaler was disconnected, the same official Codex document request returned 200 again and normal Wi-Fi routing resumed.
- Recommended approaches from the diagnostic were an IT-managed ChatGPT/Codex process bypass, approved destination exclusions, split routing, or a managed VM/jump-host test runner. Local static routes were explicitly avoided because they would be brittle and could conflict with corporate policy.

## Open Questions

- UNCERTAIN: Whether IT will approve a process-based bypass for `/Applications/ChatGPT.app`, its bundled `codex` process, or relevant networking helpers.
- UNCERTAIN: Whether a destination allowlist is sufficient, or whether the company requires a managed VM/jump-host pattern for private-site agentic testing.
- UNCERTAIN: Whether the observed Hong Kong Cloudflare edge was caused by Zscaler egress location, policy routing, or transient network state.

## Sources

- `sources/codex-conversations/2026-07-17-codex-conversations.md`

Last Updated: 2026-07-17
