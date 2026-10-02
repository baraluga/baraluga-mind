# Home Network

## Summary

Brian's home network uses a TP-Link Deco X10 connected behind a Globe Huawei OptiXstar HG8145X6-10 modem/router. On September 4, 2026, a diagnostic session found healthy Wi-Fi and internet latency, so bufferbloat was not the main concern.

The more durable issue is intermittent partial connectivity where the Mac remains associated to Wi-Fi but some internet routes stall. Bridge mode was prepared and applied on the Globe modem for LAN4, but the transcript ended while verifying whether the modem fully committed the setting. A later October 2 incident looked more like an upstream Globe routing/outage problem than a Deco DNS or MTU issue, while the Mac also had stale Microsoft-specific routes after switching Wi-Fi networks.

## Details

- Fast.com measured about 540 Mbps down, 490 Mbps up, 19 ms idle latency, and 48 ms loaded latency. Added latency under load was about 29 ms, which did not indicate severe bufferbloat.
- Direct tests from the Mac showed roughly 3-5 ms to the Deco and 6-8 ms to the internet, with Wi-Fi 6 on 5 GHz/80 MHz, about -56 dBm signal, and an 864 Mbps link rate.
- Before bridge mode, the topology was `Mac -> Deco (192.168.68.1) -> Globe modem/router (192.168.254.254) -> internet`, meaning the Deco was in router mode behind Globe's router.
- The Globe admin page was reachable at `http://192.168.254.254/`.
- The modem model was identified as Huawei OptiXstar HG8145X6-10.
- The internet WAN profile was `1_TR069_INTERNET_R_VID_400`, using IPoE/DHCP with VLAN 400, priority 0, Route WAN, and NAT enabled.
- The separate phone profile was `2_VOIP_R_VID_100` and was intentionally left untouched.
- LAN4 was identified as the likely modem port connected to the Deco.
- Bridge mode was staged with VLAN 400 preserved and only LAN4 selected, then applied after confirmation. Internet returned at about 6-7 ms with no packet loss, but the route still exposed the modem management address, so success was not yet fully confirmed in the transcript.
- On October 2, Brian's setup was still described as `Globe modem -> Deco router`, with Globe modem WLAN normally disabled and a temporary modem SSID `hello-world` re-enabled for isolation.
- During the October 2 slowdown, Google, YouTube, and fast.com stayed quick while Reddit, Microsoft Teams, Microsoft sign-in, and GitHub were slow or timing out. DNS lookups were fast, so changing DNS on the Deco was not expected to fix the issue.
- Testing on the modem SSID versus Deco showed Reddit slower through Deco, but later community reports in Philippine subreddits matched the same Globe symptoms across regions. The capture treated the broader slowdown as likely upstream Globe routing or international-path trouble, not enough evidence for a Deco configuration change.
- After switching back to Deco, the Mac had explicit Microsoft/Teams routes still pointing at the old Globe gateway `192.168.254.254` even though the default gateway was `192.168.68.1` on Deco. Zscaler was running and may have been managing those routes, but the source did not prove what created them.
- A local DNS benchmark on October 2 found Quad9 (`9.9.9.9` / `149.112.112.112`) and Google (`8.8.8.8` / `8.8.4.4`) fastest from the current connection. Quad9 was preferred when malware filtering consistency matters; mixing Quad9 with Google trades filtering consistency for provider diversity.

## Open Questions

- UNCERTAIN: Whether the Globe modem fully committed bridge mode after the September 4 change.
- UNCERTAIN: Whether bridge mode affects the intermittent no-internet issue; the September and October captures both suggest upstream Globe/WAN issues may be involved.
- UNCERTAIN: Whether Zscaler created or merely coexisted with the stale Microsoft-specific routes after Wi-Fi switching.

## Sources

- `sources/codex-conversations/2026-09-04-codex-conversations.txt`
- `sources/codex-conversations/2026-10-02-codex-conversations.txt`

Last Updated: 2026-10-03
