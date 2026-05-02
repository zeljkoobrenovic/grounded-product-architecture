---
name: team-topology-design
description: "Use when structuring stream-aligned, platform, enabling, and complicated-subsystem teams to reduce coordination overhead and keep ownership understandable."
---

# Team Topology Design

## Purpose

Choose team types and interaction patterns that fit the domain. Team topology should reduce unnecessary coordination while preserving shared standards and product coherence.

## Workflow

1. Identify streams of customer or business value that deserve stream-aligned teams.
2. Identify platform capabilities with high reuse, clear internal customers, and product-like service contracts.
3. Identify enabling teams needed for adoption, migration, data quality, compliance, or domain expertise.
4. Use complicated-subsystem teams only when specialized depth is structurally required.
5. Define dependencies and default supporting teams explicitly.

## Quality Bar

- Team type follows the work, not naming fashion.
- Platform teams have clear consumers and owned interfaces.
- Enabling teams have a transition or adoption mission, not permanent ownership ambiguity.
- Dependencies are few, understandable, and tied to real contracts or shared capabilities.
- Team topology reflects product-brick architecture.

## Repository Fit

- Use `teamType`, `teamFamilyId`, `teamFamilyName`, `dependsOnTeamIds`, and `defaultSupportingTeamIds` consistently in `teams.json`.
- Align team families with group names and product-brick root groups where practical.

## Avoid

- Creating platform teams for every technical component.
- Splitting teams by frontend/backend when the domain needs outcome ownership.
- Leaving critical shared services with no platform owner.
