# ID Spine — transfer-pricing-compliance-platform

Authoritative ID contract for this domain. Every artifact file MUST use exactly these
IDs when referencing entities owned by another file. Names/descriptions here are
one-liners; the artifact author expands them to reference-domain density.
All ids lowercase. Modeled on Reptune / Reptune.net (see DOMAIN.md).

## Customer groups and customers (customers.json)

Group "In-house Tax Teams of Multinationals" — group tax and transfer pricing functions of multinationals with 5 to 500+ legal entities (Reptune reference customers: TomTom, Stahl, Avnet, Ravago, Stanley Black & Decker):
- `htax` — Group Head of Tax / Transfer Pricing Director. Owns the global transfer pricing policy, budgets compliance, buys the platform and service level, answers to the CFO and audit committee, defends the group in tax audits, APAs and MAPs.
- `tpmg` — Transfer Pricing Manager / Documentation Coordinator. Runs the annual documentation cycle: sets up and maintains the TP model, scopes entities and countries, collects data, generates Master File and Local Files, localises, tracks deadlines, coordinates local contacts and advisers.
- `lfin` — Local Finance Controller / Country Tax Contact. Provides entity financials, segmented P&L and transactional data, reviews the local file for the local perspective, arranges translation and local forms, files with the local tax authority, responds to local audits.

Group "Legal and Corporate Governance":
- `lgcn` — Corporate Legal Counsel / Company Secretary. Maintains legal entities, shareholders, directors and authorised signatories, drafts and signs intercompany agreements, keeps corporate documents and structure charts current, collaborates with tax on agreements that back the documentation.

Group "Tax Advisory Firms":
- `tadv` — Transfer Pricing Adviser at an international or local tax advisory firm. Licenses the platform to prepare documentation for several client groups, wants leverage per adviser, consistent quality, local expertise for countries the firm does not cover, and a margin on documentation work.

Group "Reptune Service and Content Teams" — the operator's own specialists who use the platform every day:
- `tpsp` — Reptune Transfer Pricing Specialist (Full Service and Collaborative delivery). Coordinates and prepares documentation end-to-end for outsourced clients at fixed rates per Local File, from data processing and drafting to localisation and translation; gives on-demand advice in the included expert hours.
- `regr` — Country Regulations and Content Specialist. Keeps local transfer pricing regulations, thresholds, deadlines, filing formats, language and translation requirements current for 170+ countries; maintains templates, glossaries and the R-AI local-requirements knowledge base.

### JTBD ids (customers.json jobsToBeDone; insights link jobIds to these)
- htax: `jtbd-htax-1` Be audit-ready in every country without a documentation project each year, `jtbd-htax-2` Control transfer pricing compliance cost and adviser spend, `jtbd-htax-3` See group-wide compliance and risk status at a glance.
- tpmg: `jtbd-tpmg-1` Set up a transfer pricing model that generates consistent documentation everywhere, `jtbd-tpmg-2` Deliver every Master File, Local File and CbCR before its deadline, `jtbd-tpmg-3` Localise and translate documentation without losing consistency.
- lfin: `jtbd-lfin-1` Provide correct entity financials and transactional data with minimal effort, `jtbd-lfin-2` File a locally compliant local file and forms on time, `jtbd-lfin-3` Answer a local tax audit with documentation that holds.
- lgcn: `jtbd-lgcn-1` Keep every legal entity and signatory record accurate and time-stamped, `jtbd-lgcn-2` Cover every intercompany transaction with a signed agreement, `jtbd-lgcn-3` Produce current and historical structure charts on demand.
- tadv: `jtbd-tadv-1` Prepare documentation for many clients with fewer adviser hours, `jtbd-tadv-2` Deliver locally compliant files in countries my firm does not cover, `jtbd-tadv-3` Grow a recurring documentation practice.
- tpsp: `jtbd-tpsp-1` Deliver complete, compliant documentation for a client at a fixed fee and margin, `jtbd-tpsp-2` Keep the client in control and informed while we do the work, `jtbd-tpsp-3` Move clients between service levels without rework.
- regr: `jtbd-regr-1` Keep 170+ country rule sets and deadlines current and correct, `jtbd-regr-2` Turn regulatory changes into templates, validations and answers users can act on.

