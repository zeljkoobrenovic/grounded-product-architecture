# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repo Is

**Grounded Product Architecture** — a static documentation website generator for product strategy modeling. It turns JSON config files into self-contained HTML pages.

- Source of truth: `_config/` (JSON data) and `_templates/` (HTML templates)
- Output: `docs/` (generated HTML — treat as derived, never hand-edit)
- Stack: Python generators, vanilla HTML/CSS/JS, zero external JS libraries or build tooling

## Running Generators

Generators should be run from `_wiring/`:

```bash
# Regenerate product domain pages
cd _wiring/product-domains && python3 generate-customers-docs.py
cd _wiring/product-domains && python3 generate-product-bricks-docs.py
cd _wiring/product-domains && python3 generate-delivery-docs.py
cd _wiring/product-domains && python3 generate-products-docs.py
cd _wiring/product-domains && python3 generate-objectives-docs.py
cd _wiring/product-domains && python3 generate-teams-docs.py

# Regenerate standards/evidence pages
cd _wiring/standards && python3 generate-rituals-docs.py
cd _wiring/evidence  && python3 generate-aws-docs.py

# JTBD image generation (requires API key)
export OPENAI_API_KEY=...
cd _config/scripts/jtbd-image-generation
python3 generate_jtbd_images_openai_images_api.py --dry-run
python3 generate_jtbd_images_openai_images_api.py --domain nutrition --overwrite
```

There is no Makefile or top-level build script. Run generators individually as needed.

## Architecture

### Generation Pipeline

1. `_wiring/product-domains/run.sh` defines the domain list and invokes each product-domain generator with `<domain_id> <domain_name> <domain_description>`
2. Each generator handles one domain, loading domain JSON from `_config/product-domains/<domain>/`
3. Data is injected into an HTML template via string replacement (e.g., `.replace('${customers}', json.dumps(data))`)
4. Self-contained HTML files are written to `docs/product-domains/<domain>/`
5. Icons and media are copied from `_config/` to `docs/` alongside the HTML

### Per-Domain Data Shape

Each domain under `_config/product-domains/<domain>/` contains:
- `customers/customers.json` — personas, JTBD, KPI pyramids, strategy horizons
- `product-bricks/product-bricks.json` — hierarchical implementation-facing building blocks
- `product-bricks/product-capability.json` — outcome-based capabilities
- `objectives/current.json`, `next.json`, `archive.json` — quarterly OKRs
- `delivery/initiatives.json`, `delivery/releases.json` — roadmap and delivery data
- `teams/teams.json` — org structure

### Rituals (shared, not per-domain)

Rituals live at `_config/standards/rituals/meetings.json` — not inside individual domain folders.

### Template Pattern

Templates in `_templates/` are plain HTML files with `${variable}` placeholders. Generators replace these with `json.dumps(...)` of the relevant config data. The output is a fully self-contained page with the data embedded as a JS variable or inline JSON.

## Key Constraints

- No npm, no React, no build tools — keep everything vanilla
- Do not introduce external JS libraries
- Do not hand-edit `docs/` — run the appropriate generator instead
- Before regenerating, check `git status` to avoid overwriting uncommitted changes in `docs/`
- Source file names in `_config/` may be evolving (e.g., `products.json` → `delivery.json`); verify generator expectations match actual files before running
