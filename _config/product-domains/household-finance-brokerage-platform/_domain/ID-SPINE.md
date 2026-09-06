# ID Spine — household-finance-brokerage-platform

Authoritative ID contract for this domain. Every artifact file MUST use exactly these
IDs when referencing entities owned by another file. Names/descriptions here are
one-liners; the artifact author expands them to reference-domain density.
All ids lowercase. Modeled on Peasy / hypotheek.winkel / Verzekeringen.be / Aanbieders.be (see DOMAIN.md).

## Customer groups and customers (customers.json)

Group "Households Comparing and Switching" — Belgian consumers (Flanders and Brussels first, Wallonia via Meilleurtaux) who want to pay less for their recurring contracts without doing the paperwork:
- `fthb` — First-time Home Buyer. Couple or single (often late twenties to thirties) buying a first home in Flanders; wants to know how much they can borrow, prove it to sellers with a feasibility certificate, compare 25 banks without visiting them, understand notary costs, the EPC renovation obligation, outstanding-balance (schuldsaldo) and fire insurance; reaches Peasy via simulators, Google reviews or a friend, meets an expert in a nearby office or by video call.
- `refi` — Refinancing and Second-Project Owner. Existing mortgage holder who received a proposal from their own bank or elsewhere and wants it checked (upload-your-proposal), considers refinancing when rates move, or needs a renovation loan, a second home, a new build or financing as a self-employed person; price- and time-sensitive, values a one-page comparison and a quick expert verdict.
- `hshs` — Household Fixed-Cost Saver. Family that uses the budget barometer to see where it overpays versus the Belgian average and then compares and switches car, fire, funeral or outstanding-balance insurance, electricity and gas (meter type, digital meter, solar panels), internet/TV packs and mobile plans by phone, chat or self-service; wants Peasy to keep watching the contracts and to warn when it is cheaper elsewhere.

Group "Advisory Network" — the people who turn comparisons into concluded contracts:
- `hexp` — Mortgage Expert (hypotheek.expert). Advisor in a hypotheek.winkel office (about 150 experts across ~70 offices); listens to the buyer's project, compares the daily conditions of 25 banks on screen, issues feasibility certificates, assembles and submits the credit file, follows approval through compromis and notary deed, attaches insurance; a scarce-skill role (knelpuntberoep) largely trained in-house.
- `frnc` — Office Franchisee. Independent entrepreneur running one or more hypotheek.winkel offices under franchise; depends on the brand for appointments and leads, recruits and retains experts, wants clear production, conversion and commission reporting and local marketing support.
- `insa` — Customer-Care Advisor. Insurance, energy and telecom advisor in the Hasselt or Oujda customer-care centre; handles callback requests, phone and chat comparisons, quotes and policy binding across 11 insurers, energy and telecom switches, cancellations of old contracts, and follow-up of monitoring alerts; measured on first-contact resolution and error-free switches.

Group "Partners and Providers" — the organisations that pay the referral fees:
- `bank` — Lender Partner. One of the 25 banks whose mortgage conditions are compared daily; receives credit files from the broker channel, approves or declines them, pays a referral commission per concluded loan; wants complete, compliant files and predictable volume.
- `prov` — Insurer, Energy and Telecom Partner. One of the >50 partners (insurers such as those listed on Verzekeringen.be, energy suppliers, telecom operators) whose products appear in the comparison modules; supplies tariff and product data, receives switch orders and quotes, reconciles leads, contracts and commissions with Peasy.

Group "Peasy Operations":
- `opsm` — Network and Compliance Operations Manager. Head-office role in Zaventem responsible for the academy (about 30 advisors trained per year), partner contracts and tariff feeds, commission reconciliation and payout to the office network, FSMA registrations of intermediaries, advice-record quality, complaints and GDPR across three brands.

