import json
import os
import re


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


def normalize_product_brick_rendering(metadata, root_groups, path=''):
    normalized_metadata = dict(metadata or {})
    rendering = dict(
        normalized_metadata.get('rendering')
        or normalized_metadata.get('render')
        or normalized_metadata.get('renderding')
        or {}
    )

    root_group_names = [group.get('name', '') for group in root_groups or [] if group.get('name')]
    root_group_name_lookup = {name: name for name in root_group_names}
    root_group_slug_lookup = {slugify(name): name for name in root_group_names}

    normalized_rows = []
    for row_info in rendering.get('rows', []) or []:
        normalized_row = dict(row_info)
        configured_names = (
            row_info.get('rootGroupNames')
            or row_info.get('groupNames')
            or row_info.get('brickIds')
            or []
        )
        resolved_names = []
        for configured_name in configured_names:
            resolved_name = root_group_name_lookup.get(configured_name)
            if not resolved_name:
                resolved_name = root_group_slug_lookup.get(slugify(configured_name))
            if not resolved_name:
                details = f" in {path}" if path else ''
                raise ValueError(
                    f"Unknown root group '{configured_name}' referenced by metadata.rendering.rows{details}. "
                    f"Expected one of: {', '.join(root_group_names)}"
                )
            resolved_names.append(resolved_name)

        normalized_row.pop('brickIds', None)
        normalized_row.pop('groupNames', None)
        normalized_row['rootGroupNames'] = resolved_names
        normalized_rows.append(normalized_row)

    if rendering or 'rendering' in normalized_metadata or 'render' in normalized_metadata or 'renderding' in normalized_metadata:
        rendering['rows'] = normalized_rows
        normalized_metadata['rendering'] = rendering

    normalized_metadata.pop('render', None)
    normalized_metadata.pop('renderding', None)
    return normalized_metadata


def load_product_bricks_payload(path, default_title='Product Bricks', default_description=''):
    if not os.path.exists(path):
        return {'metadata': {'title': default_title, 'description': default_description}, 'rootGroups': []}

    payload = json.load(open(path))

    if isinstance(payload, list):
        return {
            'metadata': {
                'title': default_title,
                'description': default_description
            },
            'rootGroups': payload
        }

    root_groups = payload.get('rootGroups', payload.get('bricks', []))
    metadata = normalize_product_brick_rendering(dict(payload.get('metadata', {})), root_groups, path)
    if 'title' not in metadata:
        metadata['title'] = default_title
    if 'description' not in metadata:
        metadata['description'] = default_description

    return {
        'metadata': metadata,
        'rootGroups': root_groups
    }


def product_brick_root_groups(payload):
    return payload.get('rootGroups', payload.get('bricks', []))


def load_product_capabilities_payload(path, default_title='Product Experiences', default_description=''):
    if not os.path.exists(path):
        return {
            'metadata': {'title': default_title, 'description': default_description},
            'rootGroups': []
        }

    payload = json.load(open(path))

    if isinstance(payload, list):
        return {
            'metadata': {
                'title': default_title,
                'description': default_description
            },
            'rootGroups': legacy_capabilities_to_root_groups(payload)
        }

    metadata = dict(payload.get('metadata', {}))
    if 'title' not in metadata:
        metadata['title'] = default_title
    if 'description' not in metadata:
        metadata['description'] = default_description

    return {
        'metadata': metadata,
        'rootGroups': payload.get(
            'rootGroups',
            legacy_capabilities_to_root_groups(payload.get('experiences', payload.get('capabilities', [])))
        )
    }


