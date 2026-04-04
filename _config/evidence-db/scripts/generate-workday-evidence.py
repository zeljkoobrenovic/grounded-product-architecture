#!/usr/bin/env python3
"""Transform Workday org chart data into evidence fragments."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict, deque
from datetime import datetime, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_INPUT = SCRIPT_DIR.parent.parent / "data" / "workday" / "workday.json"
DEFAULT_OUTPUT = SCRIPT_DIR.parent / "database" / "workday.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate Workday evidence fragments from org chart data."
    )
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT, help="Path to Workday workday.json")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT, help="Path to generated evidence json")
    return parser.parse_args()


def load_payload(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"Expected an object in {path}")
    return data


def extract_people(payload: dict) -> list[dict]:
    for section in payload.get("data", []):
        if section.get("source") == "Org Chart":
            people = section.get("data", [])
            if not isinstance(people, list):
                raise ValueError("Expected Org Chart data to be a list")
            return people
    return []


def build_children_index(people: list[dict]) -> dict[str, list[str]]:
    children_by_manager: dict[str, list[str]] = defaultdict(list)
    valid_ids = {person.get("unique_identifier") for person in people if person.get("unique_identifier")}
    for person in people:
        manager_id = person.get("reports_to")
        person_id = person.get("unique_identifier")
        if manager_id and manager_id in valid_ids and person_id:
            children_by_manager[manager_id].append(person_id)
    return children_by_manager


def build_level_index(people: list[dict], children_by_manager: dict[str, list[str]]) -> dict[str, int]:
    roots = [person for person in people if not person.get("reports_to")]
    levels: dict[str, int] = {}
    queue: deque[tuple[str, int]] = deque()

    for root in roots:
        root_id = root.get("unique_identifier")
        if root_id:
            queue.append((root_id, 0))

    while queue:
        person_id, level = queue.popleft()
        if person_id in levels:
            continue
        levels[person_id] = level
        for child_id in children_by_manager.get(person_id, []):
            queue.append((child_id, level + 1))

    return levels


def build_facts(person: dict, children_by_manager: dict[str, list[str]], levels: dict[str, int]) -> list[dict]:
    person_id = person.get("unique_identifier", "")
    location = person.get("line_detail_2", "")
    role = person.get("line_detail_1", "")
    manager_id = person.get("reports_to", "")
    direct_reports = len(children_by_manager.get(person_id, []))

    facts = [
        {"label": "role", "value": role or "Unknown"},
        {"label": "location", "value": location or "Unknown"}
    ]
    if (direct_reports > 0): facts.append({"value": direct_reports, "label": "direct reports"})

    if manager_id:
        facts.append({"value": manager_id, "label": "manager"})
    return facts


def build_fragment(person: dict, children_by_manager: dict[str, list[str]], levels: dict[str, int]) -> dict:
    person_name = str(person.get("name", "")).strip()
    role = str(person.get("line_detail_1", "")).strip()
    location = str(person.get("line_detail_2", "")).strip()
    manager_id = str(person.get("reports_to", "")).strip()

    return {
        "type": "workday-org-person",
        "id": f"workday/{person_name}",
        "icon": "person.png",
        "title": person_name,
        "facts": build_facts(person, children_by_manager, levels),
        "links": [],
        "tags": [],
    }


def aggregate_summary(people: list[dict], children_by_manager: dict[str, list[str]], levels: dict[str, int]) -> dict:
    locations = {
        str(person.get("line_detail_2", "")).strip()
        for person in people
        if str(person.get("line_detail_2", "")).strip()
    }
    roles = {
        str(person.get("line_detail_1", "")).strip()
        for person in people
        if str(person.get("line_detail_1", "")).strip()
    }
    return {
        "people": len(people),
        "roots": sum(1 for person in people if not person.get("reports_to")),
        "managers": sum(1 for person in people if children_by_manager.get(person.get("unique_identifier", ""))),
        "locations": len(locations),
        "roles": len(roles),
        "max_org_level": max(levels.values(), default=0),
    }


def build_output(payload: dict, input_path: Path) -> dict:
    people = extract_people(payload)
    children_by_manager = build_children_index(people)
    levels = build_level_index(people, children_by_manager)
    fragments = [
        build_fragment(person, children_by_manager, levels)
        for person in sorted(people, key=lambda item: str(item.get("unique_identifier", "")))
        if str(person.get("unique_identifier", "")).strip()
    ]
    return {
        "config": {
            "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
            "source": str(input_path),
            "export_date": payload.get("metadata", {}).get("exportDate", ""),
            "people_count": len(fragments),
            "summary": aggregate_summary(people, children_by_manager, levels),
        },
        "fragments": fragments,
    }


def main() -> None:
    args = parse_args()
    payload = load_payload(args.input)
    output = build_output(payload, args.input)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