### JTBD ids (customers.json jobsToBeDone; insights link jobIds to these)
- fthb: `jtbd-fthb-1` Know how much I can borrow and prove it to sellers, `jtbd-fthb-2` Get the best total mortgage package from 25 banks without visiting them, `jtbd-fthb-3` Get from accepted offer to notary deed with loan and insurance in place.
- refi: `jtbd-refi-1` Find out fast whether my proposal or current loan can be beaten, `jtbd-refi-2` Finance a renovation, second home or new build on top of my situation, `jtbd-refi-3` Keep my loan-linked insurance optimal after the change.
- hshs: `jtbd-hshs-1` See where my household overpays compared with Belgian averages, `jtbd-hshs-2` Compare and switch insurance, energy and telecom in minutes without paperwork, `jtbd-hshs-3` Have someone watch my contracts and warn me when a better deal exists.
- hexp: `jtbd-hexp-1` Turn every appointment into a complete, bank-ready file quickly, `jtbd-hexp-2` Advise the best total package across 25 banks independently, `jtbd-hexp-3` Follow every file to the notary and attach the right insurance.
- frnc: `jtbd-frnc-1` Keep my office fed with qualified appointments, `jtbd-frnc-2` Recruit, train and retain experts and stay compliant, `jtbd-frnc-3` See my office's production, conversion and commissions clearly.
- insa: `jtbd-insa-1` Resolve a comparison request in one contact, `jtbd-insa-2` Execute switches and cancellations without errors, `jtbd-insa-3` Turn monitoring alerts into renewals and cross-sell.
- bank: `jtbd-bank-1` Receive complete, compliant credit files I can approve quickly, `jtbd-bank-2` Grow mortgage volume through the broker channel at predictable cost.
- prov: `jtbd-prov-1` Be listed accurately and win switches in the comparison modules, `jtbd-prov-2` Reconcile leads, contracts and commissions with the broker without disputes.
- opsm: `jtbd-opsm-1` Onboard and certify new advisors through the academy, `jtbd-opsm-2` Reconcile commissions from more than 50 partners and pay the network correctly, `jtbd-opsm-3` Prove FSMA and GDPR compliance across brands and offices.

### North-star KPI names (use these VERBATIM as pyramid node names; productStrategy northStar must match)
- fthb: north star "Days from first appointment to loan approval"; supporting include "Banks compared per file", "Feasibility certificate issuance rate".
- refi: north star "Savings identified per refinancing case"; supporting include "Proposal review turnaround time", "Refinancing conversion rate".
- hshs: north star "Annual household savings realised"; supporting include "Contracts switched per household", "Savings alert acceptance rate".
- hexp: north star "Files completed per expert per month"; supporting include "File first-time-complete rate", "Insurance attach rate".
- frnc: north star "Qualified appointments per office per month"; supporting include "Appointment-to-loan conversion rate", "Expert retention rate".
- insa: north star "First-contact resolution rate"; supporting include "Switches completed per advisor per day", "Switch error rate".
- bank: north star "File approval turnaround time"; supporting include "File completeness rate", "Broker channel loan volume".
- prov: north star "Switches won through comparison"; supporting include "Tariff feed accuracy", "Commission reconciliation lead time".
- opsm: north star "Advisors certified per year"; supporting include "Commission reconciliation cycle time", "Compliance audit findings".

KPI node id convention: `co-<cust>-top`, `co-<cust>-b1`, `co-<cust>-b1-c1`, `co-<cust>-b1-c1-l1` … and `bo-<cust>-…` for businessOutcomes. Every non-leaf has ≥2 children; target 4 levels (1+2+4+8). Set `icon` fields as `kpi-<cust>-<nodeid>.png`; icon files are backfilled later. KPI seed values must be arithmetically consistent within a persona (funnel totals vs per-segment leaves, child cost ≤ parent cost).
Customer icons: use `<cust>.png` (e.g. `fthb.png`) — backfilled later. Do NOT set `media` fields on JTBDs, journeys or relations (no images exist).

## Streams (product-stream.json; JTBD steps reference via streamsNeeded — use these ids only)

