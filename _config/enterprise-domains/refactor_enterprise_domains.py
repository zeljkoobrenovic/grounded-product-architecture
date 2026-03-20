import json
import os
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parent


DOMAIN_PROFILES = {
    "emobility": {
        "description": "The eMobility enterprise architecture domain covers the business, application, data, and technology structures required to run charging networks, roaming ecosystems, driver journeys, and fleet charging operations at scale.",
        "data_domains": [
            ("party-contract", "Party and Contract", ["Customer Account", "Contract", "Partner Agreement", "Authorization Token"]),
            ("asset-site", "Asset and Site", ["Charge Point", "Connector", "Site", "Energy Constraint"]),
            ("session-transaction", "Session and Transaction", ["Charging Session", "CDR", "Tariff Event", "Settlement Item"]),
            ("telemetry-monitoring", "Telemetry and Monitoring", ["Device Event", "Alert", "Incident", "Operational KPI"])
        ],
        "technology_domains": [
            ("edge-connectivity", "Edge Connectivity", "Protocols, field connectivity, and charger integration patterns required to control and observe distributed charging infrastructure."),
            ("integration-platform", "Integration Platform", "API, event, and partner integration services that connect roaming, ERP, CRM, and external platforms."),
            ("data-analytics", "Data and Analytics Platform", "Operational telemetry, analytics, and reporting services supporting SLA, optimization, and settlement insight."),
            ("security-platform", "Security and Compliance Platform", "Identity, access, audit, and compliance controls required for regulated charging operations.")
        ]
    },
    "nutrition": {
        "description": "The Nutrition enterprise architecture domain covers the business, application, data, and technology structures needed to design, manufacture, govern, and improve nutrition solutions under strict quality and compliance constraints.",
        "data_domains": [
            ("party-commercial", "Party and Commercial", ["Customer", "Account", "Commercial Agreement", "Channel"]),
            ("product-formula", "Product and Formula", ["Formula", "Ingredient", "Nutritional Profile", "Label Artifact"]),
            ("batch-quality", "Batch and Quality", ["Batch", "Specification", "Quality Result", "Deviation"]),
            ("supply-evidence", "Supply and Evidence", ["Supplier", "Inventory Position", "Regulatory Evidence", "Audit Record"])
        ],
        "technology_domains": [
            ("manufacturing-integration", "Manufacturing Integration", "Interfaces and orchestration patterns connecting product design, production, and quality systems."),
            ("master-data", "Master Data and Governance", "Reference data, specification governance, and evidence controls for compliant product operations."),
            ("analytics-platform", "Analytics and Insight Platform", "Traceability, sustainability, quality, and operational reporting capabilities."),
            ("security-controls", "Security and Control Services", "Access, segregation-of-duties, audit, and compliance services for regulated operations.")
        ]
    },
    "real-estate-marketplace": {
        "description": "The Real Estate Marketplace enterprise architecture domain covers the business, application, data, and technology structures required to operate property discovery, listing, matching, partner, and transaction workflows.",
        "data_domains": [
            ("party-profile", "Party and Profile", ["Seeker Profile", "Owner Profile", "Agent Profile", "Partner Profile"]),
            ("property-listing", "Property and Listing", ["Property", "Listing", "Availability", "Listing Content"]),
            ("lead-engagement", "Lead and Engagement", ["Search Query", "Lead", "Inquiry", "Appointment"]),
            ("transaction-contract", "Transaction and Contract", ["Offer", "Agreement", "Fee Item", "Transaction Status"])
        ],
        "technology_domains": [
            ("experience-platform", "Experience Platforms", "Web, mobile, search, and personalization services supporting marketplace engagement."),
            ("integration-ecosystem", "Partner and Ecosystem Integration", "APIs, feeds, and workflow integration services connecting intermediaries and partners."),
            ("content-data", "Content and Data Platform", "Search indexing, listing content, analytics, and reporting services supporting marketplace insight."),
            ("security-trust", "Security and Trust Services", "Identity, consent, fraud, and audit controls for trusted digital marketplace operations.")
        ]
    },
    "dkv": {
        "description": "The DKV enterprise architecture domain covers the business, application, data, and technology structures required to support fleet mobility, payment, tolling, charging, and merchant ecosystem operations.",
        "data_domains": [
            ("account-contract", "Account and Contract", ["Fleet Account", "Driver", "Merchant", "Commercial Agreement"]),
            ("mobility-transaction", "Mobility and Transaction", ["Fuel Transaction", "Charging Session", "Toll Event", "Invoice Item"]),
            ("network-location", "Network and Location", ["Merchant Site", "Station", "Acceptance Network", "Route Corridor"]),
            ("risk-compliance", "Risk and Compliance", ["Tax Artifact", "Fraud Signal", "Dispute", "Audit Record"])
        ],
        "technology_domains": [
            ("mobility-integration", "Mobility Integration Platform", "Connectivity patterns for merchants, charging networks, tolling, and fleet systems."),
            ("transaction-platform", "Transaction and Settlement Platform", "Core services for authorization, rating, settlement, and reconciliation."),
            ("data-insight", "Data and Insight Services", "Operational, fiscal, and commercial reporting services supporting mobility operations."),
            ("identity-security", "Identity and Security Services", "Card, token, access, and compliance controls across the mobility ecosystem.")
        ]
    },
    "arrive": {
        "description": "The Arrive enterprise architecture domain covers the business, application, data, and technology structures required to operate parking discovery, booking, access control, and partner mobility workflows.",
        "data_domains": [
            ("party-vehicle", "Party and Vehicle", ["Driver", "Operator", "Vehicle", "Permit"]),
            ("inventory-availability", "Inventory and Availability", ["Parking Asset", "Space Inventory", "Availability Window", "Rate Plan"]),
            ("booking-access", "Booking and Access", ["Reservation", "Access Event", "Session", "Violation"]),
            ("payment-settlement", "Payment and Settlement", ["Payment", "Invoice", "Settlement Record", "Chargeback"])
        ],
        "technology_domains": [
            ("experience-access", "Experience and Access Platform", "Digital channels and access-control services supporting end-to-end parking journeys."),
            ("partner-integration", "Partner Integration Platform", "Interfaces and orchestration services linking operators, cities, fleets, and partners."),
            ("analytics-optimization", "Analytics and Optimization Services", "Demand, utilization, pricing, and operational insight services."),
            ("security-resilience", "Security and Resilience Services", "Identity, fraud, observability, and continuity controls for high-volume mobility operations.")
        ]
    },
    "internal": {
        "description": "The Internal enterprise architecture domain covers the business, application, data, and technology structures used by internal teams to run governance, operations, analytics, support, and enabling business services.",
        "data_domains": [
            ("employee-access", "Employee and Access", ["Employee", "Role", "Entitlement", "Approval"]),
            ("work-service", "Work and Service", ["Ticket", "Case", "Project", "Knowledge Item"]),
            ("finance-procurement", "Finance and Procurement", ["Vendor", "Purchase Order", "Invoice", "Cost Center"]),
            ("performance-risk", "Performance and Risk", ["KPI", "Control Result", "Exception", "Audit Artifact"])
        ],
        "technology_domains": [
            ("enterprise-workflow", "Enterprise Workflow Platform", "Workflow, ticketing, approvals, and automation services supporting shared services."),
            ("integration-data", "Integration and Data Platform", "Shared integration, reporting, and analytics services for enterprise operations."),
            ("identity-governance", "Identity and Governance Services", "Access, policy, and evidence services supporting secure internal operations."),
            ("collaboration-platform", "Collaboration and Productivity Services", "Knowledge, communication, and document-management capabilities.")
        ]
    },
    "mambu": {
        "description": "The Mambu enterprise architecture domain covers the business, application, data, and technology structures required to operate cloud-native banking, lending, servicing, and partner ecosystem capabilities.",
        "data_domains": [
            ("party-customer", "Party and Customer", ["Customer", "Organization", "Relationship", "Consent"]),
            ("product-ledger", "Product and Ledger", ["Loan Product", "Deposit Product", "Ledger Account", "Interest Rule"]),
            ("transaction-servicing", "Transaction and Servicing", ["Transaction", "Repayment Schedule", "Case", "Delinquency Event"]),
            ("risk-compliance", "Risk and Compliance", ["Risk Assessment", "KYC Record", "Control", "Regulatory Report"])
        ],
        "technology_domains": [
            ("banking-platform", "Banking Platform Services", "Core banking, servicing, and rules-processing services supporting digital financial products."),
            ("ecosystem-integration", "Ecosystem Integration Platform", "Partner APIs, eventing, and orchestration for fintech and institutional integration."),
            ("data-insight", "Data and Insight Services", "Analytical, regulatory, and operational reporting services across banking products."),
            ("security-compliance", "Security and Compliance Services", "Identity, audit, control, and regulatory services supporting financial operations.")
        ]
    }
}


