#!/usr/bin/env python3

import copy
import json
import re
from datetime import date, timedelta
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent / "product-domains"
TODAY = "2026-03-29"

PERIOD_CONFIG = {
    "archived": {
        "quarter": "2025-Q4",
        "initiative_dates": ["2025-10-15", "2025-11-12"],
        "release_offsets": [21, 24],
        "discovery_starts": ["2025-09-29", "2025-10-27"],
        "discovery_ends": ["2025-10-20", "2025-11-24"],
        "status": "archived",
        "decision_cycle": ["proceed", "sequence"],
    },
    "current": {
        "quarter": "2026-Q1",
        "initiative_dates": ["2026-01-15", "2026-02-12"],
        "release_offsets": [23, 24],
        "discovery_starts": ["2026-01-03", "2026-01-31"],
        "discovery_ends": ["2026-02-07", "2026-03-14"],
        "status": "ongoing",
    },
    "next": {
        "quarter": "2026-Q2",
        "initiative_dates": ["2026-04-16", "2026-05-14"],
        "release_offsets": [28, 28],
        "discovery_starts": ["2026-03-29", "2026-04-21"],
        "discovery_ends": ["2026-04-18", "2026-05-23"],
        "status": "ongoing",
    },
}

RESEARCH_NOTES = {
    "bike-mobility": "multi-country employer launch repeatability, rider conversion quality, and dealer-service economics",
    "emobility": "charger reliability, roaming transparency, and fleet-depot readiness as networks scale",
    "general-listings-marketplace": "trust, liquidity, and professional-seller quality in local marketplace flows",
    "internal": "workflow automation, AI-assisted support deflection, and stronger operating transparency",
    "maas": "account-based ticketing, multimodal settlement, and partner interoperability across urban mobility systems",
    "mambu": "data-driven banking operations, embedded-finance readiness, and lower servicing complexity",
    "nutrition": "traceability, formulation governance, quality-by-design, and sustainability evidence",
    "platform-engineering": "paved-road adoption, default guardrails, AI-era runtime readiness, and cost visibility",
    "premium-long-haul-airline": "digital retailing, disruption recovery, premium ancillary conversion, and cargo resilience",
    "real-estate-marketplace": "affordability pressure, lead quality, and faster response loops for supply-constrained markets",
}

