# solvari-home-improvement-marketplace Review

## Product Domain Review

Updated: 2026-09-06

### Executive assessment

- The domain has a specific value exchange: homeowners seek useful professional contact; firms buy recurring access and demand; partners supply attributable requests; operators protect quality and recovery.
- Four customer groups contain five personas, ten substantive jobs, five fixed-stage adoption journeys, and ten four-level KPI pyramids. All five personas have distinct 1/3/5-year strategic horizons.
- The buyer/coordinator distinction explains commercial approval versus daily follow-up without asserting that every firm employs separate people.
- Ten insights resolve to eleven official sources. The model distinguishes public capability evidence from proposed metrics, modules, stores, staffing, and future strategy.
- Eight competitors cover direct regional alternatives, different home-task transaction models, and a UK benchmark. Acquired brands are excluded from the independent rival list, and incomparable counters remain explicitly scoped.

### High-priority findings

None remain in the source model. Strict validation, KPI checks, and the additional cross-file audit pass. Each customer has a product and team path; each job step has a real stream; every brick has a deployment and exactly one primary owner.

### Medium-priority findings

1. **The most useful outcome is not presently measured.** Evidence: `customers/customers.json`, `hown/ucvr` and `hown/obsc`. A delivered or charged lead does not establish useful contact, while unknown outcomes can bias a rate. Direction: establish a dated seven-day cohort, a homeowner relevance question, and the missing-observation denominator before using this proposed north star for investment decisions. KPI trees express causal diagnostics, not arithmetic identities.
2. **Personas and operating workflows need first-party validation.** Evidence: `prby`, `prco`, and `mqop`; `customers/insights.json`, `icrm` and `iscp`. Public CRM and account-support features support the role hypothesis but do not reveal actual purchasing or workflow behavior. Direction: interview small-firm combined-role users and larger-firm coordinators, then adjust segmentation only if their decisions differ materially.
3. **Public commercial and acquisition details are not fully reconcilable.** Evidence: `_domain/RESEARCH.md`, sources `pric`, `ptrm`, `vort`, and `acqu`. A misleading universal tariff or acquisition count would weaken the model. Direction: preserve the current caveats and obtain effective agreements and a dated group perimeter before adding precision.

### Targeted improvement backlog and open assumptions

- `customers/customers.json`: replace unknown baselines with dated measurements and approved pilot goals; preserve denominator and observation coverage.
- `customers/insights.json`: add interview, case, and cohort evidence for professional value and homeowner contact tolerance.
- `business/competition.json`: refresh dynamic counters before comparison; verify Checkatrade headquarters only if geography requires that precision.
- The internal workbench, differentiated coordinator role, proposed horizons, and requested separate company-specific domain are intentional modeling choices. The existing broader Solvari-based domain remains a sibling, not an automatically synchronized source.

## Product Bricks Review

Updated: 2026-09-06

### Architecture assessment

- Twenty-five bricks sit in four root groups and nine subgroups, with 103 modules using all six supported layers. They are logical capability boundaries, not a claim of 103 deployed services.
- Ten outcome streams include explicit main-path and recovery steps. All bricks participate in at least one stream and in a deployed product.
- Fifty-seven module-scoped brick dependencies and 87 data dependencies provide concrete runtime and ownership connections without a fully connected graph.
- Twenty-eight assets in fourteen logical stores have named owner/steward teams and an explicit system-of-record brick. Sensitive case records and conversation context receive restricted access and purpose-specific retention proposals.
- Joost includes an editable confirmed handoff and evaluation records; credit and partner ledgers preserve correction lineage; integration includes rollback and opening-balance reconciliation.

### Critical findings

None remain. Ownership, store classification, module references, asset references, deployment/product joins, and source references pass the supplementary audit. A renderer defect was fixed in `_wiring/product-domains/generate-product-bricks-docs.py`: brick context now reads the current deployment mappings and follows JTBD stream composition. Stream pages filter customer steps by the actual stream, so a shared identity capability does not make every product support every flow. Legacy `neededStreams` input remains supported.

### Model-quality findings

1. **Proposed module boundaries exceed available implementation evidence.** Severity: P2. Evidence: `product-bricks/product-bricks.json`, all bricks, especially `jost`, `mtch`, and `migr`. Public pages establish capabilities but not transactions, providers, or failure semantics. Direction: review real API/event contracts and operational evidence before treating these logical boundaries as deployment or migration commitments.
2. **Commercial consistency is specified but unproven.** Severity: P2. Evidence: `camp`, `cred`, `lead`, `bill`, and `sett`, plus assets `cmps`, `crle`, and `pyst`. Reservation, replay, correction, and effective-date semantics must survive real concurrent and partial failures. Direction: validate the proposed invariants against implementation and representative contract cases; the model and documentation tests do not prove production correctness.
3. **Retention and hosting are proposed governance choices.** Severity: P2. Evidence: `data/data-assets.json`, `conv`, `priv`, `casc`, and all store technology/residency descriptions. Exact periods, actual processors, and transfer arrangements are unknown. Direction: replace proposals with approved schedules and actual provider boundaries, preserving purpose and exception context.