ARCHITECTURE_RITUALS = {
    "schemaVersion": "1.0",
    "scope": "enterprise-architecture-practice",
    "description": "Core recurring meetings that support architecture vision, business alignment, solution governance, and change management in a classical enterprise architecture practice.",
    "meetings": [
        {
            "id": "architecture-vision-workshop",
            "title": "Architecture Vision Workshop",
            "category": "architecture-vision",
            "description": "A cross-functional workshop that frames the business problem, architecture scope, stakeholders, and target-state intent for a material change initiative.",
            "goal": "Create a shared architecture vision before detailed design work starts.",
            "participants": {"required": ["Lead Enterprise Architect", "Business Sponsor", "Domain Architect"], "optional": ["Product Lead", "Security Architect", "Data Architect"]},
            "owner": "Lead Enterprise Architect",
            "cadence": "per-major-change",
            "durationMinutes": 120,
            "format": "workshop",
            "inputs": ["Business drivers", "Current-state pain points", "Strategic priorities", "Change requests"],
            "outputs": ["Architecture vision", "Scope boundaries", "Stakeholder map", "High-level target state"]
        },
        {
            "id": "business-capability-review",
            "title": "Business Capability Review",
            "category": "business-architecture",
            "description": "A review of business capabilities, process pain points, ownership gaps, and target operating model changes.",
            "goal": "Keep business architecture aligned with enterprise priorities and accountable ownership.",
            "participants": {"required": ["Business Architect", "Domain Architect", "Business Owners"], "optional": ["Process Owner", "Data Architect"]},
            "owner": "Business Architect",
            "cadence": "monthly",
            "durationMinutes": 90,
            "format": "review",
            "inputs": ["Capability map", "Process issues", "Operating model changes"],
            "outputs": ["Capability updates", "Ownership clarifications", "Transformation candidates"]
        },
        {
            "id": "architecture-board",
            "title": "Architecture Review Board",
            "category": "governance",
            "description": "A formal governance forum for reviewing significant architecture decisions, exceptions, standards deviations, and target-state alignment.",
            "goal": "Provide consistent architectural decision-making and controlled deviations from standards.",
            "participants": {"required": ["Chief Architect", "Enterprise Architects", "Domain Architects"], "optional": ["Security Architect", "Platform Lead", "Delivery Lead"]},
            "owner": "Chief Architect",
            "cadence": "biweekly",
            "durationMinutes": 90,
            "format": "decision-review",
            "inputs": ["Architecture proposals", "Decision records", "Exception requests", "Standards impacts"],
            "outputs": ["Approved decisions", "Rejected options", "Exceptions with conditions", "Follow-up actions"]
        },
        {
            "id": "data-governance-council",
            "title": "Data Governance Council",
            "category": "data-architecture",
            "description": "A governance forum for data ownership, quality, master data boundaries, and information lifecycle controls.",
            "goal": "Improve data consistency, stewardship, and compliance across enterprise domains.",
            "participants": {"required": ["Data Architect", "Data Owner", "Domain Architect"], "optional": ["Security Lead", "Analytics Lead", "Operations Lead"]},
            "owner": "Lead Data Architect",
            "cadence": "monthly",
            "durationMinutes": 90,
            "format": "governance-review",
            "inputs": ["Data quality issues", "Data model changes", "Stewardship concerns", "Regulatory requirements"],
            "outputs": ["Data ownership decisions", "Model governance actions", "Priority remediation items"]
        },
        {
            "id": "technology-standards-review",
            "title": "Technology Standards Review",
            "category": "technology-architecture",
            "description": "A review of platform standards, reference technologies, integration patterns, and lifecycle risks.",
            "goal": "Maintain a coherent and supportable technology architecture over time.",
            "participants": {"required": ["Technology Architect", "Platform Lead", "Security Architect"], "optional": ["Domain Architect", "Operations Lead"]},
            "owner": "Lead Technology Architect",
            "cadence": "monthly",
            "durationMinutes": 60,
            "format": "standards-review",
            "inputs": ["Reference architectures", "Technology lifecycle status", "Platform constraints", "Risk register"],
            "outputs": ["Updated standards", "Retirement decisions", "Guardrail changes"]
        },
        {
            "id": "implementation-governance-checkpoint",
            "title": "Implementation Governance Checkpoint",
            "category": "implementation-governance",
            "description": "A checkpoint during delivery to confirm that implementation remains aligned with the approved target architecture and agreed constraints.",
            "goal": "Reduce architecture drift during execution and expose deviations early.",
            "participants": {"required": ["Domain Architect", "Delivery Lead", "Tech Lead"], "optional": ["Security Architect", "Data Architect"]},
            "owner": "Domain Architect",
            "cadence": "monthly",
            "durationMinutes": 60,
            "format": "checkpoint",
            "inputs": ["Approved architecture decisions", "Implementation status", "Deviation log", "Open risks"],
            "outputs": ["Alignment assessment", "Required corrections", "Accepted deviations"]
        },
        {
            "id": "portfolio-architecture-review",
            "title": "Portfolio Architecture Review",
            "category": "portfolio-governance",
            "description": "A portfolio-level view of major change initiatives, transition architectures, dependencies, and sequencing risks.",
            "goal": "Align enterprise change across domains rather than optimizing individual programs in isolation.",
            "participants": {"required": ["Chief Architect", "Portfolio Lead", "Domain Architects"], "optional": ["Business Sponsor", "Finance Lead", "Program Lead"]},
            "owner": "Chief Architect",
            "cadence": "quarterly",
            "durationMinutes": 120,
            "format": "portfolio-review",
            "inputs": ["Roadmaps", "Transition architectures", "Dependency map", "Investment priorities"],
            "outputs": ["Sequencing decisions", "Dependency escalations", "Portfolio architecture actions"]
        },
        {
            "id": "architecture-retrospective",
            "title": "Architecture Retrospective",
            "category": "change-management",
            "description": "A retrospective on architecture decisions, governance effectiveness, and implementation outcomes after major releases or transformation milestones.",
            "goal": "Turn architecture work into reusable learning and improve the architecture practice itself.",
            "participants": {"required": ["Enterprise Architect", "Domain Architect", "Delivery Lead"], "optional": ["Business Owner", "Security Architect", "Operations Lead"]},
            "owner": "Lead Enterprise Architect",
            "cadence": "quarterly",
            "durationMinutes": 90,
            "format": "retrospective",
            "inputs": ["Delivered outcomes", "Decision history", "Issues encountered", "Post-implementation findings"],
            "outputs": ["Lessons learned", "Practice improvements", "Updated principles or templates"]
        }
    ]
}


