# Video Content Intelligence Platform

Researched: 2026-09-06. Reference business: **Media Distillery**. This is a sourced product-domain model and a proposed implementation design, not a description of private company systems or plans.

## Domain choice and value exchange

The domain turns licensed video into useful discovery, navigation and commercial signals for existing video services. Buyers fund a managed service; editorial and engineering users integrate its outputs; viewers benefit through their operator or streamer. The operator retains its viewer accounts, playback surface, subscription terms and advertising decisions.

Media Distillery describes API delivery and subscriptions based on streams, content volume or generated outputs. The current portfolio comprises Search & Discovery, Sports Engagement and Time Marker suites. [Company source](https://mediadistillery.com/)

Vortex records a June 2016 investment alongside Peak Capital and lists Media Distillery as a current software investment when reviewed. This does not establish present ownership percentages, revenue or valuation. [Investor source](https://vortexcp.com/investment/media-distillery/)

## Boundary

Core scope: ingestion, programme identity, audiovisual understanding, programme/ad boundaries, topics and chapters, semantic retrieval, episode images, previews, sports moments, versioned API delivery, quality control and service economics.

Adjacent scope: EPG/catalogue suppliers, content management, operator players, sports feeds and advertising platforms. They are external systems with explicit contracts. Gracenote cooperation is publicly documented. [Partner source](https://gracenote.com/newsroom/media-distillery-and-nielsens-gracenote-join-forces-to-optimize-electronic-programme-guide-epg-utility/)

Excluded scope: owning video rights, producing broadcasts, operating consumer streaming subscriptions, a full ad exchange or CDN/player, general media monitoring, and biometric identity databases. Content-level recognition does not imply rights to identify private people or train across tenants.

## Strategic spine

Vision: turn existing video rights and catalogue into trusted viewing progress, with repeatable delivery economics.

- Year 1: establish acceptance sets, safe playback boundaries, editorial review and reliable delivery on a limited contracted cohort with measured baselines.
- Year 3: reuse certified integrations across discovery, sports and contextual advertising; expand where quality, audience outcomes and unit economics justify it.
- Year 5: preserve useful metadata, rights context and operational portability as formats, model providers and distribution partners change.

Proposed domain north star: **Accepted output delivery rate**, paired with persona-specific viewing and commercial outcomes. Volume alone cannot establish value; correct alignment, timely downstream acceptance and customer benefit must also hold.

Illustrative first-year pilot gates, to negotiate: at least 99% accepted output delivery within an agreed use-case deadline; at least 98% adjudicated break detection precision with zero accepted critical content-truncation defects; at least 20% lower median discovery effort against a defined control. These are modeling hypotheses with unknown baselines, not published targets or SLAs. Later horizons require demonstrated improvement over the measured baseline before expansion.

## Evidence and assumptions

Facts and access dates are catalogued in `customers/insights.json`. Insights separate source observations from proposed implications. Undated pages carry access dates, not invented publication dates. Case results are vendor-reported, cohort-specific observations, not guaranteed causal uplift. The NLZIET Olympics comparison is against regular programming, not a randomized control. [Case study](https://mediadistillery.com/cases/nlziet-case-study)

All personas, metrics, horizons, modules, stores, runtime boundaries, rights controls and staffing are proposed design. Public sources do not establish private repositories, cloud accounts, SLA terms, training permissions or internal budgets. KPI baselines are unmeasured. Source-grounded outputs need confidence, corrections and provenance. Supplied content rights remain the operator’s authority. Governance text is a contract-design proposal, not a claim of existing compliance or legal advice.

The proposed operating model has six teams (36 delivery FTE) and two shared leadership roles. This deliberately falls below the eight-team heuristic: splitting every AI feature into a separate team would fragment ownership. It is a scale-up planning option, not Media Distillery’s reported headcount. Shared incident coverage, managed infrastructure and phased sports expansion are prerequisites.

Competition covers specialist overlap, general video-AI substitutes, adjacent metadata providers and internal development. Gracenote is a partner/adjacent player. Unverified comparable financial figures are omitted.

## Workflow and structural references

Inspected `ride-sharing-marketplace` for customers, bricks, streams, data and competition; `maas` for current products/deployment/teams; `digital-news-publishing-platform` for editorial and advertising boundaries; `bi-dashboard-extensions-platform` for B2B integration and Vortex navigation patterns. Structures were reused; business content was independently authored.

Authoring follows `.claude/skills/new-product-domain` and its strategy/edit/validate/balance skills. All three `.codex/skills/gpa-*` reviews are saved in `REVIEW.md`. The current deployment schema is version 4: brick-to-product relationships live in `deployment.json`, without retired per-product `neededBricks` or interface catalogues.
