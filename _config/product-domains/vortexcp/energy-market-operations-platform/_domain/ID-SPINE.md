# ID Spine — energy-market-operations-platform

Authoritative ID contract for this domain. Every artifact file MUST use exactly these
IDs when referencing entities owned by another file. Names/descriptions here are
one-liners; the artifact author expands them to reference-domain density.
All ids lowercase. Modeled on Eneve (Energy21 + Ecedo + Jules + Gridhub + Nemon, Vortex-backed; see DOMAIN.md).

## Customer groups and customers (customers.json)

Group "Energy Suppliers" — retail energy companies serving households and businesses (Eneve reference customers: Eneco, Essent, Engie, Vattenfall, Mega, Vandebron, Scholt Energie, Pure Energie, PZEM; Barcelona Energia and ~100 Iberian suppliers via Nemon):
- `prop` — Proposition and Pricing Manager. Designs and launches energy products and tariffs (fixed, variable, dynamic spot, EV time-of-use, battery, capacity-linked, bundled), configures pricing logic, campaigns and sales-channel availability; judged on time to launch and campaign conversion.
- `bilo` — Billing and Operations Manager. Runs order-to-cash: intake and switching through market communication, contract and connection register, meter data, billing runs, VAT, guarantees of origin, reconciliation, corrections, exceptions, payments and dunning; judged on straight-through billing and cost to serve.
- `csrv` — Customer Service Lead. Owns the customer lifecycle and touchpoints: white-label portal and app, queries, disputes, service requests, onboarding communication, regulatory disclosures, retention; judged on self-service resolution and contact rate.

Group "Balancing, Trading and Portfolio Operators" — BRPs, traders, shippers and supplier portfolio desks (reference: Axpo, TotalEnergies, EBN gas shipping, Pure Energie, Vattenfall):
- `port` — Portfolio and Trading Manager. Sources and hedges the portfolio, maintains price curves and cost-plus pricing, tracks positions, volumes, value and risk per segment, structures the portfolio, and prices B2B deals.
- `brpo` — BRP and Balancing Operator. Forecasts day-ahead, intraday and ex-post, nominates and re-nominates to TenneT and gas TSOs, steers intraday via ETPA and flex assets, manages allocation, reconciliation, imbalance and settlement under Allocation 2.0.

Group "Large Consumers and Producers" — industrial sites and renewable producers who trade and manage energy through their supplier's platform (reference: BASF, USG Chemelot, wind and solar producers):
- `indm` — Industrial Energy Manager. Manages multi-site supply contracts, consumption analysis and forecasts, executes click trades within a framework contract, and monetises flexible assets (batteries, CHP, curtailable load).

Group "Energy Company Leadership and Market Entrants" — the buyers of the platform and services:
- `exec` — Energy Company Director. COO/CFO/director of a supplier or portfolio operator; buys the platform; cares about gross margin per connection, cost to serve, compliance, time to market and platform consolidation risk.
- `newe` — New Market Entrant Lead. Founder or expansion lead launching a supplier or BRP in the Netherlands or Spain: market-entry scan, ACM/CNMC licensing, operating model, BRP as a Service, go-live in months.

Group "End Energy Customers" — the households and businesses served through the white-label portal:
- `endc` — Household or Business Energy Customer. Signs up, switches or moves in, reads invoices and consumption, submits meter readings, changes tariff or payment method, raises disputes; expects a correct bill and self-service without calling.