DATA_ASSET_ROOT_GROUP_DEFINITIONS = {
    'people-accounts-access': {
        'name': 'People, Accounts, and Access Data',
        'description': 'Profiles, accounts, credentials, consent, entitlements, and access records used to identify people and govern their access.'
    },
    'commercial-financial': {
        'name': 'Commercial and Financial Data',
        'description': 'Pricing, payment, billing, subscription, revenue, settlement, ledger, and other commercial records.'
    },
    'product-catalog-content': {
        'name': 'Product, Catalog, and Content Data',
        'description': 'Catalogs, listings, inventory, content, media, products, and merchandising data exposed through customer or operator experiences.'
    },
    'operations-workflow-events': {
        'name': 'Operational Workflow and Event Data',
        'description': 'Orders, bookings, trips, tasks, incidents, service requests, workflow states, and operational events used to run the domain.'
    },
    'risk-governance-security': {
        'name': 'Risk, Governance, Security, and Compliance Data',
        'description': 'Risk signals, safety records, audit trails, policies, controls, approvals, and compliance evidence.'
    },
    'architecture-portfolio-planning': {
        'name': 'Architecture, Portfolio, and Planning Data',
        'description': 'Architecture models, portfolio records, capabilities, roadmaps, standards, and planning evidence.'
    },
    'analytics-metrics-insights': {
        'name': 'Analytics, Metrics, and Insight Data',
        'description': 'Metrics, telemetry, experiments, measurements, forecasts, recommendations, and derived analytical insight.'
    },
    'integration-platform-technical': {
        'name': 'Integration, Platform, and Technical Data',
        'description': 'API, connector, integration, runtime, infrastructure, configuration, and platform operations data.'
    },
    'reference-master-data': {
        'name': 'Reference and Master Data',
        'description': 'Reusable reference, policy, rule, taxonomy, and master data used to standardize domain behavior.'
    },
    'core-domain-records': {
        'name': 'Core Domain Records',
        'description': 'Primary domain records that do not fit a more specialized data group.'
    }
}


DATA_ASSET_ROOT_GROUP_ORDER = [
    'people-accounts-access',
    'commercial-financial',
    'product-catalog-content',
    'operations-workflow-events',
    'risk-governance-security',
    'architecture-portfolio-planning',
    'analytics-metrics-insights',
    'integration-platform-technical',
    'reference-master-data',
    'core-domain-records'
]


DATA_ASSET_SUBGROUP_DEFINITIONS = {
    'core-records': {
        'name': 'Core Records',
        'description': 'Durable domain entities and business objects.'
    },
    'events-and-logs': {
        'name': 'Events and Logs',
        'description': 'Append-only events, logs, state changes, and operational traces.'
    },
    'financial-records': {
        'name': 'Financial Records',
        'description': 'Commercial, payment, billing, ledger, and settlement records.'
    },
    'analytics-and-derived-data': {
        'name': 'Analytics and Derived Data',
        'description': 'Aggregated, calculated, scored, predicted, or insight-oriented datasets.'
    },
    'reference-and-policy-data': {
        'name': 'Reference and Policy Data',
        'description': 'Reference lists, policies, rules, configuration, and taxonomies.'
    },
    'documents-and-evidence': {
        'name': 'Documents and Evidence',
        'description': 'Documents, media, knowledge, files, and evidence packages.'
    }
}


DATA_ASSET_SUBGROUP_ORDER = [
    'core-records',
    'financial-records',
    'events-and-logs',
    'reference-and-policy-data',
    'documents-and-evidence',
    'analytics-and-derived-data'
]


def _asset_text(asset):
    values = [
        asset.get('id', ''),
        asset.get('name', ''),
        asset.get('kind', ''),
        asset.get('description', ''),
        asset.get('businessMeaning', ''),
        asset.get('ownerTeamId', ''),
        asset.get('systemOfRecordBrickId', ''),
        ' '.join(asset.get('tags', []) or [])
    ]
    return ' '.join(str(value).lower() for value in values if value)


def _asset_identity_text(asset):
    values = [
        asset.get('id', ''),
        asset.get('name', ''),
        asset.get('kind', ''),
        ' '.join(asset.get('tags', []) or [])
    ]
    return ' '.join(str(value).lower() for value in values if value)


def _text_has_any(text, keywords):
    normalized_text = re.sub(r'[^a-z0-9]+', ' ', text or '').strip()
    tokens = set(normalized_text.split())
    for keyword in keywords:
        normalized_keyword = re.sub(r'[^a-z0-9]+', ' ', keyword.lower()).strip()
        if not normalized_keyword:
            continue
        if ' ' in normalized_keyword:
            if normalized_keyword in normalized_text:
                return True
        elif normalized_keyword in tokens:
            return True
    return False


