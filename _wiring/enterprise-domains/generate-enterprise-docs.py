import datetime
import json
import os
import shutil
from pathlib import Path


DATE_STRING = datetime.date.today().strftime('%Y-%m-%d')
ROOT = Path(__file__).resolve().parents[2]
CONFIG_ROOT = ROOT / "_config" / "enterprise-domains"
TEMPLATE_ROOT = ROOT / "_templates" / "enterprise"
DOCS_ROOT = ROOT / "docs" / "enterprise-domains"
RITUAL_TEMPLATE_ROOT = ROOT / "_templates" / "rituals"


SECTION_DEFS = [
    {
        "id": "motivation",
        "title": "Motivation",
        "file": ("motivation", "architecture-vision.json"),
        "description": "Architecture vision, drivers, principles, goals, and stakeholder concerns.",
        "extractors": [
            ("Architecture Goals", "Goals driving the target-state architecture.", lambda payload: payload.get("architectureVision", {}).get("goals", [])),
            ("Stakeholders", "Stakeholders and concerns shaping architecture decisions.", lambda payload: payload.get("architectureVision", {}).get("stakeholders", []))
        ]
    },
    {
        "id": "business",
        "title": "Business",
        "file": ("business", "business-architecture.json"),
        "description": "Business actors, capabilities, services, and value streams.",
        "extractors": [
            ("Business Actors", "The core business actors in the architecture scope.", lambda payload: payload.get("businessActors", [])),
            ("Business Capabilities", "Capabilities the enterprise must organize and govern.", lambda payload: payload.get("businessCapabilities", [])),
            ("Business Services", "Services exposed by the domain to support business outcomes.", lambda payload: payload.get("businessServices", [])),
            ("Value Streams", "End-to-end value flows crossing people, process, and systems.", lambda payload: payload.get("valueStreams", []))
        ]
    },
    {
        "id": "application",
        "title": "Application",
        "file": ("application", "application-architecture.json"),
        "description": "Application components, services, and interactions across the domain landscape.",
        "extractors": [
            ("Application Components", "The core application components in the domain.", lambda payload: payload.get("applicationComponents", [])),
            ("Application Interactions", "How major components exchange information or coordinate behavior.", lambda payload: payload.get("applicationInteractions", []))
        ]
    },
    {
        "id": "data",
        "title": "Data",
        "file": ("data", "data-architecture.json"),
        "description": "Data principles, logical data domains, information objects, and system-of-record patterns.",
        "extractors": [
            ("Data Domains", "Governed logical data domains and their information objects.", lambda payload: payload.get("dataDomains", []))
        ]
    },
    {
        "id": "technology",
        "title": "Technology",
        "file": ("technology", "technology-architecture.json"),
        "description": "Technology domains, enabling building blocks, and cross-cutting platform services.",
        "extractors": [
            ("Technology Domains", "Technology architecture building blocks grouped into coherent domains.", lambda payload: payload.get("technologyDomains", []))
        ]
    },
    {
        "id": "implementation",
        "title": "Implementation",
        "file": ("implementation", "implementation-migration.json"),
        "description": "Transition architectures, work packages, milestones, and governance checkpoints for change.",
        "extractors": [
            ("Transition Architectures", "Baseline, transition, and target architecture stages.", lambda payload: payload.get("transitionArchitectures", [])),
            ("Work Packages", "Sequenced change packages that implement the architecture.", lambda payload: payload.get("workPackages", [])),
            ("Release Milestones", "Key change milestones linked to implementation progress.", lambda payload: payload.get("releaseMilestones", []))
        ]
    },
    {
        "id": "governance",
        "title": "Governance",
        "file": ("governance", "architecture-governance.json"),
        "description": "Roles, forums, controls, and decision rights supporting architecture governance.",
        "extractors": [
            ("Roles", "Architecture and business roles participating in governance.", lambda payload: payload.get("roles", [])),
            ("Forums", "Governance forums sustaining architecture decision-making.", lambda payload: [{"name": value} for value in payload.get("forums", [])]),
            ("Controls", "Controls used to steer and assure architecture quality.", lambda payload: [{"name": value} for value in payload.get("controls", [])])
        ]
    },
    {
        "id": "rituals",
        "title": "Rituals",
        "file": ("rituals", "meetings.json"),
        "description": "Recurring architecture meetings and governance rituals.",
        "extractors": [
            ("Architecture Rituals", "Meetings that keep the enterprise architecture practice active and governed.", lambda payload: payload.get("meetings", []))
        ]
    }
]


def load_json(path):
    with path.open() as handle:
        return json.load(handle)


def copy_icons(source, target_folder):
    if source.exists():
        icon_folder = target_folder / "icons"
        icon_folder.mkdir(parents=True, exist_ok=True)
        for child in source.iterdir():
            if child.is_file():
                shutil.copy2(child, icon_folder / child.name)


def slugify(text):
    value = (text or "").strip().lower()
    chars = []
    last_dash = False
    for ch in value:
        if ch.isalnum():
            chars.append(ch)
            last_dash = False
        elif not last_dash:
            chars.append("-")
            last_dash = True
    return "".join(chars).strip("-")


