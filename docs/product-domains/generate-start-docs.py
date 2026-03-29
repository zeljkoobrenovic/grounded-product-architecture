import json
import os
import shutil
import datetime
from initiatives_support import load_domain_activity, filter_for_product

date_string = datetime.date.today().strftime('%Y-%m-%d')

apps = json.load(open('../../_config/product-domains/start/apps.json'))

domains_root = '../../_config/product-domains/'
templates_root = '../../_templates/start/'

config = json.load(open(domains_root + 'config.json'))


def copy_icons(icons_path, docs_folder):
    if os.path.exists(icons_path):
        for filename in os.listdir(icons_path):
            src = os.path.join(icons_path, filename)
            dst = os.path.join(docs_folder, 'icons', filename)
            if os.path.isfile(src):
                shutil.copy2(src, dst)


def create_docs(domain_id, config, docs_folder):
    if os.path.exists(docs_folder): shutil.rmtree(docs_folder)
    os.makedirs(os.path.join(docs_folder, 'icons'), exist_ok=True)

    copy_icons(templates_root + 'icons', docs_folder)
    copy_icons(domains_root + domain_id + '/start/icons', docs_folder)

    with open(os.path.join(docs_folder, 'index.html'), 'w') as html_file:
        template = open(templates_root + 'index.html').read()
        print(config['description'])
        html_file.write(template
                        .replace('${date}', date_string)
                        .replace('${apps}', json.dumps(apps))
                        .replace('${domain_name}', config['name'])
                        .replace('${domain_description}', config['description']))


for domain in config['domains']:
    domain_id = domain['id']

    config_file_path = domains_root + domain_id + '/start/config.json'
    if not os.path.exists(config_file_path): continue

    config = json.load(open(config_file_path))

    docs_folder = domain_id + '/start/'
    create_docs(domain_id, config, docs_folder)
