# AGENTS.md

## Purpose

Use this folder-level guide when creating or extending any product domain under `_config/product-domains/<domain-id>/`.

Product-domain source should stay customer-centered and implementation-aware:

- define the strategic model in `_config/product-domains/<domain-id>/`
- keep strategy grounded in customers, JTBD, KPIs, product deployments, product bricks, data assets, teams, competition, and research/source context
- generate the matching static documentation in `docs/product-domains/<domain-id>/`

Prefer evolving the existing model and generator conventions over inventing a parallel schema.

## Local Modeling Skills

Use this `AGENTS.md` file for always-on repository rules, source-vs-generated policy, folder structure, ID conventions, validation, generator workflow, and completion checks.

For deeper review guidance, use the invocable skills under `.codex/skills/`:

- `gpa-product-domain-review` for customers, JTBD, journeys, value propositions, KPIs, strategy, insights, and competition.
- `gpa-product-bricks-review` for product bricks, product streams, data assets, layered modules, dependencies, external systems, team ownership, and implementation traceability.
- `gpa-teams-review` for organization design, ownership coverage, topology, staffing, dependencies, charters, AI-agent boundaries, and alignment with customers, product deployments, product bricks, and data assets.

Keep detailed modeling guidance in skills; keep this file focused on operational rules that apply to every product-domain edit.

## Core Principle

Work in this sequence:

1. Domain context and source research
2. Customers and jobs to be done
3. KPIs and strategy horizons
4. Products and deployment structure
5. Product streams and product bricks
6. Data assets and ownership
7. Teams and operating model
8. Competition and market context
9. Residuality stressors, attractors, residues, and cross-landscape impacts
10. Generated documentation

Do not start from pages or visuals. Start from the source model.

## Source-First Rule

- Treat `_config/product-domains/**` as the source of truth.
- Treat `docs/product-domains/**` as generated output.
- Only patch generated docs directly if the user explicitly asks for that.
- If presentation needs to change for all domains, patch the generators or templates instead of hand-editing generated HTML.

## Current Source Tree

A mature domain normally contains:

- `_domain/DOMAIN.md`
- `start/config.json`
- `customers/customers.json`
- `customers/insights.json`
- `customers/links.json`
- `product-deployments/products.json`
- `product-deployments/deployment.json`
- `product-bricks/product-bricks.json`
- `product-bricks/product-stream.json`
- `data/data-assets.json`
- `teams/teams.json`
- `business/competition.json`
- `residuality/residuality.json` (optional)

Optional media and icon folders may live beside the JSON sources they support.

## Recommended Domain Build Sequence

When creating a new domain, use this order unless there is a strong reason not to.

### 1. Gather Domain Context

Start with:

- any local seed files such as those in the `<domain-id>/_domain/` folder
- existing sibling domains with similar structure
- external primary or authoritative sources when domain understanding depends on current market, regulatory, or operational reality

Capture enough context to define:

- customer groups
- JTBD
- KPI pyramids
- product lines
- deployment channels
- enabling product bricks
- data assets
- team ownership assumptions
- competition and substitutes

### 2. Register The Domain

Update the domain list used by `_wiring/product-domains/run.sh` before generating docs. Keep the domain id lowercase and aligned with folder names.

### 3. Create The Base Source Tree

Create the minimum source package under `_config/product-domains/<domain-id>/`:

- `start/config.json`
- `customers/customers.json`
- `customers/insights.json`
- `customers/links.json`
- `product-deployments/products.json`
- `product-deployments/deployment.json`
- `product-bricks/product-bricks.json`
- `product-bricks/product-stream.json`
- `data/data-assets.json`
- `teams/teams.json`
- `business/competition.json`

If a generator expects a specific file shape, inspect that generator first and match the current implementation.

### 4. Define Customers Deeply

`customers/customers.json` should be substantive, not skeletal.

For each customer group, define:

- clear identity and context
- pains, needs, and constraints
- jobs to be done in operational language
- outcome expectations
- KPI pyramid with measurable leaves
- product strategy horizon or priority framing if the schema supports it

`productStrategy` should be treated as expected, not optional, for a mature domain model.

Preferred horizon shape:

