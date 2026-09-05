# ID Spine — paramedical-and-mental-health-practice-platform

Authoritative ID contract for this domain. Every artifact file MUST use exactly these
IDs when referencing entities owned by another file. Names/descriptions here are
one-liners; the artifact author expands them to reference-domain density.
All ids lowercase. Modeled on Health Cloud Initiative (HCI) (see DOMAIN.md).

## Customer groups and customers (customers.json)

Group "Paramedical Practices" — first-line paramedical practices on FysioRoadmap, SpotOnMedics, Incura, Evry, ParaNICE and HCI One; HCI supports "1 in 4 paramedics" in the Netherlands:
- `fyth` — Physiotherapy Practice Owner. Owner-therapist of a practice with 2–15 physiotherapists on one or more locations; treats patients, runs the agenda, declares to insurers through Vecozo, delivers LDF/Keurmerk data, is contracted by insurers with quality and administrative conditions; reports about a working day per week lost to administration; chooses between FysioRoadmap, SpotOnMedics and now HCI One.
- `alth` — Allied Health Therapist. Speech therapist, occupational therapist, exercise therapist, dietitian or podiatrist in a solo or small multidisciplinary practice (Incura, Evry); needs discipline-specific care pathways, measurement instruments and declaration rules, and works with GPs, schools and municipalities.
- `rhab` — Rehabilitation and Hospital Paramedical Coordinator. Team lead of a paramedical or rehabilitation department in a hospital or rehabilitation centre using paraNICE and NICE Connect alongside the hospital information system; coordinates multidisciplinary trajectories and remote follow-up (e.g. Amsterdam UMC premature infant network).

Group "Mental Health Care (GGZ)":
- `ggzp` — Independent GGZ Practitioner. Vrijgevestigde GZ-psychologist, psychotherapist or clinical psychologist (often an LVVP member) with a practice of 1–5 professionals on HCI CRS; registers and declares under the zorgprestatiemodel, uses ROM questionnaires and e-health modules, manages waiting lists above the 14-week Treeknorm.
- `ggzi` — GGZ Institution Application Manager. Functioneel beheerder / zorgadministratie lead of a GGZ or youth care institution with 50–500 professionals on HCI CRS, Quli and Embloom; owns registration compliance, municipal Jeugdwet/WMO contracts, integrations (ZorgDomein, ZorgMail, Bergop, Therapieland), client portal roll-out and reporting.

Group "Patients and Primary Care Network":
- `ptnt` — Patient and Client. Citizen using the Uw Zorg Online app or Quli PGO to reach their GP, pharmacy, therapist or GGZ institution: e-consult, appointments, repeat prescriptions, records, self-measurements and sharing with family; one of 4 million+ users.
- `gpph` — GP Practice and Pharmacy Manager. Practice manager or pharmacist whose HIS/AIS (Pharmapartners, CGM, Sanday, HealthConnected) connects to Uw Zorg Online as the digital front door, with a practice website and triage; wants fewer phone calls and MedMij compliance.

Group "Partners and HCI Operations":
- `intp` — Integration Partner. Vendor of an exercise app, questionnaire set, quality register, accounting, payment or HIS/AIS system (Physitrack, Qualiview, Twinfield, Mollie, Vecozo, ZorgDomein, MedMij) connecting to HCI's open platform to reach 40,000+ professionals.
- `impl` — Implementation and Support Consultant. HCI staff member who onboards practices, migrates acquired labels into HCI One, trains users, resolves support tickets and handles declaration return messages for billing-service customers.

