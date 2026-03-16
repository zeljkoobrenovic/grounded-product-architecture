import copy
import datetime
import json
import os


TODAY = datetime.date.today()
ROOT = os.path.dirname(__file__)


def load_json(path):
    with open(path) as f:
        return json.load(f)


def save_json(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=True)
        f.write('\n')


def slugify(text):
    text = (text or '').strip().lower()
    out = []
    prev_dash = False
    for ch in text:
        if ch.isalnum():
            out.append(ch)
            prev_dash = False
        elif not prev_dash:
            out.append('-')
            prev_dash = True
    return ''.join(out).strip('-')


def derive_brick_id(name, used_ids=None):
    used_ids = used_ids or set()
    words = [part for part in slugify(name).split('-') if part]
    if not words:
        words = ['capability']

    def claim(candidate):
        candidate = (candidate or 'capa')[:4].ljust(4, 'x')
        if candidate not in used_ids:
            used_ids.add(candidate)
            return candidate

        stream = ''.join(words)
        for ch in stream:
            alt = (candidate[:3] + ch)[:4]
            if alt not in used_ids:
                used_ids.add(alt)
                return alt

        for ch in 'abcdefghijklmnopqrstuvwxyz':
            alt = (candidate[:3] + ch)[:4]
            if alt not in used_ids:
                used_ids.add(alt)
                return alt

        raise ValueError(f'Unable to derive unique brick id for {name}')

    if len(words) >= 4:
        return claim(''.join(word[0] for word in words[:4]))
    if len(words) == 3:
        consonants = [ch for ch in words[2][1:] if ch.isalpha() and ch not in 'aeiou']
        tail = consonants or [ch for ch in words[2][1:] if ch.isalpha()]
        return claim(words[0][0] + words[1][0] + words[2][0] + (tail[0] if tail else words[2][0]))
    if len(words) == 2:
        return claim(words[0][:2] + words[1][:2])
    return claim(words[0][:4])


def gather_customers(customers_data):
    flat = []
    by_id = {}
    for group in customers_data:
        for customer in group.get('customers', []):
            enriched = copy.deepcopy(customer)
            enriched['customerGroup'] = group.get('group', '')
            flat.append(enriched)
            by_id[customer['id']] = enriched
    return flat, by_id


def gather_kpis(node, acc):
    if not node:
        return
    if node.get('name'):
        acc.append(node['name'])
    for child in node.get('children', []):
        gather_kpis(child, acc)


def customer_kpi_names(customer):
    pyramids = customer.get('kpiPyramids', {})
    customer_names = []
    business_names = []
    customer_outcomes = pyramids.get('customerOutcomes', {})
    business_outcomes = pyramids.get('businessOutcomes', {})
    gather_kpis(customer_outcomes.get('top'), customer_names)
    for branch in customer_outcomes.get('branches', []):
        gather_kpis(branch, customer_names)
    gather_kpis(business_outcomes.get('top'), business_names)
    for branch in business_outcomes.get('branches', []):
        gather_kpis(branch, business_names)
    customer_names = list(dict.fromkeys(customer_names))
    business_names = list(dict.fromkeys(business_names))
    return {
        'customer': customer_names or ['Outcome confidence', 'Task success rate'],
        'business': business_names or ['Revenue growth', 'Adoption rate']
    }


def pick_two(values, start_index):
    if not values:
        return ['Metric', 'Metric']
    first = values[start_index % len(values)]
    if len(values) == 1:
        return [first, first]
    second = values[(start_index + 1) % len(values)]
    if second == first:
        for candidate in values:
            if candidate != first:
                second = candidate
                break
    return [first, second]