DOMAIN_PROFILES = {
    "bike-mobility": {
        "pressure": "employer launch repeatability across markets while keeping service economics under control",
        "discovery_activities": [
            "Compare rollout friction across two mature employer markets and one expansion market.",
            "Replay service and claims journeys to identify avoidable dealer and rider handoffs.",
            "Test whether launch, handover, and maintenance interventions improve first-90-day rider activation."
        ],
        "decision": "Decide whether to scale the operating pattern cross-market now or concentrate it in the highest-volume countries first.",
    },
    "emobility": {
        "pressure": "session reliability, roaming clarity, and depot-readiness as charger density and utilization rise",
        "discovery_activities": [
            "Analyze failed-session cohorts by charger type, roaming path, and market.",
            "Interview roaming-heavy drivers and fleet managers about confidence gaps before session start.",
            "Model whether depot and fleet workflows should be standardized separately from public-network journeys."
        ],
        "decision": "Decide whether the next investment should optimize the mainstream public-network path or split more aggressively into fleet and roaming operating models.",
    },
    "general-listings-marketplace": {
        "pressure": "liquidity and trust while classifieds mix shifts toward professional sellers and services",
        "discovery_activities": [
            "Review drop-off points in listing creation, trust verification, and first-response journeys.",
            "Compare outcome quality between casual sellers, power users, and professional merchants.",
            "Test whether stronger trust cues improve reply quality without reducing listing volume."
        ],
        "decision": "Decide whether to push harder on trust controls now or sequence them behind supply and response-rate improvements.",
    },
    "internal": {
        "pressure": "automation, support deflection, and better operating transparency without creating shadow workflows",
        "discovery_activities": [
            "Replay the highest-volume internal service flows and isolate steps still handled manually.",
            "Interview support, operations, and finance users about exception handling and policy workarounds.",
            "Test where AI-assisted workflow support reduces handling time versus where it adds review burden."
        ],
        "decision": "Decide which workflows should become the next default automation path and which should remain high-touch because of policy or judgment needs.",
    },
    "maas": {
        "pressure": "multimodal interoperability, ticketing consistency, and settlement clarity across city partners",
        "discovery_activities": [
            "Map passenger drop-offs across account-based ticketing, parking, and public-transport payment flows.",
            "Review partner incidents where entitlement, pricing, or settlement states diverged across systems.",
            "Test whether a smaller set of mobility bundles reduces confusion without lowering conversion."
        ],
        "decision": "Decide whether to deepen multimodal packaging in the same cities or first stabilize the operator and settlement backbone.",
    },
    "mambu": {
        "pressure": "scaling banking workflows through cleaner data, lower servicing effort, and stronger partner readiness",
        "discovery_activities": [
            "Review where servicing, reconciliation, or compliance exceptions still require manual intervention.",
            "Interview lenders and embedded-finance teams about which operational delays most affect growth confidence.",
            "Test whether more explicit product, risk, and servicing controls improve launch confidence without slowing change."
        ],
        "decision": "Decide whether to prioritize scale in existing lending and banking motions or concentrate the next quarter on reducing servicing and compliance drag first.",
    },
    "nutrition": {
        "pressure": "traceability, formula governance, and quality evidence under tighter customer and regulatory scrutiny",
        "discovery_activities": [
            "Replay specification, quality, and document-change journeys across supplier and customer touchpoints.",
            "Compare how often teams rebuild evidence manually during audits, customer escalations, and change approvals.",
            "Test whether stronger traceability views improve confidence for both commercial and quality stakeholders."
        ],
        "decision": "Decide whether to scale shared specification and evidence workflows broadly or keep the next wave focused on the highest-risk product lines.",
    },
    "platform-engineering": {
        "pressure": "making the paved road faster and safer while keeping support and infrastructure cost flat",
        "discovery_activities": [
            "Compare adoption, time-to-value, and support demand across teams on and off the paved road.",
            "Replay common exception journeys around identity, policy, and runtime provisioning.",
            "Test whether more explicit cost and reliability signals change platform usage decisions."
        ],
        "decision": "Decide which platform capabilities should become mandatory defaults next quarter and which still need product-quality improvement before wider rollout.",
    },
    "premium-long-haul-airline": {
        "pressure": "premium revenue quality and operational resilience under disruption and partner complexity",
        "discovery_activities": [
            "Replay disrupted premium journeys to isolate where recovery, messaging, and care flows break down.",
            "Compare corporate, agency, and direct retail workflows to identify content or servicing gaps.",
            "Test whether more proactive recovery and retail messaging changes rebooking, ancillary take-up, and contact-center demand."
        ],
        "decision": "Decide whether to scale the next quarter around premium disruption resilience or around commercial content and distribution leverage.",
    },
    "real-estate-marketplace": {
        "pressure": "lead quality and response speed while affordability pressure constrains supply and conversion",
        "discovery_activities": [
            "Replay valuation, listing, and lead-routing journeys for supply-constrained segments.",
            "Compare owner and agency workflows to identify where lead quality degrades before first contact.",
            "Test whether stronger guidance and ranking signals improve response quality without hurting supply creation."
        ],
        "decision": "Decide whether the next wave should prioritize supply acquisition quality or speed-to-contact improvements on existing inventory first.",
    },
}

