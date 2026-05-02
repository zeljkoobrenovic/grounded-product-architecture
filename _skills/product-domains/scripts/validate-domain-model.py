#!/usr/bin/env python3
import argparse
import json
import re
import sys
from pathlib import Path


LOWER_ID_RE = re.compile(r'^[a-z0-9][a-z0-9._:-]*$')


def load_json(path, errors):
    try:
        return json.loads(path.read_text())
    except Exception as exc:
        errors.append(f'{path}: invalid JSON: {exc}')
        return None


def collect_bricks(payload):
    bricks = {}

    def walk(node):
        if isinstance(node, dict):
            for brick in node.get('bricks', []) or []:
                if isinstance(brick, dict) and brick.get('id'):
                    brick_id = str(brick.get('id')).strip()
                    bricks.setdefault(brick_id, []).append(brick.get('name', brick_id))
            for key in ('rootGroups', 'subGroups'):
                for child in node.get(key, []) or []:
                    walk(child)
        elif isinstance(node, list):
            for child in node:
                walk(child)

    walk(payload.get('rootGroups', []) if isinstance(payload, dict) else payload)
    return bricks


def iter_id_values(node, path=''):
    if isinstance(node, dict):
        for key, value in node.items():
            child_path = f'{path}.{key}' if path else key
            if key == 'id' or key.endswith('Id') or key.endswith('Ids') or key == 'objectId':
                if isinstance(value, str):
                    yield child_path, value
                elif isinstance(value, list):
                    for index, item in enumerate(value):
                        if isinstance(item, str):
                            yield f'{child_path}[{index}]', item
            yield from iter_id_values(value, child_path)
    elif isinstance(node, list):
        for index, item in enumerate(node):
            yield from iter_id_values(item, f'{path}[{index}]')


def validate_lowercase_ids(domain_dir, payload, errors):
    for field_path, value in iter_id_values(payload):
        if 'evidence-ids' in field_path or field_path.endswith('keyResultId'):
            continue
        if value and value != value.lower():
            errors.append(f'{domain_dir.name}: {field_path} is not lowercase: {value}')
        if value and not LOWER_ID_RE.fullmatch(value):
            errors.append(f'{domain_dir.name}: {field_path} has unexpected ID characters: {value}')


def brick_ref_id(ref):
    if not isinstance(ref, dict):
        return ''
    return str(ref.get('brickId') or ref.get('objectId') or '').strip()


def validate_team_model(domain_dir, bricks, errors):
    teams_path = domain_dir / 'teams' / 'teams.json'
    if not teams_path.exists():
        return

    payload = load_json(teams_path, errors)
    if payload is None:
        return

    groups = payload.get('groups', []) if isinstance(payload, dict) else []
    teams = [team for group in groups for team in group.get('teams', []) or []]
    team_ids = [team.get('id') for team in teams if team.get('id')]
    duplicate_team_ids = sorted({team_id for team_id in team_ids if team_ids.count(team_id) > 1})
    for team_id in duplicate_team_ids:
        errors.append(f'{domain_dir.name}: duplicate team id: {team_id}')

    team_id_set = set(team_ids)
    brick_ids = set(bricks)
    owned = {}

    for group in groups:
        group_id = group.get('id', '<missing-id>')
        leadership = group.get('groupLeadership')
        if leadership is not None:
            if not isinstance(leadership, dict):
                errors.append(f'{domain_dir.name}: group {group_id} groupLeadership must be an object')
            else:
                roles_text = ' '.join(role.get('role', '') for role in leadership.get('roles', []) or []).lower()
                if leadership.get('roles') and ('head of' not in roles_text or 'director' not in roles_text or ('staff' not in roles_text and 'principal' not in roles_text)):
                    errors.append(f'{domain_dir.name}: group {group_id} leadership should include head of, director, and staff/principal roles')

    for team in teams:
        team_id = team.get('id', '<missing-id>')
        staffing = team.get('staffing') or {}
        headcount = staffing.get('suggestedHeadcount')
        if isinstance(headcount, int):
            if headcount > 10:
                errors.append(f'{domain_dir.name}: team {team_id} has headcount above 10: {headcount}')
            role_sum = sum((role.get('count') or 0) for role in staffing.get('roles', []) or [])
            if staffing.get('roles') and role_sum != headcount:
                errors.append(f'{domain_dir.name}: team {team_id} role count {role_sum} != suggestedHeadcount {headcount}')

        for dependency_id in (team.get('dependsOnTeamIds') or []) + (team.get('defaultSupportingTeamIds') or []):
            if dependency_id not in team_id_set:
                errors.append(f'{domain_dir.name}: team {team_id} references missing team {dependency_id}')

        for ref in team.get('ownedProductBricks', []) or []:
            ref_id = brick_ref_id(ref)
            if not ref_id:
                errors.append(f'{domain_dir.name}: team {team_id} has ownedProductBricks entry without brickId/objectId')
                continue
            if brick_ids and ref_id not in brick_ids:
                errors.append(f'{domain_dir.name}: team {team_id} owns missing brick {ref_id}')
            owned.setdefault(ref_id, []).append(team_id)

        for ref in team.get('supportingProductBricks', []) or []:
            ref_id = brick_ref_id(ref)
            if ref_id and brick_ids and ref_id not in brick_ids:
                errors.append(f'{domain_dir.name}: team {team_id} supports missing brick {ref_id}')

    duplicate_owned = {brick_id: owners for brick_id, owners in owned.items() if len(owners) > 1}
    for brick_id, owners in sorted(duplicate_owned.items()):
        errors.append(f'{domain_dir.name}: brick {brick_id} has multiple owning teams: {", ".join(owners)}')

    if brick_ids and team_ids:
        missing_owners = sorted(brick_ids - set(owned))
        for brick_id in missing_owners:
            errors.append(f'{domain_dir.name}: brick {brick_id} has no owning team')