def capability_refs_from_customers(customers_data):
    refs = {}
    for group in customers_data:
        for customer in group.get('customers', []):
            for job in customer.get('jobsToBeDone', []):
                for step in job.get('steps', []):
                    for capability in step.get('capabilitiesNeeded', []):
                        key = capability.get('id') or capability.get('name')
                        if not key:
                            continue
                        if key not in refs:
                            refs[key] = {
                                'id': capability.get('id', slugify(capability.get('name', 'capability'))),
                                'name': capability.get('name', capability.get('id', 'Capability')),
                                'description': capability.get('how_it_supports', ''),
                                'domain': group.get('group', 'Customer Workflows'),
                                'group': slugify(job.get('name', 'workflow')) or 'workflow'
                            }
    return list(refs.values())


def normalize_bricks(domain_name, product_bricks_data, customers_data):
    if product_bricks_data:
        return product_bricks_data

    refs = capability_refs_from_customers(customers_data)
    generated = []
    used_ids = set()
    for ref in refs:
        generated.append({
            'name': ref['name'],
            'domain': ref['domain'],
            'id': derive_brick_id(ref['name'], used_ids),
            'type': 'full-stack',
            'group': ref['group'],
            'description': ref['description']
        })

    if not generated:
        generated = [
            {
                'name': f'{domain_name} Core Workflow',
                'domain': domain_name,
                'id': derive_brick_id(f'{domain_name} Core Workflow', used_ids),
                'type': 'full-stack',
                'group': 'core',
                'description': f'Primary workflow enablement for {domain_name}.'
            }
        ]

    return generated


def brick_lookup(product_bricks_data):
    lookup = {}
    for item in product_bricks_data:
        lookup[str(item['id'])] = item
    return lookup


def to_interfaces_from_channels(product):
    interfaces = []
    seen = set()

    def add_interface(interface_type, name, description, users=None, horizon='live'):
        key = (interface_type, name)
        if key in seen:
            return
        seen.add(key)
        interfaces.append({
            'type': interface_type,
            'name': name,
            'description': description,
            'users': users or ['Users'],
            'availabilityHorizon': horizon
        })

    for channel in product.get('channels', []):
        label = channel.lower()
        if 'web' in label or 'portal' in label or 'console' in label:
            add_interface('web', channel, f'{channel} interface for {product["name"]}.')
        elif 'ios' in label or 'android' in label or 'mobile' in label:
            add_interface('mobile_app', channel, f'{channel} interface for {product["name"]}.')
        elif 'dashboard' in label:
            add_interface('dashboard', channel, f'{channel} analytics surface for {product["name"]}.')
        elif 'public api' in label:
            add_interface('public_api', channel, f'{channel} for controlled external access to {product["name"]}.')
        elif 'partner' in label or 'integration' in label or 'rfid' in label or 'erp' in label:
            add_interface('partner_api', channel, f'{channel} interface for ecosystem connectivity around {product["name"]}.')
        else:
            add_interface('api', channel, f'{channel} interface for {product["name"]}.')

    for public_api in product.get('publicAPIs', []):
        add_interface('api', public_api.get('name', 'API'), public_api.get('purpose', ''))

    return interfaces


