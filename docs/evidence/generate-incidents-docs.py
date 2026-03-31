from __future__ import annotations

import datetime
import json
import shutil
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[2]
CONFIG_DIR = ROOT_DIR / "_config" / "evidence" / "incidents"
TEMPLATES_DIR = ROOT_DIR / "_templates" / "evidence" / "incidents"
OUTPUT_DIR = ROOT_DIR / "docs" / "evidence" / "incidents"
DATA_DIR = CONFIG_DIR / "data"
ASSETS_DIR = CONFIG_DIR / "assets"
TEMPLATE_FILE = TEMPLATES_DIR / "index.html"
SOURCE_LINK = "https://docs.google.com/spreadsheets/d/1uXrO5P-ysGQWTgfMHasojYg7bRgfTZwNqpCKUIV_ekM/edit?usp=sharing"


def copy_assets() -> None:
    target = OUTPUT_DIR / "assets"
    if target.exists():
        shutil.rmtree(target)
    if ASSETS_DIR.exists():
        shutil.copytree(ASSETS_DIR, target)


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    copy_assets()

    data = json.loads((DATA_DIR / "incidents.json").read_text(encoding="utf-8"))
    template = TEMPLATE_FILE.read_text(encoding="utf-8")
    date_string = datetime.date.today().strftime("%Y-%m-%d")

    for source in data["data"]:
        content = (
            template.replace("${date}", date_string)
            .replace("${source_link}", SOURCE_LINK)
            .replace("${data}", json.dumps(source["data"]))
        )
        (OUTPUT_DIR / f"{source['source']}.html").write_text(content, encoding="utf-8")

    index_content = (
        template.replace("${date}", date_string)
        .replace("${source_link}", SOURCE_LINK)
        .replace("${data}", json.dumps(data["data"][0]["data"]))
    )
    (OUTPUT_DIR / "index.html").write_text(index_content, encoding="utf-8")


if __name__ == "__main__":
    main()
