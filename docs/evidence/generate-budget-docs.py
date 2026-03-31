from __future__ import annotations

import datetime
import json
import shutil
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[2]
CONFIG_DIR = ROOT_DIR / "_config" / "evidence" / "budget"
TEMPLATES_DIR = ROOT_DIR / "_templates" / "evidence" / "budget"
OUTPUT_DIR = ROOT_DIR / "docs" / "evidence" / "budget"
DATA_FILE = CONFIG_DIR / "data" / "budget.json"
TEMPLATE_FILE = TEMPLATES_DIR / "budget.html"
ICON_DIR = CONFIG_DIR / "icons"
OUTPUT_ICON_DIR = OUTPUT_DIR / "icons"


def copy_icons() -> None:
    if OUTPUT_ICON_DIR.exists():
        shutil.rmtree(OUTPUT_ICON_DIR)
    if ICON_DIR.exists():
        shutil.copytree(ICON_DIR, OUTPUT_ICON_DIR)


def write_root_redirect() -> None:
    root_page = OUTPUT_DIR / "index.html"
    if root_page.exists():
        return


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    copy_icons()

    data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    template = TEMPLATE_FILE.read_text(encoding="utf-8")
    date_string = datetime.date.today().strftime("%Y-%m-%d")

    for group in data["data"]:
        content = (
            template.replace("${date}", date_string)
            .replace("${data}", json.dumps(group["data"]))
        )
        OUTPUT_DIR.joinpath("index.html").write_text(content, encoding="utf-8")

    write_root_redirect()


if __name__ == "__main__":
    main()