- `vision`
- `timeHorizons`
- `year1`
- `year3`
- `year5`

Each time horizon should normally include:

- `focus`
- `productTheme`
- `customerKPI`
- `businessKPI`
- `milestones`

Prefer specific KPI leaves such as:

- `Activation rate`
- `Quote-to-order conversion`
- `Program go-live lead time`
- `Order completeness rate`
- `Incident recovery time`

Avoid vague KPI branch labels as terminal metrics.

### 5. Define Products And Deployment

Model both:

- `product-deployments/products.json`
- `product-deployments/deployment.json`

Use products to express the market-facing offer and deployment to express:

- channels
- user journeys or touchpoints
- APIs and events
- operating flows
- MVP scope
- stream mappings
- ownership assumptions where supported

The deployment model should make it obvious how strategy turns into operating software and operations.

### 6. Define Product Streams And Bricks

`product-bricks/product-stream.json` should contain outcome-based product streams.

Product streams should:

- express the strategic "what" rather than the implementation "how"
- connect a valuable outcome to one or more product bricks
- include required external systems when the stream depends on them
- remain durable and higher-level than the underlying brick catalog

`product-bricks/product-bricks.json` should contain the implementation-facing building blocks needed to ship the domain.

Product bricks should bridge:

- customer needs
- business outcomes
- product deployment surfaces
- concrete systems, services, APIs, workflows, and data capabilities
- team ownership

Do not define bricks as vague aspirations. They should be buildable and ownable.

### 7. Define Data Assets

`data/data-assets.json` should capture the domain data model needed by the product architecture.

For important assets, define:

- business meaning
- classification and personal-data level
- system-of-record ownership
- producing and consuming product bricks
- owner and steward teams where the schema supports it
- stores and interfaces where relevant

### 8. Add Teams

Define:

- `teams/teams.json`

For a mature domain, teams should reflect a realistic operating model:

- stream-aligned customer or value-flow teams
- platform and shared-service teams
- data and reliability functions
- trust, compliance, finance, or operational-control functions where domain-relevant

Any team referenced by product bricks, data assets, or deployment surfaces must exist in `teams.json`.

### 9. Add Competition

Define:

- `business/competition.json`

Include scope, inclusion logic, caveats, direct competitors, substitutes, adjacent platforms, official source links, and comparable business statistics where useful.

### 10. Add A Residuality Stress Test When Needed

Define optional business-context stressors in:

- `residuality/residuality.json`

For each stressor, record detection, the business attractor, the business reaction, the resulting residue, and explicit impacts on existing vision, JTBD, journey, KPI, product, product-stream, product-brick, team, and competitor ids. The app groups these as Strategy & Vision, Implementation, and Organization. Do not assign probability or likelihood. Mark looping with `status: "already-survived"` and link the earlier integrated residues through `reusesResidueIds`.

### 11. Add Icons When Needed

If the domain uses custom icon names, add matching assets under the relevant local `icons/` folder.

Do not assume the generators will repair bad filenames automatically. Keep icon names normalized and consistent.

## Quality Rules

Before generating docs, check these invariants:

- simple item ids inside domain datasets should be unique within their file and use lowercase four-letter ids where the schema allows it
- four-letter ids should reflect the item name, title, or label as closely as possible
- example: `Search Engine` -> `sren`
- domain id, names, and labels are consistent across files
- customer ids referenced elsewhere exist
- product ids referenced elsewhere exist
- team ids referenced elsewhere exist
- product-brick references such as `brickId`, `coreStreamIds`, `adjacentStreamIds`, stream dependencies, and data dependencies point to real modeled objects
- data asset owner and steward references point to real teams
- customer objects include explicit product strategy horizons, not only KPIs and JTBD
- KPI leaves are measurable and specific
- terminology is consistent across customers, products, deployments, streams, bricks, data assets, teams, and competition

Prefer concrete domain language over generic product-framework wording.

## ID Conventions

Use short, human-meaningful ids consistently across the source model.

