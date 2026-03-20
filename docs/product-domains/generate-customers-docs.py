import json
import os
import shutil
import datetime
from initiatives_support import load_domain_activity, filter_for_customer

date_string = datetime.date.today().strftime('%Y-%m-%d')

domains_root = '../../_config/product-domains/'
templates_root = '../../_templates/customers/'

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
    copy_icons(domains_root + domain['id'] + '/customers/icons', docs_folder)

    with open(os.path.join(docs_folder, 'index.html'), 'w') as html_file:
        template = open(templates_root + 'index.html').read()
        html_file.write(template
                        .replace('${date}', date_string)
                        .replace('${domain_name}', domain['name'])
                        .replace('${domain_description}', domain['description'])
                        .replace('${customers}', json.dumps(customers)))


def create_landing_pages(customers, docs_folder, activity_data):
    os.makedirs(os.path.join(docs_folder, 'landing_pages'), exist_ok=True)

    template = open(templates_root + 'landing_page.html').read()

    dateString = datetime.date.today().strftime('%Y-%m-%d')

    all_customers = []

    for group in customers:
        print(group['group'])
        for customer in group['customers']:
            customer['domain'] = group['group']
            all_customers.append(customer)

    for group in customers:
        for customer in group['customers']:
            name = customer['name']

            landing_page_file = docs_folder + '/landing_pages/' + str(customer['id']) + '.html'
            with open(landing_page_file, 'w') as html_file:
                html_file.write(template
                                .replace('${date}', dateString)
                                .replace('${config}', json.dumps(config))
                                .replace('${all_customers}', json.dumps(all_customers))
                                .replace('${customer_name}', customer['name'])
                                .replace('${customer}', json.dumps(customer))
                                .replace('${discoveries}', json.dumps(filter_for_customer(activity_data['discoveries'], customer['id'])))
                                .replace('${initiatives}', json.dumps(filter_for_customer(activity_data['initiatives'], customer['id'])))
                                .replace('${releases}', json.dumps(filter_for_customer(activity_data['releases'], customer['id']))))


for domain in config['domains']:
    domain_id = domain['id']
    domain_name = domain['name']

    customers_file_path = domains_root + domain_id + '/customers/customers.json'
    if not os.path.exists(customers_file_path): continue

    customers = json.load(open(customers_file_path))
    activity_data = load_domain_activity(domains_root, domain_id)

    docs_folder = domain_id + '/customers/'
    create_overview_docs(domain, docs_folder)
    create_landing_pages(customers, docs_folder, activity_data)
