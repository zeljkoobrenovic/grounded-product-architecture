# AGENTS.md

## Project

This repository contains **Grounded Product Architecture**, a toolset for modeling product strategy in a structured, implementation-aware way.

The core idea is to describe product strategy from a customer-centric perspective and connect it to:

- customer groups and jobs to be done
- value propositions and outcomes
- KPI pyramids and north-star metrics
- roadmap horizons and milestones
- product delivery modes
- product bricks, the implementation-facing units of product development
- supporting evidence, documents, and architecture references

In practice, this repository turns that model into a static documentation website.

## Architecture Summary

The project generates a static website from JSON configuration and simple HTML templates.

- Authoring format: JSON
- Rendering format: standalone HTML files
- Frontend stack: HTML, CSS, vanilla JavaScript
- JavaScript libraries: none
- Output style: self-contained HTML pages with embedded data

All generated HTML files are intended to be self-contained and easy to publish as static assets.

## Repository Structure

- `_config/`
  - Source-of-truth data for product domains, product bricks, customers, delivery/product definitions, targets, documents, and roadmap data.
- `_templates/`
  - HTML templates used to generate the static site.
- `docs/`
  - Generated static website output.
- `_prompts/`
  - Prompt assets used to create or extend strategic/customer JSON models.

## Key Modeling Areas

### 1. Product domains

`_config/product-domains/config.json` defines the set of modeled domains and links to supporting spreadsheets.

Each domain typically contains:

- `product/customers.json`
  - Customer groups, personas, JTBD, KPI pyramids, and product strategy horizons.
- `product/delivery.json`
  - Product delivery definition, channels, APIs, events, MVP scope, and capability mappings.
- `product-bricks/product-bricks.json`
  - The catalog of product bricks/capabilities.
- `product-bricks/targets.json`
  - Release targets and planning overlays.
- `product-bricks/documents.json`
  - Discussions, notes, and evidence references.
- `product-bricks/roadmap/roadmap.json`
  - Roadmap effort and timing data.

### 2. Product bricks

Product bricks are the implementation-facing units that connect strategy to execution. They are the bridge between:

- customer and business needs
- roadmap and investment choices
- concrete systems, services, APIs, and delivery work
- architecture and evidence

### 3. Static site generation

Generation scripts live under `docs/product/`:

- `generate-customer-docs.py`
- `generate-product-docs.py`
- `generate-product-bricks-docs.py`

These scripts read from `_config/...` and `_templates/...` and write generated pages into `docs/product/<domain>/...`.

## Working Rules For Agents

- Treat `_config/**` and `_templates/**` as the primary editable sources.
- Treat `docs/**` as generated output unless the user explicitly asks for a direct patch there.
- Preserve the repository's no-framework approach. Do not introduce React, build tooling, npm dependencies, or external JS libraries unless explicitly requested.
- Keep generated pages self-contained. Avoid solutions that depend on shared runtime infrastructure or client-side package bundling.
- Prefer extending the existing JSON schemas and HTML template patterns instead of inventing a parallel model.
- Keep naming aligned with the domain language already used in the repository: customers, product strategy, delivery, product bricks, targets, roadmap, evidence, documents.

## Editing Guidance

- If the user asks to change strategic content, start in `_config/product-domains/**`.
- If the user asks to change presentation or navigation, start in `_templates/product/**`.
- If the user asks to regenerate the website, run the Python generators from `docs/product/`.
- Do not blindly overwrite generated `docs/` content if the worktree is dirty; inspect current changes first.
- Some product modeling files appear to be evolving from `products.json` to `delivery.json`. Before regenerating product pages, verify the current generator expects the same source file names present in the domain folder.

## Practical Mental Model

When working in this repo, think in this order:

1. customer value and desired outcomes
2. KPIs and strategic horizons
3. product delivery structure
4. product bricks/capabilities
5. implementation and architectural evidence
6. generated static documentation

That sequence matches the intent of Grounded Product Architecture: strategy should remain grounded in actual product building blocks and implementation reality.
