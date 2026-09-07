# Validation record

Validated: 2026-09-06.

## Source integrity

```bash
python3 .claude/skills/scripts/validate-domain-model.py solvari-home-improvement-marketplace --strict-ids
python3 .claude/skills/scripts/check-kpi-pyramids.py solvari-home-improvement-marketplace
```

Both pass: 13 JSON files and 25 product bricks. The KPI checker confirms fan-out at every level, unique per-persona IDs, and resolvable strategic KPI names. All ten pyramids contain 15 nodes. Baselines remain explicitly unknown; pilot thresholds are proposed goals.

An additional source audit verified:

- Every customer is served by at least one product and team.
- Every JTBD stream reference exists and its displayed name agrees with the stream.
- All ten streams reference real bricks; every brick participates in a stream and has a deployed product.
- All 25 bricks have exactly one primary owning team; every team owns at least one brick.
- Every asset owner/steward, derived asset, and store reference resolves. Each asset has exactly one system-of-record brick, and that brick's team agrees with the asset owner.
- Product/customer names and deployment/brick names agree across files.
- Customer relations, team dependencies, insight/source joins, and residuality impact references resolve.
- Brick types and module layers use the shared vocabulary. Store classification is at least as restrictive as the assets it contains.

The deterministic validator does not enforce every invariant above; the supplementary audit is needed in addition to the standard commands.

## Generator verification

```bash
cd _wiring/product-domains
./run-one.sh solvari-home-improvement-marketplace
```

All seven generators completed. The new target folder did not exist before generation. Only this domain's generated output was created or regenerated. A start-page-only rerun copied the reused category icon; a product-bricks-only rerun verified the context renderer correction.

Generated result: **104 HTML pages**, including start, customers, product deployments, product bricks/streams/data, teams, competition, and residuality. The complete output tree also contains local icons and the repository's existing shared-data JavaScript artifact.

Verification covered local HTML asset/link existence, unresolved generator tokens, inline JavaScript syntax with `node --check`, and standalone JavaScript syntax. All brick and stream pages have nonempty product and supported-job payloads. The affiliate stream contains affiliate jobs only despite sharing platform bricks with other flows.

## Context renderer regression checks

`_wiring/product-domains/generate-product-bricks-docs.py` now reads canonical deployment `usedInProducts` links and follows JTBD-to-stream-to-brick composition. It preserves the legacy `neededStreams` path for older source packages.

Pure context functions were checked without executing generator side effects, using the new domain and small legacy/empty fixtures:

- All 25 current-schema bricks have linked products and supported customer jobs.
- Joost links to the homeowner and internal operating products and the homeowner planning job.
- Filtering the shared identity brick to the affiliate stream yields only the affiliate product and persona.
- A legacy product with a direct `neededStreams` brick reference still resolves its customer job.
- An empty product portfolio returns empty context without errors.

The generated payloads were checked after rebuilding, and `git diff --check` passes for the generator change. These checks validate source and static documentation behavior; they do not validate Solvari production systems, staffing, or KPI performance. No interactive browser rendering was performed.
