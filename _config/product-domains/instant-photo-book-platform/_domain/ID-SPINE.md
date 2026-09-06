# ID Spine — instant-photo-book-platform

Authoritative ID contract for this domain. Every artifact file MUST use exactly these IDs when
referencing entities owned by another file. Names/descriptions here are one-liners; the artifact
author expands them to reference-domain density (reference: `freelancer-bookkeeping-service-platform`,
`ride-sharing-marketplace`; `maas` for teams/products/deployment). All ids lowercase.
Modeled on PastBook (see DOMAIN.md). The modeled company is "PastBook" (Amsterdam).

## Customer groups and customers (customers.json)

Group "Memory Keepers" — consumers who pay per printed product; about 80% in the US, then Australia, Europe, the UK:
- `fmly` — Family Memory Keeper. A parent (often the mother, 30–45) with tens of thousands of phone photos of the kids who wants one yearbook per year and a book per school year or holiday, with no time to design; uses the iOS/Android app, camera roll by date/album/Yearbook mode, expects the AI to drop duplicates and blurry shots and the book to be done in a minute.
- `trvl` — Traveller and Milestone Celebrant. Wants a large hardcover of the trip, wedding, graduation or first year of a baby right after the event while the memory is fresh; imports from phone, computer, Dropbox or Google Drive; edits more (cover photo, captions, page order), cares about print quality and vivid colours.
- `sclk` — Facebook Timeline Archivist. Has 10–15 years of life on Facebook (albums, timeline pictures, cover and profile photos, mobile uploads) and wants "my 2016" printed in one click with captions and dates; uses the web Facebook Photo Books flow, one book per year from 2009 to 2025; older, less technical, price-sensitive; lost the Instagram flow when Instagram discontinued third-party access.
- `gftr` — Seasonal Gift Giver. Orders Year in Review books, wall calendars, posters and gift cards for parents, grandparents and partners against a Christmas, Mother's Day or birthday deadline; reacts to discounts and free-shipping upgrades; cares most about delivery before the date and about tracking.

Group "PastBook Operations" — the operator's own staff who use the platform every day:
- `csup` — Customer Support Agent. Works 24/7 shifts from the Netherlands, United States, Sri Lanka or India on WhatsApp, e-mail and chat; handles order changes, address fixes, tracking questions, print-quality complaints, reprints and refunds, and answers every negative Trustpilot review within 48 hours.
- `gmkt` — Growth Marketer. Runs paid social and search, App Store featuring and ASO, e-mail and push campaigns in ten languages and seven currencies with a steep Q4 peak; owns CAC, ROAS, promo codes, the Year in Review campaign and Trustpilot/App Store rating.
- `opsm` — Production and Fulfilment Operations Manager. Runs the network of partner printing facilities on four continents: routing rules, SLAs, capacity for the holiday peak, print quality, reprint root causes, shipping performance per country, FSC paper and unit cost.

Group "Print and Platform Partners":
- `prnt` — Print Partner. A partner printing facility (for example in the US, EU, UK, Australia, Brazil or India) that receives print-ready orders through an API or hot folder, produces hardcover and softcover books, calendars and posters, packs and hands over to carriers, and is measured on SLA, defect rate and peak capacity.
- `plat` — Platform and Channel Partner. The platforms PastBook depends on and must comply with: Meta (Facebook Login and photo permissions), Apple App Store and Google Play (review, featuring, privacy labels, billing rules), Dropbox and Google Drive APIs, payment providers (Visa, Mastercard, American Express, PayPal) and carriers.

