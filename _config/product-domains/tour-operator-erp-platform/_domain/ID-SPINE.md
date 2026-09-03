# ID Spine — tour-operator-erp-platform

Authoritative ID contract for this domain. Every artifact file MUST use exactly these
IDs when referencing entities owned by another file. Names/descriptions here are
one-liners; the artifact author expands them to reference-domain density.
All ids lowercase. Modeled on the combined 1TIS + TravelSpirit group (see DOMAIN.md).

## Customer groups and customers (customers.json)

Group "Group and Coach Tour Operators" — operators selling fixed-date group departures, bus round trips, adventure/group tours (1TIS reference customers: Djoser, Kras Busreizen, Oad, NRV, SRC Reizen, Shoestring/Koning Aap, Sawadee, André Rieu Travel):
- `gops` — Group Travel Operations Manager. Runs departures end to end: capacity and minimum-participant yielding, bus seat allocation, hotel room lists, guide assignment, passenger lists, supplier and DMC confirmations.
- `resa` — Reservations and Sales Agent. The daily booking-desk user at a group or tailor-made operator: answers phone/email/web inquiries, makes bookings and options, sends quotes, takes payments, handles changes.

Group "Tailor-Made Travel Specialists and DMCs" — specialists composing individual itineraries and the destination companies delivering them (TravelSpirit reference customers: Van Verre, Tenzing Travel, SNP Natuurreizen, S-Cape Travel, Matoke Tours, Pin High Golftravel):
- `tspc` — Tailor-Made Travel Specialist. Builds custom day-by-day itineraries from stored components, sends visual online proposals, iterates with the client, converts leads to trip files at target margin.
- `dmcm` — DMC Ground Operations Manager. Receives service requests from tour operators, confirms or rejects them, keeps room lists and passenger details in sync, invoices the operator.

Group "Travel Business Owners and Finance" — the buyers and controllers of the ERP:
- `town` — Travel Company Owner. Managing director of a 5–150 FTE travel organisation; buys the ERP; cares about margin, scaling without headcount, online share, brand identity, compliance and total cost of ownership.
- `fina` — Finance and Administration Lead. Owns invoicing, payment collection, supplier settlement, accounting integration, flight settlement files, guarantee-fund and package-travel-regulation reporting, month-end close.

Group "Travelers and Trade Partners" — the people who use the operator's portals:
- `trav` — Traveler and Booker. Books a group trip or tailor-made journey online or via the desk, approves quotes, pays, shares passenger details and wishes, downloads documents, travels with the app, reviews afterwards.
- `rsel` — Reseller Travel Agent. Retail or affiliated agent (including ZRA-style independent agents) booking the operator's products through a reseller portal and retrieving documents for their clients.

### JTBD ids (customers.json jobsToBeDone; insights link jobIds to these)
- gops: `jtbd-gops-1` Fill and yield every departure profitably, `jtbd-gops-2` Turn confirmed bookings into flawless departure operations (seats, rooms, guides, lists), `jtbd-gops-3` Keep suppliers and DMCs in sync with every change.
- resa: `jtbd-resa-1` Convert an inquiry into a confirmed booking in one contact, `jtbd-resa-2` Handle changes, options and payments without re-keying, `jtbd-resa-3` Answer any customer question from one booking view.
- tspc: `jtbd-tspc-1` Turn a travel wish into a compelling visual proposal fast, `jtbd-tspc-2` Close the proposal at target margin, `jtbd-tspc-3` Confirm every ad-hoc component with suppliers before departure.
- dmcm: `jtbd-dmcm-1` Confirm operator service requests quickly and accurately, `jtbd-dmcm-2` Deliver ground services with correct passenger and room data.
- town: `jtbd-town-1` Scale bookings and revenue without scaling headcount, `jtbd-town-2` Grow direct online sales under the own brand, `jtbd-town-3` Run a compliant, insight-driven travel business.
- fina: `jtbd-fina-1` Collect every customer payment on time, `jtbd-fina-2` Settle suppliers and flights accurately, `jtbd-fina-3` Close the books and report to fund and regulator without spreadsheets.
- trav: `jtbd-trav-1` Find, book and pay for the right trip with confidence, `jtbd-trav-2` Manage my booking and documents myself, `jtbd-trav-3` Travel informed and share feedback.
- rsel: `jtbd-rsel-1` Book operator products for my clients without phone calls, `jtbd-rsel-2` Keep my clients informed with documents and changes.

