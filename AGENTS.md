# AGENTS.md

## Project

This repository contains **Productscape**, a toolset for modeling product strategy in a structured, implementation-aware way.

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
  - Source-of-truth data for product domains, product bricks, customers, product deployments, teams, data assets, residuality stress tests, evidence metadata, and supporting documents.
- `_templates/`
  - HTML templates used to generate the static site.
- `_wiring/`
  - Python generator scripts that wire `_config/...` and `_templates/...` into `docs/...`.
- `_data/evidence-db/`
  - Separate evidence pipeline: per-source scripts produce fragment files, `aggregate-evidence.py` merges them into `database/all-evidence.json`, and `run.sh` runs the chain (see Evidence database below).
- `_skills/`
  - Repo-local Codex skill guidance for cross-cutting modeling workflows that span source data, generators, templates, and generated documentation.
- `docs/`
  - Generated static website output.
- `_config/_prompts/`
  - Prompt assets used to create or extend strategic/customer JSON models.
- `_config/scripts/image-generation/`
  - Source-first image generators that write product-domain media assets and update their source JSON references.

## Key Modeling Areas

### 1. Product domains

`_wiring/product-domains/run.sh` defines the set of modeled domains and invokes the product-domain generators with explicit domain parameters.

Each domain typically contains:

- `_domain/DOMAIN.md`
  - Narrative domain brief.
- `customers/customers.json`
  - Customer groups, personas, JTBD, KPI pyramids, and product strategy horizons (with `insights.json` alongside).
- `product-deployments/products.json` and `product-deployments/deployment.json`
  - Products and the delivery/deployment model.
- `product-bricks/product-bricks.json`
  - The catalog of product bricks, the reusable implementation-facing building blocks.
- `product-bricks/product-stream.json`
  - Product streams composed from one or more product bricks and/or external systems.
- `product-bricks/bricks-evidence.json` and `product-bricks/streams-evidence.json`
  - Evidence references for bricks and streams.
- `teams/teams.json`
  - Team structure.
- `business/competition.json`
  - Competitive landscape (with `business/logos/`).
- `data/data-assets.json`
  - Domain data assets.
- `start/config.json`
  - Start-page configuration (with `start/icons/`).
- `residuality/residuality.json` (optional)
  - Business-context stressors, attractors, reactions, residues, looping links, and impacts on strategy, products, bricks, teams, and competition.

### 2. Product bricks

Product bricks are the implementation-facing units that connect strategy to execution. They are the bridge between:

- customer and business needs
- roadmap and investment choices
- concrete systems, services, APIs, and delivery work
- architecture and evidence

### 3. Static site generation

Generation scripts live under `_wiring/product-domains/` and run in this order (see `run.sh`):

- `generate-start-docs.py`
- `generate-customers-docs.py`
- `generate-products-docs.py`
- `generate-product-bricks-docs.py`
- `generate-teams-docs.py`
- `generate-competition-docs.py`
- `generate-residuality-docs.py`

These scripts read from `_config/...` and `_templates/...` and write generated pages into `docs/...`.

### 4. Evidence database and explorer

`_data/evidence-db/` is a self-contained pipeline, separate from the product-domain generators:

- Per-source scripts under `_data/evidence-db/scripts/` write `_data/evidence-db/database/evidence-files/<source>.json`.
- `database/aggregate-evidence.py` merges those into `database/all-evidence.json` — a list of `{group, fragments}` objects; each fragment has `id`, `type`, `icon`, `title`, `description`, `facts`, `links`, `tags`.
- `_data/evidence-db/run.sh` runs the per-source scripts, then aggregation, then the explorer generator.

`_wiring/evidence-explorer/generate-evidence-explorer-docs.py` renders `_templates/evidence-explorer/index.html` into `docs/evidence-explorer/index.html`, inlining `all-evidence.json` directly into the page and copying evidence-db plus template icons. The explorer shows one tab per evidence `type`; in iframe-embed mode (`?embed=1` / `?ids=<glob patterns>`), `?useTabs=false` renders stacked sections instead of tabs. To change which facts appear, edit the source fragment files (e.g. `database/evidence-files/aws-accounts.json`) and re-run `run.sh`.

### 5. Source image generation

`_config/scripts/image-generation/` contains API-backed generators for JTBD, customer journey, customer-relation, domain-icon, and residuality images. These scripts write into `_config/product-domains/**` and may update source JSON media references; they do not regenerate `docs/`.

The domain wrapper accepts `_config/scripts/image-generation/run.sh <domain-id> --lightweight`. In lightweight mode, JTBD and journey generation creates only one overview per job/journey and does not create new targets or media references for individual steps/stages. Existing detailed media is preserved. Without the flag, the full overview-plus-detail behavior remains the default.

## Working Rules For Agents

- Treat `_config/**` and `_templates/**` as the primary editable sources.
- Treat `_skills/**` as repo-local agent guidance, not product-domain source data.
- Treat `docs/**` as generated output unless the user explicitly asks for a direct patch there.
- Preserve the repository's no-framework approach. Do not introduce React, build tooling, npm dependencies, or external JS libraries unless explicitly requested.
- Keep generated pages self-contained. Avoid solutions that depend on shared runtime infrastructure or client-side package bundling.
- Prefer extending the existing JSON schemas and HTML template patterns instead of inventing a parallel model.
- Keep all ID values in `_config/**` lowercase, including `id`, `*Id`, and `*Ids` fields.
- Keep naming aligned with the domain language already used in the repository: customers, product strategy, delivery, product bricks, targets, roadmap, evidence, documents.

## Editing Guidance

- If the user asks to change strategic content, start in `_config/product-domains/**`.
- If the user asks to change presentation or navigation, start in `_templates/**`.
- If the user asks to regenerate the website, run the relevant Python generators from `_wiring/**`.
- Do not blindly overwrite generated `docs/` content if the worktree is dirty; inspect current changes first. Generators `shutil.rmtree` their target docs folder before rebuilding, so never hand-edit files under `docs/product-domains/`.
- Before regenerating, verify the current generator expects the same source file names present in the domain folder; the per-domain layout has evolved (e.g. `product-deployments/`, `product-bricks/product-stream.json`) and older domains may lag.
- Before calling image APIs, use the relevant generator's `--dry-run` when scope or cost is uncertain. Use `--lightweight` when the requested output is limited to JTBD and journey overview images.

## Practical Mental Model

When working in this repo, think in this order:

1. customer value and desired outcomes
2. KPIs and strategic horizons
3. product delivery structure
4. product bricks/capabilities
5. residuality stressors and residues across the modeled landscape
6. implementation and architectural evidence
7. generated static documentation

That sequence matches the intent of Productscape: deep research curated into a structure that stays connected to actual product building blocks and implementation reality.