### North-star KPI names (use these VERBATIM as pyramid node names; productStrategy northStar must match)
- htax: north star "Audit-ready documentation coverage"; supporting include "Transfer pricing compliance cost per entity", "Documentation-related audit adjustments".
- tpmg: north star "Local file preparation time"; supporting include "On-time filing rate", "Documentation consistency score".
- lfin: north star "Local data submission cycle time"; supporting include "Data validation error rate", "Local filing on-time rate".
- lgcn: north star "Intercompany agreement coverage"; supporting include "Entity data accuracy rate", "Agreement signature turnaround time".
- tadv: north star "Local files delivered per adviser"; supporting include "Client documentation margin", "Client retention rate".
- tpsp: north star "Local files delivered per specialist"; supporting include "Delivery lead time per local file", "Client rework rate".
- regr: north star "Country coverage currency rate"; supporting include "Regulation update lead time", "Country expert query resolution rate".

KPI node id convention (mirrors real-estate-erp-platform): `co-<cust>-top`, `co-<cust>-b1`, `co-<cust>-b1-c1`, `co-<cust>-b1-c1-l1` … and `bo-<cust>-…` for businessOutcomes. Every non-leaf has ≥2 children; target 4 levels (1+2+4+8). Set `icon` fields as `kpi-<cust>-<nodeid>.png`; icon files are backfilled later.
Customer icons: use `<cust>.png` (e.g. `htax.png`) — backfilled later. Do NOT set `media` fields on JTBDs, journeys or relations (no images exist).

## Streams (product-stream.json; JTBD steps reference via streamsNeeded — use these ids only)

- `set-up-the-transfer-pricing-model` — From entities, transactions, functional analyses, methods and templates to a configured TP model in the client's corporate identity, live in days (R-AI onboarding assistant, Excel bulk entry, free two-week trial).
- `scope-and-plan-the-annual-documentation-cycle` — From fiscal year and entity list to scoped documentation per entity and country, auto-calculated deadlines, assigned tasks, reminders and a compliance dashboard.
- `collect-and-validate-financial-and-transactional-data` — From ERP extracts and Excel templates to validated entity financials, segmented P&L and transactional data, with actions required before generation.
- `generate-master-file-and-local-files` — From a validated model to Master File and Local Files at the press of a button: template selection, benchmark and agreement insertion, custom text, styling, draft and final output.
- `localise-and-translate-documentation` — From an English local file to a locally compliant, translated file: country templates and content rules, machine translation with glossaries, human-certified translation, local forms and procedures.
- `prepare-and-file-cbcr-and-notifications` — From CbCR data to filing-ready XML and Excel, EU Public CbCR in XHTML with inline XBRL, notifications and local filing guidance.
- `benchmark-intercompany-transactions` — From transaction types and functional profiles to benchmark studies, arm's-length ranges and a comparison of each entity's segmented results against its range.
- `manage-legal-entities-and-intercompany-agreements` — From corporate registers and contracts to time-stamped entity records, signatories, intercompany agreements, corporate documents, structure charts and e-signatures that feed the documentation.
- `monitor-compliance-and-defend-audits` — From dashboards and risk indicators to audit-ready evidence: compliance status per country, value chain analysis, risk management, audit and controversy support.
- `maintain-country-regulations-and-deadlines` — From regulatory change to current rule sets: thresholds, content, format, language and deadline rules for 170+ countries, surfaced in the platform and in R-AI's country-expert answers.
- `deliver-documentation-as-a-service` — From engagement at a fixed rate per Local File to delivered documentation: Reptune specialists coordinate, prepare and deliver while the client monitors progress; clients switch between On Demand, Collaborative and Full Service.
- `integrate-with-erp-operational-tp-and-identity` — From external systems to the platform: direct ERP integration, operational transfer pricing solutions, Excel data exchange and validation, DocuSign, SSO and access control.

## Product bricks (product-bricks.json) — root group → subgroup → bricks

Root "Transfer Pricing Model and Data":
- Subgroup "Transfer Pricing Model": `tpmd` Transfer Pricing Model, Company Types and Functional Analyses, `ictx` Intercompany Transactions Register, `segp` Segmented Financials and P&L Segmentation.
- Subgroup "Data Intake": `xlio` Excel Templates, Bulk Upload and Data Validation, `erpi` ERP and Operational Transfer Pricing Integrations.