### JTBD ids (customers.json jobsToBeDone; insights link jobIds to these)
- fyth: `jtbd-fyth-1` Run the agenda and get every treatment declared and paid without rework, `jtbd-fyth-2` Keep guideline-compliant records and quality data with minimal typing, `jtbd-fyth-3` Fill the agenda and keep patients engaged between sessions.
- alth: `jtbd-alth-1` Record and declare discipline-specific care correctly, `jtbd-alth-2` Work with GPs, schools and municipalities without double registration, `jtbd-alth-3` Measure progress and show outcomes to patients and payers.
- rhab: `jtbd-rhab-1` Coordinate multidisciplinary rehabilitation trajectories next to the hospital system, `jtbd-rhab-2` Follow patients remotely after discharge, `jtbd-rhab-3` Report department productivity and outcomes.
- ggzp: `jtbd-ggzp-1` Register and declare under the zorgprestatiemodel first time right, `jtbd-ggzp-2` Treat with ROM and e-health integrated in the dossier, `jtbd-ggzp-3` Manage intake, waiting list and client contact from one place.
- ggzi: `jtbd-ggzi-1` Keep registration and declarations compliant across financiers, `jtbd-ggzi-2` Roll out the client portal and e-health to all teams, `jtbd-ggzi-3` Integrate the EPD with the institution's application landscape.
- ptnt: `jtbd-ptnt-1` Reach my care providers and arrange things without calling, `jtbd-ptnt-2` See and share my health data on my own terms, `jtbd-ptnt-3` Follow my treatment programme at home.
- gpph: `jtbd-gpph-1` Give patients a digital front door that cuts phone traffic, `jtbd-gpph-2` Meet MedMij and Wegiz obligations without extra work, `jtbd-gpph-3` Keep the practice findable and up to date online.
- intp: `jtbd-intp-1` Integrate once and reach every HCI label, `jtbd-intp-2` Keep the connection reliable through release changes.
- impl: `jtbd-impl-1` Take a practice live on schedule with clean data, `jtbd-impl-2` Migrate a label's customers into HCI One without losing them, `jtbd-impl-3` Resolve support and return-message issues fast.

### North-star KPI names (use these VERBATIM as pyramid node names; productStrategy northStar must match)
- fyth: north star "Administration minutes per treatment"; supporting include "Declaration first-time acceptance rate", "Online booking share".
- alth: north star "Administrative time per client contact"; supporting include "Declaration first-time acceptance rate", "Care pathway template coverage".
- rhab: north star "Trajectory coordination time per patient"; supporting include "Remote follow-up completion rate", "Department report preparation time".
- ggzp: north star "Direct client time share"; supporting include "Zorgprestatiemodel rejection rate", "ROM completion rate".
- ggzi: north star "Registration-to-declaration lead time"; supporting include "Client portal activation rate", "E-health module usage rate".
- ptnt: north star "Care tasks completed digitally"; supporting include "E-consult response time", "Appointment self-service rate".
- gpph: north star "Digital front door adoption rate"; supporting include "Phone contacts per 1,000 patients", "Repeat prescription digital share".
- intp: north star "Integration time to live"; supporting include "Partner API availability", "Partner-initiated transactions per month".
- impl: north star "Go-live on schedule rate"; supporting include "Migration data defect rate", "Support ticket resolution time".

KPI node id convention (mirrors freelancer-bookkeeping-service-platform): `co-<cust>-top`, `co-<cust>-b1`, `co-<cust>-b1-c1`, `co-<cust>-b1-c1-l1` … and `bo-<cust>-…` for businessOutcomes. Every non-leaf has ≥2 children; target 4 levels (1+2+4+8). Set `icon` fields as `kpi-<cust>-<nodeid>.png`; icon files are backfilled later. Seed values must be arithmetically consistent across personas.
Customer icons: use `<cust>.png` (e.g. `fyth.png`) — backfilled later. Do NOT set `media` fields on JTBDs, journeys or relations (no images exist).

## Streams (product-stream.json; JTBD steps reference via streamsNeeded — use these ids only)