GOVERNANCE_FORUMS = [
    "Architecture Review Board",
    "Data Governance Council",
    "Technology Standards Review",
    "Portfolio Architecture Review"
]


def slugify(text):
    value = (text or "").strip().lower()
    chars = []
    last_dash = False
    for ch in value:
        if ch.isalnum():
            chars.append(ch)
            last_dash = False
        elif not last_dash:
            chars.append("-")
            last_dash = True
    return "".join(chars).strip("-")


def title_case(text):
    parts = str(text or "").replace("_", " ").replace("-", " ").split()
    return " ".join(word[:1].upper() + word[1:] for word in parts)


def load_json(path, default):
    if path.exists():
        with path.open() as handle:
            return json.load(handle)
    return default


def write_json(path, payload):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w") as handle:
        json.dump(payload, handle, indent=2)
        handle.write("\n")


def domain_root(domain_id):
    return ROOT / domain_id


def load_product_led_inputs(domain_id):
    root = domain_root(domain_id)
    customers = load_json(root / "customers" / "customers.json", [])
    products = load_json(root / "products" / "products.json", {"portfolio": {"products": []}})
    bricks = load_json(root / "product-bricks" / "product-bricks.json", [])
    initiatives = load_json(root / "delivery" / "initiatives.json", {"items": []})
    releases = load_json(root / "delivery" / "releases.json", {"items": []})
    goals = {
        "current": load_json(root / "goals" / "current.json", {"goals": []}),
        "next": load_json(root / "goals" / "next.json", {"goals": []}),
        "archive": load_json(root / "goals" / "archive.json", {"goals": []})
    }
    return customers, products, bricks, initiatives, releases, goals


