# digital-supervision-and-enforcement-platform Review

This review applies the three `.codex` review skills and the `.claude` balance audit to the new source model. It distinguishes completeness of the model from verification of Twyns' actual implementation. No customer interviews, private architecture, current contracts, full audit report or operational measurements were supplied.

## Product Domain Review

Updated: 2026-09-06

### Executive assessment

- The boundary fits the two supplied references: a configurable supervision and enforcement service, including parking and specialist transport contexts. The brief distinguishes the neighboring municipal-public-space and broader mobility models.
- Four groups contain eight materially distinct personas: buyers/operators (`mund`, `pkmg`), practitioners (`boao`, `casw`), transport/partners (`trop`, `intp`), and assurance/public beneficiaries (`dpof`, `citi`). Each has two operational jobs, a six-stage adoption journey, two KPI trees and distinct 1/3/5-year priorities.
- The public-beneficiary model correctly uses authority channels and assisted contact. It does not invent a Twyns consumer subscription or classify fine income as supplier revenue.
- Thirteen insights separate sourced observations from implications, using twenty primary source entries. Undated staffing and customer counts, historic case results, audit scope and acquisition intent retain explicit caveats.
- KPI baselines are unmeasured. Customer trees have 15 nodes and supplier-business trees have 7, with no single-child branches. Names used in strategy resolve to the relevant trees, and KPI definition IDs are unique across the file.

### High-priority findings

No unresolved P1 findings after the corrections below.

**Resolved — customer-to-offer coverage.** Evidence: `customers/customers.json` jobs `mrol`, `tchg`, `icon`, `irec`, `pacc`, `prec`; `product-bricks/product-stream.json` streams `rsvc`, `dred`; `product-deployments/deployment.json` product `park`. The initial generic recovery stream depended on parking-only components, while the parking offer omitted administrative follow-up used by its decision stream. This made some customer jobs reference capabilities absent from their linked offers. The recovery flow now uses shared case, purpose and communication controls; parking explicitly includes authority-configured administrative follow-up. The complete reference-path check passes.

### Medium-priority findings

**P2 — outcome definitions require customer validation.** Evidence: `customers/customers.json`, all `*-ctop` trees and strategy horizons; `customers/insights.json`, `i001`–`i013`. The personas and causal metrics are research-based hypotheses, not observed customer behavior. Before treating targets as delivery commitments, agree cohort membership, due-date rules, sampling and comparable reporting windows with a municipal buyer, a parking manager, an officer and a case reviewer. Preserve `Not measured` until actual data is available.

**P2 — procurement economics and rollout capacity are unverified.** Evidence: `_domain/DOMAIN.md`, `products.json` offer `impl`, and the business KPI trees. Subscription and service fees are explicit assumptions. Actual pricing units, minimum contract scope, implementation effort and renewal economics could change the chosen offer boundaries. Validate these through commercial discovery before using the model for investment sizing.

**P3 — comparison detail is intentionally bounded.** Evidence: `business/competition.json`, `brik`, `roxi`, `tara`, `pass`. Some headquarters cities are unresolved, international procedure compatibility is not established, and the Passport source establishes acquisition intent rather than completion. None is used to infer local compatibility or rank market share. Refresh only when a concrete procurement comparison needs that fact.

### Targeted improvement backlog

1. Validate the composite personas and measurement contracts in `customers/customers.json`; replace unknown baselines with dated, scoped observations.
2. Validate commercial units and rollout acceptance with authority buyers; adjust `product-deployments/*.json` and the relevant business metrics together.
3. Extend `business/competition.json` with verified tender-specific comparisons, preserving the difference between Dutch specialists, wider VTH suites, international alternatives and the Genetec partnership.

### Open assumptions

The proposed roadmap, product groupings, KPI gates, current staffing, service economics and geographic rollout sequence are not published Twyns commitments. The Accoris public summary does not establish current certificate validity or completion of authority-side controls. The model makes no claim about actual legal sufficiency for a particular deployment.

## Product Bricks Review

Updated: 2026-09-06

### Architecture assessment

- Twenty-four bricks form four root groups and eight subgroups. They are reusable, ownable capabilities, rather than a claim that Twyns operates 24 separate services.
- One hundred modules cover all six supported layers. The 58 brick dependencies use concrete source and target modules; public integration context is distinguished from unverified interface contracts.
- Nine outcome streams contain 36 steps with facts, friction and capability dependencies. Recovery, review, no-action outcomes and correction are part of the flows.
- Twenty-five data assets have explicit producers, primary team owners, stewards, stores and governance. The 83 brick-to-asset relationships resolve, and source snapshots are not confused with authoritative government, payment or permit records.
- All bricks participate in a stream, a deployed offer and exactly one owning team. Every customer job's stream dependencies are covered by that customer's linked offer set. Product-to-brick relationships use the current deployment schema, rather than retired `neededBricks` fields.