- `schedule-appointments-and-online-booking` — From a referral or patient request to a booked slot: multi-therapist, multi-location agenda, 24/7 online booking from the practice website, waiting list, reminders, group lessons and subscriptions, mobile agenda.
- `keep-the-electronic-patient-record` — From intake to closed episode: discipline-specific care pathways and guideline templates (KNGF, NVLF, NVD), clinical notes, voice-to-text and AI summaries, documents and correspondence, dossier audit rules.
- `measure-outcomes-with-proms-and-rom` — From questionnaire selection to outcome dashboards: PROMs and measurement instruments in the treatment, ROM for GGZ, benchmarks, and monthly pseudonymised delivery to LDF, Keurmerk and other quality registers under opt-in consent.
- `declare-and-get-paid` — From registered treatment to money on the account: insurance eligibility (COV), GDS801 declarations and zorgprestatiemodel claims through Vecozo, return-message handling, patient invoices with Mollie payments, billing services and accounting export (Twinfield).
- `coordinate-ggz-treatment-and-medication` — From GGZ intake and diagnosis to a multidisciplinary treatment plan: settings and professionals under the zorgprestatiemodel, medication, group treatment, youth care and municipal (Jeugdwet/WMO) contracts and iJw/iWmo messaging.
- `deliver-blended-and-e-health-care` — From a treatment plan to a blended programme: Embloom questionnaires and interventions, exercise programmes from partners, Emogy behavioural support, video consultation and NICE Connect remote trajectories, monitoring of home tasks.
- `engage-patients-through-portal-and-app` — From an invitation to an active patient: Uw Zorg Online and CRS client portal activation, e-consult, appointment self-service, repeat prescriptions, record access, digital triage, notifications.
- `manage-personal-health-data-and-sharing` — From MedMij consent to a Quli or Uw Zorg Online PGO: retrieving data from GP, hospital and GGZ systems, self-measurements and diaries, granular sharing with family and informal carers, network care.
- `refer-and-exchange-with-the-care-network` — From referral to closed loop: ZorgDomein referrals, ZorgMail secure messaging, HIS/AIS connectors for GP and pharmacy systems, hospital information system links for paraNICE, reports back to the referrer.
- `run-the-practice-with-management-insight` — From registrations to decisions: practice BI dashboards on production, revenue, treatment duration, referrers and waiting times, GGZ institution reporting, contract monitoring per insurer or municipality.
- `publish-and-run-a-practice-website` — From template to findable practice: practice websites with online booking, e-consult and triage entry points, content management, hosting and accessibility.
- `integrate-partners-through-the-open-platform` — From partner agreement to live connection: partner API onboarding, credentials and consent, versioned interfaces across labels, monitoring and release coordination.
- `onboard-migrate-and-consolidate-labels` — From a signed practice or acquired label to live users on HCI One: data migration and validation, configuration, training, phased per-discipline rollout, support and hypercare.
- `secure-and-comply-with-health-information-standards` — From regulation to evidence: NEN 7510 and ISO 27001 controls, AVG consent and retention, audit logs, UZI/DigiD authentication, Wegiz and MedMij conformance, incident response.

14 streams.

## Product bricks (product-bricks.json) — root group → subgroup → bricks

Root "Paramedical Practice Management and EPD":
- Subgroup "Scheduling and Booking": `agnd` Agenda and Multi-location Scheduling, `obok` Online Booking, Waiting List and Reminders, `grpm` Group Lessons, Programmes and Subscriptions.
- Subgroup "Clinical Record": `dosr` Patient Dossier and Care Pathways, `clin` Clinical Guidelines and Discipline Templates, `vtxt` Voice-to-Text and AI Documentation, `meas` Measurement Instruments and PROMs.
- Subgroup "Declarations and Payments": `decl` Declaration Engine (GDS801 and Zorgprestatiemodel), `vcgw` Vecozo Gateway and Insurance Eligibility, `pinv` Patient Invoicing and Payments, `bils` Billing Services and Return-message Handling.
- Subgroup "Insight and Quality": `bidb` Practice BI Dashboards and Reporting, `qdat` Quality Data Delivery (LDF, Keurmerk, Benchmarks).

Root "Mental Health Care EPD (CRS)":
- Subgroup "Treatment and Coordination": `trpl` Treatment Plans and Multidisciplinary Coordination, `medm` Medication Management, `romq` ROM and Questionnaire Orchestration for GGZ, `cpor` GGZ Client Portal.
- Subgroup "Registration and Financing": `zpmc` Zorgprestatiemodel Registration and Compliance, `jzrg` Youth Care and Municipal Contracting (Jeugdwet/WMO).

Root "Patient Environments":
- Subgroup "Uw Zorg Online": `pgoa` Patient App and Web Portal, `econ` E-consult and Secure Messaging, `rxrp` Repeat Prescriptions and Medication Overview, `appb` Patient Appointment Self-service, `trig` Digital Triage.
- Subgroup "Quli Personal Health Environment": `pgom` MedMij Data Exchange and Consent, `netw` Network Care and Family Sharing, `diar` Self-measurements and Diaries.

