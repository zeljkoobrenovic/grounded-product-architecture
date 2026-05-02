---
name: competition-analysis
description: "Use when creating or refining business/competition.json with sourced competitors, substitutes, categories, regions, official links, metrics, and comparability caveats."
---

# Competition Analysis

## Purpose

Produce a sourced competitive landscape that supports the domain model without inventing metrics or flattening different businesses into false equivalence.

## Workflow

1. Define the competition scope: direct competitors, substitutes, regional leaders, ecosystem players, and important adjacent platforms.
2. Use official sources first: website, investor relations, annual reports, newsroom, official blog, engineering blog, LinkedIn, and regional business pages.
3. For each competitor, capture `id`, `name`, `description`, `hq`, `category`, `primary_regions`, `business_stats`, and `links`.
4. For every stat, preserve metric name, value, period, scope, source title, and source URL.
5. Add a top-level `scope` section explaining inclusion logic and metric comparability caveats.

## Quality Bar

- No business stat appears without a source URL.
- IDs are lowercase and stable.
- Descriptions explain domain relevance, not generic company identity.
- Categories distinguish global leader, regional leader, substitute, infrastructure provider, marketplace, SaaS platform, incumbent, or specialized challenger as appropriate.
- Comparability caveats are explicit when companies report different scopes.

## Repository Fit

- Target file: `_config/product-domains/<domain>/business/competition.json`.
- Keep source titles and URLs inside each metric object.
- Use the same naming and nesting conventions as mature existing domains.

## Avoid

- Inserting estimated revenue, users, GMV, or market share as if reported.
- Dropping important regional competitors because global sources are easier to find.
- Turning product claims into performance metrics.
- Using broad industry reports where an official company metric is available.