### JTBD ids (customers.json jobsToBeDone; insights link jobIds to these)
- prop: `jtbd-prop-1` Launch a new energy proposition in weeks, not months, `jtbd-prop-2` Price every product profitably against market and portfolio cost, `jtbd-prop-3` Run campaigns and channels that convert without operational surprises.
- bilo: `jtbd-bilo-1` Onboard and switch every customer through market communication without manual work, `jtbd-bilo-2` Bill every connection correctly and on time, `jtbd-bilo-3` Reconcile volumes, corrections and cash with minimal exceptions.
- csrv: `jtbd-csrv-1` Let customers serve themselves on the same data as billing, `jtbd-csrv-2` Resolve queries and disputes fast with full context, `jtbd-csrv-3` Keep customers informed and retained through every lifecycle event.
- port: `jtbd-port-1` Source and hedge the portfolio at the right cost and risk, `jtbd-port-2` See positions, volumes and value per segment every 15 minutes, `jtbd-port-3` Price and structure B2B deals from the portfolio position.
- brpo: `jtbd-brpo-1` Forecast and nominate the portfolio accurately and on time, `jtbd-brpo-2` Steer intraday to minimise imbalance cost, `jtbd-brpo-3` Settle allocation, reconciliation and imbalance without disputes.
- indm: `jtbd-indm-1` Understand and forecast energy consumption per site, `jtbd-indm-2` Execute trades and contract changes myself within my framework, `jtbd-indm-3` Monetise flexible assets without operational risk.
- exec: `jtbd-exec-1` Grow margin per connection while cutting cost to serve, `jtbd-exec-2` Stay compliant with every market and regulatory change, `jtbd-exec-3` Consolidate operations on one platform without disruption.
- newe: `jtbd-newe-1` Decide whether and how to enter the market, `jtbd-newe-2` Obtain licences and market roles on a realistic timeline, `jtbd-newe-3` Go live with customers and balance responsibility in months.
- endc: `jtbd-endc-1` Switch or move in without hassle, `jtbd-endc-2` Understand and trust my bill and consumption, `jtbd-endc-3` Manage my contract, payments and requests myself.

### North-star KPI names (use these VERBATIM as pyramid node names; productStrategy northStar must match)
- prop: north star "Time to launch a new proposition"; supporting include "Propositions launched per quarter", "Campaign conversion rate".
- bilo: north star "Straight-through billing rate"; supporting include "Invoice correction rate", "Cost to serve per connection".
- csrv: north star "Self-service resolution rate"; supporting include "Customer contact rate per connection", "Customer satisfaction score".
- port: north star "Portfolio gross margin per MWh"; supporting include "Hedge coverage ratio", "Forecast accuracy".
- brpo: north star "Imbalance cost per MWh"; supporting include "Nomination timeliness rate", "Allocation reconciliation accuracy".
- indm: north star "Energy cost per unit of production"; supporting include "Forecast deviation rate", "Flexibility revenue captured".
- exec: north star "Gross margin per connection"; supporting include "Cost to serve per connection", "Regulatory compliance incident rate".
- newe: north star "Time to first live customer"; supporting include "Licensing lead time", "Setup cost per market".
- endc: north star "Bill accuracy rate"; supporting include "Self-service task completion rate", "Time to switch or move in".

KPI node id convention (mirrors real-estate-erp-platform): `co-<cust>-top`, `co-<cust>-b1`, `co-<cust>-b1-c1`, `co-<cust>-b1-c1-l1` … and `bo-<cust>-…` for businessOutcomes. Every non-leaf has ≥2 children; target 4 levels (1+2+4+8). Set `icon` fields as `kpi-<cust>-<nodeid>.png`; icon files are backfilled later.
Customer icons: use `<cust>.png` (e.g. `prop.png`) — backfilled later. Do NOT set `media` fields on JTBDs/journeys (no images exist).

## Streams (product-stream.json; JTBD steps reference via streamsNeeded — use these ids only)

- `launch-energy-propositions-and-tariffs` — From idea to live product: low-code configuration of products, tariffs, pricing logic, journeys, campaigns and sales-channel availability, plugged into billing automatically.
- `onboard-and-switch-customers` — From sign-up to active supply: intake, identity and credit check, contract creation, switch or move-in via market communication (EDSN in NL, SIPS/ATR in Iberia), activation and welcome.
- `collect-and-validate-meter-data` — From smart meters, telemetry and clustered data to validated, estimated and plausibility-checked volumes per connection and interval.
- `bill-and-reconcile-customers` — From validated volumes and contracts to invoices: billing runs, VAT, guarantees of origin, split invoicing, annual and final settlements, reconciliation and corrections.
- `collect-payments-and-manage-debtors` — From invoice to cash: direct debit, payment matching, payment plans, dunning, disconnection prevention and credit management.
- `serve-customers-through-portal-and-care` — From portal account to resolved request: invoice and consumption insight, meter readings, tariff and payment changes, queries, disputes and communication on the operational backbone.
- `source-and-price-the-portfolio` — From demand forecast to procured energy: hedging strategy, procurement, price curves, cost-plus pricing, portfolio structuring and margin tracking.
- `forecast-and-nominate-the-portfolio` — From portfolio data to TSO nominations: day-ahead, intraday and ex-post forecasting, position management, nominations and re-nominations for electricity and gas.
- `steer-intraday-and-optimise-imbalance` — From near real-time position to action: intraday steering signals, ETPA trading cycle, flex-asset steering, ex-post trading opportunities.
- `settle-allocate-and-reconcile-market-volumes` — From market messages to settled volumes: allocation, reconciliation (Allocation 2.0), imbalance settlement, TenneT MMC-Hub exchange, BRP compliance reporting.
- `trade-and-manage-customer-energy-contracts` — From framework contract to executed click trades: B2B customer trading desk, forecast management, consumption analysis and flexible-asset monetisation for large consumers and producers.
- `enter-and-operate-in-a-new-energy-market` — From market-entry scan to live operations: regulatory scan, licensing (ACM, CNMC), operating model, BRP as a Service onboarding, implementation, academy training.
- `integrate-market-communication-and-external-systems` — From connectors to a compliant, integrated operation: EDSN, C-AR, TenneT, ETPA, OMIE, REE/SIPS, ERP and accounting, payment providers, meter-data providers, open API.

