# Engineering Information and Asset Lifecycle Platform Review

## Product Domain Review

Updated: 2026-09-06

### Executive assessment

- The domain connects industrial project delivery to enduring operating-asset information. Eight roles across four groups separate economic sponsorship, technical approval, document operations, external supply, maintenance, assurance and digital adoption.
- Each role has two jobs, a six-stage adoption journey, two four-level KPI pyramids and distinct 1/3/5-year sequencing. Numeric baselines are deliberately unmeasured; proposed pilot targets are labelled.
- Twelve insights distinguish public facts from implications. Links cover products, implementation, trust, case studies and investment context. The nine-player landscape contains Assai and eight alternatives; current Autodesk and Octave names are preserved.
- Product offers follow current public boundaries. Implementation services are a service offer; neither supplier transaction fees nor an additional named software SKU are invented.

### High-priority findings

No customer-model P1 findings remain. Job steps describe work; journeys describe adopting Assai, including discovery, evaluation and bounded trial. Supplier and receiving-operations roles both connect to products, streams and accountable teams.

### Medium-priority findings and open assumptions

- **P2 — Empirical calibration.** Evidence: `customers/customers.json`, all persona KPI trees and `productStrategy` objects. The trees are plausible diagnostic proposals, not observed relationships or baselines. Why it matters: target feasibility and financial attribution cannot be assessed from public product pages. Direction: collect timed retrieval, review, acceptance and rollout samples, then revise targets with customer owners. Role-based business cohorts overlap; their revenue views must not be added together.
- **P2 — Commercial and deployment discovery.** Evidence: `_domain/DOMAIN.md`, `product-deployments/products.json` (`adms`, `avpt`, `aent`, `aser`). Pricing units, contractual service levels and exact packaging remain unestablished. Direction: validate license scope, separate module requirements and implementation responsibilities against customer contracts.
- **P3 — Competitor corporate details.** Evidence: `business/competition.json`, `octv` and `cogn`. Product evidence supports inclusion, but headquarters detail is incomplete. Direction: verify current corporate entities before reusing the landscape for corporate diligence; no head-office address is used as evidence of data residency.

### Targeted improvement backlog

Use `edit-customers` for measured baselines and richer interview evidence once supplied. Use `edit-products` for confirmed contract scope. Use `edit-competition` for comparable product-specific statistics only when sources establish their period and scope. None of these open assumptions prevents this source model from being a coherent research-based domain.

## Product Bricks Review

Updated: 2026-09-06

### Architecture assessment

- Twenty-four bricks span three root groups and eight subgroups. Module responsibilities include browser experiences, APIs, workers, stateless assembly, durable domain records and external adapters.
- Seven outcome streams include explicit decisions, exception handling and accountable completion. Controlled document approval, derived asset context and verified change closure have distinct ownership.
- Twenty-three logical data assets use five proposed stores. Every asset has an owning team, steward, producing module and consuming module; external source authority and derived search state remain distinct.
- Public source links support capability context. Internal APIs, schemas, store technologies and deployment topology remain proposed, with no fabricated repository or production-infrastructure evidence.

### Critical and traceability findings

- **P1 — Optional native capabilities in standalone offers.** Evidence: `product-bricks/product-bricks.json`, `atag → dreg`, `visu → blob`, `chco → ceng`, and `adpt → migr`; deployment offers `avpt` and `aent`. Why it matters: Viewport is positioned around existing systems; unconditional native-DMS dependencies or compulsory migration would contradict this boundary. Direction: mark native-source/migration composition as conditional and check all remaining required dependency closures per product. Resolved: all four dependencies are explicitly optional where native DMS content or migration is in scope. Every required dependency resolves within each product’s deployment composition.
- **P2 — Implementation contracts remain unverified.** Evidence: `conn`, `sync`, `iden`, `arch`, `rely`. Customer-specific allowed writes, source revocation timing, source freshness, recovery and export reconstruction need acceptance tests against real systems. Direction: retain named external authorities and refine contracts during implementation discovery. These controls are proposed, not confirmed Assai behavior.

### Edit backlog

Completed the conditional migration reference, product dependency closure, all data/module/team links and generated navigation checks. Preserve the existing separation of approval, exchange and verification. Defer API or provider specificity until reliable implementation evidence exists.

## Teams Review

Updated: 2026-09-06

### Operating-model assessment