def normalize_products(domain, customers_by_id, bricks):
    products_path = os.path.join(ROOT, domain['id'], 'product', 'products.json')
    if os.path.exists(products_path):
        return load_json(products_path)

    delivery_path = os.path.join(ROOT, domain['id'], 'product', 'delivery.json')
    if os.path.exists(delivery_path):
        delivery = load_json(delivery_path)
        if 'portfolio' in delivery and 'products' in delivery['portfolio']:
            return delivery
        if 'products' in delivery:
            products = []
            for idx, product in enumerate(delivery['products'], start=1):
                normalized = {
                    'id': product.get('id', f'P{idx}'),
                    'name': product.get('name', f'{domain["name"]} Product {idx}'),
                    'type': product.get('category', product.get('type', 'Product')),
                    'primaryCustomers': [],
                    'interfaces': product.get('interfaces', []) or to_interfaces_from_channels(product),
                    'neededCapabilities': []
                }
                for persona_id in product.get('primaryPersonas', []):
                    customer = customers_by_id.get(persona_id)
                    normalized['primaryCustomers'].append({
                        'id': persona_id,
                        'name': customer.get('name', persona_id) if customer else persona_id
                    })
                capability_ids = product.get('coreCapabilityIds', []) + product.get('adjacentCapabilityIds', [])
                for capability_id in capability_ids:
                    brick = bricks.get(str(capability_id))
                    normalized['neededCapabilities'].append({
                        'capabilityCode': brick.get('id', str(capability_id)) if brick else str(capability_id),
                        'capabilityName': brick.get('name', str(capability_id)) if brick else str(capability_id),
                        'whyNeeded': f'Needed by {normalized["name"]} to support its core workflows.',
                        'mappingType': 'generated_from_delivery'
                    })
                products.append(normalized)
            return {
                'portfolio': {
                    'name': f'{domain["name"]} Portfolio',
                    'version': '1.0',
                    'products': products
                }
            }

    generated_profiles = {
        'arrive': [
            ('P1', 'Parking Operations Platform', 'B2B Operations'),
            ('P2', 'Driver Parking Experience', 'B2C / Driver'),
            ('P3', 'Open Parking Partner Hub', 'Partner Ecosystem')
        ],
        'internal': [
            ('P1', 'Revenue Operations Control Tower', 'Internal Operations'),
            ('P2', 'Seller Workflow Workspace', 'Internal Productivity'),
            ('P3', 'Commercial Intelligence Hub', 'Internal Analytics')
        ]
    }

    product_defs = generated_profiles.get(domain['id'], [
        ('P1', f'{domain["name"]} Core Platform', 'Core'),
        ('P2', f'{domain["name"]} User Workspace', 'Experience'),
        ('P3', f'{domain["name"]} Partner & Insights Hub', 'Partner')
    ])

    customer_list = list(customers_by_id.values())
    brick_list = list(bricks.values())
    products = []
    for idx, (product_id, name, product_type) in enumerate(product_defs):
        customer = customer_list[idx % len(customer_list)] if customer_list else None
        capability_slice = brick_list[idx * 4:(idx + 1) * 4] or brick_list[:4]
        interfaces = [
            {'type': 'web', 'name': f'{name} Web Workspace', 'description': f'Primary browser workspace for {name}.', 'users': ['Users'], 'availabilityHorizon': 'live'},
            {'type': 'dashboard', 'name': f'{name} Dashboard', 'description': f'Operational analytics view for {name}.', 'users': ['Managers'], 'availabilityHorizon': '1_year'},
            {'type': 'api', 'name': f'{name} API', 'description': f'Integration API for {name}.', 'users': ['Internal Systems', 'Partners'], 'availabilityHorizon': '1_year'}
        ]
        if idx == 1:
            interfaces.insert(1, {'type': 'mobile_app', 'name': f'{name} Mobile App', 'description': f'Mobile surface for {name}.', 'users': ['Mobile Users'], 'availabilityHorizon': 'live'})
        products.append({
            'id': product_id,
            'name': name,
            'type': product_type,
            'primaryCustomers': [{'id': customer['id'], 'name': customer['name']}] if customer else [],
            'interfaces': interfaces,
            'neededCapabilities': [
                {
                    'capabilityCode': capability.get('id', 'capability'),
                    'capabilityName': capability.get('name', capability.get('id', 'Capability')),
                    'whyNeeded': f'Needed by {name} to support a key workflow.',
                    'mappingType': 'generated_from_customers'
                }
                for capability in capability_slice
            ]
        })

    return {'portfolio': {'name': f'{domain["name"]} Portfolio', 'version': '1.0', 'products': products}}


