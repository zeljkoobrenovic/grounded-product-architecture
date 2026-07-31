# Product Domain Model — Shared Reference

Single source of truth for the structure, IDs, cross-file references, and the
validate→regenerate loop that every `edit-*` / `new-product-domain` skill relies on.
Skills link here instead of duplicating schema. Read this once per session before
editing any artifact.

## Repository shape

```
_config/product-domains/<domain>/   JSON source of truth (edit here)
_templates/<area>/                   HTML templates (presentation only)
_wiring/product-domains/             Python generators (logic; do not edit for content)
docs/product-domains/<domain>/       Generated output (never hand-edit)
```

Pipeline is one-directional: `_config + _templates --(Python in _wiring)--> docs`.
No framework, no build system, no npm. Generators `shutil.rmtree` their target
docs folder before rebuilding, so **never** hand-edit `docs/**`, and inspect a
dirty worktree before regenerating.

## Live artifacts (the set these skills cover)

| Artifact | File(s) | Generator |
|---|---|---|
| Start / domain config | `start/config.json` | `generate-start-docs.py` |
| Customers | `customers/customers.json`, `customers/insights.json`, `customers/links.json` | `generate-customers-docs.py` |
| Products & deployment | `product-deployments/products.json`, `deployment.json` | `generate-products-docs.py` |
| Product bricks | `product-bricks/product-bricks.json` | `generate-product-bricks-docs.py` |
| Streams | `product-bricks/product-stream.json` | `generate-product-bricks-docs.py` |
| Data assets | `data/data-assets.json` | `generate-product-bricks-docs.py` |
| Evidence | `product-bricks/bricks-evidence.json`, `streams-evidence.json` | `generate-product-bricks-docs.py` |
| Teams | `teams/teams.json` | `generate-teams-docs.py` |
| Competition | `business/competition.json` | `generate-competition-docs.py` |
| Domain brief | `_domain/DOMAIN.md` | (narrative, not generated) |

## ID conventions (enforced by `validate-domain-model.py --strict-ids`)

- Every `id`, `*Id`, `*Ids`, `objectId` value in `_config/**` is **lowercase**,
  matching `^[a-z0-9][a-z0-9._:-]*$`. Exceptions: `evidence-ids` values and
  `keyResultId` may contain regex/path-like characters.
- Customer / brick IDs are short stable codes (`ridu`, `drvu`, `trip`, `disp`).
  Stream / asset / team / insight IDs are hyphenated slugs
  (`rider-book-and-complete-a-reliable-trip`, `customer-profile`, `rider-core`,
  `rsm-01`).
- Product-brick **module** IDs must start with `module-`.
- IDs are stable: renaming an ID breaks every cross-file reference to it.

## Cross-file reference map (the integrity that must hold)

```
customers.json
  customer.id ─────────────┬─▶ insights.json     linkedCustomers[].customerId
                           ├─▶ products.json      portfolio.products[].primaryCustomers[].id
                           └─▶ teams.json         ...teams[].customerDependencies[].customerId
  jobsToBeDone[].id ───────┬─▶ insights.json     linkedCustomers[].jobIds[]
                           └─▶ customerJourneyStories[].linkedJobIds[]
  jtbd.steps[].streamsNeeded[].id ─▶ product-stream.json  stream id (or brick id)
  kpiPyramids ... names ───▶ teams.json metrics, insights kpis (by NAME, not id)

product-bricks.json
  brick.id ────────────────┬─▶ deployment.json     ...deployedBricks[].brickId
                           ├─▶ product-stream.json brickDependencies[].targetBrickId, flows steps deps
                           ├─▶ teams.json          ...brickDependencies[].brickId
                           └─▶ bricks-evidence.json object-id
  brick.dataDependencies[].assetId ─▶ data-assets.json  asset.id
  brick.layers[].modules[].id (module-*) ─▶ referenced by brickDependencies[].moduleId

product-stream.json
  stream.id ───────────────▶ streams-evidence.json object-id

products.json
  portfolio.products[].id ─▶ deployment.json ...deployedBricks[].usedInProducts[].productId

deployment.json
  channels[].channels[].deployedBricks[].brickId ─▶ product-bricks.json brick id

data-assets.json
  asset.ownerTeamId ───────▶ teams.json team id
```

