# Productscape archived

This repository preserves the original combined Productscape project and its history.
The maintained repositories are:

- [productscape](https://github.com/zeljkoobrenovic/productscape): reusable domain-authoring skills, schemas, templates, and scripts.
- [productscape-examples](https://github.com/zeljkoobrenovic/productscape-examples): example domains built with the toolkit.

The documentation below describes this original combined repository.

**Deep research. Curated structure. Visual landscape.**

Productscape is a toolset for AI-powered deep research into a product domain, curated into a structured, visual landscape — customers, products, product bricks, teams, and competition — and published as a static documentation site. Each generated domain is a *productscape*: a pragmatic structure that can later be grounded in real implementation evidence.

The generated documentation is published via GitHub Pages at:

https://zeljkoobrenovic.github.io/productscape-archived/

The core idea is to describe product strategy from a customer-centric perspective and connect it to:

- customer groups and jobs to be done
- value propositions and outcomes
- KPI pyramids and north-star metrics
- roadmap horizons and milestones
- delivery structure and channels
- product bricks, the implementation-facing building blocks
- supporting evidence, documents, and architectural references
- stress tests that show how unexpected business changes affect strategy, implementation, and organization

## How It Works

This repository uses:

- JSON as the source-of-truth authoring format under `_config/`
- HTML templates under `_templates/`
- Python generators under `_wiring/`
- self-contained generated HTML output under `docs/`

There is no frontend framework, build system, or external JavaScript runtime dependency. Generated pages are plain static assets intended for simple publishing, including GitHub Pages.

## Repository Structure

- `_config/`
  Source-of-truth data for product domains, customers, product deployments, product bricks, data assets, teams, evidence metadata, and supporting documents.
- `_templates/`
  HTML templates used by the generators.
- `docs/`
  Generated static website output only.
- `_wiring/`
  Python generation scripts that wire `_config/` and `_templates/` into `docs/`.
- `_config/_prompts/`
  Prompt assets used to create or extend strategic and customer models.
- `_config/scripts/image-generation/`
  Source-first generators for customer, JTBD, journey, relationship, domain-icon, and residuality imagery.

## Main Modeling Areas

### Product Domains

Every domain lives in `_config/product-domains/<group>/<domain-id>/`. Always choose a group when creating a domain; never place a domain directly under `_config/product-domains/`. The current groups are `other`, `platforms`, `food-and-health`, `enterprise`, `marketplaces`, `mobility`, and `vortexcp`. Groups can be added, renamed, or reorganized without editing scripts.

`_wiring/domain_paths.py` discovers the groups and resolves domains by their globally unique, lowercase domain IDs. `_wiring/product-domains/run.sh` generates every domain with a `<group>/<domain-id>/start/config.json`; there is no hardcoded domain or group list. `_config/product-domains/start/` holds shared navigation assets and is excluded from discovery.

Generated pages live under `docs/<group>/<domain-id>/`, for example `docs/vortexcp/bi-dashboard-extensions-platform/start/index.html`. Moving a domain to another source group changes its published path; CLI arguments continue to use the bare domain ID. The start-package generator resolves app links and icons against the current source group.

Start-package app links and icons in `_config/start-packages/*/apps.json` are relative to their generated package page, for example `../../vortexcp/bi-dashboard-extensions-platform/start/index.html`. After changing source groups, regenerate the domains and run `python3 _wiring/generate-start-apps-docs.py` from the repository root to refresh the package launchers.

Each domain typically contains:

- `_domain/DOMAIN.md`
  Narrative domain brief.
- `customers/customers.json`
  Customer groups, personas, JTBDs, KPI pyramids, and strategy horizons (with `insights.json` alongside).
- `product-deployments/products.json` and `product-deployments/deployment.json`
  Products and the delivery/deployment model.
- `product-bricks/product-bricks.json`
  The catalog of reusable implementation-facing building blocks.
- `product-bricks/product-stream.json`
  Product streams composed from product bricks and external systems.
- `teams/teams.json`
  Team structure.
- `business/competition.json`
  Competitive landscape (with `business/logos/`).
- `residuality/residuality.json`
  Optional outside-change tests that describe the new business situation, the required response, the concrete design change, and affected productscape items.
- `data/data-assets.json`
  Domain data assets.
- `start/config.json`
  Start-page configuration (with `start/icons/`).

## Creating A New Product Domain

The workflow described below was written from using Codex as the CLI assistant, because that is the tool used in this repository so far. The same prompt-driven approach should also work with other capable CLI tools, such as Claude, as long as they can inspect the repository, create files under `_config/product-domains/`, and follow the existing JSON and folder conventions.

The simplest way to create a new domain is to start from the prompt template at `_config/_prompts/customers/NEW-DOMAIN-PROMPT.md` and refine it with real source links plus references to existing domains in this repository.

Recommended flow:

1. Choose a group and a globally unique lowercase domain slug, such as `marketplaces/travel-accommodations-marketplace`.
2. Open `_config/_prompts/customers/NEW-DOMAIN-PROMPT.md`.
3. Replace the placeholders such as `<DOMAIN-LINK>` and `<webbsite-link>` with the company, product, or business area you want to model.
4. Add source links that give the model enough grounding to produce realistic content. Good inputs usually include:
   - official product and marketing pages
   - help center or support documentation
   - API or developer documentation
   - investor or annual-report pages
   - architecture, engineering, or trust-and-safety writeups
   - app store pages or onboarding flows
5. Ask the model to create a new folder under `_config/product-domains/<group>/<new-domain>/` by following the same structure and naming patterns used by current domains such as:
   - `_config/product-domains/marketplaces/ride-sharing-marketplace/`
   - `_config/product-domains/marketplaces/online-retail-marketplace/`
   - `_config/product-domains/mobility/premium-long-haul-airline/`
6. Refine the generated content until it matches the repository conventions:
   - IDs stay lowercase
   - terminology stays aligned with customers, product deployments, teams, product bricks, data assets, and evidence
   - JSON structure follows existing domains instead of inventing a new schema
7. Make sure the new domain contains the expected source files, typically:
   - `_domain/DOMAIN.md`
   - `customers/customers.json`
   - `customers/insights.json`
   - `product-deployments/products.json`
   - `product-deployments/deployment.json`
   - `product-bricks/product-bricks.json`
   - `product-bricks/product-stream.json`
   - `teams/teams.json`
   - `business/competition.json`
   - `start/config.json`
   - `data/data-assets.json`
8. Registration is automatic: `_wiring/product-domains/run.sh` discovers every domain that has a `start/config.json` with `id`, `name`, and `description`. Use `./run-one.sh <domain-id>` to regenerate a single domain.
9. Regenerate the documentation from `_wiring/product-domains/`.

Example prompt setup:

```text
Use _config/_prompts/customers/NEW-DOMAIN-PROMPT.md as the base.
Model the domain for https://example.com/.
Use these grounding links:
- https://example.com/
- https://help.example.com/
- https://developer.example.com/
- https://investors.example.com/

Create the new domain under _config/product-domains/other/example-domain/.
Use ride-sharing-marketplace and online-retail-marketplace as structural references.
Keep all ids lowercase and reuse the repository's existing JSON schemas and naming patterns.
```

After the new domain has a `start/config.json` in `_config/product-domains/<group>/<new-domain>/`, generate its pages with `_wiring/product-domains/run-one.sh <new-domain>`. Registration is automatic.

### Data And Evidence

- `_evidence/`
  Self-contained evidence pipeline. Example per-source scripts under `_evidence/_example_scripts/` (source-code, gcp, aws, workday) write fragment files into `_evidence/database/evidence-files/<source>.json`; `database/aggregate-evidence.py` merges them into `database/all-evidence.json`. Run the full chain with `_evidence/run.sh` (example scripts are skipped when their external input data is absent).

### Evidence Explorer

`_wiring/evidence-explorer/generate-evidence-explorer-docs.py` renders `_templates/evidence-explorer/index.html` into a standalone search UI at `docs/evidence-explorer/index.html`, inlining `all-evidence.json` into the page (no runtime fetch) and copying the evidence and template icons. It is wired as the last step of `_evidence/run.sh`, so editing fragments and re-running `run.sh` refreshes the explorer.

The explorer shows one tab per evidence type with central search. It also has an iframe-embed mode: `?embed=1` drops the page chrome, `?ids=<comma/newline-separated glob patterns>` restricts and pre-filters by fragment id (supports `*` and `?`), and `?useTabs=false` renders stacked sections instead of tabs.

### Product Bricks

Product bricks connect strategy to execution. They bridge customer and business needs with systems, services, APIs, delivery work, and architecture.

### Residuality Stress Test

Every generated productscape includes a Residuality Stress Test. It asks a practical question: if customers, markets, regulation, operations, or competitors changed unexpectedly, what would the business do and what would need to change in the product? Domains without authored tests show an empty starting state plus an explanation of the method; add `_config/product-domains/<group>/<domain-id>/residuality/residuality.json` to populate it. The eMobility domain is the flagship example, adapted from the EV-charging example in Barry M. O'Reilly's *Residues: Time, Change, and Uncertainty in Software Architecture* (2024).

Each test records what outside change occurs, what would reveal it, the new situation the business enters, how the business responds, and the exact product or architecture change required. Residuality Theory calls the outside change a *stressor*, the recurring business situation an *attractor*, and the resulting design change a *residue*, but the app presents the plain-language explanation first. Every change is linked to existing vision, JTBD, journey, KPI, competitor, product, product-stream, product-brick, and team ids, grouped as Strategy & Vision, Implementation, and Organization. The shared-impact matrix then makes it clear when one outside change requires coordinated changes across several parts of the productscape.

## Generation

Generation scripts live under `_wiring/`.

Product-domain generators:

- `generate-start-docs.py`
- `generate-customers-docs.py`
- `generate-products-docs.py`
- `generate-product-bricks-docs.py`
- `generate-teams-docs.py`
- `generate-competition-docs.py`
- `generate-residuality-docs.py`

Run them from the generator folder, either domain-by-domain or via the wrapper script:

```bash
cd _wiring/product-domains
./run.sh
```

For a single domain, run this from the repository root, passing its ID without the group:

```bash
_wiring/product-domains/run-one.sh ride-sharing-marketplace
```

From the repository root, inspect discovery or resolve a source folder with:

```bash
python3 _wiring/domain_paths.py list
python3 _wiring/domain_paths.py resolve ride-sharing-marketplace
```

From `_wiring/product-domains/`, individual generators take the same three arguments:

```bash
python3 generate-start-docs.py <domain_id> <domain_name> <domain_description>
python3 generate-customers-docs.py <domain_id> <domain_name> <domain_description>
python3 generate-products-docs.py <domain_id> <domain_name> <domain_description>
python3 generate-product-bricks-docs.py <domain_id> <domain_name> <domain_description>
python3 generate-teams-docs.py <domain_id> <domain_name> <domain_description>
python3 generate-competition-docs.py <domain_id> <domain_name> <domain_description>
python3 generate-residuality-docs.py <domain_id> <domain_name> <domain_description>
```

Other generators live under:

- `_wiring/evidence-explorer/generate-evidence-explorer-docs.py` (run via `_evidence/run.sh`)
- `_wiring/generate-start-apps-docs.py`

Offline checks for grouped discovery and both domain wrappers:

```bash
python3 -B -m unittest discover -s _wiring -p 'test_*.py'
python3 .claude/skills/scripts/validate-domain-model.py --all
```

### Product-Domain Images

Image generation is a separate, source-first workflow under `_config/scripts/image-generation/`. It writes image assets beside the relevant product-domain JSON and updates source `media` references; it does not regenerate `docs/`.

Run all image generators for one domain with Gemini:

```bash
export GEMINI_API_KEY=...
_config/scripts/image-generation/run.sh <domain-id>
```

The default JTBD and journey behavior creates both overview and individual step/stage images. For a lower-cost run that creates only one overview per JTBD and journey, while preserving any existing detailed images and references, use:

```bash
_config/scripts/image-generation/run.sh <domain-id> --lightweight
```

See `_config/scripts/image-generation/README.md` for individual provider commands, dry runs, retries, overwrite behavior, and JSON-only updates.

## Editing Guidance

- Change strategy or domain content in `_config/**`.
- Change presentation in `_templates/**`.
- Treat `docs/**` as generated output unless you intentionally want to patch generated files directly.
- Treat `_wiring/**` as the place for generator logic and script maintenance.
- Preserve the repository's no-framework approach.
- Keep generated pages self-contained.
- Before regenerating, inspect the worktree if there are existing uncommitted changes.

## Practical Mental Model

Work in this order:

1. customer value and desired outcomes
2. KPIs and strategy horizons
3. product delivery structure
4. product bricks and capabilities
5. outside-change tests and the resulting productscape changes
6. implementation and architectural evidence
7. generated static documentation

That sequence reflects the intent of the repository: strategy should stay grounded in real product building blocks and implementation reality.
