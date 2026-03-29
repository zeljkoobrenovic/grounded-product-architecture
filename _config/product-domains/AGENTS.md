# AGENTS.md

## Purpose

Use this folder-level guide when creating or extending any product domain under `_config/product-domains/<domain-id>/`.

This playbook captures the working pattern used to build the `bike-mobility` domain end to end:

- define the strategic model in `_config/product-domains/<domain-id>/`
- keep strategy grounded in customers, JTBD, KPIs, delivery, product bricks, and evidence
- generate the matching static documentation in `docs/product-domains/<domain-id>/`

Prefer evolving the existing model and generator conventions over inventing a new schema.

## Core Principle

Work in this sequence:

1. Domain context and external evidence
2. Customers and jobs to be done
3. KPIs and strategy horizons
4. Products and delivery structure
5. Product bricks and planning overlays
6. Delivery execution model
7. Discoveries, teams, and rituals
8. Generated documentation

Do not start from pages or visuals. Start from the source model.

## Source-First Rule

- Treat `_config/product-domains/**` as the source of truth.
- Treat `docs/product-domains/**` as generated output.
- Only patch generated docs directly if the user explicitly asks for that.
- If presentation needs to change for all domains, patch the generators or templates instead of hand-editing generated HTML.

## Recommended Domain Build Sequence

When creating a new domain, use this order unless there is a strong reason not to.

### 1. Gather domain context

Start with:

- any local seed files such as those in the `<domain-id>/_domain/` folder
- existing sibling domains with similar structure
- external primary or authoritative sources when domain understanding depends on current market, regulatory, or operational reality

Capture enough context to define:

- customer groups
- JTBD
- KPI pyramids
- product lines
- enabling product bricks
- delivery motions
- operating model assumptions

### 2. Register the domain

Update:

- `config.json`

Add the new domain entry before generating any docs. Keep the naming aligned with existing domains.

### 3. Create the base source tree

Create the minimum source package under `_config/product-domains/<domain-id>/`:

- `start/config.json`
- `customers/customers.json`
- `products/products.json`
- `product/delivery.json`
- `product-bricks/product-bricks.json`
- `product-bricks/product-capability.json`
- `product-bricks/targets.json`
- `product-bricks/documents.json`
- `product-bricks/roadmap/roadmap.json`

Treat both `products/products.json` and `product/delivery.json` as canonical source files for a complete domain unless the current generator implementation clearly expects something else.

If the repository conventions for a specific generator differ, inspect the generator first and match what it expects.

### 4. Define customers deeply

`customers/customers.json` should be substantive, not skeletal.

For each customer group, define:

- clear identity and context
- pains, needs, and constraints
- jobs to be done in operational language
- outcome expectations
- KPI pyramid with measurable leaves
- product strategy horizon or priority framing if the schema supports it

`productStrategy` should be treated as expected, not optional, for a mature domain model.

Preferred shape:

- `vision`
- `timeHorizons`
- `1_year`
- `3_year`
- `5_year`

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

Avoid vague KPI branch labels as the terminal metrics.

### 5. Define products and delivery

Model both:

- `products/products.json`
- `product/delivery.json`

Use products to express the market-facing offer and delivery to express:

- channels
- user journeys or touchpoints
- APIs and events
- operating flows
- MVP scope
- capability mappings
- ownership assumptions where supported

The delivery model should make it obvious how the strategy turns into operating software and operations.

### 6. Define product bricks

`product-bricks/product-bricks.json` should contain the implementation-facing building blocks needed to ship the domain.

Product bricks should bridge:

- customer needs
- business outcomes
- roadmap investment
- concrete systems, services, APIs, workflows, and data capabilities

Do not define bricks as vague aspirations. They should be buildable and ownable.

`product-bricks/product-capability.json` should contain the outcome-based product capabilities that those bricks enable.

Product capabilities should:

- express the strategic "what" rather than the implementation "how"
- connect a valuable outcome to one or more product bricks
- optionally include required external systems when the capability depends on them
- remain durable and higher-level than the underlying brick catalog

### 7. Add planning overlays

Complete:

- `product-bricks/targets.json`
- `product-bricks/documents.json`
- `product-bricks/roadmap/roadmap.json`

These should connect the static capability model to:

- target states
- planning priorities
- evidence and references
- sequencing and effort

### 8. Generate goals, then refine manually

Use:

- `generate-goals-datasets.py`

This can create a usable starting point, but it is not the final answer.

After generation, manually refine:

- `goals/current.json`
- `goals/next.json`
- `goals/archive.json`

Quality bar for goals:

- use concrete KPI leaves, not generic category labels
- make narratives sound like operating priorities, not template filler
- tie goals to real customer outcomes and operating constraints

### 9. Add delivery execution objects

Define:

- `delivery/initiatives.json`
- `delivery/releases.json`

These should describe concrete execution threads, not abstract themes.

Each initiative or release should have:

- a clear problem or outcome statement
- links to customer impact
- links to product bricks or delivery capabilities
- timing and sequencing context where the schema supports it

### 10. Add discoveries

Define:

- `discoveries/ongoing.json`
- `discoveries/archived.json`

Use discoveries to document:

- hypotheses
- decision-driving research
- unresolved constraints
- problem framing behind initiatives

Where possible, wire initiatives to discoveries so delivery is traceable back to evidence.

### 11. Add teams

Define:

- `teams/teams.json`

