# ID Spine — occupational-health-and-safety-platform

Authoritative ID contract for this domain. Every artifact file MUST use exactly these
IDs when referencing entities owned by another file. Names/descriptions here are
one-liners; the artifact author expands them to reference-domain density.
All ids lowercase. Modeled on Kitry (kitry.com; see DOMAIN.md).

## Customer groups and customers (customers.json)

Group "Occupational Health Services" — the internal or autonomous occupational health service of a large employer (industry, chemicals and pharma, healthcare facilities, universities, public sector, finance, transport, services) in France, Belgium, Luxembourg or the Netherlands:
- `ocph` — Occupational Physician (médecin du travail / arbeidsarts). Conducts examinations, issues fitness-for-work opinions with restrictions, owns the confidential occupational medical file, advises the employer on collective prevention, runs teleconsultations.
- `ohnr` — Occupational Health Nurse / Medical Assistant. Runs the consultation day: convocations, intake, questionnaires, screenings with connected devices (audiometry, spirometry, vision), nurse visits, vaccination and health campaigns, captures everything into the file.
- `ohsm` — Occupational Health Service Manager / Coordinator. Plans surveillance capacity and periodicity compliance across sites, buys and administers the platform, proves the service's activity in annual reports to the employer, works council and authorities, owns hosting and certification requirements.

Group "HSE and Prevention":
- `hsem` — HSE Manager / Prevention Adviser (préventeur, conseiller en prévention, preventieadviseur). Maintains the risk assessment (DUERP / global prevention plan), inspections and audits, chemical inventory, action plans, ISO 45001 system; analyses accidents with HR and the physician.
- `sitm` — Site / Line Manager. Uses the manager portal: sees fitness clearance and restrictions of the team without medical content, reports hazardous situations, owns corrective actions on the floor, releases workers for visits.

Group "HR and Employees":
- `hrad` — HR Administrator / Personnel Officer. Keeps employee, contract and assignment data flowing from the HRIS so surveillance triggers automatically; declares work accidents and occupational diseases to national bodies and insurers on time; coordinates absence, restrictions and return-to-work with the medical service.
- `empl` — Employee. Uses the self-service portal: books and reschedules visits, completes questionnaires privately, downloads certificates, joins teleconsultations, reports a safety concern.

Group "Kitry Services and Content Teams" — the operator's own specialists who use the platform every day:
- `kimp` — Kitry Implementation and Customer Success Consultant. Runs functional assessment, configuration, data migration, training and change management for new customers; keeps existing customers current with regulatory and product releases; dedicated account manager and support escalation.

### JTBD ids (customers.json jobsToBeDone; insights link jobIds to these)
- ocph: `jtbd-ocph-1` Deliver every required examination on time with a documented fitness opinion, `jtbd-ocph-2` Keep a complete, confidential medical file that follows the worker across sites and services, `jtbd-ocph-3` Turn individual findings into collective prevention advice.
- ohnr: `jtbd-ohnr-1` Run a full consultation day without administrative friction, `jtbd-ohnr-2` Capture screenings, measurements and questionnaires accurately into the file, `jtbd-ohnr-3` Run nurse visits, vaccination and health campaigns at scale.
- ohsm: `jtbd-ohsm-1` Keep periodic surveillance compliance above target with the medical capacity we have, `jtbd-ohsm-2` Prove the service's activity and compliance to the employer and the authorities, `jtbd-ohsm-3` Run the service on certified, secure infrastructure without an IT project.
- hsem: `jtbd-hsem-1` Maintain a living risk assessment per workstation and site, `jtbd-hsem-2` Drive hazardous situations, inspection findings and audit actions to closure, `jtbd-hsem-3` Keep chemical products and exposures under control and inspection-ready.
- sitm: `jtbd-sitm-1` Know that everyone on my team is fit and cleared for their work, `jtbd-sitm-2` Report and resolve hazardous situations from the floor, `jtbd-sitm-3` Apply medical restrictions and accommodations without breaching confidentiality.
- hrad: `jtbd-hrad-1` Keep employee and assignment data in sync so surveillance is triggered automatically, `jtbd-hrad-2` Declare and follow work accidents and occupational diseases correctly and on time, `jtbd-hrad-3` Manage absence, restrictions and return-to-work with the medical service.
- empl: `jtbd-empl-1` Attend my medical visit with minimal disruption, `jtbd-empl-2` Access my own health documents and complete questionnaires privately, `jtbd-empl-3` Raise a safety concern and see it acted on.
- kimp: `jtbd-kimp-1` Take a new organisation live with its data, configuration and trained users on schedule, `jtbd-kimp-2` Keep every customer current with regulatory and product change without disruption, `jtbd-kimp-3` Resolve support requests and grow the account.

