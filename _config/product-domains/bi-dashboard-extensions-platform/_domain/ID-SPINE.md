# ID Spine — bi-dashboard-extensions-platform

Authoritative ID contract for this domain. Every artifact file MUST use exactly these
IDs when referencing entities owned by another file. Names/descriptions here are
one-liners; the artifact author expands them to reference-domain density.
All ids lowercase. Modeled on Infotopics | Apps for Tableau (see DOMAIN.md).

## Customer groups and customers (customers.json)

Group "Dashboard Builders and BI Platform Teams" — the people who build dashboards and run the Tableau / Power BI platform inside a customer organisation (reference customers: Bank of America, Pfizer, Siemens, Johnson & Johnson, Post Holdings, Fraudio):
- `dcre` — Dashboard Creator. Tableau or Power BI developer / analytics engineer who builds dashboards for business teams; configures SuperTables, ShowMeMore, PowerKPIs, DashboardGuide and write-back forms; wants to satisfy Excel-minded users without building yet another bespoke dashboard.
- `bilr` — BI Platform Lead. Owns the Tableau Server / Cloud (or Power BI) tenant and the analytics centre of excellence: extension safelisting and governance, adoption, licence and seat management, vendor selection, renewals.

Group "Business Users and Decision Makers" — the people who consume dashboards inside the customer organisation:
- `bviw` — Business Dashboard Viewer. Excel-minded analyst or manager in finance, sales, operations or supply chain who pivots, groups, filters, drills down and exports data in a dashboard instead of asking for a new one.
- `plnr` — Planning and Finance Contributor. FP&A analyst, demand planner or budget owner who enters forecasts, budgets, targets, comments and corrections directly in the dashboard (WriteBackExtreme, InputTables, FinanceTables) instead of round-tripping spreadsheets.
- `exec` — Executive Report Recipient. Director or non-Tableau stakeholder who receives scheduled, personalised reports by email, Microsoft Teams or Slack (MailScheduler) and opens a KPI entry point (PowerKPIs) rather than exploring dashboards.

Group "IT, Security and Procurement" — the people who deploy, secure and approve the extensions:
- `itad` — IT Administrator. Installs and upgrades the Enterprise (self-hosted) extensions with ExtensionsManager on Windows or Linux, configures SSO, database connections, network access and license keys, replaces extension URLs with TrexReplacer, owns availability.
- `secr` — Security and Compliance Reviewer. Information security officer or vendor-risk analyst who assesses the vendor and the deployment: ISO 27001 evidence, penetration-test reports, data flows, on-premises isolation, audit trails, data processing agreements.

Group "Partners and Ecosystem" — the firms that resell, implement and co-market the extensions:
- `cpar` — Consulting and Reseller Partner. Tableau / Power BI consulting or reseller firm (Slalom, Biztory, USEReady, Big X Data and 28 others) that recommends, implements and resells extensions in its region and language; needs demo licences, enablement, deal registration and margin.

### JTBD ids (customers.json jobsToBeDone; insights link jobIds to these)
- dcre: `jtbd-dcre-1` Deliver an Excel-friendly interactive dashboard without building ten variants, `jtbd-dcre-2` Add write-back, planning and commenting to a dashboard the governed way, `jtbd-dcre-3` Guide users through a dashboard and prove it is used.
- bilr: `jtbd-bilr-1` Grow dashboard adoption across creators, explorers and viewers, `jtbd-bilr-2` Govern which extensions run on the platform and under which licence, `jtbd-bilr-3` Justify and renew the extensions investment with usage evidence.
- bviw: `jtbd-bviw-1` Answer my own question from the dashboard without asking for a new one, `jtbd-bviw-2` Take the numbers with me to Excel, a meeting or a slide.
- plnr: `jtbd-plnr-1` Enter and revise forecasts, budgets and targets inside the dashboard, `jtbd-plnr-2` Comment, correct and approve numbers with a full audit trail, `jtbd-plnr-3` Produce P&Ls and management statements from the dashboard data.
- exec: `jtbd-exec-1` Receive the right report at the right time where I work, `jtbd-exec-2` See the KPIs that matter and drill only when something is off.
- itad: `jtbd-itad-1` Install and upgrade the extensions on our own infrastructure without downtime, `jtbd-itad-2` Connect the extensions to our identity provider, databases and network safely, `jtbd-itad-3` Keep every workbook pointing at the right extension version and URL.
- secr: `jtbd-secr-1` Assess the vendor and deployment against our security and privacy standards quickly, `jtbd-secr-2` Prove to auditors who changed which number when.
- cpar: `jtbd-cpar-1` Win and deliver extension projects for my clients in my region, `jtbd-cpar-2` Earn recurring margin and enablement from the partner programme.

