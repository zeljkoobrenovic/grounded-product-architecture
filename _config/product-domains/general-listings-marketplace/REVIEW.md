# general-listings-marketplace Review

## Product Domain Review

Updated: 2026-06-17

### Executive assessment

- Recent changes materially improved the strategic grounding: `_domain/DOMAIN.md` now states an EU-centric horizontal classifieds scope, category priorities, monetization model, non-goals, and sequencing tradeoffs.
- Customer segmentation is credible and materially distinct across local buyers, casual sellers, professional merchants, and merchant SaaS/feed partners. The partner side is now better reflected in teams and deployments than in the previous review.
- Competition and customer links are much stronger: the model now covers horizontal classifieds, social/local substitutes, C2C recommerce, motors, real estate, jobs, integration platforms, payment/shipping rails, and EU regulatory context.
- Evidence quality improved because EU DSA and P2B sources were added and unsupported claims are explicitly summarized as assumptions. The remaining weakness is that 10 of 20 insights still have no `sourceIds`, so discovery/search, merchant ROI, pricing, feed reliability, and marketplace-intelligence claims are not yet research-backed.
- The largest cross-model defect remains customer-to-implementation traceability: all 54 `streamsNeeded` references in customer job steps point to product-brick IDs, while none point to the 12 product-stream IDs.
- KPI architecture is broad and useful, but the 55 `currentValue` fields and 23 `dashboard.example.com` links still read as synthetic data unless the model labels them as examples, baselines, targets, or placeholders.

### High-priority findings

1. Customer jobs still bypass product streams.
   - Evidence: `_config/product-domains/general-listings-marketplace/customers/customers.json` jobs `jtbd-cg1-1`, `jtbd-cg1-2`, `jtbd-cg2-1`, `jtbd-cg2-2`, `jtbd-cg3-1`, `jtbd-cg3-2`, and `jtbd-cg4-1` use `steps[].streamsNeeded[].id` values such as `home`, `serp`, `cmse`, `papl`, `clim`, and `svih`. These are brick IDs. None of the 54 references use product-stream IDs such as `buyer-search-save-and-return`, `seller-publish-a-good-listing-fast`, or `platform-operate-marketplace-integration-and-operations` from `product-bricks/product-stream.json`.
   - Why it matters: Product streams are supposed to explain outcome delivery between JTBD and implementation. The current customer model jumps directly to bricks, so generated docs cannot show how a buyer, seller, or partner job maps to a coherent flow.
   - Suggested direction: Add stream-level references from JTBD steps to product-stream IDs first, then keep brick-level references as implementation dependencies under the stream or a renamed field.

2. KPI values and dashboard links look measured but are not provenance-backed.
   - Evidence: `_config/product-domains/general-listings-marketplace/customers/customers.json` contains 55 `currentValue` fields and 23 links under `https://dashboard.example.com/general-listings-marketplace/...`.
   - Why it matters: The KPI tree appears operationally mature, but readers cannot tell whether numbers are synthetic examples, measured baselines, current production values, or targets. Placeholder dashboard URLs weaken confidence in strategy and review output.
   - Suggested direction: Add explicit baseline/target/provenance semantics, or label current values and dashboard links as examples until real measurement owners and links exist.

3. Insight assumptions are explicit but still mixed with sourced findings.
   - Evidence: `_config/product-domains/general-listings-marketplace/customers/insights.json` has 20 items and four sources (`ftc-inform`, `ftc-marketplace-consumers`, `eu-dsa`, `eu-p2b`). Items `glm-05`, `glm-06`, `glm-09`, `glm-12`, `glm-13`, `glm-14`, `glm-15`, `glm-16`, `glm-17`, and `glm-20` have empty `sourceIds`; their summaries begin with "Assumption:".
   - Why it matters: The assumptions are useful, but they sit in the same collection as sourced regulatory findings. The model can overstate evidence for discovery quality, feed health, merchant ROI, pricing confidence, saved alerts, and marketplace intelligence.
   - Suggested direction: Add an evidence type or confidence field that separates sourced insight, assumption, hypothesis, and inferred strategy. Add authoritative sources for marketplace liquidity, ranking/search behavior, seller monetization, feed APIs, pricing guidance, and transaction trust.