- `simulate-and-check-mortgage-feasibility` — From an online simulation (how much can I borrow, monthly repayment, notary costs, financial plan, feasibility check) to a feasibility certificate the buyer can show a seller.
- `book-and-hold-an-advisory-appointment` — From a website, callback or upload request to an appointment in the nearest of ~70 offices or by video call, with the expert prepared.
- `compare-mortgage-offers-across-banks` — From the buyer's situation and project to a same-screen comparison of the daily conditions of 25 banks and an independent recommendation of the best total package, including review of proposals received elsewhere.
- `assemble-and-submit-the-loan-file` — From document collection (income, savings, compromis, EPC) to a complete credit file submitted to the chosen bank, approval tracking and conditions.
- `close-the-loan-through-notary-and-insurance` — From bank approval through compromis, outstanding-balance and fire insurance, notary deed and disbursement, with the expert following up.
- `refinance-or-extend-an-existing-loan` — From a rate change, renovation obligation, second home or new-build plan to a refinancing or additional loan case.
- `compare-and-switch-insurance` — From a car, fire, funeral or outstanding-balance comparison across 11 insurers to a bound policy and the cancellation of the old one.
- `compare-and-switch-energy-contracts` — From postcode, meter type, digital meter and solar-panel data to an electricity and gas comparison and a switch executed with the new supplier.
- `compare-and-switch-telecom-and-mobile` — From current internet/TV/mobile usage to the cheapest pack and a switch under BIPT Easy Switch.
- `monitor-household-contracts-and-alert-savings` — From brokered contracts stored per household and the budget barometer to renewal alerts, re-comparison and a new switch.
- `serve-customers-through-customer-care` — From phone, chat, callback and e-mail contacts in Hasselt and Oujda to resolved requests with scripts, knowledge base and ticket follow-up.
- `run-the-franchise-office-network` — From lead routing and office onboarding to production, conversion and commission dashboards for franchisees and head office.
- `train-and-certify-advisors-in-the-academy` — From recruitment of career changers to certified mortgage experts and insurance advisors (about 30 per year) meeting FSMA knowledge requirements.
- `manage-partners-tariffs-and-commissions` — From partner contracts and tariff feeds to reconciled referral commissions from >50 partners and payout to offices and advisors.
- `comply-with-fsma-and-data-protection` — From FSMA registrations, advice and suitability records, complaints and consent to audit-ready evidence across brands.

15 streams.

## Product bricks (product-bricks.json) — root group → subgroup → bricks

Root "Consumer Comparison Platform":
- Subgroup "Mortgage Simulators": `simb` Borrowing Capacity and Monthly Repayment Simulator, `feas` Feasibility Check and Certificate, `ntry` Notary Costs and Financial Plan Calculator, `upld` Upload-Your-Proposal Intake.
- Subgroup "Comparison Modules": `insc` Insurance Comparison Module, `enrg` Energy Comparison Module, `tlcm` Telecom and Mobile Comparison Module, `bgtb` Budget Barometer.
- Subgroup "Engagement and Content": `appt` Appointment Booking and Office Locator, `cbck` Callback and Chat Requests, `cont` Content, Blog and FAQ Pages, `brnd` Multi-brand Site Shell and Language Routing.

Root "Mortgage Brokerage Workbench":
- Subgroup "Advice and Comparison": `rate` Daily Bank Rate and Conditions Feed, `cmpr` Multi-bank Proposal Comparison Engine, `advr` Advice Record and Suitability Assessment.
- Subgroup "Loan File and Closing": `cfil` Credit File and Document Collection, `bsub` Bank Submission and Approval Tracking, `clos` Closing, Notary and Disbursement Tracking, `refn` Refinancing and Renovation Loan Cases.

Root "Insurance, Energy and Telecom Brokerage":
- Subgroup "Quote, Bind and Switch": `iqte` Insurance Quote and Policy Binding, `swch` Energy and Telecom Switch Execution, `cncl` Cancellation and Old-Contract Termination.
- Subgroup "Customer Care": `tckt` Customer-Care Ticketing and Omnichannel Inbox, `know` Advisor Knowledge Base and Scripts.

Root "Household Relationship":
- Subgroup "Contract Monitoring": `cvlt` Household Contract Vault and Customer Account, `mntr` Renewal Monitoring and Savings Alerts, `crmx` Customer 360 and Cross-sell Engine.

