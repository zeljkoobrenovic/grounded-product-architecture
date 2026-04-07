from __future__ import annotations

import json
import shutil
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[2]
CONFIG_FILE = ROOT_DIR / "_data" / "data" / "workday" / "workday.json"
TEMPLATES_DIR = ROOT_DIR / "_templates" / "data-explorers" / "workday"
OUTPUT_DIR = ROOT_DIR / "docs" / "data-explorers" / "workday"
ICON_SOURCE_DIR = TEMPLATES_DIR / "icons"
IMAGE_SOURCE_DIR = TEMPLATES_DIR / "images"


def load_workday_records() -> list[dict]:
    with CONFIG_FILE.open(encoding="utf-8") as handle:
        payload = json.load(handle)

    records: list[dict] = []
    for section in payload.get("data", []):
        for item in section.get("data", []):
            if isinstance(item, dict):
                records.append(item)
    return records


def render_template(template_name: str, destination_name: str, records: list[dict]) -> None:
    template = (TEMPLATES_DIR / template_name).read_text(encoding="utf-8")
    content = template.replace("${data}", json.dumps(records))
    (OUTPUT_DIR / destination_name).write_text(content, encoding="utf-8")


def copy_icons() -> None:
    target_dir = OUTPUT_DIR / "icons"
    if target_dir.exists():
        shutil.rmtree(target_dir)
    if ICON_SOURCE_DIR.exists():
        shutil.copytree(ICON_SOURCE_DIR, target_dir)


def copy_images() -> None:
    target_dir = OUTPUT_DIR / "images"
    if target_dir.exists():
        shutil.rmtree(target_dir)
    if IMAGE_SOURCE_DIR.exists():
        shutil.copytree(IMAGE_SOURCE_DIR, target_dir)


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    copy_icons()
    copy_images()

    records = load_workday_records()
    render_template("workday.html", "index.html", records)
    render_template("force-graph-3d.html", "force-graph-3d.html", records)


if __name__ == "__main__":
    main()
