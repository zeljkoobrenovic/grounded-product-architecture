#!/usr/bin/env python3
"""Transform GCP project cost data into evidence fragments."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate GCP project evidence fragments from project cost data."
    )
    parser.add_argument("--input", type=Path, required=True, help="Path to GCP projects.json")
    parser.add_argument("--output", type=Path, required=True, help="Path to generated evidence json")
    return parser.parse_args()


def load_projects_payload(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"Expected an object in {path}")
    return data


def build_project_index(payload: dict) -> dict[str, list[dict]]:
    index: dict[str, list[dict]] = {}
    for month_entry in payload.get("perMonth", []):
        month = month_entry.get("month", "")
        for service_entry in month_entry.get("services", []):
            project_name = str(service_entry.get("service", "")).strip()
            if not project_name:
                continue
            entry = {
                "month": month,
                "costs": float(service_entry.get("costs", 0) or 0),
                "costs_without_discount": float(service_entry.get("costs_without_discount", 0) or 0),
                "usage": float(service_entry.get("usage", 0) or 0),
            }
            index.setdefault(project_name, []).append(entry)
    return index


def build_facts(project_name: str, monthly_entries: list[dict]) -> list[dict]:
    if not monthly_entries:
        return []

    sorted_entries = sorted(monthly_entries, key=lambda item: item.get("month", ""), reverse=True)
    latest_entry = sorted_entries[0]
    peak_entry = max(monthly_entries, key=lambda item: item.get("costs", 0))
    total_cost = sum(item.get("costs", 0) for item in monthly_entries)

    return [
        {"value": round(latest_entry.get("costs", 0), 2), "label": "latest monthly cost", "summable": True},
        {"value": latest_entry.get("month", ""), "label": "latest month"},
        {"value": round(total_cost, 2), "label": "observed total cost"},
        {"value": round(peak_entry.get("costs", 0), 2), "label": "peak monthly cost"},
        {"value": peak_entry.get("month", ""), "label": "peak month"},
        {"value": len(monthly_entries), "label": "months observed"},
    ]


def build_fragment(project_name: str, monthly_entries: list[dict]) -> dict:
    latest_entry = max(monthly_entries, key=lambda item: item.get("month", "")) if monthly_entries else {}
    latest_cost = round(latest_entry.get("costs", 0), 2) if latest_entry else 0
    latest_month = latest_entry.get("month", "") if latest_entry else ""

    return {
        "id": f"gcp/{project_name}",
        "type": "gcp-project-cost",
        "icon": "evidence-gcp.png",
        "title": project_name,
        "description": (
            f"GCP project cost evidence for {project_name}"
            + (f" based on the latest observed month {latest_month}" if latest_month else "")
            + (f" with cost {latest_cost}" if latest_month else "")
            + "."
        ),
        "facts": build_facts(project_name, monthly_entries),
        "links": [],
        "tags": ["gcp", "project-cost"],
    }


def aggregate_summary(project_index: dict[str, list[dict]]) -> dict:
    latest_month = ""
    latest_total_cost = 0.0

    all_months = sorted(
        {entry.get("month", "") for entries in project_index.values() for entry in entries if entry.get("month", "")},
        reverse=True,
    )
    if all_months:
        latest_month = all_months[0]
        latest_total_cost = sum(
            entry.get("costs", 0)
            for entries in project_index.values()
            for entry in entries
            if entry.get("month", "") == latest_month
        )

    return {
        "projects": len(project_index),
        "latest_month": latest_month,
        "latest_month_total_cost": round(latest_total_cost, 2),
    }


def build_output(payload: dict, input_path: Path) -> dict:
    project_index = build_project_index(payload)
    fragments = [
        build_fragment(project_name, monthly_entries)
        for project_name, monthly_entries in sorted(project_index.items(), key=lambda item: item[0].lower())
    ]
    return {
        "config": {
            "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
            "source": str(input_path),
            "project_count": len(project_index),
            "summary": aggregate_summary(project_index),
        },
        "fragments": fragments,
    }


def main() -> None:
    args = parse_args()
    payload = load_projects_payload(args.input)
    output = build_output(payload, args.input)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