### North-star KPI names (use these VERBATIM as pyramid node names; productStrategy northStar must match)
- gops: north star "Operational hours per departure"; supporting include "Departure load factor", "Room list accuracy rate".
- resa: north star "Quote-to-booking conversion rate"; supporting include "Booking handling time", "First-contact resolution rate".
- tspc: north star "Proposal turnaround time"; supporting include "Proposal acceptance rate", "Gross margin per trip file".
- dmcm: north star "Service request confirmation time"; supporting include "Request change error rate", "Operator request volume".
- town: north star "Revenue per FTE"; supporting include "Operating margin", "Online booking share".
- fina: north star "Days to close monthly books"; supporting include "Invoice accuracy rate", "Overdue receivables share".
- trav: north star "Booking completion rate"; supporting include "Document self-service rate", "Traveler satisfaction score".
- rsel: north star "Portal booking share"; supporting include "Reseller booking handling time", "Reseller repeat booking rate".

KPI node id convention (mirrors transport-management-and-freight-exchange): `co-<cust>-top`, `co-<cust>-b1`, `co-<cust>-b1-c1`, `co-<cust>-b1-c1-l1` … and `bo-<cust>-…` for businessOutcomes. Every non-leaf has ≥2 children; target 4 levels (1+2+4+8). Set `icon` fields as `kpi-<cust>-<nodeid>.png`; icon files are backfilled later.
Customer icons: use `<cust>.png` (e.g. `gops.png`) — backfilled later.

## Streams (product-stream.json; JTBD steps reference via streamsNeeded)

- `build-and-price-travel-products` — From supplier contracts to sellable packages, departures and components with pricing, yield rules and group calculations.
- `quote-and-sell-tailor-made-trips` — From lead to accepted visual proposal and opened trip file (Visual Tour Builder flow).
- `book-online-and-at-the-desk` — From website, phone or email inquiry to confirmed booking with deposit paid, whether the traveler books on the real-time site or the agent books in the back office.
- `operate-group-departures` — From confirmed bookings to executed departure: capacity decisions, seat allocation, room lists, guide assignment, passenger lists.
- `request-and-confirm-supplier-services` — From booking lines to confirmed supplier and DMC services with logged communication and synced changes.
- `collect-payments-and-invoice` — From booking to paid invoices: deposits, payment links, reminders, alerts.
- `settle-suppliers-and-close-books` — From supplier invoices and flight settlement files to accounting entries, guarantee-fund reporting and a closed month.
- `serve-travelers-before-during-and-after-the-trip` — From confirmation to documents, my-trip portal and app, in-trip information, aftercare, surveys and reviews.
- `market-and-retain-customers` — From segmented CRM data to campaigns, reviews and repeat bookings.
- `distribute-through-resellers-and-partners` — From product to reseller/agent portal bookings and partner channel feeds.
- `steer-the-travel-business-with-insight` — From transaction data to BI dashboards, margin, forecast and KPI steering.

## Product bricks (product-bricks.json) — root group → subgroup → bricks

Root "Travel Product and Supply":
- Subgroup "Product Catalog and Pricing": `prod` Travel Products and Packages, `comp` Components, Inventory and Availability, `pric` Pricing, Yield and Group Calculations, `cont` Purchasing and Supplier Contracts, `ctnt` Travel Content and Media Management.
- Subgroup "Supplier Network": `supl` Supplier Management and Communication, `sprt` Supplier and DMC Portal.

Root "Sales and Booking":
- Subgroup "Quoting and Tour Building": `vtbl` Visual Tour Builder, Quotes and Itineraries.
- Subgroup "Booking and Customer Management": `book` Booking Files and Dossiers, `crmr` CRM and Contact Management, `webs` Customer Website, CMS and Online Booking, `rsel` Reseller and Agent Portal, `flgt` Flight Import and Ticket Settlement.