def data_asset_root_group_key(asset):
    text = _asset_text(asset)
    identity_text = _asset_identity_text(asset)
    kind = str(asset.get('kind', '')).lower()

    finance_keywords = [
        'payment', 'transaction', 'ledger', 'invoice', 'billing', 'payout', 'subscription',
        'pricing', 'price', 'quote', 'proposal', 'spend', 'revenue', 'cost', 'budget',
        'costs', 'settlement', 'tariff', 'financial', 'finance', 'commerce', 'commission',
        'rate'
    ]
    product_keywords = [
        'catalog', 'content', 'listing', 'property', 'inventory', 'menu', 'media',
        'article', 'product', 'sku', 'assortment', 'creative',
        'knowledge', 'course', 'playlist', 'episode', 'track', 'classified'
    ]
    operations_keywords = [
        'order', 'booking', 'delivery', 'dispatch', 'trip', 'ride', 'shipment',
        'workflow', 'work-item', 'work item', 'service-request', 'service request',
        'case', 'operation', 'task', 'status', 'event', 'availability', 'assignment',
        'session orchestration', 'charging session', 'fulfillment'
    ]
    risk_keywords = [
        'risk', 'fraud', 'safety', 'security', 'audit', 'governance', 'compliance',
        'control', 'approval', 'permission', 'policy', 'vulnerability', 'incident',
        'evidence', 'entitlement', 'legal'
    ]
    people_keywords = [
        'customer', 'consumer', 'user', 'member', 'employee', 'traveler', 'rider',
        'driver', 'courier', 'merchant account', 'host', 'guest', 'partner account',
        'shipper account', 'carrier profile', 'seller', 'buyer', 'account', 'profile',
        'contact', 'consent', 'identity', 'credential', 'session-token',
        'session token', 'access', 'role', 'tenant'
    ]

    if _text_has_any(text, [
        'architecture', 'relationship', 'application inventory', 'capability',
        'technology standard', 'portfolio', 'roadmap', 'initiative', 'metamodel',
        'standard', 'process model', 'transformation'
    ]):
        return 'architecture-portfolio-planning'
    if _text_has_any(identity_text, finance_keywords):
        return 'commercial-financial'
    if _text_has_any(identity_text, product_keywords):
        return 'product-catalog-content'
    if _text_has_any(identity_text, risk_keywords):
        return 'risk-governance-security'
    if _text_has_any(identity_text, operations_keywords):
        return 'operations-workflow-events'
    if _text_has_any(text, people_keywords):
        return 'people-accounts-access'
    if _text_has_any(text, product_keywords):
        return 'product-catalog-content'
    if _text_has_any(text, operations_keywords):
        return 'operations-workflow-events'
    if _text_has_any(text, finance_keywords):
        return 'commercial-financial'
    if _text_has_any(text, risk_keywords):
        return 'risk-governance-security'
    if _text_has_any(text, [
        'metric', 'analytics', 'insight', 'telemetry', 'experiment', 'score',
        'forecast', 'recommendation', 'measurement', 'report', 'benchmark',
        'statistic', 'propensity', 'signal', 'quality', 'performance'
    ]):
        return 'analytics-metrics-insights'
    if _text_has_any(text, [
        'api', 'integration', 'connector', 'runtime', 'infrastructure', 'cloud',
        'configuration', 'config', 'deployment', 'environment', 'system', 'token',
        'log'
    ]):
        return 'integration-platform-technical'
    if kind == 'reference-data':
        return 'reference-master-data'
    return 'core-domain-records'