Root "Network and Partner Operations":
- Subgroup "Franchise Network": `lead` Lead Routing and Distribution, `offc` Office and Franchise Management, `prod` Production and Conversion Dashboards, `acad` Academy Learning and Certification.
- Subgroup "Partners and Commissions": `pcat` Partner Product Catalogue and Tariff Feeds, `comm` Commission Reconciliation and Network Payout, `pprt` Partner Portal and Lead Exchange.

Root "Platform Foundation":
- Subgroup "Core Services": `iden` Identity, Consent and Access Control, `cmpl` Compliance, Complaints and Audit Trail, `intg` Integration Gateway (banks, insurers, energy and telecom APIs, e-signature, telephony), `anly` Analytics and Data Platform.

38 bricks. Module ids must start with `module-` (e.g. `module-simb-web`, `module-simb-api`). `backoffice-interface` modules belong in the `interfaces` layer, never `ui`. A `message-queue` module must not be the caller of another brick's API. Dependencies point consumer → provider only.

### Brick dataDependencies → data asset ids (see below); wire at least these
simb→simulation-result,lead; feas→feasibility-certificate,simulation-result; ntry→simulation-result; upld→uploaded-proposal,lead; insc→comparison-request,partner-product-tariff; enrg→comparison-request,partner-product-tariff; tlcm→comparison-request,partner-product-tariff; bgtb→budget-profile,comparison-request; appt→appointment,office-profile,lead; cbck→callback-request,lead; cont→content-article; brnd→customer-account,content-article; rate→bank-rate-sheet; cmpr→mortgage-proposal,bank-rate-sheet; advr→advice-record,mortgage-proposal; cfil→credit-file,credit-file-document; bsub→bank-submission,credit-file; clos→closing-milestone,policy-contract; refn→refinancing-case,mortgage-proposal; iqte→insurance-quote,policy-contract; swch→switch-order,comparison-request; cncl→cancellation-request,policy-contract; tckt→care-ticket,customer-account; know→knowledge-article; cvlt→household-contract,customer-account; mntr→savings-alert,household-contract; crmx→customer-360-profile,household-contract; lead→lead,office-profile; offc→office-profile,expert-profile; prod→production-metric,office-profile; acad→academy-enrolment,expert-profile; pcat→partner-product-tariff,partner-agreement; comm→commission-statement,network-payout; pprt→partner-agreement,lead; iden→user-identity,consent-record; cmpl→complaint-record,audit-trail-entry,advice-record; intg→bank-submission,switch-order,audit-trail-entry; anly→analytics-event,production-metric.

## Data assets (data/data-assets.json) — id → ownerTeamId

- `customer-account` → customer-engagement-team
- `user-identity` → platform-and-integration-team
- `consent-record` → platform-and-integration-team
- `audit-trail-entry` → platform-and-integration-team
- `simulation-result` → consumer-platform-team
- `feasibility-certificate` → consumer-platform-team
- `uploaded-proposal` → consumer-platform-team
- `budget-profile` → consumer-platform-team
- `content-article` → consumer-platform-team
- `comparison-request` → comparison-modules-team
- `partner-product-tariff` → comparison-modules-team
- `lead` → brokerage-tooling-team
- `appointment` → customer-engagement-team
- `callback-request` → customer-engagement-team
- `office-profile` → network-development-and-franchise
- `expert-profile` → network-development-and-franchise
- `production-metric` → network-development-and-franchise
- `bank-rate-sheet` → mortgage-workbench-team
- `mortgage-proposal` → mortgage-workbench-team
- `advice-record` → mortgage-workbench-team
- `credit-file` → mortgage-workbench-team
- `credit-file-document` → mortgage-workbench-team
- `bank-submission` → mortgage-workbench-team
- `closing-milestone` → mortgage-workbench-team
- `refinancing-case` → mortgage-workbench-team
- `insurance-quote` → brokerage-tooling-team
- `policy-contract` → brokerage-tooling-team
- `switch-order` → brokerage-tooling-team
- `cancellation-request` → brokerage-tooling-team
- `care-ticket` → brokerage-tooling-team
- `knowledge-article` → customer-care-centres
- `household-contract` → customer-engagement-team
- `savings-alert` → customer-engagement-team
- `customer-360-profile` → customer-engagement-team
- `academy-enrolment` → peasy-academy
- `partner-agreement` → partner-management-and-commissions
- `commission-statement` → partner-management-and-commissions
- `network-payout` → partner-management-and-commissions
- `complaint-record` → compliance-and-risk
- `analytics-event` → platform-and-integration-team

