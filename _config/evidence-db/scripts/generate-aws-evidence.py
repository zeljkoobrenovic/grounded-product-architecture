#!/usr/bin/env python3
"""Transform AWS account cost data into evidence fragments."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_INPUT = SCRIPT_DIR.parent.parent / "data" / "aws" / "data" / "json" / "accounts.json"
DEFAULT_OUTPUT = SCRIPT_DIR / "aws" / "accounts.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate AWS account evidence fragments from account cost data."
    )
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT, help="Path to AWS accounts.json")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT, help="Path to generated evidence json")
    return parser.parse_args()


def load_accounts_payload(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"Expected an object in {path}")
    return data


def build_account_index(payload: dict) -> dict[str, list[dict]]:
    index: dict[str, list[dict]] = {}
    for month_entry in payload.get("perMonth", []):
        month = month_entry.get("month", "")
        for service_entry in month_entry.get("services", []):
            account_name = str(service_entry.get("service", "")).strip()
            if not account_name:
                continue
            entry = {
                "month": month,
                "costs": float(service_entry.get("costs", 0) or 0),
                "usage": float(service_entry.get("usage", 0) or 0),
            }
            index.setdefault(account_name, []).append(entry)
    return index


def build_facts(monthly_entries: list[dict]) -> list[dict]:
    if not monthly_entries:
        return []

    sorted_entries = sorted(monthly_entries, key=lambda item: item.get("month", ""), reverse=True)
    latest_entry = sorted_entries[0]
    peak_entry = max(monthly_entries, key=lambda item: item.get("costs", 0))
    total_cost = sum(item.get("costs", 0) for item in monthly_entries)
    total_usage = sum(item.get("usage", 0) for item in monthly_entries)

    return [
        {"value": round(latest_entry.get("costs", 0), 2), "label": "latest monthly cost", "summable": True},
        {"value": latest_entry.get("month", ""), "label": "latest month"},
        {"value": round(total_cost, 2), "label": "observed total cost"},
        {"value": round(peak_entry.get("costs", 0), 2), "label": "peak monthly cost"},
        {"value": peak_entry.get("month", ""), "label": "peak month"},
        {"value": round(total_usage, 4), "label": "observed total usage"},
        {"value": len(monthly_entries), "label": "months observed"},
    ]


def build_fragment(account_name: str, monthly_entries: list[dict]) -> dict:
    latest_entry = max(monthly_entries, key=lambda item: item.get("month", "")) if monthly_entries else {}
    latest_month = latest_entry.get("month", "") if latest_entry else ""
    latest_cost = round(latest_entry.get("costs", 0), 2) if latest_entry else 0

    description = f"AWS account cost evidence for {account_name}."
    if latest_month:
        description = f"{description} Latest observed month: {latest_month}."
    if latest_month:
        description = f"{description} Latest monthly cost: {latest_cost}."

    return {
        "id": f"aws/{account_name}",
        "type": "aws-account-cost",
        "icon": "evidence.png",
        "title": account_name,
        "description": description,
        "facts": build_facts(monthly_entries),
        "links": [],
        "tags": ["aws", "account-cost"],
    }


def aggregate_summary(account_index: dict[str, list[dict]]) -> dict:
    latest_month = ""
    latest_total_cost = 0.0

    all_months = sorted(
        {entry.get("month", "") for entries in account_index.values() for entry in entries if entry.get("month", "")},
        reverse=True,
    )
    if all_months:
        latest_month = all_months[0]
        latest_total_cost = sum(
            entry.get("costs", 0)
            for entries in account_index.values()
            for entry in entries
            if entry.get("month", "") == latest_month
        )

    return {
        "accounts": len(account_index),
        "latest_month": latest_month,
        "latest_month_total_cost": round(latest_total_cost, 2),
    }


def build_output(payload: dict, input_path: Path) -> dict:
    account_index = build_account_index(payload)
    fragments = [
        build_fragment(account_name, monthly_entries)
        for account_name, monthly_entries in sorted(account_index.items(), key=lambda item: item[0].lower())
    ]
    return {
        "config": {
            "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
            "source": str(input_path),
            "account_count": len(account_index),
            "summary": aggregate_summary(account_index),
        },
        "fragments": fragments,
    }


def main() -> None:
    args = parse_args()
    payload = load_accounts_payload(args.input)
    output = build_output(payload, args.input)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