Root "E-health and Remote Care":
- Subgroup "Content and Programmes": `qlib` Questionnaire and Intervention Library (Embloom), `bldc` Blended Care Programme Builder and Monitoring, `emgy` Emogy Behavioural Support App.
- Subgroup "Remote Care": `vidc` Video Consultation and NICE Connect Trajectories, `exrc` Exercise Programme Integration.

Root "Network and Integration":
- Subgroup "Care Network Exchange": `zdom` Referral and Secure Messaging Hub (ZorgDomein, ZorgMail), `hisc` HIS/AIS and Hospital System Connectors.
- Subgroup "Open Platform and Web": `papi` Partner API and Open Platform, `pweb` Practice Websites, `mobi` Zorgverlener Mobile App.

Root "Platform Foundation":
- Subgroup "Core Services": `iden` Identity, Access and Strong Authentication (UZI/DigiD), `audt` Audit Log, Consent and Information Security, `tnnt` Multi-tenant Cloud Runtime and Label Migration Tooling, `supp` Customer Support and Onboarding Tooling.

41 bricks (13 + 6 + 8 + 5 + 5 + 4). Module ids must start with `module-` (e.g. `module-agnd-web`, `module-agnd-api`). `backoffice-interface` modules belong in the `interfaces` layer, never `ui`. A `message-queue` module must never be the caller of another brick's API. Brick dependencies point consumer → provider.

### Brick dataDependencies → data asset ids (see below); wire at least these
agnd→appointment,patient-profile,practitioner-profile; obok→appointment,practice-website; grpm→group-programme,patient-invoice; dosr→patient-profile,treatment-episode,clinical-note; clin→care-pathway-template,treatment-episode; vtxt→clinical-note,audit-log-entry; meas→measurement-result,questionnaire-definition; decl→declaration-claim,treatment-episode,insurer-contract; vcgw→insurance-eligibility-check,declaration-claim,return-message; pinv→patient-invoice,payment-transaction; bils→return-message,declaration-claim; bidb→practice-kpi-snapshot,treatment-episode; qdat→quality-data-extract,measurement-result,data-sharing-consent; trpl→treatment-plan,treatment-episode,practitioner-profile; medm→medication-record,patient-profile; romq→measurement-result,questionnaire-definition; cpor→client-portal-account,e-consult-message; zpmc→declaration-claim,treatment-plan,insurer-contract; jzrg→municipal-assignment,declaration-claim; pgoa→client-portal-account,patient-profile; econ→e-consult-message,client-portal-account; rxrp→repeat-prescription-request,medication-record; appb→appointment,client-portal-account; trig→triage-session,client-portal-account; pgom→medmij-consent,health-data-import; netw→family-share-permission,client-portal-account; diar→self-measurement,health-data-import; qlib→questionnaire-definition,e-health-programme; bldc→e-health-programme,home-task-progress; emgy→home-task-progress,e-health-programme; vidc→video-session,remote-care-trajectory; exrc→exercise-programme-link,home-task-progress; zdom→referral-message,practitioner-profile; hisc→his-connection,patient-profile; papi→partner-api-credential,integration-event; pweb→practice-website,appointment; mobi→user-identity,appointment; iden→user-identity,practitioner-profile; audt→audit-log-entry,data-sharing-consent; tnnt→tenant-configuration,migration-batch; supp→support-ticket,tenant-configuration.

## Data assets (data/data-assets.json) — id → ownerTeamId

