---
name: edit-evidence
description: "Create or edit evidence references that link product bricks and streams to real-world evidence (contact persons from Workday, source-code repos, AWS/GCP production resources) in _config/product-domains/<domain>/product-bricks/bricks-evidence.json and streams-evidence.json. Use when attaching evidence to a brick or stream, adding evidence groups, or writing exact or regex evidence-id patterns that resolve against the evidence database."
---

# Edit Evidence

Authoring skill for `product-bricks/bricks-evidence.json` and `streams-evidence.json`
— they attach example evidence (people, code, cloud resources) to bricks and streams,
which the evidence explorer resolves against the evidence database. Read
`.claude/skills/_references/domain-model.md` first, and **read the existing files plus
the reference domain `ride-sharing-marketplace` before editing.**

## Method (what good looks like)

- Evidence makes a brick/stream credible by pointing at concrete artifacts: people who
  work on it, repositories that implement it, cloud resources that run it.
- An `evidence-id` either matches an evidence fragment id **exactly**, or — with
  `"useRegex": true` on the group — matches a **pattern**. IDs are namespaced by
  source: `workday/…`, `aws / …`, `gcp / …`, `source-code/…`.
- Don't fabricate evidence ids; use patterns that plausibly resolve against the
  evidence database. An empty/placeholder group is better than an invented exact id.

## Exact schema (both files are a top-level **array**)

```json
[
  {
    "object-id": "trip",                     // brick id (bricks-evidence) or stream id (streams-evidence)
    "tabs": [
      {
        "label": "Example Evidence",
        "evidence-groups": [
          {
            "group-name": "Contact Persons", // seen: Contact Persons, Source Code,
            "description": "",                //        AWS Production, GCP Production
            "useRegex": true,                 // when true, ids in this group are regex patterns
            "evidence-ids": [
              { "id": "workday/Employee 000[0-9]+", "note": "early employees" }
            ]
          },
          {
            "group-name": "Source Code",
            "description": "…",
            "evidence-ids": [
              { "id": "aws / aws-nitro-enclaves-samples" },
              { "id": "aws / aws-eks-*" }
            ]
          }
        ]
      }
    ]
  }
]
```

> `evidence-ids` values are exempt from the lowercase ID rule (they may contain
> regex/path/spacing). Keep the source prefix and the surrounding format consistent
> with existing entries (note the spaced `aws / …`, `gcp / …` style this repo uses).

## Evidence sources (from `_data/evidence-db/`)

`workday` (people), `source-code` (repos), `aws-accounts`/`aws` (AWS resources),
`gcp-projects`/`gcp` (GCP resources). The database is built by
`_data/evidence-db/run.sh`, which also refreshes the evidence explorer.

## Cross-file rules to keep intact

- `object-id` in `bricks-evidence.json` → a real brick id in `product-bricks.json`.
- `object-id` in `streams-evidence.json` → a real stream id in `product-stream.json`.
- When you rename a brick/stream id, update its evidence `object-id` to match.

## After editing

1. `python3 .claude/skills/scripts/validate-domain-model.py <domain-id>`
   (JSON validity; `--strict-ids` deliberately skips `evidence-ids`).
2. Regenerate the domain docs: from `_wiring/product-domains/`,
   `python3 generate-product-bricks-docs.py <domain-id> "<Domain Name>" "<Domain description>"`.
   To refresh the standalone evidence explorer too, run `_data/evidence-db/run.sh`.
3. Report which bricks/streams gained evidence and which groups/patterns you added.

## Avoid

- An `object-id` that matches no brick/stream.
- Inventing exact evidence ids; prefer regex patterns (`useRegex: true`) when unsure.
- Inconsistent source-prefix formatting vs existing entries.
