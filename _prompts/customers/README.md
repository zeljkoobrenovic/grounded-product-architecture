<DOMAIN-LINK> is stripe.com 

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

Expected output:

- A new folder in `_config/product-domains/<new-domain>/`
- All appropriate subfolders and files expected for a domain of this type
- Realistic seed data across the relevant JSON files
- A short summary explaining:
    - which  domain was selected
    - which existing domains were used as structural references
    - any assumptions made where public information was incomplete
