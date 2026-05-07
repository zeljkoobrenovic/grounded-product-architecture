Use `<DOMAIN-LINK>` as the target company, organization, product, or source link for the domain-definition task. Infer the most suitable product domain from that target and from public evidence.

Create a new product domain under `_config/product-domains/` for a business domain in which `<DOMAIN-LINK>` operates.

## Skill-Driven Workflow

Before authoring JSON, use the repo-local skills under `_skills/product-domains/`. If this library has been linked or installed into `${CODEX_HOME:-~/.codex}/skills`, use the auto-discovered `new-product-domain-definition` skill first and then load the named cluster/core skills as needed. Otherwise, load the files from the repository paths below.

Start with:

- `_skills/product-domains/SKILLS-OVERVIEW.md`
- `_skills/product-domains/meta-skills/new-product-domain-definition/SKILL.md`
- `_config/product-domains/AGENTS.md`

Then load only the relevant skill clusters for the phase you are working on:

1. Domain selection and evidence
   - `_skills/product-domains/skill-clusters/market-research-skills/SKILL.md`
   - `_skills/product-domains/core-skills/product-domain-framing/SKILL.md`
   - `_skills/product-domains/core-skills/competition-analysis/SKILL.md`
2. Customers and strategy
   - `_skills/product-domains/skill-clusters/product-strategy-skills/SKILL.md`
   - `_skills/product-domains/core-skills/customer-journey-design/SKILL.md`
   - `_skills/product-domains/core-skills/kpi-architecture/SKILL.md`
3. Architecture and delivery
   - `_skills/product-domains/skill-clusters/architecture-skills/SKILL.md`
   - `_skills/product-domains/core-skills/delivery-model-design/SKILL.md`
4. Goals, roadmap, and planning
   - `_skills/product-domains/skill-clusters/goal-setting-skills/SKILL.md`
   - `_skills/product-domains/skill-clusters/planning-skills/SKILL.md`
5. Teams and operating model
   - `_skills/product-domains/skill-clusters/organizational-design-skills/SKILL.md`
6. Source authoring and validation
   - `_skills/product-domains/core-skills/schema-and-repository-pattern-recognition/SKILL.md`
   - `_skills/product-domains/core-skills/structured-json-authoring/SKILL.md`
   - `_skills/product-domains/core-skills/static-documentation-modeling/SKILL.md`

Do not paste all skill content into the working context at once. Use the overview to select the next relevant skill, load it, do that phase, then continue.

## Task

1. Identify the most suitable `<DOMAIN-LINK>` product domain to model and briefly justify the choice.
2. Create a new domain folder using the same structure, naming patterns, file layout, and modeling depth used in mature existing domains under `_config/product-domains/`.
3. Infer required files, schemas, and content structure from:
   - `_config/product-domains/AGENTS.md`
   - `_skills/product-domains/meta-skills/new-product-domain-definition/SKILL.md`
   - relevant skill-cluster `SKILL.md` files
   - multiple existing example domains in `_config/product-domains/`
   - generator expectations under `_wiring/product-domains/`
4. Populate the new domain with realistic, high-quality source data that fits the repository's conventions and terminology.

## Requirements

- Start by inspecting existing domains to determine canonical folder structure and required files.
- Reuse the repository's established modeling language: customers, product strategy, delivery, objectives, teams, product bricks, product deployments, start, evidence, documents, and roadmap.
- Do not invent a new schema if an existing one already fits.
- Treat `_config/**` as the source of truth. Only create or modify generated `docs/**` when generation is explicitly requested.
- If different domains use slightly different structures, identify the most current and internally consistent pattern before creating the new one.
- Keep IDs lowercase and stable. Use short human-meaningful IDs where the schema allows it.
- Ensure all JSON is valid and references are internally consistent.

## Domain Model Requirements

### Research And Competition

- Base the domain on thorough research of `<DOMAIN-LINK>`'s business model, customer groups, marketplace dynamics, product flows, capabilities, competitors, substitutes, and monetization.
- Separate sourced facts, assumptions, and inferred judgments.
- Include competition analysis under `business/competition.json`.
- Build competition analysis from official or authoritative sources where available: company websites, investor relations pages, official press/newsroom pages, official blogs, engineering blogs, official social/company profile pages, and important regional or business pages.
- Identify key players globally and regionally, including major global leaders, strong regional leaders, substitutes, and category-specific competitors where they materially shape the landscape.
- Add a top-level `scope` section explaining inclusion logic and caveats about metric comparability.
- For every competitor, include `id`, `name`, domain-relevant `description`, `hq`, `category`, `primary_regions`, `business_stats`, and `links`.
- Do not invent business metrics. For every business stat, preserve reported metric name, value, period, scope, source title, and source URL.
- Preserve reporting scope exactly. If a company reports platform-wide, regional, or adjacent metrics, label that scope rather than rewriting it into a narrower domain claim.