Root "Operations and Traveler Service":
- Subgroup "Group Operations": `dept` Departures and Capacity Management, `seat` Seat and Room Allocation, `guid` Guide and Group Leader Portal, `pass` Passenger Data and Operational Lists.
- Subgroup "Traveler Experience": `docs` Travel Documents and Itinerary Delivery, `mytp` Traveler Portal and My-Trip App, `qual` Quality, Complaints, Surveys and Reviews.

Root "Finance and Insight":
- Subgroup "Payments and Invoicing": `invc` Invoicing, Payment Links and Collection, `acct` Accounting Integration and Supplier Settlement, `gfnd` Guarantee Fund and Regulatory Reporting.
- Subgroup "Marketing and Analytics": `mktg` Email Marketing and Segmentation, `bint` Business Intelligence and Reporting.

Root "Platform Foundation":
- Subgroup "Workflow and Communication": `wflw` Workflow, Tasks and Alerts, `comm` Email and Telephony Integration, `aiaa` AI Office Assistants.
- Subgroup "Core Services": `iden` Identity, Tenants and Access, `intg` Integration Hub and Partner APIs.

30 bricks. Module ids must start with `module-` (e.g. `module-book-web`, `module-book-api`).

### Brick dataDependencies → data asset ids (see below); wire at least these
prod→travel-product,travel-content-asset; comp→travel-component,supplier-contract; pric→price-and-yield-rule,travel-product; cont→supplier-contract,supplier-profile; ctnt→travel-content-asset; supl→supplier-profile,supplier-request; sprt→supplier-request,seat-and-room-assignment; vtbl→quote-proposal,travel-component,travel-content-asset; book→booking-file,customer-profile; crmr→customer-profile; webs→travel-product,booking-file; rsel→reseller-agent-profile,booking-file; flgt→flight-ticket-record; dept→departure,booking-file; seat→seat-and-room-assignment,departure; guid→departure,passenger-record; pass→passenger-record; docs→travel-document,booking-file; mytp→booking-file,travel-document,payment-transaction; qual→review-and-survey-response; invc→customer-invoice,payment-transaction; acct→supplier-invoice,customer-invoice,flight-ticket-record; gfnd→guarantee-fund-report,booking-file; mktg→marketing-consent-and-segment,customer-profile; bint→booking-file,customer-invoice; wflw→booking-file; comm→customer-profile; aiaa→quote-proposal,customer-profile; iden→tenant-organization; intg→tenant-organization.

## Data assets (data/data-assets.json) — id → ownerTeamId

- `travel-product` → product-and-pricing
- `travel-component` → product-and-pricing
- `price-and-yield-rule` → product-and-pricing
- `supplier-contract` → product-and-pricing
- `travel-content-asset` → product-and-pricing
- `supplier-profile` → supplier-network
- `supplier-request` → supplier-network
- `quote-proposal` → tour-builder
- `booking-file` → booking-desk
- `customer-profile` → booking-desk
- `flight-ticket-record` → booking-desk
- `reseller-agent-profile` → web-and-channels
- `departure` → group-operations
- `seat-and-room-assignment` → group-operations
- `passenger-record` → group-operations
- `travel-document` → traveler-experience
- `review-and-survey-response` → traveler-experience
- `customer-invoice` → payments-and-invoicing
- `payment-transaction` → payments-and-invoicing
- `supplier-invoice` → accounting-and-compliance
- `guarantee-fund-report` → accounting-and-compliance
- `marketing-consent-and-segment` → marketing-and-insight
- `tenant-organization` → platform-core

23 assets.

## Teams (teams.json) — every brick owned by exactly one team

The combined company has ~40 employees, so teams are small (2–5 people); model that honestly.

Org group "Travel Product Group":
- `product-and-pricing` (stream-aligned) owns prod, comp, pric, cont, ctnt
- `supplier-network` (stream-aligned) owns supl, sprt

Org group "Sales and Booking Group":
- `tour-builder` (stream-aligned) owns vtbl
- `booking-desk` (stream-aligned) owns book, crmr, flgt
- `web-and-channels` (stream-aligned) owns webs, rsel

