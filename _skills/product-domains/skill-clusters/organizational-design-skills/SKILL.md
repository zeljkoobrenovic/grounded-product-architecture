---
name: organizational-design-skills
description: "Use when a task needs the combined organization-design skill set: org design, team topology, ownership mapping, capability-to-team alignment, and coordination design."
---

# Organizational Design Skills

## Purpose

Apply the organizational design cluster when the user asks for operating model, teams, ownership, accountability, staffing, leadership, or capability-to-team alignment for a product domain.

## Core Skills To Combine

- `core-skills/organizational-design`
- `core-skills/team-topology-design`
- `core-skills/capability-mapping`
- `core-skills/product-brick-architecture`
- `core-skills/structured-json-authoring`

## Workflow

1. Start from product bricks, capabilities, customers, objectives, and delivery flows.
2. Group work into durable value streams, platform foundations, enabling functions, and control functions.
3. Assign primary ownership for every product brick.
4. Define team missions, team types, staffing, dependencies, and default supporting teams.
5. Add group leadership that improves cross-team coherence: Head of group, directors, and staff/principal ICs.
6. Validate team references, headcount, role counts, and brick ownership coverage.

## Quality Bar

- Every team owns a coherent product or platform surface.
- Every product brick has exactly one primary owning team unless the local model explicitly allows shared ownership.
- Teams are sized for clear accountability and fast decisions.
- Coordination mechanisms are explicit where platform, stream, and enabling teams interact.
- Leadership exists at group level without turning into a large program layer.

## Repository Fit

- Primary target: `_config/product-domains/<domain>/teams/teams.json`.
- Cross-check with product bricks, product capabilities, objectives, delivery releases, and discoveries.
- Regenerate team docs only after source validation.

## Avoid

- Designing teams from an org chart before understanding product-brick boundaries.
- Leaving shared platform capabilities as everyone-and-no-one ownership.
- Ignoring teams referenced in initiatives or releases.