40 assets. Personal-data level is high for most (income, savings, national register number, health questions for outstanding-balance insurance, EAN meter numbers); tag GDPR, FSMA record-keeping for credit and insurance intermediation, Belgian Book VII Code of Economic Law (credit), IDD (insurance distribution), Central Individual Credit Register consultation.

## Teams (teams.json) — every brick owned by exactly one team

Peasy employs about 200 people (head office Zaventem, customer care Hasselt and Oujda) plus ~150 experts in ~70 largely franchised offices. Model the organisation at ~200 people: product and technology teams of 4–8, customer care ~45, office network ~70 head-office-side and franchise experts counted in the network team.

Org group "Product and Technology" (Zaventem):
- `consumer-platform-team` (stream-aligned) owns simb, feas, ntry, upld, bgtb, cont, brnd
- `comparison-modules-team` (stream-aligned) owns insc, enrg, tlcm, pcat
- `customer-engagement-team` (stream-aligned) owns appt, cbck, cvlt, mntr, crmx
- `mortgage-workbench-team` (stream-aligned) owns rate, cmpr, advr, cfil, bsub, clos, refn
- `brokerage-tooling-team` (stream-aligned) owns iqte, swch, cncl, tckt, lead
- `platform-and-integration-team` (platform) owns iden, intg, anly

Org group "Advisory Network and Customer Care":
- `hypotheek-winkel-office-network` (stream-aligned; ~150 experts in ~70 franchised offices across Flanders and Brussels) owns no bricks; brick dependencies on cmpr, cfil, bsub, clos, advr, appt, lead; customer dependencies on fthb, refi, hexp, frnc, bank
- `customer-care-centres` (stream-aligned; Hasselt and Oujda, ~45 advisors) owns know; customer dependencies on hshs, insa, prov
- `network-development-and-franchise` (enabling) owns offc, prod; customer dependencies on frnc, hexp
- `peasy-academy` (enabling) owns acad; customer dependencies on hexp, insa, opsm

Org group "Partners, Finance and Compliance":
- `partner-management-and-commissions` (stream-aligned) owns comm, pprt; customer dependencies on bank, prov, opsm
- `compliance-and-risk` (enabling) owns cmpl; customer dependencies on opsm, hexp

12 teams. Team metrics must be KPI names that exist in the pyramids of the team's customers (by NAME) and that the team can actually move.

## Products (product-deployments/products.json) — id, primary customers

- `peasy-comparison-platform` — peasy.be: one front door for mortgage simulators, insurance, energy and telecom comparison (NL/FR) — fthb, hshs
- `hypotheek-winkel-mortgage-advice` — hypotheek.winkel: free mortgage brokerage in ~70 offices comparing 25 banks — fthb, refi
- `feasibility-certificate` — Haalbaarheidscertificaat: proof of borrowing capacity for sellers — fthb
- `upload-your-proposal-review` — Free expert review of a mortgage or insurance proposal received elsewhere — refi, fthb
- `verzekeringen-be-insurance-comparison` — Verzekeringen.be / Assurances.be: car, fire, funeral, outstanding-balance and other insurance comparison across 11 insurers — hshs, refi
- `aanbieders-be-energy-and-telecom-switching` — Aanbieders.be / Mesfournisseurs.be: free energy, telecom and mobile comparison and switching — hshs
- `budget-barometer` — Household fixed-cost benchmark against Belgian averages — hshs
- `contract-monitoring-service` — Peasy watches brokered contracts and alerts when cheaper — hshs, refi
- `expert-workbench` — Mortgage expert workbench: bank comparison, credit file, submission and closing tracking (internal) — hexp, frnc
- `customer-care-desk` — Omnichannel care desk with quote, switch and cancellation tooling (internal) — insa
- `franchise-and-academy-programme` — Franchise onboarding, production dashboards and academy certification — frnc, hexp, opsm
- `partner-portal-and-commissions` — Partner portal, tariff feeds and commission reconciliation — bank, prov, opsm

