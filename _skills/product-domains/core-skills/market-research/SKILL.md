---
name: market-research
description: "Use when building an evidence-based view of a company, category, customers, competitors, substitutes, monetization, and operating environment for a product domain."
---

# Market Research

## Purpose

Build the factual and inferential base for a product-domain model. Research should explain what the business does, how the category works, who the customers are, how value is captured, and which public signals support the model.

## Workflow

1. Start with official sources: company site, investor relations, annual reports, regulatory filings, newsroom, product docs, official blogs, and engineering blogs.
2. Add authoritative ecosystem sources only when official sources do not cover category structure or competitors.
3. Separate facts, sourced metrics, inferred operating logic, and assumptions.
4. Identify customer groups, buying centers, user roles, partners, regulators, and internal operators.
5. Translate research into modeling implications for customers, product strategy, business model, delivery, product bricks, and teams.

## Quality Bar

- Each important factual claim has a source or is clearly framed as inference.
- Metrics keep their original reported scope, period, and wording.
- Competitors and substitutes are not limited to direct product clones; include regional, platform, workflow, and manual alternatives when material.
- The research output is specific enough to produce realistic KPIs, journeys, product bricks, and team ownership.

## Repository Fit

- Research informs `_config/product-domains/<domain>/business/competition.json`, `customers/customers.json`, product-brick naming, delivery channels, and team topology.
- Prefer official reported metrics over estimates.
- Do not invent company statistics to fill a JSON field.

## Avoid

- Using unsourced market-size filler as evidence.
- Converting platform-wide reported metrics into domain-pure metrics unless the source did that conversion.
- Treating press positioning as proof of customer value without corroborating product, customer, or operating signals.