### North-star KPI names (use these VERBATIM as pyramid node names; productStrategy northStar must match)
- dcre: north star "Dashboard requests delivered per month"; supporting include "Dashboard rework rate", "Extension configuration time".
- bilr: north star "Monthly active dashboard users"; supporting include "Dashboard adoption rate", "Extension governance incidents".
- bviw: north star "Self-service answer rate"; supporting include "Time to insight", "New dashboard requests per user".
- plnr: north star "Planning cycle time"; supporting include "Write-back error rate", "Spreadsheet round-trips per cycle".
- exec: north star "On-time report delivery rate"; supporting include "Report open rate", "Decision latency".
- itad: north star "Extension upgrade lead time"; supporting include "Extension availability", "Installation effort hours".
- secr: north star "Vendor assessment cycle time"; supporting include "Open security findings", "Audit trail coverage".
- cpar: north star "Partner-sourced subscription revenue"; supporting include "Partner deal win rate", "Implementation hours per deployment".

KPI node id convention (mirrors tour-operator-erp-platform): `co-<cust>-top`, `co-<cust>-b1`, `co-<cust>-b1-c1`, `co-<cust>-b1-c1-l1` … and `bo-<cust>-…` for businessOutcomes. Every non-leaf has ≥2 children; target 4 levels (1+2+4+8). Set `icon` fields as `kpi-<cust>-<nodeid>.png`; icon files are backfilled later.
Customer icons: use `<cust>.png` (e.g. `dcre.png`) — backfilled later. Do NOT set `media` fields anywhere (no images exist).

## Streams (product-stream.json; JTBD steps reference via streamsNeeded)

- `discover-trial-and-subscribe-to-extensions` — From discovery on the website, Tableau Exchange, AppSource or a partner to free plan, trial, professional or enterprise subscription and renewal.
- `build-interactive-dashboards-with-extensions` — From a business requirement to a published dashboard with configured SuperTables, ShowMeMore, PowerKPIs, PictureThis, HierarchyFilter and DashboardGuide.
- `explore-and-self-serve-data-in-dashboards` — From a viewer's question to an answer inside the dashboard: pivot, group, filter, drill down, process view, saved views and Excel export.
- `write-back-plan-and-collaborate-in-dashboards` — From a viewed number to an entered forecast, comment, correction or approval stored in the customer's governed database with audit trail.
- `report-finance-from-dashboard-data` — From dashboard data and account hierarchies to P&Ls, budget reports and management statements (FinanceTables) and presentation exports (VizSlides).
- `distribute-reports-and-alerts` — From a schedule and recipient list to personalised PDF, PNG, CSV and Excel deliveries in email, Teams, Slack and network drives with audit trail.
- `guide-and-measure-dashboard-adoption` — From published dashboard to guided users and adoption evidence (DashboardGuide, DashboardUsage).
- `deploy-and-operate-extensions-on-premises` — From enterprise licence to installed, upgraded and monitored self-hosted extensions (ExtensionsManager, license keys, TrexReplacer).
- `govern-security-and-compliance` — From vendor assessment to safelisting, SSO, role management, audit evidence, penetration-test reports and certifications.
- `manage-licences-users-and-renewals` — From plan selection to metered active users, license keys, invoices, purchase orders and renewals through the Enterprise Customer Portal.
- `sell-and-deliver-through-partners` — From partner onboarding to registered deals, demo licences, joint delivery and partner margin.
- `support-and-enable-customers` — From a question to a resolved ticket, documentation, webinars, training and customer-success reviews.

