---
name: architecture-skills
description: "Use when a task needs product domain framing, capability mapping, product-brick architecture, systems architecture, API/event reasoning, and traceability from customer outcomes to implementation."
---

# Architecture Skills

## Purpose

Apply the architecture cluster when the user asks to model the implementation-aware product architecture of a domain: capabilities, product bricks, systems, APIs, events, data, and dependencies.

## Core Skills To Combine

- `core-skills/product-domain-framing`
- `core-skills/capability-mapping`
- `core-skills/product-brick-architecture`
- `core-skills/solution-and-systems-architecture`
- `core-skills/schema-and-repository-pattern-recognition`
- `core-skills/structured-json-authoring`

## Workflow

1. Confirm the domain boundary and root product areas.
2. Translate customer jobs and business flows into product capabilities.
3. Decompose capabilities into a three-level product-brick structure.
4. Add interfaces, dependencies, external systems, data dependencies, and operational concerns.
5. Trace customer outcome -> capability -> product brick -> owning team where practical.
6. Validate references and run the relevant product-brick generators when requested.

## Quality Bar

- Product bricks are buildable and ownable.
- Capabilities express outcomes rather than implementation components.
- APIs, events, integrations, and data assets are plausible and tied to product value.
- Architecture remains high enough for product modeling and avoids speculative low-level design.

## Repository Fit

- Primary targets: `product-bricks/product-bricks.json`, `product-bricks/product-capability.json`, `data/data-assets.json`, delivery files, and teams.
- Use lowercase IDs and stable references throughout.

## Avoid

- Flat architecture lists with no hierarchy.
- Product-brick names that are really roadmap tasks.
- Systems diagrams disconnected from customer outcomes and product strategy.
