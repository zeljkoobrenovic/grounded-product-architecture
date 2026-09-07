# ID Spine — freelancer-bookkeeping-service-platform

Authoritative ID contract for this domain. Every artifact file MUST use exactly these
IDs when referencing entities owned by another file. Names/descriptions here are
one-liners; the artifact author expands them to reference-domain density.
All ids lowercase. Modeled on Kees de Boekhouder / Founders (see DOMAIN.md).

## Customer groups and customers (customers.json)

Group "Freelancers and Sole Proprietors" — eenmanszaak clients paying €840/year (invoiced monthly); the core of the 10,000+ client base:
- `crfr` — Creative Freelancer. Designer, photographer, stylist, make-up artist, furniture maker, artist or content creator (the Kees testimonial base: Jochem, Celeste, Tynke, Marloes); member of BNO, DuPho, Kunstenbond or Stichting BOK; irregular income, many small receipts, wants admin to take almost no time and a bookkeeper who understands creative work.
- `kfrl` — Knowledge Freelancer. Consultant, developer, interim manager, coach or trainer with a few larger clients, hourly or fixed-fee invoices, higher revenue, sensitive to Wet DBA, deductions, tax reservation and buying a house as a freelancer; compares Kees with software-only tools.
- `strt` — Starting Entrepreneur. Registers at KVK for the first time, often part-time next to a job; needs guidance on VAT number, KOR, startersaftrek and the hours criterion, wants the first quarter and first income tax return done right; the Starters package at €840/year.

Group "Partnerships and Companies":
- `vofp` — VOF Partner. Two or more partners (e.g. the bakers Yoeri and Elin) sharing one administration and profit split, €1,140/year for two partners plus €100 per extra partner; needs per-partner income tax returns and clarity on who owes what.
- `bvdg` — BV Director-Major Shareholder (DGA). Owner of a holding BV (€1,750/year) and/or werkmaatschappij (€2,450/year) served by the sister company Founders: corporate tax return, statutory annual accounts and KVK filing, DGA salary through payroll, dividend and holding structure questions.

Group "Kees Service Teams" — the operator's own staff who use the platform every day:
- `bkpr` — Personal Bookkeeper. Internally trained, carries a portfolio of clients, checks administrations, files quarterly VAT, prepares annual accounts and income tax returns, answers client questions by e-mail and phone, is backed up by colleagues.
- `csux` — Client Success and Sales Executive. Runs the free Google Meet introduction, the mutual-fit check, onboarding and bookkeeper matching, the switch from a previous bookkeeper, subscription changes and cancellations, and retention.

Group "Partners and Ecosystem":
- `ecop` — Ecosystem Partner. Professional association, insurer, pension provider, legal or crowdfunding partner (BNO, DuPho, Kunstenbond, Stichting BOK, voordekunst, Unfair, Insify, BrightPensioen, DAS) offering member benefits and referral discounts to Kees clients and reaching freelancers through Kees.

### JTBD ids (customers.json jobsToBeDone; insights link jobIds to these)
- crfr: `jtbd-crfr-1` Keep my administration complete with almost no time spent, `jtbd-crfr-2` Never miss a VAT or income tax deadline or get a surprise bill, `jtbd-crfr-3` Get paid faster with professional quotes and invoices.
- kfrl: `jtbd-kfrl-1` Know my real profit, tax position and what to reserve at any moment, `jtbd-kfrl-2` Claim every deduction and stay on the right side of the Wet DBA, `jtbd-kfrl-3` Get expert answers on big decisions (house, BV, pension) without paying per hour.
- strt: `jtbd-strt-1` Start my business with the administration set up right from day one, `jtbd-strt-2` File my first VAT return and first income tax return without mistakes, `jtbd-strt-3` Learn what I can deduct and what I must reserve as a starter.
- vofp: `jtbd-vofp-1` Run one shared administration for all partners, `jtbd-vofp-2` Split profit correctly and file every partner's income tax return, `jtbd-vofp-3` Add employees or a partner without changing bookkeeper.
- bvdg: `jtbd-bvdg-1` Keep my BV compliant (corporate tax, annual accounts, KVK filing) at a fixed fee, `jtbd-bvdg-2` Pay myself correctly as DGA (salary, dividend, holding structure), `jtbd-bvdg-3` Move from sole proprietorship to BV without losing my bookkeeper.
- bkpr: `jtbd-bkpr-1` Review every client administration and file on time with first-time-right quality, `jtbd-bkpr-2` Serve more clients per week without losing the personal relationship, `jtbd-bkpr-3` Give correct, consistent tax advice backed by the knowledge base.
- csux: `jtbd-csux-1` Convert intro calls into active, well-matched clients fast, `jtbd-csux-2` Switch clients from a previous bookkeeper without gaps, `jtbd-csux-3` Keep clients through changes in plan, legal form or bookkeeper.
- ecop: `jtbd-ecop-1` Offer my members a trusted bookkeeper benefit, `jtbd-ecop-2` Track referrals and benefit uptake from the partnership.

