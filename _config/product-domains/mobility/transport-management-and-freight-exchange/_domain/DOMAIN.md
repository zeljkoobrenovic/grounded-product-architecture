# Transport Management and Freight Exchange

This product domain models the business operated by Alpega Group (alpegagroup.com): a European transportation-software company that combines enterprise SaaS for shippers with a pan-European carrier network and freight exchanges. It is an unusual and instructive combination of **enterprise SaaS + marketplace/network + transactional data platform**.

## Domain boundary

**Core scope.** The software and network a large shipper needs to run the full road-freight lifecycle — *Plan → Procure → Execute → Track → Settle → Analyse* — plus the carrier-side products that give trucking companies freight, capacity utilization, trust, and payment security:

- Transportation management for enterprise shippers (planning, carrier selection, transport orders, execution, costs, analytics) — modeled on **Alpega TMS**, positioned as a Challenger in Gartner's 2026 Magic Quadrant for Transportation Management Systems.
- Freight procurement and tendering (RFPs/RFQs, rate comparison, capacity negotiation) — modeled on **TenderEasy**.
- API-driven transport execution that connects a shipper's existing TMS/ERP/planning system directly to the carrier network at thousands of loads per day — modeled on **Alpega Transport Execution** (the relaunch of "Connected", January 2026).
- Freight exchanges matching spot freight with available truck capacity across Europe — modeled on **Teleroute, Wtransnet, and Bursa Transport**, a network of 80,000+ carriers across 80 countries with hundreds of thousands of freight transactions and offers daily.
- Dock scheduling, real-time visibility, freight settlement (self-billing, freight audit, payment guarantees), and network analytics including emissions reporting.

**Adjacent scope (modeled lightly).** ERP/telematics integration, carrier vetting and fraud prevention, CO2/CSRD reporting, market rate benchmarking.

**Explicitly excluded.** The platform operator does not move freight: no owned trucks, no brokerage margin on loads, no freight forwarding, no warehousing operations, no ocean/air modes as primary scope, no last-mile parcel delivery. This distinguishes the domain from `freight-logistics-orchestration`, which models US-centric managed transportation and digital brokerage businesses (Uber Freight, C.H. Robinson) that take principal/brokerage positions on freight. Here the business is software subscriptions, network memberships, transaction services, and data products.

## Value exchange

- **Enterprise shippers** (manufacturers, FMCG, automotive, chemicals, pharma, retail — reference customers include Heineken, Asahi UK, Höganäs, Barry Callebaut) pay SaaS subscriptions for TMS, procurement, execution, visibility, and dock scheduling; they get transport cost control, capacity coverage, and service reliability.
- **Carriers and logistics providers** pay exchange memberships and service fees; they get freight demand, fewer empty kilometers, payment security, and direct digital access to enterprise shipper contracts.
- **The network effect is the strategic asset**: more shipper freight attracts more carrier capacity; more capacity improves coverage, price discovery, and execution reliability for shippers; the transaction flow feeds data products (rate benchmarks, ETAs, trust scores, emissions) that deepen the moat.

## Strategic spine (1/3/5-year horizons)

- **Year 1 — Connected execution and trusted liquidity.** Scale the API-driven execution product inside enterprise accounts (shipper systems wired straight into the carrier network), harden network trust (carrier vetting, fraud prevention, payment guarantees) on the exchanges.
- **Year 3 — Full-lifecycle attach.** Expand each shipper account from a single entry product to the whole Plan→Settle lifecycle; make settlement and freight audit a standard attach; monetize data products (lane benchmarks, ETA, CO2 reporting).
- **Year 5 — Network-level optimization.** Move from digitizing single-shipper workflows to optimizing across the network: predictive capacity, continuous procurement, automated spot-contract arbitrage, pan-European settlement rails.

## Research notes

- Sourced facts (network scale, product launches, analyst positioning, customer names) come from alpegagroup.com and its press releases; competition statistics preserve each company's officially reported scope.
- KPI current/target values are realistic seed values for a modeled domain, informed by public European road-freight reporting (Eurostat empty-running shares, IRU driver-shortage reports, cargo-crime statistics), not official Alpega targets.

Structural references used while creating this domain: `ride-sharing-marketplace` (customers, bricks, streams, data assets, competition), `maas` (teams, products, deployment), `freight-logistics-orchestration` (adjacent-domain boundary, icon set).
