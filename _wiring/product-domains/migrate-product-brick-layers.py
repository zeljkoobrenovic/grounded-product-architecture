#!/usr/bin/env python3
import json
from pathlib import Path

from product_bricks_support import normalize_product_brick_metadata, normalize_product_brick_root_groups


REPO_ROOT = Path(__file__).resolve().parents[2]
PRODUCT_BRICKS_ROOT = REPO_ROOT / '_config' / 'product-domains'


def migrate_payload(payload):
    if isinstance(payload, list):
        return normalize_product_brick_root_groups(payload)
    if not isinstance(payload, dict):
        return payload

    migrated = dict(payload)
    if 'rootGroups' in migrated:
        migrated['metadata'] = normalize_product_brick_metadata(migrated.get('metadata', {}), migrated.get('rootGroups', []))
        migrated['rootGroups'] = normalize_product_brick_root_groups(migrated.get('rootGroups', []))
    elif 'bricks' in migrated:
        migrated['metadata'] = normalize_product_brick_metadata(migrated.get('metadata', {}), migrated.get('bricks', []))
        migrated['bricks'] = normalize_product_brick_root_groups(migrated.get('bricks', []))
    return migrated


def main():
    updated = 0
    for path in sorted(PRODUCT_BRICKS_ROOT.glob('*/product-bricks/product-bricks.json')):
        payload = json.loads(path.read_text())
        migrated = migrate_payload(payload)
        migrated_text = json.dumps(migrated, indent=2) + '\n'
        if migrated_text == path.read_text():
            continue
        path.write_text(migrated_text)
        updated += 1
        print(path.relative_to(REPO_ROOT))
    print(f'Updated {updated} product-bricks.json files.')


if __name__ == '__main__':
    main()
