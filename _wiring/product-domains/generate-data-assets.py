import json
import os
from product_bricks_support import load_product_bricks_payload, flatten_product_bricks


REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
DOMAINS_ROOT = os.path.join(REPO_ROOT, '_config', 'product-domains')


def load_json(path, default):
    if not os.path.exists(path):
        return default
    with open(path) as f:
        return json.load(f)


def save_json(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=True)
        f.write('\n')


def slugify(text):
    value = (text or '').strip().lower()
    chars = []
    last_dash = False
    for ch in value:
        if ch.isalnum():
            chars.append(ch)
            last_dash = False
        elif not last_dash:
            chars.append('-')
            last_dash = True
    return ''.join(chars).strip('-')


def titleize_asset_id(asset_id):
    return ' '.join(part.capitalize() for part in asset_id.split('-') if part)


def clean_brick_name(name):
    value = (name or '').strip()
    value = value.split('(')[0].strip()
    suffixes = [
        ' management',
        ' services',
        ' service',
        ' platform',
        ' experience',
        ' page',
        ' portal',
        ' workspace',
        ' console',
        ' foundation',
        ' hub',
        ' engine',
        ' tools',
        ' tool',
        ' shell'
    ]
    lowered = value.lower()
    for suffix in suffixes:
        if lowered.endswith(suffix):
            value = value[: -len(suffix)].strip()
            lowered = value.lower()
    return value.strip() or (name or '').strip()


def infer_asset_kind(name, description):
    text = f'{name} {description}'.lower()
    if any(token in text for token in ['event', 'stream', 'log', 'notification']):
        return 'event'
    if any(token in text for token in ['media', 'document', 'content', 'creative', 'file']):
        return 'document'
    if any(token in text for token in ['reference', 'georef', 'geo', 'catalog', 'taxonomy', 'policy', 'rule', 'config']):
        return 'reference-data'
    if any(token in text for token in ['score', 'scoring', 'analytics', 'recommend', 'forecast', 'pricing', 'fraud', 'trust']):
        return 'derived-metric'
    return 'logical-object'


def infer_classification(name, description):
    text = f'{name} {description}'.lower()
    if any(token in text for token in ['credential', 'secret', 'token', 'session', 'audit', 'payment', 'ledger', 'verification', 'identity']):
        return 'restricted'
    if any(token in text for token in ['customer', 'profile', 'contact', 'account', 'booking', 'order', 'transaction', 'consent']):
        return 'confidential'
    return 'internal'


def infer_personal_data_level(name, description):
    text = f'{name} {description}'.lower()
    if any(token in text for token in ['credential', 'secret', 'token', 'verification', 'payment']):
        return 'sensitive'
    if any(token in text for token in ['customer', 'profile', 'contact', 'account', 'identity', 'session', 'consent', 'booking', 'order', 'transaction', 'conversation', 'message']):
        return 'personal'
    return 'none'


def infer_data_subjects(name, description):
    text = f'{name} {description}'.lower()
    subjects = []
    if any(token in text for token in ['customer', 'buyer', 'rider', 'traveler', 'guest', 'listener', 'user', 'consumer']):
        subjects.append('customer')
    if any(token in text for token in ['seller', 'merchant', 'partner', 'host', 'driver', 'dealer']):
        subjects.append('partner')
    if any(token in text for token in ['employee', 'operator', 'internal']):
        subjects.append('employee')
    return subjects


def infer_store_kind(asset_kind, asset_id):
    text = asset_id.lower()
    if asset_kind == 'event':
        return 'event-topic'
    if asset_kind == 'document':
        return 'blob-store'
    if asset_kind == 'reference-data':
        return 'operational-database'
    if asset_kind == 'derived-metric':
        return 'feature-store'
    if any(token in text for token in ['session', 'cache']):
        return 'cache'
    return 'operational-database'


def infer_store_id(asset_id, asset_kind):
    if asset_kind == 'event':
        return asset_id + '-stream'
    if asset_kind == 'document':
        return asset_id + '-store'
    if asset_kind == 'derived-metric':
        return asset_id + '-store'
    return asset_id + '-db'


def infer_legal_tags(classification, personal_data_level):
    tags = []
    if personal_data_level in ('personal', 'sensitive'):
        tags.append('gdpr')
    if any(token in classification for token in ['restricted']):
        return tags
    return tags


def build_brick_owner_lookup(teams_payload):
    owner_lookup = {}
    for group in teams_payload.get('groups', []):
        for team in group.get('teams', []):
            for owned in team.get('ownedProductBricks', []):
                brick_id = str(owned.get('brickId', ''))
                if brick_id and brick_id not in owner_lookup:
                    owner_lookup[brick_id] = team.get('id', '')
    return owner_lookup