### North-star KPI names (use these VERBATIM as pyramid node names; productStrategy northStar must match)
- crfr: north star "Hours spent on administration per month"; supporting include "Tax filing on-time rate", "Unexpected tax bill incidence".
- kfrl: north star "Tax position accuracy"; supporting include "Deductions captured per year", "Advice response time".
- strt: north star "Time to first compliant filing"; supporting include "Starter deductions captured", "Onboarding completion time".
- vofp: north star "Administration hours per partner per month"; supporting include "Partner return on-time rate", "Profit split accuracy".
- bvdg: north star "Corporate filings completed on time"; supporting include "Annual accounts delivery lead time", "Total cost of compliance".
- bkpr: north star "Clients served per bookkeeper"; supporting include "Review turnaround time", "Filing first-time-right rate".
- csux: north star "Intro-to-active conversion rate"; supporting include "Time to bookkeeper assignment", "Client churn rate".
- ecop: north star "Referred members activated"; supporting include "Referral conversion rate", "Partner benefit uptake".

KPI node id convention (mirrors transfer-pricing-compliance-platform): `co-<cust>-top`, `co-<cust>-b1`, `co-<cust>-b1-c1`, `co-<cust>-b1-c1-l1` … and `bo-<cust>-…` for businessOutcomes. Every non-leaf has ≥2 children; target 4 levels (1+2+4+8). Set `icon` fields as `kpi-<cust>-<nodeid>.png`; icon files are backfilled later.
Customer icons: use `<cust>.png` (e.g. `crfr.png`) — backfilled later. Do NOT set `media` fields on JTBDs, journeys or relations (no images exist).

## Streams (product-stream.json; JTBD steps reference via streamsNeeded — use these ids only)

- `start-and-onboard-a-new-client` — From a website request to an active client: free Google Meet intro, mutual-fit check, plan choice by legal form, account access, personal bookkeeper assignment, first upload coaching.
- `switch-from-a-previous-bookkeeper` — From digital copies of old returns and personal data to a continued administration without gaps in VAT or income tax history.
- `capture-receipts-and-expenses` — From a photo, upload or e-mail to a recognised, categorised expense booking with VAT (Scan & Herken), ready for bookkeeper review.
- `create-quotes-and-invoices-and-get-paid` — From quote to invoice to paid: templates, multiple trading names, VAT rules (incl. reverse charge), status tracking and reminders.
- `sync-and-match-bank-transactions` — From a Ponto PSD2 consent to transactions synced four times a day and matched automatically against bookings, with manual matching and re-authorisation every 90–180 days.
- `review-administration-and-file-vat-returns` — From submitted bookings to a bookkeeper-checked quarter and a VAT return filed with the Belastingdienst before the deadline.
- `close-the-year-and-file-income-tax` — From a full fiscal year to annual accounts, deductions applied (zelfstandigenaftrek, startersaftrek, mkb-winstvrijstelling), the income tax return filed, and partner returns on request.
- `serve-partnerships-and-companies` — From VOF profit split and partner returns to BV corporate tax, statutory annual accounts and KVK filing through Founders, including the eenmanszaak-to-BV transition.
- `run-payroll-for-small-employers` — From employee or DGA data to monthly payslips, wage tax filing and payroll journal entries at €17.50 per payslip.
- `ask-your-bookkeeper-and-get-advice` — From a client question by e-mail, phone or video to a consistent answer backed by the advice knowledge base, with proactive updates on deadlines and rule changes.
- `monitor-your-finances-on-the-dashboard` — From bookings to real-time revenue per quarter, cost categories, investments, profit, VAT to pay and tax reservation on web and mobile.
- `manage-subscription-billing-and-plans` — From plan choice to monthly invoicing of the fixed yearly fee, add-ons (bank connection €5/account, partner return €125, payroll per payslip), plan changes and cancellation rules.
- `grow-through-partners-and-referrals` — From partner agreements to member benefits, referral tracking, client stories and network profiles that turn satisfied clients into ambassadors.
- `plan-bookkeeper-capacity-and-quality` — From client volume per office to bookkeeper allocation, backup coverage, four-eyes QA checks, internal training and first-time-right measurement.

