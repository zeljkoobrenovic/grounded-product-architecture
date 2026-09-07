# Invoice-to-Cash and Credit Management Review

## Product Domain Review

Updated: 2026-09-06

### Executive assessment

- The boundary fits POM's three publicly named offers and gives creditors, operators, payers, representatives and integration partners distinct responsibilities.
- Four groups and nine personas each have two jobs, a six-stage adoption journey, two four-level KPI trees and distinct one-, three- and five-year horizons.
- Source observations and proposed implications are separated. Marketing statistics do not become measured KPI baselines.
- Housing is a vertical operating context within the portfolio. Mail to Pay and Mind2Pay are not presented as independent current products or competitors.
- The customer model is mature as an outside-in strategy hypothesis. It is not validated company intelligence.

### High-priority findings

No P1 strategy or customer-coverage defect identified. Deterministic reference and generation checks are recorded in the balance audit below.

### Medium-priority findings

- **P2 — Customer validation remains open.** Evidence: customers/customers.json, all nine personas; customers/insights.json, inte and stud. Vendor cases establish plausible contexts but do not establish prevalence, current behavior or a representative baseline. Validate the distinct buying, paying and support journeys with interviews and measured cohorts before investment decisions.
- **P2 — Product entitlements remain unverified.** Evidence: product-deployments/products.json, pinv/ppay/pcol; deployment.json, shared case and measurement facilities. Shared runtime use does not imply that every feature is included in each commercial offer. Obtain current packaging and connector contracts; retain explicit capability and entitlement boundaries.
- **P2 — Commercial attribution needs a measurement contract.** Evidence: the nine businessOutcomes trees in customers/customers.json. They intentionally use a shared contract-retention and contribution-margin framework sliced by use case. Cohorts overlap and cannot be summed as independent company revenue. Agree allocation and cohort rules before reporting.
- **P3 — Headquarters precision is limited for one alternative.** Evidence: business/competition.json, bill. The reviewed official page lists offices without designating one headquarters; the model preserves that uncertainty.

### Targeted improvement backlog

1. Use edit-customers to incorporate interview and pilot evidence into finc, coll, hous, payr, strs and advr without fabricating currentValue measurements.
2. Use edit-products after packaging discovery to refine shared runtime participation for pinv and ppay.
3. Use edit-competition during procurement to refresh official scope, availability and comparable metrics; omitted statistics remain unknown.

### Open assumptions

Pricing, revenue mix, product entitlements, local rollout, source API contracts, published uplift methodology, actual staffing and private architecture are unknown. Proposed numerical targets require baselines. The source and interpretation register is in _domain/RESEARCH.md.

## Product Bricks Review

Updated: 2026-09-06

### Architecture assessment

- Twenty-four bricks span four durable root areas and meaningful subgroups. Their 105 modules use all six supported layers.
- Eight outcome streams include corrected invoices, delayed or reversed payments, dispute holds, plan reassessment, accepted adviser handoff and service recovery.
- Twenty-four logical assets identify a primary owning team and system-of-record brick. External ERP, housing and bank authorities are distinguished from owned operational projections.
- Shared foundations include scoped access, audit, retention, integration acceptance, service recovery and usage-cost evidence.
- Proposed implementation details are explicitly separated from public product descriptions.

### Critical findings

No P1 boundary or missing-core-capability defect identified. Cross-file integrity is checked below.

### Model-quality and traceability findings

- **P2 — Adapter linkage corrected.** Evidence: product-bricks/product-bricks.json, rece/deli/paym/mtch/rtrn/case/hard/rent/conn/iamc/oper. The initial draft named external adapters without an explicit state-module call. All eleven now have that dependency, confirmed in both the source audit and generated output.
- **P2 — Runtime and governance are design hypotheses.** Evidence: deployment.json, comm/pays/cols/decs/core; data/data-assets.json, governance on every asset. No actual POM provider, database, retention period or guaranteed region has been verified. Validate contractual and operational constraints before technology selection.
- **P3 — Public context is the available evidence level.** Evidence: grouped links on every brick and stream. These point to official product or case pages, not repositories, deployed services or employee contacts. Do not fabricate evidence-explorer fragment IDs.

### Edit backlog

Connect the adapter modules in the initial draft, then confirm contract details before narrowing the proposed APIs or external system roles. Preserve the current explicit financial-state and case-hold boundaries.

## Teams Review

Updated: 2026-09-06

### Operating-model assessment