Root "Documentation Generation":
- Subgroup "Report Generator": `gene` Master File and Local File Generator, `tmpl` Templates, Report Styling and Custom Text, `vald` Pre-generation Validation and Actions Required.
- Subgroup "Localisation": `ctry` Country Regulations, Local Requirements and Local Forms, `trns` Machine Translation and Glossaries.

Root "CbCR and Benchmarks":
- Subgroup "Country-by-Country Reporting": `cbcr` CbCR Data Management and XML Output, `pcbc` EU Public CbCR (XHTML with inline XBRL), `cbcn` CbCR Notifications.
- Subgroup "Benchmarking": `bnch` Benchmark Studies, Arm's-Length Ranges and Entity Comparison.

Root "Compliance Workflow":
- Subgroup "Workflow": `scop` Documentation Scoping, `task` Task Assignment, Collaboration and Reminders, `dead` Deadline Calculation Engine.
- Subgroup "Insight and Risk": `dash` Compliance Dashboard and Worldmap, `rskm` Risk Management and Value Chain Analysis.

Root "Legal Module":
- Subgroup "Entities and Agreements": `lent` Legal Entity Management, `icag` Intercompany Agreement Repository, `cdoc` Corporate Document Repository, `lsch` Legal Structure Charts, `esig` E-Signature Integration (DocuSign).

Root "AI and Assistance":
- Subgroup "AI Capabilities": `rai` R-AI Assistant (Onboarding and Country Expert), `aiwr` AI-assisted Writing and Editing.

Root "Platform Foundation":
- Subgroup "Core Services": `iden` Identity, SSO, User Profiles and Access Control, `divs` Divisions and Client Organisations, `audt` Audit Trail, Versioning and Archive, `docx` Document Rendering and Export, `secp` Security and ISO 27001 Controls.
- Subgroup "Service Delivery": `fsvc` Full Service Delivery Workspace, `supp` Expert Support and Advisory Hours.

33 bricks. Module ids must start with `module-` (e.g. `module-gene-web`, `module-gene-api`).

### Brick dataDependencies → data asset ids (see below); wire at least these
tpmd→transfer-pricing-model,company-type-profile,legal-entity; ictx→intercompany-transaction,legal-entity; segp→segmented-financial-statement,intercompany-transaction; xlio→data-upload-batch,validation-finding; erpi→data-upload-batch,integration-connection; gene→local-file-document,master-file-document,transfer-pricing-model; tmpl→report-template,local-file-document; vald→validation-finding,documentation-scope; ctry→country-regulation-record,filing-deadline; trns→translation-glossary,local-file-document; cbcr→cbcr-dataset,legal-entity; pcbc→public-cbcr-report,cbcr-dataset; cbcn→cbcr-notification,filing-deadline; bnch→benchmark-study,segmented-financial-statement; scop→documentation-scope,legal-entity; task→workflow-task,documentation-scope; dead→filing-deadline,country-regulation-record; dash→compliance-status-snapshot,filing-deadline; rskm→risk-assessment,intercompany-transaction; lent→legal-entity,corporate-document; icag→intercompany-agreement,intercompany-transaction; cdoc→corporate-document,legal-entity; lsch→legal-structure-chart,legal-entity; esig→e-signature-envelope,intercompany-agreement; rai→ai-interaction-log,country-regulation-record; aiwr→ai-interaction-log,local-file-document; iden→user-account,client-organisation; divs→client-organisation,legal-entity; audt→audit-trail-entry,local-file-document; docx→local-file-document,master-file-document,public-cbcr-report; secp→audit-trail-entry,user-account; fsvc→service-engagement,documentation-scope; supp→service-engagement,ai-interaction-log.

## Data assets (data/data-assets.json) — id → ownerTeamId