- `patient-profile` → clinical-record-team
- `practitioner-profile` → platform-security-team
- `appointment` → agenda-and-booking-team
- `group-programme` → agenda-and-booking-team
- `treatment-episode` → clinical-record-team
- `clinical-note` → clinical-record-team
- `care-pathway-template` → clinical-record-team
- `measurement-result` → clinical-record-team
- `questionnaire-definition` → embloom-content-team
- `declaration-claim` → declarations-and-payments-team
- `insurance-eligibility-check` → declarations-and-payments-team
- `return-message` → declarations-and-payments-team
- `patient-invoice` → declarations-and-payments-team
- `payment-transaction` → declarations-and-payments-team
- `insurer-contract` → ggz-registration-and-financing-team
- `municipal-assignment` → ggz-registration-and-financing-team
- `practice-kpi-snapshot` → insight-and-quality-team
- `quality-data-extract` → insight-and-quality-team
- `treatment-plan` → crs-treatment-team
- `medication-record` → crs-treatment-team
- `client-portal-account` → uw-zorg-online-team
- `e-consult-message` → uw-zorg-online-team
- `repeat-prescription-request` → uw-zorg-online-team
- `triage-session` → uw-zorg-online-team
- `medmij-consent` → quli-and-medmij-team
- `health-data-import` → quli-and-medmij-team
- `family-share-permission` → quli-and-medmij-team
- `self-measurement` → quli-and-medmij-team
- `e-health-programme` → embloom-content-team
- `home-task-progress` → remote-care-team
- `video-session` → remote-care-team
- `remote-care-trajectory` → remote-care-team
- `exercise-programme-link` → remote-care-team
- `referral-message` → care-network-integration-team
- `his-connection` → care-network-integration-team
- `partner-api-credential` → open-platform-team
- `integration-event` → open-platform-team
- `practice-website` → open-platform-team
- `user-identity` → platform-security-team
- `audit-log-entry` → platform-security-team
- `data-sharing-consent` → platform-security-team
- `tenant-configuration` → cloud-runtime-and-migration-team
- `migration-batch` → cloud-runtime-and-migration-team
- `support-ticket` → implementation-and-support-team

44 assets. Personal-data level is high (medical data, BSN, medication, psychological questionnaires); tag AVG/GDPR special-category health data, WGBO (medical file retention 20 years), NEN 7510, Wegiz, MedMij, zorgprestatiemodel and Jeugdwet retention rules. Data residency EU/Netherlands.

## Teams (teams.json) — every brick owned by exactly one team

HCI has ~250 staff in the Netherlands and Switzerland, organised in business units (paramedical, GGZ, patient platforms, e-health) plus shared platform, integration and customer operations. Model ~245 people: product/engineering teams of 6–12, customer operations larger.

Org group "Paramedical Business Unit":
- `agenda-and-booking-team` (stream-aligned) owns agnd, obok, grpm
- `clinical-record-team` (stream-aligned) owns dosr, clin, vtxt, meas
- `declarations-and-payments-team` (complicated-subsystem) owns decl, vcgw, pinv, bils
- `insight-and-quality-team` (stream-aligned) owns bidb, qdat

Org group "GGZ Business Unit":
- `crs-treatment-team` (stream-aligned) owns trpl, medm, romq, cpor
- `ggz-registration-and-financing-team` (complicated-subsystem) owns zpmc, jzrg

Org group "Patient Platforms":
- `uw-zorg-online-team` (stream-aligned) owns pgoa, econ, rxrp, appb, trig
- `quli-and-medmij-team` (stream-aligned) owns pgom, netw, diar

Org group "E-health":
- `embloom-content-team` (stream-aligned; psychologists and content developers in Maastricht) owns qlib, bldc, emgy
- `remote-care-team` (stream-aligned) owns vidc, exrc

Org group "Platform and Integration":
- `care-network-integration-team` (platform) owns zdom, hisc
- `open-platform-team` (platform) owns papi, pweb, mobi
- `platform-security-team` (platform) owns iden, audt
- `cloud-runtime-and-migration-team` (platform) owns tnnt

Org group "Customer Operations":
- `implementation-and-support-team` (stream-aligned; onboarding, training, support desk, billing services) owns supp; customer dependencies on impl, fyth, ggzi

Team customer dependencies: paramedical teams → fyth, alth, rhab; GGZ teams → ggzp, ggzi; patient platforms → ptnt, gpph; e-health → ggzp, ggzi, ptnt; integration/open platform → intp, gpph; security → ggzi; runtime/migration → impl. Consumer → provider team dependencies only (no "Provides …" edges). Team metrics must be KPI names that exist in the persona pyramids and that the team can move.

15 teams.

## Products (product-deployments/products.json) — id, primary customers

