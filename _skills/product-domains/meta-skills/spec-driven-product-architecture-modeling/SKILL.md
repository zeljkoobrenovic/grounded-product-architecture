---
name: spec-driven-product-architecture-modeling
description: "Use when aligning customer needs, strategy, goals, delivery, product capabilities, product bricks, teams, and planning artifacts into one implementation-aware Spec-Driven Product Architecture model."
---

# Spec-Driven Product Architecture Modeling

## Purpose

Maintain coherence across the full Spec-Driven Product Architecture model. This meta-skill is for creating, reviewing, or repairing a domain so customer value, strategy, delivery, implementation bricks, teams, and planning artifacts remain connected.

## Required Skill Stack

- `core-skills/product-domain-framing`
- `core-skills/customer-segmentation`
- `core-skills/jobs-to-be-done-modeling`
- `core-skills/kpi-architecture`
- `core-skills/product-strategy`
- `core-skills/capability-mapping`
- `core-skills/product-brick-architecture`
- `core-skills/delivery-model-design`
- `core-skills/organizational-design`
- `core-skills/teams-org-design`
- `core-skills/roadmap-design`
- `core-skills/evidence-based-modeling`
- `core-skills/structured-json-authoring`

## Workflow

1. Start with customer value and desired outcomes.
2. Connect KPIs and strategic horizons to jobs and journeys.
3. Define delivery structure through channels, APIs, events, workflows, releases, and operations.
4. Map product capabilities to implementation-facing product bricks.
5. Assign product bricks to teams and define coordination points.
6. Tie objectives, roadmap, releases, discoveries, targets, and evidence back to customers and bricks.
7. Validate references and check the generated documentation story.

## Validation

Use the scoped domain validator after cross-artifact edits:

```bash
python3 _skills/product-domains/scripts/validate-domain-model.py <domain-id>
```

The validator checks JSON parsing, product-brick ownership, duplicate brick IDs, team dependencies, and team staffing consistency. Use `--all` only for deliberate full-repo audits.

## Coherence Checks

- Every major customer job has supporting capabilities or delivery flows.
- Every strategic theme has measurable KPIs and related objectives.
- Every important capability maps to product bricks.
- Every product brick has an owning team.
- Roadmap and release items reference customers, KPIs, teams, or bricks where supported.
- Evidence and assumptions are clear enough for future maintainers.

## Repository Fit

- Source-of-truth files live under `_config/product-domains/<domain-id>/`.
- Templates live under `_templates/**`.
- Generators live under `_wiring/**`.
- Generated output lives under `docs/**` and should normally be regenerated, not hand-edited.

## Avoid

- Optimizing one artifact while breaking cross-file traceability.
- Allowing customers, capabilities, bricks, teams, and objectives to diverge semantically.
- Adding process or architecture detail that does not serve the domain model.
