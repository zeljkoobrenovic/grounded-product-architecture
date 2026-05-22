# Skills For Defining Product Domains

This directory contains the repo-local skill set used to create and refine Spec-Driven Product Architecture domain models. The skills are stored outside `_config/product-domains/` because they guide work across source data, generators, templates, and generated documentation.

The skills are organized into three groups:

- `core-skills/` - individual modeling skills used for focused tasks
- `skill-clusters/` - combined skill sets for common multi-step workflows
- `meta-skills/` - end-to-end workflows that combine research, strategy, architecture, delivery, planning, and source authoring

These skills are aligned with `NEW-DOMAIN-PROMPT.md` and the repository model described in `_config/product-domains/AGENTS.md`: source JSON first, implementation-aware product architecture, lowercase stable IDs, evidence-backed assumptions, and generated static documentation.

## Operating Principles

- Start from existing domain examples and generator expectations before inventing structure.
- Treat `_config/product-domains/**` as the source of truth.
- Treat `docs/product-domains/**` as generated output.
- Keep strategy grounded in customers, JTBD, KPIs, delivery, product capabilities, product bricks, teams, and evidence.
- Preserve the repository's domain language: customers, product strategy, delivery, objectives, product bricks, product deployments, teams, evidence, documents, and roadmap.
- Use lowercase stable IDs in JSON.
- Separate sourced facts, assumptions, and inferences.
- Do not invent business metrics or source-backed claims.

## Validation Tools

Use the bundled scripts for deterministic checks while maintaining this skill library and while editing product domains:

- `python3 _skills/product-domains/scripts/validate-skills.py`
  - Validates skill frontmatter, naming, descriptions, overview links, and stale prompt references.
- `python3 _skills/product-domains/scripts/validate-domain-model.py <domain-id>`
  - Validates JSON parsing, product-brick ownership, team dependencies, team headcount/role counts, and duplicate product-brick IDs for a scoped domain.
- `python3 _skills/product-domains/scripts/validate-domain-model.py --all`
  - Runs the same domain checks across all domains. Use deliberately because older domains may expose pre-existing issues outside the current task.
- Add `--strict-ids` when you want an additional lowercase/simple-ID pass. This is intentionally opt-in because evidence and trace IDs may contain regex-like or path-like values.

## Core Skills

### Domain And Research

- [Product Domain Framing](core-skills/product-domain-framing/SKILL.md) - select, name, scope, and justify a product domain.
- [Market Research](core-skills/market-research/SKILL.md) - build an evidence-backed view of company, category, customer behavior, monetization, and operating environment.
- [Competition Analysis](core-skills/competition-analysis/SKILL.md) - create sourced `business/competition.json` landscapes with official links, metrics, scope, and comparability caveats.
- [Evidence-Based Modeling](core-skills/evidence-based-modeling/SKILL.md) - separate facts, assumptions, and inferences while keeping the model coherent.

### Customer And Strategy

- [Customer Segmentation](core-skills/customer-segmentation/SKILL.md) - identify customer groups, personas, buyers, users, operators, beneficiaries, and distinct segment logic.
- [Jobs To Be Done Modeling](core-skills/jobs-to-be-done-modeling/SKILL.md) - translate customer intent into jobs, outcomes, steps, frictions, and success criteria.
- [Customer Journey Design](core-skills/customer-journey-design/SKILL.md) - model discovery, evaluation, trial, engagement, trust moments, adoption barriers, and retention.
- [Value Proposition Design](core-skills/value-proposition-design/SKILL.md) - express why a segment chooses the product and which outcomes make the offer compelling.
- [Business Model Design](core-skills/business-model-design/SKILL.md) - explain value creation, delivery, capture, pricing, marketplace economics, and operating drivers.
- [Product Strategy](core-skills/product-strategy/SKILL.md) - define vision, differentiation, themes, and 1-year, 3-year, and 5-year horizons.

### Goals And Planning