def derive_actors(customers):
    actors = []
    stakeholders = []
    for group in customers:
        group_id = slugify(group.get("group", "stakeholders"))
        actors.append({
            "id": f"actor-{group_id}",
            "name": group.get("group", "Stakeholders"),
            "type": "business-actor",
            "description": f"Represents the {group.get('group', 'stakeholder')} business constituency within the enterprise architecture scope."
        })
        for customer in group.get("customers", [])[:3]:
            stakeholders.append({
                "id": customer.get("id", slugify(customer.get("name", "stakeholder"))),
                "name": customer.get("name", "Stakeholder"),
                "concern": customer.get("description", ""),
                "mapsToActor": f"actor-{group_id}"
            })
    return actors, stakeholders


def derive_capabilities(bricks, products):
    seen = set()
    capabilities = []
    index = 1
    for brick in bricks:
        name = title_case(brick.get("group") or brick.get("domain") or brick.get("name"))
        key = slugify(name)
        if not key or key in seen:
            continue
        seen.add(key)
        capabilities.append({
            "id": f"cap-{index}",
            "name": name,
            "description": f"Business capability centered on {name.lower()} within the domain operating model.",
            "maturityTarget": "managed",
            "realizedBy": []
        })
        index += 1
        if len(capabilities) >= 8:
            break
    if not capabilities:
        for product in products.get("portfolio", {}).get("products", [])[:5]:
            capabilities.append({
                "id": f"cap-{index}",
                "name": product.get("name", "Domain Capability"),
                "description": f"Business capability enabling {product.get('name', 'core domain operations')}.",
                "maturityTarget": "managed",
                "realizedBy": []
            })
            index += 1
    return capabilities


