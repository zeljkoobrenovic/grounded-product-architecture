# Build notes

- [x] Read `.claude` domain creation, per-artifact, validation, and balance skills and all three `.codex` GPA review skills.
- [x] Inspect `home-improvement-services-marketplace`, `general-listings-marketplace`, `ride-sharing-marketplace`, and the canonical `maas` product/deployment/team shapes.
- [x] Research the two supplied sources and supporting official product, trust, partner, and competition pages.
- [x] Establish a separate Solvari-specific boundary and register it through `start/config.json`.
- [x] Author customers, journeys, KPIs, horizons, insights, and relations.
- [x] Author product bricks, streams, data assets, products, deployment, and ownership.
- [x] Complete sourced competition and residuality scenarios.
- [x] Save the three GPA reviews and balance audit in `REVIEW.md`; resolve blocking findings.
- [x] Pass strict schema/ID validation, KPI checks, cross-file traceability, and scoped generator verification.

Source JSON is authoritative. Any generated output verification is scoped to this new domain. Existing domains and their in-progress source edits are preserved.

Registration uses the current generator's automatic discovery of `start/config.json`; no global domain list was rewritten. The start-page illustration was copied from the existing home-improvement domain icon. The source model remains independently editable; the temporary authoring helper was removed.

One shared generator correction was necessary: product-brick and stream context now resolves the current deployment mapping and the actual customer stream, while preserving legacy input support. Validation and review details are in `VALIDATION.md` and `../REVIEW.md`.
