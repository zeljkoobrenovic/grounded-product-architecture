---
name: edit-customers
description: "Create or edit customer data for a product domain: customer groups, personas, jobs-to-be-done (JTBD), customer journey stories, KPI pyramids, per-customer product strategy, customer insights, and external reference links. Use when adding a customer segment, refining a persona, writing JTBD/journeys, building KPI pyramids, adding sourced insights, or curating external links in _config/product-domains/<domain>/customers/customers.json, insights.json, and links.json. Keeps customer IDs consistent across products, teams, and insights."
---

# Edit Customers

Authoring skill for `customers/customers.json` and `customers/insights.json`. Combines
the customer-modeling methodology with this repo's exact schema, ID wiring, and the
validate→regenerate loop. Read `.claude/skills/_references/domain-model.md` first.

Target files (per domain):
- `_config/product-domains/<domain>/customers/customers.json`
- `_config/product-domains/<domain>/customers/insights.json`
- `_config/product-domains/<domain>/customers/links.json` (optional — external reference links)
- icons in `customers/icons/`, media in `customers/media/`

**Always read the existing files and a reference domain
(`ride-sharing-marketplace`) before editing** — match its shape and depth.

## Method (what good looks like)

### Segmentation
- List every party in the value exchange: buyers, users, admins, operators,
  partners, beneficiaries, regulators.
- Group by materially different job context, risk, economics, decision process, and
  success criteria — not demographics.
- Each segment must change product strategy or capability priorities; merge any that
  don't. Avoid one generic "user" for multi-sided domains.

### Jobs-to-be-done
- Write jobs as outcome progress ("Book a reliable ride for a time-sensitive trip"),
  never "use feature X".
- Break each into real steps with decisions, frictions, and the streams/capabilities
  that support them.
- `Discovery` = awareness before use; `Evaluation` = the decide-before-trial step.
  Neither is in-product browsing/search.

### Journeys
- Separate the commercial/adoption journey from in-product task workflow.
- Cover discovery → evaluation → trial/onboarding → active use → support/recovery →
  retention/expansion. Include trust/compliance/payment moments when material.

### KPI pyramids
- A top customer outcome and (where modeled) business outcome, decomposed into
  branches with ≥2 meaningful children. Measurable leaves with units. Avoid
  one-child chains and vanity metrics. Reuse KPI **names** consistently across
  customers, teams, and insights (they link by name, not id).

### Insights (evidence)
- Record sourced facts with `sourceIds`; make inference explicit; don't invent
  metrics. Link each insight to the customers/jobs/KPIs it affects.

### External links (further reading)
- Optional `links.json` curates external pages for a reader who wants to probe the
  domain further (product surfaces, industry context, trust/safety, regulators).
- Organize links into named groups; give each link a one-sentence `relevance` that
  says *why this matters to this domain* — not a generic site description.
- Prefer primary/official sources; verify URLs resolve. Omit the file entirely if
  there is nothing worth linking — the Links tab then shows an empty state.

## Exact schema

### customers.json — top level is an **array of groups**

```json
[
  {
    "group": "Riders",
    "customers": [ { /* persona */ } ]
  }
]
```

### persona object

```json
{
  "id": "ridu",                         // lowercase short stable code
  "name": "Urban Time-Sensitive Rider",
  "description": "…",
  "icon": "ridu.png",                   // file in customers/icons/
  "careAbout": ["…"],                   // list of strings
  "winsThem": ["…"],
  "theirFear": ["…"],
  "jobsToBeDone": [ { /* jtbd */ } ],
  "customerJourneyStories": [ { /* journey */ } ],
  "kpiPyramids": { /* see below */ },
  "productStrategy": { "vision": "…", "timeHorizons": { /* 1/3/5 year */ } }
}
```

### jobsToBeDone[] item

```json
{
  "id": "book",
  "name": "Book a reliable ride for a time-sensitive trip",
  "what_it_is": "…",
  "outcome": "…",
  "steps": [
    {
      "step": "Define the trip and compare options",
      "description": "…",
      "streamsNeeded": [
        { "id": "trip", "name": "Trip Request and Intent Capture",
          "how_it_supports": "…" }
      ],
      "media": []
    }
  ],
  "media": []
}
```
> `steps[].streamsNeeded[].id` must reference a real stream id in
> `product-stream.json` (or a brick id in `product-bricks.json`). Keep `name` in sync.

### customerJourneyStories[] item