- `hci-one` — HCI One multidisciplinary paramedical platform (built on FysioRoadmap; consolidates 8 labels; physiotherapy first) — fyth, alth
- `fysioroadmap` — FysioRoadmap physiotherapy EPD and agenda — fyth
- `spotonmedics` — SpotOnMedics physiotherapy practice software (online booking, mobile agenda, BI, Mollie, billing services, group management) — fyth
- `incura` — Incura multidisciplinary paramedical EPD (~7,500 providers) — alth, fyth
- `evry` — Evry dietitian and weight-consultant practice software — alth
- `paranice` — ParaNICE and NICE Connect for paramedical and rehabilitation care in hospitals — rhab
- `hci-crs` — HCI CRS all-in-one EPD for GGZ and youth care — ggzp, ggzi
- `uw-zorg-online` — Uw Zorg Online patient app and portal (4 million+ users) — ptnt, gpph
- `quli` — Quli personal health environment (MedMij) — ptnt, ggzi
- `embloom` — Embloom e-health platform (500+ questionnaires, 450 interventions) — ggzp, ggzi
- `emogy` — Emogy client app for cognitive and behavioural support — ptnt, ggzi
- `zorgverlener-app` — Zorgverlener App for professionals on the go — fyth, alth
- `praktijkwebsites` — Practice websites with online booking and portal entry — gpph, fyth
- `hci-partner-platform` — Partner API and integration programme — intp
- `implementation-and-billing-services` — Onboarding, migration, training and billing services (internal/professional services) — impl, fyth

15 products. Use `<product-id>.png` icons (rendered later into product-deployments/icons). `neededBricks`/`interfaces` are retired fields; brick coverage is expressed via deployment.json `usedInProducts`.

## Deployment channels (deployment.json; maas is the structural reference)

Channel groups: "Web Applications" (practitioner web apps for each label and HCI One; CRS web client; Uw Zorg Online web portal; Quli web; Embloom professional portal; practice websites), "Mobile Apps" (Uw Zorg Online iOS/Android app; Quli app; Zorgverlener App; Emogy app; mobile agenda), "Integrations" (Vecozo declarations and COV, ZorgDomein, ZorgMail, HIS/AIS connectors, MedMij DVZA, LDF/Keurmerk delivery, Physitrack and exercise partners, Twinfield, Mollie, partner API), "Document Outputs" (declaration files and return messages, patient invoices, treatment reports and referral letters, quality data extracts), "Internal Operations" (tenant configuration, migration tooling, support desk, billing-service back office). Map deployedBricks with usedInProducts referencing product ids above.

## Sourced company facts (reuse consistently; do not invent numbers)