### JTBD ids (customers.json jobsToBeDone; insights link jobIds to these)
- fmly: `jtbd-fmly-1` Turn a year of phone photos into a finished yearbook in minutes, `jtbd-fmly-2` Trust the automatic selection so I do not have to review 5,000 photos, `jtbd-fmly-3` Make the yearbook an annual habit for the family.
- trvl: `jtbd-trvl-1` Print the trip or milestone as a large hardcover right after the event, `jtbd-trvl-2` Personalise cover, order and captions without learning a design tool, `jtbd-trvl-3` Get a book whose print quality matches the moment.
- sclk: `jtbd-sclk-1` Print a whole Facebook year with captions in one click, `jtbd-sclk-2` Keep my photos safe and private while the book is made, `jtbd-sclk-3` Reorder past years and gift copies to family.
- gftr: `jtbd-gftr-1` Get a personalised gift delivered before the date, `jtbd-gftr-2` Pick the right product, size and price for the recipient, `jtbd-gftr-3` Give when I have no photos: gift cards and shared albums.
- csup: `jtbd-csup-1` Resolve an order problem in one contact, `jtbd-csup-2` Reprint or refund quickly when quality or delivery fails, `jtbd-csup-3` Turn complaints and reviews into product and partner fixes.
- gmkt: `jtbd-gmkt-1` Acquire customers profitably across countries and seasons, `jtbd-gmkt-2` Convert installs and previews into paid orders, `jtbd-gmkt-3` Bring customers back every year.
- opsm: `jtbd-opsm-1` Route every order to the right partner and deliver on time, `jtbd-opsm-2` Keep print quality and unit cost within target across partners, `jtbd-opsm-3` Scale capacity for the holiday peak without failures.
- prnt: `jtbd-prnt-1` Receive print-ready, error-free orders I can produce within SLA, `jtbd-prnt-2` Plan capacity and get paid for volume with clear quality expectations.
- plat: `jtbd-plat-1` Keep the app and integrations compliant with platform policies, `jtbd-plat-2` Grow orders through the channel without policy incidents.

### North-star KPI names (use these VERBATIM as pyramid node names; productStrategy northStar must match)
- fmly: north star "Minutes from opening the app to ordering a book"; supporting include "Photo selection acceptance rate", "Books ordered per family per year".
- trvl: north star "Days from event end to book ordered"; supporting include "Large-format share of orders", "Print quality complaint rate".
- sclk: north star "Facebook books completed per connected account"; supporting include "Facebook import completion rate", "Repeat yearbook rate".
- gftr: north star "Gifts delivered before the occasion"; supporting include "On-time delivery rate in peak season", "Gift card redemption rate".
- csup: north star "First-contact resolution rate"; supporting include "Median first response time", "Reprint rate".
- gmkt: north star "Blended customer acquisition cost"; supporting include "Return on ad spend", "Install to order conversion rate".
- opsm: north star "On-time production and shipping rate"; supporting include "Print defect rate", "Unit production cost per book".
- prnt: north star "Orders produced within SLA"; supporting include "Print file rejection rate", "Peak capacity utilisation".
- plat: north star "Orders originating through the channel"; supporting include "Policy compliance incidents", "Integration uptime".

KPI node id convention (mirrors freelancer-bookkeeping-service-platform): `co-<cust>-top`, `co-<cust>-b1`, `co-<cust>-b1-c1`, `co-<cust>-b1-c1-l1` … and `bo-<cust>-…` for businessOutcomes. Every non-leaf has ≥2 children; target 4 levels (1+2+4+8). Set `icon` fields as `kpi-<cust>-<nodeid>.png`; icon files are backfilled later. Seed values must be arithmetically consistent across personas (funnel totals vs per-segment leaves, child cost ≤ parent cost). Mark seed values as modeled, not official PastBook figures.
Customer icons: use `<cust>.png` (e.g. `fmly.png`) — backfilled later. Do NOT set `media` fields on JTBDs, journeys or relations (no images exist).

## Streams (product-stream.json; JTBD steps reference via streamsNeeded — use these ids only)

