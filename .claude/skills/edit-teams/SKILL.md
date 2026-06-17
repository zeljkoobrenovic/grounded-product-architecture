---
name: edit-teams
description: "Create or edit the team and org model for a product domain: org design, team groups/families, individual teams, team types (stream-aligned/platform/enabling/complicated-subsystem), team charters, owned and supporting product bricks, primary customers, team dependencies, and staffing/headcount in _config/product-domains/<domain>/teams/teams.json. Use when adding a team, restructuring org groups, assigning brick ownership, or sizing teams. Keeps team IDs consistent with brick ownership and data-asset ownership."
---

# Edit Teams

Authoring skill for `teams/teams.json` — the organizational design. Combines team
topology methodology with this repo's exact schema and the validate→regenerate loop.
Read `.claude/skills/_references/domain-model.md` first, and **read the existing file
plus the reference domain `ride-sharing-marketplace` (3 groups, 10+ teams) before
editing.**

## Method (what good looks like)

- Use **team topology types**: `stream-aligned` (owns a customer/value stream),
  `platform` (provides internal products), `enabling` (uplifts other teams),
  `complicated-subsystem` (deep specialist area).
- Each team has a clear mission, owns a coherent set of **bricks**, serves **primary
  customers**, and depends on a small number of other teams. Avoid teams with no
  distinct mission or no owned bricks.
- Group teams into **families/groups** with group leadership. Keep ownership
  unambiguous: each brick is owned by exactly one team.
- Staffing is realistic (roles + counts) for the team's scope.

## Exact schema

```json
{
  "orgDesign": {
    "domainId": "…", "domainName": "…", "companyProfile": "…", "operatingModel": "…",
    "designPrinciples": [ … ], "staffingPrinciple": "…", "groupingPrinciple": "…",
    "groupLeadershipPrinciple": "…"
    // optional: "teamTypes": [{ "id": "stream-aligned", … }],
    //           "teamDependencyTypes": [{ "id": "…", … }]   (validator checks against these IF present)
  },
  "groups": [
    {
      "id": "rider-growth", "name": "Rider Growth and Trip Experience", "mission": "…",
      "groupLeadership": { "orgLayer": "group", "includedInDomainHeadcountEstimate": true,
                           "purpose": "…", "leadershipModel": "…" },
      "teams": [ { /* team */ } ],
      "groups": []                          // groups may nest
    }
  ]
}
```

### team object (canonical shape — used by 748 of the teams in the repo)

```json
{
  "id": "rider-core",                        // lowercase slug, unique across all teams
  "name": "Rider Core Experience",
  "teamType": "stream-aligned",
  "teamFamilyId": "rider-growth", "teamFamilyName": "Rider Growth and Trip Experience",
  "orgLayer": "team",
  "mission": "…",
  "teamCharter": {
    "mission": "…", "vision": "…", "customers": "…",
    "metrics": [ { "name": "Reliable on-time trip completion",   // reuse KPI names from customers.json
                   "measuring": "…", "targetValue": "…" } ],
    "strategicImportance": "…", "majorRisks": "…",
    "providedInterfaces": ["…"], "dependentInterfaces": ["…"]
  },
  "primaryCustomers": [
    { "customerId": "ridu", "customerName": "Urban Time-Sensitive Rider",
      "relatedKPIs": ["…"] }                 // customerId → customers.json persona id
  ],
  "ownedProductBricks":      [ { "brickId": "ridp", "objectId": "ridp", "brickName": "…" } ],
  "supportingProductBricks": [ { "brickId": "…",   "objectId": "…",    "brickName": "…" } ],
  "dependsOnTeamIds": ["marketplace-dispatch", "trust-ops"],     // → other team ids
  "defaultSupportingTeamIds": ["…"],
  "staffing": {
    "suggestedHeadcount": 10,
    "roles": [ { "role": "Product Manager", "count": 1, "responsibility": "…" } ],
    "staffingGuidance": "…"
  }
}
```

> **Validator note.** `validate-domain-model.py` understands an alternate (minority,
> ~legacy) team shape with `type`, `teamHeadcount.headcount`, `otherTeamDependencies[].teamId`,
> and `brickDependencies[].brickId`, and checks those against `orgDesign.teamTypes`/
> `teamDependencyTypes` when present. Prefer the **canonical shape above** to match the
> rest of the repo; if you use the validator's fields, keep `orgDesign.teamTypes`/
> `teamDependencyTypes` populated and headcount a non-negative integer. Don't mix the
> two shapes within one domain.

## Cross-file rules to keep intact

- `ownedProductBricks`/`supportingProductBricks` `brickId` → real brick ids in
  `product-bricks.json`. Every brick should be owned by exactly one team; flag
  unowned bricks and double-owned bricks.
- `primaryCustomers[].customerId` → persona ids in `customers/customers.json`;
  `relatedKPIs` and charter `metrics[].name` reuse exact KPI names.
- `dependsOnTeamIds` / `defaultSupportingTeamIds` → real team ids (no dangling refs;
  the validator catches these in its field shape).
- `data/data-assets.json` `ownerTeamId`/`stewardTeamIds` should point back at real
  team ids — wiring ownership both ways improves traceability.

## After editing

1. `python3 .claude/skills/scripts/validate-domain-model.py <domain-id> --strict-ids`
   (validator checks team uniqueness, headcount, and brick/team deps for its field
   shape; verify the canonical-shape refs and brick-ownership coverage with
   `audit-domain-balance`).
2. Regenerate: from `_wiring/product-domains/`,
   `python3 generate-teams-docs.py <domain-id> "<Domain Name>" "<Domain description>"`.
3. Report teams added or changed, brick ownership assigned, and dependencies wired.

## Avoid

- Bricks owned by zero or multiple teams.
- Teams with no owned bricks or no distinct mission.
- Dangling team/brick/customer references.
- Mixing the canonical and validator team field shapes in one domain.
- Arbitrary headcounts unmoored from the staffing roles.
