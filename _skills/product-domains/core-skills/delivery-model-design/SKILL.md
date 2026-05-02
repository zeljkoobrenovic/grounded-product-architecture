---
name: delivery-model-design
description: "Use when describing how a product is delivered through channels, interfaces, APIs, events, operational workflows, MVP scope, releases, and capability mappings."
---

# Delivery Model Design

## Purpose

Describe how the product reaches customers and operates in practice. Delivery connects strategy to channels, journeys, APIs, events, operational flows, MVP boundaries, and release structures.

## Workflow

1. Inspect current delivery schemas in comparable domains before editing.
2. Identify channels, touchpoints, APIs, events, user journeys, operational workflows, and support/recovery paths.
3. Define MVP scope and expansion path.
4. Map delivery elements to product capabilities and product bricks.
5. Connect releases and initiatives to teams and measurable outcomes where supported.

## Quality Bar

- Delivery is specific to how this domain is bought, accessed, integrated, operated, and supported.
- APIs and events have clear users and business purpose.
- Operational workflows include human-in-the-loop steps where realistic.
- MVP and expansion scope are clear enough for roadmap decisions.

## Repository Fit

- Target files include `delivery/releases.json`, `product-deployments/products.json`, and `product-deployments/deployment.json`.
- Some domains evolved from older product files to delivery files; inspect generator expectations before changing filenames.

## Avoid

- Modeling delivery as just "web and mobile".
- Creating delivery flows that cannot be traced to customer journeys or capabilities.
- Ignoring operational delivery for marketplaces, regulated domains, logistics, finance, or enterprise workflows.
