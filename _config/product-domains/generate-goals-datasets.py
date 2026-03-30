import datetime
import json
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parent
CONFIG_PATH = ROOT / "config.json"


def load_json(path, default):
    if path.exists():
        return json.loads(path.read_text())
    return default


def slugify(value):
    chars = []
    last_dash = False
    for ch in (value or "").strip().lower():
        if ch.isalnum():
            chars.append(ch)
            last_dash = False
        elif not last_dash:
            chars.append("-")
            last_dash = True
    return "".join(chars).strip("-")


def quarter_key(date_value):
    quarter = ((date_value.month - 1) // 3) + 1
    return f"{date_value.year}-Q{quarter}"


def quarter_start_end(year, quarter):
    start_month = ((quarter - 1) * 3) + 1
    start = datetime.date(year, start_month, 1)
    if quarter == 4:
        end = datetime.date(year, 12, 31)
    else:
        end = datetime.date(year, start_month + 3, 1) - datetime.timedelta(days=1)
    return start, end


def previous_quarters(current_year, current_quarter, count):
    year = current_year
    quarter = current_quarter
    result = []
    for _ in range(count):
        quarter -= 1
        if quarter == 0:
            quarter = 4
            year -= 1
        result.append((year, quarter))
    return list(reversed(result))


def next_quarter(year, quarter):
    if quarter == 4:
        return year + 1, 1
    return year, quarter + 1


def target2_date(year, quarter):
    if quarter in (1, 2):
        return datetime.date(year, 12, 31), f"{year}-year-end target"
    if quarter == 3:
        next_year, next_q = next_quarter(year, 4)
        _, end_date = quarter_start_end(next_year, next_q)
        return end_date, f"{next_year}-Q{next_q} target"
    _, end_date = quarter_start_end(year + 1, 2)
    return end_date, f"{year + 1}-Q2 target"


def confidence_for_status(status):
    mapping = {
        "achieved": "green",
        "on-track": "green",
        "at-risk": "amber",
        "off-track": "red",
        "planned": "undefined",
        "active": "undefined",
        "archived": "undefined"
    }
    return mapping.get((status or "").strip().lower(), "undefined")


def soften_confidence(confidence, status):
    if (status or "").strip().lower() == "achieved":
        return confidence
    mapping = {
        "green": "amber",
        "amber": "red",
        "red": "red",
        "undefined": "undefined"
    }
    return mapping.get(confidence, "undefined")


def clean_text(text):
    value = (text or "").strip()
    if not value:
        return ""
    return value[:-1] if value.endswith(".") else value


def lc_first(text):
    value = clean_text(text)
    if not value:
        return ""
    return value[0].lower() + value[1:]


def projected_value(metric, direction, horizon, target_text, statement_text):
    metric_name = metric or "the metric"
    target_fragment = lc_first(target_text) or f"improve {metric_name}"
    statement_fragment = lc_first(statement_text)
    if horizon == 1:
        if statement_fragment:
            return f"Current estimate: {metric_name} moves far enough to show clear momentum toward {target_fragment}, driven by {statement_fragment}."
        return f"Current estimate: {metric_name} moves far enough to show clear momentum toward {target_fragment}."

    if direction == "decrease":
        return f"Current estimate: {metric_name} ends the horizon sustainably lower than today's baseline, with {target_fragment} holding across the broader operating model."
    return f"Current estimate: {metric_name} ends the horizon sustainably ahead of today's baseline, with {target_fragment} holding across the broader operating model."


def collect_kpis(node, target):
    if not node:
        return
    if node.get("name"):
        target.append({
            "id": node.get("id", slugify(node.get("name", ""))),
            "name": node.get("name", ""),
            "description": node.get("description", ""),
            "unit": node.get("unit", "")
        })
    for child in node.get("children", []):
        collect_kpis(child, target)


def flatten_customer(customer):
    pyramids = customer.get("kpiPyramids", {})
    customer_kpis = []
    business_kpis = []

    customer_outcomes = pyramids.get("customerOutcomes", {})
    business_outcomes = pyramids.get("businessOutcomes", {})
    collect_kpis(customer_outcomes.get("top"), customer_kpis)
    for branch in customer_outcomes.get("branches", []):
        collect_kpis(branch, customer_kpis)
    collect_kpis(business_outcomes.get("top"), business_kpis)
    for branch in business_outcomes.get("branches", []):
        collect_kpis(branch, business_kpis)

    return {
        "id": customer.get("id"),
        "name": customer.get("name", customer.get("id", "Customer")),
        "group": customer.get("group", ""),
        "strategy": customer.get("productStrategy", {}),
        "customerKpis": customer_kpis,
        "businessKpis": business_kpis
    }


def load_customers(domain_root, domain_name):
    raw = load_json(domain_root / "customers" / "customers.json", [])
    customers = []
    for group in raw:
        for customer in group.get("customers", []):
            customer["group"] = group.get("group", "")
            customers.append(flatten_customer(customer))

    if customers:
        return customers

    synthetic_id = f"{slugify(domain_name)}-synthetic-customer"
    return [{
        "id": synthetic_id,
        "name": f"{domain_name} Ecosystem Stakeholder",
        "group": "Synthetic fallback",
        "strategy": {
            "vision": f"Strengthen the {domain_name} operating model with measurable customer and business outcomes.",
            "timeHorizons": {
                "1_year": {
                    "focus": "Operational reliability and outcome clarity",
                    "productTheme": "Foundational platform execution",
                    "customerKPI": {
                        "northStar": "Customer adoption and satisfaction",
                        "supporting": [
                            "Service reliability",
                            "Workflow completion rate"
                        ]
                    },
                    "businessKPI": {
                        "northStar": "Account growth and retention",
                        "supporting": [
                            "Expansion",
                            "Platform usage"
                        ]
                    },
                    "milestones": [
                        "Establish baseline customer metrics",
                        "Connect roadmap execution to measurable outcomes"
                    ]
                }
            }
        },
        "customerKpis": [
            {
                "id": "customer-adoption-satisfaction",
                "name": "Customer adoption and satisfaction",
                "description": "Synthetic fallback KPI used when no customer model exists in source data.",
                "unit": "index"
            },
            {
                "id": "service-reliability",
                "name": "Service reliability",
                "description": "Synthetic fallback KPI used when no customer model exists in source data.",
                "unit": "%"
            }
        ],
        "businessKpis": [
            {
                "id": "account-growth-retention",
                "name": "Account growth and retention",
                "description": "Synthetic fallback KPI used when no customer model exists in source data.",
                "unit": "%"
            }
        ]
    }]


def load_activities(domain_root, filename):
    items = load_json(domain_root / "delivery" / filename, {}).get("items", [])
    result = []
    for index, item in enumerate(items):
        if not item.get("date"):
            continue
        date_value = datetime.date.fromisoformat(item["date"])
        customer_ids = [impact.get("customerId") for impact in item.get("customerImpact", []) if impact.get("customerId")]
        result.append({
            "id": f"{filename.replace('.json', '')}-{date_value.isoformat()}-{index}",
            "date": date_value.isoformat(),
            "quarter": quarter_key(date_value),
            "description": item.get("title") or item.get("name") or item.get("description", "").strip(),
            "customerIds": customer_ids,
            "deliveryChannels": [channel.get("channelId") for channel in item.get("deliveryChannels", []) if channel.get("channelId")],
            "productBricks": [brick.get("brickId") for brick in item.get("productBricks", []) if brick.get("brickId")]
        })
    return result


def direction_for_kpi(kpi_name):
    tokens = [token for token in re.split(r"[^a-z0-9]+", (kpi_name or "").lower()) if token]
    negative_terms = {
        "cost",
        "latency",
        "time",
        "failure",
        "dispute",
        "queue",
        "risk",
        "churn",
        "leakage",
        "incident",
        "repair",
        "manual"
    }
    for token in tokens:
        if token in negative_terms:
            return "decrease"
    return "increase"


def build_kpi_links(customer, kind, limit):
    source = customer["customerKpis"] if kind == "customer" else customer["businessKpis"]
    result = []
    for item in source[:limit]:
        result.append({
            "customerId": customer["id"],
            "customerName": customer["name"],
            "kpiId": item.get("id", slugify(item.get("name", ""))),
            "kpiName": item.get("name", ""),
            "description": item.get("description", ""),
            "unit": item.get("unit", ""),
            "kind": kind,
            "targetDirection": direction_for_kpi(item.get("name", ""))
        })
    return result


def build_key_results(customer, period_key, key_result_status):
    key_results = []
    year_text, quarter_text = period_key.split("-Q")
    year = int(year_text)
    quarter = int(quarter_text)
    next_year, next_q = next_quarter(year, quarter)
    _, target1_end = quarter_start_end(next_year, next_q)
    target2_end, target2_label = target2_date(year, quarter)
    base_confidence = confidence_for_status(key_result_status)
    linked_customer = build_kpi_links(customer, "customer", 2)
    linked_business = build_kpi_links(customer, "business", 1)
    for index, item in enumerate(linked_customer + linked_business, start=1):
        target_text = "Improve quarter over quarter"
        statement_text = f"{'Increase' if item['targetDirection'] == 'increase' else 'Decrease'} {item['kpiName']} during the quarter."
        key_results.append({
            "id": f"kr-{index}",
            "metric": item["kpiName"],
            "kind": item["kind"],
            "targetDirection": item["targetDirection"],
            "target": target_text,
            "baseline": "Baseline to be confirmed from quarterly reporting",
            "statement": statement_text,
            "target1": {
                "label": f"{next_year}-Q{next_q} target",
                "date": target1_end.isoformat(),
                "target": target_text,
                "projectedValue": projected_value(item["kpiName"], item["targetDirection"], 1, target_text, statement_text),
                "confidence": base_confidence
            },
            "target2": {
                "label": target2_label,
                "date": target2_end.isoformat(),
                "target": target_text,
                "projectedValue": projected_value(item["kpiName"], item["targetDirection"], 2, target_text, statement_text),
                "confidence": soften_confidence(base_confidence, key_result_status)
            }
        })
    return key_results


def describe_objective(customer, timeframe_label):
    horizon = customer.get("strategy", {}).get("timeHorizons", {}).get("1_year", {})
    focus = horizon.get("focus", "delivery reliability")
    product_theme = horizon.get("productTheme", "platform execution")
    north_star = horizon.get("customerKPI", {}).get("northStar")
    fallback_kpi = customer["customerKpis"][0]["name"] if customer["customerKpis"] else "customer outcomes"
    target_kpi = north_star or fallback_kpi

    if timeframe_label == "current":
        prefix = "Improve"
    elif timeframe_label == "next":
        prefix = "Prepare to improve"
    else:
        prefix = "Improve"

    return f"{prefix} {target_kpi} for {customer['name']} by advancing {focus.lower()} through {product_theme.lower()}."


def summarize_links(items, customer_id=None, limit=5):
    filtered = []
    for item in items:
        if customer_id and item["customerIds"] and customer_id not in item["customerIds"]:
            continue
        filtered.append({
            "id": item["id"],
            "date": item["date"],
            "description": item["description"],
            "customerIds": item["customerIds"],
            "deliveryChannels": item["deliveryChannels"][:4],
            "productBricks": item["productBricks"][:4]
        })
    if filtered:
        return filtered[:limit]
    if customer_id:
        return summarize_links(items, None, limit)
    return []


def choose_customers_for_quarter(customers, quarter_activities, fallback_count):
    counts = Counter()
    for item in quarter_activities:
        for customer_id in item["customerIds"]:
            counts[customer_id] += 1

    selected = []
    for customer_id, _ in counts.most_common(fallback_count):
        customer = next((item for item in customers if item["id"] == customer_id), None)
        if customer:
            selected.append(customer)

    if selected:
        return selected

    return customers[:fallback_count]


def build_objective(domain, customer, period_key, period_type, initiatives, releases):
    year, quarter = period_key.split("-Q")
    start_date, end_date = quarter_start_end(int(year), int(quarter))

    objective = {
        "id": f"{domain['id']}-{period_key.lower()}-{slugify(customer['id'])}",
        "title": f"{period_key} {customer['name']} outcome goal",
        "objective": describe_objective(customer, period_type),
        "okrStyle": "objective-and-key-results",
        "status": "planned" if period_type == "next" else "active" if period_type == "current" else "archived",
        "period": {
            "quarter": period_key,
            "startDate": start_date.isoformat(),
            "endDate": end_date.isoformat(),
            "type": period_type
        },
        "linkedCustomers": [
            {
                "customerId": customer["id"],
                "customerName": customer["name"],
                "customerGroup": customer.get("group", "")
            }
        ],
        "linkedCustomerKPIs": build_kpi_links(customer, "customer", 2),
        "linkedBusinessKPIs": build_kpi_links(customer, "business", 1),
        "keyResults": build_key_results(customer, period_key, "planned" if period_type == "next" else "on-track"),
        "linkedInitiatives": summarize_links(initiatives, customer["id"]),
        "linkedReleases": summarize_links(releases, customer["id"]),
        "sourceReferences": {
            "customers": "customers/customers.json" if (ROOT / domain["id"] / "customers" / "customers.json").exists() else None,
            "initiatives": "delivery/initiatives.json" if (ROOT / domain["id"] / "delivery" / "initiatives.json").exists() else None,
            "releases": "delivery/releases.json" if (ROOT / domain["id"] / "delivery" / "releases.json").exists() else None
        }
    }
    return objective


def write_json(path, payload):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2))