### Medium-priority findings

1. Competitive scope is broader, but direct competitors and benchmarks need clearer labels.
   - Evidence: `_config/product-domains/general-listings-marketplace/_domain/DOMAIN.md` defines a primary European horizontal-classifieds market. `business/competition.json` includes EU-relevant references such as OLX, Adevinta, Vinted, Wallapop, Rightmove, and Auto Trader UK, but also U.S. or global benchmarks such as Craigslist, OfferUp, Zillow, Indeed, Mercari, and Facebook Marketplace.
   - Why it matters: These are useful substitutes and benchmarks, but without a direct/substitute/benchmark role readers may treat incomparable businesses and regions as equal competitors.
   - Suggested direction: Add competitor role, region relevance, and category relevance fields or make those distinctions explicit in descriptions and caveats.

2. Journey stories still carry generated phrasing.
   - Evidence: `_config/product-domains/general-listings-marketplace/customers/customers.json` journey narratives include repeated phrases such as "the current way of working can no longer protect..." and media alt text such as "Enterprise journey panel" for buyer, casual seller, professional merchant, and partner journeys.
   - Why it matters: The customer strategy is stronger than the journey copy. Generated wording makes the model feel less grounded in real marketplace behavior and weakens the generated documentation.
   - Suggested direction: Rewrite the main journey stories around concrete marketplace triggers: scam exposure, stale local supply, noisy results, feed failures, moderation rejects, merchant lead leakage, and partner breaking changes.

3. Category-gated transaction strategy should be carried into customer horizons.
   - Evidence: `_domain/DOMAIN.md` says protected transactions start in shippable goods/recommerce and are not forced onto motors, real estate, jobs, or services. Customer strategies for `cg1-p1` and `cg2-p1` discuss expanding protection, payment, shipping, reservation, proof-of-handoff, and transaction rails across high-risk or high-value categories.
   - Why it matters: The brief has the right tradeoff, but the customer horizon copy can still be read as a broad transaction-platform push. That risks blurring the intentional lead-generation model for motors, real estate, jobs, and services.
   - Suggested direction: Add category gates and explicit non-goals inside the relevant customer horizons and milestones, not only in the domain brief.

4. Customer links are useful but should become more traceable to insights and competition.
   - Evidence: `_config/product-domains/general-listings-marketplace/customers/links.json` now has eight groups covering reference marketplaces, industry background, trust/compliance, partner APIs, local substitutes, verticals, payment/shipping infrastructure, and EU platform regulation.
   - Why it matters: The curated links are a good context layer, but they are not connected to insight IDs, competitor IDs, or customer/job IDs. Readers cannot see which links support which modeled claims.
   - Suggested direction: Add optional references from links to insight IDs, competitor IDs, customer IDs, or JTBD IDs where a link materially grounds the model.

### Targeted improvement backlog

1. Update `customers/customers.json` so JTBD steps reference product-stream IDs from `product-bricks/product-stream.json`; keep brick IDs as lower-level implementation dependencies.
2. Add KPI provenance semantics to `customers/customers.json`: example, baseline, target, measured source, owner, reporting date, and dashboard URL status.
3. Split `customers/insights.json` items into sourced findings and assumptions, then add sources for marketplace liquidity, search/ranking, pricing guidance, merchant economics, feed reliability, and safe transaction behavior.
4. Add direct/substitute/benchmark role labels and region/category relevance to `business/competition.json`.
5. Rewrite the highest-traffic journey stories for `jtbd-cg1-1`, `jtbd-cg1-2`, `jtbd-cg2-1`, `jtbd-cg3-1`, and `jtbd-cg4-1`.
6. Carry category-scoped transaction rules from `_domain/DOMAIN.md` into customer strategy horizons for buyers and casual sellers.
7. Add optional trace links from `customers/links.json` to related insight, competitor, customer, or job IDs.

### Open assumptions

