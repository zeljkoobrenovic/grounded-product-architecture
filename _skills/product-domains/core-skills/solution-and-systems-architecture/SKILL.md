---
name: solution-and-systems-architecture
description: "Use when connecting product capabilities to systems, APIs, events, integrations, data, reliability, security, and operations at a practical level."
---

# Solution And Systems Architecture

## Purpose

Ground product strategy in plausible systems and integration reality without over-specifying low-level implementation. This skill connects capabilities and bricks to APIs, events, data flows, external systems, and operational qualities.

## Workflow

1. Start from capabilities and product bricks.
2. Identify systems of record, systems of engagement, workflow services, decision engines, data platforms, and external integrations.
3. Define key APIs, event streams, data dependencies, and operational interfaces.
4. Include non-functional concerns: reliability, latency, privacy, compliance, security, observability, and cost.
5. Keep architecture at a product-domain level unless the schema asks for deeper detail.

## Quality Bar

- Architecture choices are plausible for the business and operating model.
- APIs and events have clear producers, consumers, and purposes.
- External systems are named by role or known provider category where exact vendor is not warranted.
- Reliability, data quality, and trust concerns are visible where they affect product outcomes.

## Repository Fit

- Architecture detail appears in product bricks, delivery, data assets, product deployments, and evidence references.
- Avoid introducing runtime dependencies or code frameworks; this repository is a static documentation generator.

## Avoid

- Speculative low-level designs that are not needed for product modeling.
- Ignoring integration and operational reality.
- Describing systems without linking them to capabilities, bricks, or customer outcomes.
