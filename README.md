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

- JSON as the source-of-truth authoring format under `_config/`
- HTML templates under `_templates/`
- Python generators under `_wiring/`
- self-contained generated HTML output under `docs/`

There is no frontend framework, build system, or external JavaScript runtime dependency. Generated pages are plain static assets intended for simple publishing, including GitHub Pages.

## Repository Structure

- `_config/`
  Source-of-truth data for product domains, customers, delivery models, product bricks, roadmap overlays, data sources, evidence metadata, and supporting documents.
- `_templates/`
  HTML templates used by the generators.
- `docs/`
  Generated static website output only.
- `_wiring/`
  Python generation scripts that wire `_config/` and `_templates/` into `docs/`.
- `_prompts/`
  Prompt assets used to create or extend strategic and customer models.

## Main Modeling Areas

### Product Domains

`_wiring/product-domains/run.sh` defines the modeled domains and invokes the product-domain generators with explicit domain parameters.

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

## Creating A New Product Domain

The simplest way to create a new domain is to start from the prompt template at `_config/_prompts/customers/NEW-DOMAIN-PROMPT.md` and refine it with real source links plus references to existing domains in this repository.

Recommended flow:

1. Choose a clear domain and a lowercase slug such as `travel-accommodations-marketplace`.
2. Open `_config/_prompts/customers/NEW-DOMAIN-PROMPT.md`.
3. Replace the placeholders such as `<DOMAIN-LINK>` and `<webbsite-link>` with the company, product, or business area you want to model.
4. Add source links that give the model enough grounding to produce realistic content. Good inputs usually include:
   - official product and marketing pages
   - help center or support documentation
   - API or developer documentation
   - investor or annual-report pages
   - architecture, engineering, or trust-and-safety writeups
   - app store pages or onboarding flows
5. Ask the model to create a new folder under `_config/product-domains/<new-domain>/` by following the same structure and naming patterns used by current domains such as:
   - `_config/product-domains/ride-sharing-marketplace/`
   - `_config/product-domains/online-retail-marketplace/`
   - `_config/product-domains/premium-long-haul-airline/`
6. Refine the generated content until it matches the repository conventions:
   - IDs stay lowercase
   - terminology stays aligned with customers, objectives, delivery, teams, product bricks, and evidence
   - JSON structure follows existing domains instead of inventing a new schema
7. Make sure the new domain contains the expected source files, typically:
   - `_domain/DOMAIN.md`
   - `customers/customers.json`
   - `customers/insights.json`
   - `product-deployments/products.json`
   - `product-deployments/deployment.json`
   - `delivery/releases.json`
   - `product-bricks/product-bricks.json`
   - `product-bricks/product-capability.json`
   - `product-bricks/bricks-evidence.json`
   - `product-bricks/capabilities-evidence.json`
   - `objectives/current|next|ktlo|archived/{objectives,initiatives,discoveries}.json`
   - `teams/teams.json`
   - `start/config.json`
   - `data/data-assets.json`
   - `business/scorecard.json`
8. Register the new domain in `_wiring/product-domains/run.sh` by adding a new `domain_id|Domain Name|Domain description` entry to the `domains=(...)` list.
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

Create the new domain under _config/product-domains/example-domain/.
Use ride-sharing-marketplace and online-retail-marketplace as structural references.
Keep all ids lowercase and reuse the repository's existing JSON schemas and naming patterns.
```

After the new domain exists in `_config/product-domains/<new-domain>/`, generate the site pages by adding it to `_wiring/product-domains/run.sh` and running the generators.

### Data And Evidence

- `_data/data/`
  Source data used by evidence and reporting generators such as AWS, GCP, budget, incidents, history, brands, and Slack.
- `_data/evidence-db/`
  Cached evidence fragment metadata used to enrich generated product-brick documentation.

### Product Bricks

Product bricks connect strategy to execution. They bridge customer and business needs with systems, services, APIs, delivery work, and architecture.

## Generation

Generation scripts live under `_wiring/`.

Product-domain generators:

- `generate-customers-docs.py`
- `generate-products-docs.py`
- `generate-product-bricks-docs.py`
- `generate-delivery-docs.py`
- `generate-objectives-docs.py`
- `generate-start-docs.py`
- `generate-teams-docs.py`

Run them from the generator folder, either domain-by-domain or via the wrapper script:

```bash
cd _wiring/product-domains
./run.sh
```

```bash
python3 generate-customers-docs.py <domain_id> <domain_name> <domain_description>
python3 generate-products-docs.py <domain_id> <domain_name> <domain_description>
python3 generate-product-bricks-docs.py <domain_id> <domain_name> <domain_description>
python3 generate-delivery-docs.py <domain_id> <domain_name> <domain_description>
python3 generate-objectives-docs.py <domain_id> <domain_name> <domain_description>
python3 generate-start-docs.py <domain_id> <domain_name> <domain_description>
python3 generate-teams-docs.py <domain_id> <domain_name> <domain_description>
```

Other generator groups live under:

- `_wiring/evidence/`
- `_wiring/standards/`
- `_wiring/controls/`
- `_wiring/enterprise-domains/`
- `_wiring/generate-start-apps-docs.py`

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
5. implementation and architectural evidence
6. generated static documentation

That sequence reflects the intent of the repository: strategy should stay grounded in real product building blocks and implementation reality.