## Product bricks (product-bricks.json) — root group → subgroup → bricks

Root "Extension Products":
- Subgroup "Write-back and Collaboration": `wbxt` WriteBackExtreme Write-back Extension, `inpt` InputTables Data Entry Grid, `fint` FinanceTables Financial Statements.
- Subgroup "Self-Service Tables and Discovery": `sptb` SuperTables Interactive Grid, `drdt` DrillDownTree Hierarchy Explorer, `hrfl` HierarchyFilter, `prcm` ProcessMining Visualizer.
- Subgroup "Visual Storytelling": `smmr` ShowMeMore Chart Library, `pkpi` PowerKPIs KPI Hub, `pict` PictureThis Image Tables, `vzsl` VizSlides Presentation Export, `xdsg` MarginalHistogram and EasyDesigns Helpers.
- Subgroup "Distribution and Adoption": `mlsc` MailScheduler Report Distribution, `dbgd` DashboardGuide Onboarding Overlays, `dbus` DashboardUsage Analytics.

Root "Extension Runtime and Platform Services":
- Subgroup "Extension Runtime": `xfrm` Extension Framework and Shared UI Kit (dashboard and viz extension shells on the Tableau Extensions API, settings persistence in the workbook, theming), `dcon` Dashboard Data Connector (worksheet data fetch, filters and parameters sync, server-side row model), `mpad` Multi-Platform Adapters (Power BI custom visuals, Looker Studio community visualizations).
- Subgroup "Write-back Backend": `wbdb` Write-back Data Store and Database Connectors, `wbwf` Write-back Workflow, Approvals and Audit Trail.
- Subgroup "Rendering and Delivery": `rndr` Dashboard Rendering and Export Service (PDF, PNG, CSV, Excel), `msgd` Messaging Delivery Gateway (email, Microsoft Teams, Slack, network drives, REST API).
- Subgroup "AI Services": `aiin` AI Insight and Generative Fill Services.

Root "Licensing, Deployment and Trust":
- Subgroup "Licensing and Accounts": `lics` License Service, Usage Metering and Billing (anonymous unique tokens, rolling 12-month active users, plans, invoices), `eprt` Enterprise Customer Portal (license keys, downloads, account management, my-appsfortableau).
- Subgroup "Deployment and Operations": `xmgr` ExtensionsManager, Installers and TrexReplacer (Windows one-click, Linux, admin console, extension URL management), `saas` SaaS Hosting and Release Pipeline (multi-tenant extension hosting, versioning, Tableau safelisting metadata, Exchange and AppSource listings), `idnt` Identity, SSO and Role Management.
- Subgroup "Security and Compliance": `sect` Security, Audit and Compliance Evidence (ISO 27001:2022 controls, penetration tests, data-flow documentation, DPAs, trust centre).

Root "Go-to-Market and Customer Success":
- Subgroup "Growth and Partners": `webt` Website, Trials and Self-Service Signup, `gall` Gallery, Demo Workbooks and Templates, `part` Partner Network Portal and Deal Registration.
- Subgroup "Support and Enablement": `supp` Support Portal, SLAs and Ticketing, `docs` Documentation, Webinars and Training, `csuc` Customer Success and Account Health.

35 bricks. Module ids must start with `module-` (e.g. `module-sptb-web`, `module-wbxt-api`). Brick icons: `product-bricks/icons/<brick>.png` — backfilled later.

