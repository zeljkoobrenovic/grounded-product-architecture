---
name: teams-org-design
description: "Use when creating, changing, splitting, merging, staffing, or validating product teams in this repository's product-domain teams model."
---

# Teams Org Design

## Purpose

Use this project-specific skill whenever a task creates or changes teams for a product domain. The goal is to keep `_config/product-domains/<domain>/teams/teams.json` coherent with customers, product bricks, capabilities, objectives, delivery work, generated docs, and the repository's team-documentation templates.

## Trigger Examples

- Create teams for a new or existing product domain.
- Change team names, missions, team types, staffing, dependencies, or group leadership.
- Move product bricks between teams or remove duplicate ownership.
- Add or change AI agents, but only as software-development assistants.
- Regenerate or verify team documentation after source changes.

## Source Files

- Primary source: `_config/product-domains/<domain>/teams/teams.json`.
- Cross-check source: `_config/product-domains/<domain>/product-bricks/*.json`, objectives, delivery, releases, discoveries, and customer strategy files.
- Presentation source: `_templates/teams/index.html` and `_templates/teams/landing_page.html`.
- Generated output: `docs/product-domains/<domain>/teams/`.

Treat `_config/**` and `_templates/**` as editable source. Treat `docs/**` as generated output unless the user explicitly asks for a direct docs-only patch.

## Workflow

1. Inspect the current domain model before editing:
   - `teams/teams.json`
   - product-brick catalog and ownership references
   - objectives, releases, discoveries, and delivery references when team IDs may be touched.
2. Preserve stable lowercase IDs unless the user explicitly requests a rename. If renaming, update all references in the domain.
3. Keep top-level groups aligned to durable value streams, platform foundations, enabling functions, or control functions.
4. Keep teams small enough for real ownership. If a team owns unrelated surfaces, split it or make the boundary explicit.
5. Assign every owned product brick to one primary team unless the local model explicitly supports shared ownership.
6. Define each team through mission, team type, team family, owned bricks, dependencies, primary customers, staffing, and charter.
7. Add group leadership only where multiple teams need cross-team coherence; avoid making leadership a heavy program layer.
8. If adding AI agents, keep them software-development-only: backend development, frontend development, QA automation, code review, test planning, release risk, or developer workflow support. Do not add product, pricing, trust, marketing, marketplace operations, or customer-facing decision agents to teams.
9. Regenerate the scoped team docs after source/template changes.
10. Validate JSON, domain references, and generated JavaScript before finishing.

## Team Model Rules

- `teamType` should follow work shape: `stream-aligned`, `platform`, `enabling`, or a locally established type.
- `teamFamilyId` and `teamFamilyName` should group related teams without hiding ownership.
- `dependsOnTeamIds` should describe real operational or delivery dependencies, not vague collaboration.
- `defaultSupportingTeamIds` should represent recurring support relationships.
- `staffing.suggestedHeadcount` must match the sum of `staffing.roles[*].count`.
- Team missions should name owned outcomes and surfaces, not generic responsibilities.
- Team charters should include major risks, provided interfaces, dependent interfaces, and customer/KPI links where the model supports them.
- AI-agent IDs must be lowercase and scoped enough to avoid collisions. Use shared names for repeated generic agent types when the overview should aggregate them.

## Validation

After changing teams or team templates, run the narrowest useful checks:

```bash
python3 -m json.tool _config/product-domains/<domain>/teams/teams.json >/tmp/<domain>-teams.json
python3 _skills/product-domains/scripts/validate-domain-model.py <domain-id>
python3 _wiring/product-domains/generate-teams-docs.py <domain-id> "<Domain Name>" "<Domain Description>"
```

For template changes, also validate generated inline JavaScript with `node --check` when Node is available.

## Quality Bar

- The org design is understandable from the generated teams index without reading raw JSON.
- Every team has a coherent customer, product, platform, or control surface.
- Ownership changes do not strand product bricks, objectives, releases, discoveries, or dependencies.
- Staffing reflects the mission and owned surfaces instead of copying a generic role list blindly.
- AI agents support software delivery only and remain bounded by human review, tests, approvals, and production-change controls.

## Avoid

- Creating teams as a thin wrapper over an existing component list.
- Splitting frontend and backend teams when end-to-end product ownership is the better fit.
- Moving product bricks without checking downstream team, objective, release, and discovery references.
- Leaving duplicate product-brick ownership across teams.
- Adding customer-facing, marketplace, pricing, trust, or marketing AI agents into team org design.