- [KPI Architecture](core-skills/kpi-architecture/SKILL.md) - design KPI pyramids, north-star metrics, supporting metrics, diagnostic metrics, and targets.
- [Goal Setting](core-skills/goal-setting/SKILL.md) - convert strategy into objectives and measurable outcomes.
- [Strategic Planning](core-skills/strategic-planning/SKILL.md) - convert strategy into milestones, phases, assumptions, and horizon-based sequencing.
- [Roadmap Design](core-skills/roadmap-design/SKILL.md) - shape initiatives, releases, dependencies, MVPs, expansion paths, and risk-reduction sequence.

### Architecture And Delivery

- [Capability Mapping](core-skills/capability-mapping/SKILL.md) - define product capabilities and trace them to customer outcomes, bricks, systems, and strategy.
- [Product Brick Architecture](core-skills/product-brick-architecture/SKILL.md) - create three-level implementation-facing brick structures with clean boundaries and traceability.
- [Solution And Systems Architecture](core-skills/solution-and-systems-architecture/SKILL.md) - connect capabilities to systems, APIs, events, integrations, data, reliability, and operations.
- [Delivery Model Design](core-skills/delivery-model-design/SKILL.md) - describe channels, interfaces, APIs, events, workflows, MVP scope, and release structures.

### Organization And Source Authoring

- [Organizational Design](core-skills/organizational-design/SKILL.md) - define team ownership, responsibilities, leadership, coordination, and accountability.
- [Team Topology Design](core-skills/team-topology-design/SKILL.md) - structure stream-aligned, platform, enabling, and complicated-subsystem teams.
- [Schema And Repository Pattern Recognition](core-skills/schema-and-repository-pattern-recognition/SKILL.md) - infer current canonical JSON structure, naming, references, and generator expectations.
- [Structured JSON Authoring](core-skills/structured-json-authoring/SKILL.md) - produce valid, internally consistent JSON with lowercase IDs and stable references.
- [Static Documentation Modeling](core-skills/static-documentation-modeling/SKILL.md) - write source content that renders clearly in the standalone static documentation site.

## Skill Clusters

- [Organizational Design Skills](skill-clusters/organizational-design-skills/SKILL.md) - org design, topology, ownership mapping, capability-to-team alignment, and coordination design.
- [Architecture Skills](skill-clusters/architecture-skills/SKILL.md) - domain framing, capability mapping, product bricks, systems architecture, APIs/events, and traceability.
- [Product Strategy Skills](skill-clusters/product-strategy-skills/SKILL.md) - customer modeling, value proposition, business model, product strategy, and strategic planning.
- [Market Research Skills](skill-clusters/market-research-skills/SKILL.md) - market research, competition, substitutes, category dynamics, public signals, and assumptions.
- [Goal Setting Skills](skill-clusters/goal-setting-skills/SKILL.md) - KPI architecture, objectives, north-star metrics, leading/lagging metrics, and target calibration.
- [Planning Skills](skill-clusters/planning-skills/SKILL.md) - strategic planning, roadmap design, milestones, release planning, dependencies, MVP, and expansion paths.

## Meta-Skills

- [New Product Domain Definition](meta-skills/new-product-domain-definition/SKILL.md) - end-to-end creation of a complete domain under `_config/product-domains/<domain-id>/`.
- [Spec-Driven Product Architecture Modeling](meta-skills/spec-driven-product-architecture-modeling/SKILL.md) - cross-artifact modeling that keeps customer needs, strategy, delivery, capabilities, bricks, teams, and planning coherent.

## Prompt Alignment

When using these skills for `NEW-DOMAIN-PROMPT.md`, apply these additional rules:

- Choose a domain clearly relevant to the target company or business and justify that choice.
- Inspect existing domains before creating files.
- Create realistic three-level product bricks with 20+ bricks for mature new domains.
- Define `Discovery` as how customers become aware of the offer before active use.
- Define `Evaluation` as how customers decide whether the product is right after discovery and before trial.
- Do not use `Discovery` or `Evaluation` for in-product task execution.
- Include a sourced `business/competition.json` with official links and non-invented metrics.
- Ensure JSON is valid and references are internally consistent before generating docs.