14 streams.

## Product bricks (product-bricks.json) — root group → subgroup → bricks

Root "Client Administration App":
- Subgroup "Dashboard and Insight": `dash` Financial Dashboard and Quarterly Results, `vatv` VAT Position and Tax Reservation View, `ntfy` Deadlines, To-dos and Notifications.
- Subgroup "Documents and Expenses": `scan` Scan & Herken Receipt Capture and Recognition, `expn` Expense and Purchase Booking, `docs` Document Archive.
- Subgroup "Sales and Invoicing": `quot` Quotes and Proposals, `invc` Invoices, Credit Notes and Trading Names, `dunn` Payment Tracking and Reminders.
- Subgroup "Banking": `bank` Bank Connection (Ponto PSD2), `mtch` Transaction Matching Engine.

Root "Bookkeeping Engine and Filings":
- Subgroup "Ledger and Tax": `ledg` General Ledger and Booking Rules, `vatr` VAT Return Preparation, `yend` Year-end Close and Annual Accounts, `itax` Income Tax Return (IB) Preparation, `ctax` Corporate Tax (VPB) and BV Statutory Accounts, `payr` Payroll and Payslips.
- Subgroup "Authority Connectivity": `bdgw` Belastingdienst Filing Gateway, `kvkf` KVK Filing and Company Data.

Root "Bookkeeper Workspace":
- Subgroup "Review and Workflow": `bkws` Bookkeeper Client File and Review Queue, `qaud` Quality Assurance and Four-eyes Checks, `wkld` Client Allocation and Workload Planning, `dlin` Filing Calendar and Deadline Orchestration.
- Subgroup "Client Communication": `msgc` Client Messaging, E-mail and Call Log, `advk` Advice Knowledge Base and Tax Rules Content.

Root "Growth and Client Lifecycle":
- Subgroup "Acquisition and Onboarding": `lead` Lead Capture and Intro Call Booking, `onbd` Onboarding, Fit Check and Bookkeeper Matching, `swch` Switch Service and Historical Data Import.
- Subgroup "Subscription and Community": `subs` Subscription Plans, Billing and Cancellation, `prtn` Partner Programme and Referral Benefits, `cnet` Entrepreneur Network Profiles and Client Stories.

Root "Platform Foundation":
- Subgroup "Core Services": `iden` Identity, Login and Access Control, `mobi` Mobile App Shell (iOS/Android), `audt` Audit Trail, AVG Compliance and Retention, `intg` Integration and API Gateway (Ponto, Belastingdienst, KVK, e-mail, payments).

35 bricks. Module ids must start with `module-` (e.g. `module-scan-web`, `module-scan-api`).