### Brick dataDependencies → data asset ids (see below); wire at least these
wbxt→write-back-record,write-back-schema,write-back-audit-log; inpt→write-back-record,write-back-schema,comment-and-annotation; fint→financial-statement-model,dashboard-data-snapshot; sptb→extension-configuration,dashboard-data-snapshot,saved-view; drdt→extension-configuration,dashboard-data-snapshot; hrfl→extension-configuration,dashboard-data-snapshot; prcm→process-event-log,extension-configuration; smmr→extension-configuration,dashboard-data-snapshot; pkpi→extension-configuration,dashboard-data-snapshot; pict→extension-configuration,dashboard-data-snapshot; vzsl→rendered-report-artifact,dashboard-data-snapshot; xdsg→extension-configuration; mlsc→report-schedule,report-delivery-log,rendered-report-artifact; dbgd→dashboard-guide-content,extension-configuration; dbus→dashboard-usage-event; xfrm→extension-configuration; dcon→dashboard-data-snapshot; mpad→extension-configuration,dashboard-data-snapshot; wbdb→write-back-record,write-back-schema; wbwf→write-back-audit-log,comment-and-annotation; rndr→rendered-report-artifact; msgd→report-delivery-log; aiin→ai-request-log,dashboard-data-snapshot; lics→license-entitlement,usage-token-record,subscription-and-invoice,customer-account; eprt→customer-account,license-entitlement,release-artifact; xmgr→release-artifact,tenant-deployment-record; saas→release-artifact,tenant-deployment-record; idnt→identity-and-role; sect→security-evidence-document,write-back-audit-log; webt→customer-account,subscription-and-invoice; gall→release-artifact; part→partner-profile-and-deal; supp→support-ticket,customer-account; docs→release-artifact; csuc→customer-account,usage-token-record,support-ticket.

## Data assets (data/data-assets.json) — id → ownerTeamId

- `extension-configuration` → extension-runtime
- `dashboard-data-snapshot` → extension-runtime
- `saved-view` → tables-and-discovery
- `process-event-log` → tables-and-discovery
- `write-back-record` → write-back-and-planning
- `write-back-schema` → write-back-and-planning
- `write-back-audit-log` → write-back-and-planning
- `comment-and-annotation` → write-back-and-planning
- `financial-statement-model` → write-back-and-planning
- `report-schedule` → distribution-and-adoption
- `report-delivery-log` → distribution-and-adoption
- `rendered-report-artifact` → distribution-and-adoption
- `dashboard-usage-event` → distribution-and-adoption
- `dashboard-guide-content` → distribution-and-adoption
- `ai-request-log` → ai-enablement
- `license-entitlement` → deployment-and-licensing
- `usage-token-record` → deployment-and-licensing
- `customer-account` → deployment-and-licensing
- `subscription-and-invoice` → deployment-and-licensing
- `release-artifact` → deployment-and-licensing
- `tenant-deployment-record` → deployment-and-licensing
- `identity-and-role` → deployment-and-licensing
- `security-evidence-document` → security-and-compliance
- `partner-profile-and-deal` → growth-and-partners
- `support-ticket` → support-and-enablement

25 assets. Write-back records, comments, audit logs and process event logs live in the CUSTOMER's databases (on-premises) — model stores and residency accordingly; the vendor never sees that data in Enterprise deployments.

## Teams (teams.json) — every brick owned by exactly one team

The company has about 30 employees, so teams are small (2–4 people); model that honestly (total headcount ≈ 30).

Org group "Extension Product Teams":
- `write-back-and-planning` (stream-aligned) owns wbxt, inpt, fint, wbdb, wbwf
- `tables-and-discovery` (stream-aligned) owns sptb, drdt, hrfl, prcm
- `visual-storytelling` (stream-aligned) owns smmr, pkpi, pict, vzsl, xdsg
- `distribution-and-adoption` (stream-aligned) owns mlsc, dbgd, dbus, rndr, msgd

Org group "Platform and Enablement Teams":
- `extension-runtime` (platform) owns xfrm, dcon, mpad
- `deployment-and-licensing` (platform) owns lics, eprt, xmgr, saas, idnt
- `ai-enablement` (enabling) owns aiin
- `security-and-compliance` (enabling) owns sect

Org group "Go-to-Market and Customer Success":
- `growth-and-partners` (stream-aligned) owns webt, gall, part
- `support-and-enablement` (enabling) owns supp, docs, csuc

10 teams, 35 bricks.

## Products (product-deployments/products.json) — id, primary customers