- Are the KPI `currentValue` fields examples, measured baselines, target values, or seeded demo data?
- Should `streamsNeeded` be redefined as brick references, or should customer jobs explicitly reference product streams?
- Which competitors are direct EU operating competitors versus global benchmarks or substitutes?
- Which unsupported insights are intended as accepted strategic assumptions versus hypotheses awaiting research?
- How far should protected transactions expand beyond shippable goods, and what category economics gate that expansion?
- Should customer links remain context-only, or become first-class evidence supporting insights and competitive claims?

## Product Bricks Review

Updated: 2026-06-17

### Architecture assessment

- The implementation model is broad and mostly well-wired: 88 bricks, 12 product streams, 20 data assets, 26 teams, no missing brick owners, no missing stream brick dependencies, no missing data asset references, and no invalid data owner team IDs were found.
- Recent data changes fixed the previous high-risk ownership defects. Data assets now align with their system-of-record brick owners, and duplicate `role: own` data dependencies were not found.
- Product and deployment coverage improved: `products.json` and `deployment.json` now reference 23 unique bricks, including partner-support bricks such as `ause`, `buan`, `doma`, and `prba`.
- The remaining architecture risk is not reference validity; it is realism. Every brick has exactly three brick dependencies, every brick has exactly two inbound and two outbound external-system relationships, and repeated module signatures make unlike capabilities look operationally identical.
- Streams are outcome-named, but they are not yet acting as the strategy-to-architecture bridge because customer jobs do not reference them and stream flows still contain repeated generated key facts and pain points.
- Investment status is too narrow for the stated strategy: only six bricks are marked `invest`, while protected transactions, payments, partner APIs, fraud/risk, pricing intelligence, data products, and marketplace intelligence remain `sustaining`.

### Critical findings

1. JTBD-to-stream traceability is absent.
   - Severity: High
   - Source: `_config/product-domains/general-listings-marketplace/customers/customers.json` `jobsToBeDone[].steps[].streamsNeeded`; `_config/product-domains/general-listings-marketplace/product-bricks/product-stream.json`.
   - Why it matters: The 12 product streams should be the primary architecture bridge from customer progress to composed bricks. Instead, all 54 customer job references point directly to bricks and none point to streams.
   - Suggested direction: Link job steps to stream IDs first, then let streams carry the composed `brickDependencies`, external systems, and flow steps.

2. The dependency graph looks generated rather than operational.
   - Severity: High
   - Source: `_config/product-domains/general-listings-marketplace/product-bricks/product-bricks.json` `brickDependencies`, `externalSystemsThisBrickDependsOn`, and `externalSystemsDependingOnThisBrick`.
   - Why it matters: All 88 bricks have exactly three brick dependencies. Dependency targets are heavily concentrated on `loin` (67 incoming), `opad` (63), `ccma` (55), and `csor` (29). Every brick also has exactly two external systems it depends on and two external systems depending on it. This pattern hides real runtime, data, risk, and operational dependencies.
   - Suggested direction: Prune boilerplate dependencies and keep relationships that shape ownership, reliability, data movement, policy, release sequencing, or incident response. Add missing real dependencies only where they affect delivery or risk.

3. Deployment traceability still covers only a minority of the architecture.
   - Severity: High
   - Source: `_config/product-domains/general-listings-marketplace/product-deployments/products.json`; `_config/product-domains/general-listings-marketplace/product-deployments/deployment.json`; `_config/product-domains/general-listings-marketplace/product-bricks/product-bricks.json`.
   - Why it matters: Products and channels now reference 23 unique bricks, but 65 of 88 bricks remain outside product and deployment coverage. Important capabilities such as `acsc`, `frde`, `clre`, `pres`, `damo`, `dapl`, `ccma`, `clma`, `geor`, `maau`, `spma`, `pdto`, and `qato` are not connected to a delivery surface.
   - Suggested direction: Add platform, data, trust/risk, monetization, and operations deployment surfaces where these bricks are delivered or operated. For intentionally non-deployable bricks, add an explicit modeling convention rather than leaving them absent.

### Model-quality findings

