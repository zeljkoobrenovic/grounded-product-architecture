import calendar
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1] / "product-domains"


def quarter_end(year, quarter):
    month = quarter * 3
    return f"{year:04d}-{month:02d}-{calendar.monthrange(year, month)[1]:02d}"


def parse_quarter(quarter_key):
    year_text, quarter_text = quarter_key.split("-Q")
    return int(year_text), int(quarter_text)


def next_quarter(year, quarter):
    if quarter == 4:
        return year + 1, 1
    return year, quarter + 1


def target2_date(year, quarter):
    if quarter in (1, 2):
        return f"{year:04d}-12-31", f"{year}-year-end target"
    if quarter == 3:
        next_year, next_q = next_quarter(year, 4)
        return quarter_end(next_year, next_q), f"{next_year}-Q{next_q} target"
    return quarter_end(year + 1, 2), f"{year + 1}-Q2 target"


def target1_date(year, quarter):
    next_year, next_q = next_quarter(year, quarter)
    return quarter_end(next_year, next_q), f"{next_year}-Q{next_q} target"


def confidence_for_status(status):
    mapping = {
        "achieved": "green",
        "on-track": "green",
        "at-risk": "amber",
        "off-track": "red",
        "planned": "undefined",
        "active": "undefined",
        "archived": "undefined"
    }
    return mapping.get((status or "").strip().lower(), "undefined")


def soften_confidence(confidence, status):
    if (status or "").strip().lower() == "achieved":
        return confidence
    mapping = {
        "green": "amber",
        "amber": "red",
        "red": "red",
        "undefined": "undefined"
    }
    return mapping.get(confidence, "undefined")


def clean_text(text):
    value = (text or "").strip()
    if not value:
        return ""
    return value[:-1] if value.endswith(".") else value


def lc_first(text):
    value = clean_text(text)
    if not value:
        return ""
    return value[0].lower() + value[1:]


def projected_value(metric, direction, horizon, target_text, statement_text):
    metric_name = metric or "the metric"
    target_fragment = lc_first(target_text) or f"improve {metric_name}"
    statement_fragment = lc_first(statement_text)
    if horizon == 1:
        if statement_fragment:
            return f"Current estimate: {metric_name} moves far enough to show clear momentum toward {target_fragment}, driven by {statement_fragment}."
        return f"Current estimate: {metric_name} moves far enough to show clear momentum toward {target_fragment}."

    if (direction or "").strip().lower() == "decrease":
        return f"Current estimate: {metric_name} ends the horizon sustainably lower than today's baseline, with {target_fragment} holding across the broader operating model."
    return f"Current estimate: {metric_name} ends the horizon sustainably ahead of today's baseline, with {target_fragment} holding across the broader operating model."


def ensure_targets(key_result, period_quarter):
    year, quarter = parse_quarter(period_quarter)
    target1_date_value, target1_label = target1_date(year, quarter)
    target2_date_value, target2_label = target2_date(year, quarter)
    status = key_result.get("status")
    base_confidence = confidence_for_status(status)

    target_text = key_result.get("target") or key_result.get("statement") or "Target to be defined"
    direction = key_result.get("targetDirection")
    metric = key_result.get("metric") or key_result.get("kpiName") or "the metric"

    key_result["target1"] = {
        "label": target1_label,
        "date": target1_date_value,
        "target": target_text,
        "projectedValue": projected_value(metric, direction, 1, target_text, key_result.get("statement")),
        "confidence": base_confidence
    }
    key_result["target2"] = {
        "label": target2_label,
        "date": target2_date_value,
        "target": target_text,
        "projectedValue": projected_value(metric, direction, 2, target_text, key_result.get("statement")),
        "confidence": soften_confidence(base_confidence, status)
    }


def update_file(path):
    data = json.loads(path.read_text())
    changed = False
    for objective in data.get("objectives", []):
        period_quarter = ((objective.get("period") or {}).get("quarter")) or data.get("quarter")
        if not period_quarter:
            continue
        for key_result in objective.get("keyResults", []):
            before = json.dumps(
                {
                    "target1": key_result.get("target1"),
                    "target2": key_result.get("target2")
                },
                sort_keys=True
            )
            ensure_targets(key_result, period_quarter)
            after = json.dumps(
                {
                    "target1": key_result.get("target1"),
                    "target2": key_result.get("target2")
                },
                sort_keys=True
            )
            if before != after:
                changed = True

    if changed:
        path.write_text(json.dumps(data, indent=2) + "\n")
    return changed


def main():
    updated = 0
    for path in sorted(ROOT.glob("*/objectives/*/objectives.json")):
        if update_file(path):
            updated += 1
            print(path)
    print(f"Updated {updated} objective dataset files.")


if __name__ == "__main__":
    main()
