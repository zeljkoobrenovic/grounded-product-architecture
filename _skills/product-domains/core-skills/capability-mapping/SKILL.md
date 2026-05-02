---
name: capability-mapping
description: "Use when defining product capabilities required for customer jobs and business flows, and tracing capabilities to customer outcomes, bricks, systems, and strategy."
---

# Capability Mapping

## Purpose

Map what the product must be able to do to satisfy customer jobs and business outcomes. Capabilities are outcome-oriented and durable; product bricks are implementation-facing.

## Workflow

1. Start from customer jobs, journey stages, value propositions, and business flows.
2. Define capabilities as strategic "what", not implementation "how".
3. Link each capability to one or more product bricks or external systems.
4. Explain why the capability matters for customer outcomes and business KPIs.
5. Check coverage across acquisition, activation, core use, trust, operations, monetization, support, and retention.

## Quality Bar

- Capability names are durable and outcome-oriented.
- The map avoids one capability per feature.
- Capabilities bridge customer value and implementation reality.
- Required external systems are named when material.
- Capabilities are granular enough to guide product-brick and roadmap decisions.

## Repository Fit

- Target file: `_config/product-domains/<domain>/product-bricks/product-capability.json`.
- Link capabilities to product bricks using stable lowercase IDs.
- Keep capability descriptions useful in generated product-brick documentation.

## Avoid

- Defining capabilities as internal services only.
- Duplicating product bricks under different labels.
- Omitting operational, trust, compliance, data, or support capabilities when the domain depends on them.
