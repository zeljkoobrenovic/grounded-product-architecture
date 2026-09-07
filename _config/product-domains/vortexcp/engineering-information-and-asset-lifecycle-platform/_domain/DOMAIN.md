# Engineering Information and Asset Lifecycle Platform

Updated: 2026-09-06

## Domain thesis and evidence boundary

This domain models the customer and delivery landscape around Assai. Engineering information must remain controlled through project delivery, handover, operations and later modifications. The boundary joins three published offers: document control in Assai DMS, connected asset context in Assai Viewport, and coordination of engineering updates in Assai Enterprise. This is sufficiently distinct from generic document storage, CAD authoring and maintenance execution to support a coherent product domain. [Assai platform](https://assai-software.com/)

Vortex records a 2019 buyout, describes support for cloud modernization and organizational development, and reports the 2024 acquisition of viewport.ai. Its profile labels Assai a current investment. These establish investment context; they do not establish Assai's present internal architecture or staffing. [Vortex investment profile](https://vortexcp.com/investment/assai/)

All customer strategies, personas, KPI trees, milestones, product bricks, module boundaries, stores, deployment boundaries, team sizes and stress-test scenarios below are analytical proposals. They are not Assai's published roadmap, organization chart, commercial terms, measured performance or production design. Product names and explicitly attributed capabilities are public facts. Undated pages are recorded with access dates in `customers/insights.json`; customer case studies remain vendor-reported examples.

## Scope and value exchange

- Core: controlled engineering documents and revisions; planned deliverables; review decisions; transmittals; supplier information; acceptance and handover; asset and tag context; information search; concurrent modifications; accountable completion of updates across systems.
- Enabling scope: identity and project permissions, source connectors, migration, customer configuration, training, service operations, evidence export, data stewardship and subscription administration.
- Adjacent systems: CAD/BIM authoring tools, EAM/CMMS applications, historians, customer identity providers, BI tools and existing document repositories. Their records retain explicit source authority.
- Excluded: CAD design authoring, physical plant control, maintenance work authorization, financial project accounting, procurement execution and autonomous engineering or statutory approval. These are external responsibilities rather than promised Assai capabilities.

Asset owners and EPC organizations are modeled as economic buyers. Document controllers, engineers and invited suppliers create or consume controlled information. Operations teams receive enduring asset value. Customer IT and implementation partners make adoption supportable. Subscription and professional-service revenue are a plausible commercial model; pricing units, contract sizes, margins and supplier charges are not established by the reviewed sources.

## Customer and strategic spine

Four groups contain eight distinct roles: asset-owner programme directors and EPC engineering managers; document controllers and supplier coordinators; maintenance engineers and information-assurance managers; enterprise application owners and implementation leads. Supplier participation is not modeled as a separate marketplace, and an assurance role does not replace an authorized engineering approver.

The vision is dependable engineering information at the point of decision, with an accountable path from the accepted document to the information used in operations. The central outcome is information readiness and trustworthy use, not document volume or AI interaction count.

1. Year 1: establish baseline measures and prove one bounded project or operating-asset use case, including migration acceptance, source permissions, exception handling and successful retrieval.
2. Year 3: reuse deliverable and configuration contracts across projects and sites; expand context to existing maintenance and engineering systems; coordinate concurrent changes.
3. Year 5: sustain verified information continuity across asset modifications, source-system replacement and organizational turnover; exercise portable exports and recovery.

Horizons run from the September 2026 modeling date. All numerical milestone targets are proposed acceptance criteria. No KPI baseline is fabricated: `currentValue` is `Not measured`. Driver trees support diagnosis; their branches are not asserted to sum arithmetically. Business cohorts are overlapping role-based views and their revenue or retention measures must not be added as separate customer populations. Customer outcome evidence, recurring revenue retention and direct service cost should be measured together.

## Architecture and delivery decisions

The model separates the controlled document record, the derived cross-system asset view, and the ledger of required change updates. A search result or linked tag does not by itself prove that an engineering change has been implemented. Conflicting concurrent modifications require accountable resolution before incorporation into the operating master. [Assai Enterprise](https://assai-software.com/platform/assai-enterprise/), [concurrent engineering](https://assai-software.com/ce-module/)

REST exchange, changed-data synchronization, Power BI extraction and scheduled file publication are supported by the integration material. Specific module APIs, event schemas, storage technologies, cloud regions and recovery objectives in this model remain design choices to validate. [Assai integrations](https://assai-software.com/platform/integrations/)

The proposed MVP is a bounded DMS project with supplier intake, governed revisions, accountable review, controlled issue and an accepted handover. Viewport can also start from existing repositories, with clear provenance and access controls. Enterprise adds named obligations and completion evidence across affected systems. Migration and adoption services are a service offer, not an asserted fourth software SKU. [Assai DMS](https://assai-software.com/platform/assai-dms/), [Viewport](https://assai-software.com/platform/assai-viewport/), [implementation services](https://assai-software.com/professional-services/implementation/)

Every brick has one primary team, at least one deployment/product mapping and an outcome stream. Logical data assets name accountable teams, producing and consuming modules, provenance and retention assumptions. Customer-owned source data and derived context are distinguished from Assai-controlled document records. Tenant/project access, source revocation, stale-data handling and human review of inferred tag associations are explicit design controls to validate, not verified vendor implementation claims.

## Operating model and assurance

Eight proposed teams cover document records, engineering collaboration, handover/change, asset context, integration/data, platform reliability, information assurance and customer enablement. Team sizes are planning assumptions for product delivery and operation, not total company headcount. Corporate sales, finance, HR and leadership outside the modeled delivery groups are excluded. Customer-side engineering sign-off and plant operating responsibilities remain external.

Assai publicly states ISO/IEC 27001 certification, SOC 2 Type II attestation and CSA STAR disclosures. The underlying certificates, report scope, exceptions and contractual assurances have not been independently reviewed here. These statements inform enterprise evaluation; they do not establish that a customer's deployment or operation complies with any particular legal requirement. Retention and residency are contract- and asset-specific assumptions, not universal country or duration claims. [Assai trust and security](https://assai-software.com/platform/security/)

## Competitive choices and structural references

Competition covers project CDEs, engineering document management, asset-information platforms and the existing SharePoint substitute. Competitor descriptions state the relevant buying alternative without inferring market share. Product-specific revenue and customer counts are omitted where the reviewed sources do not provide a comparable figure. Historic product names are retained only to explain current branding.

Structure was checked against `technical-design-collaboration-platform`, `enterprise-integration-and-data-management-platform` and the mature `ride-sharing-marketplace` reference. Products/deployment and teams follow the canonical `maas` shapes. The current per-artifact skills and generators take precedence over older prompt examples: use the `worker` layer, wire product-to-brick composition through deployment `usedInProducts`, and use team `brickDependencies` for sole primary ownership.

## Work checklist

- [x] Public research and domain boundary
- [x] Customer jobs, adoption journeys, KPI pyramids and strategy horizons
- [x] Implementation model, ownership and competition
- [x] Codex reviews and balance audit
- [x] Strict validation and scoped generated-output verification