- `writebackextreme` — WriteBackExtreme and InputTables (Enterprise-only write-back suite) — plnr, dcre, itad
- `supertables` — SuperTables — bviw, dcre
- `financetables` — FinanceTables — plnr, exec
- `mailscheduler` — MailScheduler (Enterprise-only) — exec, bilr
- `visual-storytelling-extensions` — Visual Storytelling Extensions (ShowMeMore, PowerKPIs, PictureThis, VizSlides, MarginalHistogram, EasyDesigns) — dcre, exec
- `discovery-extensions` — Discovery Extensions (DrillDownTree, HierarchyFilter, ProcessMining) — bviw, dcre
- `dashboard-workflow-tools` — Dashboard Workflow Tools (DashboardGuide, DashboardUsage, TrexReplacer) — bilr, dcre
- `enterprise-deployment` — Enterprise Deployment (self-hosted extensions, ExtensionsManager, Enterprise Customer Portal, SLAs) — itad, secr, bilr
- `apps-for-power-bi-and-looker-studio` — Apps for Power BI and Looker Studio — dcre, plnr
- `partner-network-program` — Partner Network Program — cpar

## Deployment channels (deployment.json; maas is the structural reference)

Channel groups: "Tableau Dashboard and Viz Extensions" (Tableau Cloud SaaS-hosted extensions, Tableau Server safelisted extensions, Tableau Desktop, Tableau Exchange listing), "Power BI and Looker Studio Visuals" (Microsoft AppSource custom visuals, Looker Studio community visualizations), "Enterprise Self-Hosted Runtime" (Windows one-click installer, Linux install, ExtensionsManager admin console, WriteBackExtreme and MailScheduler servers), "Web Portals" (website and pricing, Enterprise Customer Portal, partner portal, support portal, docs.infotopics.com), "Delivery Channels and APIs" (email, Microsoft Teams, Slack, network drives, MailScheduler and WriteBackExtreme REST APIs, database connectors), "Internal Operations" (license administration, release pipeline, customer success tooling). Map deployedBricks with usedInProducts referencing product ids above.

## Sourced company facts (reuse consistently; do not invent numbers)

- Infotopics | Apps for Tableau: Lage Doelen 2, Hardenberg (NL) and 25 Watling Street, London (UK). Founded 2018 by Merlijn Buit (CTO, Tableau Visionary) and Richard van Wijk (CEO); Infotopics a Tableau Gold Partner since 2011; ~30 employees; two of the 25 global Tableau Hall of Fame Visionaries on the team.
- Origin: Tableau dashboard extensions released July 2018 (2018.2); first product ShowMeMore shown in the Tableau Conference 2018 keynote (New Orleans); Tableau Innovative Solution Award 2018. Apps for Power BI established 2022 (SuperTables, PictureThis, InputTables, WriteBackExtreme); Apps for Looker Studio companion.
- Scale: 600+ organisations, 150+ countries, 30+ (viz) extensions, 32 partners worldwide. Named customers: Bank of America, Pfizer, Siemens, Johnson & Johnson, Amgen, BNP Paribas, Sony Interactive Entertainment, McDonald's, Toyota, US Bank, Post Holdings (1,000+ Tableau users), Fraudio.
- Plans: Free 1–5 users (all extensions, no time limit, no credit card); Professional up to 100 users, cloud, annual billing, live chat and email support; Enterprise unlimited users, SaaS or on-premises, dedicated customer success manager, priority support, bank transfer and purchase orders, prioritised feature requests. Users counted as anyone interacting with a published dashboard (creators, explorers, viewers) via anonymous unique tokens over a rolling 12 months; inactive 12 months = not counted. WriteBackExtreme and MailScheduler are Enterprise-only; 30-day WriteBackExtreme trial in a personal cloud environment. Student licences; SLAs; Tableau OEM, Core and Enterprise licences supported.
- Security: ISO/IEC 27001:2022 certified; annual penetration testing; Enterprise deployment needs no internet and gives Infotopics no data access.
- Partners: 32 firms incl. Slalom, Biztory, USEReady, Big X Data; serve customers in native language by region.
- Vortex Capital Partners: buyout announced 26 March 2026 (Vortex category Software, year 2026); goals: accelerate international growth, expand portfolio with AI functionality, selective strategic acquisitions. Quotes: van Wijk — the partnership "enables us to accelerate our product development and further expand our international presence"; Buit — "Vortex understands our culture and people well and aims to preserve and strengthen both."
- Industries: finance, healthcare, retail, government and public sector, leisure and hospitality.
