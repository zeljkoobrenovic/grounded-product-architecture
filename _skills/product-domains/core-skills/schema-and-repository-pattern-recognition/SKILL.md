---
name: schema-and-repository-pattern-recognition
description: "Use when inferring canonical folder structure, JSON schemas, naming patterns, generator expectations, and modeling depth from existing product domains."
---

# Schema And Repository Pattern Recognition

## Purpose

Understand the repository's current modeling conventions before editing. This is essential because domains may reflect older and newer schema variants.

## Workflow

1. Read `_config/product-domains/AGENTS.md`.
2. Inspect multiple mature comparable domains, not just one.
3. Check generator scripts under `_wiring/product-domains/` before assuming filenames or field names.
4. Identify required files, optional files, ID conventions, and reference fields.
5. Prefer the most current internally consistent pattern over inventing a new schema.

## Quality Bar

- File layout matches existing domains of similar maturity.
- Field names, nesting, and IDs align with generator expectations.
- References resolve across customers, teams, product bricks, delivery, objectives, and releases.
- Differences between older and newer domain variants are handled deliberately.

## Repository Fit

- Primary sources are `_config/product-domains/**`, `_templates/**`, and `_wiring/product-domains/**`.
- Treat `docs/**` as generated output unless asked to patch it directly.

## Avoid

- Creating parallel structures because one example is incomplete.
- Regenerating docs before validating source JSON.
- Assuming `products.json` and `delivery.json` names without checking the current generator.