```json
{
  "id": "journey-ridu-airport",
  "name": "Airport ride without pickup friction",
  "linkedJobIds": ["book", "trust"],      // ids from this persona's jobsToBeDone
  "summary": "…",
  "stages": [ { "stage": "Discovery", "narrative": "…", "media": [] } ],
  "media": [ { "type": "image", "src": "…", "title": "…", "alt": "…" } ]
}
```

### kpiPyramids

```json
{
  "customerOutcomes": {
    "top": { "id": "rrel", "name": "Reliable on-time trip completion",
             "description": "…", "unit": "%", "currentValue": "72.5",
             "link": "…", "linkLabel": "Open KPI dashboard",
             "icon": "kpi-ridu-rrel.png" },
    "branches": [
      { "id": "rspd", "name": "Speed and predictability",
        "children": [
          { "id": "reta", "name": "ETA accuracy", "unit": "minutes",
            "children": [ { "id": "rwtm", "name": "Rider wait time",
                            "unit": "minutes", "children": [] } ] }
        ] }
    ]
  }
  // a businessOutcomes pyramid of the same shape may also be present
}
```

### productStrategy.timeHorizons (per horizon: `1_year`, `3_year`, `5_year`)

```json
{
  "focus": "…",
  "productTheme": "…",
  "customerKPI": { "northStar": "…", "supporting": ["…"] },
  "businessKPI": { "northStar": "…", "revenueStreams": ["…"], "supporting": ["…"] }
}
```
> `northStar`/`supporting` should reuse exact KPI **names** from the pyramids.

### insights.json

```json
{
  "domainId": "<domain>",
  "updated": "YYYY-MM-DD",
  "sources": [
    { "id": "uber-q4-2025", "title": "…", "url": "https://…",
      "publisher": "…", "date": "YYYY-MM-DD" }
  ],
  "items": [
    {
      "id": "rsm-01",                       // domain-prefix + number
      "title": "…", "summary": "…", "implication": "…",
      "priority": "high",                   // high | medium | low
      "tags": ["scale", "frequency"],
      "sourceIds": ["uber-q4-2025"],        // → sources[].id
      "linkedCustomers": [
        { "customerId": "ridu", "jobIds": ["book"],
          "kpis": ["Reliable on-time trip completion"] }  // kpis by NAME
      ]
    }
  ]
}
```

### links.json (optional) — external reference links

```json
{
  "domainId": "<domain>",
  "updated": "YYYY-MM-DD",
  "groups": [
    {
      "group": "Product surfaces",
      "description": "Optional one-line description of the group.",
      "links": [
        {
          "title": "How Uber works — ride options",
          "url": "https://www.uber.com/us/en/ride/how-uber-works/",
          "relevance": "Why this page matters to this domain (one sentence).",
          "tags": ["rider", "product"]          // optional
        }
      ]
    }
  ]
}
```
> Top level is an **object** with `groups[]` (not a bare array). Rendered as the
> **Links** tab in `customers/index.html`. `description` and `tags` are optional;
> `title`, `url`, and `relevance` carry the value. No cross-file ID references.

## Cross-file rules to keep intact

When you add/rename a **persona id**, update references in:
- `product-deployments/products.json` → `portfolio.products[].primaryCustomers[].id`
- `teams/teams.json` → `…teams[].primaryCustomers[].customerId`
- `customers/insights.json` → `items[].linkedCustomers[].customerId`

When you add/rename a **JTBD id**, update `linkedJobIds` in the same persona's
journeys and `jobIds` in insights. When you change a **KPI name**, update teams'
metrics, insights' `kpis`, and the persona's `productStrategy` northStar/supporting
(these link by name). When a JTBD step needs a stream that doesn't exist yet, either
add the stream (`edit-streams`) or point at an existing brick id.

## After editing

1. `python3 .claude/skills/scripts/validate-domain-model.py <domain-id> --strict-ids`
   (validator does not check customer-ID refs — verify those by hand against the
   files above, or run `audit-domain-balance`).
2. Regenerate: from `_wiring/product-domains/`,
   `python3 generate-customers-docs.py <domain-id> "<Domain Name>" "<Domain description>"`
   (name/description from `run.sh` `domains_ALL`). Generator wipes the customers docs
   folder — ensure that area's worktree is clean first.
3. Report personas/insights added or changed and which referencing files you updated.

## Avoid

- A single generic "user" segment in a multi-sided domain.
- JTBD written as feature usage, or `Discovery`/`Evaluation` used for in-product
  search/browse.
- One-child KPI chains, vanity terminal metrics, arbitrary precise targets.
- Inventing business metrics or sources; copying identical strategy horizons across
  personas.
- Leaving cross-file customer references dangling.