### Brick dataDependencies → data asset ids (see below); wire at least these
dash→dashboard-snapshot,ledger-entry; vatv→vat-return,ledger-entry; ntfy→notification,filing-deadline; scan→receipt-document,expense-booking; expn→expense-booking,ledger-entry; docs→receipt-document,business-entity-profile; quot→quote,customer-contact; invc→sales-invoice,customer-contact,business-entity-profile; dunn→sales-invoice,notification; bank→bank-connection,bank-transaction; mtch→bank-transaction,transaction-match,ledger-entry; ledg→ledger-entry,business-entity-profile; vatr→vat-return,ledger-entry; yend→annual-accounts,ledger-entry; itax→income-tax-return,annual-accounts; ctax→corporate-tax-return,annual-accounts; payr→payslip,filing-submission; bdgw→filing-submission,vat-return,income-tax-return; kvkf→business-entity-profile,filing-submission; bkws→review-task,client-account; qaud→qa-finding,review-task; wkld→client-allocation,client-account; dlin→filing-deadline,review-task; msgc→client-message,client-account; advk→tax-rule-article,client-message; lead→lead-and-intro-call; onbd→onboarding-case,client-allocation,client-account; swch→historical-return-import,onboarding-case; subs→subscription-plan,subscription-invoice; prtn→partner-referral,client-account; cnet→entrepreneur-network-profile,client-account; iden→user-identity,client-account; mobi→user-identity,notification; audt→audit-trail-entry,user-identity; intg→bank-connection,filing-submission,audit-trail-entry.

## Data assets (data/data-assets.json) — id → ownerTeamId

- `client-account` → platform-and-security-team
- `user-identity` → platform-and-security-team
- `audit-trail-entry` → platform-and-security-team
- `business-entity-profile` → client-app-team
- `dashboard-snapshot` → client-app-team
- `notification` → client-app-team
- `receipt-document` → expenses-and-banking-team
- `expense-booking` → expenses-and-banking-team
- `bank-connection` → expenses-and-banking-team
- `bank-transaction` → expenses-and-banking-team
- `transaction-match` → expenses-and-banking-team
- `quote` → invoicing-team
- `sales-invoice` → invoicing-team
- `customer-contact` → invoicing-team
- `ledger-entry` → bookkeeping-engine-team
- `vat-return` → bookkeeping-engine-team
- `annual-accounts` → bookkeeping-engine-team
- `income-tax-return` → bookkeeping-engine-team
- `corporate-tax-return` → founders-bv-services
- `payslip` → bookkeeping-pods
- `filing-submission` → filing-and-integrations-team
- `filing-deadline` → bookkeeper-workspace-team
- `review-task` → bookkeeper-workspace-team
- `client-allocation` → bookkeeper-workspace-team
- `client-message` → bookkeeping-pods
- `qa-finding` → quality-and-tax-knowledge
- `tax-rule-article` → quality-and-tax-knowledge
- `lead-and-intro-call` → growth-and-marketing
- `partner-referral` → growth-and-marketing
- `entrepreneur-network-profile` → growth-and-marketing
- `onboarding-case` → client-success-and-onboarding
- `historical-return-import` → client-success-and-onboarding
- `subscription-plan` → client-success-and-onboarding
- `subscription-invoice` → client-success-and-onboarding

34 assets. Personal-data level is high for most (names, BSN in tax returns, bank transactions); tag AVG/GDPR, Belastingdienst retention (7 years fiscal retention duty, 10 years for real-estate related VAT).

## Teams (teams.json) — every brick owned by exactly one team

Kees de Boekhouder has ~100 staff (about 40% bookkeepers) plus the Founders sister company; model the organisation at ~115 people. Product/engineering is small (full-stack developers, solution architects, heads of QA/Growth/Operations/Finance/People) — keep product teams at 3–6 people and bookkeeping pods large.

Org group "Product and Engineering":
- `client-app-team` (stream-aligned) owns dash, vatv, ntfy, docs, mobi
- `expenses-and-banking-team` (stream-aligned) owns scan, expn, bank, mtch
- `invoicing-team` (stream-aligned) owns quot, invc, dunn
- `bookkeeping-engine-team` (complicated-subsystem) owns ledg, vatr, yend, itax
- `filing-and-integrations-team` (platform) owns bdgw, kvkf, intg
- `bookkeeper-workspace-team` (stream-aligned) owns bkws, wkld, dlin
- `platform-and-security-team` (platform) owns iden, audt

Org group "Bookkeeping Operations" (Amsterdam, Rotterdam, Utrecht):
- `bookkeeping-pods` (stream-aligned, ~45 bookkeepers and team leads in three offices) owns msgc, payr; customer dependencies on crfr, kfrl, strt, vofp, bkpr
- `quality-and-tax-knowledge` (complicated-subsystem; Head of QA, fiscal specialists, internal training) owns qaud, advk; customer dependencies on bkpr, kfrl
- `founders-bv-services` (stream-aligned; Founders Finance B.V. bookkeepers for BVs) owns ctax; customer dependencies on bvdg

