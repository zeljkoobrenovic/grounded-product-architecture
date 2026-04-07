from __future__ import annotations

import datetime
import json
import shutil
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[2]
CONFIG_DIR = ROOT_DIR / "_data" / "data" / "brands"
TEMPLATES_DIR = ROOT_DIR / "_templates" / "data-explorers" / "brands"
OUTPUT_DIR = ROOT_DIR / "docs" / "data-explorers" / "brands"
DATA_FILE = CONFIG_DIR / "data" / "brands.json"
TEMPLATE_FILE = TEMPLATES_DIR / "brands.html"
ICON_DIR = CONFIG_DIR / "icons"
LOGO_DIR = CONFIG_DIR / "logos"
OUTPUT_ICON_DIR = OUTPUT_DIR / "icons"
OUTPUT_LOGO_DIR = OUTPUT_DIR / "logos"
SOURCE_LINK = "https://docs.google.com/spreadsheets/d/195iHjfUCGlHEREka2hvWxV9WWBeX9PfDp6OizYSWqiQ/edit?usp=sharing"


def copy_directory(source: Path, target: Path) -> None:
    if target.exists():
        shutil.rmtree(target)
    if source.exists():
        shutil.copytree(source, target)


def write_root_redirect() -> None:
    root_page = OUTPUT_DIR / "brands.html"
    if root_page.exists():
        OUTPUT_DIR.joinpath("index.html").write_text(root_page.read_text(encoding="utf-8"), encoding="utf-8")


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    copy_directory(ICON_DIR, OUTPUT_ICON_DIR)
    copy_directory(LOGO_DIR, OUTPUT_LOGO_DIR)

    data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    template = TEMPLATE_FILE.read_text(encoding="utf-8")
    date_string = datetime.date.today().strftime("%Y-%m-%d")

    for source in data["data"]:
        source_name = source["source"]
        content = (
            template.replace("${data}", json.dumps(source["data"]))
            .replace("${date}", date_string)
            .replace("${source}", source_name.lower())
            .replace("${source_title}", source_name)
            .replace("${source_link}", SOURCE_LINK)
        )

        OUTPUT_DIR.joinpath(f"{source_name.lower()}.html").write_text(
            content.replace('class="hidden"', ""),
            encoding="utf-8",
        )
        OUTPUT_DIR.joinpath(f"{source_name.lower()}-embed.html").write_text(
            content,
            encoding="utf-8",
        )

    write_root_redirect()


if __name__ == "__main__":
    main()
