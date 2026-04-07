from __future__ import annotations

import csv
import datetime
import json
import shutil
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[2]
CONFIG_DIR = ROOT_DIR / "_data" / "data" / "gcp"
TEMPLATES_DIR = ROOT_DIR / "_templates" / "data-explorers" / "gcp"
OUTPUT_DIR = ROOT_DIR / "docs" / "data-explorers" / "gcp"
ICON_SOURCE_DIR = CONFIG_DIR / "icons" / "logos"
MEDIA_LINK_PREFIX = "../logos/"
GROUP_SPECS = (
    {"name": "services", "label": "Services", "service_index": 1, "cost_index": 3},
    {"name": "projects", "label": "Projects", "service_index": 1, "cost_index": 4},
    {"name": "project-hierarchy", "label": "Project Hierarchy", "service_index": 2, "cost_index": 5},
    {"name": "regions", "label": "Regions", "service_index": 1, "cost_index": 2},
    {"name": "skus", "label": "SKUs", "service_index": 3, "cost_index": 7},
)


def parse_csv_group(group: str, service_index: int, cost_index: int) -> dict:
    csv_file = CONFIG_DIR / "data" / "csv" / f"{group}.csv"
    with csv_file.open(newline="", encoding="utf-8") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",", quotechar='"')

        first_row = True
        months: list[dict] = []
        months_map: dict[str, dict] = {}
        services: list[str] = []
        services_map: dict[str, bool] = {}

        for row in csvreader:
            if first_row:
                first_row = False
                continue

            month = row[0].strip() if len(row) > 0 else ""
            service = row[service_index].strip() if len(row) > service_index else ""

            if not month or not service:
                continue

            try:
                cost = float(row[cost_index])
                discount = float(row[cost_index + 1])
            except (IndexError, ValueError):
                continue

            if service not in services_map:
                services.append(service)
                services_map[service] = True

            if month not in months_map:
                months_map[month] = {"month": month, "total": 0, "services": []}
                months.append(months_map[month])

            entry = {
                "service": service,
                "usage": 0,
                "costs": cost + discount,
                "costs_without_discount": cost,
            }
            months_map[month]["services"].append(entry)
            months_map[month]["total"] += entry["costs"]

    parsed = {"services": services, "perMonth": months}
    json_file = CONFIG_DIR / "data" / "json" / f"{group}.json"
    json_file.parent.mkdir(parents=True, exist_ok=True)
    json_file.write_text(json.dumps(parsed), encoding="utf-8")
    return parsed


def render_month_pages(group: str, data: dict, template: str) -> None:
    group_dir = OUTPUT_DIR / group
    group_dir.mkdir(parents=True, exist_ok=True)

    date_string = datetime.date.today().strftime("%Y-%m-%d")
    months = [source["month"] for source in data["perMonth"]]
    latest_source = data["perMonth"][-1]

    for source in data["perMonth"]:
        content = (
            template.replace("${data}", json.dumps(source["services"]))
            .replace("${months}", json.dumps(months))
            .replace("${totalCosts}", str(source["total"]))
            .replace("${focusMonth}", source["month"])
            .replace("${date}", date_string)
            .replace("${source}", source["month"].lower())
            .replace("${sourceTitle}", source["month"])
            .replace("${media-link-prefix}", MEDIA_LINK_PREFIX)
        )
        (group_dir / f"{source['month'].lower()}.html").write_text(content, encoding="utf-8")

    latest_content = (
        template.replace("${data}", json.dumps(latest_source["services"]))
        .replace("${months}", json.dumps(months))
        .replace("${totalCosts}", str(latest_source["total"]))
        .replace("${focusMonth}", latest_source["month"])
        .replace("${date}", date_string)
        .replace("${source}", "latest")
        .replace("${sourceTitle}", "latest")
        .replace("${media-link-prefix}", MEDIA_LINK_PREFIX)
    )
    (group_dir / "latest.html").write_text(latest_content, encoding="utf-8")


def render_trends_page(group: str, data: dict, template: str) -> None:
    group_dir = OUTPUT_DIR / group
    group_dir.mkdir(parents=True, exist_ok=True)

    date_string = datetime.date.today().strftime("%Y-%m-%d")
    months = [source["month"] for source in data["perMonth"]]
    content = (
        template.replace("${all}", json.dumps(data["perMonth"]))
        .replace("${data}", json.dumps(data["perMonth"][-1]["services"]))
        .replace("${months}", json.dumps(months))
        .replace("${date}", date_string)
        .replace("${media-link-prefix}", MEDIA_LINK_PREFIX)
    )
    (group_dir / "trends.html").write_text(content, encoding="utf-8")


def render_group_index(group: str, active_group: str) -> None:
    template = (TEMPLATES_DIR / "group-index.html").read_text(encoding="utf-8")
    tab_template = (TEMPLATES_DIR / "group-tab.html").read_text(encoding="utf-8")

    tabs = []
    for spec in GROUP_SPECS:
        background = "#c0c0c0" if spec["name"] == active_group else "#f6f6f6"
        margin_right = "40px" if spec["name"] in {"regions", "skus"} else "10px"
        tabs.append(
            tab_template.replace("${marginRight}", margin_right)
            .replace("${background}", background)
            .replace("${group}", spec["name"])
            .replace("${label}", spec["label"])
        )

    content = template.replace("${tabs}", "".join(tabs))
    (OUTPUT_DIR / group / "index.html").write_text(content, encoding="utf-8")


def write_root_redirect() -> None:
    content = (TEMPLATES_DIR / "root-redirect.html").read_text(encoding="utf-8")
    (OUTPUT_DIR / "index.html").write_text(content, encoding="utf-8")


def copy_icons() -> None:
    target_dir = OUTPUT_DIR / "logos"
    if target_dir.exists():
        shutil.rmtree(target_dir)
    shutil.copytree(ICON_SOURCE_DIR, target_dir)


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    copy_icons()

    group_template = (TEMPLATES_DIR / "gcp.html").read_text(encoding="utf-8")
    trends_template = (TEMPLATES_DIR / "gcp-trends.html").read_text(encoding="utf-8")

    parsed_data = {}
    for spec in GROUP_SPECS:
        parsed_data[spec["name"]] = parse_csv_group(spec["name"], spec["service_index"], spec["cost_index"])

    for spec in GROUP_SPECS:
        render_month_pages(spec["name"], parsed_data[spec["name"]], group_template)
        render_group_index(spec["name"], spec["name"])

    for spec in GROUP_SPECS:
        render_trends_page(spec["name"], parsed_data[spec["name"]], trends_template)

    write_root_redirect()


if __name__ == "__main__":
    main()