Org group "Growth and Client Success":
- `growth-and-marketing` (stream-aligned; Head of Growth, marketing, partnerships, content) owns lead, prtn, cnet; customer dependencies on strt, crfr, ecop
- `client-success-and-onboarding` (stream-aligned; sales, client success executives, support) owns onbd, swch, subs; customer dependencies on csux, strt, vofp

12 teams.

## Products (product-deployments/products.json) — id, primary customers

- `kees-personal-bookkeeper-eenmanszaak` — Kees de Boekhouder for Sole Proprietors: personal bookkeeper + app, €840/year — crfr, kfrl
- `kees-starters-package` — Starters package: same subscription with starter guidance (KVK, VAT number, KOR, startersaftrek) — strt
- `kees-vof-package` — Kees for VOF partnerships (€1,140/year for two partners, +€100 per partner) — vofp
- `founders-bv-package` — Founders for Holding BV (€1,750) and Werkmaatschappij (€2,450) — bvdg
- `client-app-dashboard` — Client web and mobile app: dashboard, documents, notifications — crfr, kfrl, strt, vofp
- `scan-en-herken` — Scan & Herken receipt recognition — crfr, strt
- `offertes-en-facturen` — Quotes and Invoices — crfr, kfrl, vofp
- `bankkoppeling` — Bank Connection add-on via Ponto (€5/month per account) — kfrl, crfr, vofp
- `salarisadministratie` — Payroll administration (€17.50 per payslip per employee per month) — vofp, bvdg
- `partner-aangifte-inkomstenbelasting` — Partner income tax return (€125 incl. VAT) — kfrl, crfr
- `bookkeeper-workspace` — Bookkeeper Workspace and QA tooling (internal) — bkpr, csux
- `onboarding-and-switch-service` — Free intro call, onboarding and switch service — csux, strt
- `partner-programme` — Partner programme with member benefits and referral discounts — ecop, crfr

13 products. Use `<product-id>.png` icons (rendered later into product-deployments/icons).

## Deployment channels (deployment.json; maas is the structural reference)

Channel groups: "Web Applications" (client web app mijn.keesdeboekhouder.nl; bookkeeper workspace back office; public website with appointment booking and partner pages), "Mobile Apps" (iOS and Android client app: photo capture, dashboard, invoices, notifications), "Integrations" (Ponto/Isabel PSD2 bank connection, Belastingdienst filing channel, KVK, e-mail-in receipts, payment providers, Google Meet scheduling), "Document Outputs" (PDF quotes and invoices, annual accounts, filed return copies, payslips), "Internal Operations" (QA and allocation tooling, subscription billing, partner programme administration). Map deployedBricks with usedInProducts referencing product ids above.

## Sourced company facts (reuse consistently; do not invent numbers)