### North-star KPI names (use these VERBATIM as pyramid node names; productStrategy northStar must match)
- ocph: north star "Medical surveillance compliance rate"; supporting include "Consultation documentation time", "Fitness opinion turnaround time".
- ohnr: north star "Examinations completed per nurse day"; supporting include "Screening data capture error rate", "Pre-visit questionnaire completion rate".
- ohsm: north star "Workforce surveillance coverage rate"; supporting include "Medical capacity utilisation", "Annual activity report preparation time".
- hsem: north star "Risk assessment currency rate"; supporting include "Corrective action closure rate", "Chemical inventory completeness".
- sitm: north star "Team fitness clearance rate"; supporting include "Hazardous situation resolution time", "Restriction application lead time".
- hrad: north star "Work accident declaration on-time rate"; supporting include "Employee data sync accuracy", "Return-to-work coordination time".
- empl: north star "Visit self-service rate"; supporting include "Appointment rescheduling effort", "Safety report response time".
- kimp: north star "Go-live on schedule rate"; supporting include "Data migration defect rate", "Support ticket resolution time".

KPI node id convention (mirrors transfer-pricing-compliance-platform): `co-<cust>-top`, `co-<cust>-b1`, `co-<cust>-b1-c1`, `co-<cust>-b1-c1-l1` … and `bo-<cust>-…` for businessOutcomes. Every non-leaf has ≥2 children; target 4 levels (1+2+4+8). Set `icon` fields as `kpi-<cust>-<nodeid>.png`; icon files are backfilled later.
Customer icons: use `<cust>.png` (e.g. `ocph.png`) — backfilled later. Do NOT set `media` fields on JTBDs, journeys or relations (no images exist).

## Streams (product-stream.json; JTBD steps reference via streamsNeeded — use these ids only)

- `maintain-workforce-and-exposure-data` — From HRIS feeds and site structures to a current register of workers, contracts, assignments, workstations and exposure/risk profiles that drives surveillance, safety and reporting.
- `plan-and-schedule-medical-surveillance` — From surveillance rules and periodicity per country and profile to convocations, appointment slots, SMS/e-mail reminders and a capacity plan per physician and nurse.
- `conduct-examinations-and-teleconsultations` — From convocation to a completed examination: pre-visit questionnaire, device measurements, consultation workspace, fitness-for-work opinion with restrictions, secure teleconsultation, certificates with e-signature.
- `keep-the-occupational-medical-file` — From every contact and document to a complete, confidential medical file: medical secrecy and access segregation, retention, transfer between services, interoperability with national health records.
- `assess-and-control-workplace-risks` — From workstations and exposures to a living risk assessment (DUERP / global prevention plan), prevention measures, ISO 45001 evidence and annual action plans.
- `report-and-resolve-hazardous-situations` — From a field report, inspection or audit finding to a corrective action assigned, followed and closed, with evidence.
- `track-chemical-products-and-exposures` — From chemical inventory and safety data sheets to hazard classification, exposure groups, CMR tracking and workstation exposure records feeding surveillance.
- `declare-and-analyse-accidents-and-occupational-diseases` — From an event to declaration on national forms (CERFA/Ameli, Fedris, insurers), root-cause analysis, frequency and severity statistics and follow-up to recognition and return-to-work.
- `serve-employees-and-managers-through-portals` — From role-based portals to self-service: appointments, questionnaires, documents, teleconsultation, safety reports for employees; fitness status, restrictions, actions and declarations for managers.
- `monitor-health-and-safety-performance` — From cross-module data to dashboards, KPIs, regulatory and annual reports and collective health monitoring.
- `deploy-migrate-and-train-a-customer` — From contract to go-live: functional assessment, configuration, project management, data migration, training, change management, and ongoing regulatory updates and support.
- `integrate-with-hr-devices-and-ecosystem` — From external systems to the platform: HRIS synchronisation, SSO, electronic signature, telehealth, SMS, measurement devices, national reporting connectors, and HDS/ISO 27001 hosting environments.

## Product bricks (product-bricks.json) — root group → subgroup → bricks