def build_payload(domain, timeframe_name, customers, initiatives, releases, objectives, extra=None):
    payload = {
        "schemaVersion": "1.0",
        "domainId": domain["id"],
        "domainName": domain["name"],
        "timeframe": timeframe_name,
        "generatedOn": datetime.date.today().isoformat(),
        "methodology": "Derived from customer KPI pyramids, 1-year product strategy horizons, and delivery activity using an OKR-inspired objective structure.",
        "objectives": objectives
    }
    if extra:
        payload.update(extra)
    return payload


def main():
    config = load_json(CONFIG_PATH, {"domains": []})
    today = datetime.date.today()
    current_quarter_number = ((today.month - 1) // 3) + 1
    current_quarter_key = f"{today.year}-Q{current_quarter_number}"
    next_year, next_quarter_number = next_quarter(today.year, current_quarter_number)
    next_quarter_key = f"{next_year}-Q{next_quarter_number}"
    archive_quarters = previous_quarters(today.year, current_quarter_number, 8)
    archive_keys = [f"{year}-Q{quarter}" for year, quarter in archive_quarters]

    for domain in config["domains"]:
        domain_root = ROOT / domain["id"]
        customers = load_customers(domain_root, domain["name"])
        initiatives = load_activities(domain_root, "initiatives.json")
        releases = load_activities(domain_root, "releases.json")

        current_initiatives = [item for item in initiatives if item["quarter"] == current_quarter_key]
        current_releases = [item for item in releases if item["quarter"] == current_quarter_key]
        next_selected_customers = choose_customers_for_quarter(customers, current_initiatives + current_releases, min(2, len(customers)))
        current_selected_customers = choose_customers_for_quarter(customers, current_initiatives + current_releases, min(2, len(customers)))

        current_objectives = [
            build_objective(domain, customer, current_quarter_key, "current", current_initiatives, current_releases)
            for customer in current_selected_customers
        ]

        next_objectives = [
            build_objective(domain, customer, next_quarter_key, "next", current_initiatives, current_releases)
            for customer in next_selected_customers
        ]

        archive_objectives = []
        for index, archive_key in enumerate(archive_keys):
            quarter_initiatives = [item for item in initiatives if item["quarter"] == archive_key]
            quarter_releases = [item for item in releases if item["quarter"] == archive_key]
            if quarter_initiatives or quarter_releases:
                selected_customers = choose_customers_for_quarter(customers, quarter_initiatives + quarter_releases, 1)
                customer = selected_customers[0]
            else:
                customer = customers[index % len(customers)]
            archive_objectives.append(build_objective(domain, customer, archive_key, "archive", quarter_initiatives, quarter_releases))

        objectives_root = domain_root / "objectives"
        write_json(
            objectives_root / "current.json",
            build_payload(
                domain,
                "current_quarter",
                customers,
                initiatives,
                releases,
                    current_objectives,
                    {
                        "quarter": current_quarter_key,
                        "description": "Objectives for the current quarter."
                    }
                )
            )
        write_json(
            objectives_root / "next.json",
            build_payload(
                domain,
                "next_quarter_preparation",
                customers,
                initiatives,
                releases,
                    next_objectives,
                    {
                        "quarter": next_quarter_key,
                        "description": "Preparation objectives for the next quarter."
                    }
                )
            )
        write_json(
            objectives_root / "archive.json",
            build_payload(
                domain,
                "archive",
                customers,
                initiatives,
                releases,
                    archive_objectives,
                    {
                        "quartersCovered": archive_keys,
                        "description": "Archived quarterly objectives covering the past two years before the current quarter."
                    }
                )
            )


if __name__ == "__main__":
    main()