def channel_alias(interface):
    name = interface.get('name', '').lower()
    interface_type = interface.get('type', 'web')
    if 'ios' in name:
        return 'ios'
    if 'android' in name:
        return 'android'
    if 'email' in name:
        return 'email-alerts'
    if 'push' in name:
        return 'push'
    if 'dashboard' in name or interface_type == 'dashboard':
        return 'dashboard'
    if 'partner' in name and 'api' in name:
        return 'partner-api'
    if 'public' in name and 'api' in name:
        return 'public-api'
    if 'api' in name or interface_type == 'api':
        return 'api'
    if interface_type == 'mobile_app':
        return 'mobile'
    return slugify(interface.get('name', interface_type)) or interface_type


def channel_id(product, interface):
    return f"{product.get('id', 'P')}-{channel_alias(interface)}"


def month_schedule():
    start_month = TODAY.month - 11
    year = TODAY.year
    month = TODAY.month
    months = []
    for offset in range(12):
        index = month - 11 + offset
        y = year
        while index <= 0:
            index += 12
            y -= 1
        while index > 12:
            index -= 12
            y += 1
        months.append((y, index))
    return months


def safe_date(year, month, day):
    if year == TODAY.year and month == TODAY.month and day > TODAY.day:
        day = max(1, TODAY.day - 1)
    return datetime.date(year, month, min(day, 28)).isoformat()


def synth_description(item_type, product, bricks, interfaces, customer):
    brick_names = [brick.get('name', brick.get('capabilityName', 'core capability')) for brick in bricks[:3]]
    channel_names = [interface.get('name', interface.get('type', 'channel')) for interface in interfaces[:2]]
    if item_type == 'initiative':
        return f"{product['name']} initiative focused on improving {', '.join(name.lower() for name in brick_names[:2])}, strengthening customer value for {customer['name']}, and evolving delivery across {', '.join(channel_names)}."
    return f"Release of {product['name']} improvements covering {', '.join(name.lower() for name in brick_names[:2])} across {', '.join(channel_names)}."


def expected_impact_text(kpi_name, brick_name, item_type):
    verb = 'Improve' if item_type == 'release' else 'Increase'
    return f"{verb} {kpi_name.lower()} through stronger {brick_name.lower()} support and cleaner workflow execution."


def generate_item(item_type, date_string, domain, product, customer, kpis, bricks, interfaces, item_index):
    customer_impact = []
    secondary_customer = None
    if product.get('primaryCustomers'):
        primary_id = product['primaryCustomers'][0]['id']
    else:
        primary_id = customer['id']
    customer_ids = [primary_id]
    if len(product.get('primaryCustomers', [])) > 1:
        customer_ids.append(product['primaryCustomers'][1]['id'])
    elif item_index % 4 == 0 and customer.get('id') != primary_id:
        customer_ids.append(customer['id'])

    for customer_id in customer_ids[:2]:
        c = domain['customers_by_id'].get(customer_id, customer)
        names = customer_kpi_names(c)
        brick_a = bricks[0].get('name', bricks[0].get('capabilityName', 'workflow')) if bricks else 'workflow'
        brick_b = bricks[1].get('name', bricks[1].get('capabilityName', 'workflow')) if len(bricks) > 1 else brick_a
        customer_pair = pick_two(names['customer'], item_index)
        business_pair = pick_two(names['business'], item_index)
        customer_impact.append({
            'customerId': c['id'],
            'customerKPIs': [
                {'kpi': customer_pair[0], 'expectedImpact': expected_impact_text(customer_pair[0], brick_a, item_type)},
                {'kpi': customer_pair[1], 'expectedImpact': expected_impact_text(customer_pair[1], brick_b, item_type)}
            ],
            'businessKPIs': [
                {'kpi': business_pair[0], 'expectedImpact': expected_impact_text(business_pair[0], brick_a, item_type)},
                {'kpi': business_pair[1], 'expectedImpact': expected_impact_text(business_pair[1], brick_b, item_type)}
            ]
        })

    return {
        'date': date_string,
        'description': synth_description(item_type, product, bricks, interfaces, customer),
        'customerImpact': customer_impact,
        'productBricks': [
            {
                'brickId': str(brick.get('id', brick.get('capabilityCode', f'brick-{idx}'))),
                'change': f"{'Released' if item_type == 'release' else 'Extended'} {brick.get('name', brick.get('capabilityName', 'capability'))} with domain-specific workflow improvements."
            }
            for idx, brick in enumerate(bricks[:4], start=1)
        ],
        'deliveryChannels': [
            {
                'channelId': channel_id(product, interface),
                'change': f"{'Deployed' if item_type == 'release' else 'Introduced'} workflow updates in {interface.get('name', interface.get('type', 'channel'))}."
            }
            for interface in interfaces[:3]
        ]
    }