def data_asset_subgroup_key(asset):
    text = _asset_identity_text(asset)
    kind = str(asset.get('kind', '')).lower()
    kind_terms = set(re.sub(r'[^a-z0-9]+', ' ', kind).split())

    if 'financial' in kind_terms or _text_has_any(text, [
        'ledger', 'payment', 'billing', 'invoice', 'settlement', 'transaction',
        'payout', 'revenue', 'pricing', 'price', 'quote', 'proposal', 'spend',
        'cost', 'budget', 'tariff'
    ]):
        return 'financial-records'
    if {'event', 'log', 'stream'} & kind_terms or _text_has_any(text, ['event', 'log', 'telemetry', 'stream']):
        return 'events-and-logs'
    if kind == 'reference-data' or _text_has_any(text, ['reference', 'policy', 'rule', 'taxonomy', 'config', 'standard']):
        return 'reference-and-policy-data'
    if 'document' in kind or _text_has_any(text, ['document', 'evidence', 'media', 'content', 'article', 'knowledge', 'file']):
        return 'documents-and-evidence'
    if any(token in kind for token in ['analytics', 'derived', 'metric', 'cache']) or _text_has_any(text, [
        'metric', 'analytics', 'insight', 'score', 'forecast', 'recommendation',
        'measurement', 'report', 'benchmark', 'statistic', 'performance'
    ]):
        return 'analytics-and-derived-data'
    return 'core-records'


def group_data_assets(assets):
    root_index = {}
    sub_index = {}

    for asset in assets or []:
        root_key = data_asset_root_group_key(asset)
        subgroup_key = data_asset_subgroup_key(asset)

        if root_key not in root_index:
            root_info = DATA_ASSET_ROOT_GROUP_DEFINITIONS[root_key]
            root_index[root_key] = {
                'name': root_info['name'],
                'description': root_info['description'],
                'subGroups': []
            }
            sub_index[root_key] = {}

        if subgroup_key not in sub_index[root_key]:
            subgroup_info = DATA_ASSET_SUBGROUP_DEFINITIONS[subgroup_key]
            subgroup = {
                'name': subgroup_info['name'],
                'description': subgroup_info['description'],
                'assets': []
            }
            sub_index[root_key][subgroup_key] = subgroup
            root_index[root_key]['subGroups'].append(subgroup)

        sub_index[root_key][subgroup_key]['assets'].append(asset)

    def root_order(item):
        key, _ = item
        return DATA_ASSET_ROOT_GROUP_ORDER.index(key) if key in DATA_ASSET_ROOT_GROUP_ORDER else len(DATA_ASSET_ROOT_GROUP_ORDER)

    def subgroup_order(subgroup):
        name = subgroup.get('name', '')
        for key in DATA_ASSET_SUBGROUP_ORDER:
            if DATA_ASSET_SUBGROUP_DEFINITIONS[key]['name'] == name:
                return DATA_ASSET_SUBGROUP_ORDER.index(key)
        return len(DATA_ASSET_SUBGROUP_ORDER)

    groups = []
    for root_key, root_group in sorted(root_index.items(), key=root_order):
        root_group['subGroups'] = sorted(root_group.get('subGroups', []), key=subgroup_order)
        groups.append(root_group)
    return groups


def flatten_data_asset_groups(groups):
    assets = []

    def walk(group):
        assets.extend(group.get('assets', []) or [])
        for subgroup in group.get('subGroups', []) or []:
            walk(subgroup)

    for group in groups or []:
        walk(group)
    return assets


def load_data_assets_payload(path, default_title='Data Assets', default_description=''):
    if not os.path.exists(path):
        return {
            'metadata': {'title': default_title, 'description': default_description},
            'rootGroups': [],
            'assets': [],
            'stores': []
        }

    payload = json.load(open(path))
    metadata = dict(payload.get('metadata', {}))
    if 'title' not in metadata:
        metadata['title'] = default_title
    if 'description' not in metadata:
        metadata['description'] = default_description
    root_groups = payload.get('rootGroups') or payload.get('assetGroups') or payload.get('dataAssetGroups') or []
    assets = payload.get('assets') or flatten_data_asset_groups(root_groups)
    if assets and not root_groups:
        root_groups = group_data_assets(assets)

    return {
        'metadata': metadata,
        'rootGroups': root_groups,
        'assets': assets,
        'stores': payload.get('stores', [])
    }


def product_capability_root_groups(payload):
    return payload.get('rootGroups', legacy_capabilities_to_root_groups(payload.get('experiences', payload.get('capabilities', []))))


def sanitize_capability_flows(flows):
    sanitized_flows = []
    for flow in flows or []:
        sanitized_flow = dict(flow)
        sanitized_steps = []
        for step in flow.get('steps', []) or []:
            sanitized_step = dict(step)
            sanitized_step['dependencies'] = [
                dependency for dependency in step.get('dependencies', [])
                if dependency.get('type', 'brick') == 'brick'
            ]
            sanitized_steps.append(sanitized_step)
        sanitized_flow['steps'] = sanitized_steps
        sanitized_flows.append(sanitized_flow)
    return sanitized_flows