### Critical findings

No unresolved P1 architecture or reference findings.

**Resolved — sensitive lifecycle records were mixed with policy definitions.** Evidence: `data/data-assets.json` assets `ppol`, `life`, `comm`; `product-bricks/product-bricks.json` bricks `priv`, `case`, `evid`. Case-specific holds and lifecycle actions carry subject and case information, while reusable policy definitions can be non-personal. A separate restricted `life` asset now owns those records, with explicit consumers. Communication records are also classified for their potentially sensitive, purpose-dependent content.

**Resolved — evaluation and integration modules lacked explicit invocation paths.** Evidence: `product-bricks/product-bricks.json`, `module-rght-evaluate` and outbound adapter modules. The parking-right API and worker now invoke the evaluator, while the evaluator orchestrates source access and snapshot persistence. Outbound state modules invoke their adapters; inbound report and scan adapters retain their API entry path. Module and dependency checks pass.

### Model-quality findings

**P2 — deployment and interface contracts remain hypotheses.** Evidence: `product-deployments/deployment.json` channels `prod`, `test`, `iosd`, `andd`, `papi`; bricks `fldc`, `rght`, `xchg`, `oper`. Actual hosting provider, region, tenant isolation, mobile distribution, offline behavior, source access and acknowledgement semantics were not established from the public pages. Qualify them during authority acceptance before presenting this as a deployment specification.

**P2 — lifecycle and assurance policy needs deployment-specific evidence.** Evidence: assets `case`, `evid`, `psub`, `life`, `aggr`; bricks `priv`, `audt`; source insight `i007`. Classification alone does not establish operational controls. Obtain approved record schedules, role matrices, export boundaries and the relevant supplier assurance scope; test disposal, denied access, holds and aggregate re-identification boundaries. No universal retention duration has been invented.

### Traceability findings

The reference audit found zero unresolved customer, job, stream, brick, module, product, deployment, asset, store, steward or primary-owner gaps. Every asset has one modeled system-of-record producer, and its owner matches that capability's primary team. All five residuality scenarios resolve their typed vision, product, stream, brick, team and competitor impacts through the current generator catalog. Job and KPI effects are named in narrative because their generator-qualified identifiers use a different format from the strict source-ID convention.

Public-source links attached to bricks and streams establish operating context. They are not presented as repository, cloud-resource or production implementation evidence. No fictional evidence-database IDs were added.

### Edit backlog

1. Replace unverified interface and deployment assumptions with customer-approved contracts in `product-bricks/product-bricks.json` and `product-deployments/deployment.json`.
2. Add approved lifecycle and disclosure details to `data/data-assets.json`, preserving the `ppol`/`life` separation and local source authority.
3. Validate the five stress scenarios with an implementation team and authority operators; revise only capabilities that the exercise shows are missing or overloaded.

## Teams Review

Updated: 2026-09-06

### Operating-model assessment

- Four teams and one shared leader form a 26-FTE proposed scenario. The comparison point is an undated company statement of about 25 people; the allocation is not asserted to be Twyns' organization chart.
- The smaller team count is intentional. Eight conventional delivery teams would imply an organization substantially larger than the public company context without supporting evidence.
- `fldt` owns eight field/case capabilities, `prkt` owns seven parking/remedy capabilities, `plat` owns seven shared platform/data/control capabilities, and `adpt` owns two configuration/adoption capabilities. Every brick has exactly one primary owner.
- Customer and stream responsibilities are explicit. Team descriptions and customer-dependency records reuse customer-outcome KPI names. Shared needs are expressed through specific team collaboration and service relationships.
- Supplier capabilities support human authority staff. Legal decision powers, resident remedies and processing-controller responsibilities remain with the appropriate authority. No operational AI agents are modeled.

### Ownership findings

No orphaned or multiply owned bricks were found. All 25 asset owners match the primary owning teams of their producer bricks. Cross-team cooperation for shared remedies is explicit: `prkt` owns `appe`, while `fldt` and authority reviewers supply the relevant non-parking procedure context.

### Topology and staffing findings