def ensure_item(item, fallback_prefix, index):
    if isinstance(item, dict):
        normalized = dict(item)
    else:
        normalized = {"name": str(item)}
    item_id = normalized.get("id") or slugify(normalized.get("name") or normalized.get("title") or f"{fallback_prefix}-{index}")
    normalized["id"] = item_id or f"{fallback_prefix}-{index}"
    return normalized


def title_of(item):
    return item.get("title") or item.get("name") or item.get("id") or "Item"


def summary_of(item):
    for key in ["description", "goal", "responsibility", "focus", "statement", "concern"]:
        if item.get(key):
            return item.get(key)
    return "Detailed architecture element."


def subtitle_of(item):
    parts = []
    for key in ["type", "category", "horizon", "cadence", "maturityTarget", "relationship"]:
        if item.get(key):
            parts.append(str(item.get(key)))
    return " | ".join(parts[:2])


def pills_of(item):
    pills = []
    mapping = [
        ("owner", "Owner"),
        ("systemOfRecordPattern", "System of Record"),
        ("targetDate", "Target Date"),
        ("format", "Format"),
        ("durationMinutes", "Minutes")
    ]
    for key, meta in mapping:
        if item.get(key) not in (None, "", []):
            pills.append({"name": str(item.get(key)), "meta": meta})
    return pills[:3]


def section_groups(section_def, payload):
    groups = []
    all_items = []
    for index, extractor in enumerate(section_def["extractors"], start=1):
        title, description, fn = extractor
        raw_items = fn(payload)
        items = []
        for item_index, raw in enumerate(raw_items, start=1):
            normalized = ensure_item(raw, f"{section_def['id']}-{index}", item_index)
            items.append({
                "id": normalized["id"],
                "title": title_of(normalized),
                "subtitle": subtitle_of(normalized),
                "summary": summary_of(normalized),
                "description": normalized.get("description", ""),
                "pills": pills_of(normalized),
                "raw": normalized
            })
        if items:
            groups.append({"title": title, "description": description, "items": items})
            all_items.extend(items)
    return groups, all_items


def build_stats(section_def, payload, all_items):
    stats = [{"label": "Entities", "value": len(all_items)}]
    if section_def["id"] == "motivation":
        stats.append({"label": "Principles", "value": len(payload.get("architectureVision", {}).get("principles", []))})
        stats.append({"label": "Drivers", "value": len(payload.get("architectureVision", {}).get("drivers", []))})
    elif section_def["id"] == "business":
        stats.append({"label": "Capabilities", "value": len(payload.get("businessCapabilities", []))})
        stats.append({"label": "Value Streams", "value": len(payload.get("valueStreams", []))})
    elif section_def["id"] == "application":
        stats.append({"label": "Components", "value": len(payload.get("applicationComponents", []))})
        stats.append({"label": "Interactions", "value": len(payload.get("applicationInteractions", []))})
    elif section_def["id"] == "data":
        stats.append({"label": "Data Domains", "value": len(payload.get("dataDomains", []))})
        stats.append({"label": "Principles", "value": len(payload.get("dataPrinciples", []))})
    elif section_def["id"] == "technology":
        stats.append({"label": "Tech Domains", "value": len(payload.get("technologyDomains", []))})
        stats.append({"label": "Cross-Cutting", "value": len(payload.get("crossCuttingServices", []))})
    elif section_def["id"] == "implementation":
        stats.append({"label": "Work Packages", "value": len(payload.get("workPackages", []))})
        stats.append({"label": "Milestones", "value": len(payload.get("releaseMilestones", []))})
    elif section_def["id"] == "governance":
        stats.append({"label": "Roles", "value": len(payload.get("roles", []))})
        stats.append({"label": "Forums", "value": len(payload.get("forums", []))})
    elif section_def["id"] == "rituals":
        stats.append({"label": "Meetings", "value": len(payload.get("meetings", []))})
        cadences = len(set(item.get("cadence", "") for item in payload.get("meetings", [])))
        stats.append({"label": "Cadences", "value": cadences})
    return stats


def nav_flags(section_id):
    flags = {}
    for entry in SECTION_DEFS:
        flags[f"{entry['id']}_active"] = "active" if entry["id"] == section_id else ""
    return flags