DOMAIN_TUNING = {
    "nutrition": {
        "itmn": {
            "title": "Traceability & Spec Control Hub",
            "capability": "spec exchange, evidence controls, and platform observability",
            "description": "Stabilize the data and evidence backbone behind specifications, supplier changes, and compliance artifacts so platform reliability improves without manual audit reconstruction.",
        },
        "exec": {
            "title": "Margin & Customer Assurance Workspace",
            "capability": "customer-specific specs, order transparency, and margin visibility workflows",
            "description": "Give leaders a tighter view of margin, service cost, and customer assurance so commercial tradeoffs stay grounded in reliable operational evidence.",
        },
    },
    "internal": {
        "cmmo": {
            "title": "Demand Engine Control Tower",
            "capability": "routing, approval, and pipeline-risk workflows",
            "description": "Reduce handoff and attribution noise in the demand engine so marketing can create more qualified pipeline without scaling manual ops work.",
        },
        "hsup": {
            "title": "Support Resolution & Knowledge Hub",
            "capability": "case intake, triage, and knowledge-assisted resolution workflows",
            "description": "Tighten intake, triage, and guided resolution so support organizations protect retention while lowering resolution drag and avoidable rework.",
        },
    },
    "platform-engineering": {
        "penm": {
            "title": "Team Onboarding Paved Road",
            "capability": "portal onboarding, service catalog, and golden-path templates",
            "description": "Make the default team setup path fast enough that product teams stop treating onboarding as a local project.",
        },
        "swtl": {
            "title": "Runtime Delivery Self-Service",
            "capability": "environment provisioning, release automation, and runtime connectivity patterns",
            "description": "Shorten the path from repo to production by making the standard runtime and delivery path more complete, visible, and self-service.",
        },
    },
}


def slugify(text):
    value = (text or "").strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def clean_sentence(value):
    value = re.sub(r"\s+", " ", value or "").strip()
    return value


def sentence_case(value):
    value = clean_sentence(value)
    if not value:
        return value
    return value[0].upper() + value[1:]


def kpi_direction(kpi_name):
    value = (kpi_name or "").lower()
    if "visibility" in value:
        return "increase"
    decrease_tokens = [
        "time", "latency", "cost", "churn", "failure", "mttr", "wait", "defect",
        "incident", "error", "manual", "queue", "cycle", "delay", "lead time",
        "reimbursement", "drop", "support tickets", "effort", "load", "cost-to-serve"
    ]
    if any(token in value for token in decrease_tokens):
        return "decrease"
    return "increase"


def impact_phrase(kpi_name, capability_name, business=False):
    direction = kpi_direction(kpi_name)
    capability = clean_sentence(capability_name).lower().rstrip(".")
    metric = clean_sentence(kpi_name)
    if direction == "decrease":
        lead = "Reduce" if business else "Decrease"
        return f"{lead} {metric.lower()} by improving {capability} and removing avoidable workflow friction."
    lead = "Increase"
    return f"{lead} {metric.lower()} by strengthening {capability} and making the core workflow more reliable end to end."


def normalize_note(text, note):
    pattern = re.compile(rf"(?:\s*{re.escape(note)}\.?)+", re.IGNORECASE)
    cleaned = pattern.sub("", text or "")
    cleaned = re.sub(r"\s+\.", ".", cleaned)
    return clean_sentence(cleaned).rstrip(".")


def objective_customer_id(objective):
    customers = objective.get("linkedCustomers", []) if objective else []
    return customers[0].get("customerId", "") if customers else ""


def seed_customer_id(seed):
    impacts = seed.get("customerImpact", []) if seed else []
    return impacts[0].get("customerId", "") if impacts else ""


def tuned_metadata(domain_id, objective, seed=None):
    customer_id = objective_customer_id(objective) or seed_customer_id(seed)
    return DOMAIN_TUNING.get(domain_id, {}).get(customer_id, {})