**P2 — compact platform capacity is a binding assumption.** Evidence: `teams/teams.json`, `plat` (6 FTE), `fldt` (8 FTE), `prkt` (7 FTE), `adpt` (4 FTE); `_domain/DOMAIN.md`. This allocation is plausible only for shared infrastructure, sequenced configurations and contracted specialist support. It does not establish a standalone 24/7 rota, multiple simultaneous bespoke implementations or separate service ownership per brick. Before promising coverage, validate actual staffing, supplier contracts, incident load and rollout concurrency. Split ownership only if measured operating load warrants it.

**P2 — specialist assurance and public operational capacity are external.** Evidence: `plat` staffing description, `adpt` acceptance responsibilities, `dpof` persona and deployment service notes. The model depends on authority reviewers, physical enforcement operators and contracted hosting/assurance capacity. These are explicitly outside the supplier FTE count. Validate availability and handoff responsibilities during each rollout rather than adding invented internal departments.

### Strategy alignment findings

Year-1 acceptance has explicit ownership in `adpt`, with product and platform teams retaining behavior and control ownership. Parking review accuracy belongs to `prkt`; field and public-report outcomes to `fldt`; identity, exchange, data use and service recovery to `plat`. Every persona is served by a product and a team. No strategy priority is left without an accountable capability owner.

### Edit backlog

1. Replace the scenario in `teams/teams.json` with verified staffing and contracted coverage when available.
2. Measure rollout concurrency and support effort before broadening year-3/5 commitments.
3. Review `appe` and `plat` boundaries using actual change and incident load; preserve shared ownership semantics and authority decision powers.

## Balance Audit

Updated: 2026-09-06

Integrity: **pass** after corrections. Overall: **mature public-research seed with an intentionally compact organization**; not a verified production design.

| Artifact | New domain | Ride-sharing reference | Assessment |
|---|---:|---:|---|
| Customer groups / personas | 4 / 8 | 4 / 4 | Buyers, users, partners, assurance and beneficiaries covered |
| Jobs / adoption journeys | 16 / 8 | 8 / 6 | Three steps per job; six fixed stages per journey |
| Customer / business KPI nodes | 120 / 56 | Not used as a numerical target | Branching trees; unknown baselines remain explicit |
| Bricks / streams | 24 / 9 | 20 / 10 | Four roots, eight subgroups, 36 flow steps |
| Data assets | 25 | 17 | Producer, owner, stewardship and storage links resolve |
| Products | 4 | 3 | Uses the current lean portfolio and deployment schema |
| Teams | 4 | 24 | Intentional company-scale exception to the 8+ guideline |
| Landscape entries | 10 | 11 | Modeled company, eight comparisons, one ecosystem partner |
| Sourced insights | 13 | 8 | Twenty primary source entries |
| Residuality scenarios | 5 | Not a density target | Qualitative scenarios with no assigned likelihood |

P1: none unresolved. P2: measurement, commercial terms, deployment contracts, local assurance and staffing remain clearly labeled discovery work, as detailed above. P3: unverified headquarters cities and refreshed competitor context when needed for a specific decision.

### Validation evidence

- All 13 source JSON files parse.
- `.claude/skills/scripts/validate-domain-model.py digital-supervision-and-enforcement-platform --strict-ids`: passed.
- `.codex/skills/scripts/validate-domain-model.py digital-supervision-and-enforcement-platform --strict-ids`: passed.
- `.claude/skills/scripts/check-kpi-pyramids.py digital-supervision-and-enforcement-platform`: passed; no one-child branches, duplicate KPI definitions or unresolved strategy metric names.
- Additional full-path audit: all customer job streams are served by their linked offers; product dependencies close; all bricks occur in streams and deployments; one primary owner and one modeled producer per data asset; source, store, derivation, relation and flow references resolve.
- All seven generators succeeded in an isolated temporary preview, producing 98 HTML pages: start 1, customers 9, products/deployment 12, bricks/streams/data 59, teams 5, competition 11, residuality 1.
- Generated JavaScript syntax: 208 distinct inline scripts and the generated shared-data script passed `node --check`.
- Static internal link and asset inspection identified a missing start icon. The source now reuses the existing repository public-space pictogram, and the start preview was regenerated. No custom company logo or new image API is involved.
- Final inspection of all 98 preview pages found no missing internal static links or assets. The optional residuality schema also passed explicitly.
- Overview and Vortex source catalogs each gained exactly one entry. Comparing each catalog after removing that entry with its pre-edit snapshot confirmed that all prior content was preserved. Both JSON files and the scoped whitespace check passed.

Generation verification uses a temporary copy of the generators with source/template links. Existing main-worktree documentation is not the verification artifact. Interactive browser behavior was not exercised. These checks establish source and generator integrity, not the operational truth of modeled company assumptions.