When you add or rename an entity, update **every** referencing file in the same
edit. The validator catches brick/team/module breakage; customer- and
asset-level references you must check by hand (see each `edit-*` skill).

## Product-brick layer model (fixed)

`PRODUCT_BRICK_LAYER_ORDER` = `ui → interfaces → worker → stateless-service → service → integration`.

Module `type` must be one of:
`web-component, mobile-component, bff, api, backoffice-interface, message-queue,
message-consumer, daemon, stateless-service, stateful-service, service, integration`.

`metadata.modulesConfig.layerTypes` / `moduleTypes` (when present) must match these
sets exactly, and each module type needs a `color`. Source of truth:
`_wiring/product-domains/product_bricks_support.py`.

## KPI pyramid model (fixed)

`customers.json` → each persona's `kpiPyramids` holds a `customerOutcomes` and
(usually) a `businessOutcomes` pyramid. A pyramid is `top` + `branches[]`, each node
having `children[]`.

- **Shape invariant: every non-leaf node has ≥2 children; a leaf has `children: []`.
  Never exactly one child, at any level.** A `top → 1 branch → 1 child → 1 leaf` chain
  is a line, not a pyramid — the most common authoring mistake.
- **Target: 4 levels** — `top → 2 branches → 2 mid metrics each → 2 leaves each`
  (1 + 2 + 4 + 8 = 15 nodes). A 3-level `top → 2 branches → 2 leaves` is acceptable only
  when diagnostics are genuinely sparse. Don't pad with vanity metrics to hit a count.
- KPI **ids** are unique within a persona (across both pyramids). KPI **names** link by
  NAME (not id) to `teams.json` metrics, `insights.json` `kpis`, and the persona's
  `productStrategy` `northStar`/`supporting` — every such name must exist as a node in
  that persona's pyramids. The customer landing page shows "No KPI pyramid defined"
  unless BOTH pyramids are present. See `edit-customers` for the full schema.

## Validate → regenerate loop (run after every edit)

```bash
# 1. Validate JSON + cross-file references for the domain you touched
python3 .claude/skills/scripts/validate-domain-model.py <domain-id>
#    add --strict-ids for a lowercase/ID-format pass

# 2. Regenerate that domain's docs (from _wiring/product-domains/)
cd _wiring/product-domains
#    run ./run-one.sh <domain-id> (name/description come from start/config.json),
#    or run a single generator directly:
python3 generate-customers-docs.py <domain-id> "<Domain Name>" "<Domain description>"
```

> `run.sh` regenerates every domain discovered from the config tree; use `run-one.sh <domain-id>` for one domain.
> To regenerate a different domain without editing run.sh, call the relevant
> generator(s) directly with the three positional args (id, name, description) —
> the canonical name/description live in the domain's `start/config.json`.

## Reference domain

`maas` is the structural reference for **teams** and **product-deployments**
(`teams.json`, `products.json`, `deployment.json`) — it carries the canonical schema
those three files use across the repo. `ride-sharing-marketplace` is the structural
reference for the rest (customers, bricks, streams, data assets, competition) and a
good density target. `audio-streaming-platform` is an example of a **sparse** domain —
useful as a "before" for balance audits, not as a structural model.

## Working principles (apply to all edits)

- Source JSON first; presentation in templates; `docs/**` is output.
- Separate sourced facts from assumptions and inference. Don't invent business
  metrics or source-backed claims. Use official URLs for competition stats.
- Reuse existing JSON schemas and `${...}` template patterns; don't invent parallel
  structures.
- Keep domain language: customers, product deployments, product bricks, streams,
  teams, data assets, competition, and evidence.
- Every entity must earn its place — a segment/brick/team that doesn't change a
  decision should be merged or dropped.
