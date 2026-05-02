---
name: new-product-domain-definition
description: "Use when creating a complete new product domain under _config/product-domains, combining research, customers, strategy, KPIs, delivery, product bricks, teams, planning, evidence, and JSON authoring."
---

# New Product Domain Definition

## Purpose

Create a complete, repository-consistent product domain from a company or business prompt. This meta-skill combines market research, customer modeling, strategy, KPI design, delivery, product capabilities, product bricks, teams, planning, evidence, and structured JSON authoring.

## Required Skill Stack

- `skill-clusters/market-research-skills`
- `skill-clusters/product-strategy-skills`
- `skill-clusters/architecture-skills`
- `skill-clusters/goal-setting-skills`
- `skill-clusters/planning-skills`
- `skill-clusters/organizational-design-skills`
- `core-skills/schema-and-repository-pattern-recognition`
- `core-skills/structured-json-authoring`
- `core-skills/static-documentation-modeling`

## Workflow

1. Inspect `_config/product-domains/AGENTS.md`, `_wiring/product-domains/`, `_templates/`, and several mature comparable domains.
2. Select and justify the most suitable product domain for the target company or business.
3. Build an evidence-backed view of category, competitors, customers, business model, and operating environment.
4. Create the domain source tree under `_config/product-domains/<domain-id>/` using current repository patterns.
5. Populate customers, JTBD, journeys, KPI pyramids, product strategy horizons, products/deployments, delivery, product capabilities, product bricks, objectives, releases, teams, data assets, scorecard, and competition files where applicable.
6. Keep all IDs lowercase and references stable across files.
7. Validate JSON, references, brick ownership, team dependencies, KPI quality, and generator expectations.
8. Generate docs only when requested or when the task explicitly includes static output.

## Validation

After source edits, run scoped validation before generating documentation:

```bash
python3 _skills/product-domains/scripts/validate-domain-model.py <domain-id>
```

Use `--strict-ids` only when checking simple domain object IDs. Do not use strict ID validation as a blanket rule for evidence or trace identifiers.

## Model Alignment Rules

- Discovery means pre-use awareness through channels such as search, referrals, sales outreach, app stores, partner ecosystems, procurement shortlists, internal enablement, or brand touchpoints.
- Evaluation means the pre-trial decision process: alternatives, fit, value, trust, cost, adoption effort, and risk.
- Product bricks use a three-level implementation-facing structure and should include 20 or more realistic bricks for mature new domains.
- Competition analysis uses only sourced metrics, preserves metric scope, and includes official links.
- Strategy includes 1-year, 3-year, and 5-year horizons with focus, product theme, customer KPI, business KPI, and milestones.

## Quality Bar

- The model is source-first, coherent, and implementation-aware.
- Existing schema patterns are reused rather than reinvented.
- Customers, strategy, objectives, delivery, product bricks, teams, and competition reinforce each other.
- Assumptions are explicit where public information is incomplete.
- Generated static documentation would be navigable and useful.

## Avoid

- Creating a folder skeleton with shallow filler.
- Starting from docs pages instead of source JSON.
- Inventing business metrics or product architecture details without evidence or clear inference.
- Treating product bricks, capabilities, objectives, and teams as independent lists.