### Traceability findings and edit backlog

- Every brick has one owner; every asset's owning team agrees with its system-of-record brick's team; no asset or brick is orphaned.
- Products use the canonical deployment `usedInProducts` mapping. No obsolete `neededBricks`, environment list, or per-product interface catalog was added.
- Public brick/stream links are labeled capability context; no proprietary evidence IDs or implementation repositories were invented.
- Next edits should follow observed contracts and telemetry: validate the `jost` release rubric, commercial event invariants, and migration reconciliation before expanding the catalog.

## Teams Review

Updated: 2026-09-06

### Operating-model assessment

- Nine teams across three groups own the full architecture. Seventy-seven team FTE and six group-direct FTE are explicitly a proposed 83-FTE allocation.
- Team missions cover homeowner intent/choice, professional supply, demand/follow-up, economics, partner exchange, quality, trusted platform, and data/integration.
- All 25 bricks have exactly one primary owner. Every team owns meaningful capabilities and has valid customer, stream, and team dependencies.
- Joost is a governed product capability, not an organizational decision maker. Human owners retain release, eligibility, disputed-case, finance, and cutover accountability.

### Ownership findings

No missing, duplicate, or mismatched brick ownership remains. The supplementary audit verifies that all asset owner/steward references resolve and that each system-of-record brick belongs to the asset's owning team.

### Topology and staffing findings

1. **The 83-FTE allocation cannot be inferred from company-wide counters.** Severity: P2. Evidence: `teams/teams.json`, `orgDesign.companyProfile` and group staffing. The public 100+ employee counter supplies no engineering, sales, support, or country-function breakdown. Direction: calibrate this reference allocation against actual staffing and shared functions before proposing hiring or reorganization.
2. **Quality owns a demanding optimization/control boundary.** Severity: P2. Evidence: team `mqua` owns `mtch`, `qual`, `case`, and `opsc` with 10 proposed FTE. Combining matching, integrity, and case policy can overload review capacity. Direction: maintain the named independent human review rule and separate commercial override authority; split allocation engineering from quality control only when workload warrants it.
3. **Platform and integration work can compete with critical operations.** Severity: P2. Evidence: `plat` owns identity/privacy, communication, and reliability; `dint` owns measurement and migration. Direction: validate duty rotations, reserve incident capacity, and stage migrations against actual load. Team descriptions already call for distinct duty owners.

### Strategy alignment findings and edit backlog

- Year-1 briefing, useful contact, and cost explanation have named owners in `hint`, `psup`, `pgrw`, `mqua`, and `econ`.
- Year-3 workflow and partner value map to `pgrw` and `part`; year-5 integration and recovery map to `dint` and `plat` with quality gates from `mqua`.
- Legal/privacy and finance assurance are explicit supporting responsibilities but have no invented standalone department. Confirm who supplies those controls, how independence works, and how much capacity is committed.

## Balance Audit

Updated: 2026-09-06

Integrity: **pass** — all 13 JSON files parse and pass strict validation. The additional audit confirms the customer/job/stream/brick/product/deployment/team and data-ownership chains. KPI checks find no single-child nodes, duplicate per-persona KPI IDs, or unresolved strategy names.

| Artifact | Count | Mature target | Assessment |
|---|---:|---:|---|
| Customer groups / personas | 4 / 5 | About 4 groups | Distinct decision roles; buyer/coordinator can be combined in small firms |
| Jobs / adoption journeys | 10 / 5 | Complete per persona | Two jobs and one six-stage adoption journey per persona |
| KPI pyramids / nodes | 10 / 150 | Two real pyramids per persona | Four levels; unknown baselines remain explicit |
| Insights / sources | 10 / 11 | 8+ insights | Official source links and explicit implications |
| Products | 4 | Scope dependent | Three external offers and one proposed internal product |
| Bricks / modules | 25 / 103 | 20+ bricks | Four root groups, nine subgroups, all six layers |
| Outcome streams | 10 | Complete outcome coverage | Every brick used |
| Data assets / stores | 28 / 14 | 15+ assets | Complete owning and stewardship references |
| Teams | 9 | 8+ | Exactly one owner for every brick |
| Competitors | 8 | 8+ | Direct, substitute, and international benchmark scope |
| Residuality stressors | 5 | Optional | Integrated into the reference model; no probability or survival claims |

### P1 — realism or traceability breaks

None remain.

### P2 — evidence and operating-model assumptions

Validate unknown baselines, role separation, commercial agreements, actual architecture, and staffing before using this reference model for investment or organizational commitments. Relevant skills: `edit-customers`, `edit-teams`, `edit-products`, `edit-product-bricks`, and `edit-data-assets`.

### P3 — presentation and research polish

The start icon reuses the existing home-improvement domain illustration. Persona and capability views use template fallback icons; custom illustrations and private implementation evidence were not invented. The residuality renderer currently exposes JTBD-step identifiers as its journey targets; this model uses stable vision, product, stream, brick, team, and competitor impacts rather than adding incompatible slash-delimited references under strict ID validation.

Overall: **mature reference model**, with decision-relevant evidence limitations documented and all required ownership and implementation connections intact.