- `discover-and-install-the-app` — From an ad, App Store feature, GQ gift guide or a friend's book to an installed PastBook app (1M+ downloads) or a visit to pastbook.com with photo-library permission granted.
- `import-photos-from-phone-and-cloud` — From the camera roll (by date, location, album or Yearbook mode), a computer upload, Dropbox or Google Drive to an indexed photo set with timestamps and locations, uploaded over encrypted connections.
- `connect-facebook-and-pick-a-year` — From Facebook Login to albums, timeline pictures, cover and profile photos and mobile uploads with captions, grouped per year 2009–2025, with the permission scope Meta allows.
- `curate-the-best-photos-with-ai` — From thousands of photos to the best moments in under 60 seconds: quality and context analysis, duplicate and near-duplicate removal, blur detection, smart grouping into moments.
- `auto-design-the-book-and-preview` — From curated moments to a laid-out book with cover, theme colours and captions, a free preview in under a minute and a shareable highlight video.
- `edit-and-personalise-the-book` — From the automatic design to the customer's book: reorder pages, swap or remove photos, add captions and a quote, choose cover photo, theme colours and a back-cover photo add-on.
- `choose-format-price-and-checkout` — From a finished design to a paid order: small or large hardcover, cover rules by page count, extra pages, calendars and posters, promo codes and gift cards, seven currencies, Visa/Mastercard/Amex/PayPal.
- `render-print-ready-files-and-route-to-a-printer` — From a paid order to imposed, preflighted print-ready files routed to the partner facility nearest the customer with capacity, with order data and packing slips.
- `produce-ship-and-track-the-order` — From a routed job to a produced, packed, shipped and tracked parcel within the published delivery windows (US 4–8 business days, UK 4–5, FR/NL/IT/DE 3–5, EU 5–7, CA/AU 5–10, NZ/IN/BR 7–10).
- `resolve-support-requests-and-reprints` — From a WhatsApp, e-mail or chat contact to a resolved order change, tracking answer, reprint or refund, and a public reply to every negative Trustpilot review within 48 hours.
- `run-seasonal-campaigns-and-promotions` — From a marketing calendar to campaigns, discounts and Year in Review promotions in ten languages and seven currencies with app-store featuring and attribution, peaking in Q4.
- `retain-customers-with-yearbooks-and-reminders` — From a first order to the next: yearbook and calendar reminders, reorders of past years, gifting copies to family, ratings prompts that feed Trustpilot and the App Store.
- `manage-the-global-print-partner-network` — From partner selection to SLAs, integration, capacity planning for peaks, quality audits, reprint root causes, unit cost, FSC paper and local production on four continents.
- `protect-photo-privacy-and-platform-compliance` — From consent to deletion: encrypted transfer and storage of personal photos, GDPR/CCPA rights, Meta platform terms and app review, App Store and Google Play privacy labels, payment compliance.

14 streams.

## Product bricks (product-bricks.json) — root group → subgroup → bricks

Root "Consumer App and Web Creator":
- Subgroup "Mobile App": `mapp` Mobile App Shell (iOS and Android), `phot` Photo Library Access and Import (by date, location, album, Yearbook mode), `prev` Instant Preview and Highlight Video Sharing.
- Subgroup "Web Creator": `webc` Web Book Creator, `upld` Upload from Computer, Dropbox and Google Drive, `fbim` Facebook Connect and Year Selector.
- Subgroup "Editing and Personalisation": `edit` Page and Photo Editor (reorder, swap, remove, captions), `cvrd` Cover, Theme and Add-on Designer (cover photo, theme colours, quote, back-cover photo).

Root "Intelligent Curation Engine":
- Subgroup "Photo Analysis": `qual` Image Quality Scoring (blur, exposure, resolution), `dedu` Duplicate and Near-duplicate Detection, `mmnt` Moment and Event Grouping (time, place, people), `sele` Best-photo Selection and Ranking.
- Subgroup "Automatic Design": `layo` Smart Layout Generator (page designs, photo placement, captions and dates), `thme` Theme and Colour Palette Engine.

Root "Commerce":
- Subgroup "Catalog and Pricing": `ctlg` Product Catalog (book sizes, cover types, calendars, posters), `pric` Pricing, Page Rules and Currencies (24-page base, extra pages, soft/hard cover thresholds, seven currencies), `prom` Promotions, Discount Codes and Gift Cards.
- Subgroup "Checkout and Orders": `cart` Cart and Checkout, `paym` Payments (Visa, Mastercard, American Express, PayPal), `ordr` Order Management and Status, `acct` Customer Account and Order History.

Root "Production and Fulfilment":
- Subgroup "Print Preparation": `rndr` Print-ready PDF Rendering and Imposition, `pflt` Preflight and Print Quality Checks.
- Subgroup "Partner Network and Shipping": `rout` Print Partner Routing (nearest facility, capacity, cost), `pint` Print Partner Integration (order API, hot folder, status callbacks), `ship` Shipping Rates, Carrier Labels and Tracking, `qmon` Production SLA and Quality Monitoring.