- Eight proposed teams own all 24 bricks once each. Shared-platform consumption is represented through explicit team dependencies; supporting teams do not duplicate primary ownership.
- The model allocates 73 people across teams plus six group-level leaders. These are differentiated planning allocations, not Assai headcount or a complete company organization.
- Four customer-facing delivery teams, one specialist asset-context team and platform responsibilities cover review, supplier exchange, handover, change, integration, access, reliability, custody and enablement. Team topology follows the work rather than separate frontend/backend departments.
- Engineering approval, operating authorization, assurance acceptance and source-system authority remain customer responsibilities. AI-assisted relationships are product proposals subject to stewardship, not autonomous organizational decision-makers.

### Ownership, topology and staffing findings

- The final integrity pass confirms no orphan or duplicate primary brick ownership. The `assr` team owns audit and export software and does not claim to provide statutory engineering assurance.
- **P2 — Capacity and specialist concentration.** Evidence: `teams/teams.json`, `plat`, `cntx`, `enab`. A nine-person platform team includes three reliability specialists; asset context requires specialized search and visualization skills; implementation consultants share responsibility with product engineers. Why it matters: parallel enterprise rollouts and incident coverage could exceed these allocations. Direction: validate workload and rotation assumptions before using this model for hiring. Domain teams participate in incident response.
- **P2 — Organizational scope.** Evidence: `orgDesign.companyProfile`. Corporate selling, finance, people operations and other company functions are outside the product/delivery model. Direction: add those functions only if a whole-company operating model is requested.

### Strategy alignment and edit backlog

Every team names customer outcome metrics and supported streams. Preserve the connection between source freshness and operating trust (`cntx`, `data`, `plat`), between accepted changes and receiving-system evidence (`life`), and between go-live and customer independence (`enab`). Validate staffing against actual demand and confirmed service obligations rather than expanding team count to match the brick taxonomy.

## Balance Audit

Updated: 2026-09-06

| Dimension | Model | Mature target |
|---|---:|---:|
| Customer groups / personas | 4 / 8 | About 4 groups |
| Jobs / adoption journeys | 16 / 8 | Substantive coverage per persona |
| Four-level KPI pyramids / metric nodes | 16 / 240 | Both outcome types, branching trees |
| Product bricks | 24 | 20+ across three levels |
| Streams / flow steps | 7 / 28 | Outcome-based, traceable flows |
| Logical data assets / stores | 23 / 5 | 15+ assets |
| Teams | 8 | 8+ |
| Software offers / service offers | 3 / 1 | Match public product boundary |
| Competitors, excluding Assai | 8 | 8+ |
| Sourced insights / source pages | 12 / 12 | 8+ insights |
| Candidate stress tests | 5 | Optional, no claimed incidents |

Integrity: both `.claude` and `.codex` domain validators pass with `--strict-ids` (13 JSON files, 24 bricks). The KPI checker confirms 16 branching pyramids, unique metric IDs and matching strategy names. An additional integrity pass confirms sole primary brick and data ownership, all steward/store/module references, complete customer/job/stream/product/team coverage, required product dependency closure and source/statistic provenance.

P1: none remaining; the optional native-source/migration composition finding is resolved. P2: empirical, contract and staffing calibration remain explicit research gaps. P3: custom illustrations and complete competitor corporate details are optional polish.

Overall: mature research-based source model with integrity and scoped generation verification completed. It is suitable for strategy and architecture discussion, not a verified reconstruction of Assai internals.

### Generated-output verification

- Ran all seven generators through `run-one.sh engineering-information-and-asset-lifecycle-platform`: 97 domain HTML pages, including all five residuality scenarios and their target references.
- Regenerated only the overview and Vortex launcher packages. Before rendering, verified their existing modified HTML exactly matched the current templates and prior source JSON. All previous launcher entries and configuration values are preserved.
- Checked all 97 domain pages: no missing static local references or unresolved generator placeholders. Both new launcher destinations and icons resolve.
- Compiled all 401 inline JavaScript blocks across the 97 domain pages and two launchers with Node: no syntax errors. The launchers retain 12 pre-existing shared-template navigation URLs in their disabled global navigation; these are outside this domain change.
- `git diff --check` passes for the scoped changes. Headless Chrome could not start in this environment (exit -6), so browser execution and visual inspection were not completed.

### Applied skills

Used `.claude/skills/new-product-domain`, `set-domain-strategy`, the customer/bricks/streams/data/products/teams/competition edit skills, `validate-domain` and `audit-domain-balance`. Applied `.codex/skills/gpa-product-domain-review`, `gpa-product-bricks-review` and `gpa-teams-review` to this combined review. Current canonical schema and generator behavior resolve older prompt references to retired product/ownership fields and the old `bus` layer.
