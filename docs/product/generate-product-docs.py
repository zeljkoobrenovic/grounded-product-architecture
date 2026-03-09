import json
import os
import shutil
import datetime

date_string = datetime.date.today().strftime('%Y-%m-%d')

domains_root = '../../_config/product-domains/'
templates_root = '../../_templates/product/product/'

config = json.load(open(domains_root + 'config.json'))


def copy_icons(icons_path, docs_folder):
    if os.path.exists(icons_path):
        for filename in os.listdir(icons_path):
            src = os.path.join(icons_path, filename)
            dst = os.path.join(docs_folder, 'icons', filename)
            if os.path.isfile(src):
                shutil.copy2(src, dst)


def create_overview_docs(domain, docs_folder):
    if os.path.exists(docs_folder): shutil.rmtree(docs_folder)
    os.makedirs(os.path.join(docs_folder, 'icons'), exist_ok=True)

    copy_icons(templates_root + 'icons', docs_folder)
    copy_icons(domains_root + domain['id'] + '/product/icons', docs_folder)

    with open(os.path.join(docs_folder, 'index.html'), 'w') as html_file:
        template = open(templates_root + 'products.html').read()
        html_file.write(template
                        .replace('${date}', date_string)
                        .replace('${domain_name}', domain['name'])
                        .replace('${domain_description}', domain['customer_description'])
                        .replace('${products}', json.dumps(products)))


def create_landing_pages(products, docs_folder):
    os.makedirs(os.path.join(docs_folder, 'landing_pages'), exist_ok=True)

    template = open(templates_root + 'landing_page.html').read()

    dateString = datetime.date.today().strftime('%Y-%m-%d')

    for product in group['products']:
        name = product['name']

        landing_page_file = docs_folder + '/landing_pages/' + str(product['id']) + '.html'
        with open(landing_page_file, 'w') as html_file:
            html_file.write(template
                            .replace('${date}', dateString)
                            .replace('${config}', json.dumps(config))
                            .replace('${all_products}', json.dumps(all_products))
                            .replace('${product_name}', product['name'])
                            .replace('${product}', json.dumps(product)))


for domain in config['domains']:
    domain_id = domain['id']
    domain_name = domain['name']

    products_file_path = domains_root + domain_id + '/product/products.json'
    if not os.path.exists(products_file_path): continue

    products = json.load(open(products_file_path))

    docs_folder = domain_id + '/product/'
    create_overview_docs(domain, docs_folder)
    # create_landing_pages(products, docs_folder)
