# Validation record

Date: 2026-09-06. Domain: invoice-to-cash-and-credit-management.

## Repository gates

- Strict model validator: passed across all 13 JSON source files and 24 product bricks.
- KPI checker: passed. Eighteen four-level pyramids, 270 nodes, no single-child chains, unique per-persona IDs and resolvable horizon metric names.
- Scoped run-one.sh: all seven generators completed, including four validated residuality stressors.
- Source whitespace check and scoped git diff check: passed.

From the repository root, the repeatable validation commands are:

    python3 .claude/skills/scripts/validate-domain-model.py invoice-to-cash-and-credit-management --strict-ids
    python3 .claude/skills/scripts/check-kpi-pyramids.py invoice-to-cash-and-credit-management

To regenerate only this domain:

    _wiring/product-domains/run-one.sh invoice-to-cash-and-credit-management

## Additional snapshot audit

The build-time integrity audit checked customer-to-job-to-stream links, stream composition against individual flow dependencies, product/customer references, all deployed bricks and transitive product dependencies, exactly one team per brick, data system-of-record and owner agreement, stores and stewardship, insight/job/KPI references, and internal adapter connections. No orphan, duplicate ownership, unresolved reference or runtime dependency cycle remained.

Inventory: four groups, nine personas, eighteen jobs, nine adoption journeys, three products, twenty-four bricks, 105 modules, eight streams, twenty-four assets, five stores, five proposed runtime partitions, eight teams, fourteen sources and insights, twenty-three curated research links, ten landscape entries and four candidate stressors. The staffing scenario is 78 FTE including six group leadership FTE.

## Generated artifacts

Output: docs/vortexcp/invoice-to-cash-and-credit-management/

| Area | HTML pages |
|---|---:|
| Start | 1 |
| Customers | 10 |
| Products and deployment | 9 |
| Bricks, streams and data assets | 57 |
| Teams | 9 |
| Competition | 11 |
| Residuality | 1 |
| Total | 98 |

All 394 inline scripts passed JavaScript syntax compilation. All 758 static local href/src references resolve. Checked server-substitution markers are absent. The generated brick data contains the corrected external adapter dependencies.

The first link check found start/icons/logo.png missing. The existing shared repository logo was copied into the domain's source start/icons directory, then the start generator and link check were rerun successfully.

This verifies JSON integrity, generator compatibility, script syntax and static local targets. It does not claim an interactive browser test, live API behavior, operational performance, private POM architecture, independently validated market metrics or compliance certification.
