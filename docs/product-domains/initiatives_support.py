import json
import os


def load_json_if_exists(path, default_value):
    if os.path.exists(path):
        return json.load(open(path))
    return default_value


def load_first_existing(paths, default_value):
    for path in paths:
        if os.path.exists(path):
            return json.load(open(path))
    return default_value


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


def collect_kpis(node, target):
    if not node:
        return
    if node.get('name'):
        target[node['name'].lower()] = {
            'name': node.get('name', ''),
            'description': node.get('description', ''),
            'unit': node.get('unit', '')
        }
    for child in node.get('children', []):
        collect_kpis(child, target)


def build_customers_lookup(customers):
    customer_icon_map = {
        'house-search': 'seeker.png',
        'owner-key': 'owner.png',
        'briefcase-building': 'intermediary.png'
    }

    lookup = {}
    kpi_lookup = {}

    for group in customers:
        group_name = group.get('group', '')
        for customer in group.get('customers', []):
            lookup[customer['id']] = {
                'id': customer['id'],
                'name': customer.get('name', customer['id']),
                'group': group_name,
                'icon': customer_icon_map.get(customer.get('icon', ''), customer.get('icon', 'customer') + '.png')
            }

            pyramids = customer.get('kpiPyramids', {})
            customer_map = {}
            business_map = {}
            collect_kpis(pyramids.get('customerOutcomes', {}).get('top'), customer_map)
            collect_kpis(pyramids.get('businessOutcomes', {}).get('top'), business_map)
            for branch in pyramids.get('customerOutcomes', {}).get('branches', []):
                collect_kpis(branch, customer_map)
            for branch in pyramids.get('businessOutcomes', {}).get('branches', []):
                collect_kpis(branch, business_map)
            kpi_lookup[customer['id']] = {
                'customer': customer_map,
                'business': business_map
            }

    return lookup, kpi_lookup


def build_bricks_lookup(product_bricks):
    lookup = {}
    for item in product_bricks:
        lookup[str(item['id'])] = {
            'id': str(item['id']),
            'name': item.get('name', str(item['id'])),
            'domain': item.get('domain', ''),
            'group': item.get('group', ''),
            'icon': str(item['id']) + '.png'
        }
    return lookup


def interface_aliases(interface):
    aliases = set()
    aliases.add(slugify(interface.get('name', '')))
    aliases.add(slugify(interface.get('type', '')))

    name = (interface.get('name', '')).lower()
    interface_type = interface.get('type', '')

    if 'ios' in name:
        aliases.add('ios')
    if 'android' in name:
        aliases.add('android')
    if 'email' in name:
        aliases.add('email')
        aliases.add('email-alerts')
    if 'push' in name:
        aliases.add('push')
    if 'web' in name or interface_type == 'web':
        aliases.add('web')
    if 'dashboard' in name or interface_type == 'dashboard':
        aliases.add('dashboard')
    if 'api' in name:
        aliases.add(slugify(name.replace('api', ' api ')))
    if 'agent handoff' in name:
        aliases.add('agent-handoff-api')

    aliases.discard('')
    return aliases


def build_channels_lookup(products):
    lookup = {}
    for product in products.get('portfolio', {}).get('products', []):
        product_id = product.get('id', '')
        for interface in product.get('interfaces', []):
            icon = interface.get('type', 'product') + '.png'
            info = {
                'productId': product_id,
                'productName': product.get('name', product_id),
                'name': interface.get('name', ''),
                'type': interface.get('type', ''),
                'icon': icon
            }

            for alias in interface_aliases(interface):
                lookup[product_id + '-' + alias] = info

    return lookup


def enrich_kpi(kpi, details, kind):
    info = details.get(kind, {}).get(kpi.get('kpi', '').lower(), {})
    return {
        'kpi': kpi.get('kpi', ''),
        'expectedImpact': kpi.get('expectedImpact', ''),
        'description': info.get('description', ''),
        'unit': info.get('unit', ''),
        'kind': kind
    }


