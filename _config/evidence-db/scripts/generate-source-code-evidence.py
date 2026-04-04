#!/usr/bin/env python3
"""Transform raw Sokrates repository data into tech evidence fragments."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_INPUT = SCRIPT_DIR.parent.parent / ".." / "data" / "sokrates" / "repositories.json"
DEFAULT_OUTPUT = SCRIPT_DIR / "source-code" / "repositories.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate tech evidence fragments from raw Sokrates repository data."
    )
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT, help="Path to raw repositories.json")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT, help="Path to generated repositories.json")
    parser.add_argument(
        "--sokrates-report-url-prefix",
        required=True,
        help="Base URL prefix for Sokrates HTML reports, for example https://example.com/aws",
    )
    return parser.parse_args()


def load_repositories(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, list):
        raise ValueError(f"Expected a list of repositories in {path}")
    return data


def split_repo_name(full_name: str) -> tuple[str, str]:
    parts = [part.strip() for part in full_name.split("/")]
    if len(parts) >= 2:
        return parts[0], parts[-1]
    return "", full_name.strip()


def slugify(value: str) -> str:
    return value.strip().lower().replace(" / ", "-").replace(" ", "-")


def build_fragment_id(repository: dict) -> str:
    metadata = repository.get("metadata") or {}
    _, repo_name = split_repo_name(metadata.get("name", "").strip())
    return "source-code/" + slugify(repo_name)


def github_url(repository: dict) -> str | None:
    links = repository.get("metadata", {}).get("links", [])
    for link in links:
        if link.get("href"):
            return link["href"]
    return None


def list_count(values: object) -> int:
    return len(values) if isinstance(values, list) else 0


def sum_loc(repository: dict, keys: tuple[str, ...]) -> int:
    return sum(int(repository.get(key, 0) or 0) for key in keys)


def size_tag(main_loc: int) -> str:
    if main_loc >= 100_000:
        return "size:xl"
    if main_loc >= 25_000:
        return "size:large"
    if main_loc >= 5_000:
        return "size:medium"
    return "size:small"


def activity_tag(commits_90d: int) -> str:
    if commits_90d >= 50:
        return "activity:high"
    if commits_90d >= 10:
        return "activity:medium"
    if commits_90d > 0:
        return "activity:low"
    return "activity:inactive"


def freshness_tag(latest_commit_date: str) -> str:
    if not latest_commit_date:
        return "freshness:unknown"
    latest = datetime.strptime(latest_commit_date, "%Y-%m-%d").date()
    age_days = (datetime.now(timezone.utc).date() - latest).days
    if age_days <= 30:
        return "freshness:30d"
    if age_days <= 90:
        return "freshness:90d"
    if age_days <= 365:
        return "freshness:1y"
    return "freshness:stale"


def build_facts(repository: dict) -> list[list[str, str, bool]]:
    main_loc = int(repository.get("mainLinesOfCode", 0) or 0)
    test_loc = int(repository.get("testLinesOfCode", 0) or 0)
    generated_loc = int(repository.get("generatedLinesOfCode", 0) or 0)
    build_loc = int(repository.get("buildAndDeployLinesOfCode", 0) or 0)
    other_loc = int(repository.get("otherLinesOfCode", 0) or 0)
    commits_90d = int(repository.get("commitsCount90Days", 0) or 0)
    contributors_90d = list_count(repository.get("contributors90Days"))
    latest_commit = repository.get("latestCommitDate") or "unknown date"

    all_other_loc = generated_loc + build_loc + other_loc

    return [
        {"value": main_loc, "label": "main LOC", "summable": True},
        {"value": test_loc, "label": "test LOC", "summable": True},
        {"value": all_other_loc, "label": "other LOC", "summable": True},
        {"value": commits_90d, "label": "commits 90 days", "summable": True},
        {"value": contributors_90d, "label": "contributors 90 days"},
        {"value": latest_commit, "label": "latest commit date"}
    ]


def join_url(base: str, suffix: str) -> str:
    return base.rstrip("/") + "/" + suffix.lstrip("/")


def build_links(repository: dict, sokrates_report_url_prefix: str) -> list[dict]:
    repo_link = github_url(repository)
    sokrates = repository.get("sokratesRepositoryLink") or {}
    links = []
    if repo_link:
        links.append({"label": "GitHub Repo", "url": repo_link})
    if sokrates.get("htmlReportsRoot"):
        links.append({
            "label": "Sokrates Report",
            "url": join_url(sokrates_report_url_prefix, sokrates["htmlReportsRoot"] + "/index.html")
        })
    return links


def build_fragment(repository: dict, sokrates_report_url_prefix: str) -> dict:
    metadata = repository.get("metadata") or {}
    full_name = metadata.get("name", "").strip()
    owner, repo_name = split_repo_name(full_name)

    tags = []

    return {
        "id": full_name or repo_name,
        "type": "source-code-repository-analysis",
        "icon": "source-code-repository-analysis.png",
        "title": full_name or repo_name,
        "description": metadata.get("description") or "",
        "facts": build_facts(repository),
        "links": build_links(repository, sokrates_report_url_prefix),
        "tags": tags
    }


def aggregate_summary(repositories: list[dict]) -> dict:
    repo_count = len(repositories)
    active_90d = sum(1 for repo in repositories if int(repo.get("commitsCount90Days", 0) or 0) > 0)
    stale_1y = 0
    for repo in repositories:
        latest_commit_date = repo.get("latestCommitDate")
        if not latest_commit_date:
            continue
        latest = datetime.strptime(latest_commit_date, "%Y-%m-%d").date()
        if (datetime.now(timezone.utc).date() - latest).days > 365:
            stale_1y += 1

    totals = {
        "repositories": repo_count,
        "active_repositories_90d": active_90d,
        "stale_repositories_gt_1y": stale_1y,
        "commits_total": sum(int(repo.get("commitsCount", 0) or 0) for repo in repositories),
        "commits_30d": sum(int(repo.get("commitsCount30Days", 0) or 0) for repo in repositories),
        "commits_90d": sum(int(repo.get("commitsCount90Days", 0) or 0) for repo in repositories),
        "contributors_total_distinct_observed": len(
            {
                contributor
                for repo in repositories
                for contributor in (repo.get("contributors") or [])
                if contributor
            }
        ),
        "loc_main": sum(int(repo.get("mainLinesOfCode", 0) or 0) for repo in repositories),
        "loc_test": sum(int(repo.get("testLinesOfCode", 0) or 0) for repo in repositories),
        "loc_generated": sum(int(repo.get("generatedLinesOfCode", 0) or 0) for repo in repositories),
        "loc_build_and_deploy": sum(
            int(repo.get("buildAndDeployLinesOfCode", 0) or 0) for repo in repositories
        ),
        "loc_other": sum(int(repo.get("otherLinesOfCode", 0) or 0) for repo in repositories),
        "files_main": sum(int(repo.get("mainFilesCount", 0) or 0) for repo in repositories),
        "files_test": sum(int(repo.get("testFilesCount", 0) or 0) for repo in repositories),
        "files_generated": sum(int(repo.get("generatedFilesCount", 0) or 0) for repo in repositories),
        "files_build_and_deploy": sum(
            int(repo.get("buildAndDeployFilesCount", 0) or 0) for repo in repositories
        ),
        "files_other": sum(int(repo.get("otherFilesCount", 0) or 0) for repo in repositories),
    }
    totals["loc_total_tracked"] = (
            totals["loc_main"]
            + totals["loc_test"]
            + totals["loc_generated"]
            + totals["loc_build_and_deploy"]
            + totals["loc_other"]
    )
    return totals


def build_output(repositories: list[dict], input_path: Path, sokrates_report_url_prefix: str) -> dict:
    fragments = [build_fragment(repository, sokrates_report_url_prefix) for repository in repositories]
    return {
        "config": {
            "generated_at": datetime.now(timezone.utc)
            .replace(microsecond=0)
            .isoformat()
            .replace("+00:00", "Z"),
            "source": str(input_path),
            "repository_count": len(repositories),
            "sokrates_report_url_prefix": sokrates_report_url_prefix,
            "summary": aggregate_summary(repositories),
        },
        "fragments": fragments,
    }


def main() -> None:
    args = parse_args()
    repositories = load_repositories(args.input)
    output = build_output(repositories, args.input, args.sokrates_report_url_prefix)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
