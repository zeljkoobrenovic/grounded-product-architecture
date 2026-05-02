---
name: kpi-architecture
description: "Use when designing KPI pyramids, north-star metrics, supporting metrics, diagnostic metrics, leading and lagging indicators, and target calibration."
---

# KPI Architecture

## Purpose

Create KPI pyramids that connect customer outcomes to business outcomes and diagnostic measures. The model should make tradeoffs visible and support decisions, not just list metrics.

## Workflow

1. Define a top-level customer outcome and a top-level business outcome for each segment or domain area.
2. Decompose each into branches with at least two meaningful children where possible.
3. Use measurable leaves with clear names, units, and decision relevance.
4. Include leading indicators, lagging indicators, quality/risk metrics, and diagnostic metrics.
5. Calibrate targets from research, benchmarks, or explicit assumptions.

## Quality Bar

- KPI leaves are specific, measurable, and relevant to the domain.
- The tree avoids one-child chains unless the schema or concept requires it.
- Customer and business KPIs are connected but not collapsed into one metric.
- Metrics are useful for product and operating decisions.
- Targets are realistic and not arbitrary.

## Repository Fit

- Target location is usually `kpiPyramids` in `customers/customers.json`, plus objective success criteria and scorecards.
- Use exact KPI names consistently across customers, teams, objectives, and product strategy.

## Avoid

- Generic labels such as "engagement", "efficiency", or "quality" as terminal metrics.
- Vanity metrics with no decision use.
- Unsourced precision when only directional assumptions are available.
