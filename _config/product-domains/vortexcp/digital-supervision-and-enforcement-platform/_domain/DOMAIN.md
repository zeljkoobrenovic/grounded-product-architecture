# Digital Supervision and Enforcement Platform

Research date: 2026-09-06. Modeled company: **Twyns**. Domain id: `digital-supervision-and-enforcement-platform`.

This is a public-source product model of digital supervision and enforcement for municipalities, parking operators and specialist transport organizations. Its central outcome is an accountable, proportionate and explainable public service. Observations and scans support decisions; sanction volume and fine revenue are not the supplier's north-star outcome.

## Why this boundary

[Twyns](https://www.twyns.com/) identifies supervision and parking enforcement as its principal product areas. [Vortex](https://vortexcp.com/investment/twyns/) identifies a January 2016 investment and describes European expansion. Those sources support a shared enforcement-platform domain, with specialist transport configurations and public-service delivery around it.

Core scope includes resident-report handoffs, assignments and briefing, mobile observations, case records, parking observations and rights checking, human review, route-specific decisions, corrections, evidence, partner exchange, governed reporting and authority onboarding. [Twyns' platform page](https://www.twyns.com/platform) supports configuration, effective rule data and hosted delivery as product themes. [Its parking page](https://www.twyns.com/parkeerhandhaving) describes a process from scans and rights checks through desk review to follow-up, including authorized correction.

Adjacent scope includes removal contractors, authority public channels, government and parking-right sources, external recipients, scan hardware and authority analytics. A source or receiving body retains its own system-of-record authority. [Genetec AutoVu](https://www.genetec.com/products/unified-security/autovu/parking-management) is an ecosystem reference and a publicly named Twyns partner, not a new internal product brick.

Excluded scope: full permit origination and generic VTH suites, a parking-payment marketplace, broad police intelligence, general-purpose surveillance, autonomous sanction decisions, emergency dispatch, vehicle manufacturing and in-house physical enforcement staffing. A separate Twyns consumer application is not assumed. The authority retains the resident relationship, legal powers and applicable processing responsibilities.

The neighboring `municipal-public-space-enforcement` model emphasizes public-space detection, fly-tipping and field response. This domain intentionally focuses on Twyns' configurable shared service, parking rights and review, specialist remits and authority-system handoffs. `maas` covers broader mobility and payment products; it is not the commercial boundary used here.

## Sources, claims and uncertainty

The 20 primary source entries in `customers/insights.json` record access dates separately from publication dates. Thirteen insights separate a short sourced observation from its inferred implication. Further official company links in competition support headquarters where available. Vendor descriptions are not independent product-performance verification.

- [Hardinxveld-Giessendam](https://www.twyns.com/cases/hardinxveld-giessendam) describes a two-officer authority and an eight-week implementation. This undated case is a bounded historic example, not a current headcount or a generally promised delivery time.
- [Rijkswaterstaat](https://www.twyns.com/cases/rijkswaterstaat) describes a waterway rollout beginning in August 2020. It establishes a specialist use context, not today's user population.
- [About Twyns](https://www.twyns.com/over-twyns) describes Parkius and Redora combining in 2019, the Twyns name from 2021 and about 25 people. The staffing statement is undated and is not treated as current measured headcount.
- [The Accoris summary](https://www.twyns.com/cases/wpg-audit-accoris) discusses Redline application assurance and additional customer controls. The full report was not obtained; no current certification validity or universal compliance claim is inferred.
- [The OM instruction](https://www.om.nl/onderwerpen/b/beleidsregels/instructies/privacy/instructie-besluit-politiegegevens-buitengewoon-opsporingsambtenaren-en-de-rol-van-de-officier-van-justitie) gives authoritative context for BOA investigative processing. Actual purpose, powers, recipients and lifecycle schedules require responsible-authority review for each enabled workflow.

All personas are composites. JTBD, adoption journeys, strategy horizons, acceptance gates, KPI definitions, modules, stores, interfaces, logical products and staffing allocations are **proposed modeling assumptions**, not customer interviews, published roadmap commitments or reverse-engineered Twyns architecture. A subscription plus contracted implementation/support is a working business-model assumption; public pricing, fee bases, margins and revenue were not established. Fine and tax receipts belong to the relevant authority process and are not asserted to be Twyns revenue.

## Value exchange and strategic sequence

Authorities commission usable enforcement outcomes; practitioners gain reliable records and handoffs; residents gain understandable reporting and response routes. Partners provide qualified devices, source data and receiving systems. Supplier economics depend, as a model assumption, on retained authority contracts and reusable delivery with sustainable service effort.

Year 1 establishes accepted workflows, data responsibilities, review quality and recovery in a narrow authority pilot. Year 3 reuses tested configurations, connects departments and reduces repairs and support burden. Year 5 extends through independently approved jurisdiction and specialist packs, with demonstrable export and supplier-substitution paths. These horizons are relative to model adoption, not calendar commitments by Twyns.

Tradeoffs are explicit: review quality constrains scan throughput; purpose limits convenience of data sharing; reusable configuration constrains bespoke requests; specialist acceptance constrains geographic expansion. New investment is concentrated in rights certainty, remedies, privacy controls, partner exchange, acceptance and recovery. Brick statuses express this proposed investment posture.

## Measurement contract

Eight personas each have two outcome trees: a four-level customer pyramid (15 nodes) and a three-level supplier-business pyramid (7 nodes). The commercial tree is intentionally shallower because no finer verified unit economics are available. Every non-leaf branches at least twice. These are causal diagnostic trees, not additive numerical formulas.

Terminal values are **Not measured**. No synthetic baseline is displayed as an operating fact. Each leaf states a unit and measurement definition; reporting windows, service objectives, denominator inclusion, sampling and handling of reopened cases must be agreed with the authority. Percentile time measures refer to completed eligible events; monitor still-open backlogs separately. The two explicit pilot gates in municipal and parking strategy are illustrative assumptions for negotiation, not market benchmarks.

Public-service quality includes no-action, warning, referral, justified decision and correction outcomes. A resident does not buy a Twyns subscription; the resident persona's business tree measures the authority contract supporting that service. Policy interpretation must account for incomplete coverage and confounding; no causal benefit is asserted from higher sanction counts.

## Delivery and ownership

Four offer groupings cover supervision, parking, specialist transport configuration and implementation/assurance services. The latter two are analytical groupings, not asserted public SKUs. Seven deployment surfaces distinguish hosted operation and acceptance, managed iOS/Android distribution, back-office access, qualified interfaces and the authority's public/assisted channels. Provider, region, tenancy, distribution method, detailed API contracts and offline behavior are unverified design choices.

Twenty-four bricks are logical capability boundaries within a shared modular product, not 24 claimed microservices. Twenty-five data assets identify source ownership, producers, consumers, stores and team stewardship. Authority purpose and record class govern retention; the model deliberately does not invent a universal statutory duration. Local rights-response snapshots do not replace permit or payment source registers. Routine policy analytics is limited to assessed non-identifying aggregates.

The compact operating scenario has four teams: Field and Case Outcomes (8), Parking and Decision Remedies (7), Platform, Data and Assurance (6), and Authority Adoption and Service Enablement (4), plus one shared leader: **26 proposed FTE**. This is close in scale to the undated company context without pretending to describe its actual organization. Every brick has one primary owner. Hosted infrastructure, specialist assurance and physical field work remain external where contracted; their cost and coverage are unknown. This staffing does not establish an independent 24/7 rota. Simultaneous bespoke implementations or separate releases for every brick would exceed the intended model.

## Competition and stress tests

The landscape contains Twyns, eight functional competitor/suite comparisons, and Genetec as an explicitly separate ecosystem option. It distinguishes Dutch specialists, adjacent VTH suites and international alternatives. Four reported statistics retain scope and dating caveats; there is no normalized market-share table. An acquisition-intent announcement for Passport is not treated as evidence of completion.

Five qualitative residuality scenarios cover rights-source outage, new jurisdictions, workload spikes, excessive disclosure and supplier substitution. Integrated residues mean present in this proposed architecture, not proven in Twyns production. Typed impacts cover customer vision, offer, stream, brick, team and competitor evaluation; effects name the affected jobs and metrics.

## Repository conventions and validation

The authoring workflow uses `.claude/skills/new-product-domain` with its strategy, customer, brick, stream, data, product, team, competition, validation and balance skills. The three `.codex` reviews are recorded in `REVIEW.md`.

Structural references: `ride-sharing-marketplace`; `transport-management-and-freight-exchange`; `occupational-health-and-safety-platform`; `maas` for current products, deployments and teams. The adjacent municipal-enforcement model was checked to avoid conflating scopes. Current `edit-products` keeps brick-to-product relationships in `deployment.json`; retired `neededBricks` and team charter fields are intentionally omitted even where older audit prose mentions them.

Creating `start/config.json` registers the domain for the current dynamically discovering generator. Source is authoritative. Generation is verified in an isolated temporary preview so existing generated documentation and unrelated worktree changes are preserved. Exact validation and review outcomes are recorded in `REVIEW.md`.

The start icon reuses the existing repository public-space shield from `municipal-public-space-enforcement/start/icons/logo.png`. It is a domain pictogram, not the Twyns company logo. No new image API was used.

Source navigation entries also register Twyns in the overview catalog and the Vortex 2016 investment group. Existing catalog entries are preserved; the catalogs themselves are not regenerated by this task.