13 streams. Stream icons: `<stream-id>.png` in product-bricks/icons (backfilled later).

## Product bricks (product-bricks.json) — root group → subgroup → bricks

Root "Supplier Suite":
- Subgroup "Products and Pricing": `prod` Proposition and Tariff Builder, `camp` Campaign and Sales Channel Management, `quot` B2B Quoting and Cost-Plus Pricing.
- Subgroup "Customer Onboarding": `intk` Intake, Credit Check and Activation, `swch` Switching and Move-In Market Processes.
- Subgroup "Contract and Billing": `cntr` Contracts and Connections Register, `bill` Billing Runs and Invoicing, `recn` Billing Reconciliation and Corrections, `paym` Payments, Direct Debit and Debtor Management.
- Subgroup "Customer Interfacing": `port` White-Label Customer Portal and App, `care` Customer Service Case Management, `comm` Customer Communication and Documents.

Root "Balancing and Shipping Suite":
- Subgroup "Meter Data and Allocation": `mdat` Meter Data Collection and Validation, `allo` Allocation and Reconciliation.
- Subgroup "Forecasting and Nomination": `fcst` Portfolio Forecasting, `nomi` Nominations and Position Management.
- Subgroup "Intraday and Settlement": `intr` Intraday Steering and Flex Signals, `imbs` Imbalance Settlement and BRP Compliance, `gass` Gas Shipping and Trading.

Root "Trade and Portfolio Suite":
- Subgroup "Sourcing and Portfolio": `srcg` Sourcing, Hedging and Procurement, `pric` Price Curves and Market Data, `risk` Portfolio Position and Risk Analytics.
- Subgroup "Customer Trading": `ctrd` Customer Trading Desk and Click Contracts, `cons` Consumption Analysis and Forecast Self-Service.

Root "Market and Data Foundation":
- Subgroup "Market Communication": `mcom` Dutch Market Messaging Hub, `imcm` Iberian Market Communication.
- Subgroup "Data and Insight": `dash` Operational Dashboards and Analytics, `regs` Regulatory Reporting and Compliance.
- Subgroup "Platform Core": `iden` Identity, Tenants and Brand Isolation, `wflw` Workflow, Exceptions and Notifications, `apip` Open API and Integration Connectors, `migr` Migration and Platform Consolidation Tooling.

32 bricks. Module ids must start with `module-` (e.g. `module-bill-web`, `module-bill-api`). Brick icons `<brick-id>.png` backfilled later.

### Brick dataDependencies → data asset ids (see below); wire at least these
prod→energy-product-and-tariff,price-curve; camp→campaign,energy-product-and-tariff; quot→b2b-quote,price-curve,consumption-profile; intk→customer-account,connection-point,supply-contract; swch→switch-request,connection-point,market-message; cntr→supply-contract,connection-point,customer-account; bill→invoice,supply-contract,meter-reading; recn→billing-correction,invoice,allocation-volume; paym→payment-transaction,debtor-case,invoice; port→portal-account,invoice,meter-reading; care→service-case,customer-account; comm→customer-communication,customer-account; mdat→meter-reading,connection-point; allo→allocation-volume,reconciliation-volume,meter-reading; fcst→portfolio-forecast,consumption-profile; nomi→nomination,portfolio-forecast,portfolio-position; intr→intraday-position,steering-signal; imbs→imbalance-settlement,allocation-volume,nomination; gass→nomination,portfolio-position; srcg→hedge-transaction,portfolio-position; pric→price-curve; risk→portfolio-position,hedge-transaction,price-curve; ctrd→customer-trade,supply-contract,price-curve; cons→consumption-profile,meter-reading; mcom→market-message,connection-point; imcm→market-message,connection-point; dash→analytics-dataset; regs→regulatory-report,analytics-dataset; iden→tenant-organization,portal-account; wflw→workflow-task; apip→integration-connection; migr→tenant-organization,customer-account.

