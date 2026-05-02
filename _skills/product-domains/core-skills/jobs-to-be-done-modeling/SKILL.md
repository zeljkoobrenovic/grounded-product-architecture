---
name: jobs-to-be-done-modeling
description: "Use when translating customer intent into jobs, desired outcomes, process steps, frictions, and success criteria for a product-domain model."
---

# Jobs To Be Done Modeling

## Purpose

Model customer progress, not feature usage. JTBD should explain what the customer is trying to accomplish, what makes the job hard, and what outcomes prove the product helped.

## Workflow

1. Start from the customer's trigger, context, constraints, and desired progress.
2. Write jobs as outcome-oriented statements, not UI tasks.
3. Break each job into meaningful steps with pains, decisions, evidence needs, and capability needs.
4. Attach success criteria and KPI leaves that can be measured.
5. Connect steps to product capabilities and product bricks where the schema supports it.

## Quality Bar

- Jobs are stable across implementation changes.
- Steps reflect real customer work, decisions, and risks.
- Frictions are specific enough to motivate capabilities.
- Desired outcomes are measurable or observable.
- Capability needs do not prematurely name internal systems unless the job requires a technical interface.

## Repository Fit

- Target file: `_config/product-domains/<domain>/customers/customers.json`.
- Use JTBD to inform product capabilities, delivery flows, objectives, and product bricks.
- Keep the model grounded in customer value before internal architecture.

## Avoid

- Writing "use feature X" as a job.
- Treating discovery or evaluation as in-product search/browse tasks.
- Creating one-step jobs that hide the operational workflow.
- Adding generic pains such as "needs efficiency" without concrete context.
