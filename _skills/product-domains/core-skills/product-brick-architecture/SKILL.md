---
name: product-brick-architecture
description: "Use when decomposing a domain into a three-level implementation-facing product-brick structure with clean boundaries, realistic names, dependencies, and traceability."
---

# Product Brick Architecture

## Purpose

Create the implementation-facing architecture of the product domain. Product bricks are buildable, ownable units that connect customer value, roadmap investment, delivery, systems, APIs, data, and teams.

## Workflow

1. Define root groups that reflect durable product or platform areas.
2. Define subgroups that organize related workflows, systems, or capabilities.
3. Define 20 or more realistic bricks for mature new domains unless the domain is intentionally smaller.
4. For each brick, specify type, status, description, internal modules, interfaces, dependencies, external systems, and data dependencies where the schema supports them.
5. Validate every brick can have an owning team and trace to customer or business value.

## Quality Bar

- Three-level structure is meaningful: domain/root group, subgroup, brick.
- Bricks are neither vague aspirations nor tiny implementation tasks.
- Names sound like product or platform building blocks.
- Dependencies use stable lowercase IDs and realistic interfaces.
- Brick status reflects investment posture such as invest, sustaining, or sunset.

## Repository Fit

- Target file: `_config/product-domains/<domain>/product-bricks/product-bricks.json`.
- Align brick IDs with teams, capabilities, delivery, roadmap, evidence, targets, and documents.
- Product bricks should remain self-contained enough for generated static pages.

## Avoid

- Creating a flat list when the repository expects root groups and subgroups.
- Using architecture jargon without customer or operating relevance.
- Duplicating one brick across multiple groups.
