# corporate-learning-and-skills-platform Review

## Product Domain Review

Updated: 2026-09-06

### Executive assessment

- A mature reference model for employer learning and skills development, with four customer groups and eight materially distinct personas. Employers buy, learners and managers create outcomes, L&D operates, authors and providers supply learning, and IT approves integration and processing.
- Sixteen jobs have operational steps; eight journeys use the six fixed product-adoption stages. Every customer has a product, an accountable team, both KPI pyramids and distinct 1/3/5-year horizons.
- Fourteen insights connect sixteen primary sources to customer jobs and KPI IDs. Product descriptions support the domain boundary; proposed strategy, architecture, staffing and operating policies are explicitly labeled as hypotheses.
- The competition model separates full learning platforms, HR suites, content substitutes and provider-oriented platforms. Published statistics retain their original scope.
- Readiness: suitable for product/domain review and demonstration. It is not a verified operating model of Studytube or an approved investment case.

### High-priority findings

No open P1 realism or traceability defects were found in the completed reference model.

### Medium-priority findings

**P2 — Measurement and economics require employer evidence.** Evidence: `customers/customers.json`, especially `ldld` and `exec`; `_domain/DOMAIN.md`, Measurement and economics. Baselines are deliberately unmeasured, and commercial contribution pyramids are proposed views of shared account economics. Why it matters: renewal value, skill closure and learning transfer cannot be inferred from product marketing. Suggested direction: validate the cohort, assessment rubric, denominator, collection method and commercial attribution with one employer pilot before setting targets. This is an explicit research boundary, not missing source-model wiring.

**P2 — Qualification and processing rules require a specific customer context.** Evidence: `ldad/vqua`, `itad/assr`, and `data/data-assets.json` assets `qrec`, `asmt`, `prvc`. Why it matters: employer role policies, accepted evidence, access rights and contract terms materially change the implementation. Suggested direction: obtain policy-owner and IT approval for the pilot's actual rules, retention and processor scope before deployment. The model avoids claiming universal legal compliance.

### Targeted improvement backlog

- Use `edit-customers` to refine the hypotheses from interviews with a sponsor, administrator, learner, manager and provider. Replace proposed KPI definitions only when actual measurement is available; preserve name/ID joins.
- Use `edit-competition` to fill two minor location-provenance gaps: `thsl` headquarters is unverified; `mood` location context is historical and direct product-page retrieval failed. Product-category evidence exists, so neither gap changes the modeled boundary.
- Compare the prototype buying journey with commercial discovery: which offers are contracted separately, when DOI is enabled, and which invoice arrangements apply. Do not turn inferred offer boundaries into claimed Studytube SKUs.

### Open assumptions

Market positioning is inferred from public capabilities. Pricing, margin, revenue mix, customer renewal, learned-skill gains and staffing are not established by the sources. The a.s.r. case is company-authored and is not generalized into a performance target. Business KPI trees have three levels; customer trees have four. This is intentional to avoid fictional commercial allocation and duplicate diagnostic branches.

## Product Bricks Review

Updated: 2026-09-06

### Architecture assessment

- Twenty-seven buildable bricks sit beneath four roots and named subgroups. Their 113 modules use the six supported layers and supported module types.
- Eight outcome streams contain 39 flow steps with explicit brick dependencies and recovery considerations. All bricks appear in streams, deployment and primary team ownership.
- Twenty-six logical data assets identify their owning brick, owner/steward teams, consumers, derivation, interface, store and proposed governance. Seven logical stores do not assert an actual vendor stack.
- External systems remain outside the academy boundary: HR is authoritative for employment, identity providers for authentication, finance for accounting, providers for training delivery, and approved model providers for assisted generation.
- Critical dependencies distinguish publication-time provenance, optional AI assistance, asynchronous reminders, accepted workforce projections and derived analytics. Ordinary learning does not synchronously depend on authoring or outcome reporting.

### Critical findings

No open P1 architecture or reference-integrity defects were found. Every data asset has exactly one owning brick, whose primary team agrees with the asset owner. Every module dependency, stream composition, product deployment and asset reference resolves.

### Model-quality findings

**P2 — Runtime and integration guarantees remain reference-design choices.** Evidence: `product-deployments/deployment.json`; `product-bricks/product-bricks.json` bricks `apix`, `hris`, `oper`. Why it matters: deployment zones and retry semantics are logical design boundaries rather than evidence of current Studytube infrastructure. Suggested direction: map the design to actual integration contracts, service objectives and recovery exercises when implementation evidence is available. Preserve the current separation between proposed design and observed product capability.

**P2 — Assessment quality needs a domain-specific evaluation set.** Evidence: `skas`, `aigr`, `cont` and the `skcl`/`know` streams. Why it matters: structurally correct review workflows do not establish calibrated assessments or trustworthy generated learning. Suggested direction: build reviewed examples for the pilot role family and include ambiguous assessments, incorrect generated questions and content-withdrawal exercises before increasing automation.

### Traceability findings

The audited spine is `customer → job step → stream → brick → deployment.usedInProducts → product`, with `team.brickDependencies` providing exactly one primary owner. The current deployment schema is used; retired `neededBricks` and environment blocks are not reintroduced. Asset consumers agree with brick data dependencies. Public product context is attached directly to bricks and streams; private implementation evidence is intentionally absent.

