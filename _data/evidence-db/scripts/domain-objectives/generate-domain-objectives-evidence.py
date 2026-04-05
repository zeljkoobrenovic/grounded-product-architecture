#!/usr/bin/env python3
"""Transform domain-specific objectives data into evidence fragments."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

OBJECTIVE_PERIODS = ("current", "next", "ktlo", "archived")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate evidence fragments from domain-specific objectives, initiatives, and discoveries."
    )
    parser.add_argument(
        "--input-root",
        type=Path,
        required=True,
        help="Path to the objectives root containing period folders.",
    )
    parser.add_argument("--output", type=Path, required=True, help="Path to generated evidence json")
    return parser.parse_args()


def load_json(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"Expected an object in {path}")
    return data


def compact_text(*parts: str) -> str:
    return " ".join(part.strip() for part in parts if str(part).strip())


def append_fact(facts: list[dict], label: str, value: object, *, summable: bool = False) -> None:
    if value is None:
        return
    if isinstance(value, str) and not value.strip():
        return
    fact: dict[str, object] = {"label": label, "value": value}
    if summable:
        fact["summable"] = True
    facts.append(fact)


def extract_team_counts(key_results: list[dict]) -> tuple[int, int]:
    executing = set()
    supporting = set()
    for key_result in key_results:
        for team in key_result.get("executingTeams", []):
            team_id = str(team.get("teamId", "")).strip()
            if team_id:
                executing.add(team_id)
        for team in key_result.get("supportingTeams", []):
            team_id = str(team.get("teamId", "")).strip()
            if team_id:
                supporting.add(team_id)
    return len(executing), len(supporting)


def build_company_objective_fragment(item: dict, payload: dict, period: str) -> dict:
    facts: list[dict] = []
    append_fact(facts, "domain", payload.get("domainName"))
    append_fact(facts, "period", period)
    append_fact(facts, "status", item.get("status"))
    append_fact(facts, "quarter", payload.get("quarter"))
    append_fact(facts, "source objectives", len(item.get("sourceObjectiveIds", [])), summable=True)
    append_fact(facts, "inspired insights", len(item.get("inspiredByInsights", [])), summable=True)

    return {
        "id": f"domain-objectives/company-objective/{period}/{item.get('id', '')}",
        "type": "domain-company-objective",
        "icon": "evidence-objective.png",
        "title": item.get("title", item.get("id", "Company Objective")),
        "description": compact_text(item.get("statement", ""), item.get("okrDesignNotes", "")),
        "facts": facts,
        "links": [],
        "tags": ["domain-objectives", "company-objective", f"period:{period}", f"status:{item.get('status', 'unknown')}"],
    }


def build_objective_fragment(item: dict, payload: dict, period: str) -> dict:
    key_results = item.get("keyResults", [])
    executing_count, supporting_count = extract_team_counts(key_results)
    period_info = item.get("period", {})

    facts: list[dict] = []
    append_fact(facts, "domain", payload.get("domainName"))
    append_fact(facts, "period", period)
    append_fact(facts, "status", item.get("status"))
    append_fact(facts, "quarter", period_info.get("quarter") or payload.get("quarter"))
    append_fact(facts, "period type", period_info.get("type"))
    append_fact(facts, "start date", period_info.get("startDate"))
    append_fact(facts, "end date", period_info.get("endDate"))
    append_fact(facts, "linked customers", len(item.get("linkedCustomers", [])), summable=True)
    append_fact(facts, "customer KPIs", len(item.get("linkedCustomerKPIs", [])), summable=True)
    append_fact(facts, "business KPIs", len(item.get("linkedBusinessKPIs", [])), summable=True)
    append_fact(facts, "key results", len(key_results), summable=True)
    append_fact(facts, "executing teams", executing_count, summable=True)
    append_fact(facts, "supporting teams", supporting_count, summable=True)

    return {
        "id": f"domain-objectives/objective/{item.get('id', '')}",
        "type": "domain-objective",
        "icon": "evidence-objective.png",
        "title": item.get("title", item.get("id", "Objective")),
        "description": item.get("objective", ""),
        "facts": facts,
        "links": [],
        "tags": ["domain-objectives", "objective", f"period:{period}", f"status:{item.get('status', 'unknown')}"],
    }


def build_key_result_fragment(objective: dict, key_result: dict, payload: dict, period: str) -> dict:
    facts: list[dict] = []
    append_fact(facts, "domain", payload.get("domainName"))
    append_fact(facts, "period", period)
    append_fact(facts, "objective", objective.get("title"))
    append_fact(facts, "status", key_result.get("status"))
    append_fact(facts, "kind", key_result.get("kind"))
    append_fact(facts, "target direction", key_result.get("targetDirection"))
    append_fact(facts, "commitment", key_result.get("commitmentLabel"))
    append_fact(facts, "executing teams", len(key_result.get("executingTeams", [])), summable=True)
    append_fact(facts, "supporting teams", len(key_result.get("supportingTeams", [])), summable=True)
    append_fact(facts, "target 1 date", (key_result.get("target1") or {}).get("date"))
    append_fact(facts, "target 2 date", (key_result.get("target2") or {}).get("date"))

    description = compact_text(
        key_result.get("statement", ""),
        f"Target: {key_result.get('target', '').strip()}" if str(key_result.get("target", "")).strip() else "",
        f"Baseline: {key_result.get('baseline', '').strip()}" if str(key_result.get("baseline", "")).strip() else "",
    )

    return {
        "id": f"domain-objectives/key-result/{objective.get('id', '')}/{key_result.get('id', '')}",
        "type": "domain-key-result",
        "icon": "evidence-key-result.png",
        "title": key_result.get("metric", key_result.get("id", "Key Result")),
        "description": description,
        "facts": facts,
        "links": [],
        "tags": [
            "domain-objectives",
            "key-result",
            f"period:{period}",
            f"status:{key_result.get('status', 'unknown')}",
            f"kind:{key_result.get('kind', 'unknown')}",
        ],
    }


def build_initiative_fragment(item: dict, period: str) -> dict:
    teams = item.get("teams", {})

    facts: list[dict] = []
    append_fact(facts, "period", period)
    append_fact(facts, "date", item.get("date"))
    append_fact(facts, "priority", item.get("priority"))
    append_fact(facts, "category", item.get("category"))
    append_fact(facts, "linked key result", item.get("keyResultId"))
    append_fact(facts, "discoveries", len(item.get("discoveryIds", [])), summable=True)
    append_fact(facts, "product bricks", len(item.get("productBricks", [])), summable=True)
    append_fact(facts, "delivery channels", len(item.get("deliveryChannels", [])), summable=True)
    append_fact(facts, "primary teams", len(teams.get("primaryTeamIds", [])), summable=True)
    append_fact(facts, "supporting teams", len(teams.get("supportingTeamIds", [])), summable=True)

    return {
        "id": f"domain-objectives/initiative/{item.get('initiativeId', item.get('title', ''))}",
        "type": "domain-initiative",
        "icon": "evidence-initiative.png",
        "title": item.get("title", item.get("initiativeId", "Initiative")),
        "description": item.get("description", ""),
        "facts": facts,
        "links": [],
        "tags": [
            "domain-objectives",
            "initiative",
            f"period:{period}",
            f"priority:{item.get('priority', 'unknown')}",
        ],
    }


def build_discovery_fragment(item: dict, period: str) -> dict:
    teams = item.get("teams", {})

    facts: list[dict] = []
    append_fact(facts, "period", period)
    append_fact(facts, "status", item.get("status"))
    append_fact(facts, "last updated", item.get("lastUpdated"))
    append_fact(facts, "start date", item.get("startDate"))
    append_fact(facts, "end date", item.get("endDate"))
    append_fact(facts, "linked initiatives", len(item.get("linkedInitiatives", [])), summable=True)
    append_fact(facts, "risk areas", len(item.get("riskFocus", [])), summable=True)
    append_fact(facts, "planned activities", len(item.get("plannedActivities", [])), summable=True)
    append_fact(facts, "team assignments", len(teams.get("assignments", [])), summable=True)
    append_fact(facts, "lead team", teams.get("leadTeamId"))

    return {
        "id": f"domain-objectives/discovery/{item.get('id', item.get('title', ''))}",
        "type": "domain-discovery",
        "icon": "evidence-discovery.png",
        "title": item.get("title", item.get("name", item.get("id", "Discovery"))),
        "description": compact_text(item.get("summary", ""), item.get("opportunity", "")),
        "facts": facts,
        "links": [],
        "tags": [
            "domain-objectives",
            "discovery",
            f"period:{period}",
            f"status:{item.get('status', 'unknown')}",
        ],
    }


def build_output(input_root: Path) -> dict:
    fragments: list[dict] = []
    summary = {
        "periods": {},
        "company_objectives": 0,
        "objectives": 0,
        "key_results": 0,
        "initiatives": 0,
        "discoveries": 0,
    }
    domains: set[str] = set()

    for period in OBJECTIVE_PERIODS:
        objectives_payload = load_json(input_root / period / "objectives.json")
        initiatives_payload = load_json(input_root / period / "initiatives.json")
        discoveries_payload = load_json(input_root / period / "discoveries.json")

        domains.add(str(objectives_payload.get("domainId", "")).strip())

        company_objectives = objectives_payload.get("companyObjectives", [])
        objectives = objectives_payload.get("objectives", [])
        initiatives = initiatives_payload.get("items", [])
        discoveries = discoveries_payload.get("items", [])
        key_results = sum(len(item.get("keyResults", [])) for item in objectives)

        summary["periods"][period] = {
            "company_objectives": len(company_objectives),
            "objectives": len(objectives),
            "key_results": key_results,
            "initiatives": len(initiatives),
            "discoveries": len(discoveries),
        }
        summary["company_objectives"] += len(company_objectives)
        summary["objectives"] += len(objectives)
        summary["key_results"] += key_results
        summary["initiatives"] += len(initiatives)
        summary["discoveries"] += len(discoveries)

        for item in company_objectives:
            fragments.append(build_company_objective_fragment(item, objectives_payload, period))
        for item in objectives:
            fragments.append(build_objective_fragment(item, objectives_payload, period))
            for key_result in item.get("keyResults", []):
                fragments.append(build_key_result_fragment(item, key_result, objectives_payload, period))
        for item in initiatives:
            fragments.append(build_initiative_fragment(item, period))
        for item in discoveries:
            fragments.append(build_discovery_fragment(item, period))

    return {
        "config": {
            "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
            "source": str(input_root),
            "periods": list(OBJECTIVE_PERIODS),
            "domain_count": len({domain for domain in domains if domain}),
            "fragment_count": len(fragments),
            "summary": summary,
        },
        "fragments": fragments,
    }


def main() -> None:
    args = parse_args()
    output = build_output(args.input_root)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