Root "Growth and Customer Care":
- Subgroup "Marketing and Lifecycle": `camp` Campaign and Seasonal Promotion Management, `attr` App Store Optimisation and Marketing Attribution, `lcyc` Lifecycle Messaging and Yearbook Reminders (push, e-mail), `loca` Localisation (ten languages, seven currencies), `revw` Reviews and Ratings Management (Trustpilot, App Store, Google Play).
- Subgroup "Support": `help` Help Center and Self-service, `sprt` Support Desk (WhatsApp, e-mail, chat, 24/7), `rprt` Reprint and Refund Handling.

Root "Platform Foundation":
- Subgroup "Core Services": `iden` Identity and Social Login, `medi` Photo Media Storage and CDN, `priv` Privacy, Consent and Data Deletion (GDPR, CCPA), `anly` Analytics and Experimentation, `intg` Integration Gateway (Meta Graph API, Dropbox, Google Drive, payment providers, carriers, app stores).

40 bricks. Module ids must start with `module-` (e.g. `module-phot-mobile`, `module-sele-service`). `backoffice-interface` modules belong in the `interfaces` layer; a `message-queue` module must never call another brick's API; dependencies point consumer → provider.

### Brick dataDependencies → data asset ids (see below); wire at least these
mapp→customer-account,analytics-event; phot→photo-asset,photo-source-connection; prev→preview-video,book-project; webc→book-project,photo-asset; upld→photo-asset,photo-source-connection; fbim→photo-source-connection,photo-asset,consent-record; edit→book-project,page-layout; cvrd→book-project,design-theme; qual→photo-asset,photo-quality-score; dedu→photo-asset,photo-cluster; mmnt→photo-cluster,photo-asset; sele→selection-result,photo-quality-score,photo-cluster; layo→page-layout,selection-result,design-theme; thme→design-theme; ctlg→product-catalog-item; pric→price-list,product-catalog-item; prom→promotion-code,gift-card; cart→checkout-session,price-list; paym→payment-transaction,checkout-session; ordr→order,payment-transaction; acct→customer-account,order; rndr→print-file,book-project; pflt→preflight-report,print-file; rout→production-job,print-partner-profile; pint→production-job,print-partner-profile,print-file; ship→shipment,shipping-rate; qmon→quality-incident,production-job,shipment; camp→marketing-campaign,promotion-code; attr→attribution-event,marketing-campaign; lcyc→lifecycle-message,customer-account; loca→localisation-string; revw→customer-review; help→help-article; sprt→support-ticket,order; rprt→reprint-case,quality-incident,support-ticket; iden→user-identity,customer-account; medi→photo-asset,print-file; priv→consent-record,audit-trail-entry; anly→analytics-event,attribution-event; intg→photo-source-connection,payment-transaction,shipment,audit-trail-entry.

## Data assets (data/data-assets.json) — id → ownerTeamId

- `customer-account` → commerce-team
- `user-identity` → platform-and-data-team
- `consent-record` → platform-and-data-team
- `audit-trail-entry` → platform-and-data-team
- `analytics-event` → platform-and-data-team
- `photo-asset` → platform-and-data-team
- `photo-source-connection` → web-creator-team
- `photo-quality-score` → curation-ai-team
- `photo-cluster` → curation-ai-team
- `selection-result` → curation-ai-team
- `page-layout` → curation-ai-team
- `design-theme` → curation-ai-team
- `book-project` → web-creator-team
- `preview-video` → mobile-app-team
- `product-catalog-item` → commerce-team
- `price-list` → commerce-team
- `promotion-code` → growth-marketing-team
- `gift-card` → commerce-team
- `checkout-session` → commerce-team
- `payment-transaction` → commerce-team
- `order` → commerce-team
- `shipping-rate` → print-and-fulfilment-engineering
- `print-file` → print-and-fulfilment-engineering
- `preflight-report` → print-and-fulfilment-engineering
- `print-partner-profile` → production-operations
- `production-job` → print-and-fulfilment-engineering
- `shipment` → print-and-fulfilment-engineering
- `quality-incident` → production-operations
- `support-ticket` → customer-support-team
- `reprint-case` → customer-support-team
- `help-article` → customer-support-team
- `marketing-campaign` → growth-marketing-team
- `attribution-event` → growth-marketing-team
- `lifecycle-message` → growth-marketing-team
- `customer-review` → brand-content-and-localisation
- `localisation-string` → brand-content-and-localisation