Root "Workforce and Exposure Data":
- Subgroup "Workforce Master Data": `wrkr` Worker, Contract and Assignment Registry, `orgs` Organisation, Sites and Workstations, `hris` HRIS Synchronisation and Import.
- Subgroup "Exposure and Surveillance Rules": `expo` Exposure and Risk Profile Register, `surv` Surveillance Rules and Periodicity Engine.

Root "Occupational Health":
- Subgroup "Scheduling": `schd` Convocation and Appointment Scheduling, `noti` Reminders, SMS and E-mail Notifications.
- Subgroup "Clinical Consultation": `cons` Consultation Workspace and Fitness Opinions, `ques` Questionnaires and Pre-visit Intake, `devs` Medical Device Measurement Capture, `tele` Secure Teleconsultation, `vacc` Vaccination and Health Campaigns.
- Subgroup "Medical Records": `dmst` Occupational Medical File, `mdoc` Medical Documents, Certificates and E-signature, `conf` Medical Confidentiality and Access Segregation.

Root "Workplace Safety":
- Subgroup "Risk Management": `risk` Risk Assessment and Prevention Plan, `hazs` Hazardous Situation Reporting, `insp` Inspections, Audits and Compliance Checks, `actn` Action Plan Management.
- Subgroup "Chemicals": `chem` Chemical Product Inventory and Safety Data Sheets.

Root "Accidents and Occupational Diseases":
- Subgroup "Events and Declarations": `acci` Work Accident and Occupational Disease Declaration, `rcaa` Event Analysis and Statistics, `nreg` National Reporting Forms and Connectors.

Root "Portals and Insight":
- Subgroup "Portals": `epor` Employee Portal, `mpor` Manager Portal.
- Subgroup "Analytics": `dash` Dashboards and KPIs, `rept` Regulatory and Annual Reports, `cohm` Collective Health Monitoring.

Root "Platform Foundation":
- Subgroup "Core Services": `iden` Identity, SSO, Roles and Consent, `cfgr` Configuration Engine (forms, workflows, business rules, multilingual), `regc` Country Regulation Content (FR/BE/LU/NL), `audt` Audit Trail and Data Retention, `host` HDS/ISO 27001 Hosting and Tenant Isolation.
- Subgroup "Integrations": `intg` Ecosystem Integrations (e-signature, telehealth, SMS, devices).
- Subgroup "Service Delivery": `impl` Implementation, Migration and Training Workspace, `supp` Support and Account Management.

36 bricks. Module ids must start with `module-` (e.g. `module-cons-web`, `module-cons-api`).

### Brick dataDependencies → data asset ids (see below); wire at least these
wrkr→worker-record,organisation-unit-and-workstation; orgs→organisation-unit-and-workstation,worker-record; hris→hris-import-batch,worker-record; expo→exposure-and-risk-profile,organisation-unit-and-workstation; surv→surveillance-schedule,exposure-and-risk-profile,country-regulation-rule; schd→convocation-and-appointment,surveillance-schedule; noti→notification-message,convocation-and-appointment; cons→consultation-record,fitness-opinion,occupational-medical-file; ques→questionnaire-response,consultation-record; devs→device-measurement,consultation-record; tele→teleconsultation-session,consultation-record; vacc→vaccination-and-campaign-record,worker-record; dmst→occupational-medical-file,medical-document; mdoc→medical-document,fitness-opinion; conf→consent-and-access-grant,occupational-medical-file; risk→risk-assessment,exposure-and-risk-profile; hazs→hazardous-situation-report,corrective-action; insp→inspection-and-audit-record,corrective-action; actn→corrective-action,risk-assessment; chem→chemical-product-and-sds,exposure-and-risk-profile; acci→work-accident-event,occupational-disease-case,worker-record; rcaa→event-analysis-and-statistic,work-accident-event; nreg→national-declaration-form,work-accident-event,occupational-disease-case; epor→portal-session-and-request,convocation-and-appointment,medical-document; mpor→portal-session-and-request,fitness-opinion,corrective-action; dash→kpi-snapshot,surveillance-schedule; rept→annual-activity-report,kpi-snapshot; cohm→collective-health-indicator,exposure-and-risk-profile; iden→user-account-and-role,consent-and-access-grant; cfgr→tenant-configuration,country-regulation-rule; regc→country-regulation-rule,surveillance-schedule; audt→audit-trail-entry,occupational-medical-file; host→tenant-configuration,audit-trail-entry; intg→integration-connection,notification-message,device-measurement; impl→implementation-project,hris-import-batch,tenant-configuration; supp→support-ticket,tenant-configuration.

