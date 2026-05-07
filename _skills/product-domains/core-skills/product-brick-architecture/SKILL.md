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
4. For each brick, specify type, status, description, layered modules, dependencies, external systems, and data dependencies where the schema supports them.
5. Validate every brick can have an owning team and trace to customer or business value.

## Module Layers

Each brick uses a root-level `layers` array. Do not add root-level `interfaces` or `internalModules` fields.

```json
{
  "layers": [
    {
      "layer": "ui",
      "description": "User-facing web, mobile, backoffice, and operator experience modules.",
      "modules": [
        {
          "id": "module-customer-portal",
          "name": "Customer portal",
          "type": "web-component",
          "description": "Primary user-facing workflow surface."
        }
      ]
    },
    {
      "layer": "interfaces",
      "description": "APIs, BFFs, and explicit service boundary interfaces exposed to clients or other systems.",
      "modules": [
        {
          "id": "module-customer-api",
          "name": "Customer API",
          "type": "api",
          "description": "Programmatic access for product and partner clients."
        }
      ]
    }
  ]
}
```

Supported layers:

- `ui`: `mobile-component`, `web-component`.
- `interfaces`: `bff`, `api`, `backoffice-interface`.
- `bus`: `message-queue`, `message-consumer`, `daemon`.
- `stateless-service`: `stateless-service`; use only for orchestration services that aggregate other services without owning durable state.
- `service`: `stateful-service`, `service`.
- `integration`: `integration`.

Only include a layer when it contains modules. If a module type is ambiguous, choose the closest supported module type from the list above and keep the rest of the module metadata intact.

Each brick must have an `id`. Each module must have a short lowercase `id` that starts with `module-`, for example `module-customer-api`. Keep module IDs stable because brick-to-brick dependencies refer to them.

## Module Data And Dependencies

Modules may optionally declare data assets and dependencies:

```json
{
  "id": "module-customer-profile-service",
  "name": "Customer profile service",
  "type": "stateful-service",
  "data": [
    "customer-profile"
  ],
  "dependencies": {
    "modules": [
      "module-customer-api"
    ],
    "externalSystems": [
      "Identity Provider"
    ]
  }
}
```

Use `data` only for existing IDs from `_config/product-domains/<domain>/data/data-assets.json`. Use `dependencies.modules` for other modules in the same brick and `dependencies.externalSystems` for named external systems. Do not invent references just to fill the fields.

Brick-level `dataDependencies` reference the modules in the brick that use or own each asset. Do not use `storeIds` in product-brick data dependencies; stores belong in the data asset catalog.

```json
{
  "assetId": "customer-profile",
  "moduleIds": [
    "module-customer-profile-service"
  ],
  "role": "own",
  "description": "Acts as the primary owning brick for Customer Profile."
}
```

## Brick Dependencies

Use `brickDependencies` for dependencies between product bricks. Do not use the legacy `interface` field. Describe the dependency by module:

```json
{
  "targetBrickId": "identity",
  "moduleId": "module-identity-api",
  "sourceModuleId": "module-customer-profile-service",
  "type": "runtime-call",
  "description": "Reads account identity and entitlement state."
}
```

`sourceModuleId` identifies the module in the current brick. `moduleId` identifies the target module in `targetBrickId`.

## Metadata

The `metadata` section uses `brickTypes` and `brickStatuses` for brick-level rendering and filtering. Do not use the legacy names `types` or `statuses`.

Define module governance in `metadata.modulesConfig`:

- `layerTypes`: allowed layers with `id`, `name`, `description`, and `hostsModules`.
- `moduleTypes`: allowed module types with `id`, `name`, `description`, and `color`.

Keep `modulesConfig.layerTypes[].hostsModules` aligned with the layer assignment rules so future modules can be validated and rendered consistently.
Keep `modulesConfig.moduleTypes[].color` aligned with the product-brick palette; generated module cards and data-dependency module references use this color.

## Quality Bar

- Three-level structure is meaningful: domain/root group, subgroup, brick.
- Bricks are neither vague aspirations nor tiny implementation tasks.
- Names sound like product or platform building blocks.
- Dependencies use stable lowercase brick and module IDs.
- Modules are grouped under `layers` by architectural responsibility.
- Brick status reflects investment posture such as invest, sustaining, or sunset.

## Repository Fit

- Target file: `_config/product-domains/<domain>/product-bricks/product-bricks.json`.
- Align brick IDs with teams, capabilities, delivery, roadmap, evidence, targets, and documents.
- Product bricks should remain self-contained enough for generated static pages.

## Avoid

- Creating a flat list when the repository expects root groups and subgroups.
- Using architecture jargon without customer or operating relevance.
- Duplicating one brick across multiple groups.