def derive_business_services(products):
    services = []
    for idx, product in enumerate(products.get("portfolio", {}).get("products", []), start=1):
        services.append({
            "id": f"service-{idx}",
            "name": product.get("name", f"Service {idx}"),
            "description": product.get("type", "Domain business service"),
            "supportedByApplications": [product.get("id", f"app-{idx}")],
            "channels": [interface.get("name", "") for interface in product.get("interfaces", [])]
        })
    return services


def derive_value_streams(customers, products):
    streams = []
    added = set()
    for group in customers:
        for customer in group.get("customers", []):
            for jtbd in customer.get("jobsToBeDone", [])[:1]:
                stream_name = jtbd.get("name", "Operational Value Stream")
                key = slugify(stream_name)
                if key in added:
                    continue
                added.add(key)
                streams.append({
                    "id": key,
                    "name": stream_name,
                    "description": jtbd.get("what_it_is", ""),
                    "stages": [
                        {"name": step.get("step", "Stage"), "description": step.get("description", "")}
                        for step in jtbd.get("steps", [])[:5]
                    ]
                })
                if len(streams) >= 4:
                    return streams
    if not streams:
        for product in products.get("portfolio", {}).get("products", [])[:3]:
            streams.append({
                "id": slugify(product.get("name", "value-stream")),
                "name": product.get("name", "Value Stream"),
                "description": f"End-to-end value stream supported by {product.get('name', 'the domain application landscape')}.",
                "stages": [
                    {"name": "Intake", "description": "Business demand, request, or transaction enters the domain."},
                    {"name": "Orchestration", "description": "Core domain services coordinate the required processing and decisions."},
                    {"name": "Fulfillment", "description": "The requested business outcome is delivered and recorded."},
                    {"name": "Control", "description": "Operational, financial, and compliance controls are applied."}
                ]
            })
    return streams