- HCI (Health Cloud Initiative), hci-software.com; mission "Better care, made easy"; 40,000+ healthcare professionals daily and 4 million+ patients (2025); 3.5 million+ people helped with digital care and 200+ colleagues (site); 250+ employees in the Netherlands and Switzerland (May 2025); 30+ years of combined experience; NEN 7510 and ISO 27001 certified; cloud-based open platform with partner ecosystem.
- Vortex Capital Partners: buyout 2021 with founder Eric de Boer (formerly Winbase; founder of Incura); June 2022 announcement: 7,500+ professionals, €500 million+ annual declarations, 45+ team members, 2 million+ patients, ambition 20,000 professionals; "more than 14 add-on acquisitions" since 2021; turnover €20 million and 30,000+ providers reported September/October 2023.
- Acquisitions: Incura, CRS, FysioRoadmap, Winbase and two customer portfolios (by 2022); Ensemble/Evry (Alphen aan den Rijn, founded 1996, market leader for dietitians) and Footfit/PodoFile (January 2023, 18,000+ providers after); NICE Software (paraNICE, NICE Connect; May 2023; 21,000+ workers after); Uw Zorg Online (merged June 2023; 3 million users, 20+ years); Quli (September 2023; previously five care organisations, NextGen Ventures and Ordina); Praktijkinfo practice websites (October 2023); Embloom (July 2024; founded 2010 as TelePsy in Maastricht by Marco Essed, 35 employees, 500+ questionnaires, 300+ treatment modules, 270,000+ users per year, ~2,500 organisations, NL/BE/DE, ISO 27001 and NEN 7510; HCI then 35,000 providers and 3.5 million users); SpotOnMedics (August 2024, from VvAA; founded 2011, Hoofddorp; director Geert van den Enden; HCI "market leader in physiotherapy software", "1 in 4 paramedics"); also Trompbx, LogicData (FysioLogic), Abakus, Edevop.
- Leadership: Marc Prette CEO (two years, to 2025); Robin Dunki Jacobs CEO from 1 May 2025 (joined 2024 as Business Unit Director integrating labels); strategy: integrate acquired solutions, expand digital patient access through a unified network, invest in digital triage, AI and e-health.
- Products: HCI One (multidisciplinary paramedical platform on the FysioRoadmap web foundation consolidating FysioRoadmap, SpotOnMedics, Incura, Evry, Abakus, Podofile, Edevop, FysioLogic; phased per discipline, physiotherapy first, no forced migration); FysioRoadmap (agenda as central hub, invoices generated from the agenda, Vecozo, web-based; partners Physitrack, FysioTopics, Qualiview, Twinfield, Fysiovergoeding, ZorgMail); SpotOnMedics (online booking 24/7, mobile agenda, BI tooling, specialisation cards, EU cloud, Mollie payments, billing services, group management; custom quote within one business day); Incura (physio, speech, OT, exercise therapy, dietetics; ~7,500 providers, 2 million+ patients, 20 years; partners Physitrack, Mollie, Abakus, Vecozo, Kiwa, KNGF, Philips, MediQuest, QualiView); Evry (dietetics); ParaNICE (multidisciplinary cloud registration supporting hospital information systems) and NICE Connect (remote trajectories since 2014 with Amsterdam UMC premature infant network; German rehabilitation centres; Emogy autism environment); HCI CRS (all-in-one EPD for GGZ and youth care: dossiers, treatment plans, medication, agenda, declarations, central client portal, SmartAI voice-to-text, reporting; integrations Embloom, Bergop, Therapieland, ZorgDomein, ZorgMail, Minddistrict; custom quote); Uw Zorg Online (e-consult, records, medication and repeat prescriptions, self-measurements, appointment booking in the agenda, triage; connects to Sanday, HealthConnected, Pharmapartners, CGM, Bricks, Vertimart; MedMij; DigiDok, Quin, "Moet ik naar de Dokter?"; 3 million+ app users; HCI won a MedMij PGO tender); Quli (PGO with MedMij label, fifth PGO provider; GGZ appwijzer with 50+ apps; secure messaging and video, diary, reminders, single login for e-health apps, sharing control; IC aftercare; 2 top-50 GGZ organisations in 2025); Embloom (500+ questionnaires, 450 e-health interventions, fully integrated in the EPD, hybrid care, GGZ and somatic); Emogy; Zorgverlener App; Praktijkwebsites.
- Partners named on hci-software.com: DigiDoc, HC, QUIN, ProMedico, Pharmapartners, MicroHIS, Fysio AI, PhysioTrack, Vecozo.
- Regulatory/market: GDS801 replaced PM304 for paramedical declarations on 1 January 2025 (developed with PPN, KNGF, ZN, Vektis, Vecozo and EPD vendors); zorgprestatiemodel 2026: mandatory referral date on every declaration, system therapist added to professional standards, transitional benefit ended, core model unchanged; Wegiz in force April 2023; 16 MedMij-labelled PGOs (November 2025); ~50% of GGZ institutions connected to PGOs, paramedical care still exploratory; LDF: monthly pseudonymised delivery from the EPD, opt-in patient consent, Keurmerk practice register requires it; Nivel 2024: 7,848 physiotherapists in 543 registered practices, 1,162,545 patients; physiotherapists spend about a full working day per week on administration (VFW) and 1 in 5 report work disability due to stress (Movir, 715 respondents); GGZ waiting times exceed the 14-week Treeknorm in all regions H1 2025 (basic GGZ exactly at the norm); NZa indexes 2026 tariffs for independent GGZ practitioners.

## Competitor facts (business/competition.json; official sources only; keep reported scope)

