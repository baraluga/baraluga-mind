# Game Price Tracker

## Summary

Brian wants a master game wishlist and sale-alert tool across Steam Philippines, Nintendo Hong Kong, and PlayStation Indonesia. The captured research found that PSPrices is the closest existing option, but a personal-first custom tracker is buildable if regional price collection and store-product identity are kept deliberately scoped.

## Details

- Existing-tool finding: PSPrices appears to support one account across multiple regions and has Steam Philippines, Nintendo Hong Kong, and PlayStation Indonesia listings.
- PSPrices likely tracks individual regional store listings rather than one abstract game mapped automatically across all stores. This means Brian may need to add multiple listings for the same game.
- Deku Deals may have stronger cross-platform presentation, but the capture says it uses one country setting per account and therefore does not fit Brian's mixed-region setup.
- A custom MVP should avoid automatic cross-store matching at first. The recommended shape is one master item with manually attached official store links for Steam PH, Nintendo HK, and PlayStation Indonesia.
- The source estimated a private MVP at roughly 2-4 focused days for wishlist, URL attachment, regional collectors, price history, and email alerts, with more time for mobile polish, Telegram/push alerts, duplicate-edition handling, retry logic, monitoring, and deployment.

## Open Questions

- UNCERTAIN: Whether PSPrices is reliable enough across Brian's exact regions after one or two sale cycles.
- UNCERTAIN: Whether PlayStation account-specific discounts would make anonymous/public price collection materially inaccurate for Brian's use.
- UNCERTAIN: Whether Brian wants to proceed with a personal URL-driven tracker before trying PSPrices.

## Sources

- `sources/codex-conversations/2026-08-07-codex-conversations.txt`

Last Updated: 2026-08-08