def objective_customer_impact(objective, capability_label):
    if not objective:
        return []
    customers = objective.get("linkedCustomers", [])
    if not customers:
        return []
    customer = customers[0]
    impact = {
        "customerId": customer.get("customerId", ""),
        "customerKPIs": [],
        "businessKPIs": [],
    }
    for entry in objective.get("linkedCustomerKPIs", [])[:2]:
        impact["customerKPIs"].append(
            {
                "kpi": entry.get("kpiName", entry.get("kpi", "")),
                "expectedImpact": impact_phrase(entry.get("kpiName", entry.get("kpi", "")), capability_label, business=False),
            }
        )
    for entry in objective.get("linkedBusinessKPIs", [])[:2]:
        impact["businessKPIs"].append(
            {
                "kpi": entry.get("kpiName", entry.get("kpi", "")),
                "expectedImpact": impact_phrase(entry.get("kpiName", entry.get("kpi", "")), capability_label, business=True),
            }
        )
    return [impact]


def load_json(path, default):
    if not path.exists():
        return copy.deepcopy(default)
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def save_json(path, payload):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2, ensure_ascii=False)
        handle.write("\n")


def parse_date(value):
    year, month, day = [int(part) for part in value.split("-")]
    return date(year, month, day)


def shift_date(value, days):
    return (parse_date(value) + timedelta(days=days)).isoformat()


def load_team_names(domain_root):
    teams_payload = load_json(domain_root / "teams" / "teams.json", {})
    mapping = {}
    for group in teams_payload.get("groups", []):
        for team in group.get("teams", []):
            mapping[team.get("id", "")] = team.get("name", team.get("id", "Team"))
    return mapping


def select_objectives(domain_root, period):
    payload = load_json(domain_root / "objectives" / period / "objectives.json", {})
    objectives = payload.get("objectives", [])
    target_quarter = PERIOD_CONFIG[period]["quarter"]
    if period == "archived":
        quarter_matches = [item for item in objectives if item.get("period", {}).get("quarter") == target_quarter]
        if quarter_matches:
            objectives = quarter_matches
    return objectives[:2]


def normalize_initiative_seed(item):
    seed = copy.deepcopy(item)
    seed["title"] = re.sub(r"\s+release$", " Initiative", seed.get("title", "Quarter Initiative"), flags=re.IGNORECASE)
    if not seed["title"].endswith("Initiative"):
        seed["title"] = f"{seed['title'].rstrip()} Initiative"
    description = seed.get("description", "").replace("Release of ", "").replace("release of ", "")
    if description and "initiative focused on" not in description.lower():
        description = description.rstrip(".") + " initiative focused on coordinated product and technology improvements."
    description = description.replace("Released ", "Extended ").replace("released ", "extended ")
    description = description.replace("Deployed ", "Introduced ").replace("deployed ", "introduced ")
    seed["description"] = description
    for brick in seed.get("productBricks", []):
        brick["change"] = brick.get("change", "").replace("Released", "Extended").replace("released", "extended")
    for channel in seed.get("deliveryChannels", []):
        channel["change"] = channel.get("change", "").replace("Deployed", "Introduced").replace("deployed", "introduced")
    return seed


def collect_initiative_seeds(domain_root, period):
    seeds = []
    for source_period in [period, "current", "next", "archived"]:
        payload = load_json(domain_root / "objectives" / source_period / "initiatives.json", {"items": []})
        for item in payload.get("items", []):
            seeds.append(copy.deepcopy(item))
    if not seeds:
        releases = load_json(domain_root / "delivery" / "releases.json", {"items": []})
        for item in releases.get("items", []):
            seeds.append(normalize_initiative_seed(item))
    deduped = []
    seen = set()
    for item in seeds:
        title_key = slugify(item.get("title", "initiative"))
        if not title_key or title_key in seen:
            continue
        seen.add(title_key)
        deduped.append(item)
    return deduped


