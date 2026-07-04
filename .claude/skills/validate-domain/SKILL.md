---
name: validate-domain
description: "Validate a product domain's JSON and cross-file references, then regenerate its static docs. Use after any edit under _config/product-domains/** — adding/changing customers, bricks, products, teams, streams, data assets, competition, or evidence — to confirm JSON parses, IDs are consistent, product-brick/team/module references resolve, and docs rebuild cleanly. The gate every edit-* skill calls before reporting done."
---

# Validate Domain

Run the deterministic checks and regenerate docs after editing
`_config/product-domains/**`. This is the "did I break anything" gate. Read
`.claude/skills/_references/domain-model.md` for the validate→regenerate loop.

## 1. Validate

From the repo root:

```bash
# Scoped to the domain you edited (preferred):
python3 .claude/skills/scripts/validate-domain-model.py <domain-id>

# Add the ID-format pass when you touched IDs:
python3 .claude/skills/scripts/validate-domain-model.py <domain-id> --strict-ids

# Whole-repo scan (use deliberately — older domains may have pre-existing issues):
python3 .claude/skills/scripts/validate-domain-model.py --all
```

What the validator checks:
- Every `*.json` in the domain parses.
- Product bricks: valid layers (`ui, interfaces, worker, stateless-service,
  service, integration`) and module types; module IDs start with `module-`; no
  duplicate brick/module IDs; brick/module/data dependencies resolve; no legacy
  fields (`interfaces`/`internalModules` top-level, `storeIds`, `interface`).
- `modulesConfig.layerTypes`/`moduleTypes` match the supported sets and carry colors.
- Teams: valid team `type` and dependency types vs `orgDesign`; `otherTeamDependencies`
  resolve to real teams; `brickDependencies` resolve to real bricks; non-negative
  integer headcount; no duplicate team IDs.
- `--strict-ids`: lowercase and `^[a-z0-9][a-z0-9._:-]*$` for all id/`*Id`/`*Ids`
  (skips `evidence-ids` and `keyResultId`).

**What it does NOT check** — verify these by hand or with `audit-domain-balance`:
customer-ID references in insights/products/teams, `assetId` ownership wiring,
deployment channel/environment refs, stream↔brick links, and overall realism/balance.

## 2. Fix and re-run

Address every reported error, smallest fix first, then re-run until it prints
`Domain validation passed`. If an error is in an artifact you didn't touch and is
pre-existing, say so explicitly rather than silently leaving or "fixing" it.

## 3. Regenerate docs

From `_wiring/product-domains/`. Generators wipe their target docs folder, so ensure
the worktree is clean for that area first.

```bash
cd _wiring/product-domains
# Run only the generator(s) for the artifact you changed, with the three positional
# args (id, name, description). Canonical name/description are in run.sh `domains_ALL`.
python3 generate-customers-docs.py <domain-id> "<Domain Name>" "<Domain description>"
```

Generator ↔ artifact map:

| Edited | Generator |
|---|---|
| start/config.json | generate-start-docs.py |
| customers/*.json | generate-customers-docs.py |
| product-deployments/*.json | generate-products-docs.py |
| product-bricks/*, product-stream, data-assets, *-evidence | generate-product-bricks-docs.py |
| teams/teams.json | generate-teams-docs.py |
| business/competition.json | generate-competition-docs.py |

To rebuild everything for the active domain, run `./run.sh` (regenerates the
domain(s) listed in its `domains=(...)` array, in fixed generator order).

## 4. Report

State: which domain, validator result (passed / errors fixed / pre-existing noted),
which generators ran, and which docs paths changed. Never report an edit as done
before validation passes.