def flatten_product_bricks(payload):
    flat_bricks = []

    def walk_group(group, ancestors):
        next_ancestors = ancestors + [group]
        for sub_group in group.get('subGroups', []):
            walk_group(sub_group, next_ancestors)

        domain_name = next_ancestors[0].get('name', '') if next_ancestors else ''
        group_name = next_ancestors[-1].get('name', '') if next_ancestors else ''

        for node in group.get('bricks', []):
            flat_bricks.append({
                'id': node.get('id', ''),
                'name': node.get('name', ''),
                'type': node.get('type', ''),
                'description': node.get('description', ''),
                'links': node.get('links', []),
                'internalModules': node.get('internalModules', []),
                'interfaces': node.get('interfaces', []),
                'dataDependencies': node.get('dataDependencies', []),
                'brickDependencies': node.get('brickDependencies', []),
                'externalSystemsThisBrickDependsOn': node.get('externalSystemsThisBrickDependsOn', node.get('externalSystemDependencies', [])),
                'externalSystemsDependingOnThisBrick': node.get('externalSystemsDependingOnThisBrick', []),
                'domain': domain_name,
                'group': group_name
            })

    for group in product_brick_root_groups(payload):
        walk_group(group, [])

    return flat_bricks


def flatten_product_capabilities(payload):
    flat_capabilities = []

    def walk_group(group, ancestors):
        next_ancestors = ancestors + [group]
        for sub_group in group.get('subGroups', []):
            walk_group(sub_group, next_ancestors)

        root_group_name = next_ancestors[0].get('name', '') if next_ancestors else ''
        group_name = next_ancestors[-1].get('name', '') if next_ancestors else ''

        for capability in group.get('capabilities', []):
            flat_capabilities.append({
                'id': capability.get('id', ''),
                'name': capability.get('name', ''),
                'icon': capability.get('icon', str(capability.get('id', '')) + '.png'),
                'type': capability.get('type', 'outcome-based-experience'),
                'description': capability.get('description', ''),
                'group': capability.get('group', group_name),
                'rootGroup': capability.get('rootGroup', root_group_name),
                'flows': sanitize_capability_flows(capability.get('flows', [])),
                'outcomes': capability.get('outcomes', []),
                'brickDependencies': capability.get('brickDependencies', capability.get('productBrickDependencies', []))
            })

    for group in product_capability_root_groups(payload):
        walk_group(group, [])

    return flat_capabilities


def sanitize_product_capability_root_groups(groups, ancestors=None):
    sanitized_groups = []
    ancestors = ancestors or []

    for group in groups or []:
        next_ancestors = ancestors + [group]
        root_group_name = next_ancestors[0].get('name', '') if next_ancestors else ''
        group_name = next_ancestors[-1].get('name', '') if next_ancestors else ''

        sanitized_groups.append({
            'name': group.get('name', ''),
            'description': group.get('description', ''),
            'subGroups': sanitize_product_capability_root_groups(group.get('subGroups', []), next_ancestors),
            'capabilities': [
                {
                    'id': capability.get('id', ''),
                    'name': capability.get('name', ''),
                    'icon': capability.get('icon', str(capability.get('id', '')) + '.png'),
                    'type': capability.get('type', 'outcome-based-experience'),
                    'description': capability.get('description', ''),
                    'group': capability.get('group', group_name),
                    'rootGroup': capability.get('rootGroup', root_group_name),
                    'flows': sanitize_capability_flows(capability.get('flows', [])),
                    'outcomes': capability.get('outcomes', []),
                    'brickDependencies': capability.get('brickDependencies', capability.get('productBrickDependencies', []))
                }
                for capability in group.get('capabilities', [])
            ]
        })

    return sanitized_groups


