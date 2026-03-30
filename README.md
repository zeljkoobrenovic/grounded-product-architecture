# Grounded Product Architecture

Grounded Product Architecture is a repository for modeling product strategy in a structured, implementation-aware way and publishing that model as a static documentation site.

The generated documentation is published via GitHub Pages at:

https://zeljkoobrenovic.github.io/grounded-product-architecture/

The core idea is to describe product strategy from a customer-centric perspective and connect it to:

- customer groups and jobs to be done
- value propositions and outcomes
- KPI pyramids and north-star metrics
- roadmap horizons and milestones
- delivery structure and channels
- product bricks, the implementation-facing building blocks
- supporting evidence, documents, and architectural references

## How It Works

This repository uses:

- JSON as the source-of-truth authoring format
- HTML templates under `_templates/`
- Python generators under `docs/product-domains/`
- self-contained generated HTML output under `docs/`

There is no frontend framework, build system, or external JavaScript runtime dependency. Generated pages are plain static assets intended for simple publishing, including GitHub Pages.

## Repository Structure

- `_config/`
  Source-of-truth data for product domains, customers, delivery models, product bricks, roadmap overlays, evidence, and supporting documents.
- `_templates/`
  HTML templates used by the generators.
- `docs/`
  Generated static website output plus the Python generation scripts under `docs/product-domains/`.
- `_prompts/`
  Prompt assets used to create or extend strategic and customer models.

## Main Modeling Areas

### Product Domains

`_config/product-domains/config.json` defines the modeled domains.

Each domain typically contains:

- `customers/customers.json`
  Customer groups, personas, JTBDs, KPI pyramids, and strategy horizons.
- `product/delivery.json`
  Delivery model, channels, APIs, events, MVP scope, and capability mappings.
- `product-bricks/product-bricks.json`
  The catalog of reusable implementation-facing building blocks.
- `product-bricks/product-capability.json`
  Outcome-based capabilities composed from product bricks and external systems.
- `product-bricks/targets.json`
  Release targets and planning overlays.
- `product-bricks/documents.json`
  Notes, discussions, and evidence references.
- `product-bricks/roadmap/roadmap.json`
  Roadmap timing and effort data.

### Product Bricks

Product bricks connect strategy to execution. They bridge customer and business needs with systems, services, APIs, delivery work, and architecture.

## Generation

Generation scripts live in `docs/product-domains/`.

Common generators:

- `generate-customers-docs.py`
- `generate-products-docs.py`
- `generate-product-bricks-docs.py`
- `generate-delivery-docs.py`
- `generate-objectives-docs.py`
- `generate-start-docs.py`
- `generate-teams-docs.py`

Run them from the generator folder so their relative paths resolve correctly:

```bash
cd docs/product-domains
python3 generate-customers-docs.py
python3 generate-products-docs.py
python3 generate-product-bricks-docs.py
python3 generate-delivery-docs.py
python3 generate-objectives-docs.py
python3 generate-start-docs.py
python3 generate-teams-docs.py
```

## Editing Guidance

- Change strategy or domain content in `_config/**`.
- Change presentation in `_templates/**`.
- Treat `docs/**` as generated output unless you intentionally want to patch generated files directly.
- Preserve the repository's no-framework approach.
- Keep generated pages self-contained.
- Before regenerating, inspect the worktree if there are existing uncommitted changes.

## Practical Mental Model

Work in this order:

1. customer value and desired outcomes
2. KPIs and strategy horizons
3. product delivery structure
4. product bricks and capabilities
5. implementation and architectural evidence
6. generated static documentation

That sequence reflects the intent of the repository: strategy should stay grounded in real product building blocks and implementation reality.