def derive_application_architecture(products, business_services):
    components = []
    interactions = []
    for idx, product in enumerate(products.get("portfolio", {}).get("products", []), start=1):
        components.append({
            "id": product.get("id", f"app-{idx}"),
            "name": product.get("name", f"Application {idx}"),
            "type": product.get("type", "application-component"),
            "description": f"Application component supporting the {product.get('name', 'domain')} service landscape.",
            "supportsBusinessServices": [service["id"] for service in business_services if service["name"] == product.get("name")],
            "applicationServices": [
                {
                    "id": f"{product.get('id', f'app-{idx}')}-svc-{service_idx}",
                    "name": interface.get("name", interface.get("type", "Interface")),
                    "channelType": interface.get("type", ""),
                    "description": interface.get("description", "")
                }
                for service_idx, interface in enumerate(product.get("interfaces", []), start=1)
            ]
        })
    for left, right in zip(components, components[1:]):
        interactions.append({
            "source": left["id"],
            "target": right["id"],
            "relationship": "serves-and-exchanges-information-with",
            "description": f"{left['name']} exchanges domain information with {right['name']} as part of the end-to-end operating model."
        })
    return {"applicationComponents": components, "applicationInteractions": interactions}


def derive_data_architecture(domain_id, products):
    profile = DOMAIN_PROFILES[domain_id]
    components = [item.get("id", "") for item in products.get("portfolio", {}).get("products", [])]
    data_domains = []
    for idx, (data_id, name, entities) in enumerate(profile["data_domains"], start=1):
        data_domains.append({
            "id": data_id,
            "name": name,
            "description": f"Logical data domain governing {name.lower()} information within the enterprise architecture scope.",
            "informationObjects": entities,
            "systemOfRecordPattern": components[idx - 1] if idx - 1 < len(components) else "shared-domain-platform"
        })
    return {
        "schemaVersion": "1.0",
        "perspective": "data-architecture",
        "dataPrinciples": [
            "Data ownership must be explicit at the domain level.",
            "Master data should be shared through governed interfaces rather than copied ad hoc.",
            "Analytical use of data must be traceable to operational sources.",
            "Sensitive information must be classified and protected according to policy."
        ],
        "dataDomains": data_domains
    }


def derive_technology_architecture(domain_id, bricks):
    profile = DOMAIN_PROFILES[domain_id]
    brick_names = [brick.get("name", "") for brick in bricks[:12]]
    technology_domains = []
    for tech_id, name, description in profile["technology_domains"]:
        technology_domains.append({
            "id": tech_id,
            "name": name,
            "description": description,
            "enablingBuildingBlocks": brick_names[:4] if brick_names else [],
            "standardsProfile": ["Security by design", "API-first integration", "Observable operations", "Lifecycle-managed platforms"]
        })
        brick_names = brick_names[2:] if len(brick_names) > 2 else brick_names
    return {
        "schemaVersion": "1.0",
        "perspective": "technology-architecture",
        "technologyDomains": technology_domains,
        "crossCuttingServices": [
            "Identity and access management",
            "Integration and eventing",
            "Observability and operational telemetry",
            "Security, compliance, and audit"
        ]
    }