1. Stream flow details are still too generic.
   - Severity: Medium
   - Source: `_config/product-domains/general-listings-marketplace/product-bricks/product-stream.json` flows such as `buyer-browse-interesting-listings-flow`, `seller-publish-a-good-listing-fast-flow`, `pro-seller-run-a-storefront-flow`, and `users-transact-on-a-trusted-marketplace-flow`.
   - Why it matters: Repeated phrases such as "Users need clear guidance and feedback here to keep moving forward" and "Confidence decreases when the product does not explain what happens next" appear across many stream steps. The stream names are good, but the flow facts do not yet expose classifieds-specific operational reality.
   - Suggested direction: Rewrite flow facts and pain points around marketplace-specific constraints: stale supply, listing quality, seller credibility, scam risk, moderation rejects, feed validation, protected payment state, dispute handling, and category-specific handoffs.

2. Module models repeat a small set of templates across unlike capabilities.
   - Severity: Medium
   - Source: `_config/product-domains/general-listings-marketplace/product-bricks/product-bricks.json` `layers`.
   - Why it matters: Thirty-four bricks share the same operations-workspace/service-api/domain-event-feed/core-domain-engine pattern, and thirteen share the same user-experience-interface/experience-backend-api/event-stream/service pattern. Search, payments, identity, fraud, feeds, media, analytics, and developer tooling should not all look architecturally interchangeable.
   - Suggested direction: Customize module shapes for the highest-risk domains: search/ranking, payments and protected transactions, identity and consent, fraud/risk scoring, feed ingestion, media processing, data platform, analytics, partner APIs, and support operations.

3. Investment status is not aligned to the strategic sequencing.
   - Severity: Medium
   - Source: `_config/product-domains/general-listings-marketplace/product-bricks/product-bricks.json` `status`.
   - Why it matters: Only `serp`, `ssal`, `cdpc`, `esfu`, `prpa`, and `ocma` are marked `invest`. Strategy also depends on `hpfi`, `papl`, `svih`, `clim`, `acsc`, `frde`, `pres`, `buan`, `dapl`, and `damo`, but these are all `sustaining`.
   - Suggested direction: Reclassify statuses by horizon and category gate: foundational discovery/listing work, transaction rails for goods, partner integration, trust/risk controls, pricing intelligence, and data monetization.

4. Legacy and placeholder language remains in brick descriptions.
   - Severity: Low
   - Source: `_config/product-domains/general-listings-marketplace/product-bricks/product-bricks.json` examples include `home` with "General Listings Marketplace brand brands", `b2cr` and `b2cc` Salesforce/country-specific CRM descriptions, and long names such as `Professional Seller / Dealer / Storefront Entity Single Source of Truth`.
   - Why it matters: The generated architecture pages will expose this language. It makes the model feel partly imported from a legacy capability map rather than intentionally normalized for this domain.
   - Suggested direction: Normalize descriptions into concise current product language and expand unavoidable legacy acronyms once.

### Traceability findings

1. Streams lack explicit customer, job, and KPI references.
   - Severity: High
   - Source: `_config/product-domains/general-listings-marketplace/product-bricks/product-stream.json`.
   - Why it matters: Streams are named around buyer, seller, professional seller, trust, and platform outcomes, but they do not contain explicit customer IDs, job IDs, KPI names/IDs, or strategy horizon references. Generated pages must infer mappings from names.
   - Suggested direction: Add supported mapping fields if the generator supports them; otherwise encode concise references in stream descriptions and flow metadata.

2. Data assets are structurally sound but not visible enough in streams and deployments.
   - Severity: Medium
   - Source: `_config/product-domains/general-listings-marketplace/data/data-assets.json`; `_config/product-domains/general-listings-marketplace/product-bricks/product-stream.json`; `_config/product-domains/general-listings-marketplace/product-deployments/products.json`.
   - Why it matters: The data model is now strong: assets have owners, classifications, stores, interfaces, governance, and system-of-record bricks. But critical assets such as `trust-signal`, `payment-ledger`, `identity-verification-record`, `search-query-event`, and `listing` are only indirectly visible through brick dependencies, not through the streams or deployment products that carry the strategic risk.
   - Suggested direction: For high-risk streams, call out the data assets that make the flow reliable, compliant, or measurable. Add deployment/data-product surfaces for data platform and marketplace intelligence where applicable.