def validate_domain(domain_dir, strict_ids=False):
    errors = []
    json_payloads = []

    for json_path in sorted(domain_dir.rglob('*.json')):
        payload = load_json(json_path, errors)
        if payload is not None:
            json_payloads.append((json_path, payload))
            if strict_ids and 'evidence' not in json_path.name:
                validate_lowercase_ids(domain_dir, payload, errors)

    bricks = {}
    product_bricks_path = domain_dir / 'product-bricks' / 'product-bricks.json'
    if product_bricks_path.exists():
        payload = load_json(product_bricks_path, errors)
        if payload is not None:
            bricks = collect_bricks(payload)
            duplicate_bricks = sorted(brick_id for brick_id, values in bricks.items() if len(values) > 1)
            for brick_id in duplicate_bricks:
                errors.append(f'{domain_dir.name}: duplicate product brick id: {brick_id}')

    validate_team_model(domain_dir, bricks, errors)
    return errors, len(json_payloads), len(bricks)


def main():
    parser = argparse.ArgumentParser(description='Validate product-domain JSON and core cross-file references.')
    parser.add_argument('--all', action='store_true', help='Validate every product domain. By default, pass one or more domain IDs for scoped validation.')
    parser.add_argument('--strict-ids', action='store_true', help='Also check lowercase/simple ID conventions. This can flag intentional evidence or trace identifiers.')
    parser.add_argument('domains', nargs='*', help='Domain IDs to validate.')
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[3]
    domains_root = repo_root / '_config' / 'product-domains'
    if args.domains:
        domain_dirs = [domains_root / domain for domain in args.domains]
    elif args.all:
        domain_dirs = sorted(path for path in domains_root.iterdir() if path.is_dir() and not path.name.startswith('_') and any(path.rglob('*.json')))
    else:
        parser.error('pass one or more domain IDs, or use --all for a full repository scan')

    all_errors = []
    summaries = []
    for domain_dir in domain_dirs:
        if not domain_dir.exists():
            all_errors.append(f'{domain_dir.name}: domain directory does not exist')
            continue
        errors, json_count, brick_count = validate_domain(domain_dir, strict_ids=args.strict_ids)
        all_errors.extend(errors)
        summaries.append((domain_dir.name, json_count, brick_count))

    if all_errors:
        print('Domain validation failed:')
        for error in all_errors:
            print(f'- {error}')
        return 1

    print(f'Domain validation passed: {len(summaries)} domains checked.')
    for domain, json_count, brick_count in summaries:
        print(f'- {domain}: {json_count} JSON files, {brick_count} product bricks')
    return 0


if __name__ == '__main__':
    sys.exit(main())