def pick_seed_for_objective(available, objective):
    if not available:
        return None
    if not objective:
        return available.pop(0)

    linked_customer_ids = {item.get("customerId", "") for item in objective.get("linkedCustomers", [])}
    for index, seed in enumerate(available):
        customer_ids = {item.get("customerId", "") for item in seed.get("customerImpact", [])}
        if linked_customer_ids & customer_ids:
            return available.pop(index)

    objective_text = " ".join(
        [
            objective.get("title", ""),
            objective.get("objective", ""),
            " ".join([kr.get("metric", "") for kr in objective.get("keyResults", [])]),
        ]
    ).lower()
    best_index = 0
    best_score = -1
    for index, seed in enumerate(available):
        score = 0
        seed_text = " ".join(
            [
                seed.get("title", ""),
                seed.get("description", ""),
                " ".join([item.get("kpi", "") for impact in seed.get("customerImpact", []) for item in impact.get("customerKPIs", [])]),
            ]
        ).lower()
        for token in objective_text.split():
            if len(token) > 4 and token in seed_text:
                score += 1
        if score > best_score:
            best_score = score
            best_index = index
    return available.pop(best_index)


def ensure_list(value):
    return value if isinstance(value, list) else []


def initiative_title(seed_title):
    title = re.sub(r"\s+release\b", "", seed_title, flags=re.IGNORECASE).strip()
    if not title.endswith("Initiative"):
        title = f"{title} Initiative"
    return sentence_case(title)


def build_initiative(domain_id, period, idx, seed, objective):
    cfg = PERIOD_CONFIG[period]
    item = copy.deepcopy(seed)
    initiative_date = cfg["initiative_dates"][idx]
    title = initiative_title(item.get("title", f"{domain_id.title()} Initiative"))
    research_note = RESEARCH_NOTES.get(domain_id, "clear customer outcomes and disciplined delivery")
    profile = DOMAIN_PROFILES.get(domain_id, {})
    tuning = tuned_metadata(domain_id, objective, seed)
    first_brick = item.get("productBricks", [{}])[0].get("change", "")
    first_brick = clean_sentence(first_brick.replace("Extended ", "").replace("Released ", ""))
    first_brick = re.sub(r"\s+with domain-specific workflow improvements\.?$", "", first_brick, flags=re.IGNORECASE)
    capability_label = tuning.get("capability", first_brick or title.replace(" Initiative", ""))

    item["title"] = tuning.get("title", title)
    item["date"] = initiative_date
    item["initiativeId"] = f"initiative-{domain_id}-{initiative_date}-{idx:02d}"
    item["priority"] = "p1" if idx == 0 else "p2"
    item["keyResultId"] = item.get("keyResultId", "")
    base_description = normalize_note(item.get("description", f"{title} initiative focused on cross-functional product and technology improvements."), f"The quarter concentrates on {research_note} so the work reads like a realistic OKR-driven investment set for a company with roughly 250 product and technology people")
    customer_kpis = [entry.get("kpi", "") for impact in item.get("customerImpact", []) for entry in impact.get("customerKPIs", [])]
    business_kpis = [entry.get("kpi", "") for impact in item.get("customerImpact", []) for entry in impact.get("businessKPIs", [])]
    if objective:
        item["customerImpact"] = objective_customer_impact(objective, capability_label)
        customer_kpis = [entry["kpi"] for entry in item["customerImpact"][0].get("customerKPIs", [])] if item["customerImpact"] else []
        business_kpis = [entry["kpi"] for entry in item["customerImpact"][0].get("businessKPIs", [])] if item["customerImpact"] else []
    if customer_kpis or business_kpis:
        focus_bits = [kpi for kpi in [customer_kpis[0] if customer_kpis else "", business_kpis[0] if business_kpis else ""] if kpi]
        base_description = (
            f"{item['title']} is the quarter's focused investment to move {' and '.join(focus_bits)}, "
            f"anchored in {profile.get('pressure', research_note)} and led through {capability_label}."
        )
    if tuning.get("description"):
        base_description = f"{item['title']} exists to {tuning['description'].rstrip('.')}"
    note = f"The quarter concentrates on {research_note} so the work reads like a realistic OKR-driven investment set for a company with roughly 250 product and technology people."
    base_description = f"{base_description}. {note}"
    base_description = base_description.replace("..", ".")
    base_description = base_description.replace(".,", ",")
    item["description"] = base_description
    if " release Initiative" in item["title"]:
        item["title"] = item["title"].replace(" release Initiative", " Initiative")
    if " release" in item["title"].lower():
        item["title"] = re.sub(r"\s+release\b", "", item["title"], flags=re.IGNORECASE).strip()
        if not item["title"].endswith("Initiative"):
            item["title"] = f"{item['title']} Initiative"
    item["discoveryIds"] = []
    item["discoveryLinks"] = []
    for impact in item.get("customerImpact", []):
        capability = capability_label
        for entry in impact.get("customerKPIs", []):
            entry["expectedImpact"] = impact_phrase(entry.get("kpi", ""), capability, business=False)
        for entry in impact.get("businessKPIs", []):
            entry["expectedImpact"] = impact_phrase(entry.get("kpi", ""), capability, business=True)
    return item


