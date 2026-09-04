# Home Network

## Summary

Brian's home network uses a TP-Link Deco X10 connected behind a Globe Huawei OptiXstar HG8145X6-10 modem/router. On September 4, 2026, a diagnostic session found healthy Wi-Fi and internet latency, so bufferbloat was not the main concern.

The more durable issue is an intermittent afternoon internet drop where the Mac remains associated to Wi-Fi but loses internet access. Bridge mode was prepared and applied on the Globe modem for LAN4, but the transcript ended while verifying whether the modem fully committed the setting.

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

## Open Questions

- UNCERTAIN: Whether the Globe modem fully committed bridge mode after the September 4 change.
- UNCERTAIN: Whether bridge mode affects the 13:00-15:00 intermittent no-internet issue; the transcript suggested it may still be an upstream Globe/WAN issue.

## Sources

- `sources/codex-conversations/2026-09-04-codex-conversations.txt`

Last Updated: 2026-09-05