36 assets. Personal-data level is high for photo assets (faces, children, locations, EXIF), source connections (OAuth tokens) and accounts; tag GDPR (EU customers, Dutch company), CCPA (US majority), COPPA-adjacent care for children's photos, PCI DSS scope for payments (tokenised via providers), Meta Platform Terms for Facebook data (delete on request, no retention beyond the order), retention of print files limited after delivery.

## Teams (teams.json) — every brick owned by exactly one team

PastBook is a scale-up with about 16 named core staff on the careers page, engineering and support colleagues in Amsterdam, Milan, Vilnius, New York, Colombo (with Gapstars) and New Delhi, and 24/7 support from the Netherlands, US, Sri Lanka and India. Model the organisation at about 75 people: small product teams (3–7), an outsourced-inclusive support team and a lean operations team; printing is done by partners, not staff.

Org group "Product and Engineering" (Amsterdam, Vilnius, Milan, Colombo):
- `mobile-app-team` (stream-aligned) owns mapp, phot, prev
- `web-creator-team` (stream-aligned) owns webc, upld, fbim, edit, cvrd
- `curation-ai-team` (complicated-subsystem) owns qual, dedu, mmnt, sele, layo, thme
- `commerce-team` (stream-aligned) owns ctlg, pric, prom, cart, paym, ordr, acct
- `print-and-fulfilment-engineering` (platform) owns rndr, pflt, rout, pint, ship
- `platform-and-data-team` (platform) owns iden, medi, priv, anly, intg

Org group "Operations and Customer Care" (Amsterdam, New York, Colombo, New Delhi):
- `production-operations` (stream-aligned; partner managers and quality) owns qmon; customer dependencies on opsm, prnt
- `customer-support-team` (stream-aligned; 24/7 agents in four countries) owns help, sprt, rprt; customer dependencies on csup, fmly, gftr, trvl

Org group "Growth and Brand" (Amsterdam, Milan, New York):
- `growth-marketing-team` (stream-aligned; performance marketing, CRM, ASO) owns camp, attr, lcyc; customer dependencies on gmkt, fmly, gftr, plat
- `brand-content-and-localisation` (enabling; content, ten languages, reviews, sustainability communication) owns loca, revw; customer dependencies on gmkt, sclk, trvl

10 teams. Team metrics must be KPI names that exist in the pyramids of a customer the team serves. No provider-side "Provides …" edges: dependencies are consumer → provider only (as in maas).

## Products (product-deployments/products.json) — id, primary customers

- `pastbook-app` — PastBook: 1-Click Photo Book app (iOS and Android; 1M+ downloads; camera roll import, AI curation, books, calendars, posters) — fmly, trvl, gftr
- `facebook-photo-books` — Facebook Photo Books: one book per year 2009–2025 from albums, timeline, cover and profile photos with captions — sclk, gftr
- `web-photo-book-creator` — Photo book from computer, Dropbox or Google Drive on pastbook.com with curation in 60 seconds — trvl, sclk
- `year-in-review-photo-book` — Year in Review yearbook campaign product (phone or Facebook), holiday-season gift — fmly, sclk, gftr
- `photo-calendars` — Wall calendars 8" × 11.7" (USD 24.99) and 11.7" × 16" (USD 34.99), iOS — gftr, fmly
- `photo-posters` — Folded (USD 29.99) and rolled (USD 39.99) posters 16.5" × 23.4" — gftr, trvl
- `gift-cards-and-promotions` — Gift cards, promo codes and seasonal discounts — gftr, gmkt
- `pastbook-website-and-help-center` — pastbook.com, pricing and shipping, sustainability, help center in ten languages — sclk, trvl, csup
- `customer-support-desk` — 24/7 support via WhatsApp, e-mail and chat with reprint handling (internal) — csup, fmly
- `print-partner-order-feed` — Partner order API, hot folder, status callbacks and SLA dashboard (partner-facing) — prnt, opsm
- `production-control-tower` — Routing rules, capacity, SLA and quality monitoring (internal) — opsm
- `growth-and-campaign-console` — Campaign, promo, attribution, lifecycle and review management (internal) — gmkt, plat

