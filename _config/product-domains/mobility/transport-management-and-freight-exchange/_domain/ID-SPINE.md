# ID Spine — transport-management-and-freight-exchange

Authoritative ID contract for this domain. Every artifact file MUST use exactly these
IDs when referencing entities owned by another file. Names/descriptions here are
one-liners; the artifact author expands them to reference-domain density.
All ids lowercase. Modeled on Alpega Group (see DOMAIN.md).

## Customer groups and customers (customers.json)

Group "Enterprise Shippers" — manufacturers, FMCG, automotive, chemicals, pharma, retail (Heineken, Asahi UK, Höganäs, Barry Callebaut are reference customers):
- `tdir` — Transportation Director. Owns multi-country freight spend and carrier strategy at an enterprise shipper; cares about cost vs market, capacity coverage, service levels, CO2 reporting.
- `tpln` — Transport Planner. Runs daily planning/tendering/execution/exceptions for plants and DCs; lives in the TMS all day.

Group "Carriers":
- `cdsp` — Carrier Dispatcher. Plans trucks and drivers at a mid-size European trucking company (30-300 trucks); mixes contract freight with spot loads from exchanges.
- `ownr` — Owner-Operator. Runs 1-5 trucks; finds return loads on freight exchanges; fears fraud and non-payment.

Group "Freight Forwarders and Brokers":
- `fwdr` — Freight Forwarder Operator. Covers client loads with subcontracted network capacity; uses exchanges on both sides (posts freight, finds trucks).

Group "Warehouse and Dock Operations":
- `dksm` — Dock Site Manager. Runs inbound/outbound docks at a plant or DC; wants smooth slot utilization and short truck turnaround.

### JTBD ids (customers.json jobsToBeDone; insights link jobIds to these)
- tdir: `jtbd-tdir-1` Secure yearly capacity at target cost (procurement/tendering), `jtbd-tdir-2` Control total freight spend end to end (budget, audit, settlement), `jtbd-tdir-3` De-risk and decarbonize the carrier base (compliance, trust, CO2).
- tpln: `jtbd-tpln-1` Plan and tender the daily load plan, `jtbd-tpln-2` Track shipments and resolve exceptions before customers notice, `jtbd-tpln-3` Cover uncovered loads fast on the spot market.
- cdsp: `jtbd-cdsp-1` Keep every truck loaded in both directions, `jtbd-cdsp-2` Win and execute enterprise shipper contracts digitally, `jtbd-cdsp-3` Get paid on time and safely.
- ownr: `jtbd-ownr-1` Find a good return load before driving home empty, `jtbd-ownr-2` Avoid fraudsters and bad payers.
- fwdr: `jtbd-fwdr-1` Cover client loads with reliable network capacity, `jtbd-fwdr-2` Manage a trusted subcontractor pool.
- dksm: `jtbd-dksm-1` Smooth dock utilization across the day, `jtbd-dksm-2` Cut truck waiting and turnaround times.

### North-star KPI names (use these VERBATIM as pyramid node names; productStrategy northStar must match)
- tdir: north star "Transport cost per shipment vs market"; supporting include "On-time delivery rate", "Tender acceptance rate".
- tpln: north star "Planner touches per load"; supporting include "Track and trace coverage", "Exception resolution time".
- cdsp: north star "Loaded kilometers share"; supporting include "Empty kilometers share", "Days sales outstanding".
- ownr: north star "Return-load coverage rate"; supporting include "Time to find a load", "Payment loss rate".
- fwdr: north star "Client load coverage rate"; supporting include "Subcontractor fill time", "Gross margin per load".
- dksm: north star "Truck turnaround time"; supporting include "Dock slot utilization", "Late slot arrivals share".

KPI node id convention (mirrors freight-logistics-orchestration): `co-<cust>-top`, `co-<cust>-b1`, `co-<cust>-b1-c1` … and `bo-<cust>-…` for businessOutcomes. Icon names: `kpi-<cust>-co-…​.png` pattern optional — set `icon` fields as `kpi-<cust>-<nodeid>.png`; files are backfilled later.
Customer icons: use `<cust>.png` (e.g. `tdir.png`) — backfilled later.

## Streams (product-stream.json; JTBD steps reference via streamsNeeded)

- `procure-freight-capacity` — From transport RFP to signed rate cards and routing guides (TenderEasy-like).
- `plan-and-optimize-transport` — From ERP orders to an optimized, tendable load plan.
- `execute-transport-orders` — From planned load to accepted, dispatched, documented transport order via the carrier network (Transport Execution).
- `match-spot-freight` — From posted spot load or free truck to a matched, booked deal on the exchange.
- `track-and-manage-exceptions` — From dispatched order to delivered with live ETA and resolved disruptions.
- `schedule-docks-and-yards` — From booked transport to a confirmed dock slot and fast site turnaround.
- `settle-and-audit-freight` — From proof of delivery to audited invoice, self-billing, and secured payment.
- `analyze-network-performance` — From transaction data to cost/service/CO2 insight and lane benchmarks.
- `onboard-and-trust-network` — From carrier signup to vetted, rated, fraud-screened network member.

## Product bricks (product-bricks.json) — root group → subgroup → bricks

Root "Shipper Products":
- Subgroup "Planning and Execution Management": `tord` Transport Order Management, `plan` Transport Planning and Optimization, `csel` Carrier Selection and Load Tendering.
- Subgroup "Procurement and Rates": `tndr` Freight Procurement and Tendering, `rate` Rates and Contract Management.

