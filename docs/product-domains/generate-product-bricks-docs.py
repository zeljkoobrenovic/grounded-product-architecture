import json
import datetime
import os
import shutil
from initiatives_support import load_domain_activity, filter_for_brick
from product_bricks_support import flatten_product_bricks, load_product_bricks_payload

def load_json_if_exists(path, default_value):
    if os.path.exists(path):
        return json.load(open(path))
    return default_value


def copy_icons(icons_path, docs_folder):
    if os.path.exists(icons_path):
        for filename in os.listdir(icons_path):
            src = os.path.join(icons_path, filename)
            dst = os.path.join(docs_folder, 'icons', filename)
            if os.path.isfile(src):
                shutil.copy2(src, dst)


date_string = datetime.date.today().strftime('%Y-%m-%d')

domains_root = '../../_config/product-domains/'
root_templates = '../../_templates/product-bricks/'

config = json.load(open(domains_root + 'config.json'))
evidence_fragments_cache = load_json_if_exists('../../_config/evidence-fragments/cache/evidence-fragments.json', [])


def slugify(value):
    return str(value).strip().lower().replace(' / ', '-').replace(' ', '-')


def build_fragment_id(group_title, fragment):
    report_link = ''
    for link in fragment.get('links', []):
        if link.get('label') == 'Sokrates HTML Reports':
            report_link = link.get('url', '')
            break
    slug = report_link.split('/')[0] if report_link else slugify(fragment.get('title', ''))
    return slugify(group_title) + '/' + slug


def build_evidence_lookup(cache_groups):
    lookup = {}
    for group in cache_groups:
        group_title = group.get('group', {}).get('title', '')
        group_description = group.get('group', {}).get('description', '')
        for fragment in group.get('fragments', []):
            fragment_id = build_fragment_id(group_title, fragment)
            enriched_fragment = dict(fragment)
            enriched_fragment['id'] = fragment_id
            enriched_fragment['evidenceGroupTitle'] = group_title
            enriched_fragment['evidenceGroupDescription'] = group_description
            lookup[fragment_id] = enriched_fragment
    return lookup


evidence_fragment_lookup = build_evidence_lookup(evidence_fragments_cache)


def build_customer_lookup(customers):
    lookup = {}
    for group in customers:
        group_name = group.get('group', '')
        for customer in group.get('customers', []):
            enriched = dict(customer)
            enriched['group'] = group_name
            lookup[customer['id']] = enriched
    return lookup


def build_brick_context(brick, products, customers):
    customer_lookup = build_customer_lookup(customers)
    linked_products = []
    supported_jobs = []
    supported_jobs_index = {}

    brick_id = str(brick.get('id', '')).strip().lower()
    brick_name = str(brick.get('name', '')).strip().lower()

    def capability_matches(capability):
        capability_code = str(capability.get('id', capability.get('capabilityCode', ''))).strip().lower()
        capability_name = str(capability.get('name', capability.get('capabilityName', ''))).strip().lower()
        return capability_code == brick_id or capability_name == brick_name

    def append_supported_job(customer, primary_customer, product, job, step, capability, matched_capability):
        item_key = (
            customer.get('id', primary_customer.get('id', '')),
            product.get('id', ''),
            job.get('id', ''),
        )
        if item_key not in supported_jobs_index:
            supported_jobs_index[item_key] = {
                'customerId': customer.get('id', primary_customer.get('id', '')),
                'customerName': customer.get('name', primary_customer.get('name', '')),
                'customerGroup': customer.get('group', ''),
                'customerIcon': customer.get('icon', 'customer.png'),
                'productId': product.get('id', ''),
                'productName': product.get('name', ''),
                'productIcon': product.get('icon', 'product.png'),
                'jobId': job.get('id', ''),
                'jobName': job.get('name', ''),
                'jobWhatItIs': job.get('what_it_is', ''),
                'jobOutcome': job.get('outcome', ''),
                'supportRationale': capability.get('how_it_supports', '') or matched_capability.get('whyNeeded', ''),
                'usedInSteps': []
            }
            supported_jobs.append(supported_jobs_index[item_key])

        supported_job = supported_jobs_index[item_key]
        used_step = {
            'step': step.get('step', ''),
            'description': step.get('description', ''),
            'howItSupports': capability.get('how_it_supports', '') or matched_capability.get('whyNeeded', '')
        }
        if used_step not in supported_job['usedInSteps']:
            supported_job['usedInSteps'].append(used_step)

    for product in products.get('portfolio', {}).get('products', []):
        matched_capability = None
        for capability in product.get('neededCapabilities', []):
            if capability_matches(capability):
                matched_capability = capability
                break

        if not matched_capability:
            continue

        linked_products.append({
            'id': product.get('id', ''),
            'name': product.get('name', ''),
            'icon': product.get('icon', 'product.png'),
            'type': product.get('type', ''),
            'whyUsed': matched_capability.get('whyNeeded', '')
        })

        for primary_customer in product.get('primaryCustomers', []):
            customer = customer_lookup.get(primary_customer.get('id', ''), {})
            for job in customer.get('jobsToBeDone', []):
                for step in job.get('steps', []):
                    for capability in step.get('capabilitiesNeeded', []):
                        if capability_matches(capability):
                            append_supported_job(customer, primary_customer, product, job, step, capability, matched_capability)

    return linked_products, supported_jobs