- `transfer-pricing-model` → tp-model-and-data
- `company-type-profile` → tp-model-and-data
- `intercompany-transaction` → tp-model-and-data
- `segmented-financial-statement` → tp-model-and-data
- `data-upload-batch` → tp-model-and-data
- `validation-finding` → report-generation
- `documentation-scope` → compliance-workflow
- `master-file-document` → report-generation
- `local-file-document` → report-generation
- `report-template` → report-generation
- `country-regulation-record` → localisation-and-country-content
- `filing-deadline` → localisation-and-country-content
- `translation-glossary` → localisation-and-country-content
- `cbcr-dataset` → cbcr-and-benchmarking
- `public-cbcr-report` → cbcr-and-benchmarking
- `cbcr-notification` → cbcr-and-benchmarking
- `benchmark-study` → cbcr-and-benchmarking
- `workflow-task` → compliance-workflow
- `compliance-status-snapshot` → compliance-workflow
- `risk-assessment` → compliance-workflow
- `legal-entity` → legal-module
- `intercompany-agreement` → legal-module
- `corporate-document` → legal-module
- `legal-structure-chart` → legal-module
- `e-signature-envelope` → legal-module
- `ai-interaction-log` → ai-and-assistance
- `user-account` → platform-core-and-security
- `client-organisation` → platform-core-and-security
- `audit-trail-entry` → platform-core-and-security
- `integration-connection` → integrations
- `service-engagement` → full-service-delivery

31 assets.

## Teams (teams.json) — every brick owned by exactly one team

Reptune had 20+ team members at the August 2024 Vortex transaction; model the company at ~40 after commercial scaling, with small teams (2–5 people) that mix software engineers and transfer pricing specialists.

Org group "Documentation Product Group":
- `tp-model-and-data` (stream-aligned) owns tpmd, ictx, segp, xlio
- `report-generation` (stream-aligned) owns gene, tmpl, vald, docx
- `localisation-and-country-content` (complicated-subsystem) owns ctry, trns

Org group "Compliance and Reporting Group":
- `cbcr-and-benchmarking` (stream-aligned) owns cbcr, pcbc, cbcn, bnch
- `compliance-workflow` (stream-aligned) owns scop, task, dead, dash, rskm

Org group "Legal Module Group":
- `legal-module` (stream-aligned) owns lent, icag, cdoc, lsch, esig

Org group "Platform and AI Group":
- `ai-and-assistance` (enabling) owns rai, aiwr
- `platform-core-and-security` (platform) owns iden, divs, audt, secp
- `integrations` (platform) owns erpi

Org group "Services and Customer Group":
- `full-service-delivery` (stream-aligned) owns fsvc; customer dependencies on htax, tpsp, lfin
- `customer-success-and-advisory` (enabling) owns supp; runs onboarding, training, on-demand expert hours, consultation (VCA, APAs, MAPs, controversy); customer dependencies on htax, tpmg, tadv

11 teams.

## Products (product-deployments/products.json) — id, primary customers

- `reptune-net-platform` — Reptune.net Platform (Core / Advanced / Enterprise plans: unlimited users, dashboard, workflow, country regulations, report styling, data exchange) — htax, tpmg, lfin
- `automated-report-generator` — Automated Report Generator (Master File and Local Files, 170+ countries) — tpmg, tadv, tpsp
- `cbcr-and-public-cbcr` — Country-by-Country Reporting and EU Public CbCR (add-on / Enterprise) — tpmg, lfin
- `compliance-workflow-and-dashboard` — Transfer Pricing Workflow and Dashboard — tpmg, htax, lfin
- `legal-module` — Legal Module (entities, agreements, structure charts, DocuSign) — lgcn, htax
- `benchmark-offerings` — Benchmark Offerings — tpmg, tadv
- `ai-and-machine-translation` — R-AI, AI-assisted Writing and Machine Translation (28 languages) — tpmg, lfin, regr
- `country-regulations-and-local-forms` — Country Regulations, Local Forms and Procedures — regr, tpmg, tadv
- `full-service-documentation` — Full Service and Collaborative Documentation Services (fixed rate per Local File) — htax, tpsp
- `transfer-pricing-advisory` — Transfer Pricing Consultation, Risk Management, VCA and Operational TP support — htax, tpsp
- `integrations-and-data-exchange` — ERP and Operational TP Integrations, Excel Data Exchange, SSO — lfin, tpmg

11 products. Use `<product-id>.png` icons (rendered later into product-deployments/icons).

## Deployment channels (deployment.json; maas is the structural reference)