3. Partner architecture is improved but still blended into the professional seller product.
   - Severity: Medium
   - Source: `_config/product-domains/general-listings-marketplace/product-deployments/products.json` product `p3`; `_config/product-domains/general-listings-marketplace/teams/teams.json` team `merchant-platform-merchant-platform`; `_config/product-domains/general-listings-marketplace/product-bricks/product-bricks.json` bricks `svih`, `ause`, `buan`, `doma`, `prba`, and `clim`.
   - Why it matters: Recent changes added partner APIs, authentication, analytics, documents, and backoffice support to `p3`, which is good. But `cg4-p2` still shares the Professional Seller Workspace product rather than having a clearly named partner integration platform surface.
   - Suggested direction: Either rename/split `p3` to make the partner integration surface first-class, or add a dedicated partner product that owns API docs, sandbox, certification, diagnostics, auth scopes, and support workflows.

### Edit backlog

1. Change customer job `streamsNeeded` references from brick IDs to product-stream IDs, then keep brick dependencies inside streams.
2. Add explicit stream-to-customer/job/KPI mappings in `product-stream.json` or in generator-supported metadata.
3. Prune generated brick dependencies and external-system boilerplate; keep only relationships with real delivery, reliability, data, policy, or operational impact.
4. Extend deployment modeling beyond the 23 currently covered bricks, especially for trust/risk, data/intelligence, platform services, monetization, operations, and quality tooling.
5. Customize module shapes for search/ranking, payments, identity, fraud/risk, feeds, media, analytics, data platform, partner APIs, and support operations.
6. Reclassify brick investment statuses to match the domain brief's sequencing and customer strategy horizons.
7. Rewrite stream flow key facts and pain points with classifieds-specific operational detail.
8. Preserve the corrected data ownership model and make high-risk data assets visible in relevant streams and deployment products.

## Teams Review

Updated: 2026-06-17

### Operating-model assessment

- Recent changes materially improved the team model. The domain now has 24 delivery teams: 10 stream-aligned teams, 13 platform teams, and 1 complicated-subsystem team, with Marketplace Growth, Merchant & Partner Platform, and Marketplace Foundations as the main operating groups.
- Staffing arithmetic is internally consistent. Delivery teams sum to 238 FTE, role counts also sum to 238, and the three group-leadership blocks add 12 FTE, matching the stated 250 FTE principle.
- Product-brick ownership is structurally strong: all 88 bricks have exactly one owning team, no duplicate owners were found, all team dependencies resolve, and all data assets now align with the owning team of their system-of-record brick.
- The previous partner gap is fixed. `partner-platform` explicitly owns customer `cg4-p2`, partner API reliability, certification, sandbox-to-production flow, connector templates, feed diagnostics, and partner support.
- The remaining weakness is not basic reference integrity. It is operating clarity: several product streams span many owning teams without an explicit stream owner, platform teams use external `primaryCustomers` where consuming-team contracts would be clearer, and team KPI names drift from the customer KPI model.
- AI-agent boundaries remain appropriate. Agents are software-delivery assistants for backend, frontend, QA, code review, and release-risk work, with human review, testing, and production-change controls.

### Ownership findings

1. Buyer homepage ownership is assigned to the seller listing team.
   - Severity: High
   - Affected team/group ID: `seller-growth-listing-funnel`, `buyer-growth-discovery`, `buyer-engagement-comms`
   - Source: `_config/product-domains/general-listings-marketplace/teams/teams.json` team `seller-growth-listing-funnel`; `_config/product-domains/general-listings-marketplace/product-bricks/product-bricks.json` brick `home`; `_config/product-domains/general-listings-marketplace/product-deployments/products.json` product `p1`; `_config/product-domains/general-listings-marketplace/product-bricks/product-stream.json` stream `buyer-browse-interesting-listings`.
   - Why it matters: `home` is modeled as a buyer/seeker homepage, is used by the Buyer Discovery Experience product, and appears in the buyer browsing stream. Assigning it to `seller-growth-listing-funnel` gives the seller listing team ownership over a buyer acquisition and discovery surface.
   - Suggested direction: Reassign `home` to `buyer-growth-discovery` or `buyer-engagement-comms`, or split it into buyer homepage and seller listing-entry bricks if both flows need distinct ownership.