def choose_objective_for_initiative(objectives, initiative, fallback_index):
    if not objectives:
        return None
    customer_id = ""
    if initiative.get("customerImpact"):
        customer_id = initiative["customerImpact"][0].get("customerId", "")
    if customer_id:
        for objective in objectives:
            if objective_customer_id(objective) == customer_id:
                return objective
    return objectives[min(fallback_index, len(objectives) - 1)]


def team_assignments(initiative, team_names):
    primary = ensure_list(initiative.get("teams", {}).get("primaryTeamIds", []))
    supporting = ensure_list(initiative.get("teams", {}).get("supportingTeamIds", []))
    assignments = []
    if primary:
        assignments.append(
            {
                "teamId": primary[0],
                "teamName": team_names.get(primary[0], primary[0]),
                "role": "lead",
                "roleLabel": "Lead discovery team",
                "how": "Leads the discovery framing, evidence synthesis, and recommendation on how far this initiative should scale.",
            }
        )
    for team_id in primary[1:] + supporting[:3]:
        assignments.append(
            {
                "teamId": team_id,
                "teamName": team_names.get(team_id, team_id),
                "role": "support",
                "roleLabel": "Supporting discovery team",
                "how": "Adds workflow, commercial, and implementation evidence needed to close the main delivery risks.",
            }
        )
    return primary[0] if primary else "", supporting, assignments


def build_risk_focus(initiative):
    customer_kpis = [
        item.get("kpi", "")
        for impact in initiative.get("customerImpact", [])
        for item in impact.get("customerKPIs", [])[:2]
    ]
    business_kpis = [
        item.get("kpi", "")
        for impact in initiative.get("customerImpact", [])
        for item in impact.get("businessKPIs", [])[:2]
    ]
    title = initiative.get("title", "initiative").replace(" Initiative", "")
    customer_metric = customer_kpis[0] if customer_kpis else "the main customer KPI"
    business_metric = business_kpis[0] if business_kpis else "the main business KPI"
    return [
        {
            "riskType": "valuable",
            "question": "Will customers buy the product and/or choose to use it?",
            "hypothesis": f"Customers will engage more consistently if {title.lower()} measurably improves {customer_metric.lower()}.",
            "evidenceToCollect": [
                f"Whether target users describe {customer_metric.lower()} as a top-priority pain point.",
                "Whether the proposed workflow changes are strong enough to change behavior, not just preference."
            ],
            "methods": ["Problem interviews", "Workflow walkthroughs", "Usage and funnel review"],
        },
        {
            "riskType": "viable",
            "question": "Will the solution meet the needs of the business?",
            "hypothesis": f"The investment is worth scaling when it improves {business_metric.lower()} without creating disproportionate operating cost or support load.",
            "evidenceToCollect": [
                "Which economic or operating constraints cap the upside.",
                "What minimum KPI movement would justify continued investment."
            ],
            "methods": ["Business case review", "Unit economics analysis", "Operating model workshop"],
        },
        {
            "riskType": "usable",
            "question": "Can customers figure out how to use it?",
            "hypothesis": "Users can complete the redesigned workflow with less guidance and less back-and-forth than the current path.",
            "evidenceToCollect": [
                "Where users hesitate in the new flow.",
                "Which messages, states, or transitions remain unclear."
            ],
            "methods": ["Task-based usability test", "Support case review", "Journey replay session"],
        },
        {
            "riskType": "feasible",
            "question": "Can we build it within given resources and constraints?",
            "hypothesis": "The teams can deliver the smallest useful slice inside current architecture and staffing constraints without creating a long tail of one-off work.",
            "evidenceToCollect": [
                "Which dependencies create sequencing risk.",
                "What can be standardized versus localized or custom."
            ],
            "methods": ["Technical spike", "Dependency mapping", "Incremental rollout planning"],
        },
    ]


