# Corporate Learning and Skills Development

Updated: 2026-09-06
Reference company: Studytube
Model status: research-grounded reference design; not a representation of Studytube's private architecture, organization, financial performance or committed roadmap.

## Scope and value exchange

The domain covers employer-funded workforce learning: establish role expectations, identify development needs, deliver and procure learning, maintain qualification evidence, and reassess whether people can apply what they learned. Employers are buyers; employees and managers create the outcomes; L&D administrators operate academies; internal experts and training providers supply knowledge; IT owners maintain access and integration.

Core scope includes an LMS, learner experience, skills mapping and assessment, AI-assisted authoring with human publication decisions, e-learning subscriptions, external training procurement, internal events, reporting, integration and implementation support. These are connected offers within one domain, not assumptions about separately priced Studytube SKUs.

Adjacent scope includes HR master data, identity providers, finance systems, external content delivery, instructor calendars and employer business-outcome datasets. Those remain external systems of record. Excluded scope includes payroll, recruiting, performance-based employment decisions, formal degree accreditation, clinical fitness decisions, payment acquiring, and operating the training providers' businesses.

The choice of domain reflects the current [Studytube product portfolio](https://www.studytube.com/). [Vortex's investment page](https://vortexcp.com/investment/studytube/) supplies historical context: it describes an investment with henQ in November 2016 and a corporate learning offer combining courses, an LMS and authoring. This historical description is not treated as the limit of today's product.

## Proposed strategy

Vision: make useful, demonstrable workforce development repeatable while keeping learning administration and training spend accountable.

The proposed competitive thesis combines an employer's own knowledge, external training supply and role-specific development in one operating process. It requires relevance and reliable evidence as well as ease of use; a large content catalog alone does not demonstrate impact.

- Year 1: establish accurate learner membership, accessible academy use, qualification rules, trusted completion evidence and approved training purchases. Pilot with bounded departments and establish KPI baselines.
- Year 3: connect reviewed role/skill maps to learning plans, calibrated assessments, versioned content and reconciled external training. Expand only after integration and support performance hold.
- Year 5: compare development interventions using longitudinal skill and work-application evidence, extending across employer entities with clear data boundaries. Human owners remain accountable for assessment interpretation and spending.

These horizons start from adoption of this reference design, not Studytube release dates. Tradeoffs: standard integration patterns before bespoke deployments; reviewed skill definitions before AI-generated scale; qualification evidence before automation of high-consequence decisions; relevant content before catalog volume.

## Measurement and economics

Proposed domain north star: verified skill-gap closure rate, measured for an explicitly defined cohort against a versioned role requirement and an agreed assessment rubric. Supporting outcomes include time to role readiness, valid qualification coverage, work-application confirmation and training purchase reconciliation. Course completion is evidence of participation and is never automatically equated with competence.

All KPI baselines are unmeasured. No numeric target is presented as an observed Studytube result. Customer KPI pyramids have four levels; focused commercial contribution pyramids use three levels to avoid allocating fictional revenue independently to every persona. Shared renewal metrics are alternative diagnostic views of the same vendor economics and must not be summed. Prices, contract values, take rates, marketplace gross/net accounting and revenue mix require commercial validation. Software subscription, content subscription and implementation services are modeled revenue hypotheses; supplier invoicing is modeled only where contracted.

## Modeling assumptions and boundaries

- Personas, jobs, journeys, priorities, bricks, modules, dependencies, stores, teams and headcount are authored design hypotheses informed by public product descriptions.
- Proposed runtime zones are logical responsibility boundaries, not claims about cloud vendors, regions, accounts, microservices or database technology used by Studytube.
- The employer owns role requirements and qualification policy. Human reviewers approve content, assess contested evidence and decide exemptions; the model does not claim automated legal compliance.
- Governance text is a proposed operating policy. Residency, retention, processor terms, subprocessor coverage and certificate applicability must be confirmed against the relevant contract.
- Role and skill data may affect employees. Minimize access, allow correction, preserve assessment provenance and exclude automatic promotion, dismissal or suitability judgments.
- Synthetic residuality scenarios are forward-looking design exercises. They do not allege that Studytube suffered any modeled incident.
- Optional images and implementation-evidence inventories are omitted. Public research links are attached directly to bricks and streams; no private source repositories or infrastructure evidence is invented.

## Sources and provenance

Current product facts and their implications are recorded with canonical URLs and access dates in [customers/insights.json](../customers/insights.json), with further reading in [customers/links.json](../customers/links.json). Undated webpages use an access date without inventing a publication date. Competitor descriptions are category comparisons, not market-share rankings.

## Structure and quality workflow

Structural references: `ride-sharing-marketplace` for customers, bricks, streams, data and competition; `maas` for the current product/deployment/team schema; `occupational-health-and-safety-platform` for workforce and qualification boundaries; `enterprise-integration-and-data-management-platform` for integration/service ownership.

Authoring follows `.claude/skills/new-product-domain` and its per-artifact skills. Strategy, architecture and operating-model reviews follow the three `.codex/skills/gpa-*-review` skills and are saved in the domain-root `REVIEW.md`. The live deployment schema records brick-to-product composition in `deployedBricks[].usedInProducts`; retired `neededBricks` fields in older guidance are not added.