- Intramed (intramed.nl; product of Convenient B.V., Moordrecht): physio, podiatry, speech, OT, GGZ, dietetics, exercise therapy, skin therapy, haptotherapy, osteopathy; products Intramed Compleet/Web/OnLine/Plus/Basis, HealthTrain, MijnZorgApp, Fysio.AI, Intramed Insight, AfsprakenApp, ParaBench, GGZ praktijkdashboard, Intramed Financieel, D-Pay; ISO 9001, ISO/IEC 27001, NEN 7510 ("first practice software supplier certified"); 3 months free trial; 53% calculated market share among physiotherapy practices (Marktdata 2017, third-party, dated).
- Fysiomanager (fysiomanager.nl; Heerenveen): browser-based EPD for paramedics, FM-VideoConsult, online scheduling, MijnZorgtoegang patient portal, FM Analytics, Twinfield, iDEAL/Wero; NEN 7510 and ISO/IEC 27001; ~90% satisfaction; multi-location included; integrations with SpotOnMedics and Intramed.
- Crossuite (crossuite.com; Belgium/Netherlands): 9 disciplines incl. physio, speech, psychology, podiatry, dietetics; "10,000 practitioners", "13 countries", "98% customer satisfaction", 18 years.
- James Software (jamessoftware.nl): paramedical EPD listed among Dutch physiotherapy options (Physitrack 2026 comparison); no verifiable stats — description only.
- Nedap Ons (nedap-ons.nl; Nedap N.V., listed, Groenlo): VVT, GHZ, GGZ, HBH; "over 1,900 care organisations", "approximately 400,000 care professionals"; 14 of top-50 GGZ organisations (27%) and Caren portal 22.5% (M&I/Partners 2025).
- SDB Groep / USER and Karify (sdbzorgt.nl): USER EPD developed by Avinty, part of SDB Groep since 1 April 2023; 45+ years in care; 15 of top-50 GGZ organisations (30%), Karify portal 22.5% (M&I/Partners 2025); GGZ Friesland switched to Nedap in 2025.
- PinkRoccade GGZ (pinkroccade-ggz.nl, official site to confirm; part of TSS/Total Specific Solutions): mijnQuarant and mQ suite; 7 of top-50 (14%); mQ suite at Parnassia Groep (M&I 2025).
- Adapcare (adapcare.nl; Ede; part of CareRatio): Pluriform Zorg ECD and App Anne; GGZ, disability, youth, social support, VVT; "55,000+ users"; 6 of top-50 GGZ (12%).
- Nexus Nederland (nexus-nederland.nl): modular EPD/ECD for GGZ institutions; 5 of top-50 (10%), down from 7 (M&I 2024/2025).
- Medicore (medicore.nl; Utrecht, Kanaalweg 29): "complete and open ECD for clinical and outpatient GGZ, youth care and independent clinics"; Mijn Medicore, Zorgapp, UP, API platform, Wellbee client portal; 20+ partners (AI agents, speech-to-text, e-health).
- Minddistrict (minddistrict.com; Amsterdam): e-health platform, "250,000+ users", ISO 27001:2022, NEN 7510-1:2017, CE Class I medical device; modules, diaries, questionnaires, video, messaging; customers GGZ Delfland, GGZ NHN, Lentis, Tactus; also integrates with CRS.
- Therapieland (therapieland.nl; Amsterdam): "largest e-health platform of the Netherlands", 300+ online programmes, 200+ questionnaires; integrates with HCI GGZ, Nedap ONS, Medicore, Careweb, Medicom, Ksyos; partnered with QuestManager.
- Madeware Medikad (madeware.nl): affordable EPD for independent psychologists and GGZ therapists, also physio/speech/youth/OT; questionnaires (SQ48, CQi, HoNos, 4DKL), Vecozo, GDS801-PM integrated, 3 months free trial.
- Praktijkdata (praktijkdata.nl; Telasoft): fully web-based GGZ EPD for independent practitioners and organisations; youth care, WMO and zorgprestatiemodel; Vecozo declarations; client portal and e-health.
- Axians Zorg GGZ (axians.nl): ECD for private practices and mid/large GGZ organisations in adult and youth GGZ.
- Physitrack (physitrack.com): exercise/e-health partner, not a competitor (11 Dutch EPD integrations incl. Intramed, Incura, Abakus, Fysiomanager, SpotOnMedics; 1,500+ Dutch clinicians; ISO 27001/13485).
Every business stat must carry an official source URL and reported scope; leave stats out rather than invent them. Third-party market-share figures must cite mxi.nl or marktdata.nl with the scope "top-50 GGZ organisations by revenue" or "2017 survey".
