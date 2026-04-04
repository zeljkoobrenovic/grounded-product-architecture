import json
import os
import shutil
import datetime
from domain_cli import load_domain_args

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
os.chdir(os.path.join(REPO_ROOT, 'docs', 'product-domains'))

date_string = datetime.date.today().strftime('%Y-%m-%d')

apps = json.load(open('../../_config/product-domains/start/apps.json'))

domains_root = '../../_config/product-domains/'
templates_root = '../../_templates/start/'
domain, _ = load_domain_args()


def copy_icons(icons_path, docs_folder):
    if os.path.exists(icons_path):
        for filename in os.listdir(icons_path):
            src = os.path.join(icons_path, filename)
            dst = os.path.join(docs_folder, 'icons', filename)
            if os.path.isfile(src):
                shutil.copy2(src, dst)


def create_docs(domain, docs_folder):
    if os.path.exists(docs_folder): shutil.rmtree(docs_folder)
    os.makedirs(os.path.join(docs_folder, 'icons'), exist_ok=True)

    domain_id = domain['id']
    copy_icons(templates_root + 'icons', docs_folder)
    copy_icons(domains_root + domain_id + '/start/icons', docs_folder)

    with open(os.path.join(docs_folder, 'index.html'), 'w') as html_file:
        template = open(templates_root + 'index.html').read()
        print(domain['description'])
        html_file.write(template
                        .replace('${date}', date_string)
                        .replace('${apps}', json.dumps(apps))
                        .replace('${domain_name}', domain['name'])
                        .replace('${domain_description}', domain['description']))


docs_folder = domain['id'] + '/start/'
create_docs(domain, docs_folder)
