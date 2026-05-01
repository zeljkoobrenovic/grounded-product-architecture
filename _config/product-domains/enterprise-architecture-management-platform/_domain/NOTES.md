# Working Notes

Reviewed `_config/_prompts/SKILLS.md` before modeling. The work used the skill set called out there: product domain framing, market research, customer segmentation, JTBD modeling, KPI architecture, product brick architecture, delivery model design, organizational design, and evidence-based modeling.

The shared customer prompt path named in the task, `_prompts/customers/prompt.txt`, is not present in this repository. The available prompt asset is `_config/_prompts/NEW-DOMAIN-PROMPT.md`, which mirrors the task. Customer schema and content depth were inferred from current example domains instead.

Assumptions:

- The domain is modeled as a product category rather than as one vendor, because the input listed multiple competing vendors rather than one company.
- Public financial metrics are uneven. SAP and ServiceNow report public company metrics, while most EA specialists are private and disclose customer counts, ratings, growth signals, or outcome examples rather than revenue.
- Competition statistics preserve their published reporting scope and are not normalized into domain-pure revenue.
- KPI targets are calibrated from public outcome examples and common enterprise SaaS operating targets, but they remain seed data for domain modeling rather than claimed vendor performance.

Improvement pass on 2026-05-01:

- Converted product brick and capability evidence files to the list shape expected by the product-bricks generator.
- Added focused evidence tabs for the highest-leverage bricks and all modeled product capabilities.
- Added customer persona SVG icons so generated customer, team, release, and initiative pages can use domain-specific assets instead of generic fallbacks.