## Data assets (data/data-assets.json) — id → ownerTeamId

- `energy-product-and-tariff` → products-and-pricing
- `campaign` → products-and-pricing
- `b2b-quote` → products-and-pricing
- `customer-account` → customer-onboarding
- `connection-point` → customer-onboarding
- `switch-request` → customer-onboarding
- `supply-contract` → contract-and-billing
- `invoice` → contract-and-billing
- `billing-correction` → contract-and-billing
- `payment-transaction` → contract-and-billing
- `debtor-case` → contract-and-billing
- `portal-account` → customer-interfacing (system of record brick: `port`; `iden` only authenticates)
- `service-case` → customer-interfacing
- `customer-communication` → customer-interfacing
- `meter-reading` → meter-data-and-allocation
- `allocation-volume` → meter-data-and-allocation
- `reconciliation-volume` → meter-data-and-allocation
- `portfolio-forecast` → forecasting-and-nomination
- `nomination` → forecasting-and-nomination
- `intraday-position` → intraday-and-settlement
- `steering-signal` → intraday-and-settlement
- `imbalance-settlement` → intraday-and-settlement
- `hedge-transaction` → sourcing-and-portfolio
- `price-curve` → sourcing-and-portfolio
- `portfolio-position` → sourcing-and-portfolio
- `customer-trade` → customer-trading
- `consumption-profile` → customer-trading
- `market-message` → market-communication
- `regulatory-report` → data-and-insight
- `analytics-dataset` → data-and-insight
- `tenant-organization` → platform-core
- `workflow-task` → platform-core
- `integration-connection` → integration-hub

33 assets.

## Teams (teams.json) — every brick owned by exactly one team

Eneve has about 180 people (post-Nemon, 2026) across the Netherlands, Spain, Portugal, the UK and Paraguay; model 15 teams of 5–14 people. Every brick exactly once.

Org group "Supplier Suite Group":
- `products-and-pricing` (stream-aligned) owns prod, camp, quot
- `customer-onboarding` (stream-aligned) owns intk, swch
- `contract-and-billing` (stream-aligned) owns cntr, bill, recn, paym
- `customer-interfacing` (stream-aligned) owns port, care, comm

Org group "Balancing and Shipping Group":
- `meter-data-and-allocation` (complicated-subsystem) owns mdat, allo
- `forecasting-and-nomination` (stream-aligned) owns fcst, nomi
- `intraday-and-settlement` (stream-aligned) owns intr, imbs, gass

Org group "Trade and Portfolio Group":
- `sourcing-and-portfolio` (stream-aligned) owns srcg, pric, risk
- `customer-trading` (stream-aligned) owns ctrd, cons

Org group "Market and Platform Group":
- `market-communication` (complicated-subsystem) owns mcom, imcm
- `data-and-insight` (stream-aligned) owns dash, regs
- `platform-core` (platform) owns iden, wflw, migr
- `integration-hub` (platform) owns apip

Org group "Expertise Services Group":
- `market-enablement-and-brp-services` (enabling) owns no bricks; runs BRP as a Service operations desk, market-entry scans, ACM/CNMC licensing support; customer dependencies on newe, brpo, exec, port
- `customer-success-and-academy` (enabling) owns no bricks; implementation, migration of heritage-product customers, Eneve Academy training, ongoing support; customer dependencies on bilo, csrv, exec, prop

15 teams.

## Products (product-deployments/products.json) — id, primary customers

- `supplier-suite` — Supplier Suite (Customer Onboarding, Contract & Billing, Customer Interfacing, Sourcing & Pricing) — bilo, csrv, prop, exec
- `proposition-launch-studio` — Proposition Launch Studio (low-code product, tariff, journey and campaign builder) — prop, exec
- `customer-self-service-portal` — White-Label Customer Portal and App — endc, csrv
- `balancing-and-shipping-suite` — Balancing & Shipping Suite (EBASE heritage: meter data, allocation, forecasting, nominations, settlement) — brpo, port
- `brp-as-a-service` — BRP as a Service (managed balance responsibility) — newe, exec, brpo
- `trade-and-portfolio-suite` — Trade & Portfolio Suite (sourcing, pricing, risk, customer trading) — port, indm
- `iberia-supplier-platform` — Nemon Trade Energy for Spain and Portugal (Trade Energy, CRM, SIPS) — bilo, prop, csrv
- `market-entry-and-expertise-services` — Market Entry Scan, Licensing Support, Academy and Customer Services — newe, exec
- `open-api-and-integrations` — Open API and Integration Connectors — bilo, brpo, exec

