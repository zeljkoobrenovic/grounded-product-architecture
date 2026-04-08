import json
import os
import shutil
import datetime
from domain_cli import load_domain_args
from initiatives_support import load_domain_activity, filter_for_product

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
os.chdir(os.path.join(REPO_ROOT, 'docs', 'product-domains'))

date_string = datetime.date.today().strftime('%Y-%m-%d')

domains_root = '../../_config/product-domains/'
templates_root = '../../_templates/products/'
domain, site_config = load_domain_args()
common_style = open(templates_root + '../_imports/common/style.html').read()
tabs_style = open(templates_root + '../_imports/tabs/style.html').read()
tabs_script = open(templates_root + '../_imports/tabs/script.html').read()
breadcrumbs_style = open(templates_root + '../_imports/breadcrumbs/style.html').read()
breadcrumbs_script = open(templates_root + '../_imports/breadcrumbs/script.html').read()


def render_breadcrumbs(template_name, replacements):
    breadcrumbs = open(os.path.join(templates_root, template_name)).read()
    for key, value in replacements.items():
        breadcrumbs = breadcrumbs.replace('${' + key + '}', value)
    return breadcrumbs


def copy_icons(icons_path, docs_folder):
    if os.path.exists(icons_path):
        target_root = os.path.join(docs_folder, 'icons')
        for root, _, filenames in os.walk(icons_path):
            rel_root = os.path.relpath(root, icons_path)
            target_dir = target_root if rel_root == '.' else os.path.join(target_root, rel_root)
            os.makedirs(target_dir, exist_ok=True)
            for filename in filenames:
                src = os.path.join(root, filename)
                dst = os.path.join(target_dir, filename)
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


def build_customers_lookup(customers):
    customer_icon_map = {
        'house-search': 'seeker.png',
        'owner-key': 'owner.png',
        'briefcase-building': 'intermediary.png'
    }

    lookup = {}
    for group in customers:
        for customer in group.get('customers', []):
            lookup[customer['id']] = {
                'id': customer['id'],
                'name': customer.get('name', customer['id']),
                'icon': normalize_icon_name(customer_icon_map.get(customer.get('icon', ''), customer.get('icon', 'customer.png')))
            }
    return lookup


def enrich_products_with_customers(products, customers_lookup):
    enriched = json.loads(json.dumps(products))
    for product in enriched.get('portfolio', {}).get('products', []):
        primary_customers = []
        for customer in product.get('primaryCustomers', []):
            customer_id = customer.get('id', '')
            info = customers_lookup.get(customer_id, {})
            primary_customers.append({
                'id': customer_id,
                'name': customer.get('name', info.get('name', customer_id)),
                'icon': info.get('icon', 'customer.png')
            })
        product['primaryCustomers'] = primary_customers
    return enriched


def create_overview_docs(domain, docs_folder):
    if os.path.exists(docs_folder): shutil.rmtree(docs_folder)
    os.makedirs(os.path.join(docs_folder, 'icons'), exist_ok=True)

    copy_icons(templates_root + 'icons', docs_folder)
    copy_icons(domains_root + domain['id'] + '/products/icons', docs_folder)

    with open(os.path.join(docs_folder, 'index.html'), 'w') as html_file:
        template = open(templates_root + 'index.html').read()
        deployment_path = domains_root + domain['id'] + '/products/deployment.json'
        deployment = json.load(open(deployment_path)) if os.path.exists(deployment_path) else {'metadata': {}, 'channels': []}
        html_file.write(template
                        .replace('${tabs_style}', tabs_style)
                        .replace('${tabs_script}', tabs_script)
                        .replace('${breadcrumbs_style}', breadcrumbs_style)
                        .replace('${breadcrumbs_script}', breadcrumbs_script)
                        .replace('${breadcrumbs}', render_breadcrumbs('index_breadcrumbs.json', {
                            'domain_name': domain['name']
                        }))
                        .replace('${date}', date_string)
                        .replace('${domain_name}', domain['name'])
                        .replace('${domain_description}', domain['description'])
                        .replace('${products}', json.dumps(products))
                        .replace('${deployment}', json.dumps(deployment)))