def discovery_title(initiative):
    base = initiative.get("title", "initiative").replace(" Initiative", "").replace(" initiative", "")
    return f"{base}: operating discovery"


def build_discovery(domain_id, period, idx, initiative, team_names):
    cfg = PERIOD_CONFIG[period]
    title = sentence_case(discovery_title(initiative).replace(" initiative:", ":"))
    discovery_date = cfg["discovery_starts"][idx]
    lead_team_id, supporting_ids, assignments = team_assignments(initiative, team_names)
    research_note = RESEARCH_NOTES.get(domain_id, "clear customer outcomes")
    profile = DOMAIN_PROFILES.get(domain_id, {})
    discovery_id = f"discovery-{domain_id}-{discovery_date}-{idx:02d}-{slugify(title)[:36]}"

    initiative_base = initiative.get("title", "").replace(" Initiative", "").replace(" initiative", "").lower()
    item = {
        "title": title,
        "id": discovery_id,
        "name": title,
        "status": cfg["status"],
        "lastUpdated": TODAY if period == "next" else cfg["discovery_ends"][idx],
        "summary": f"Discovery work is testing whether {initiative_base} can move the linked customer and business KPIs while addressing {profile.get('pressure', research_note)}.",
        "opportunity": f"Clarify whether this bet is strong enough to scale in the next planning cycle, or whether the organization should narrow scope and protect focus.",
        "linkedInitiatives": [
            {
                "initiativeId": initiative["initiativeId"],
                "description": initiative["description"],
            }
        ],
        "teams": {
            "leadTeamId": lead_team_id,
            "supportingTeamIds": supporting_ids,
            "assignments": assignments,
        },
        "riskFocus": build_risk_focus(initiative),
        "plannedActivities": profile.get("discovery_activities", [
            "Interview a balanced mix of heavy users, moderate users, and edge-case operators.",
            "Replay recent high-friction journeys to separate structural pain from market noise.",
            "Prototype the smallest credible improvement slice and test whether it changes real behavior."
        ]),
        "decisionToMake": profile.get("decision", "Decide whether to proceed as planned, narrow the scope, or sequence the investment behind a smaller enabling step."),
        "startDate": discovery_date,
        "endDate": cfg["discovery_ends"][idx],
    }
    if period == "archived":
        decision = cfg["decision_cycle"][idx % len(cfg["decision_cycle"])]
        item["outcome"] = {
            "decision": decision,
            "summary": "Discovery closed enough uncertainty to make a concrete sequencing and investment decision for the following quarter.",
        }
    return item


def release_title(initiative):
    return initiative.get("title", "Initiative").replace("Initiative", "Release").strip()


def transform_release_change(value):
    return (
        value.replace("Introduced", "Deployed")
        .replace("Extended", "Released")
        .replace("introduced", "deployed")
        .replace("extended", "released")
    )


