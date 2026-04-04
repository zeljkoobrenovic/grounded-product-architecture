import json
import os


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

    metadata = dict(payload.get('metadata', {}))
    if 'title' not in metadata:
        metadata['title'] = default_title
    if 'description' not in metadata:
        metadata['description'] = default_description

    return {
        'metadata': metadata,
        'rootGroups': payload.get('rootGroups', payload.get('bricks', []))
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
                'internalModules': node.get('internalModules', []),
                'interfaces': node.get('interfaces', []),
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
            'domain': item.get('domain', ''),
            'group': item.get('group', ''),
            'internalModules': item.get('internalModules', []),
            'interfaces': item.get('interfaces', []),
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
            'internalModules': item.get('internalModules', []),
            'interfaces': item.get('interfaces', []),
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
                                'internalModules': child.get('internalModules', []),
                                'interfaces': child.get('interfaces', []),
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
