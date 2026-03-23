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
        return {'metadata': {'title': default_title, 'description': default_description}, 'bricks': []}

    payload = json.load(open(path))

    if isinstance(payload, list):
        return {
            'metadata': {
                'title': default_title,
                'description': default_description
            },
            'bricks': payload
        }

    metadata = dict(payload.get('metadata', {}))
    if 'title' not in metadata:
        metadata['title'] = default_title
    if 'description' not in metadata:
        metadata['description'] = default_description

    return {
        'metadata': metadata,
        'bricks': payload.get('bricks', [])
    }


def flatten_product_bricks(payload):
    flat_bricks = []

    def walk(node, ancestors):
        children = node.get('children', []) or []
        node_type = node.get('type', '')

        if node_type == 'group':
            next_ancestors = ancestors + [node]
            for child in children:
                walk(child, next_ancestors)
            return

        domain_name = ancestors[0].get('name', '') if ancestors else node.get('domain', '')
        group_name = ancestors[-1].get('name', '') if ancestors else node.get('group', '')

        flat_bricks.append({
            'id': node.get('id', ''),
            'name': node.get('name', ''),
            'type': node.get('type', ''),
            'description': node.get('description', ''),
            'children': [],
            'domain': domain_name,
            'group': group_name
        })

    for brick in payload.get('bricks', []):
        walk(brick, [])

    return flat_bricks


def build_bricks_lookup(product_bricks_payload):
    lookup = {}
    for item in flatten_product_bricks(product_bricks_payload):
        lookup[str(item['id'])] = {
            'id': str(item['id']),
            'name': item.get('name', str(item['id'])),
            'domain': item.get('domain', ''),
            'group': item.get('group', ''),
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
            'children': []
        })

    return {
        'metadata': {
            'title': title,
            'description': description
        },
        'bricks': domains
    }