def baseline_assets():
    return [
        {
            'id': 'customer-profile',
            'name': 'Customer Profile',
            'kind': 'logical-object',
            'description': 'Core customer account, profile, and preference data used across domain journeys.',
            'classification': 'restricted',
            'personalDataLevel': 'personal',
            'dataSubjects': ['customer'],
            'legalTags': ['gdpr'],
            'securityCriticality': 'high',
            'accessScope': 'customer-facing journeys and approved internal operations'
        },
        {
            'id': 'customer-contact-point',
            'name': 'Customer Contact Point',
            'kind': 'logical-object',
            'description': 'Verified email, phone, and contactability state used for messaging and recovery.',
            'classification': 'restricted',
            'personalDataLevel': 'personal',
            'dataSubjects': ['customer'],
            'legalTags': ['gdpr'],
            'securityCriticality': 'high',
            'accessScope': 'communication and identity workflows'
        },
        {
            'id': 'consent-record',
            'name': 'Consent Record',
            'kind': 'logical-object',
            'description': 'Privacy, tracking, and communication consent history with auditable decisions.',
            'classification': 'restricted',
            'personalDataLevel': 'personal',
            'dataSubjects': ['customer', 'partner'],
            'legalTags': ['gdpr'],
            'securityCriticality': 'high',
            'accessScope': 'privacy and compliant product flows'
        },
        {
            'id': 'identity-credential',
            'name': 'Identity Credential',
            'kind': 'logical-object',
            'description': 'Credential metadata, password hashes, or authentication factor references.',
            'classification': 'restricted',
            'personalDataLevel': 'sensitive',
            'dataSubjects': ['customer', 'partner', 'employee'],
            'legalTags': ['gdpr'],
            'securityCriticality': 'critical',
            'authenticationMaterial': 'password',
            'accessScope': 'identity platform only'
        },
        {
            'id': 'session-token',
            'name': 'Session Token',
            'kind': 'logical-object',
            'description': 'Short-lived authenticated session state, refresh metadata, and revocation information.',
            'classification': 'restricted',
            'personalDataLevel': 'sensitive',
            'dataSubjects': ['customer', 'partner', 'employee'],
            'legalTags': ['gdpr'],
            'securityCriticality': 'critical',
            'authenticationMaterial': 'token',
            'accessScope': 'runtime identity enforcement only'
        },
        {
            'id': 'access-policy',
            'name': 'Access Policy',
            'kind': 'reference-data',
            'description': 'Authorization rules, entitlements, restrictions, and access guardrails.',
            'classification': 'restricted',
            'personalDataLevel': 'none',
            'dataSubjects': [],
            'legalTags': [],
            'securityCriticality': 'critical',
            'accessScope': 'authorization and trust systems only'
        },
        {
            'id': 'audit-log',
            'name': 'Audit Log',
            'kind': 'event',
            'description': 'Security and compliance event trail for sensitive operations and lifecycle changes.',
            'classification': 'restricted',
            'personalDataLevel': 'personal',
            'dataSubjects': ['customer', 'partner', 'employee'],
            'legalTags': ['gdpr'],
            'securityCriticality': 'critical',
            'accessScope': 'security, audit, and compliance only'
        }
    ]


def payment_assets():
    return [
        {
            'id': 'payment-instrument-reference',
            'name': 'Payment Instrument Reference',
            'kind': 'logical-object',
            'description': 'Tokenized payment method references or vaulted instrument links used in protected commerce flows.',
            'classification': 'restricted',
            'personalDataLevel': 'sensitive',
            'dataSubjects': ['customer', 'partner'],
            'legalTags': ['gdpr', 'pci'],
            'securityCriticality': 'critical',
            'authenticationMaterial': 'token',
            'accessScope': 'approved payment workflows only'
        },
        {
            'id': 'transaction',
            'name': 'Transaction',
            'kind': 'logical-object',
            'description': 'Commercial or financial transaction state tracked across purchase, settlement, or payout workflows.',
            'classification': 'confidential',
            'personalDataLevel': 'personal',
            'dataSubjects': ['customer', 'partner'],
            'legalTags': ['gdpr'],
            'securityCriticality': 'high',
            'accessScope': 'commerce and finance workflows'
        }
    ]


