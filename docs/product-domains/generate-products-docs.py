import json
import os
import shutil
import datetime
from initiatives_support import load_domain_activity, filter_for_product

date_string = datetime.date.today().strftime('%Y-%m-%d')

domains_root = '../../_config/product-domains/'
templates_root = '../../_templates/products/'

config = json.load(open(domains_root + 'config.json'))


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
                                .replace('${date}', date_string)
                                .replace('${config}', json.dumps(config))
                                .replace('${all_products}', json.dumps(products['portfolio']['products']))
                                .replace('${product_name}', product['name'])
                                .replace('${product}', json.dumps(product))
                                .replace('${initiatives}', json.dumps(filter_for_product(activity_data['initiatives'], product['id'])))
                                .replace('${releases}', json.dumps(filter_for_product(activity_data['releases'], product['id']))))


for domain in config['domains']:
    domain_id = domain['id']
    domain_name = domain['name']

    products_file_path = domains_root + domain_id + '/products/products.json'
    print(products_file_path)
    if not os.path.exists(products_file_path): continue

    products = json.load(open(products_file_path))
    activity_data = load_domain_activity(domains_root, domain_id)

    docs_folder = domain_id + '/products/'
    create_overview_docs(domain, docs_folder)
    create_landing_pages(products, docs_folder, activity_data)