12 products. Use `<product-id>.png` icons (rendered later into product-deployments/icons). `neededBricks`/`interfaces` are retired fields — brick coverage is expressed via deployment.json `usedInProducts`.

## Deployment channels (deployment.json; maas is the structural reference)

Channel groups: "Mobile Apps" (iOS App Store, Google Play: photo import, curation, preview, editor, checkout, calendars), "Web Applications" (pastbook.com creator and Facebook flow, customer account and order history, help center, pricing pages in ten languages), "Integrations" (Meta Graph API and Facebook Login, Dropbox and Google Drive, payment providers Visa/Mastercard/Amex/PayPal, carriers and tracking, print partner APIs and hot folders, App Store and Google Play, Trustpilot, attribution/MMP), "Print Outputs" (print-ready PDFs for books, calendars and posters, packing slips, partner job tickets), "Internal Operations" (support desk, production control tower, growth and campaign console, analytics and experimentation, privacy and deletion tooling). Map deployedBricks with usedInProducts referencing product ids above.

## Sourced company facts (reuse consistently; do not invent numbers)

- PastBook, Amsterdam, founded 2012 in the Rockstart Accelerator by Stefano Cutello (former eBay tech lead; Tech.eu also names co-founder Giuseppe Prioriello and dates the start to 2010). Mission "make reliving memories frictionless"; home page "Your Memories, Turned into Beautiful Photo Books in Seconds".
- Vortex Capital Partners: EUR 350k seed round December 2015 (StartupJuncture); USD 2M convertible note plus follow-on led by Vortex September 2017, total raised above USD 2.5M (Business Wire, Tech.eu: 10x year-on-year revenue growth three years in a row, 80% of customers in the USA). Vortex page: growth capital, tech-enabled, high growth, production facilities on four continents, shipping to 150+ countries, current investment.
- Leadership since 23 April 2020: Wouter Staatsen CEO (ex-CEO Albelli, ex-VP Cimpress, board advisor since 2018), Stefano Cutello Chief Product & Innovation Officer, Daniel Scheijen CMO (ex-Albelli country manager).
- Revenue USD 14.3M in 2019, projected to triple to about USD 42.9M in 2020; AI app launched on iOS July 2021 with patent-pending technology (books in under 60 seconds, quality and context analysis, duplicate removal, smart grouping); North America largest market, then Australia, Europe, UK (londonlovestech.com, 6 July 2021).
- Awards: Deloitte Technology Fast50 2019 winner Media & Entertainment, top 3 overall, 4,623% turnover growth (Business Wire, 13 October 2019); Fast50 2021 top half, 528% growth, third year in a row; Deloitte Rising Star 2016; FT1000 position 20 (2020) and listed 2020, 2021, 2022; Wired hottest startups in Europe; TNW Tech5; App Store featured in several countries (27 September 2022); highlight video sharing on iOS (17 July 2023); GQ gift guide.
- Scale: 10M+ books created since 2012 (year-in-review page); 1M+ app downloads (app page); Trustpilot TrustScore 4.5 from 35,837 reviews, 79% five-star, 2% one-star, replies to 100% of negative reviews typically within 48 hours (September 2026); 24/7 support via WhatsApp, e-mail and chat; ten site languages; seven currencies (USD, EUR, GBP, CAD, AUD, NZD, BRL).
- Sources: phone camera roll (by date, location, album, Yearbook mode), Facebook (albums, cover and profile photos, timeline pictures, mobile uploads; years 2009–2025), computer upload, Dropbox, Google Drive. Instagram: "Instagram has shifted its focus, discontinuing support for third-party tools designed for personal accounts" — PastBook no longer connects to Instagram and points to Facebook, the app and manual upload (pastbook.com/instagram-ends-support-for-photo-products/). Photos are imported over encrypted connections.
- Prices and formats: see DOMAIN.md (Small Hardcover 8.5" × 6" USD 19.99 / EUR 24.99 / GBP 16.99 for 24 pages, +USD 0.40 per page; Large Hardcover 12" × 8.5" USD 34.99 / EUR 41.99 / GBP 27.99, +USD 0.55 per page; calendars USD 24.99 / 34.99; posters USD 29.99 / 39.99; cover rules ≤16 soft, 18–26 choice, 27–300 hard, >300 soft; delivery windows per country; production starts on payment; local printing to reduce CO2).
- Sustainability: FSC-certified paper, most products produced in the country of the order, reforestation with Land Life Company, suppliers committed to sustainable practices, waste and energy reduction in offices and facilities.
- Team and culture: about 16 named team members on the careers page; operations in the Netherlands, US, Sri Lanka and India for 24/7 support; LinkedIn: Amsterdam, Milan, New York, Vilnius, Colombo, New Delhi; hybrid work, flexible hours; Colombo tech team with Gapstars (October 2025).
- Market: Europe photobook and album market USD 1.05 billion in 2025, 29.96% of the global market (Fortune Business Insights); CEWE is Europe's photobook leader with 6.32 million CEWE PHOTOBOOK copies in 2025.