def domain_asset_from_brick(brick, owner_lookup):
    cleaned_name = clean_brick_name(brick.get('name', ''))
    asset_id = slugify(cleaned_name)
    if not asset_id or len(asset_id) < 3:
        asset_id = slugify(brick.get('id', 'asset'))
    asset_kind = infer_asset_kind(cleaned_name, brick.get('description', ''))
    store_id = infer_store_id(asset_id, asset_kind)
    classification = infer_classification(cleaned_name, brick.get('description', ''))
    personal_data_level = infer_personal_data_level(cleaned_name, brick.get('description', ''))

    return {
        'id': asset_id,
        'name': titleize_asset_id(asset_id),
        'kind': asset_kind,
        'description': brick.get('description', '') or f'Core domain data managed or served through {brick.get("name", brick.get("id", "this brick"))}.',
        'businessMeaning': f'Reusable domain data centered on {cleaned_name or brick.get("name", "the domain workflow")}.',
        'status': 'active',
        'tags': [slugify(brick.get('domain', 'domain')) or 'domain'],
        'classification': classification,
        'personalDataLevel': personal_data_level,
        'dataSubjects': infer_data_subjects(cleaned_name, brick.get('description', '')),
        'legalTags': infer_legal_tags(classification, personal_data_level),
        'systemOfRecordBrickId': brick.get('id', ''),
        'ownerTeamId': owner_lookup.get(brick.get('id', ''), ''),
        'stewardTeamIds': [],
        'derivedFromAssetIds': [],
        'stores': [{'storeId': store_id, 'role': 'system-of-record'}],
        'interfaces': [
            {
                'type': 'api',
                'name': asset_id + ' api',
                'description': f'Access interface for {titleize_asset_id(asset_id)}.'
            }
        ],
        'governance': {
            'retention': 'active lifecycle plus audit window',
            'residency': 'eu',
            'sharingPolicy': 'internal and approved domain consumers only'
        }
    }


def include_payment_assets(bricks):
    payment_keywords = ('payment', 'billing', 'invoice', 'ledger', 'payout', 'settlement', 'revenue', 'charge', 'expense', 'tax')
    for brick in bricks:
        text = f'{brick.get("name", "")} {brick.get("description", "")}'.lower()
        if any(keyword in text for keyword in payment_keywords):
            return True
    return False


def score_brick_for_asset(brick):
    text = f'{brick.get("name", "")} {brick.get("description", "")}'.lower()
    score = 0
    if brick.get('type') in ('service', 'full-stack', 'integration'):
        score += 3
    if any(token in text for token in ['data', 'record', 'profile', 'account', 'booking', 'order', 'inventory', 'catalog', 'content', 'media', 'message', 'payment', 'ledger', 'policy', 'identity', 'geo', 'pricing', 'search']):
        score += 3
    if any(token in text for token in ['page', 'homepage', 'shell', 'workspace', 'portal', 'experience']):
        score -= 2
    if any(token in text for token in ['foundation', 'platform', 'tooling', 'developer']):
        score -= 1
    return score


def build_store_records(assets):
    stores = {}
    for asset in assets:
        for link in asset.get('stores', []):
            store_id = link.get('storeId')
            if not store_id or store_id in stores:
                continue
            store_kind = infer_store_kind(asset.get('kind', 'logical-object'), asset.get('id', store_id))
            stores[store_id] = {
                'id': store_id,
                'name': titleize_asset_id(store_id.replace('-db', '').replace('-store', '').replace('-stream', '')) + (
                    ' DB' if store_kind == 'operational-database' else
                    ' Store' if store_kind in ('feature-store', 'blob-store') else
                    ' Stream' if store_kind == 'event-topic' else
                    ' Cache' if store_kind == 'cache' else
                    ''
                ),
                'kind': store_kind,
                'description': f'Primary {store_kind.replace("-", " ")} for {asset.get("name", asset.get("id", "domain data"))}.',
                'technology': 'generated-starter',
                'status': 'active',
                'classification': asset.get('classification', 'internal')
            }
    return list(stores.values())


