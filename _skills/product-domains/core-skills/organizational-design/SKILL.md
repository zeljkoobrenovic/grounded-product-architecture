---
name: organizational-design
description: "Use when defining the team and ownership model needed to execute a domain, including responsibilities, boundaries, coordination, leadership, and accountable product areas."
---

# Organizational Design

## Purpose

Design the operating model that can execute the product domain. The organization should make ownership understandable, keep decision loops short, and align teams to customer outcomes, platform capabilities, and operational controls.

## Workflow

1. Start from customer groups, product capabilities, product bricks, roadmap, and operating constraints.
2. Define major groups around value streams, platforms, controls, or enabling functions.
3. Assign each team clear owned product bricks and supporting dependencies.
4. Add group leadership where multiple teams share outcomes: Head of group, product director, engineering director, and staff/principal IC coverage.
5. Validate team size, ownership completeness, dependency sanity, and customer/KPI alignment.

## Validation

After changing teams or product-brick ownership, run:

```bash
python3 _skills/product-domains/scripts/validate-domain-model.py <domain-id>
```

This catches missing brick owners, duplicate brick owners, broken team dependencies, oversized teams, and team role-count mismatches.

## Quality Bar

- Teams are small enough to own outcomes and make decisions.
- Every product brick has a primary owning team.
- Shared platforms exist only where reuse and leverage are real.
- Group leadership improves coherence without creating a heavy program layer.
- Team missions describe outcomes and owned surfaces, not vague responsibilities.

## Repository Fit

- Target file: `_config/product-domains/<domain>/teams/teams.json`.
- Keep IDs lowercase.
- Team references from objectives, delivery, releases, discoveries, and product bricks must resolve.

## Avoid

- Oversized teams that hide multiple products under one manager.
- Teams with no owned bricks.
- Treating all platform work as central architecture.
- Designing the org independently from roadmap and product-brick boundaries.
