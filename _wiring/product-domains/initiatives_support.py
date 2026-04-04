import json
import os

from product_bricks_support import build_bricks_lookup, load_product_bricks_payload

OBJECTIVE_PERIODS = ['current', 'next', 'archived']


def load_json_if_exists(path, default_value):
    if os.path.exists(path):
        return json.load(open(path))
    return default_value


def load_first_existing(paths, default_value):
    for path in paths:
        if os.path.exists(path):
            return json.load(open(path))
    return default_value


def load_objective_period_payload(domain_root, period, filename, default_value):
    return load_json_if_exists(os.path.join(domain_root, 'objectives', period, filename), default_value)


def merge_item_payloads(payloads):
    merged = {'items': []}
    for payload in payloads:
        merged['items'].extend(payload.get('items', []))
    return merged


def normalize_icon_name(icon_name, fallback='customer.png'):
    value = (icon_name or fallback).strip()
    if not value:
        value = fallback
    while value.endswith('.png.png'):
        value = value[:-4]
    while value.endswith('.svg.png'):
        value = value[:-4]
    if '.' in value:
        return value
    return value + '.png'


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
            'unit': node.get('unit', ''),
            'currentValue': node.get('currentValue', ''),
            'link': node.get('link', ''),
            'linkLabel': node.get('linkLabel', '')
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
                'icon': normalize_icon_name(customer_icon_map.get(customer.get('icon', ''), customer.get('icon', 'customer.png')))
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
        'currentValue': info.get('currentValue', ''),
        'link': info.get('link', ''),
        'linkLabel': info.get('linkLabel', ''),
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
    domain_root = os.path.join(domains_root, domain_id)

    customers = load_first_existing([
        domain_root + '/customers/customers.json',
        domain_root + '/product/customers.json'
    ], [])
    products = load_first_existing([
        domain_root + '/products/products.json',
        domain_root + '/product/products.json'
    ], {'portfolio': {'products': []}})
    product_bricks = load_product_bricks_payload(domain_root + '/product-bricks/product-bricks.json')
    initiatives = merge_item_payloads([
        load_objective_period_payload(domain_root, period, 'initiatives.json', {'items': []})
        for period in OBJECTIVE_PERIODS
    ])
    releases = load_json_if_exists(domain_root + '/delivery/releases.json', {'items': []})
    ongoing_discoveries = merge_item_payloads([
        load_objective_period_payload(domain_root, period, 'discoveries.json', {'items': []})
        for period in ['current', 'next']
    ])
    archived_discoveries = load_objective_period_payload(domain_root, 'archived', 'discoveries.json', {'items': []})

    customers_lookup, kpi_lookup = build_customers_lookup(customers)
    bricks_lookup = build_bricks_lookup(product_bricks)
    channels_lookup = build_channels_lookup(products)
    initiatives_enriched = enrich_items(initiatives, customers_lookup, kpi_lookup, bricks_lookup, channels_lookup)

    initiative_lookup = {
        item.get('initiativeId', ''): item
        for item in initiatives_enriched.get('items', [])
        if item.get('initiativeId')
    }

    return {
        'initiatives': initiatives_enriched,
        'releases': enrich_items(releases, customers_lookup, kpi_lookup, bricks_lookup, channels_lookup),
        'discoveries': enrich_discoveries(ongoing_discoveries, archived_discoveries, initiative_lookup)
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


def sort_discovery_items(items, ongoing):
    if ongoing:
        return sorted(items, key=lambda item: (
            item.get('endDate', ''),
            item.get('startDate', ''),
            item.get('name', '')
        ))
    return sorted(items, key=lambda item: (
        item.get('endDate', ''),
        item.get('startDate', ''),
        item.get('name', '')
    ), reverse=True)


def enrich_discoveries(ongoing_data, archived_data, initiative_lookup=None):
    initiative_lookup = initiative_lookup or {}
    enriched = {
        'ongoing': [],
        'archived': [],
        'items': []
    }

    next_index = 0
    for status_name, source, ongoing in [
        ('ongoing', ongoing_data, True),
        ('archived', archived_data, False)
    ]:
        section_items = []
        for item in sort_discovery_items(source.get('items', []), ongoing):
            enriched_item = dict(item)
            enriched_item['status'] = status_name
            enriched_item['statusLabel'] = 'Ongoing' if ongoing else 'Archived'
            enriched_item['landingPageIndex'] = next_index
            enriched_item['date'] = item.get('startDate', item.get('lastUpdated', ''))
            next_index += 1

            linked_initiatives = []
            customer_impact_by_id = {}
            product_bricks_by_id = {}
            delivery_channels_by_id = {}
            for linked in item.get('linkedInitiatives', []):
                linked_item = dict(linked)
                initiative_info = initiative_lookup.get(linked.get('initiativeId', ''), {})
                linked_item['landingPageIndex'] = initiative_info.get('landingPageIndex')
                linked_item['initiativeDescription'] = initiative_info.get('description', linked.get('description', ''))
                linked_initiatives.append(linked_item)

                for impact in initiative_info.get('customerImpact', []):
                    customer_impact_by_id[impact.get('customerId', '')] = impact
                for brick in initiative_info.get('productBricks', []):
                    product_bricks_by_id[brick.get('brickId', '')] = brick
                for channel in initiative_info.get('deliveryChannels', []):
                    delivery_channels_by_id[channel.get('channelId', '')] = channel

            enriched_item['linkedInitiatives'] = linked_initiatives
            enriched_item['customerImpact'] = list(customer_impact_by_id.values())
            enriched_item['productBricks'] = list(product_bricks_by_id.values())
            enriched_item['deliveryChannels'] = list(delivery_channels_by_id.values())
            enriched_item['riskFocus'] = item.get('riskFocus', [])
            enriched_item['plannedActivities'] = item.get('plannedActivities', [])
            section_items.append(enriched_item)
            enriched['items'].append(enriched_item)

        enriched[status_name] = section_items

    return enriched