def baseline_dependency_candidates(brick):
    text = f'{brick.get("name", "")} {brick.get("description", "")}'.lower()
    candidates = []

    if any(token in text for token in ['identity', 'auth', 'credential', 'login', 'session', 'access']):
        candidates.extend([
            ('identity-credential', 'read'),
            ('session-token', 'own'),
            ('access-policy', 'own'),
            ('audit-log', 'publish')
        ])
    if any(token in text for token in ['consent', 'privacy', 'cookie']):
        candidates.extend([
            ('consent-record', 'own'),
            ('audit-log', 'publish')
        ])
    if any(token in text for token in ['profile', 'account', 'portal', 'customer', 'user', 'consumer']):
        candidates.extend([
            ('customer-profile', 'own'),
            ('customer-contact-point', 'write'),
            ('consent-record', 'read')
        ])
    if any(token in text for token in ['message', 'chat', 'conversation', 'inbox', 'support']):
        candidates.extend([
            ('customer-contact-point', 'read'),
            ('audit-log', 'publish')
        ])
    if any(token in text for token in ['payment', 'billing', 'invoice', 'checkout', 'ledger', 'expense', 'revenue', 'payout', 'tax']):
        candidates.extend([
            ('payment-instrument-reference', 'read'),
            ('transaction', 'write'),
            ('audit-log', 'publish')
        ])
    return candidates


def domain_dependency_candidates(brick, assets):
    text = f'{brick.get("name", "")} {brick.get("description", "")}'.lower()
    exact_own = []
    reads = []
    for asset in assets:
        asset_id = asset.get('id', '')
        asset_name = asset.get('name', '').lower()
        asset_text = f'{asset_id} {asset_name}'.lower()
        if asset_id in {
            'customer-profile',
            'customer-contact-point',
            'consent-record',
            'identity-credential',
            'session-token',
            'access-policy',
            'audit-log',
            'payment-instrument-reference',
            'transaction'
        }:
            continue
        if brick.get('id', '') and asset.get('systemOfRecordBrickId', '') == brick.get('id', ''):
            exact_own.append((asset_id, 'own'))
            continue
        tokens = [part for part in asset_id.split('-') if len(part) > 3]
        overlap = sum(1 for token in tokens if token in text)
        if overlap:
            role = 'query' if asset.get('kind') in ('derived-metric', 'event') else 'read'
            reads.append((asset_id, role, overlap))
    reads.sort(key=lambda item: item[2], reverse=True)
    return exact_own + [(asset_id, role) for asset_id, role, _ in reads[:2]]


def store_id_lookup(assets):
    lookup = {}
    for asset in assets:
        store_refs = [item.get('storeId', '') for item in asset.get('stores', []) if item.get('storeId')]
        lookup[asset.get('id', '')] = store_refs
    return lookup


def build_data_dependency_entry(asset, role, store_lookup):
    entry = {
        'assetId': asset.get('id', ''),
        'role': role,
        'description': ''
    }
    store_ids = list(store_lookup.get(asset.get('id', ''), []))
    if store_ids:
        entry['storeIds'] = store_ids
    asset_name = asset.get('name', asset.get('id', 'asset'))
    if role == 'own':
        entry['description'] = f'Acts as the primary owning brick for {asset_name}.'
    elif role == 'write':
        entry['description'] = f'Writes or updates {asset_name} during domain workflows.'
    elif role == 'publish':
        entry['description'] = f'Publishes events or audit records related to {asset_name}.'
    elif role == 'query':
        entry['description'] = f'Queries {asset_name} to support search, analytics, or decision flows.'
    else:
        entry['description'] = f'Reads {asset_name} to support domain workflows.'
    return entry


def enrich_payload_with_data_dependencies(payload, assets):
    store_lookup = store_id_lookup(assets)
    asset_lookup = {asset.get('id', ''): asset for asset in assets}

    def walk_group(group):
        for sub_group in group.get('subGroups', []):
            walk_group(sub_group)
        for brick in group.get('bricks', []):
            if brick.get('dataDependencies'):
                continue

            candidates = []
            seen = set()
            for asset_id, role in baseline_dependency_candidates(brick) + domain_dependency_candidates(brick, assets):
                if not asset_id or asset_id not in asset_lookup:
                    continue
                key = (asset_id, role)
                if key in seen:
                    continue
                seen.add(key)
                candidates.append(build_data_dependency_entry(asset_lookup[asset_id], role, store_lookup))

            if not candidates:
                fallback_assets = [
                    asset for asset in assets
                    if asset.get('id') not in {
                        'identity-credential',
                        'session-token',
                        'access-policy',
                        'audit-log'
                    }
                ]
                fallback_assets.sort(key=lambda item: (
                    0 if item.get('kind') == 'logical-object' else 1,
                    item.get('classification', 'internal'),
                    item.get('id', '')
                ))
                for asset in fallback_assets[:2]:
                    role = 'query' if asset.get('kind') in ('derived-metric', 'event') else 'read'
                    candidates.append(build_data_dependency_entry(asset, role, store_lookup))

            if candidates:
                brick['dataDependencies'] = candidates[:4]

    for root_group in payload.get('rootGroups', []):
        walk_group(root_group)

    return payload