## Data assets (data/data-assets.json) — id → ownerTeamId

- `worker-record` → workforce-and-surveillance
- `organisation-unit-and-workstation` → workforce-and-surveillance
- `hris-import-batch` → integrations
- `exposure-and-risk-profile` → workforce-and-surveillance
- `surveillance-schedule` → workforce-and-surveillance
- `convocation-and-appointment` → workforce-and-surveillance
- `notification-message` → workforce-and-surveillance
- `consultation-record` → clinical-consultation
- `fitness-opinion` → clinical-consultation
- `questionnaire-response` → clinical-consultation
- `device-measurement` → clinical-consultation
- `teleconsultation-session` → clinical-consultation
- `vaccination-and-campaign-record` → clinical-consultation
- `occupational-medical-file` → medical-records-and-confidentiality
- `medical-document` → medical-records-and-confidentiality
- `consent-and-access-grant` → medical-records-and-confidentiality
- `risk-assessment` → risk-and-prevention
- `hazardous-situation-report` → risk-and-prevention
- `inspection-and-audit-record` → risk-and-prevention
- `corrective-action` → risk-and-prevention
- `chemical-product-and-sds` → risk-and-prevention
- `work-accident-event` → accidents-and-occupational-diseases
- `occupational-disease-case` → accidents-and-occupational-diseases
- `event-analysis-and-statistic` → accidents-and-occupational-diseases
- `national-declaration-form` → accidents-and-occupational-diseases
- `portal-session-and-request` → portals-and-self-service
- `kpi-snapshot` → analytics-and-reporting
- `annual-activity-report` → analytics-and-reporting
- `collective-health-indicator` → analytics-and-reporting
- `user-account-and-role` → platform-core-and-security
- `tenant-configuration` → platform-core-and-security
- `audit-trail-entry` → platform-core-and-security
- `country-regulation-rule` → regulatory-content
- `integration-connection` → integrations
- `implementation-project` → implementation-and-migration
- `support-ticket` → support-and-account-management

36 assets. Medical assets (occupational-medical-file, consultation-record, fitness-opinion, questionnaire-response, device-measurement, teleconsultation-session, vaccination-and-campaign-record, medical-document, occupational-disease-case) are health data under medical secrecy: highest personal-data level, HDS hosting, physician-only access.

## Teams (teams.json) — every brick owned by exactly one team

Kitry does not publish headcount; model the company at about 70 people with small teams (3–7 people) that mix software engineers, occupational health professionals and implementation consultants.

Org group "Occupational Health Product Group":
- `workforce-and-surveillance` (stream-aligned) owns wrkr, orgs, expo, surv, schd, noti
- `clinical-consultation` (stream-aligned) owns cons, ques, devs, tele, vacc
- `medical-records-and-confidentiality` (complicated-subsystem) owns dmst, mdoc, conf

Org group "Workplace Safety Product Group":
- `risk-and-prevention` (stream-aligned) owns risk, hazs, insp, actn, chem
- `accidents-and-occupational-diseases` (stream-aligned) owns acci, rcaa, nreg

Org group "Experience and Insight Group":
- `portals-and-self-service` (stream-aligned) owns epor, mpor
- `analytics-and-reporting` (stream-aligned) owns dash, rept, cohm

Org group "Platform Group":
- `platform-core-and-security` (platform) owns iden, cfgr, audt, host
- `integrations` (platform) owns hris, intg
- `regulatory-content` (enabling) owns regc; occupational health lawyers and content specialists for FR/BE/LU/NL

Org group "Customer Services Group":
- `implementation-and-migration` (enabling) owns impl; customer dependencies on kimp, ohsm, hsem, hrad
- `support-and-account-management` (enabling) owns supp; customer dependencies on kimp, ohsm, ocph, hsem

12 teams.

## Products (product-deployments/products.json) — id, primary customers