def derive_motivation(domain, stakeholders, goals):
    current_goals = goals.get("current", {}).get("goals", [])
    next_goals = goals.get("next", {}).get("goals", [])
    architecture_goals = []
    for goal in (current_goals + next_goals)[:6]:
        architecture_goals.append({
            "id": goal.get("id", slugify(goal.get("title", "goal"))),
            "name": goal.get("title", "Architecture Goal"),
            "description": goal.get("objective", ""),
            "horizon": goal.get("period", {}).get("quarter", "")
        })
    if not architecture_goals:
        architecture_goals.append({
            "id": f"{domain['id']}-target-operating-model",
            "name": f"{domain['name']} Target Operating Model",
            "description": f"Establish a coherent target operating model across business, application, data, and technology layers for {domain['name']}.",
            "horizon": "rolling"
        })
    return {
        "schemaVersion": "1.0",
        "perspective": "motivation",
        "architectureVision": {
            "statement": f"Enable {domain['name']} through an integrated enterprise architecture spanning business, application, data, and technology domains.",
            "drivers": [
                "Reduce fragmentation across organizational and technology change.",
                "Make dependencies and ownership explicit across architecture layers.",
                "Improve governance of strategic change and target-state decisions."
            ],
            "goals": architecture_goals,
            "principles": [
                "Business capabilities drive application and technology design.",
                "Information is modeled as a shared enterprise asset.",
                "Technology choices should be standardized unless a domain-specific need justifies variation.",
                "Implementation should be governed against explicit target and transition architectures."
            ],
            "stakeholders": stakeholders[:8]
        }
    }


def derive_business_architecture(domain_id, actors, business_services, capabilities, value_streams):
    return {
        "schemaVersion": "1.0",
        "perspective": "business-architecture",
        "businessActors": actors,
        "businessCapabilities": capabilities,
        "businessServices": business_services,
        "valueStreams": value_streams,
        "operatingModelNotes": [
            f"{DOMAIN_PROFILES[domain_id]['description']}",
            "Business capabilities should be mapped to accountable owners and supported by governed application services.",
            "Cross-domain dependencies should be handled through explicit value streams and service contracts."
        ]
    }


def derive_implementation(initiatives, releases):
    items = sorted(initiatives.get("items", []), key=lambda item: item.get("date", ""))
    rel_items = sorted(releases.get("items", []), key=lambda item: item.get("date", ""))
    work_packages = []
    for idx, item in enumerate(items[:6], start=1):
        work_packages.append({
            "id": f"wp-{idx}",
            "name": item.get("description", f"Work Package {idx}")[:140],
            "type": "architecture-work-package",
            "targetDate": item.get("date", ""),
            "impactedBuildingBlocks": [brick.get("brickId", "") for brick in item.get("productBricks", [])[:4]],
            "deliveryTouchpoints": [channel.get("channelId", "") for channel in item.get("deliveryChannels", [])[:4]]
        })
    if not work_packages:
        work_packages.append({
            "id": "wp-1",
            "name": "Establish baseline, target, and transition architectures",
            "type": "architecture-work-package",
            "targetDate": "",
            "impactedBuildingBlocks": [],
            "deliveryTouchpoints": []
        })
    return {
        "schemaVersion": "1.0",
        "perspective": "implementation-and-migration",
        "transitionArchitectures": [
            {"name": "Baseline Architecture", "focus": "Current-state applications, data domains, and technology patterns."},
            {"name": "Transition Architecture", "focus": "Sequenced change packages reducing fragmentation and target-state gaps."},
            {"name": "Target Architecture", "focus": "Coherent business, application, data, and technology landscape."}
        ],
        "workPackages": work_packages,
        "releaseMilestones": [
            {"date": item.get("date", ""), "name": item.get("description", "")[:120]}
            for item in rel_items[:6]
        ],
        "governanceCheckpoints": [
            "Architecture vision approval",
            "Domain architecture review",
            "Implementation governance checkpoint",
            "Post-implementation architecture review"
        ]
    }