9 products. Product icons: `<product-id>.png` in product-deployments/icons (backfilled later).

## Deployment channels (deployment.json; maas is the structural reference)

Channel groups: "Web Applications" (supplier back-office web app, white-label customer portal web, portfolio and trading workspace, BRP operations dashboard, Iberian supplier back office), "Mobile Apps" (white-label customer app iOS/Android), "APIs and Integrations" (open REST API, Dutch market messaging connectors EDSN/C-AR/MMC-Hub, TenneT and gas TSO nomination interfaces, ETPA intraday trading, Iberian market connectors OMIE/REE/SIPS/distributors, ERP and accounting connectors, payment and direct-debit providers, smart-meter and telemetry data providers, price and weather data feeds), "Automation Runtime" (billing batch engine, forecasting and steering engines, intraday guaranteed cycle, market-message processors), "Internal Operations" (BRP-as-a-service operations desk, tenant administration, migration and support back office). Map deployedBricks with usedInProducts referencing product ids above.

## Sourced company facts (reuse consistently; do not invent numbers)

- Eneve, headquartered in the Netherlands (Utrecht heritage of Energy21), offices in Spain, Portugal, the UK and Paraguay; ~180 employees after Nemon (2026); earlier 130+ specialists at the June 2025 merger; expected turnover EUR 25M+ (2025) and over EUR 30M after Nemon.
- Timeline: 1997 Energy21 founded as GEN; 2002 EBASE launched for BRP market messages; 2003 Ecedo founded (full SaaS platform 2013); 2010/2011 Jules founded (Loughborough); 2022 Vortex Capital Partners partnership/buyout of Energy21; 2023 Gridhub founded, Ecedo and Jules join Energy21; 2024 Gridhub joins; 10 Sep 2024 EBN signs gas trading and shipping agreement; 18 Mar 2025 Pure Energie collaboration; 18 Jun 2025 Energy21, Ecedo, Jules and Gridhub become Eneve; 30 Mar 2026 Nemon acquired.
- Scale claims: "50+ Energy Companies" / "more than 100 energy suppliers" (with Iberia); "20 Million Connections" daily; largest implementation more than 25 million connections; validates over 90% of Dutch energy consumption data; "28 Years of Experience"; Dutch supplier clients serve 7M+ households and 3M+ business customers.
- Named customers: Eneco, Essent, Engie, Vattenfall, Mega, Vandebron, Scholt Energie, Pure Energie, PZEM, EBN, Axpo, TotalEnergies, BASF, USG-Chemelot, Barcelona Energia (Nemon).
- BRP as a Service claims: up to 53% reduction in imbalance costs; day-ahead, intraday and ex-post forecasting; TenneT nominations/re-nominations; ETPA integration run as a guaranteed cycle; all EAN types incl. BSP and flex assets; from 40 GWh portfolio; tiered MWh pricing; 15-minute financial insight per segment.
- Market-entry scan: five workstreams, 5 weeks; ACM licensing 8–14 weeks, CNMC 12–20 weeks, dual 16–20 weeks; "most new entrants underestimate the ACM and CNMC licensing ramp by six months or more".
- Dutch market 2025: Allocation 2.0 tranche 3 (1 Jan 2025) reconciliation for SMA/TMT connections via TenneT MMC-Hub; day-ahead market to 15-minute blocks (30 Sep 2025); aFRR 0.1 MW setpoints and 4-hour capacity auctions (11 Nov 2025).
- Leadership: Michiel Kuiper CEO; Gaston Hendriks founder; Teun Levering Managing Director Software (June 2025); Atilano Villanueva MD Nemon; Nemon founders Nàdia Contreras Jordà and Ivan Solé Martinez. Vortex: buyout 2022, software & services, current investment.
- Taglines/quotes: "Energy software and expertise services, built for Europe"; "From idea to live product. In weeks."; "Eighteen months to launch a new product is eighteen months for competitors to land first"; Kuiper: "Our mission is to make the energy chain manageable and future-proof"; "This step allows us to expand internationally and support energy suppliers more broadly in managing risk."