- `kitry-occupational-health` — Occupational Health module (medical file, scheduling, questionnaires, devices, fitness opinions, campaigns) — ocph, ohnr, ohsm
- `kitry-workplace-safety` — Workplace Safety module (risk assessment, hazardous situations, inspections, action plans, chemicals) — hsem, sitm
- `kitry-accidents-and-occupational-diseases` — Work Accidents and Occupational Diseases module (declaration, national forms, analysis, statistics) — hrad, hsem, ocph
- `kitry-employee-and-manager-portals` — Employee and Manager Portals — empl, sitm
- `kitry-analytics-and-reporting` — Monitoring, Dashboards, KPIs and Regulatory Reports (transversal module) — ohsm, hsem
- `kitry-teleconsultation` — Integrated Secure Teleconsultation (Vonage) — ocph, empl
- `kitry-ecosystem-integrations` — HRIS, SSO, e-signature (Goodflag), SMS (Cegedim), measurement devices (Eolys, FIM, Essilor, JLM Medical, Siemens) — hrad, ohnr
- `kitry-saas-hosting` — Shared and Dedicated HDS/ISO 27001 SaaS Hosting (EEA only) — ohsm
- `kitry-implementation-and-services` — Functional assessment, configuration, project management, migration, training, change management, support, account management — kimp, ohsm, hsem

9 products. Use `<product-id>.png` icons (rendered later into product-deployments/icons).

## Deployment channels (deployment.json; maas is the structural reference)

Channel groups: "Web Application" (Kitry web app for health, safety, accidents, analytics and administration; role-based interfaces for physicians, nurses, HSE, HR), "Portals and Mobile" (employee portal, manager portal, responsive field safety reporting), "Integrations" (HRIS synchronisation, SSO identity providers, Goodflag e-signature, Vonage telehealth, Cegedim SMS, measurement devices, national reporting connectors), "Hosting Environments" (Shared HDS SaaS, Dedicated HDS SaaS — EEA only, ISO 27001), "Internal Operations" (implementation and migration workspace, regulatory content back office, support desk). Map deployedBricks with usedInProducts referencing product ids above.

## Sourced company facts (reuse consistently; do not invent numbers)

- Kitry: Belgian vendor, 35+ years of expertise in occupational health and safety software (kitry.eu: specialised since 1989); Kitry SA, Nivelles, Belgium, legal entity founded 2003 (registries); Vortex's 2022 release lists Antwerp as base. CEO Pierre Letargez (quoted 2022).
- Vortex Capital Partners strategic partnership / buyout announced 29 March 2022 (Vortex partner Evert Jan de Groot quoted). At the time: 100+ blue-chip and public customers, about 5,400 users, Belgium, France and Luxembourg (Vortex: Belgium, France, Netherlands). Vortex investment page now: 150+ organisations, more than 2.5 million medical files, sectors healthcare, chemicals, financial services, manufacturing, government; tools to comply with ISO 45001; transition to "pure-play SaaS provider" ("Kitry as a Service"); Vortex strengthened leadership and organisation.
- kitry.com: 4M+ employee records tracked, 6,000+ active users, 50%+ of employees use self-service (FR/BE/LU); modules Occupational Health, Workplace Safety, Work Accidents and Occupational Diseases, Employee and Manager Portals, Monitoring and KPIs; integrations electronic signature (Goodflag), teleconsultation (Vonage), SMS (Cegedim), measurement devices (Eolys, FIM, Essilor, JLM Medical, Siemens); HDS and ISO 27001 certified; shared and dedicated SaaS hosting; no access from outside the EEA; four-phase implementation (functional assessment, configuration, project management, training), data migration, change management, support, dedicated account managers; languages EN/FR/NL; sectors industry, chemicals and pharma, healthcare facilities, universities and research, public sector, financial services, transport and logistics, services.
- Named clients: SNCF, Thales, Ville de Bruxelles, Umicore, Ville de Paris, Empreva, Engie, BNP, EIB, Stellantis, EDF, RATP, CNRS, Disney, BASF.
- Regulatory context: EU Directive 89/391/EEC; France law 2021-1018 of 2 August 2021 (DMST, prevention passport, interoperability of occupational health information systems by 1 January 2024), decree 2022-1434 of 15 November 2022 on the DMST, DUERP; Belgium Code on well-being at work, internal/external prevention services, Fedris; ISO 45001.
- Market context (official sources to cite): Padoa raised EUR 80M (February 2022, Five Arrows Growth Capital); Val Solutions uEgar covers 12 million workers and 12,000 health professionals in France; IDEWE is Belgium's largest external prevention service (35,000 employers, ~880,000 employees); Mensura serves 50,000+ customers; more than 99.5% of Belgian companies use an external prevention service.
