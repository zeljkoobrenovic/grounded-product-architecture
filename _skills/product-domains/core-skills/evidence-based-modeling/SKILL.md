---
name: evidence-based-modeling
description: "Use when separating facts, assumptions, and inferences while creating coherent product-domain models from incomplete public information."
---

# Evidence-Based Modeling

## Purpose

Use evidence honestly while still producing a useful model. Public information is often incomplete, so the model must distinguish sourced facts from structured inference and avoid pretending assumptions are facts.

## Workflow

1. Gather official and authoritative sources first.
2. Record facts with source context and preserve reported scope.
3. Make inferences explicit when connecting public signals to customer, system, or operating models.
4. Use assumptions only where necessary and keep them plausible.
5. Prefer conservative language in areas with weak evidence.

## Quality Bar

- Important factual claims can be traced.
- Inferences are reasonable and based on visible product, market, operational, or architectural signals.
- The model remains coherent even when some data is missing.
- Uncertainty is documented in summaries, competition scope, or evidence notes where useful.

## Repository Fit

- Evidence informs competition, scorecards, product-brick links, documents, roadmap assumptions, and customer models.
- Use official source URLs in `business/competition.json` business stats.
- Keep generated documentation credible by not overstating certainty.

## Avoid

- Fabricating metrics, customers, or architecture details.
- Hiding assumptions inside definitive language.
- Over-indexing on a single blog post or marketing page.
