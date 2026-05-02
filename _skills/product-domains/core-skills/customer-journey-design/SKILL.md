---
name: customer-journey-design
description: "Use when describing end-to-end customer journeys including discovery, evaluation, trial, engagement, trust moments, adoption barriers, and retention drivers."
---

# Customer Journey Design

## Purpose

Describe how a customer becomes aware of the offer, decides whether it is right, starts using it, gets value, and keeps returning. Journeys should connect customer behavior to product, channel, trust, and operating choices.

## Workflow

1. Separate the commercial/adoption journey from the in-product task workflow.
2. Define `Discovery` as awareness through search, referrals, sales outreach, app stores, partner ecosystems, procurement shortlists, internal enablement, or brand touchpoints.
3. Define `Evaluation` as the decision process before trial or commitment: alternatives, fit, value, trust, cost, effort, and risk.
4. Continue through trial, onboarding, active use, support/recovery, renewal, retention, or expansion.
5. Identify trust moments, drop-off risks, adoption barriers, and repeat-use drivers.

## Quality Bar

- Every journey stage has a clear customer question and product/business response.
- Discovery and evaluation do not describe in-product browsing, searching, or task execution.
- Trust, compliance, payments, support, or operational recovery are included when material.
- Journey stages inform delivery channels, product capabilities, and KPIs.

## Repository Fit

- Target file: `_config/product-domains/<domain>/customers/customers.json`.
- Reuse journey language in delivery, value propositions, objectives, and release planning.
- Keep journey data concise enough to render well in generated static docs.

## Avoid

- Making the journey a marketing funnel only.
- Skipping post-purchase or repeat-use stages.
- Using the same journey for every segment when buying logic and risk differ.