def build_brick_evidence(brick_id, evidence_items):
    matched_item = next((item for item in evidence_items if str(item.get('brick-id', '')).strip() == str(brick_id).strip()), None)
    if not matched_item:
        return {'brickId': brick_id, 'groups': []}

    groups = []
    for item in matched_item.get('evidence-filters', []):
        fragments = []
        for fragment_id in item.get('evidence-fragment-ids', []):
            fragment = evidence_fragment_lookup.get(fragment_id)
            if fragment:
                fragments.append(fragment)
        groups.append({
            'name': item.get('group-name', ''),
            'description': item.get('description', ''),
            'fragments': fragments
        })

    return {'brickId': brick_id, 'groups': groups}


def create_landing_pages(bricks, activity_data, products, customers, evidence_items):
    landing_page_template = open(root_templates + 'landing_page.html').read();

    capabilities_map = {}
    for brick in bricks:
        capabilities_map[brick['name']] = brick

    capabilities_name_index = {}

    for brick in bricks:
        name = brick['name']
        capabilities_name_index[name.lower().strip()] = brick

    for brick in bricks:
        name = brick['name']
        linked_products, supported_jobs = build_brick_context(brick, products, customers)
        evidence = build_brick_evidence(brick['id'], evidence_items)

        htmlFile = docs_folder + 'landing_pages/' + str(brick['id']) + '.html'
        with open(htmlFile, 'w') as html_file:
            html_file.write(landing_page_template
                            .replace('${date}', date_string)
                            .replace('${config}', json.dumps(config))
                            .replace('${all_bricks}', json.dumps(bricks))
                            .replace('${brick_name}', name.replace('&', '&amp;'))
                            .replace('${brick_data}', json.dumps(brick))
                            .replace('${evidence}', json.dumps(evidence))
                            .replace('${linked_products}', json.dumps(linked_products))
                            .replace('${supported_jobs}', json.dumps(supported_jobs))
                            .replace('${initiatives}', json.dumps(filter_for_brick(activity_data['initiatives'], brick['id'])))
                            .replace('${releases}', json.dumps(filter_for_brick(activity_data['releases'], brick['id']))))


for domain in config['domains']:
    domain_id = domain['id']
    domain_name = domain['name']

    docs_folder = domain_id + '/product-bricks/'

    root_domain = domains_root + docs_folder

    product_bricks_config_path = root_domain + 'product-bricks.json'

    if not os.path.exists(product_bricks_config_path):
        print("Skipping " + root_domain)
        continue

    print(root_domain)

    if os.path.exists(docs_folder): shutil.rmtree(docs_folder)
    os.makedirs(os.path.join(docs_folder, 'icons'), exist_ok=True)
    os.makedirs(os.path.join(docs_folder, 'landing_pages'), exist_ok=True)

    data = load_product_bricks_payload(product_bricks_config_path)
    flat_bricks = flatten_product_bricks(data)
    activity_data = load_domain_activity(domains_root, domain_id)
    products = load_json_if_exists(domains_root + domain_id + '/products/products.json', {'portfolio': {'products': []}})
    customers = load_json_if_exists(domains_root + domain_id + '/customers/customers.json', [])
    evidence_items = load_json_if_exists(root_domain + 'evidence.json', [])

    def get_groups(bricks_list):
        groups_map = {}
        groups_list = []
        sub_groups = {}

        for (item) in bricks_list:
            sub_domain = item['domain'].strip()

            if sub_domain not in groups_map:
                groups_map[sub_domain] = []
                groups_list.append({'domain': sub_domain, 'groups': groups_map[sub_domain]})

            if item.get('group'):
                sub_group = item['group']
            else:
                sub_group = ''

            key = sub_domain + '_' + sub_group

            if key not in sub_groups:
                sub_groups[key] = {'group': sub_group, 'items': []}
                groups_map[sub_domain].append(sub_groups[key])

            sub_groups[key]['items'].append(item)

        return groups_list


    copy_icons(root_templates + 'icons', docs_folder)
    copy_icons(domains_root + domain_id + '/product-bricks/icons', docs_folder)

    def process():
        with open(docs_folder + 'index.html', 'w') as html_file:
            template = open(root_templates + 'index.html').read()
            content = template.replace('${domain_name}', domain_name)
            content = content.replace('${domain_description}', domain['description'])
            content = content.replace('${bricks}', json.dumps(data))
            html_file.write(content)

    process()

    create_landing_pages(flat_bricks, activity_data, products, customers, evidence_items)