def write_file(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w") as handle:
        handle.write(content)


def render_template(template_name, replacements):
    template = (TEMPLATE_ROOT / template_name).read_text()
    for key, value in replacements.items():
        template = template.replace("${" + key + "}", value)
    return template


def render_start(domain):
    folder = DOCS_ROOT / domain["id"] / "start"
    if folder.exists():
        shutil.rmtree(folder)
    folder.mkdir(parents=True, exist_ok=True)
    copy_icons(CONFIG_ROOT / domain["id"] / "start" / "icons", folder)
    page = {
        "stats": [
            {"label": "Viewpoints", "value": 7},
            {"label": "Governance", "value": 1},
            {"label": "Ritual Sets", "value": 1}
        ],
        "sections": [
            {"group": "Architecture Core", "title": "Motivation", "description": "Vision, principles, goals, and stakeholder concerns.", "meta": "Why change and what matters", "href": "../motivation/index.html"},
            {"group": "Architecture Core", "title": "Business", "description": "Business actors, capabilities, services, and value streams.", "meta": "Operating model and business structure", "href": "../business/index.html"},
            {"group": "Architecture Core", "title": "Application", "description": "Application components, services, and interactions.", "meta": "Application landscape and service structure", "href": "../application/index.html"},
            {"group": "Architecture Core", "title": "Data", "description": "Logical data domains, information objects, and data principles.", "meta": "Information structure and stewardship", "href": "../data/index.html"},
            {"group": "Architecture Core", "title": "Technology", "description": "Technology domains, standards, and cross-cutting platform services.", "meta": "Infrastructure and platform direction", "href": "../technology/index.html"},
            {"group": "Change", "title": "Implementation", "description": "Transition architectures, work packages, and milestones.", "meta": "How target architecture is delivered", "href": "../implementation/index.html"},
            {"group": "Change", "title": "Governance", "description": "Roles, forums, controls, and decision rights.", "meta": "Architecture governance model", "href": "../governance/index.html"},
            {"group": "Practice", "title": "Rituals", "description": "Recurring meetings that keep the EA practice running.", "meta": "Architecture operating cadence", "href": "../rituals/index.html"}
        ]
    }
    content = render_template("start.html", {
        "domain_name": domain["name"],
        "domain_description": domain["description"],
        "page": json.dumps(page)
    })
    write_file(folder / "index.html", content)


def render_section(domain, section_def):
    if section_def["id"] == "rituals":
        payload = load_json(CONFIG_ROOT / "rituals" / section_def["file"][1])
    else:
        payload = load_json(CONFIG_ROOT / domain["id"] / section_def["file"][0] / section_def["file"][1])
    groups, all_items = section_groups(section_def, payload)
    page = {"stats": build_stats(section_def, payload, all_items), "sections": groups}
    folder = DOCS_ROOT / domain["id"] / section_def["id"]
    if folder.exists():
        shutil.rmtree(folder)
    folder.mkdir(parents=True, exist_ok=True)
    if section_def["id"] == "rituals":
        copy_icons(RITUAL_TEMPLATE_ROOT / "icons", folder)
        section_nav = """
<div class="section-nav">
    <a class="section-link" href="../start/index.html">Home</a>
    <a class="section-link" href="../motivation/index.html">Motivation</a>
    <a class="section-link" href="../business/index.html">Business</a>
    <a class="section-link" href="../application/index.html">Application</a>
    <a class="section-link" href="../data/index.html">Data</a>
    <a class="section-link" href="../technology/index.html">Technology</a>
    <a class="section-link" href="../implementation/index.html">Implementation</a>
    <a class="section-link" href="../governance/index.html">Governance</a>
    <a class="section-link active" href="../rituals/index.html">Rituals</a>
</div>
""".strip()
        rituals_template = (RITUAL_TEMPLATE_ROOT / "index.html").read_text()
        content = (rituals_template
                   .replace('${date}', DATE_STRING)
                   .replace('${domain_name}', domain["name"])
                   .replace('${domain_description}', domain["description"])
                   .replace('${section_nav}', section_nav)
                   .replace('${rituals}', json.dumps(payload)))
        write_file(folder / "index.html", content)
    else:
        content = render_template("section_index.html", {
            "domain_name": domain["name"],
            "page_title": section_def["title"],
            "page_description": section_def["description"],
            "page": json.dumps(page),
            **nav_flags(section_def["id"])
        })
        write_file(folder / "index.html", content)
    landing_folder = folder / "landing_pages"
    landing_folder.mkdir(parents=True, exist_ok=True)
    for group in groups:
        for item in group["items"]:
            if section_def["id"] == "rituals":
                rituals_landing = (RITUAL_TEMPLATE_ROOT / "landing_page.html").read_text()
                raw = item["raw"]
                landing = (rituals_landing
                           .replace('${date}', DATE_STRING)
                           .replace('${domain_name}', domain["name"])
                           .replace('${meeting_title}', raw.get("title", "Ritual"))
                           .replace('${meeting}', json.dumps(raw)))
            else:
                landing = render_template("entity_landing.html", {
                    "domain_name": domain["name"],
                    "section_title": group["title"],
                    "entity_title": item["title"],
                    "entity": json.dumps(item),
                    "page_meta": json.dumps({
                        "domainName": domain["name"],
                        "pageTitle": section_def["title"],
                        "subtitle": item.get("subtitle", "")
                    })
                })
            write_file(landing_folder / f"{item['id']}.html", landing)


def main():
    config = load_json(CONFIG_ROOT / "config.json")
    for domain in config["domains"]:
        render_start(domain)
        for section_def in SECTION_DEFS:
            render_section(domain, section_def)


if __name__ == "__main__":
    main()