12 products. Use `<product-id>.png` icons (rendered later into product-deployments/icons). `neededBricks` and `interfaces` are retired fields; brick coverage is expressed through deployment.json `usedInProducts`.

## Deployment channels (deployment.json; maas is the structural reference)

Channel groups: "Consumer Websites" (peasy.be, hypotheekwinkel.be, verzekeringen.be/assurances.be, aanbieders.be/mesfournisseurs.be — simulators, comparison modules, booking, upload, budget barometer, content), "Customer Account" (household contract vault, alerts, e-signature), "Advisor Workbenches" (expert workbench in offices, customer-care desk in Hasselt/Oujda, knowledge base), "Integrations" (bank rate feeds and file submission, insurer quote and bind APIs, energy and telecom switch interfaces, e-signature, telephony and chat, e-mail/SMS), "Network and Partner Back Office" (franchise management, production dashboards, academy LMS, partner portal, commission reconciliation, compliance and audit), "Documents" (feasibility certificate PDF, proposal comparison PDF, policy documents, commission statements). Map deployedBricks with usedInProducts referencing product ids above.

## Sourced company facts (reuse consistently; do not invent numbers)

- Peasy (easypeasy.be / peasy.be), HQ Zaventem; customer care in Hasselt and Oujda (Morocco); hypotheek.winkels across Flanders and Brussels; CEO David Geerts; ">150 experten, 70 winkels, >50.000 contracten afgesloten per jaar, >50 partners" (easypeasy.be/over-ons); "4,5/5 klanttevredenheid"; phone 03 501 22 22; NL and FR; brands "Onderdeel van een familie van merken"; revenue model: partners pay a referral fee (aanbrengvergoeding) when a contract is concluded via Peasy, consumer pays nothing extra; Peasy monitors contracts and warns when better or cheaper; customers never contract with Peasy itself (klantenservice FAQ).
- hypotheek.winkel (hypotheekwinkel.be; hypotheek.winkel BV, BE 0474.087.795, Zaventem): started 2001; "70 hypotheek.winkels"; compares 25 banks daily; free for the buyer, commission from the bank's head office; Trustpilot 4.8/5; feasibility certificate (haalbaarheidscertificaat) compares 25 banks on salary and savings, accounts for renovation obligation of low-EPC homes; simulators: hoeveel kan ik lenen, maandlast, rentevoet, financieel plan, notariskosten, haalbaarheid, aflossingstabel; projects: first home, next home, second home, new build, refinancing, self-employed, renovation loan; supervisory authority FPS Economy Economic Inspectorate; franchise.be (22 Jan 2024): 63 locations and 83 experts, management buy-in backed by private equity since 2020.
- Verzekeringen.be / Assurances.be (acquired 2021): car, motor, bike, travel, cancellation, luggage, fire, contents, outstanding-balance, hospitalisation, accident, dental, family liability, pension savings, funeral, pet, legal assistance, self-employed cover; insurer pages incl. AXA, Allianz, Ethias, KBC, Belfius, DVV, DKV, DELA, NN, Athora, Cardif, Euromex, Europ Assistance, Fidea, Patronale Life, Qover, Santevet, DAS.
- Aanbieders.be / Mesfournisseurs.be (acquired 2022): "4,6 / 2765 Google reviews"; energy (save up to €600 claim on homepage; "tot 1.100€ deze winter" on energy page), insurance across 11 insurers (save €500), internet/TV/telephony (save €348), mobile (save €144); charging stations; business energy and telecom; free switching; opening hours Mon–Thu to 17:00, Fri to 16:00.
- Vortex Capital Partners (vortexcp.com/investment/peasy/): invested 2020 in Hypotheek.winkel (68 physical branches, proprietary comparison technology); Horizon Group formed 2020; acquisitions Verzekeringen.be/Assurances.be 2021 and Aanbieders.be/Mesfournisseurs.be 2022; in-house training academy ~30 advisors annually; kept investing while the mortgage market contracted ~40%; realised investment, exit December 2025 to Meilleurtaux; quote David Geerts "Vortex played a crucial role in every key phase of this journey".
- Meilleurtaux acquisition (hypotheekwinkel.be blog 23 Dec 2025; meilleurtaux.com press; vdp.be): 100% of Peasy shares; Peasy ~200 employees, ~€30 million revenue, ~70 offices; Meilleurtaux founded 1999, Silver Lake majority since 2020, entered Belgium 2023 via MiD Finance, active mainly in Wallonia plus offices in Ghent and Antwerp; combined group 81 offices; David Geerts leads Belgium and Luxembourg; Thomas Vandeville CEO Meilleurtaux; VDP exclusive advisor to Peasy and Vortex.
- Market and regulation: Febelfin — mortgage credit applications excl. refinancing down ~37% in Q1 2023 and ~29% in Q2 2023 vs 2022; up ~7.5% in number and ~12% in amount in Q3 2024 (febelfin.be press room); FSMA registers of credit intermediaries (mortgage and consumer credit) and insurance intermediaries (fsma.be); BIPT Easy Switch — new fixed operator terminates the old contract, >99,125 switches in 2021 (bipt.be); VREG V-test and V-check — invoice code mandatory since 1 July 2025 (vtest.vreg.be; vrt.be 28 Aug 2025); Wikifin is the FSMA financial-education programme launched 31 January 2013 with a savings-account comparison tool and IMMOsimulator (wikifin.be).