def build_release(domain_id, period, idx, initiative):
    initiative_date = initiative["date"]
    release_date = shift_date(initiative_date, PERIOD_CONFIG[period]["release_offsets"][idx])
    research_note = RESEARCH_NOTES.get(domain_id, "clear customer outcomes and disciplined delivery")
    note = f"The quarter concentrates on {research_note} so the work reads like a realistic OKR-driven investment set for a company with roughly 250 product and technology people."
    base = normalize_note(initiative.get("description", ""), note)
    release_base = base.replace(" is the quarter's focused investment to ", " improvements focused on ")
    release_base = release_base.replace("focused on move ", "aimed at moving ")
    release_base = release_base.replace(" Initiative ", " ")
    release_base = clean_sentence(release_base)
    item = {
        "title": release_title(initiative),
        "date": release_date,
        "description": f"Release of {release_base}. {note}",
        "customerImpact": copy.deepcopy(initiative.get("customerImpact", [])),
        "productBricks": copy.deepcopy(initiative.get("productBricks", [])),
        "deliveryChannels": copy.deepcopy(initiative.get("deliveryChannels", [])),
        "teams": copy.deepcopy(initiative.get("teams", {})),
        "initiativeId": initiative["initiativeId"],
    }
    for brick in item["productBricks"]:
        brick["change"] = transform_release_change(brick.get("change", "Released domain-specific workflow improvements."))
    for channel in item["deliveryChannels"]:
        channel["change"] = transform_release_change(channel.get("change", "Deployed workflow updates."))
    return item


def generate_period_payload(domain_id, domain_root, period):
    team_names = load_team_names(domain_root)
    objectives = select_objectives(domain_root, period)
    seeds = collect_initiative_seeds(domain_root, period)
    selected = []
    working_seeds = copy.deepcopy(seeds)
    target_count = 2
    for index in range(target_count):
        objective = objectives[index] if index < len(objectives) else None
        seed = pick_seed_for_objective(working_seeds, objective)
        if seed is None:
            fallback = {
                "title": f"{domain_id.replace('-', ' ').title()} Core Flow Initiative",
                "description": "Cross-functional initiative focused on improving a high-friction domain workflow.",
                "customerImpact": [],
                "productBricks": [],
                "deliveryChannels": [],
                "teams": {"primaryTeamIds": [], "supportingTeamIds": []},
            }
            seed = fallback
        selected.append(build_initiative(domain_id, period, index, seed, objective))

    objective_use_count = {}
    for index, initiative in enumerate(selected):
        objective = choose_objective_for_initiative(objectives, initiative, index)
        if not objective or not objective.get("keyResults"):
            initiative["keyResultId"] = ""
            continue
        used = objective_use_count.get(objective["id"], 0)
        kr = objective["keyResults"][used % len(objective["keyResults"])]
        initiative["keyResultId"] = f"{objective['id']}/{kr.get('id', 'kr-1')}"
        objective_use_count[objective["id"]] = used + 1

    discoveries = []
    for index, initiative in enumerate(selected):
        discovery = build_discovery(domain_id, period, index, initiative, team_names)
        initiative["discoveryIds"] = [discovery["id"]]
        initiative["discoveryLinks"] = [
            {
                "discoveryId": discovery["id"],
                "discoveryName": discovery["name"],
                "status": discovery["status"],
            }
        ]
        discoveries.append(discovery)

    return {"items": selected}, {"items": discoveries}


def main():
    config = load_json(ROOT / "config.json", {"domains": []})
    all_releases = {}
    for domain in config.get("domains", []):
        domain_id = domain["id"]
        domain_root = ROOT / domain_id
        releases = []
        for period in ["archived", "current", "next"]:
            initiatives_payload, discoveries_payload = generate_period_payload(domain_id, domain_root, period)
            save_json(domain_root / "objectives" / period / "initiatives.json", initiatives_payload)
            save_json(domain_root / "objectives" / period / "discoveries.json", discoveries_payload)
            for idx, initiative in enumerate(initiatives_payload["items"]):
                releases.append(build_release(domain_id, period, idx, initiative))
        releases.sort(key=lambda item: item["date"])
        all_releases[domain_id] = len(releases)
        save_json(domain_root / "delivery" / "releases.json", {"items": releases})

    for domain_id in sorted(all_releases):
        print(f"{domain_id}: {all_releases[domain_id]} releases written")


if __name__ == "__main__":
    main()
