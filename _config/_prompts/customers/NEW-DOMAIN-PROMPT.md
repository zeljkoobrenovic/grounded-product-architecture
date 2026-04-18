<DOMAIN-LINK> is https://www.dmgmedia.co.uk/

Before starting, review [skills.md](./skills.md) for the capability set required to define a new product domain well. It captures the organizational design, architecture, product strategy, market research, goal setting, planning, and modeling skills this task depends on.

Create a new product domain under `_config/product-domains/` for a business domain in which <DOMAIN-LINK> operates.

Your task is to:

1. Identify the most suitable <DOMAIN-LINK> product domain to model.
2. Create a new domain folder using the same structure, naming patterns, file layout, and level of detail used in existing domains under `_config/product-domains/`.
3. Infer the required files, schemas, and content structure by combining:
    - the shared customer modeling prompt in `_prompts/customers/prompt.txt`
    - multiple existing example domains in `_config/product-domains/`
4. Populate the new domain with realistic, high-quality data that fits the repository’s conventions and terminology.

Requirements:

- Start by inspecting existing domains to determine the canonical folder structure and required files.
- Reuse the repository’s established modeling language: customers, products, delivery, objectives, teams, product-bricks, start, and related supporting files where applicable.
- create three level product bricks, domina, group and brick, 20+ bricks in total, with realistic names and descriptions that fit the chosen domain.
- Match the depth and style of the existing JSON content, not just the file names.
- KPIs should be specific, measurable, and relevant to the domain, with realistic target values based on public information about <DOMAIN-LINK> or similar businesses. Proper tree (minimize 1 child links).
- Base the new domain on thorough research of <DOMAIN-LINK>’s business model, customer groups, marketplace dynamics, product flows, capabilities, and monetization.
- Choose a domain that is clearly relevant to <DOMAIN-LINK> and justify that choice briefly in your working notes or summary.
- Do not invent a new schema if an existing one already exists in the repo.
- Treat `_config/**` as the source of truth. Only create or modify files there unless generation is explicitly required.
- If different domains use slightly different structures, identify the most current and internally consistent pattern before creating the new one.
- Ensure all JSON is valid and consistent with surrounding examples.
- Include competition analysis for the selected domain under `business/competition.json`.
- Build the competition analysis from thorough online research, using official company websites, investor relations pages, official press/newsroom pages, official blogs, official engineering blogs, and official social/company profile pages where available.
- Identify the key players in the domain globally and regionally. Include major global leaders, strong regional leaders, and important marketplace or category-specific competitors where they materially shape the competitive landscape.
- For each competitor, include:
  - `id`
  - `name`
  - short domain-relevant `description`
  - `hq`
  - competitor `category`
  - `primary_regions`
  - `business_stats` with only sourced metrics
  - `links` to relevant official properties
- Do not invent business metrics. Only include stats that can be traced to a source. Prefer official reported metrics such as revenue, gross bookings, GMV/GTV, trips/rides, users, transacting users, drivers, cities, countries, or similar operating scale indicators.
- Preserve the reporting scope of each metric exactly as reported. If a company reports platform-wide, on-demand, mobility, or regional metrics instead of domain-pure metrics, keep them and label their scope clearly rather than rewriting them into a narrower claim.
- For every business stat, include the metric name, value, period, scope, source title, and source URL.
- For every competitor, add a rich `links` object with relevant official URLs where available, such as website, investor relations, about/company page, newsroom/press page, blog, engineering blog, LinkedIn page, and important regional or business pages.
- Add a top-level `scope` section in `business/competition.json` that explains what was included, the inclusion logic used, and any caveats about metric comparability.

Expected output:

- A new folder in `_config/product-domains/<new-domain>/`
- All appropriate subfolders and files expected for a domain of this type
- Realistic seed data across the relevant JSON files
- A sourced `business/competition.json` file for the domain
- A short summary explaining:
    - which  domain was selected
    - which existing domains were used as structural references
    - any assumptions made where public information was incomplete
