#!/usr/bin/env python3
"""
Data model migration script.
Applies the following improvements across all 10 product domains:

1. Upgrade premium-long-haul-airline objectives from schema v1.0 to v2.0
2. Fix duplicate KR IDs in general-listings-marketplace
3. Add keyResultIds to initiatives (linking initiatives back to KRs)
4. Add initiativeId to releases (linking releases to their initiative)
5. Add status field to key results
6. Standardize discovery outcome vocabulary
7. Add sourceObjectiveIds to company objectives (reverse references)
8. Add priority field to initiatives
"""

import json
import os
import re
import sys

BASE = os.path.join(os.path.dirname(__file__), '..', 'product-domains')
DOMAINS_CONFIG = os.path.join(os.path.dirname(__file__), '..', 'product-domains', 'config.json')


def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_json(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write('\n')


def get_domain_ids():
    config = load_json(DOMAINS_CONFIG)
    return [d['id'] for d in config['domains']]


# ─── 1. Upgrade premium-long-haul-airline to v2.0 ───

def upgrade_airline_to_v2(domain_path):
    """Add companyObjectives, team assignments, commitment fields to airline objectives."""
    for filename in ['current.json', 'next.json', 'archive.json']:
        path = os.path.join(domain_path, 'objectives', filename)
        if not os.path.exists(path):
            continue
        data = load_json(path)
        if data.get('schemaVersion') == '2.0':
            continue

        data['schemaVersion'] = '2.0'
        data['methodology'] = (
            'Refactored to Empowered-style OKRs: a small set of company objectives, '
            'linked source objectives, source-level key results, explicit team ownership, '
            'and limited use of High Integrity Commitments.'
        )
        data['okrDesignPrinciples'] = [
            'Objectives describe meaningful business and customer outcomes, not feature delivery.',
            'Key results measure source objectives, while source objectives map upward into a small set of company objectives.',
            'Every key result names executing and supporting teams so accountability is explicit.',
            'High Integrity Commitments are used sparingly and only for work that is materially deadline-sensitive.'
        ]

        # Add company objectives if missing
        if 'companyObjectives' not in data:
            data['companyObjectives'] = [
                {
                    'id': 'obj-operations',
                    'title': f'{data.get("quarter", "2026-Q1")} Make execution reliably repeatable',
                    'statement': 'Improve the operating system behind the product so launches, service recovery, reliability, and cross-functional delivery become predictably repeatable.',
                    'objectiveType': 'company',
                    'okrDesignNotes': 'Keeps teams accountable for operational outcomes.',
                    'status': 'active',
                    'inspiredByInsights': []
                },
                {
                    'id': 'obj-leverage',
                    'title': f'{data.get("quarter", "2026-Q1")} Turn product progress into economic leverage',
                    'statement': 'Translate better customer and operational outcomes into stronger revenue quality, retention, and strategic leverage for the business.',
                    'objectiveType': 'company',
                    'okrDesignNotes': 'Separates commercial results from activity metrics.',
                    'status': 'active',
                    'inspiredByInsights': []
                }
            ]

        # Upgrade each source objective
        for obj in data.get('objectives', []):
            # Add team assignments to KRs if missing
            for kr in obj.get('keyResults', []):
                if 'executingTeams' not in kr:
                    kr['executingTeams'] = []
                if 'supportingTeams' not in kr:
                    kr['supportingTeams'] = []
                if 'commitmentType' not in kr:
                    kr['commitmentType'] = 'standard'
                    kr['commitmentLabel'] = 'Standard KR'
                    kr['commitmentRationale'] = 'This KR should be pursued as an outcome target with room for discovery, iteration, and tradeoff.'

            # Add v2.0 source objective fields
            if 'objectiveRole' not in obj:
                obj['objectiveRole'] = 'source_objective_for_company_okrs'
            if 'companyObjectiveIds' not in obj:
                obj['companyObjectiveIds'] = ['obj-operations', 'obj-leverage']
            if 'inspiredByInsights' not in obj:
                obj['inspiredByInsights'] = []

        save_json(path, data)
        print(f'  Upgraded {filename} to v2.0')


# ─── 2. Fix duplicate KR IDs ───

def fix_duplicate_kr_ids(domain_path):
    """Renumber KR IDs within each objective to be unique."""
    changed = False
    for filename in ['current.json', 'next.json', 'archive.json']:
        path = os.path.join(domain_path, 'objectives', filename)
        if not os.path.exists(path):
            continue
        data = load_json(path)

        for obj in data.get('objectives', []):
            krs = obj.get('keyResults', [])
            seen = set()
            has_dupes = False
            for kr in krs:
                if kr['id'] in seen:
                    has_dupes = True
                    break
                seen.add(kr['id'])

            if has_dupes:
                for i, kr in enumerate(krs):
                    kr['id'] = f'kr-{i + 1}'
                changed = True

        if changed:
            save_json(path, data)
            print(f'  Fixed duplicate KR IDs in {filename}')

    return changed


# ─── 3. Add keyResultIds to initiatives ───

def add_key_result_ids_to_initiatives(domain_path, domain_id):
    """Link initiatives back to KRs by matching on product brick overlap."""
    initiatives_path = os.path.join(domain_path, 'delivery', 'initiatives.json')
    if not os.path.exists(initiatives_path):
        return

    initiatives = load_json(initiatives_path)

    # Collect all KRs with their objective's linked product bricks
    # Each objective links to initiatives that share product bricks with KRs
    kr_brick_map = []  # list of (qualified_kr_id, set_of_bricks)
    for filename in ['current.json', 'next.json', 'archive.json']:
        obj_path = os.path.join(domain_path, 'objectives', filename)
        if not os.path.exists(obj_path):
            continue
        obj_data = load_json(obj_path)
        for obj in obj_data.get('objectives', []):
            # Gather all bricks referenced by this objective's linked initiatives
            obj_bricks = set()
            for linked in obj.get('linkedInitiatives', []):
                for b in linked.get('productBricks', []):
                    obj_bricks.add(b if isinstance(b, str) else b.get('brickId', ''))
            # Each KR in this objective is associated with those bricks
            for kr in obj.get('keyResults', []):
                qualified_id = f'{obj["id"]}/{kr["id"]}'
                kr_brick_map.append((qualified_id, obj_bricks))

    changed = False
    for item in initiatives.get('items', []):
        if 'keyResultIds' not in item:
            init_bricks = set()
            for b in item.get('productBricks', []):
                init_bricks.add(b.get('brickId', b) if isinstance(b, dict) else b)

            # Find KRs whose objective shares product bricks with this initiative
            matched_krs = sorted(set(
                kr_id for kr_id, kr_bricks in kr_brick_map
                if init_bricks & kr_bricks
            ))
            item['keyResultIds'] = matched_krs
            changed = True

    if changed:
        save_json(initiatives_path, initiatives)
        print(f'  Added keyResultIds to initiatives ({sum(1 for i in initiatives["items"] if i.get("keyResultIds"))} linked)')


# ─── 4. Add initiativeId to releases ───

def add_initiative_id_to_releases(domain_path, domain_id):
    """Link releases to their corresponding initiative by matching on product bricks and customers."""
    releases_path = os.path.join(domain_path, 'delivery', 'releases.json')
    initiatives_path = os.path.join(domain_path, 'delivery', 'initiatives.json')
    if not os.path.exists(releases_path) or not os.path.exists(initiatives_path):
        return

    releases = load_json(releases_path)
    initiatives = load_json(initiatives_path)

    # Build initiative lookup by product brick overlap
    init_items = initiatives.get('items', [])

    changed = False
    for release in releases.get('items', []):
        if 'initiativeId' in release:
            continue

        release_bricks = set(b.get('brickId', b) if isinstance(b, dict) else b
                            for b in release.get('productBricks', []))
        release_customers = set(c.get('customerId', c) if isinstance(c, dict) else c
                                for c in release.get('customerImpact', []))

        # Find best matching initiative by brick + customer overlap
        best_match = None
        best_score = 0
        for init in init_items:
            init_bricks = set(b.get('brickId', b) if isinstance(b, dict) else b
                             for b in init.get('productBricks', []))
            init_customers = set(c.get('customerId', c) if isinstance(c, dict) else c
                                for c in init.get('customerImpact', []))
            score = len(release_bricks & init_bricks) + len(release_customers & init_customers)
            if score > best_score:
                best_score = score
                best_match = init

        release['initiativeId'] = best_match.get('initiativeId', '') if best_match and best_score > 0 else ''
        changed = True

    if changed:
        save_json(releases_path, releases)
        print(f'  Added initiativeId to releases')


# ─── 5. Add status to KRs ───

def add_status_to_krs(domain_path):
    """Add status field to key results based on timeframe."""
    for filename in ['current.json', 'next.json', 'archive.json']:
        path = os.path.join(domain_path, 'objectives', filename)
        if not os.path.exists(path):
            continue
        data = load_json(path)
        timeframe = data.get('timeframe', filename.replace('.json', ''))

        # Determine default status based on timeframe
        if 'archive' in filename:
            default_status = 'achieved'
        elif 'next' in filename:
            default_status = 'planned'
        else:
            default_status = 'on-track'

        changed = False
        for obj in data.get('objectives', []):
            for kr in obj.get('keyResults', []):
                if 'status' not in kr:
                    kr['status'] = default_status
                    changed = True

        if changed:
            save_json(path, data)
            print(f'  Added KR status ({default_status}) to {filename}')


# ─── 6. Standardize discovery outcomes ───

OUTCOME_MAP = {
    'proceed': 'proceed',
    'narrow': 'narrow',
    'sequence': 'sequence',
    'pivot': 'pivot',
    'park': 'park',
    'kill': 'kill',
}

def standardize_discovery_outcomes(domain_path):
    """Ensure outcome.decision uses standard vocabulary."""
    for filename in ['archived.json', 'ongoing.json']:
        path = os.path.join(domain_path, 'discoveries', filename)
        if not os.path.exists(path):
            continue
        data = load_json(path)

        # Add allowedDecisions to the schema metadata if not present
        if 'allowedDecisions' not in data:
            data['allowedDecisions'] = ['proceed', 'narrow', 'sequence', 'pivot', 'park', 'kill']

        changed = False
        for item in data.get('items', []):
            outcome = item.get('outcome')
            if outcome and 'decision' in outcome:
                raw = outcome['decision'].lower().strip()
                normalized = OUTCOME_MAP.get(raw, raw)
                if normalized != outcome['decision']:
                    outcome['decision'] = normalized
                    changed = True

        save_json(path, data)
        if changed:
            print(f'  Standardized outcomes in {filename}')
        else:
            print(f'  Added allowedDecisions to {filename}')


# ─── 7. Add sourceObjectiveIds to company objectives ───

def add_source_objective_ids(domain_path):
    """Add reverse references from company objectives to their source objectives."""
    for filename in ['current.json', 'next.json', 'archive.json']:
        path = os.path.join(domain_path, 'objectives', filename)
        if not os.path.exists(path):
            continue
        data = load_json(path)

        company_objs = data.get('companyObjectives', [])
        if not company_objs:
            continue

        # Build reverse map: company_obj_id -> [source_obj_ids]
        reverse = {co['id']: [] for co in company_objs}
        for obj in data.get('objectives', []):
            for co_id in obj.get('companyObjectiveIds', []):
                if co_id in reverse:
                    reverse[co_id].append(obj['id'])

        changed = False
        for co in company_objs:
            if 'sourceObjectiveIds' not in co:
                co['sourceObjectiveIds'] = reverse.get(co['id'], [])
                changed = True

        if changed:
            save_json(path, data)
            print(f'  Added sourceObjectiveIds to company objectives in {filename}')


# ─── 8. Add priority to initiatives ───

def add_priority_to_initiatives(domain_path):
    """Add priority field to initiatives. Default to p1 (standard priority)."""
    path = os.path.join(domain_path, 'delivery', 'initiatives.json')
    if not os.path.exists(path):
        return
    data = load_json(path)

    changed = False
    for item in data.get('items', []):
        if 'priority' not in item:
            item['priority'] = 'p1'
            changed = True

    if changed:
        save_json(path, data)
        print(f'  Added priority field to initiatives')


# ─── Main ───

def main():
    domain_ids = get_domain_ids()
    print(f'Found {len(domain_ids)} domains: {", ".join(domain_ids)}\n')

    for domain_id in domain_ids:
        domain_path = os.path.join(BASE, domain_id)
        if not os.path.isdir(domain_path):
            print(f'[SKIP] {domain_id} — directory not found')
            continue

        print(f'[{domain_id}]')

        # 1. Upgrade airline to v2.0
        if domain_id == 'premium-long-haul-airline':
            upgrade_airline_to_v2(domain_path)

        # 2. Fix duplicate KR IDs
        if domain_id == 'general-listings-marketplace':
            fix_duplicate_kr_ids(domain_path)

        # 3. Add keyResultIds to initiatives
        add_key_result_ids_to_initiatives(domain_path, domain_id)

        # 4. Add initiativeId to releases
        add_initiative_id_to_releases(domain_path, domain_id)

        # 5. Add status to KRs
        add_status_to_krs(domain_path)

        # 6. Standardize discovery outcomes
        standardize_discovery_outcomes(domain_path)

        # 7. Add sourceObjectiveIds to company objectives
        add_source_objective_ids(domain_path)

        # 8. Add priority to initiatives
        add_priority_to_initiatives(domain_path)

        print()

    print('Done. All data model improvements applied.')


if __name__ == '__main__':
    main()
