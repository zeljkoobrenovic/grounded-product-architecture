# Real Estate ERP Platform

This product domain models the business operated by **Bloxs** (vortexcp.com/investment/bloxs/, bloxs.com): a Utrecht-based PropTech company founded in 2015 that sells ERP software for real estate investment and property management organisations. Vortex Capital Partners became majority shareholder in a 2024 buyout and backs a Dutch and international buy-and-build strategy; the first add-on was **Informant Software** (Wateringen, founded 1990/1991, acquired 7 July 2025), a 35-year-old property-management and owners'-association (VvE) software house whose customers migrate to Bloxs at no cost while Informant support runs until 31 December 2027. It is an instructive example of **vertical ERP SaaS for an asset-heavy trade** — one integrated system of record for objects, contracts, money and maintenance, with automation robots and stakeholder portals hanging off it.

> Research note on the brief. The request named both `blox.global/en` and the Vortex Bloxs page. At research time `blox.global` presented an unrelated digital-asset payments company ("the financial operating system for digital assets"), while every Vortex, press and review source describes Bloxs as Dutch real estate ERP software. The domain is modeled on the Vortex portfolio company Bloxs; nothing from the crypto site was used.

## Domain boundary

**Core scope.** Everything a real estate organisation needs to run the lifecycle *Portfolio → Let → Contract → Collect → Maintain → Account → Report → Serve* on one integrated system, following Bloxs' eight modules:

- **Relations** (Relaties) — one contact database for tenants, owners, investors, suppliers, brokers and accountants, with correspondence and documents.
- **Objects and projects** (Objecten, Projecten) — portfolios, complexes, buildings and rental units of every type (residential, commercial, retail, logistics, healthcare, parking), valuations and market data, and the financial management of new-build, renovation and transformation projects.
- **Letting and contracts** (Contracten) — vacancy and letting, candidate screening and rent-price compliance checks (Huurprijscheck.app partnership), lease contracts captured once and signed digitally, automated rent indexation, service charge calculations and settlements, special terms and break options.
- **Financial** (Financieel) — a real estate accounting platform: periodic rent invoicing runs, direct debit and bank reconciliation, debtor management and dunning, accounts payable and supplier invoices, VAT, multi-organisation and multi-entity general ledger, period close and consolidation.
- **Technical management** (Techniek) — fault reports and tickets, work orders and supplier dispatch (Ziezodan and Proprli partnerships), installation registers with automatic supplier reminders for periodic maintenance, multi-year maintenance plans and budgets.
- **Owners' associations** (VvE) — the Informant heritage: association budgets, owner contributions and reserve funds, meetings, decisions and owner communication.
- **Reporting** (Rapportages) — standard real-estate reports customised per employee, interactive dashboards and data analytics, investor and owner reporting.
- **Portals** (Portalen) — branded tenant, owner and maintenance-partner portals and apps with real-time information.
- **Foundation** — hyper automation (AI and robotics that fully process repetitive financial tasks), an open standardised API with an API Platform add-on module and certified integrations (accounting, banking, BI tools such as Power BI, e-mail such as Gmail and Outlook), identity, tenants and workflow, and migration tooling for acquired products.

**Adjacent scope (modeled lightly).** AI assistants for document drafting, invoice coding and inbox triage; market analysis and financial forecasting; German-market localisation; integration of acquired products under the buy-and-build strategy.

**Explicitly excluded.** The platform operator owns no property and takes no rent: no brokerage marketplace, no consumer listings portal, no mortgage or investment fund products, no facility-services workforce. This distinguishes the domain from `real-estate-marketplace` (consumer listings) and `hosted-stays-marketplace` (short-stay bookings). Here the business is software subscriptions per organisation, add-on modules (portals, API Platform, projects, VvE), implementation, data migration, training and unlimited support.

## Value exchange

- **Real estate investors and asset managers** (reference customers include Rockfield, Urban Interest, Burgstate, Dunavast) and **property management and VvE firms** (FIT Vastgoedbeheer, Ruijters, CRMD Vastgoed Management, plus the Informant base of property managers, owners and association administrators) pay a subscription that scales with modules and portfolio size; published review directories describe customers managing 50 to 20,000 units. They get one system of record from object to bank statement, fewer manual errors in complex processes such as indexation and service charge settlement, reporting that no longer costs days, and scalable operations — one testimonial reports 100% time savings on repetitive financial processes through hyper automation.
- **Tenants, private owners and maintenance suppliers** use the portals for free; the organisation pays. Their self-service reduces handling time and errors on both sides.
- **The strategic asset** is the integrated real estate data model: every object, unit, contact, contract, invoice, bank line, ticket and work order lives in one place, which makes portals, robots, AI assistance, dashboards and investor reporting compound rather than bolt on. Published scale: 5,000+ users, 450,000+ rental units (Vortex: more than 500,000 rented properties), about €4 billion of annual rent invoiced and roughly €70 billion of property value managed, with about 35 employees before the Informant acquisition.

## Strategic spine (1/3/5-year horizons)

- **Year 1 — One platform, migrated base.** Bring Informant customers onto Bloxs without losing trusted service (phased migration, free of charge, Informant support until end 2027), extend VvE administration, deepen technical and financial hyper automation, and professionalise onboarding, support and the sales organisation under the new CEO.
- **Year 3 — The real estate ERP standard for the Netherlands and a foothold in Germany.** A modular platform with a certified-integration marketplace, portals and API Platform as standard attach, German localisation (accounting, VAT, tenancy law), and selective acquisitions that add segments, geography or capabilities.
- **Year 5 — European scale and autonomous administration.** Multi-country operation, AI agents that run routine administration (invoice coding, reconciliation, ticket triage, indexation letters) under human supervision, and data products (rent benchmarks, maintenance forecasts, portfolio market analysis) that make the platform the trade's operating system.

## Research notes

- Sourced facts (founding year, headcount, transaction dates, leadership, named customers, module list, partner integrations, user and unit counts, rent invoiced and property value managed, Informant acquisition terms) come from vortexcp.com, bloxs.com, informant.nl, press coverage (vastgoedjournaal.nl, propertynl.com, mena.nl, springfinance.com) and software review directories (Capterra, GetApp). Competition statistics preserve each company's officially reported scope.
- Leadership: André Proost CEO since 1 May 2025 (previously CompuGroup Medical and Centric); founder Dennis Gubbels remains board member, shareholder and M&A director; Joost Moerland is the Vortex partner.
- KPI current/target values are realistic seed values for a modeled domain, informed by public Dutch real estate reporting (CBS housing statistics, Huurcommissie rent rules, Vastgoedmanagement Nederland benchmarks), not official Bloxs targets.

Structural references used while creating this domain: `ride-sharing-marketplace` (customers, bricks, streams, data assets, competition), `maas` (teams, products, deployment), `tour-operator-erp-platform` (ID spine approach, vertical-ERP shape, relations, residuality).