Channel groups: "Web Application" (Reptune.net web app: dashboard, generator, workflow, CbCR, legal module, benchmarks, admin), "Document Outputs" (Word/PDF Master File and Local Files, Excel data exchange, CbCR XML, EU Public CbCR XHTML with inline XBRL, structure chart exports), "Integrations" (ERP integration, operational transfer pricing solutions, Excel interface, DocuSign, SSO identity providers, e-mail reminders), "AI Runtime" (R-AI assistant, AI writing service, machine translation engine), "Internal Operations" (full-service delivery workspace, country regulations content back office, support and onboarding). Map deployedBricks with usedInProducts referencing product ids above.

## Sourced company facts (reuse consistently; do not invent numbers)

- Reptune (formerly TP Tuned), Amsterdam (NL), founded 2015 by Lennart van den Kommer and Allard Posthuma, later joined by David Zářecký; Big 4 and in-house experience. Named team: Lennart van den Kommer (CEO, TP adviser and co-founder), Giovanni Vajna de Pava (CTO), Alexandra Robins (Head of Legal). 20 team members at the transaction (reptune.tax news), "20+" (Vortex).
- Vortex Capital Partners became majority shareholder alongside management; announced 5 August 2024 (buyout, software and services). Quotes: Lennart van den Kommer ("proven offering and a loyal customer base... serve more clients in additional countries and expand our offering"); Evert Jan de Groot, Managing Partner Vortex ("proprietary software (Reptune.net), combined with Reptune's deep knowledge of transfer pricing"). Vortex focus since: organisational infrastructure, commercial scaling, go-to-market, international expansion, possibly acquisitions.
- Scale: trusted by 150+ companies / multinationals worldwide; automated documentation for 170+ countries (Vortex: 169+); 5 to 500+ entities; 50–75% time and cost savings; specialists prepare documentation in 25% of the time of traditional advisers; machine translation into 28 languages; ISO 27001 certified; free two-week trial; up and running in days, no installation.
- Named customers: TomTom, Stahl, Avnet (global since 2019), Ravago (about 4 years), Stanley Black & Decker. Testimonials: Peter Roelofsen (VP Taxation Europe, partner since 2015, "saved the day in various tax audits", CbCR and VCA support), Alberta de Vries (Chief Compliance Officer and Head of Tax, Stahl), An Beckers (Tax, Ravago), Olivier Noël (Director Global Transfer Pricing, Avnet).
- Plans: Core (up to 25 local files; unlimited users, Automated Report Generator, Dashboard, TP Workflow, AI-assisted writing, R-AI Onboarding Assistant, country regulations, report styling, data exchange and validation, 2 expert hours/year; add-ons machine translation, CbCR OECD/EU public, SSO, R-AI Country Expert), Advanced (up to 50; adds SSO, R-AI Country Expert, custom text, 4 hours; add-ons custom template, custom transactional data model), Enterprise (50+; adds custom user profiles, CbCR, divisions, 8 hours; add-on custom development). Service levels: On Demand (client-led), Collaborative (joint), Full Service (Reptune-led). Fixed rates per Local File.
- Features: rule-based generator (company types, functional analyses, TP methods, benchmarks configured once), OECD-aligned templates, localised templates (e.g. Italy), built-in validation, segmented financials vs benchmark, Excel bulk entry, dashboard with worldmap and filing deadlines per entity; workflow with scoping, task assignment, e-mail reminders, auto-calculated deadlines for Master File, Local Files, CbCR and CbCR notifications; CbCR XML and Excel, EU Public CbCR XHTML inline XBRL, Australian Public CbCR coming; Legal Module with time-stamped entity data, signatories, agreements, corporate document repository, current and historical structure charts, DocuSign; R-AI assistant (any language, Local Requirements coming), AI writing, machine translation with glossaries and human-certified option; operational TP: P&L segmentation, direct ERP integration, Excel mass upload; consultation: VCA, CbCR analysis, functional analysis, TP model review, policy write-up, controversy, restructurings, APAs, MAPs.
- Regulatory context: OECD BEPS Action 13 three-tiered documentation; EU Directive (EU) 2021/2101 public CbCR; Pillar Two transitional CbCR safe harbour.
