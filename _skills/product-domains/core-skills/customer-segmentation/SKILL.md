---
name: customer-segmentation
description: "Use when identifying customer groups, personas, buyers, users, operators, beneficiaries, and materially different segments for customers/customers.json."
---

# Customer Segmentation

## Purpose

Separate the domain's customers into groups with different goals, constraints, value logic, usage context, and buying or adoption behavior. Segmentation should drive distinct JTBD, KPIs, journeys, strategy horizons, and product capabilities.

## Workflow

1. List all parties in the value exchange: buyers, users, administrators, operators, partners, beneficiaries, and regulators.
2. Group them by materially different job context, risk, economics, decision process, and success criteria.
3. Name each segment in domain language, such as "Fleet Operations Manager" or "Enterprise Data Platform Owner".
4. For each segment, capture pains, needs, constraints, desired outcomes, and measurable KPIs.
5. Validate that each segment changes product strategy or capability priorities. Merge segments that do not.

## Quality Bar

- Segments are mutually understandable and not just demographic labels.
- Each segment has a clear reason to exist in the model.
- Buyer/user/operator differences are explicit when they affect value or delivery.
- Segment IDs are lowercase and stable.
- Segments are deep enough to support jobs, journeys, KPI pyramids, and product strategy horizons.

## Repository Fit

- Target file: `_config/product-domains/<domain>/customers/customers.json`.
- Align customer IDs used in teams, objectives, delivery, and product deployments.
- Preserve repository language around customer groups, personas, jobs to be done, KPIs, and product strategy.

## Avoid

- Creating one generic "user" segment for multi-sided domains.
- Segmenting by internal department when the customer need is actually the same.
- Inventing personas that do not affect product decisions.
