---
name: edit-products
description: "Create or edit products and the deployment model for a product domain: the product portfolio, each product's interfaces, primary customers, needed bricks with deployment channels, and the deployment.json channel groups, sub-channels, environments, and deployed bricks. Use when adding a product, defining interfaces/availability, wiring products to bricks and deployment channels, or editing runtime/app-store/dashboard channels and environments in _config/product-domains/<domain>/product-deployments/."
---

# Edit Products & Deployment

Authoring skill for `product-deployments/products.json` and `deployment.json`.
Combines delivery/business-model methodology with this repo's exact schema and the
validate→regenerate loop. Read `.claude/skills/_references/domain-model.md` first, and
**read the existing files plus the reference domain `ride-sharing-marketplace`
(3 products, 4 channel groups) before editing.**

## Method (what good looks like)

- A **product** is a customer-facing offering with its own interfaces, customers, and
  the bricks it needs. Products compose bricks; they don't redefine them.
- Describe **channels, interfaces, availability, and rollout** — where the capability
  runs and how it ships. Name interface types by role (mobile_app, web, partner_api,
  dashboard).
- Every product traces to ≥1 primary customer and the bricks that deliver it. Every
  needed brick maps to a deployment channel + environment that actually exists.
- `deployment.json` is the menu of runtime/app-store/dashboard/partner channels and
  environments; `products.json` references into it.

## Exact schema — products.json

```json
{
  "portfolio": {
    "name": "Ride Sharing Marketplace Portfolio",
    "version": "1.0",
    "products": [
      {
        "id": "rapp",                       // lowercase short stable code
        "name": "Rider Mobility App",
        "icon": "",
        "type": "B2C Mobility",
        "primaryCustomers": [ { "id": "ridu", "name": "Urban Time-Sensitive Rider" } ],
        "interfaces": [
          { "type": "mobile_app", "name": "Rider iOS App", "description": "…",
            "users": ["Riders"], "availabilityHorizon": "live" }
        ],
        "deploymentModelRef": "deployment.json",
        "neededBricks": [
          {
            "whyNeeded": "…",
            "mappingType": "inferred_from_customer_and_bricks",
            "brickId": "trip",                       // → product-bricks.json brick id
            "brickName": "Trip Request and Intent Capture",
            "deploymentChannels": [
              {
                "deploymentUnit": "…", "pipeline": "…",
                "supportsInterfaces": ["mobile_app","partner_api"], // interface types of this product
                "deploymentChannelRef": "runtime-cloud/aws-core-runtime", // group/subChannel in deployment.json
                "deploymentEnvironmentRef": "cloud-production",           // environmentId in deployment.json
                "channelId": "be-service", "channelName": "Backend service rollout",
                "deploymentPart": "backend", "environmentName": "Cloud Production Runtime"
              }
            ]
          }
        ]
      }
    ]
  }
}
```

## Exact schema — deployment.json

```json
{
  "metadata": { "title": "…", "description": "…", "modelVersion": "…", "notes": "…" },
  "channels": [
    {
      "groupId": "runtime-cloud", "groupName": "Cloud Runtime Environments",
      "groupType": "runtime", "description": "…",
      "channels": [
        {
          "subChannelId": "aws-core-runtime", "subChannelName": "Core Cloud Runtime",
          "channelType": "public-cloud", "description": "…",
          "environments": [
            { "environmentId": "cloud-production", "environmentName": "Cloud Production Runtime",
              "description": "…", "links": [] }
          ],
          "deployedBricks": [
            { "brickId": "trip", "brickName": "Trip Request and Intent Capture",
              "deploymentRole": "…" }                // → product-bricks.json brick id
          ]
        }
      ]
    }
  ]
}
```
> `deploymentChannelRef` in products.json is `"<groupId>/<subChannelId>"`;
> `deploymentEnvironmentRef` is an `environmentId`. Both must resolve in deployment.json.

## Cross-file rules to keep intact

- `primaryCustomers[].id` → real persona id in `customers/customers.json`.
- `neededBricks[].brickId` and `deployedBricks[].brickId` → real brick id in
  `product-bricks.json` (keep `brickName` in sync). Adding a needed brick that
  doesn't exist? Create it with `edit-product-bricks` first.
- `deploymentChannelRef` / `deploymentEnvironmentRef` → existing `groupId/subChannelId`
  and `environmentId` in `deployment.json`. Add the channel/environment there before
  referencing it.
- `supportsInterfaces[]` values should match this product's `interfaces[].type`.

## After editing

1. `python3 .claude/skills/scripts/validate-domain-model.py <domain-id> --strict-ids`
   (validator checks JSON + IDs; it does NOT verify customer/brick/channel
   back-references in products — check those by hand or with `audit-domain-balance`).
2. Regenerate: from `_wiring/product-domains/`,
   `python3 generate-products-docs.py <domain-id> "<Domain Name>" "<Domain description>"`.
3. Report products/channels added or changed and the references you wired.

## Avoid

- A product that needs a brick, channel, or environment that doesn't exist.
- Duplicating brick definitions inside products (products reference bricks).
- `supportsInterfaces` values with no matching product interface.
- Inventing customers or bricks just to populate fields.
