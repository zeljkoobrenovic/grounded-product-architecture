from __future__ import annotations

import csv
import datetime
import json
import shutil
import re
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[2]
CONFIG_DIR = ROOT_DIR / "_config" / "evidence" / "aws"
TEMPLATES_DIR = ROOT_DIR / "_templates" / "evidence" / "aws"
OUTPUT_DIR = ROOT_DIR / "docs" / "evidence" / "aws"
TEMPLATE_ICON_DIR = TEMPLATES_DIR / "icons"
REMOTE_MEDIA_PREFIX = "https://zeljkoobrenovic.github.io/sokrates-media/"
AWS_GROUPS = ("services", "regions", "accounts", "api-operations")


def ignore(name: str) -> bool:
    lowered = name.lower()

    if lowered in {
        "total cost",
        "total costs",
        "refund",
        "savings plans for  compute usage",
        "savings plans for compute usage",
    }:
        return True

    return (
        lowered.startswith("no tagkey")
        or lowered.startswith("ocb reinvent passes")
        or lowered.startswith("no database engine")
        or lowered.startswith("no instance type")
    )


def rename(name: str) -> str:
    if name.startswith("EC2"):
        return "EC2"
    if name.startswith("db."):
        return "DB"
    if name.startswith("ml."):
        return "ML"
    if name.startswith("cache."):
        return "CACHE"

    info = {
        "m": "general",
        "t": "general",
        "c": "compute",
        "r": "memory",
        "x": "memory",
        "z": "memory",
        "p": "accelerate",
        "g": "accelerate",
        "i": "storage",
        "d": "stroage",
    }
    letters = ["m", "t", "r", "c", "g", "i", "ra", "mac", "dc", "ds", "p", "x", "z"]

    for letter in letters:
        for i in range(1, 20):
            prefix = f"{letter}{i}"
            if name.startswith(prefix):
                return f"{letter.upper()} {info[letter]}".strip() if info.get(letter) else letter.upper()

    if name.startswith("Kinesis"):
        return "Kinesis"
    if name.startswith("AWS EMEA SARL"):
        return "Amazon Web Services EMEA SARL"
    if name.startswith("Amazon Web Services, Inc."):
        return "Amazon Web Services EMEA SARL"

    return name


def parse_csv_group(group: str) -> dict:
    csv_file = CONFIG_DIR / "data" / "csv" / f"{group}.csv"
    with csv_file.open(newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",", quotechar='"')

        first_row = True
        columns: list[str] = []
        months: list[dict] = []

        for row in csvreader:
            month = row[0]
            if len(month) == 10:
                month = month[0:7]

            if first_row:
                for item in row[1:]:
                    service = item.replace("($)", "").strip()
                    service = re.sub(r"\:.*", "", service)
                    columns.append(service)
                first_row = False
                continue

            if not month.startswith("20"):
                continue

            month_object = {"month": month, "total": 0, "services": []}
            months.append(month_object)
            services_map: dict[str, dict] = {}

            for i, cost in enumerate(row[1:]):
                column = columns[i]
                if ignore(column):
                    continue

                value = float(cost) if cost else 0.0
                month_object["total"] += value
                column = rename(column)

                if column not in services_map:
                    services_map[column] = {"service": column, "usage": 0, "costs": value}
                    month_object["services"].append(services_map[column])
                else:
                    services_map[column]["costs"] += value

            for item in month_object["services"]:
                item["usage"] = item["costs"] / month_object["total"] if month_object["total"] else 0

    active_columns: list[str] = []
    for column in columns:
        if ignore(column):
            continue
        renamed = rename(column)
        if renamed not in active_columns:
            active_columns.append(renamed)

    parsed = {"services": active_columns, "perMonth": months}
    json_file = CONFIG_DIR / "data" / "json" / f"{group}.json"
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
            .replace("${media-link-prefix}", REMOTE_MEDIA_PREFIX)
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
        .replace("${media-link-prefix}", REMOTE_MEDIA_PREFIX)
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
        .replace("${media-link-prefix}", REMOTE_MEDIA_PREFIX)
    )
    (group_dir / "trends.html").write_text(content, encoding="utf-8")


def render_group_index(group: str, active_group: str) -> None:
    group_index_template = (TEMPLATES_DIR / "group-index.html").read_text(encoding="utf-8")
    group_tab_template = (TEMPLATES_DIR / "group-tab.html").read_text(encoding="utf-8")
    tabs = []
    for tab_group, label in (
        ("services", "Services"),
        ("regions", "Regions"),
        ("accounts", "Accounts"),
        ("api-operations", "API Operations"),
    ):
        background = "#c0c0c0" if tab_group == active_group else "#f6f6f6"
        margin_right = "10px" if tab_group in {"services", "api-operations"} else "40px"
        tabs.append(
            group_tab_template
            .replace("${marginRight}", margin_right)
            .replace("${background}", background)
            .replace("${group}", tab_group)
            .replace("${label}", label)
        )

    content = group_index_template.replace("${tabs}", "".join(tabs))
    (OUTPUT_DIR / group / "index.html").write_text(content, encoding="utf-8")


def write_root_redirect() -> None:
    content = (TEMPLATES_DIR / "root-redirect.html").read_text(encoding="utf-8").replace("docs/services/index.html", "services/index.html")
    (OUTPUT_DIR / "index.html").write_text(content, encoding="utf-8")


def copy_icons() -> None:
    target = OUTPUT_DIR / "logos"
    if target.exists():
        shutil.rmtree(target)
    if TEMPLATE_ICON_DIR.exists():
        shutil.copytree(TEMPLATE_ICON_DIR / "logos", target)


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    copy_icons()

    aws_template = (TEMPLATES_DIR / "aws.html").read_text(encoding="utf-8")
    trends_template = (TEMPLATES_DIR / "aws-trends.html").read_text(encoding="utf-8")

    for group in AWS_GROUPS:
        data = parse_csv_group(group)
        render_month_pages(group, data, aws_template)
        render_trends_page(group, data, trends_template)
        render_group_index(group, group)

    write_root_redirect()


if __name__ == "__main__":
    main()
