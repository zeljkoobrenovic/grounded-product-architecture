import json
import os
import shutil

from domain_cli import load_domain_args
from generator_common import copy_icons, enter_docs_root, today_string

enter_docs_root()

date_string = today_string()

apps = json.load(open('../../_config/product-domains/start/apps.json'))

domains_root = '../../_config/product-domains/'
templates_root = '../../_templates/start/'
domain, _ = load_domain_args()

tabs_style = open(templates_root + '../_imports/tabs/style.html').read()
tokens_style = open(templates_root + '../_imports/tokens/style.html').read()
tabs_script = open(templates_root + '../_imports/tabs/script.html').read()


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
                        .replace('${tabs_style}', tabs_style)
                        .replace('${tokens_style}', tokens_style)
                        .replace('${tabs_script}', tabs_script)
                        .replace('${date}', date_string)
                        .replace('${apps}', json.dumps(apps))
                        .replace('${domain_name}', domain['name'])
                        .replace('${domain_description}', domain['description']))


docs_folder = domain['id'] + '/start/'
create_docs(domain, docs_folder)