def legacy_capabilities_to_root_groups(items):
    groups = []
    group_index = {}

    for item in items:
        group_name = item.get('group', 'Ungrouped') or 'Ungrouped'
        if group_name not in group_index:
            group_index[group_name] = {
                'name': group_name,
                'description': '',
                'subGroups': [],
                'capabilities': []
            }
            groups.append(group_index[group_name])

        capability = dict(item)
        capability.pop('group', None)
        capability.pop('children', None)
        group_index[group_name]['capabilities'].append(capability)

    return groups


def build_bricks_lookup(product_bricks_payload):
    lookup = {}
    for item in flatten_product_bricks(product_bricks_payload):
        lookup[str(item['id'])] = {
            'id': str(item['id']),
            'name': item.get('name', str(item['id'])),
            'type': item.get('type', ''),
            'description': item.get('description', ''),
            'links': item.get('links', []),
            'domain': item.get('domain', ''),
            'group': item.get('group', ''),
            'internalModules': item.get('internalModules', []),
            'interfaces': item.get('interfaces', []),
            'dataDependencies': item.get('dataDependencies', []),
            'brickDependencies': item.get('brickDependencies', []),
            'externalSystemsThisBrickDependsOn': item.get('externalSystemsThisBrickDependsOn', item.get('externalSystemDependencies', [])),
            'externalSystemsDependingOnThisBrick': item.get('externalSystemsDependingOnThisBrick', []),
            'icon': str(item['id']) + '.png'
        }
    return lookup


def legacy_bricks_to_payload(items, title='Product Bricks', description=''):
    domains = []
    domain_index = {}

    for item in items:
        domain_name = item.get('domain', 'Other')
        group_name = item.get('group', 'Ungrouped')

        if domain_name not in domain_index:
            domain_node = {
                'id': slugify(domain_name) or 'group',
                'name': domain_name,
                'type': 'group',
                'description': '',
                'children': []
            }
            domain_index[domain_name] = {
                'node': domain_node,
                'groups': {}
            }
            domains.append(domain_node)

        domain_entry = domain_index[domain_name]

        if group_name not in domain_entry['groups']:
            group_node = {
                'id': slugify(domain_name + ' ' + group_name) or slugify(group_name) or 'group',
                'name': group_name,
                'type': 'group',
                'description': '',
                'children': []
            }
            domain_entry['groups'][group_name] = group_node
            domain_entry['node']['children'].append(group_node)

        domain_entry['groups'][group_name]['children'].append({
            'id': item.get('id', ''),
            'name': item.get('name', ''),
            'type': item.get('type', ''),
            'description': item.get('description', ''),
            'links': item.get('links', []),
            'internalModules': item.get('internalModules', []),
            'interfaces': item.get('interfaces', []),
            'dataDependencies': item.get('dataDependencies', []),
            'brickDependencies': item.get('brickDependencies', []),
            'externalSystemsThisBrickDependsOn': item.get('externalSystemsThisBrickDependsOn', item.get('externalSystemDependencies', [])),
            'externalSystemsDependingOnThisBrick': item.get('externalSystemsDependingOnThisBrick', []),
            'children': []
        })

    return {
        'metadata': {
            'title': title,
            'description': description
        },
        'rootGroups': [
            {
                'name': domain.get('name', ''),
                'description': domain.get('description', ''),
                'subGroups': [
                    {
                        'name': group.get('name', ''),
                        'description': group.get('description', ''),
                        'subGroups': [],
                        'bricks': [
                            {
                                'id': child.get('id', ''),
                                'name': child.get('name', ''),
                                'type': child.get('type', ''),
                                'description': child.get('description', ''),
                                'links': child.get('links', []),
                                'internalModules': child.get('internalModules', []),
                                'interfaces': child.get('interfaces', []),
                                'dataDependencies': child.get('dataDependencies', []),
                                'brickDependencies': child.get('brickDependencies', []),
                                'externalSystemsThisBrickDependsOn': child.get('externalSystemsThisBrickDependsOn', child.get('externalSystemDependencies', [])),
                                'externalSystemsDependingOnThisBrick': child.get('externalSystemsDependingOnThisBrick', [])
                            }
                            for child in group.get('children', [])
                        ]
                    }
                    for group in domain.get('children', [])
                ],
                'bricks': []
            }
            for domain in domains
        ]
    }