- Kees de Boekhouder, Amsterdam (Nieuwe Teertuinen 25A), offices in Rotterdam (Stationsplein 45) and Utrecht (Oudegracht 27); founded 2009 by Kees Monteban and Marlou ter Berg; "15 years" and "more than 10,000 entrepreneurs throughout the Netherlands" (site, 2026); ~100 staff incl. bookkeepers, marketers, IT and HR; internally trained bookkeepers; growth target 20,000 clients (Top of Minds vacancy); addressable market ~1.4 million freelancers (vacancy) / CBS 1.2 million zzp'ers in 2025 (−62,000 vs 2024).
- Vortex Capital Partners took a stake announced 24–25 May 2022 (buyout, tech-enabled, 6,500+ clients then). Quotes: Kees Monteban (CEO) on solving administrative challenges nationwide; Joost Moerland (Vortex partner) on the loyal customer base and brand ambassadors. Vortex: >10,000 clients, >25% revenue CAGR, focus on leadership, organisational structure and professionalising the technology function; ambition "the go-to brand for bookkeeping services".
- Leadership: Kees Monteban (CEO, co-founder), Marlou ter Berg (co-founder), Rody Turpijn (COO), Rogier van den Heuvel (CEO per 2026 team page); Founders founded 2018 (Founders Finance B.V., KVK 69951276; KeesdeBoekhouder Office B.V. KVK 60972262).
- Pricing (ex VAT, per year, invoiced monthly): eenmanszaak €840; VOF €1,140 for 2 partners, +€100 per partner; holding BV €1,750; werkmaatschappij €2,450 (via Founders). Add-ons: payroll €17.50 per payslip per employee per month; partner income tax return €125 incl. VAT; bank connection €5 per month per account. First year: full fiscal year; thereafter monthly cancellation with one calendar month notice. Free intro via Google Meet; external accounting software not accepted; multiple trading names per entity; AVG-compliant.
- Bank connection: Ponto (Isabel Group, PSD2 licence), banks incl. Knab, Rabobank, ABN AMRO, bunq; sync 4x daily; automatic matching; re-authorise every 90–180 days.
- Partners: voordekunst, BNO, Insify, DuPho, Unfair, Kunstenbond, BrightPensioen (€50 discount), Stichting BOK (2,300+ members; no admin costs + 3 months free), DAS. BridgeFund lists Kees as expert partner.
- Testimonials: Jochem (furniture designer/maker), Celeste (stylist/influencer), Nathalie (founder TEN Women), Yoeri & Elin (bakers), Tynke (make-up artist/hairstylist), Marloes (artist).
- Regulatory: VAT quarterly deadline last day of month after quarter; zelfstandigenaftrek €1,200 (2026) → €900 (2027); startersaftrek €2,123; KOR ≤ €20,000 turnover, relaxed 1 Jan 2025; Wet DBA enforcement since 1 Jan 2025, soft landing in 2026; model agreements no longer assessed since 6 Sep 2024, usable until 31 Dec 2029.

## Competitor facts (business/competition.json; official sources only; keep reported scope)

- Moneybird (moneybird.nl; Enschede; software-only): plans Compact €3, Start €15, Groei €29, Compleet €41 per month; 60-day trial; "more than 400,000 entrepreneurs" (moneybird.nl/prijzen); ~17 years old; Moneybird business account €7/month.
- e-Boekhouden.nl (e-boekhouden.nl; founded 2002; Brabant): "over 500,000 entrepreneurs have used the platform", ~90+ staff, 4.5 stars Trustpilot (e-boekhouden.nl/over-ons); ZZP Pakket €9.95 (promo €4.98), Standaard €14.50, Standaard + Factureren €24.00 per month; 15 months free for starters (e-boekhouden.nl/prijzen).
- Jortt (jortt.nl; Almere; KvK 64073319): own PSD2 licence from DNB; AI-boekhoudbot; built-in IB and VPB returns; payroll; Peppol; 30 days free; 50,000+ zzp'ers (jortt.nl).
- Tellow (tellow.nl; Amsterdam; founded 2015; Shine Netherlands B.V., part of Ageras): free plan, paid plans, "Compleet" plan with personal bookkeeper (tellow.nl/plan/compleet; third-party listings ~€69.99/month); business IBAN and cards; 50,000+ zzp'ers (third-party).
- MoneyMonk (moneymonk.nl; Utrecht): Starter €0 for 15 months for new registrations, Pro €32.50/month (promo €15 for 3 months), Ultra €37.50/month; 9.8/10 over 800 reviews; 4.8/5 Google (200+), 4.6/5 App Store (750+).
- SnelStart (snelstart.nl; Alkmaar; founded 1982; part of Visma): 165,000 entrepreneurs, 215 employees, 5 offices, 4.6/5 Trustpilot, ISO 27001 (snelstart.nl/over-snelstart).
- Rompslomp (rompslomp.nl; Den Haag; part of Visma): 900+ reviews, 4.3 stars Google/FeedbackCompany; invoicing, VAT, receipts, e-invoicing, mobile apps.
- Exact Online (exact.com; Delft): cloud accounting for SMEs and accountants — use only facts from exact.com/nl; if no stat is verifiable, leave stats empty.
- Founders (founders.nl; Amsterdam; 2018) is the sister brand, not a competitor.
Every business stat must carry an official source URL and reported scope; leave stats out rather than invent them.