- For simple item ids in domain datasets, use a lowercase four-letter id whenever the schema allows it.
- Keep ids unique within each file.
- Derive the four letters from the item name, title, or label as directly as possible.
- Example: `Search Engine` can become `sren`.
- Reuse the same four-letter id everywhere that item is referenced across customers, products, deployments, product bricks, data assets, and teams.

This convention is intended for local domain objects such as streams, products, customers, teams, data assets, and similar modeled entities.

Do not force this convention onto ids that already rely on a longer structured format for traceability, such as domain ids like `<domain-id>`.

## JSON Validation

Validate every JSON file you add or modify.

Recommended command:

```bash
python3 -m json.tool <path-to-file>.json
```

If changing many files, validate all touched files before generating docs.

When the domain includes linked objects across files, also validate cross-file references before calling the work complete.

## Scoped Generation Workflow

Generators typically iterate the domain list in `_wiring/product-domains/run.sh`. Do not blindly regenerate everything in a dirty worktree if the task is only about one domain.

Creating or extending source data under `_config/product-domains/<domain-id>/` does not by itself imply regenerating `docs/`. Regenerate documentation only when the user asks for it or when the task explicitly requires generated output verification.

Use a scoped workflow:

1. Read and preserve the domain definitions embedded in `_wiring/product-domains/run.sh`
2. Temporarily rewrite it to include only the target domain
3. Run the needed generator scripts
4. Restore the original config in a `finally` block

## Source Image Generation

Product-domain image generators live under `_config/scripts/image-generation/`. They write media files into the relevant domain source folders and may update JSON `media` references; they do not regenerate `docs/`.

Use an individual generator with `--dry-run` before calling an image API when scope or cost is uncertain. The Gemini wrapper can run all image generators for one domain:

```bash
export GEMINI_API_KEY=...
_config/scripts/image-generation/run.sh <domain-id>
```

For overview-only JTBD and customer-journey imagery, pass `--lightweight`. This skips new individual step/stage targets and media references while preserving any detailed media already present. Omitting the flag retains full overview-plus-detail generation:

```bash
_config/scripts/image-generation/run.sh <domain-id> --lightweight
```

See `_config/scripts/image-generation/README.md` for provider-specific commands and option details.

## Generators Commonly Used

From `_wiring/product-domains/`:

- `python3 generate-start-docs.py`
- `python3 generate-customers-docs.py`
- `python3 generate-products-docs.py`
- `python3 generate-product-bricks-docs.py`
- `python3 generate-teams-docs.py`
- `python3 generate-competition-docs.py`
- `python3 generate-residuality-docs.py`

Run only the generators relevant to the files you changed.

## When To Patch Generators

Patch generators instead of domain data when the issue is structural, cross-domain, or caused by generation logic.

Examples:

- icon filename normalization
- broken cross-link generation
- shared navigation defects
- missing rendering support for an existing source-model field

When patching a generator:

- fix the shared logic once
- regenerate only the affected domain if possible
- verify the fix in generated output

## Practical Completion Checklist

A domain is usually complete enough for review when all of the following exist:

- `start`
- `customers`
- `customers` includes `productStrategy` horizons for each substantive customer
- `product-deployments`
- `product-bricks`
- `data`
- `teams`
- `business`

And all key references resolve across:

- customers
- products
- product deployments
- product streams
- product bricks
- data assets
- teams

And the generated docs exist under:

- `docs/product-domains/<domain-id>/start/`
- `docs/product-domains/<domain-id>/customers/`
- `docs/product-domains/<domain-id>/product-deployments/`
- `docs/product-domains/<domain-id>/product-bricks/`
- `docs/product-domains/<domain-id>/teams/`
- `docs/product-domains/<domain-id>/business/`
- `docs/product-domains/<domain-id>/residuality/`

## Biases To Keep

- Prefer depth over placeholder breadth.
- Prefer measurable outcomes over framework vocabulary.
- Prefer one coherent domain model over many disconnected files.
- Prefer realistic operating structure over idealized org charts.
- Prefer scoped regeneration over full-site churn.

## Biases To Avoid

- do not treat generated HTML as the primary artifact
- do not stop at customer and product definitions without implementation and ownership grounding
- do not create teams or data assets that do not connect to product bricks and customer outcomes
- do not regenerate unrelated domains unless the user asked for it