def build_data_assets_payload(domain_id):
    domain_root = os.path.join(DOMAINS_ROOT, domain_id)
    product_bricks_path = os.path.join(domain_root, 'product-bricks', 'product-bricks.json')
    teams_path = os.path.join(domain_root, 'teams', 'teams.json')
    bricks_payload = load_product_bricks_payload(product_bricks_path)
    flat_bricks = flatten_product_bricks(bricks_payload)
    teams_payload = load_json(teams_path, {'groups': []})
    owner_lookup = build_brick_owner_lookup(teams_payload)

    assets = []
    asset_ids = set()

    def add_asset(asset):
        if asset['id'] in asset_ids:
            return
        asset_ids.add(asset['id'])
        assets.append(asset)

    for asset in baseline_assets():
        asset = dict(asset)
        store_id = infer_store_id(asset['id'], asset['kind'])
        asset.update({
            'businessMeaning': asset['description'],
            'status': 'active',
            'stores': [{'storeId': store_id, 'role': 'system-of-record'}],
            'interfaces': [{'type': 'api', 'name': asset['id'] + ' api', 'description': f'Access interface for {asset["name"]}.'}],
            'ownerTeamId': '',
            'stewardTeamIds': [],
            'derivedFromAssetIds': [],
            'governance': {
                'retention': 'regulated or security retention window',
                'residency': 'eu',
                'sharingPolicy': 'strictly controlled internal usage'
            }
        })
        add_asset(asset)

    if include_payment_assets(flat_bricks):
        for asset in payment_assets():
            asset = dict(asset)
            store_id = infer_store_id(asset['id'], asset['kind'])
            asset.update({
                'businessMeaning': asset['description'],
                'status': 'active',
                'stores': [{'storeId': store_id, 'role': 'system-of-record'}],
                'interfaces': [{'type': 'api', 'name': asset['id'] + ' api', 'description': f'Access interface for {asset["name"]}.'}],
                'ownerTeamId': '',
                'stewardTeamIds': [],
                'derivedFromAssetIds': [],
                'governance': {
                    'retention': 'regulated finance retention window',
                    'residency': 'eu',
                    'sharingPolicy': 'approved payment and finance usage only'
                }
            })
            add_asset(asset)

    ranked_bricks = sorted(flat_bricks, key=score_brick_for_asset, reverse=True)
    for brick in ranked_bricks[:8]:
        add_asset(domain_asset_from_brick(brick, owner_lookup))

    return {
        'metadata': {
            'title': titleize_asset_id(domain_id) + ' Data Assets',
            'description': f'Starter catalog of key business, PII, and security-sensitive data assets for the {titleize_asset_id(domain_id)} domain.',
            'modelVersion': '1.0'
        },
        'assets': assets,
        'stores': build_store_records(assets)
    }


def enrich_domain_bricks_with_data_dependencies(domain_id):
    domain_root = os.path.join(DOMAINS_ROOT, domain_id)
    product_bricks_path = os.path.join(domain_root, 'product-bricks', 'product-bricks.json')
    data_assets_path = os.path.join(domain_root, 'data', 'data-assets.json')
    if not os.path.exists(product_bricks_path) or not os.path.exists(data_assets_path):
        return False

    payload = load_json(product_bricks_path, {})
    assets_payload = load_json(data_assets_path, {'assets': []})
    original = json.dumps(payload, sort_keys=True)
    enriched = enrich_payload_with_data_dependencies(payload, assets_payload.get('assets', []))
    updated = json.dumps(enriched, sort_keys=True)
    if updated == original:
        return False
    save_json(product_bricks_path, enriched)
    return True


def main():
    domains = []
    for domain_id in sorted(os.listdir(DOMAINS_ROOT)):
        product_bricks_path = os.path.join(DOMAINS_ROOT, domain_id, 'product-bricks', 'product-bricks.json')
        if os.path.exists(product_bricks_path):
            domains.append(domain_id)

    created = []
    skipped = []
    enriched = []
    for domain_id in domains:
        output_path = os.path.join(DOMAINS_ROOT, domain_id, 'data', 'data-assets.json')
        if os.path.exists(output_path):
            skipped.append(domain_id)
        else:
            payload = build_data_assets_payload(domain_id)
            save_json(output_path, payload)
            created.append(domain_id)

        if enrich_domain_bricks_with_data_dependencies(domain_id):
            enriched.append(domain_id)

    print('Created:', ', '.join(created))
    print('Skipped:', ', '.join(skipped))
    print('Enriched bricks:', ', '.join(enriched))


if __name__ == '__main__':
    main()