def enrich_items(data, customers_lookup, kpi_lookup, bricks_lookup, channels_lookup):
    items = sorted(data.get('items', []), key=lambda item: item.get('date', ''), reverse=True)
    enriched = []

    for index, item in enumerate(items):
        enriched_item = dict(item)
        enriched_item['landingPageIndex'] = index

        enriched_impacts = []
        for impact in item.get('customerImpact', []):
            customer_id = impact.get('customerId', '')
            customer_info = customers_lookup.get(customer_id, {
                'id': customer_id,
                'name': customer_id,
                'group': '',
                'icon': 'customer.png'
            })
            details = kpi_lookup.get(customer_id, {'customer': {}, 'business': {}})
            enriched_impacts.append({
                'customerId': customer_id,
                'customer': customer_info,
                'customerKPIs': [enrich_kpi(kpi, details, 'customer') for kpi in impact.get('customerKPIs', [])],
                'businessKPIs': [enrich_kpi(kpi, details, 'business') for kpi in impact.get('businessKPIs', [])]
            })

        enriched_bricks = []
        for brick in item.get('productBricks', []):
            brick_id = str(brick.get('brickId', ''))
            brick_info = bricks_lookup.get(brick_id, {
                'id': brick_id,
                'name': brick_id,
                'domain': '',
                'group': '',
                'icon': 'capability_404.png'
            })
            enriched_bricks.append({
                'brickId': brick_id,
                'change': brick.get('change', ''),
                'brick': brick_info
            })

        enriched_channels = []
        for channel in item.get('deliveryChannels', []):
            channel_id = channel.get('channelId', '')
            channel_info = channels_lookup.get(channel_id, {
                'productId': channel_id.split('-')[0] if '-' in channel_id else channel_id,
                'productName': '',
                'name': channel_id,
                'type': 'product',
                'icon': 'product.png'
            })
            enriched_channels.append({
                'channelId': channel_id,
                'change': channel.get('change', ''),
                'channel': channel_info
            })

        enriched_item['customerImpact'] = enriched_impacts
        enriched_item['productBricks'] = enriched_bricks
        enriched_item['deliveryChannels'] = enriched_channels
        enriched.append(enriched_item)

    return {'items': enriched}


def load_domain_activity(domains_root, domain_id):
    customers = load_first_existing([
        domains_root + domain_id + '/customers/customers.json',
        domains_root + domain_id + '/product/customers.json'
    ], [])
    products = load_first_existing([
        domains_root + domain_id + '/products/products.json',
        domains_root + domain_id + '/product/products.json'
    ], {'portfolio': {'products': []}})
    product_bricks = load_json_if_exists(domains_root + domain_id + '/product-bricks/product-bricks.json', [])
    initiatives = load_json_if_exists(domains_root + domain_id + '/initiatives/initiatives.json', {'items': []})
    releases = load_json_if_exists(domains_root + domain_id + '/initiatives/releases.json', {'items': []})

    customers_lookup, kpi_lookup = build_customers_lookup(customers)
    bricks_lookup = build_bricks_lookup(product_bricks)
    channels_lookup = build_channels_lookup(products)

    return {
        'initiatives': enrich_items(initiatives, customers_lookup, kpi_lookup, bricks_lookup, channels_lookup),
        'releases': enrich_items(releases, customers_lookup, kpi_lookup, bricks_lookup, channels_lookup)
    }


def filter_for_customer(items, customer_id):
    return {'items': [item for item in items.get('items', []) if any(impact.get('customerId') == customer_id for impact in item.get('customerImpact', []))]}


def filter_for_brick(items, brick_id):
    brick_id = str(brick_id)
    return {'items': [item for item in items.get('items', []) if any(str(brick.get('brickId')) == brick_id for brick in item.get('productBricks', []))]}


def filter_for_product(items, product_id):
    return {
        'items': [
            item for item in items.get('items', [])
            if any(
                channel.get('channel', {}).get('productId') == product_id
                or str(channel.get('channelId', '')).startswith(product_id + '-')
                or channel.get('channelId') == product_id
                for channel in item.get('deliveryChannels', [])
            )
        ]
    }
