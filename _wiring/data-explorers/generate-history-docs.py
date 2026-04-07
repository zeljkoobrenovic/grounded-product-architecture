from __future__ import annotations

import datetime
import json
import shutil
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[2]
CONFIG_DIR = ROOT_DIR / "_data" / "data" / "history"
TEMPLATES_DIR = ROOT_DIR / "_templates" / "data-explorers" / "history"
OUTPUT_DIR = ROOT_DIR / "docs" / "data-explorers" / "history"
DATA_DIR = CONFIG_DIR / "data"
ASSETS_DIR = CONFIG_DIR / "assets"
TEMPLATE_FILE = TEMPLATES_DIR / "history.html"


def copy_assets() -> None:
    target = OUTPUT_DIR / "assets"
    if target.exists():
        shutil.rmtree(target)
    if ASSETS_DIR.exists():
        shutil.copytree(ASSETS_DIR, target)


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    copy_assets()

    data = json.loads((DATA_DIR / "history.json").read_text(encoding="utf-8"))
    logos = json.loads((DATA_DIR / "logos.json").read_text(encoding="utf-8"))
    template = TEMPLATE_FILE.read_text(encoding="utf-8")
    date_string = datetime.date.today().strftime("%Y-%m-%d")

    for source in data["data"]:
        content = template.replace("${logos}", json.dumps(logos)).replace(
            "${data}", json.dumps([source], ensure_ascii=False)
        )
        (OUTPUT_DIR / f"{source['source']}.html").write_text(content, encoding="utf-8")

    content = (
        template.replace("${logos}", json.dumps(logos))
        .replace("${date}", date_string)
        .replace("${data}", json.dumps(data["data"], ensure_ascii=False))
    )
    (OUTPUT_DIR / "index.html").write_text(content.replace('class="hidden', ""), encoding="utf-8")
    (OUTPUT_DIR / "embed.html").write_text(content, encoding="utf-8")


if __name__ == "__main__":
    main()
