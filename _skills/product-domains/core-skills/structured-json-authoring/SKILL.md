---
name: structured-json-authoring
description: "Use when producing valid, internally consistent JSON aligned with repository conventions, lowercase IDs, stable references, clean nesting, and consistent semantic depth."
---

# Structured JSON Authoring

## Purpose

Author JSON that is valid, stable, readable, and compatible with the repository generators. JSON is the source of truth for the static documentation site.

## Workflow

1. Inspect nearby examples and generator expectations before editing.
2. Keep all IDs lowercase, including `id`, `*Id`, and `*Ids`.
3. Use stable identifiers that will survive display-name changes.
4. Keep reference fields synchronized across files.
5. Validate with JSON parsing and targeted consistency checks before generating docs.

## Validation

For a scoped product-domain check, run:

```bash
python3 _skills/product-domains/scripts/validate-domain-model.py <domain-id>
```

Use `--strict-ids` for an additional lowercase/simple-ID pass after accounting for evidence and trace identifiers.

## Quality Bar

- JSON parses cleanly.
- IDs are lowercase and unique in their scope.
- Required references resolve.
- Nesting is consistent with the target schema.
- Content depth is even across similar objects.
- Arrays are not padded with empty or generic filler.

## Repository Fit

- Edit `_config/**` first.
- Run relevant generators only after source validation.
- Avoid touching `docs/**` directly unless explicitly requested.

## Avoid

- Ad hoc string manipulation when structured editing or validation is practical.
- Inconsistent object shapes inside the same array.
- Broken references caused by renaming IDs casually.