2. Product stream ownership is still implicit and handoff-heavy.
   - Severity: High
   - Affected team/group ID: `buyer-growth-discovery`, `buyer-discovery-intelligence`, `marketplace-growth-casual-seller-household-lister`, `seller-success-experience`, `merchant-platform`, `marketplace-foundations`
   - Source: `_config/product-domains/general-listings-marketplace/product-bricks/product-stream.json`; `_config/product-domains/general-listings-marketplace/teams/teams.json`.
   - Why it matters: Streams now correctly appear in customer jobs, but teams do not own product-stream IDs. `buyer-contact-sellers-confidently` uses 8 bricks owned by 8 teams, `seller-manage-live-listings` uses 7 bricks owned by 6 teams, and `platform-operate-shared-experience-foundation` uses 8 bricks owned by 6 teams. Without a stream owner or steward, incidents, roadmap tradeoffs, and KPI accountability are inferred from brick ownership.
   - Suggested direction: Add explicit stream ownership to the model, such as `ownedProductStreams`, `primaryStreamOwnerTeamId`, or stream-level steward/supporting-team fields. For high-traffic streams, name the accountable lead team and the recurring platform contracts.

3. Data stewardship still references a removed team ID.
   - Severity: Medium
   - Affected team/group ID: `platform-core-services`
   - Source: `_config/product-domains/general-listings-marketplace/data/data-assets.json`; `_config/product-domains/general-listings-marketplace/teams/teams.json`.
   - Why it matters: Data ownership is now aligned with system-of-record brick ownership, but 9 data assets still list `platform-core-services` in `stewardTeamIds`. That team no longer exists in `teams.json`, so stewardship for saved search, conversation, customer contact, transaction, payment, geo, listing, and media assets cannot resolve.
   - Suggested direction: Replace `platform-core-services` with current platform teams by asset domain: `experience-services-platform` for conversations and notifications, `payments-and-transactions` for payment and transaction assets, `marketplace-foundations-data-2` for geo/catalog/tracking, and `trust-and-identity` or `identity-verification-platform` where privacy or identity control is the stewardship concern.

4. Owned bricks still lack product and deployment visibility.
   - Severity: Medium
   - Affected team/group ID: multiple teams, including `marketplace-growth-casual-seller-household-lister`, `buyer-engagement-comms`, `buyer-discovery-intelligence`, `seller-success-experience`, `developer-platform`, and `marketplace-foundations-frontend-core`
   - Source: `_config/product-domains/general-listings-marketplace/teams/teams.json`; `_config/product-domains/general-listings-marketplace/product-deployments/products.json`; `_config/product-domains/general-listings-marketplace/product-deployments/deployment.json`; `_config/product-domains/general-listings-marketplace/product-bricks/product-bricks.json`.
   - Why it matters: Product and deployment coverage improved to 62 of 88 bricks, but 26 owned bricks are still absent from products and deployment channels, including `ccnm`, `copo`, `arre`, `orma`, `ubws`, `sema`, `awfo`, `desy`, `unfr`, `ustr`, and `udpr`. Teams are accountable for capabilities whose delivery surface is not modeled.
   - Suggested direction: Add internal platform, operations, analytics, and customer-product surfaces for these bricks, or mark intentionally non-deployable bricks with a clear convention so team accountability is not mistaken for deployable product coverage.

### Topology and staffing findings

1. Marketplace Foundations is more coherent, but still contract-heavy.
   - Severity: Medium
   - Affected team/group ID: `marketplace-foundations`
   - Source: `_config/product-domains/general-listings-marketplace/teams/teams.json` group `marketplace-foundations` and nested families `identity-and-trust`, `payments-and-transactions`, `experience-platform`, `data-and-intelligence`, and `developer-platform`.
   - Why it matters: The previous fragmentation is improved, but Marketplace Foundations still contains 12 of 24 delivery teams and 119 of 238 delivery FTE. That is plausible for a data-heavy marketplace, but only if the platform teams operate through explicit contracts, SLOs, incident ownership, support tiers, and roadmap intake from stream-aligned teams.
   - Suggested direction: Keep the five durable platform families, but make each platform team's provided/dependent interfaces operational: API/data contracts, consumers, SLOs, on-call boundaries, release gates, and escalation paths.