## Competitor facts (business/competition.json; official sources only; keep reported scope)

- `immotheker-finotheker` — Immotheker Finotheker (immothekerfinotheker.be; Belgium-wide): "100% independent", "+10,000 products compared", "100 offices", "+55,000 loans concluded", "150 employees", "30 years experience"; compares more than 2,000 mortgage loans at 16 banks daily; first office 1 April 1995 (Schoten); mortgage monitor since 2004; attestation of purchase security 2024; founders John Romain, Alex Geens, Jan Romain (immothekerfinotheker.be/en/, /en/about-us/).
- `meilleurtaux-belgium` — Meilleurtaux Belgium (meilleurtaux.be; acquirer of Peasy, previously competitor in Wallonia): personal loans, credit grouping, mortgage, car and renovation loans, insurance; entered Belgium 2023 via MiD Finance; group founded 1999; Silver Lake majority since 2020 (meilleurtaux.com press release Dec 2025).
- `credishop` — Credishop (credishop.be): independent credit intermediary in mortgage credit and instalment loans, personal service, renovation and energy loans focus (credishop.be). No published stats — leave stats empty.
- `yago` — Yago, formerly Seraphin (yago.be; Brussels): digital insurance broker, FSMA-recognised; "30.000+ klanten"; "In 2025, 97% of them recommend us after a claim"; customer service responds within 2 hours; single digital interface for all contracts (yago.be/nl/).
- `callmepower` — CallMePower (callmepower.be): free comparison and advice service for energy, broadband, mobile, TV, insurance and moving in Belgium; part of the Selectra group founded 2007 and active in 18 countries; phone advisors compare and switch (callmepower.be/en/about-us).
- `daretocompare` — DareToCompare.be / DurfBesparen.be (daretocompare.be): independent energy and telecom comparator founded (relaunched) 2021 by Evert Engelen, 20+ years market experience, first Belgian online energy/telecom comparator in 2007; families and self-employed (daretocompare.be/about).
- `topcompare` — TopCompare.be (topcompare.be; Brussels): comparison of personal loans, mortgages, credit cards, bank accounts and insurance policies. No verified stats — leave stats empty.
- `wikifin` — Wikifin (wikifin.be; FSMA public programme, non-commercial): launched 31 January 2013; independent information, savings-account comparison tool and IMMOsimulator; Wikifin School and Wikifin Lab (wikifin.be/nl/over-wikifin).
- `vreg-v-test` — VREG V-test and V-check (vtest.vreg.be; Flemish energy regulator, non-commercial): compares energy contracts; V-check reads the invoice code mandatory since 1 July 2025; tens of thousands of uses in the first two months (vtest.vreg.be; vrt.be 28 Aug 2025).
Logos: `logos/<player-id>.png`. Every business stat must carry an official source URL and reported scope; leave stats out rather than invent them.