def derive_governance(domain):
    return {
        "schemaVersion": "1.0",
        "perspective": "architecture-governance",
        "roles": [
            {"name": "Enterprise Architect", "responsibility": f"Maintains enterprise-wide consistency across the {domain['name']} architecture landscape."},
            {"name": "Domain Architect", "responsibility": f"Owns the target and transition architectures for {domain['name']}."},
            {"name": "Business Owner", "responsibility": "Provides business accountability for capability and process decisions."},
            {"name": "Technology Owner", "responsibility": "Owns platform standards, lifecycle, and technical risk posture."}
        ],
        "forums": GOVERNANCE_FORUMS,
        "decisionRights": [
            "Architecture principles and standards are approved through formal governance forums.",
            "Exceptions must be time-bound and explicitly owned.",
            "Major change must trace back to architecture vision and transition-state decisions."
        ],
        "controls": [
            "Architecture decision records",
            "Reference architecture compliance checks",
            "Data stewardship and classification reviews",
            "Technology lifecycle and obsolescence reviews"
        ]
    }


def remove_old_subfolders(domain_path):
    keep = {"start"}
    for child in domain_path.iterdir():
        if child.name not in keep:
            if child.is_dir():
                shutil.rmtree(child)
            else:
                child.unlink()


def rewrite_start(domain_path, domain):
    start_path = domain_path / "start"
    start_path.mkdir(parents=True, exist_ok=True)
    write_json(start_path / "config.json", {
        "title": f"{domain['name']} Enterprise Architecture",
        "description": DOMAIN_PROFILES[domain["id"]]["description"]
    })


def rewrite_domain(domain):
    domain_id = domain["id"]
    domain_path = domain_root(domain_id)
    customers, products, bricks, initiatives, releases, goals = load_product_led_inputs(domain_id)

    actors, stakeholders = derive_actors(customers)
    capabilities = derive_capabilities(bricks, products)
    business_services = derive_business_services(products)
    value_streams = derive_value_streams(customers, products)
    application = derive_application_architecture(products, business_services)

    remove_old_subfolders(domain_path)
    rewrite_start(domain_path, domain)

    write_json(domain_path / "motivation" / "architecture-vision.json", derive_motivation(domain, stakeholders, goals))
    write_json(domain_path / "business" / "business-architecture.json", derive_business_architecture(domain_id, actors, business_services, capabilities, value_streams))
    write_json(domain_path / "application" / "application-architecture.json", {
        "schemaVersion": "1.0",
        "perspective": "application-architecture",
        **application
    })
    write_json(domain_path / "data" / "data-architecture.json", derive_data_architecture(domain_id, products))
    write_json(domain_path / "technology" / "technology-architecture.json", derive_technology_architecture(domain_id, bricks))
    write_json(domain_path / "implementation" / "implementation-migration.json", derive_implementation(initiatives, releases))
    write_json(domain_path / "governance" / "architecture-governance.json", derive_governance(domain))


def rewrite_root_config():
    config_path = ROOT / "config.json"
    config = load_json(config_path, {"domains": []})
    for domain in config.get("domains", []):
        if domain["id"] in DOMAIN_PROFILES:
            domain["description"] = DOMAIN_PROFILES[domain["id"]]["description"]
    write_json(config_path, config)


def rewrite_rituals():
    rituals_path = ROOT / "rituals" / "meetings.json"
    write_json(rituals_path, ARCHITECTURE_RITUALS)


def main():
    rewrite_root_config()
    config = load_json(ROOT / "config.json", {"domains": []})
    for domain in config.get("domains", []):
        rewrite_domain(domain)
    rewrite_rituals()


if __name__ == "__main__":
    main()