2. Platform teams use external customers as primary customers.
   - Severity: Medium
   - Affected team/group ID: all 13 platform teams, especially `developer-platform`, `marketplace-data-platform`, `marketplace-foundations-frontend-core`, `marketplace-analytics`, and `marketplace-data-monetization`
   - Source: `_config/product-domains/general-listings-marketplace/teams/teams.json` `primaryCustomers`; `_config/product-domains/general-listings-marketplace/customers/customers.json`.
   - Why it matters: Platform teams often list external marketplace customers as primary customers, even when their actual operating customer is an internal team. This blurs direct outcome ownership. For example, `developer-platform` lists `cg1-p1` and `cg2-p1`, although its real customers are delivery teams using build, test, deployment, and on-call tooling.
   - Suggested direction: Split semantics: keep `primaryCustomers` for direct external outcome ownership, add `consumerTeamIds` or `platformConsumers` for internal consumers, and use `customerImpact` to explain which external outcomes the platform supports indirectly.

3. Some topology labels and placements still blur team intent.
   - Severity: Medium
   - Affected team/group ID: `merchant-crm-contracts`, `buyer-engagement-comms`, `marketplace-foundations-data-2`
   - Source: `_config/product-domains/general-listings-marketplace/teams/teams.json`.
   - Why it matters: `merchant-crm-contracts` sits under the Experience Platform family even though its bricks (`b2cr`, `b2cc`, `ucga`) are merchant commercial systems. `buyer-engagement-comms` mixes SEO, consumer advertising, and the unified web shell. `marketplace-foundations-data-2` still carries a generated suffix. These are not fatal, but they weaken the otherwise clearer operating model.
   - Suggested direction: Move `merchant-crm-contracts` under Merchant & Partner Platform or rename it as a commercial contracts platform; separate buyer growth work from shared web-shell platform ownership if needed; rename `marketplace-foundations-data-2` to a stable domain name such as `geo-catalog-tracking-data`.

4. High-scope teams are already at the 10-FTE ceiling.
   - Severity: Medium
   - Affected team/group ID: `market-intelligence-and-pricing`, `partner-platform`, `seller-success-experience`, `merchant-platform-professional-seller-dealer-storefront`
   - Source: `_config/product-domains/general-listings-marketplace/teams/teams.json` `ownedProductBricks` and `staffing`.
   - Why it matters: `market-intelligence-and-pricing` owns 7 bricks across catalog data, market knowledge, price estimation, rules, engine, and page experience. Several other teams own 5 bricks while also carrying customer, support, or platform obligations. The 10-FTE cap is disciplined, but these teams may be under-modeled if the roadmap assumes active investment across all owned surfaces.
   - Suggested direction: Keep the current headcount model if only part of each portfolio is active at once. If multiple owned bricks are strategic in the same horizon, split teams or add specialist capacity, especially data science, partner solutions, product operations, and reliability roles.

### Strategy alignment findings

1. Team KPI names drift from the customer KPI model.
   - Severity: High
   - Affected team/group ID: `seller-growth-listing-funnel`, `seller-success-experience`, `merchant-platform`, `partner-platform`, `payments-and-transactions`, `experience-services-platform`, `merchant-crm-contracts`, `market-intelligence-and-pricing`
   - Source: `_config/product-domains/general-listings-marketplace/teams/teams.json` `teamCharter.metrics` and `primaryCustomers.relatedKPIs`; `_config/product-domains/general-listings-marketplace/customers/customers.json` KPI pyramids.
   - Why it matters: The customer KPI model has 55 KPI names, but 21 non-operating team metrics and 32 `relatedKPIs` references do not match those names exactly. Examples include `Listing publish success rate`, `Time to first response`, `Professional seller GMV contribution`, `Lead quality score`, `Certified partner connectors live`, and `Feed validation pass rate`. Generated docs cannot reliably connect team accountability to customer KPI pyramids by name.
   - Suggested direction: Use stable KPI IDs in team metrics instead of free-text names, or normalize team metric names to the existing KPI pyramid names. Keep `metricKind: team-operating-metric` for internal platform metrics that should not roll up to customer KPIs.