### Customers, JTBD, Journeys, Strategy, And KPIs

- Define materially distinct customer groups, personas, buyers, users, operators, partners, and beneficiaries where relevant.
- Model jobs to be done as customer progress, not feature usage.
- In journey stories, define `Discovery` as how customers become aware of the product or offer before active use through channels such as search, referrals, sales outreach, app stores, partner ecosystems, procurement shortlists, internal enablement, or brand touchpoints.
- Define `Evaluation` as how customers decide whether the product is right after discovery and before trial, using alternatives, fit, value, trust, cost, adoption effort, and risk.
- Do not use `Discovery` or `Evaluation` for in-product search, browsing, or task execution.
- Define product strategy horizons for substantive customer groups: 1-year, 3-year, and 5-year focus, product theme, customer KPI, business KPI, and milestones.
- KPIs should be specific, measurable, and relevant to the domain, with realistic target values based on public information or explicit assumptions. Use a proper tree and minimize one-child branches.

### Product Capabilities, Bricks, Delivery, And Planning

- Create a three-level product-brick structure: domain/root group, group/subgroup, and brick.
- Use 20+ product bricks for a mature domain unless the scope is intentionally smaller and justified.
- Product bricks must be realistic, buildable, ownable, and connected to customer or business value.
- Give every brick an `id`. Model each brick's modules under a root-level `layers` array using `ui`, `interfaces`, `bus`, `stateless-service`, `service`, and `integration`; every module needs a short lowercase `id` starting with `module-`.
- Use only these module types: `web-component`, `mobile-component`, `bff`, `api`, `backoffice-interface`, `message-queue`, `message-consumer`, `daemon`, `stateless-service`, `stateful-service`, `service`, and `integration`.
- Model `brickDependencies` through `sourceModuleId` and target `moduleId`; do not use the legacy dependency `interface` field.
- Model product-brick `dataDependencies` with `moduleIds` listing the modules that use or own the data asset; do not use `storeIds` there.
- In product-brick metadata, use `brickTypes`, `brickStatuses`, and `modulesConfig`; include a `color` on each `modulesConfig.moduleTypes` item and do not use legacy `types` or `statuses`.
- Define product capabilities as strategic outcomes, not implementation components, and map them to product bricks and external systems where relevant.
- Model delivery through channels, interfaces, APIs, events, operational workflows, MVP scope, releases, and capability mappings.
- Add objectives, initiatives, releases, roadmap, targets, documents, discoveries, and data assets where the current domain pattern supports them.

### Teams And Operating Model

- Define a realistic operating model in `teams/teams.json`.
- Use value-stream, platform, enabling, data, reliability, compliance, finance, trust, or operational-control teams where domain-relevant.
- Ensure every product brick has a primary owning team.
- Keep team references from initiatives, delivery, releases, and discoveries resolvable.
- Keep team sizes and group leadership aligned with the current repository convention unless the user asks for a different staffing model.

## Validation Gates

Before calling the work complete:

1. Validate all changed JSON files parse.
2. Run the scoped domain validator:

   ```bash
   python3 _skills/product-domains/scripts/validate-domain-model.py <new-domain-id>
   ```

3. If changing the skill library or prompt, run:

   ```bash
   python3 _skills/product-domains/scripts/validate-skills.py
   ```

4. Run only the relevant generators if generated documentation is explicitly required.
5. Do not regenerate unrelated domains in a dirty worktree.

## Expected Output

- A new folder in `_config/product-domains/<new-domain-id>/`.
- All appropriate subfolders and source files expected for a mature domain of this type.
- Realistic seed data across relevant JSON files.
- A sourced `business/competition.json` file for the domain.
- A short summary explaining:
  - which product domain was selected
  - which existing domains were used as structural references
  - which skill clusters were used
  - any assumptions made where public information was incomplete
  - validation performed and any remaining gaps