Root "Network and Carrier Products":
- Subgroup "Freight Exchange": `fxch` Freight Exchange Marketplace, `mtch` Freight Matching and Recommendations.
- Subgroup "Carrier Experience and Trust": `cprt` Carrier Portal and Mobile, `cvet` Carrier Vetting and Compliance, `trst` Trust Scores and Fraud Prevention, `pgar` Payment Guarantee and Collections.

Root "Execution and Visibility":
- Subgroup "Connected Execution": `texe` Transport Execution Orchestration, `conn` Carrier Connectivity Gateway (API/EDI/telematics), `edoc` e-Documents (eCMR, POD).
- Subgroup "Visibility and Sites": `trck` Real-Time Visibility and ETA, `excp` Exception Management, `dock` Dock Scheduling.

Root "Commercial and Insight":
- Subgroup "Settlement": `cost` Freight Cost Management, `audt` Freight Audit and Self-Billing.
- Subgroup "Analytics": `anly` Transport Analytics and Benchmarking, `co2e` Emissions Reporting.

Root "Platform Foundation":
- Subgroup "Integration and Data": `intg` ERP and Systems Integration Hub, `mdat` Logistics Master Data.
- Subgroup "Core Services": `iden` Identity and Organization Management, `notf` Notifications and Messaging, `bill` Subscription and Usage Billing.

26 bricks. Module ids must start with `module-` (e.g. `module-tord-web`).

### Brick dataDependencies → data asset ids (see below); wire at least the obvious ones
tord→transport-order; plan→transport-order,location-master; csel→contract-rate-card,carrier-profile; tndr→tender-event,contract-rate-card; rate→contract-rate-card; fxch→spot-freight-offer,vehicle-capacity-offer; mtch→spot-freight-offer,vehicle-capacity-offer,network-trust-score; cprt→carrier-profile; cvet→carrier-profile; trst→network-trust-score; pgar→payment-guarantee-case; texe→shipment-execution-record,transport-order; conn→tracking-event-stream; edoc→transport-document; trck→tracking-event-stream,eta-prediction; excp→shipment-execution-record; dock→dock-slot-booking; cost→freight-invoice,contract-rate-card; audt→freight-invoice; anly→lane-rate-benchmark; co2e→emissions-record; iden→shipper-organization; mdat→location-master; bill→shipper-organization.

## Data assets (data/data-assets.json) — id → ownerTeamId

- `transport-order` → transport-planning
- `shipment-execution-record` → transport-execution
- `contract-rate-card` → freight-procurement
- `tender-event` → freight-procurement
- `spot-freight-offer` → freight-exchange
- `vehicle-capacity-offer` → freight-exchange
- `carrier-profile` → network-trust
- `shipper-organization` → platform-foundation
- `tracking-event-stream` → visibility
- `eta-prediction` → visibility
- `dock-slot-booking` → site-logistics
- `freight-invoice` → settlement
- `payment-guarantee-case` → network-trust
- `network-trust-score` → network-trust
- `transport-document` → transport-execution
- `lane-rate-benchmark` → analytics
- `emissions-record` → analytics
- `location-master` → integration-and-data

## Teams (teams.json) — every brick owned by exactly one team

Org group "Shipper Product Group":
- `transport-planning` (stream-aligned) owns tord, plan, csel
- `freight-procurement` (stream-aligned) owns tndr, rate

Org group "Network Product Group":
- `freight-exchange` (stream-aligned) owns fxch, mtch
- `carrier-experience` (stream-aligned) owns cprt
- `network-trust` (complicated-subsystem) owns cvet, trst, pgar

Org group "Execution Group":
- `transport-execution` (stream-aligned) owns texe, edoc
- `connectivity` (platform) owns conn
- `visibility` (stream-aligned) owns trck, excp
- `site-logistics` (stream-aligned) owns dock

Org group "Commercial and Insight Group":
- `settlement` (stream-aligned) owns cost, audt
- `analytics` (stream-aligned) owns anly, co2e

Org group "Platform Group":
- `platform-foundation` (platform) owns iden, notf, bill
- `integration-and-data` (platform) owns intg, mdat

## Products (product-deployments/products.json) — id, primary customers

- `enterprise-tms` — Enterprise TMS (Alpega TMS-like) — tdir, tpln
- `transport-execution` — Transport Execution (API-first, connects shipper ERP/TMS to carrier network; relaunched from "Connected" Jan 2026) — tpln, cdsp
- `freight-procurement` — Freight Procurement (TenderEasy-like) — tdir
- `freight-exchange` — Freight Exchange (Teleroute/Wtransnet/Bursa Transport-like) — cdsp, ownr, fwdr
- `carrier-companion` — Carrier Portal and Mobile App — cdsp, ownr
- `dock-scheduler` — Dock Scheduling — dksm, tpln
- `network-analytics` — Network Analytics and Benchmarking — tdir

## Deployment channels (deployment.json; maas is the structural reference)

Channel groups: "Web Applications" (shipper TMS web, procurement web, freight exchange web, carrier portal web, dock scheduling web), "Mobile Apps" (carrier mobile app), "APIs and Integrations" (public REST API, EDI gateway, telematics gateway), "Internal Operations" (network admin and support backoffice). Map deployedBricks with usedInProducts referencing product ids above.

## Sourced company facts (reuse consistently; do not invent numbers)

- Network: 80,000+ carriers, 80 countries; hundreds of thousands of freight transactions/offers daily (alpegagroup.com).
- Alpega TMS: Challenger, Gartner Magic Quadrant for TMS 2026.
- Transport Execution: relaunch of "Connected", January 2026; modular, API-driven; scales to thousands of loads per day.
- Freight exchange brands: Teleroute, Wtransnet, Bursa Transport.
- Reference shipper customers: Heineken, Asahi UK, Höganäs, Barry Callebaut.