2. Partner team accountability is fixed, but partner measurement still needs normalization.
   - Severity: Medium
   - Affected team/group ID: `partner-platform`, `marketplace-data-monetization`, customer `cg4-p2`
   - Source: `_config/product-domains/general-listings-marketplace/teams/teams.json`; `_config/product-domains/general-listings-marketplace/customers/customers.json`; `_config/product-domains/general-listings-marketplace/product-deployments/products.json` product `p4`.
   - Why it matters: `partner-platform` now owns `cg4-p2` and product `p4` gives partners a first-class deployment surface. However, team metrics such as `Certified partner connectors live` and `Feed validation pass rate` do not match the partner KPI language in customers and insights, which uses terms such as partner certification lead time, validation error recurrence, certified partner count, coverage, and partner-enabled supply scale.
   - Suggested direction: Normalize partner KPIs across `customers.json`, `teams.json`, `insights.json`, and product `p4`; use IDs to connect certification, validation, reliability, supply scale, and partner support outcomes.

3. Trust and transaction control ownership is improved but still needs an explicit operating contract.
   - Severity: Medium
   - Affected team/group ID: `trust-and-identity`, `identity-verification-platform`, `payments-and-transactions`, `experience-services-platform`
   - Source: `_config/product-domains/general-listings-marketplace/teams/teams.json`; `_config/product-domains/general-listings-marketplace/data/data-assets.json`; product bricks `hpfi`, `papl`, `idve`, `frde`, `acsc`, `ccma`, `cmse`.
   - Why it matters: The data and brick ownership model is now coherent, but safe completion depends on shared policy decisions across fraud, actor scoring, identity verification, messaging, payment ledger, protected checkout, disputes, and incident response. Mutual dependencies among trust, identity, payments, and data platform teams are reasonable, but need a named decision owner for controls.
   - Suggested direction: Define a Trust and Transactions control contract: policy owner, approval rights, escalation path, model/rule release process, incident commander, audit evidence owner, and category gates for protected transactions.

4. Platform products use external customer labels too narrowly.
   - Severity: Medium
   - Affected team/group ID: products `p5`, `p6`, `p7`; teams in `marketplace-foundations`
   - Source: `_config/product-domains/general-listings-marketplace/product-deployments/products.json`; `_config/product-domains/general-listings-marketplace/teams/teams.json`.
   - Why it matters: `Trust & Safety Platform` lists only `cg1-p1`, `Marketplace Data & Intelligence` lists only `cg3-p1`, and `Platform & Operations` lists only `cg2-p1`, while the related platform teams support multiple external customer outcomes and many internal consuming teams. This mirrors the platform `primaryCustomers` issue and can hide who actually consumes the platform.
   - Suggested direction: Add internal platform consumers and customer-impact mapping to products, or separate external customer-facing products from internal platform products.

### Edit backlog

1. Reassign `home` from `seller-growth-listing-funnel` to the buyer discovery or buyer engagement team, or split the brick if the homepage has separate buyer and seller entry surfaces.
2. Add explicit product-stream ownership fields for the 12 streams, including lead team, supporting teams, and operating contract per high-traffic stream.
3. Replace stale `platform-core-services` steward references in `data/data-assets.json` with current team IDs.
4. Normalize team KPI references against customer KPI IDs; keep team operating metrics separate with `metricKind: team-operating-metric`.
5. Split `primaryCustomers` from platform consumer semantics by adding `consumerTeamIds`, `platformConsumers`, or `customerImpact` fields for platform teams.
6. Add product/deployment coverage or explicit non-deployable conventions for the 26 owned bricks not present in products or deployment channels.
7. Rename or relocate residual topology mismatches: `marketplace-foundations-data-2`, `merchant-crm-contracts`, and possibly `buyer-engagement-comms`.
8. Define the Trust and Transactions control contract across `trust-and-identity`, `identity-verification-platform`, `payments-and-transactions`, and `experience-services-platform`.
9. Recheck staffing for high-scope teams if the roadmap invests in several owned bricks at once, especially `market-intelligence-and-pricing` and `partner-platform`.
10. Preserve the current bounded AI-agent model; only add team-specific agent detail where it maps to concrete engineering risks or repos.