- Eight teams have distinct missions and exactly one primary owner is intended for each brick.
- Teams range from eight to ten FTE with domain-specific role mixes; six group leadership FTE yield a 78-FTE scenario, not a POM headcount claim.
- Invoicing owns recipient preferences and delivery recovery; Payment owns initiation and returns; Integration owns creditor setup and source-sensitive matching.
- Collections controls permitted treatment, Sustainable Support owns plans and referrals, and Decision Intelligence owns controlled recommendations and outcome evidence.
- Shared Trust and Platform teams retain controls and recovery accountability. No autonomous payer decision-maker is represented as staff.

### Ownership findings

No orphaned, duplicated or mission-incompatible ownership identified in the inventory. Confirm the complete ownership and asset cross-check below before implementation.

### Topology and staffing findings

- **P2 — Specialist capacity is assumed.** Evidence: teams/teams.json, supt and trst. Two support specialists and one privacy specialist may not cover the eventual country and creditor mix. Validate workload, professional responsibilities and partner capacity before staffing.
- **P2 — On-call coverage must be designed.** Evidence: teams/teams.json, plat/payt/intg; product-bricks/product-bricks.json, oper/paym/conn. Shared reliability supplements product-team ownership. A 78-FTE scenario does not by itself demonstrate a sustainable service rotation.
- **P3 — Integration spans onboarding and matching.** Evidence: intg owns conn/tnan/mtch. This is intentional because source and provider reference quality determines acceptance. Split only if discovery shows incompatible workload or operational cadence.

### Strategy alignment findings

Every persona has an accountable team relationship and a product surface. Team descriptions reuse existing customer KPI names. External advisers, creditors and bank operations remain outside proposed software-team staffing.

### Edit backlog

Use edit-teams after capacity discovery to adjust supt, trst and plat. Preserve unique brick ownership and update data-asset owner and steward links together.

## Balance Audit

Updated: 2026-09-06

Integrity: **passed**. Overall: **mature outside-in domain model**, with commercial, customer and implementation hypotheses explicitly open.

| Dimension | New domain | Ride-sharing reference | Assessment |
|---|---:|---:|---|
| Customer groups | 4 | 4 | Distinct creditor, operations, payer/support and integration contexts |
| Personas | 9 | 4 | Buyer, operator, payer and representative responsibilities separated |
| Bricks | 24 | 20 | Four root areas, eleven subgroups, supported layered modules |
| Streams | 8 | 10 | Every job and brick has an outcome path |
| Data assets | 24 | 17 | Every asset has one owning brick and matching owner team |
| Teams | 8 | 24 | Intentional smaller scenario for the bounded SaaS domain |
| Landscape entries | 10 | 11 | POM anchor plus nine alternatives, including substitutes |
| Sourced insights | 14 | 8 | All source, persona, job and KPI references resolve |

### P1 — realism or traceability breaks

None remaining. The final audit confirmed:

- All nine personas have product and team coverage; all eighteen jobs connect to existing streams.
- All nine adoption journeys use Trigger, Discovery, Evaluation, Trial, Engagement and Retention.
- All eighteen KPI trees have four levels and two children per internal node; 270 node IDs and every strategy metric reference are consistent.
- Every brick is in a stream, deployed for a product and assigned to exactly one primary team.
- Every asset has a matching system-of-record brick, team owner, valid store and valid stewardship references.
- Stream composition matches its flow steps; each product's deployed set includes its required shared dependencies.
- The runtime dependency graph has no cycle; external adapters have explicit internal callers.
- All fourteen insights resolve their sources, personas, jobs and KPI nodes.

### P2 — remaining discovery, not structural blockers

Validate commercial packaging, pilot baselines, customer interviews, local policies and staffing capacity as detailed in the three reviews. Shared service participation is not a claim about feature entitlements. Candidate stressors are not reported incidents or proof of resilience.

### P3 — polish and evidence limits

Domain-specific images and third-party logos are intentionally absent. The start page uses the existing repository logo asset. Public product references are attached to every brick and stream; private implementation evidence is unavailable and no evidence fragment IDs are fabricated.

### Generation and artifact verification

All seven generators completed for this domain. The 98 generated HTML pages have no unresolved checked server placeholders; 394 inline scripts compile, and all 758 static local href/src references resolve. The missing start-page logo detected on the first link pass was supplied from the repository's shared asset and the start page regenerated.

Validation was structural and static; an interactive browser session was not run. Details and repeatable repository commands are recorded in [_domain/VALIDATION.md](_domain/VALIDATION.md).
