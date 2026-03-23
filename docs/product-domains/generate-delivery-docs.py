import datetime
import json
import os
import shutil

from initiatives_support import enrich_discoveries
from product_bricks_support import build_bricks_lookup, load_product_bricks_payload

date_string = datetime.date.today().strftime('%Y-%m-%d')

domains_root = '../../_config/product-domains/'
config = json.load(open(domains_root + 'config.json'))


def copy_icons(icons_path, docs_folder):
    if os.path.exists(icons_path):
        for filename in os.listdir(icons_path):
            src = os.path.join(icons_path, filename)
            dst = os.path.join(docs_folder, 'icons', filename)
            if os.path.isfile(src):
                shutil.copy2(src, dst)


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
                'icon': normalize_icon_name(customer_icon_map.get(customer.get('icon', ''), customer.get('icon', 'customer.png')))
            }

            pyramids = customer.get('kpiPyramids', {})
            customer_map = {}
            business_map = {}
            collect_kpis(pyramids.get('customerOutcomes', {}).get('top'), customer_map)
            collect_kpis(pyramids.get('businessOutcomes', {}).get('top'), business_map)
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
                'productId': channel_id.split('-')[0] if '-' in channel_id else '',
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


def render_list(template_root, template_name, docs_folder, domain, placeholder_name, data):
    if os.path.exists(docs_folder):
        shutil.rmtree(docs_folder)

    os.makedirs(os.path.join(docs_folder, 'landing_pages'), exist_ok=True)
    os.makedirs(os.path.join(docs_folder, 'icons'), exist_ok=True)

    if os.path.exists(os.path.join(template_root, 'icons')):
        copy_icons(os.path.join(template_root, 'icons'), docs_folder)

    template = open(os.path.join(template_root, template_name)).read()

    with open(os.path.join(docs_folder, 'index.html'), 'w') as html_file:
        html_file.write(template
                        .replace('${date}', date_string)
                        .replace('${domain_name}', domain['name'])
                        .replace('${domain_description}', domain['description'])
                        .replace('${' + placeholder_name + '}', json.dumps(data)))

    return data['items']


def render_landing_pages(template_root, docs_folder, template_placeholder, template_name, domain, items):
    template = open(os.path.join(template_root, template_name)).read()

    for index, item in enumerate(items):
        landing_page_file = os.path.join(docs_folder, 'landing_pages', str(index) + '.html')
        with open(landing_page_file, 'w') as html_file:
            html_file.write(template
                            .replace('${date}', date_string)
                            .replace('${domain_name}', domain['name'])
                            .replace('${' + template_placeholder + '}', json.dumps(item)))


for domain in config['domains']:
    domain_id = domain['id']
    base_path = domains_root + domain_id + '/delivery/'
    customers_path = domains_root + domain_id + '/customers/customers.json'
    products_path = domains_root + domain_id + '/products/products.json'
    if not os.path.exists(customers_path):
        customers_path = domains_root + domain_id + '/product/customers.json'
    if not os.path.exists(products_path):
        products_path = domains_root + domain_id + '/product/products.json'
    bricks_path = domains_root + domain_id + '/product-bricks/product-bricks.json'

    initiatives_path = base_path + 'initiatives.json'
    releases_path = base_path + 'releases.json'

    customers = json.load(open(customers_path)) if os.path.exists(customers_path) else []
    products = json.load(open(products_path)) if os.path.exists(products_path) else {}
    bricks = load_product_bricks_payload(bricks_path)

    customers_lookup, kpi_lookup = build_customers_lookup(customers)
    bricks_lookup = build_bricks_lookup(bricks)
    channels_lookup = build_channels_lookup(products)

    initiatives_enriched = {'items': []}
    discoveries_enriched = {'ongoing': [], 'archived': [], 'items': []}

    if os.path.exists(initiatives_path):
        initiatives = json.load(open(initiatives_path))
        initiatives_enriched = enrich_items(initiatives, customers_lookup, kpi_lookup, bricks_lookup, channels_lookup)

    initiative_lookup = {
        item.get('initiativeId', ''): {
            'landingPageIndex': item.get('landingPageIndex'),
            'description': item.get('description', '')
        }
        for item in initiatives_enriched.get('items', [])
        if item.get('initiativeId')
    }

    ongoing_discoveries_path = domains_root + domain_id + '/discoveries/ongoing.json'
    archived_discoveries_path = domains_root + domain_id + '/discoveries/archived.json'
    if os.path.exists(ongoing_discoveries_path) or os.path.exists(archived_discoveries_path):
        ongoing_discoveries = json.load(open(ongoing_discoveries_path)) if os.path.exists(ongoing_discoveries_path) else {'items': []}
        archived_discoveries = json.load(open(archived_discoveries_path)) if os.path.exists(archived_discoveries_path) else {'items': []}
        discoveries_enriched = enrich_discoveries(ongoing_discoveries, archived_discoveries, initiative_lookup)

    discovery_lookup = {
        item.get('id', ''): {
            'landingPageIndex': item.get('landingPageIndex'),
            'name': item.get('name', ''),
            'status': item.get('status', '')
        }
        for item in discoveries_enriched.get('items', [])
        if item.get('id')
    }

    for item in initiatives_enriched.get('items', []):
        linked_discoveries = []
        for linked in item.get('discoveryLinks', []):
            linked_info = discovery_lookup.get(linked.get('discoveryId', ''), {})
            linked_item = dict(linked)
            linked_item['landingPageIndex'] = linked_info.get('landingPageIndex')
            linked_item['discoveryName'] = linked_info.get('name', linked.get('discoveryName', linked.get('discoveryId', '')))
            linked_item['status'] = linked_info.get('status', linked.get('status', ''))
            linked_discoveries.append(linked_item)
        item['discoveryLinks'] = linked_discoveries

    if initiatives_enriched.get('items'):
        initiatives_docs_folder = domain_id + '/initiatives/'
        initiatives_template_root = '../../_templates/initiatives/'
        initiative_items = render_list(initiatives_template_root, 'initiatives.html', initiatives_docs_folder, domain, 'initiatives', initiatives_enriched)
        render_landing_pages(initiatives_template_root, initiatives_docs_folder, 'initiative', 'landing_page.html', domain, initiative_items)

    if discoveries_enriched.get('items'):
        discoveries_docs_folder = domain_id + '/discoveries/'
        discoveries_template_root = '../../_templates/discoveries/'
        discovery_items = render_list(discoveries_template_root, 'index.html', discoveries_docs_folder, domain, 'discoveries', discoveries_enriched)
        render_landing_pages(discoveries_template_root, discoveries_docs_folder, 'discovery', 'landing_page.html', domain, discovery_items)

    if os.path.exists(releases_path):
        releases = json.load(open(releases_path))
        releases_docs_folder = domain_id + '/releases/'
        releases_template_root = '../../_templates/releases/'
        enriched = enrich_items(releases, customers_lookup, kpi_lookup, bricks_lookup, channels_lookup)
        release_items = render_list(releases_template_root, 'index.html', releases_docs_folder, domain, 'releases', enriched)
        render_landing_pages(releases_template_root, releases_docs_folder, 'release', 'landing_page.html', domain, release_items)
