---
name: product-domain-framing
description: "Use when selecting, naming, scoping, or refining a product domain for Spec-Driven Product Architecture under _config/product-domains."
---

# Product Domain Framing

## Purpose

Define the business domain that will be modeled before any JSON is authored. A good domain is large enough to contain a coherent customer, business, delivery, and product-brick model, but narrow enough that boundaries, customers, economics, and team ownership remain understandable.

## Workflow

1. Inspect adjacent existing domains under `_config/product-domains/` before choosing the boundary.
2. Name the domain in business language, not implementation language.
3. Define core scope, adjacent scope, and explicitly excluded scope.
4. Identify the main value exchange: who gets value, who pays, who operates, and which systems make the value repeatable.
5. Confirm that the domain can support customers, delivery, product bricks, teams, objectives, and competition analysis.

## Quality Bar

- The selected domain maps to a real operating area, not a broad company description.
- Boundary decisions explain why adjacent businesses or capabilities are included or excluded.
- The domain can support at least 20 realistic product bricks for mature domains.
- The domain name is lowercase hyphen-case for IDs and clear title case for display names.
- Claims about market position, category, or scope are separated from assumptions.

## Repository Fit

- Start from `_config/product-domains/AGENTS.md` and at least two comparable existing domains.
- Keep `_config/**` as source of truth.
- Use repository terms: customers, product strategy, delivery, objectives, product bricks, product deployments, teams, evidence, and documents.
- Do not create a schema before checking how current domains represent the same concept.

## Avoid

- Modeling the whole company when the prompt asks for a product domain.
- Choosing a technology platform as the domain unless the company actually sells or operates that platform as a product.
- Blurring discovery/evaluation journeys with in-product task workflows.
- Treating support, operations, finance, trust, or compliance as outside scope when they are structurally part of the domain.