def create_landing_pages(products, docs_folder, activity_data):
    os.makedirs(os.path.join(docs_folder, 'landing_pages'), exist_ok=True)

    template = open(templates_root + 'landing_page.html').read()

    date_string = datetime.date.today().strftime('%Y-%m-%d')

    if 'portfolio' in products:
        for product in products['portfolio']['products']:
            landing_page_file = docs_folder + '/landing_pages/' + str(product['id']) + '.html'
            with open(landing_page_file, 'w') as html_file:
                html_file.write(template
                                .replace('${common_style}', common_style)
                                .replace('${tabs_style}', tabs_style)
                                .replace('${tabs_script}', tabs_script)
                                .replace('${breadcrumbs_style}', breadcrumbs_style)
                                .replace('${breadcrumbs_script}', breadcrumbs_script)
                                .replace('${breadcrumbs}', render_breadcrumbs('landing_page_breadcrumbs.json', {
                                    'domain_name': domain['name'],
                                    'product_name': product['name']
                                }))
                                .replace('${date}', date_string)
                                .replace('${config}', json.dumps(site_config))
                                .replace('${all_products}', json.dumps(products['portfolio']['products']))
                                .replace('${product_name}', product['name'])
                                .replace('${product}', json.dumps(product))
                                .replace('${initiatives}', json.dumps(filter_for_product(activity_data['initiatives'], product['id'])))
                                .replace('${releases}', json.dumps(filter_for_product(activity_data['releases'], product['id']))))


def create_deployment_landing_pages(domain, products, docs_folder):
    deployment_path = domains_root + domain['id'] + '/products/deployment.json'
    deployment = json.load(open(deployment_path)) if os.path.exists(deployment_path) else {'metadata': {}, 'channels': []}

    target_folder = os.path.join(docs_folder, 'deployment')
    os.makedirs(target_folder, exist_ok=True)

    template = open(templates_root + 'deployment_landing_page.html').read()

    for group in deployment.get('channels', []):
        group_id = group.get('groupId', '')
        for channel in group.get('channels', []):
            channel_id = channel.get('subChannelId', '')
            if not group_id or not channel_id:
                continue

            channel_ref = group_id + '/' + channel_id
            landing_page_file = os.path.join(target_folder, channel_id + '.html')
            with open(landing_page_file, 'w') as html_file:
                html_file.write(template
                                .replace('${common_style}', common_style)
                                .replace('${tabs_style}', tabs_style)
                                .replace('${tabs_script}', tabs_script)
                                .replace('${breadcrumbs_style}', breadcrumbs_style)
                                .replace('${breadcrumbs_script}', breadcrumbs_script)
                                .replace('${breadcrumbs}', render_breadcrumbs('deployment_landing_page_breadcrumbs.json', {
                                    'domain_name': domain['name'],
                                    'channel_name': channel.get('name', channel_id)
                                }))
                                .replace('${date}', date_string)
                                .replace('${domain_description}', domain['description'])
                                .replace('${products}', json.dumps(products))
                                .replace('${deployment}', json.dumps(deployment))
                                .replace('${channel_ref}', json.dumps(channel_ref)))

domain_id = domain['id']
products_file_path = domains_root + domain_id + '/products/products.json'
print(products_file_path)
if not os.path.exists(products_file_path):
    raise SystemExit(f"Missing products config for domain '{domain_id}'")

customers_path = domains_root + domain_id + '/customers/customers.json'
if not os.path.exists(customers_path):
    customers_path = domains_root + domain_id + '/product/customers.json'

customers = json.load(open(customers_path)) if os.path.exists(customers_path) else []
customers_lookup = build_customers_lookup(customers)

products = enrich_products_with_customers(json.load(open(products_file_path)), customers_lookup)
activity_data = load_domain_activity(domains_root, domain_id)

docs_folder = domain_id + '/products/'
create_overview_docs(domain, docs_folder)
create_landing_pages(products, docs_folder, activity_data)
create_deployment_landing_pages(domain, products, docs_folder)