## Verified URLs (use ONLY these in insights.json sources, links.json and competition.json; do not invent slugs)

PastBook: https://pastbook.com/ · https://pastbook.com/app/ · https://pastbook.com/facebook-photo-books/ · https://pastbook.com/pricing-and-shipping/ · https://pastbook.com/sustainability/ · https://pastbook.com/newsroom/ · https://pastbook.com/careers/ · https://pastbook.com/year-in-review-photo-book/ · https://pastbook.com/instagram-ends-support-for-photo-products/ · https://pastbook.com/newsroom/pastbook-announces-wouter-staatsen-as-its-new-ceo-and-stefano-cutello-as-its-chief-product-innovation-officer/ · https://pastbook.com/newsroom/pastbook-named-as-one-of-the-fastest-growing-companies-in-the-netherlands-for-the-3rd-year-in-a-row/ · https://help.pastbook.com/hc/en-us/articles/115001811103--What-book-sizes-are-available- · https://help.pastbook.com/hc/en-us/articles/115001811183-How-much-does-a-Photo-Book-cost · https://help.pastbook.com/hc/en-us/articles/115001850806--How-much-does-shipping-cost · https://help.pastbook.com/hc/en-us/categories/115000419183-Photo-Books · https://apps.apple.com/us/app/pastbook-1-click-photo-book/id1524251801 · https://play.google.com/store/apps/details?id=com.pastbook.app · https://www.trustpilot.com/review/pastbook.com · https://www.linkedin.com/company/pastbook/
Investor and press: https://vortexcp.com/investment/pastbook/ · https://www.businesswire.com/news/home/20170921005099/en/PastBook-Raises-2-Million-to-Scale-Up-its-One-Click-Photo-Books-Platform · https://www.businesswire.com/news/home/20191013005013/en/PastBook-Wins-the-Deloitte-Technology-Fast50-2019-for-the-Media-Entertainment-Sector-and-Makes-It-to-the-Podium-of-the-Competition · https://tech.eu/2017/09/21/pastbook-funding/ · https://startupjuncture.com/2015/12/26/photo-book-startup-pastbook-raises-eur-350k-in-seed-funding/ · https://londonlovestech.com/pastbook-launches-cutting-edge-ai-driven-app-following-exponential-growth/ · https://thedeadpixelssociety.com/pastbook-appoints-wouter-staatsen-as-ceo-stefano-cutello-moves-to-chief-product-and-innovation-officer/ · https://thenextweb.com/news/pastbook-now-lets-create-collaborate-photo-albums-directly-iphone
Market: https://www.fortunebusinessinsights.com/europe-photobook-and-album-market-107495 · https://www.fortunebusinessinsights.com/photo-album-market-104421 · https://www.beyond-print.net/the-photobook-market-2025-those-who-dont-scale-lose/