For a mature domain, teams should reflect a realistic operating model. The `bike-mobility` pattern used a domain-oriented layout with shared platform and control functions.

For a company around 500 people, think in terms of:

- market or value-stream teams
- platform and shared services
- data and reliability functions
- compliance, finance, or operational control functions where domain-relevant

Any team referenced by initiatives, delivery, or discoveries must exist in `teams.json`.

### 12. Add rituals

If the domain needs operating cadence beyond the default rituals, add:

- `rituals/meetings.json`

Use rituals for recurring cross-functional mechanisms such as:

- product triad
- delivery standup
- KPI review
- launch readiness
- operations sync
- claims or finance review
- roadmap review
- release readiness
- incident review
- quarterly planning

The rituals generator supports an optional per-domain ritual file. If absent, the default ritual set is used.

### 13. Add icons when needed

If the domain uses custom icon names, add matching assets under:

- `customers/icons/`
- `products/icons/`

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
- initiative-to-discovery links point to real discovery items
- goals link to real initiatives or releases when those connections are modeled
- product-brick references such as `brickId`, `coreCapabilityIds`, `adjacentCapabilityIds`, and target capability links point to real capabilities
- delivery and discovery team references point to real teams
- customer objects include explicit product strategy horizons, not only KPIs and JTBD
- KPI leaves are measurable and specific
- terminology is consistent across customers, products, bricks, and delivery

Prefer concrete domain language over generic product-framework wording.

## ID Conventions

Use short, human-meaningful ids consistently across the source model.

- For simple item ids in domain datasets, use a lowercase four-letter id whenever the schema allows it.
- Keep ids unique within each file.
- Derive the four letters from the item name, title, or label as directly as possible.
- Example: `Search Engine` can become `sren`.
- Reuse the same four-letter id everywhere that item is referenced across customers, products, delivery, product bricks, targets, and teams.

This convention is intended for local domain objects such as capabilities, products, customers, teams, targets, and similar modeled entities.

Do not force this convention onto ids that already rely on a longer structured format for traceability, such as:

- `initiativeId`
- `discoveryId`
- release or event ids generated from dates
- domain ids like `<domain-id>`

## JSON Validation

Validate every JSON file you add or modify.

Recommended command:

```bash
python3 -m json.tool <path-to-file>.json
```

If changing many files, validate all touched files before generating docs.

When the domain includes linked objects across files, also validate cross-file references before calling the work complete.

## Scoped Generation Workflow

Generators typically iterate all domains in `config.json`. Do not blindly regenerate everything in a dirty worktree if the task is only about one domain.

Creating or extending source data under `_config/product-domains/<domain-id>/` does not by itself imply regenerating `docs/`. Regenerate documentation only when the user asks for it or when the task explicitly requires generated output verification.

Use a scoped workflow:

1. Read and preserve the original `_config/product-domains/config.json`
2. Temporarily rewrite it to include only the target domain
3. Run the needed generator scripts
4. Restore the original config in a `finally` block

This was the safest pattern used for `bike-mobility`.

### Generators commonly used

From `docs/product-domains/`:

- `python3 generate-start-docs.py`
- `python3 generate-customers-docs.py`
- `python3 generate-products-docs.py`
- `python3 generate-product-bricks-docs.py`
- `python3 generate-goals-docs.py`
- `python3 generate-delivery-docs.py`
- `python3 generate-teams-docs.py`

From `docs/standards/`:

- `python3 generate-rituals-docs.py`

From `_config/product-domains/`:

- `python3 generate-goals-datasets.py`

Run only the generators relevant to the files you changed.

## When To Patch Generators

Patch generators instead of domain data when the issue is structural, cross-domain, or caused by generation logic.

Examples:

- shared rituals owned under standards
- icon filename normalization
- broken cross-link generation
- shared navigation defects

When patching a generator:

- fix the shared logic once
- regenerate only the affected domain if possible
- verify the fix in generated output

## Practical Completion Checklist

A domain is usually complete enough for review when all of the following exist:

- `start`
- `customers`
- `customers` includes `productStrategy` horizons for each substantive customer
- `products`
- `product`
- `product-bricks`
- `goals`
- `delivery`
- `discoveries`
- `teams`
- links to shared `standards/rituals`

And all key references resolve across:

- customers
- products
- product bricks
- goals
- initiatives and releases
- discoveries
- teams

And the generated docs exist under:

- `docs/product-domains/<domain-id>/start/`
- `docs/product-domains/<domain-id>/customers/`
- `docs/product-domains/<domain-id>/products/`
- `docs/product-domains/<domain-id>/product-bricks/`
- `docs/product-domains/<domain-id>/objectives/`
- `docs/product-domains/<domain-id>/initiatives/`
- `docs/product-domains/<domain-id>/releases/`
- `docs/product-domains/<domain-id>/discoveries/`
- `docs/product-domains/<domain-id>/teams/`
- `docs/standards/rituals/`

## Biases To Keep

- Prefer depth over placeholder breadth.
- Prefer measurable outcomes over framework vocabulary.
- Prefer one coherent domain model over many disconnected files.
- Prefer realistic operating structure over idealized org charts.
- Prefer scoped regeneration over full-site churn.

## Biases To Avoid

- do not treat generated HTML as the primary artifact
- do not stop at customer and product definitions without execution objects
- do not leave goals as auto-generated boilerplate
- do not create teams, discoveries, initiatives, and releases that do not connect to each other
- do not regenerate unrelated domains unless the user asked for it
