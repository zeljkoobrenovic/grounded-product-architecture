# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

Grounded Product Architecture models product strategy as structured JSON and generates a self-contained static documentation site (published via GitHub Pages). There is **no frontend framework, build system, npm, or external JS runtime** — generators are plain Python 3, output is standalone HTML with embedded data. Preserve this no-framework approach; do not introduce React, bundlers, or client-side package dependencies.

The pipeline is one-directional:

```
_config/**  (JSON source of truth)  +  _templates/**  (HTML)  --Python in _wiring/**-->  docs/**  (generated)
```

## Generating the site

All product-domain generators run from `_wiring/product-domains/` and take three positional args (`domain_id`, `domain_name`, `domain_description`). The wrapper script discovers every domain from `_config/product-domains/*/start/config.json` and defines the generator order:

```bash
cd _wiring/product-domains
./run.sh                      # regenerate all domains with all generators
```

Run a single generator for one domain:

```bash
cd _wiring/product-domains
python3 generate-customers-docs.py ride-sharing-marketplace "Ride Sharing Marketplace" "Description..."
```

Generator order matters and is fixed in `run.sh`: `generate-start-docs` -> `customers` -> `products` -> `product-bricks` -> `teams` -> `competition`. Each generator `chdir`s into `docs/product-domains/` and resolves config/template paths relative to the repo root via `domain_cli.load_domain_args()`.

There is no test suite, linter config, or package manifest. Validation is: run the generator and inspect the produced HTML under `docs/`.

## Adding or registering a domain

1. Create `_config/product-domains/<lowercase-slug>/` following an existing domain (use `ride-sharing-marketplace` as the structural reference).
2. Create `start/config.json` with `id`, `name`, and `description` — that registers the domain; `run.sh` discovers every domain from the config tree (use `./run-one.sh <domain-id>` to regenerate just one).
3. Regenerate from `_wiring/product-domains/`.

The prompt scaffold for a new domain lives at `_config/_prompts/customers/NEW-DOMAIN-PROMPT.md`.

## Domain config layout

Inside `_config/product-domains/<domain>/`:

- `_domain/DOMAIN.md` — narrative domain brief
- `customers/customers.json` — customer groups, personas, JTBDs, KPI pyramids, strategy horizons (+ `insights.json`, optional `links.json` external reference links, `icons/`, `media/`)
- `product-deployments/products.json`, `product-deployments/deployment.json` — products and delivery/deployment model
- `product-bricks/product-bricks.json` — catalog of implementation-facing building blocks
- `product-bricks/product-stream.json` — product streams composed from bricks
- `teams/teams.json`
- `business/competition.json` (+ `business/logos/`)
- `data/data-assets.json`
- `start/config.json` (+ `start/icons/`)

## Generator architecture

Shared Python modules in `_wiring/product-domains/` (import these rather than re-implementing):

- `domain_cli.py` — arg parsing; every generator calls `load_domain_args()`
- `product_bricks_support.py` — product-brick layer model (`PRODUCT_BRICK_LAYER_ORDER`: ui → interfaces → worker → stateless-service → service → integration) and labels/descriptions
- `generator_common.py` — shared generator helpers: `enter_docs_root()`, JSON loading, icon/media copying, breadcrumb rendering, `normalize_icon_name`, group-tree iteration, customers/KPI lookups. Import these rather than re-implementing per generator.

Templates live in `_templates/<area>/` with shared partials under `_templates/_imports/` (e.g. `tabs/`, `breadcrumbs/`, `common/`). Generators read template HTML and substitute `${key}` placeholders. Output for each area is fully rebuilt: generators `shutil.rmtree` the target docs folder before regenerating, so do not hand-edit files under `docs/product-domains/`.

## Evidence database & explorer

`_evidence/` is a separate pipeline from the product domains. Example per-source scripts under `_evidence/_example_scripts/` (source-code, gcp, aws, workday) write fragment files into `_evidence/database/evidence-files/<source>.json`, then `database/aggregate-evidence.py` concatenates them into `database/all-evidence.json` (a list of `{group, fragments}` objects; each fragment has `id`, `type`, `icon`, `title`, `description`, `facts`, `links`, `tags`). `_evidence/run.sh` runs the whole chain; the example scripts need external input data and are skipped when it is absent, keeping the committed fragment files.

`_wiring/evidence-explorer/generate-evidence-explorer-docs.py` builds a standalone search UI at `docs/evidence-explorer/index.html` from `_templates/evidence-explorer/index.html`: it inlines `all-evidence.json` into the page (so the page needs no runtime fetch) and copies both the evidence icons and the template's own `icons/` into the output. It is wired as the last step of `_evidence/run.sh`, so editing fragments and re-running `run.sh` refreshes the explorer too. The explorer shows one tab per evidence `type`; in iframe-embed mode (`?embed=1` / `?ids=<glob patterns>`) `?useTabs=false` switches to stacked sections instead of tabs.

## Schemas and validation

Structural contracts for every config artifact live in `_config/_schema/*.schema.json` (required fields, types, fixed enums, retired-field bans). They are enforced by a dependency-free checker (`.claude/skills/scripts/schema_check.py`) as part of `validate-domain-model.py`, which also verifies cross-file references. Run it after any config edit:

```bash
python3 .claude/skills/scripts/validate-domain-model.py <domain-id>   # or --all
```

Shared enum/definition defaults (brick types/statuses, module config, team types, stream definitions) live in `_config/_shared/*.json`; domain files only declare those blocks to override the shared model.

## Conventions

- All ID values in `_config/**` (`id`, `*Id`, `*Ids`) are **lowercase**.
- Reuse existing JSON schemas and template `${...}` patterns instead of inventing parallel structures.
- Keep terminology aligned with the domain language: customers, product deployments, product bricks, streams, teams, data assets, evidence.
- Edit strategy/content in `_config/**`; edit presentation in `_templates/**`; treat `_wiring/**` as generator logic; treat `docs/**` as generated output (patch directly only when explicitly asked).
- Before regenerating, inspect the worktree if it is dirty — generators wipe and rebuild docs folders.