def generate_time_series(domain, products_data, product_bricks_data, customers_flat, item_type):
    products = products_data.get('portfolio', {}).get('products', [])
    brick_map = brick_lookup(product_bricks_data)
    brick_list = list(brick_map.values())
    months = month_schedule()
    counts = [2 if idx % 2 == 0 else 3 for idx in range(12)]
    items = []
    running_index = 0

    for month_index, (year, month) in enumerate(months):
        count = counts[month_index]
        for position in range(count):
            product = products[running_index % len(products)]
            customer = customers_flat[running_index % len(customers_flat)]
            needed = product.get('neededCapabilities', [])
            product_bricks = []
            for needed_capability in needed:
                matched = None
                for brick in brick_list:
                    if brick.get('name') == needed_capability.get('capabilityName') or str(brick.get('id')) == str(needed_capability.get('capabilityCode')):
                        matched = brick
                        break
                if matched:
                    product_bricks.append(matched)
            if not product_bricks:
                product_bricks = brick_list[running_index % max(1, len(brick_list)):] + brick_list[:running_index % max(1, len(brick_list))]
            if not product_bricks:
                product_bricks = [{'id': 'cap-core', 'name': f'{domain["name"]} Core Capability'}]

            interfaces = product.get('interfaces', []) or [{'type': 'web', 'name': f'{product["name"]} Web'}]
            day = 6 + position * 9
            if item_type == 'release':
                day += 3
            item = generate_item(item_type, safe_date(year, month, day), domain, product, customer, customer_kpi_names(customer), product_bricks, interfaces, running_index)
            items.append(item)
            running_index += 1

    return {'items': items}


def ensure_domain_data(domain):
    domain_root = os.path.join(ROOT, domain['id'])
    customers_path = os.path.join(domain_root, 'product', 'customers.json')
    customers_data = load_json(customers_path)
    customers_flat, customers_by_id = gather_customers(customers_data)

    product_bricks_path = os.path.join(domain_root, 'product-bricks', 'product-bricks.json')
    existing_bricks = load_json(product_bricks_path) if os.path.exists(product_bricks_path) else None
    normalized_bricks = normalize_bricks(domain['name'], existing_bricks, customers_data)
    if not os.path.exists(product_bricks_path):
        save_json(product_bricks_path, normalized_bricks)

    bricks = brick_lookup(normalized_bricks)
    products_data = normalize_products(domain, customers_by_id, bricks)
    products_path = os.path.join(domain_root, 'product', 'products.json')
    if not os.path.exists(products_path):
        save_json(products_path, products_data)

    domain_context = {
        'id': domain['id'],
        'name': domain['name'],
        'customers_by_id': customers_by_id
    }
    initiatives = generate_time_series(domain_context, products_data, normalized_bricks, customers_flat, 'initiative')
    releases = generate_time_series(domain_context, products_data, normalized_bricks, customers_flat, 'release')
    save_json(os.path.join(domain_root, 'initiatives', 'initiatives.json'), initiatives)
    save_json(os.path.join(domain_root, 'initiatives', 'releases.json'), releases)


def main():
    config = load_json(os.path.join(ROOT, 'config.json'))
    for domain in config.get('domains', []):
        ensure_domain_data(domain)


if __name__ == '__main__':
    main()