Org group "Operations and Traveler Group":
- `group-operations` (stream-aligned) owns dept, seat, guid, pass
- `traveler-experience` (stream-aligned) owns docs, mytp, qual

Org group "Finance and Insight Group":
- `payments-and-invoicing` (stream-aligned) owns invc
- `accounting-and-compliance` (complicated-subsystem) owns acct, gfnd
- `marketing-and-insight` (stream-aligned) owns mktg, bint

Org group "Platform and Enablement Group":
- `platform-core` (platform) owns iden, intg, wflw, comm
- `ai-enablement` (enabling) owns aiaa
- `customer-success-and-consulting` (enabling) owns no bricks; runs onboarding, process-optimisation advisory and support; customer dependencies on town, gops, tspc, fina

## Products (product-deployments/products.json) — id, primary customers

- `group-travel-erp` — Group Travel ERP (1TIS GRIP-like back office incl. group operations) — gops, resa, town
- `tailor-made-travel-suite` — Tailor-Made Travel Suite (TravelSpirit-like back office + Visual Tour Builder) — tspc, resa, town
- `online-booking-websites` — Online Booking Websites and CMS (Klantwebsite / SPoE) — trav, town
- `traveler-portal-and-app` — Traveler Portal and My-Trip App — trav
- `partner-portals` — Supplier, DMC, Reseller and Guide Portals — dmcm, rsel, gops
- `finance-and-compliance` — Finance, Payments and Compliance — fina
- `marketing-and-insight` — Marketing and Business Intelligence — town
- `ai-office-assistant` — AI Travel Office Assistant — resa, tspc

## Deployment channels (deployment.json; maas is the structural reference)

Channel groups: "Web Applications" (back-office web app, visual tour builder web, customer website and CMS, traveler portal web, supplier/DMC portal web, reseller portal web, guide portal web), "Mobile Apps" (traveler app via partner apps, guide mobile), "APIs and Integrations" (partner REST API, accounting connectors, payment connectors, flight/GDS import, channel and bed-bank feeds, email marketing connector), "Internal Operations" (tenant administration and support back office). Map deployedBricks with usedInProducts referencing product ids above.

## Sourced company facts (reuse consistently; do not invent numbers)

- Vortex Capital Partners acquired 1TIS and a majority stake in TravelSpirit on 7 May 2026 (buyout; vortexcp.com, livingstonepartners.com). Both brands continue for now; a single brand is planned long-term.
- Combined: 3,000+ daily users, ~€1.5 billion annual travel revenue processed, ~40 employees.
- Leadership: Michiel Stoffels (CEO, formerly TravelSpirit general director), Rico van Loenen (CPO, 1TIS founder and former general director).
- 1TIS: Rijswijk (NL); back office named GRIP; modules Product Management, CRM, Booking, Invoicing & Payments, Process Management, Quality; sites & portals (customer website with real-time booking, traveler "booking inzien" pages, customer portal, reseller portal, supplier portal, group-leader and tour-guide portals); base package from €129/month plus modules. Customers: ACSI, André Rieu Travel, Djoser, Kras Busreizen, NRV, Oad, Sawadee, Shoestring/Koning Aap, SRC Reizen, Nordic, Live To Travel.
- TravelSpirit: Baarn (NL); 100+ travel companies; BackOffice (CRM, telephony, email, workflow, travel plans/products, orders, MediaSpirit photos, invoicing, BI, documents), Visual Tour Builder, Finance & Accounting, Flights (GDS/Airtrade imports, IATA HOT/Airtrade settlement), SPoE website, marketing (email, Trustpilot reviews, segmentation); partners Travelia, Appit, Hubby eSIM, Mollie, Exact, Spotler, Travel Intelligence, WeCloudIT, Airtrotter; member of VVKR and ANVR; ten-phase customer journey (Inspiration → Retention). Customers: Van Verre, Tenzing Travel, SNP Natuurreizen, S-Cape Travel, Matoke Tours, Pin High Golftravel.
- Strategy: build a market-leading travel ERP through product capabilities, embedded AI, organisational professionalisation, and selective acquisitions.
