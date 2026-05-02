---
name: static-documentation-modeling
description: "Use when creating source content that remains clear, navigable, and useful after rendering into the repository's static HTML documentation site."
---

# Static Documentation Modeling

## Purpose

Write source JSON so the generated standalone HTML pages are clear, navigable, and useful. The model should work both as structured data and as rendered documentation.

## Workflow

1. Inspect the relevant template to understand how fields render.
2. Keep names concise enough for cards, tables, filters, and landing pages.
3. Write descriptions that explain purpose, ownership, and outcome without overloading UI surfaces.
4. Ensure links between customers, objectives, delivery, product bricks, teams, and evidence create useful navigation.
5. Regenerate docs only after source validation.

## Quality Bar

- Generated pages have meaningful headings, summaries, and cross-links.
- Text is specific but not too long for cards and lists.
- Repeated items use consistent depth and terminology.
- Product-brick, team, and customer landing pages tell a coherent story.

## Repository Fit

- Templates live in `_templates/**`.
- Generators live in `_wiring/product-domains/**`.
- Generated output lives in `docs/product-domains/**`.
- Static pages should remain self-contained and not require new JS frameworks or external libraries.

## Avoid

- Writing source text that only makes sense in raw JSON.
- Overlong names that break navigation or card layouts.
- Adding presentation-only fields when the existing template can render semantic source data.
