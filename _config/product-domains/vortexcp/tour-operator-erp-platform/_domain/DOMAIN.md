# Tour Operator ERP Platform

This product domain models the business operated by the combined **1TIS + TravelSpirit** group (vortexcp.com/investment/1tis-travelspirit/): two Dutch travel-software companies brought together by Vortex Capital Partners in May 2026 to build a market-leading ERP platform for the travel industry. It is an instructive example of **vertical ERP SaaS for a mid-market trade** — a modular front-, mid- and back-office system for travel organisations, plus the customer-, supplier- and partner-facing portals that hang off it.

## Domain boundary

**Core scope.** Everything a travel organisation needs to run the trade lifecycle *Product → Sell → Book → Operate → Serve → Settle → Steer* on one integrated system:

- **Travel product and supply management** — packages, departures and series, individual components (accommodation, transport, activities), inventory and availability, purchasing and supplier contracts, pricing, yielding and group calculations, travel content and photo management (1TIS Product Management, TravelSpirit travel plans/products and MediaSpirit).
- **Selling and booking** — CRM, visual tour building and customised online quotes for tailor-made travel (TravelSpirit Visual Tour Builder), booking files/dossiers, real-time bookable customer websites fully integrated with the back office (1TIS Klantwebsite, TravelSpirit SPoE/Single Point of Entry), reseller and agent portals, flight imports and settlement (GDS, Airtrade).
- **Group travel operations** — the 1TIS speciality: bus seat allocation and seating lists for drivers, hotel room lists with guest wishes and dietary requirements, tour-guide and group-leader portals with participant lists, one-to-one data exchange with DMCs and direct suppliers, supplier approval portals.
- **Traveler service** — travel documents, itineraries, personal "my trip" portals where travelers approve quotes, pay and download documents, partner mobile apps (Travelia, Appit), eSIM (Hubby), complaint handling, surveys and reviews (Trustpilot).
- **Finance and compliance** — invoicing, payment links and alerts (Mollie), accounts payable/receivable, accounting integrations (Exact), electronic invoicing, IATA/Airtrade settlement files, travel-guarantee-fund and package-travel-regulation compliance.
- **Marketing, workflow and insight** — email marketing and segmentation (Spotler), workflow automation, task lists and alerts, email and telephony integration (WeCloudIT), business intelligence (Travel Intelligence).

**Adjacent scope (modeled lightly).** AI assistance for proposal drafting and inbox triage (the Vortex thesis explicitly includes embedding AI), process-optimisation advisory alongside the software (TravelSpirit's model), partner ecosystem integrations, multi-currency and multi-language support.

**Explicitly excluded.** The platform operator does not sell travel: no own tour packages, no bed bank or GDS content ownership, no consumer marketplace, no airline/hotel inventory. This distinguishes the domain from `travel-accommodations-marketplace` (consumer stay marketplace) and `travel-and-expense-management` (corporate T&E). Here the business is software subscriptions per tenant, add-on modules, portals and websites, integrations, and advisory services.

## Value exchange

- **Travel organisations** — group and coach tour operators (1TIS reference customers include Djoser, Kras Busreizen, Oad, NRV, SRC Reizen, Shoestring/Koning Aap, Sawadee, ACSI, André Rieu Travel, Nordic, Live To Travel), tailor-made specialists and DMCs (TravelSpirit reference customers include Van Verre, Tenzing Travel, SNP Natuurreizen, S-Cape Travel, Matoke Tours, Pin High Golftravel), OTAs, MICE/B2B specialists, travel agencies and small travel entrepreneurs — pay a monthly subscription (1TIS publishes a €129/month base package, scaled with modular add-ons; TravelSpirit offers a start package for small operators and enterprise contracts for larger ones). They get one system of record from first lead to aftercare, fewer re-keying errors, faster quoting, scalable operations and compliant finance.
- **Travelers, resellers, suppliers, DMCs and guides** use the portals for free; the operator pays. Their self-service reduces the operator's handling time and errors.
- **The strategic asset** is the integrated data model: every product, contract, booking, passenger, payment and supplier request lives in one place, which makes portals, automation, AI assistance and BI compound rather than bolt on. Combined scale: 3,000+ daily users and roughly €1.5 billion in annual travel revenue processed, with about 40 employees.

## Strategic spine (1/3/5-year horizons)

- **Year 1 — One platform, two brands.** Keep both brands live while unifying the product roadmap: shared portals and integrations, AI assistance for quotes and inbox triage, professionalised onboarding and support. Prove that group-travel depth (1TIS) and tailor-made flexibility (TravelSpirit) can be sold to each other's customers.
- **Year 3 — The travel ERP standard for the Benelux trade.** A single-brand modular ERP with a partner marketplace of integrations, finance and compliance as a standard attach, and selective acquisitions that broaden the value proposition (payments, apps, BI, adjacent segments).
- **Year 5 — European scale and automated operations.** Multi-country expansion beyond the Netherlands and Belgium, AI agents that run routine operations (supplier requests, document generation, reconciliation) under human supervision, and data products (margin benchmarks, demand forecasts) that make the platform the trade's operating system.

## Research notes

- Sourced facts (user and revenue-processed figures, headcount, transaction date, leadership, named customers, module lists, integration partners, memberships, published base price) come from vortexcp.com, 1tis.nl, travelspirit.nl, livingstonepartners.com and software review directories; competition statistics preserve each company's officially reported scope.
- KPI current/target values are realistic seed values for a modeled domain, informed by public Dutch travel-trade reporting (ANVR, SGR, CBS holiday statistics, ACM/Package Travel Directive guidance), not official 1TIS or TravelSpirit targets.

Structural references used while creating this domain: `ride-sharing-marketplace` (customers, bricks, streams, data assets, competition), `maas` (teams, products, deployment), `transport-management-and-freight-exchange` (ID spine approach, relations).