Six candidate residuality scenarios link to existing visions, products, streams, bricks, teams and competitors. They are proposed stress exercises, with no alleged incidents, likelihood scores or invented survival results.

### Edit backlog

- Verify external offer freshness, confirmation timeouts, cancellation transitions and the contracted invoice route for `catl`, `book`, `invc` and `buyt`.
- Exercise the `hrev` scenario with duplicate workers, moved reporting lines and missing historical evidence. Check that rejected input cannot corrupt accepted learning records.
- Exercise `aifl` and `tout` with named decision owners. Candidate controls become operationally credible only after accepted tests and evidence.

## Teams Review

Updated: 2026-09-06

### Operating-model assessment

- Nine teams in three groups provide complete ownership of 27 bricks: five stream-aligned teams, three platform teams and one enabling implementation/support team.
- The illustrative size is 81 team FTE plus six group-leadership FTE. This is a proposed staffing model, not Studytube's org chart or reported headcount.
- Team missions name customer outcomes and exact KPI names from the customer model. Each team has real customer and stream references.
- Training Procurement and Supplier Operations is intentionally the largest team because bookings and financial exceptions require supplier and finance expertise alongside engineering.
- AI is a governed product capability. No autonomous agents are inserted into the organization as decision-making employees.

### Ownership findings

No orphan or multiply owned bricks were found. Skill requirements and assessments belong to `skil`; learner delivery to `lear`; qualifications/events to `lops`; content/AI quality to `knld`; procurement and reconciliation to `proc`; outcomes/reporting to `dval`; identity/integration to `intg`; common assurance/reliability to `trst`; rollout/support tooling to `csuc`.

Data ownership matches these boundaries. Team-to-team dependencies describe collaboration, platform consumption or facilitation rather than declaring shared primary brick ownership.

### Topology and staffing findings

**P2 — Capacity assumptions need workload and coverage evidence.** Evidence: `teams/teams.json`, `proc` (11 FTE), `trst` (9 FTE), `csuc` (8 FTE). Why it matters: provider exceptions, service coverage and concurrent implementations may dominate staffing. Suggested direction: size against actual ticket volume, integration count, rollout load and required support hours. Keep the current end-to-end ownership until evidence justifies splitting it.

### Strategy alignment findings

The skills strategy has `skil` and `dval` accountability; dependable qualification operations have `lops`; reviewed knowledge has `knld`; supplier commitment closure has `proc`; trustworthy adoption has `intg`, `trst` and `csuc`. Employer policy and budget owners remain represented as customers, separate from platform delivery teams.

### Edit backlog

Validate the proposed charters with actual product and service leads. Establish named employer contacts for qualification policy, invoice disputes and incident decisions. Corporate sales, HR, finance and legal functions are outside this software/service reference model; their exclusion must not be interpreted as evidence that the company lacks them.

## Domain Balance Audit

Updated: 2026-09-06

Integrity: passed both domain validators with strict IDs, the KPI checker, and the extended ownership/deployment/asset/source/relationship audit.

| Artifact | New domain | Ride-sharing reference | Assessment |
| --- | ---: | ---: | --- |
| Personas | 8 | 4 | Distinct buyer, user, operator and supplier contexts |
| Product bricks | 27 | 20 | Three levels; every brick has an implementation and owner |
| Streams | 8 | 10 | 39 meaningful flow steps |
| Data assets | 26 | 17 | Governed and connected to modules |
| Teams | 9 | 24 | Deliberately more compact operating scope |
| Competitors | 8 plus Studytube | 11 players | Direct, regional, adjacent and substitute coverage |
| Sourced insights | 14 | 8 | Sixteen primary sources |

Additional coverage: seven products; two deployment channel groups with eight subchannels; twelve customer relationships; sixteen jobs; eight adoption journeys; 176 KPI nodes; six stress scenarios.

P1: none open. P2: empirical validation of operating, commercial, assessment and staffing assumptions, as itemized above. P3: optional bespoke illustrations and competitor logos are omitted; the domain start page reuses the repository's coaching icon. Headquarters/provenance gaps are explicitly labeled.

Overall: **mature reference model**, with observed public facts separated from proposed strategy and implementation.

## Verification

- Source: thirteen JSON files; both `.claude` and `.codex` domain validators pass with `--strict-ids`.
- KPI coherence: all trees fan out, IDs are unique within personas, and all strategy metric names resolve.
- Extended integrity: no missing customer/product/stream/brick/team/asset/source links; no ownership conflicts; all stress impacts resolve.
- Scoped documentation generation: all seven generators completed successfully via `run-one.sh corporate-learning-and-skills-platform`; 109 HTML pages were generated without regenerating other domains.
- Static navigation: every local `href` and `src` in those 109 pages resolves to an existing target.
- Browser smoke test: the seven main pages returned HTTP 200, displayed populated content, and had no JavaScript page errors or broken visible images in Chromium. Start, customer and product-brick screenshots were visually inspected.
- Optional imagery: the existing renderer requests per-entity icons before falling back to generic repository icons, so missing bespoke icons produce fallback image 404s. Generic icons render successfully; no shared template was changed to suppress this behavior.
