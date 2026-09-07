---
name: new-product-domain
description: "Author a complete, balanced, realistic product domain from scratch under _config/product-domains/<group>/<domain>/ — framing, customers, strategy, products/deployment, product bricks, streams, data assets, teams, competition, and evidence — in the right dependency order, with cross-file references kept consistent and docs regenerated. Use when creating a brand-new domain end-to-end, not editing one artifact. Orchestrates the edit-* skills and the validate/audit gates."
---

# New Product Domain (orchestrator)

End-to-end workflow for building a whole domain. It composes the per-artifact `edit-*`
skills in dependency order so cross-file references resolve as you go, and gates the
result with `validate-domain` and `audit-domain-balance`. Read
`.claude/skills/_references/domain-model.md` first.

This is a large, multi-step task — track it with a task list and build incrementally,
validating after each artifact rather than at the end.

## Before starting

- Inspect two comparable existing domains and the reference `ride-sharing-marketplace`
  for shape and density. Copy its structure, not its content.
- Targets for a **mature** domain: ~4 customer groups with real personas, 20+ bricks
  across 3 group levels, 15+ data assets, 8+ teams, 8+ competitors, 8+ sourced
  insights. A smaller domain is fine if intentional — say so.
- The new-domain prompt scaffold lives next to this skill:
  `.claude/skills/new-product-domain/NEW-DOMAIN-PROMPT.md`.

## Build order (dependencies flow downward)

Author top-to-bottom; later artifacts reference earlier IDs, so this order keeps
references resolvable.

1. **Frame & register** → `set-domain-strategy`
   - Choose an existing group or create an appropriate new group, and place the
     domain in `_config/product-domains/<group>/<domain-id>/`. Never create a domain
     directly in the source root. Keep its lowercase ID unique across all groups.
   - `_domain/DOMAIN.md`, `start/config.json` (creating `start/config.json`
     registers the domain — `run.sh` discovers domains from the config tree).
     Decide scope, value exchange, vision, 1/3/5-year horizons.
2. **Customers** → `edit-customers`
   - Groups, personas, JTBD, journeys, KPI pyramids, per-customer productStrategy,
     `insights.json`, `relations.json`. Establishes customer ids + KPI names
     everything else reuses. Journey stories use the fixed adoption stages
     (Trigger → Discovery → Evaluation → Trial → Engagement → Retention) — they
     describe adopting the product, not performing the job.
3. **Product bricks** → `edit-product-bricks`
   - Root groups → subgroups → 20+ bricks with layered modules and dependencies.
     Establishes brick ids.
4. **Streams** → `edit-streams`
   - Outcome streams + flows over the bricks; reconcile with JTBD `streamsNeeded`.
5. **Data assets** → `edit-data-assets`
   - Assets + stores + governance; wire `dataDependencies` from bricks (back-edit
     bricks if needed).
6. **Products & deployment** → `edit-products`
   - Portfolio, interfaces, `neededBricks`, and `deployment.json` channels/environments;
     reference customer ids and brick ids.
7. **Teams** → `edit-teams`
   - Org groups + teams; assign **every brick to exactly one owning team**; wire
     primary customers and data-asset `ownerTeamId` back-references.
8. **Competition** → `edit-competition`
   - Sourced landscape with official URLs.
   - Attach evidence to key bricks/streams.

## Reference-integrity pass (do this before declaring done)

Walk the spine and confirm it's unbroken (this is exactly what `audit-domain-balance`
checks):
`customer → JTBD → stream/brick → product.neededBricks → deployment → team.ownedBricks`,
plus `insight → linkedCustomers`, `brick.dataDependencies → asset`, `asset.ownerTeamId
→ team`. No orphan bricks, no unowned bricks, no dangling customer/asset/channel refs,
KPI names consistent everywhere.

## Validate & generate

1. `python3 .claude/skills/scripts/validate-domain-model.py <domain-id> --strict-ids`
   — fix every error.
2. `python3 .claude/skills/scripts/validate-skills.py` is for the skill
   library itself, not domains — skip unless editing skills.
3. Regenerate all docs for the domain: from `_wiring/product-domains/`, set
   run `./run-one.sh <domain-id>` (start → customers → products →
   product-bricks → teams → competition, in fixed order).
4. Run `audit-domain-balance <domain-id>` and resolve P1 findings before calling the
   domain done.

## Report

Summarize: scope/boundary, counts per artifact vs the mature targets, the integrity
result, the audit verdict (skeletal/partial/mature), and any intentional gaps.