## Competitor facts (business/competition.json; official sources only; keep reported scope; leave stats out rather than invent)

- PastBook (pastbook.com; Amsterdam; category modeled-company) — facts above.
- CEWE (cewe.de; company.cewe.de; Oldenburg, Germany; Europe's photobook market leader): 2025 group turnover EUR 864.5M (+3.8%), EBIT EUR 88.2M, photofinishing turnover EUR 745.5M, 6.32 million CEWE PHOTOBOOK copies (record), about 4,000 employees in 21 countries, more than 100 million CEWE PHOTOBOOKs sold since launch, 2026 guidance EUR 870–900M — source https://www.eqs-news.com/news/corporate-news/cewe-achieves-all-targets-in-2025-and-aims-to-further-increase-revenue-and-earnings-in-2026-plans-to-uphold-continuous-dividend-growth/70292c17-c943-4783-bd11-4323b6ce54d8_en (26 March 2026).
- Storio group (storiogroup.com; Amsterdam; formerly albelli-Photobox Group, rebranded March 2024; brands albelli, Photobox, bonusprint, Posterxxl, Fotoknudsen, Hofmann, Önskefoto): six brands in thirteen European markets, over eleven million customers, multiple manufacturing sites across Europe, CEO Alessandro Coppo (2024), consolidated revenue above EUR 340M (press release, 2024) — https://www.storiogroup.com/ · https://www.storiogroup.com/about-us/ · https://www.storiogroup.com/press-release/ · https://www.storiogroup.com/our-brands/
- Shutterfly (shutterfly.com; California, US; owned by Apollo Global Management since 2019; founded 1999) — use only https://www.shutterfly.com/ ; if no official stat is verifiable leave stats empty (third-party e-commerce estimate ~USD 937M 2025 must NOT be used as official).
- Snapfish (snapfish.com; US; owned by District Photo; photo books 5x7 to 12x12, hardcover, softcover, layflat, linen, leather; 8x11 hardcover from USD 13.50; ships US, UK, Ireland, Germany, France, Italy, Australia, New Zealand) — https://www.snapfish.com/photo-book
- Mixbook (mixbook.com; Redwood City, California; founded 2006): 6 million+ customers, 20 million+ projects printed, books up to 400 pages, Mixbook Studio AI design tool and Story Mode, iOS app, ships to Australia, Canada, EU, UK, "#1 rated in photo books" claim — https://www.mixbook.com/
- Chatbooks (chatbooks.com; Lehi, Utah; founded 2014 by Nate and Vanessa Quigley; subscription "Monthbooks" auto-printed from phone/Instagram photos; USD 11.5M Series B 2017 per PR Newswire https://www.prnewswire.com/news-releases/chatbooks-raises-115-million-series-b-funding-300403536.html) — https://chatbooks.com/ ; no other stats.
- Popsa (popsa.com; London): USD 1M revenue per employee (May 2025), 46 people, 2 million customers, 50+ countries, marketing in 12 languages, AI across marketing, support, supplier negotiation and logistics — https://popsa.com/perspectives/scaling-revenue-with-ai/ ; third-party USD 58M 2025 revenue (thedeadpixelssociety.com) may be cited only as third-party.
- Google Photos photo books (photos.google.com; Mountain View): 7-inch softcover and 9-inch hardcover, 20–140 pages, 2–4 business days to print, US economy 8–11 business days, available in the US, Canada and 28+ European countries — https://support.google.com/photos/answer/9079710
- Saal Digital (saal-digital.com; Germany, production in Röttenbach; founded 1981): photo books on real photo paper, delivery to more than 25 countries in Europe and the US, 4.9/5 from over 235,000 verified reviews, many orders leave production within 24 hours — https://www.saal-digital.com/
- smartphoto group (smartphotogroup.com; Wetteren, Belgium; brands smartphoto, naYan, TopFanZ, Image Insight; active in 12 European countries; delisted from Euronext Brussels 9 July 2025) — https://www.smartphotogroup.com/ ; 2024 revenue EUR 80.5M is third-party (stockanalysis.com) and must be labelled as such or omitted.
Every business stat must carry a source URL and reported scope.
