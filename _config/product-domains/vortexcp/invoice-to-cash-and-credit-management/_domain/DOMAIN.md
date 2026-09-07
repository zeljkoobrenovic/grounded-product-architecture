# Invoice-to-Cash and Credit Management

Research snapshot: 2026-09-06. This is an outside-in product strategy model informed by POM, not a description of its private systems, organization, contracts, or roadmap.

## Boundary and value exchange

The domain begins with an approved receivable and ends with a reconciled payment, a maintained arrangement, a resolved dispute, or an authorized handoff. Institutional creditors pay for software and implementation that improve cash collection and operating efficiency. Their staff operate billing and arrears processes; consumers and business payers receive creditor-branded communication and payment options. Integration partners connect the platform to systems of record. Debt-support advisers participate only with a verified mandate and purpose-limited access.

Core scope covers invoice composition and delivery, payment requests, payment-provider connections, cash matching, collection policies, case handling, payment arrangements, housing arrears, and outcome measurement. Adjacent scope covers ERP and housing-system integration, bank reconciliation inputs, social-support referrals, and collection-agency handoff. General-ledger accounting, lending and credit underwriting, debt purchasing, holding customer funds, court enforcement, tenancy administration, and clinical records are outside the modeled product boundary. The model does not establish POM's regulatory status or imply that one contract supports every payment method or country.

## Public grounding

POM markets three connected offers: [POM Invoice](https://www.pom.eu/en/solutions/pom-invoice), [POM Payment](https://www.pom.eu/en/solutions/pom-payment), and [POM Collect](https://www.pom.eu/en/solutions/pom-collect). These names anchor the portfolio. The payment page describes a direct-to-creditor-bank-account arrangement; the proposed architecture therefore treats bank and provider confirmations as external inputs rather than inventing a POM custody ledger.

[Vortex's investment profile](https://vortexcp.com/investment/pom/) dates its Mail to Pay investment to 2018, describes the combination with Belgian POM in 2022, and the POM group rebrand and Mind2Pay addition in 2024. It reports more than €5 billion collected for customers in 2024 and more than 2,500 corporate clients, without dating the client-count snapshot. These are investor-reported group figures. The POM Netherlands homepage separately displays more than 150 customers and monthly transaction figures without an equivalent scope definition. They are not interchangeable, and no modeled KPI uses them as a baseline.

The [Intermaris case](https://www.pom.eu/en/testimonials/zorgvuldigheid-staat-voorop-bij-huurdersbrieven-intermaris) illustrates targeted tenant communication and postal alternatives. The [UvA/HvA case](https://www.pom.eu/en/testimonials/studenten-uva-en-hva-betalen-beter-dankzij-pom) illustrates returned-payment follow-up and multilingual reminders. These are vendor-published examples, not representative outcome measurements. Housing is modeled as a vertical use of the three offers; Mind2Pay is group context, not a fourth independently verified current offer.

## Strategic thesis

Help creditors collect legitimate receivables while preserving payers' ability to understand, challenge, and sustainably resolve an obligation. Compete on continuity across communication, payment, and follow-up, with reliable settlement context and practical support for difficult cases. The proposed domain north star is **Sustainably resolved receivable rate**: eligible due receivables settled without reversal or maintained under an agreed arrangement through the observation window, divided by eligible due receivables. Settled and arranged outcomes must also be reported separately; an arrangement is never counted as cash. Exclude unresolved disputes from automated collection eligibility, retain them in an explicit denominator reconciliation, and report hold reasons to prevent metric gaming.

This is a causal KPI model, not an arithmetic decomposition. Individual customer pyramids measure the part each persona can influence. All baselines are unavailable; numeric targets are explicitly proposed pilot hypotheses, contingent on a measured cohort and agreed definitions. No target is represented as a POM result or commitment.

## Horizons and tradeoffs

- **Year 1:** establish receivable accuracy, reliable delivery, payment-state reconciliation, dispute holds, and controlled pilots. Start with creditor-defined policy and verified integrations. Proposed gates include a 20% relative reduction in unnecessary manual touches and no increase in substantiated complaints against a matched baseline.
- **Year 3:** deepen housing and supported-payment workflows, introduce repeatable partner onboarding, and evaluate contact optimization with holdouts, documented overrides, and cohort-level guardrails. Expand only after existing customers demonstrate sustained value.
- **Year 5:** support reusable country and sector operating policies with portable integrations, customer-controlled configuration, and demonstrable long-term payer outcomes. Country availability and rollout dates remain hypotheses requiring local validation.

Tradeoffs are explicit: an affordable arrangement can delay cash; postal inclusion costs more than email; conservative payment matching leaves a manual queue; an experiment can be stopped despite higher conversion when complaints or unfair treatment rise. Disputed obligations, revoked representative access, uncertain payment states, and vulnerability flags require controlled handling. Predictive contact recommendations are separate from decisions on entitlement, affordability, litigation, or adverse action.

## Architecture and operating assumptions

The bricks, module boundaries, APIs, event contracts, logical stores, deployment partitions, operational service objectives, and eight-team design are proposals. They are not reverse-engineered claims. ERP and bank systems remain authoritative for their own records; the platform owns imported receivable versions, collection state, and reconciled references. Proposed EU deployment and retention controls require contractual verification. Prices, take rates, revenue mix, vendor infrastructure, actual staffing, and certificate scope are unknown.

The operating model assigns one team to every brick and one system-of-record brick to each data asset. Specialist platform and trust teams support teams responsible for invoicing, payments, integrations, collections, payment support, and decision intelligence. Publicly described POM AI capabilities inform a proposed decision-support subsystem; no autonomous collection or customer-decision agent is represented as staff.

Structural references: `payments-and-revenue-infrastructure` and `real-estate-erp-platform` for adjacent domain boundaries; `ride-sharing-marketplace` for customer, stream, brick, and data shapes; `maas` for the current lean product/deployment and team schemas. Product composition belongs in `deployment.json`; retired `neededBricks` and per-product environment fields are omitted.

See [research notes](RESEARCH.md), [build notes](BUILD-NOTES.md), and the [domain reviews](../REVIEW.md) for evidence limitations, validation, and outstanding discovery work.
