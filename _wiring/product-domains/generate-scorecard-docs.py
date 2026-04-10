import json
import os
import shutil

from domain_cli import load_domain_args

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
os.chdir(os.path.join(REPO_ROOT, 'docs', 'product-domains'))

domains_root = '../../_config/product-domains/'
templates_root = '../../_templates/scorecard/'

tabs_style = open(os.path.join(templates_root, '../_imports/tabs/style.html')).read()
tabs_script = open(os.path.join(templates_root, '../_imports/tabs/script.html')).read()
breadcrumbs_style = open(os.path.join(templates_root, '../_imports/breadcrumbs/style.html')).read()
breadcrumbs_script = open(os.path.join(templates_root, '../_imports/breadcrumbs/script.html')).read()

domain, _ = load_domain_args()


def render_breadcrumbs(template_name, replacements):
    breadcrumbs = open(os.path.join(templates_root, template_name)).read()
    for key, value in replacements.items():
        breadcrumbs = breadcrumbs.replace('${' + key + '}', value)
    return breadcrumbs


def load_json_if_exists(path):
    if not os.path.exists(path):
        return None
    with open(path) as handle:
        return json.load(handle)


def copy_icons(icons_path, docs_folder):
    if not os.path.exists(icons_path):
        return
    os.makedirs(os.path.join(docs_folder, 'icons'), exist_ok=True)
    for filename in os.listdir(icons_path):
        src = os.path.join(icons_path, filename)
        dst = os.path.join(docs_folder, 'icons', filename)
        if os.path.isfile(src):
            shutil.copy2(src, dst)


def create_docs(domain_config, payload):
    docs_folder = os.path.join(domain_config['id'], 'business-scorecard')
    os.makedirs(docs_folder, exist_ok=True)
    copy_icons(os.path.join(templates_root, 'icons'), docs_folder)

    template = open(os.path.join(templates_root, 'index.html')).read()
    page_title = f"{domain_config['name']} Business Scorecard"

    with open(os.path.join(docs_folder, 'index.html'), 'w') as html_file:
        html_file.write(
            template
            .replace('${page_title}', page_title)
            .replace('${tabs_style}', tabs_style)
            .replace('${tabs_script}', tabs_script)
            .replace('${breadcrumbs_style}', breadcrumbs_style)
            .replace('${breadcrumbs_script}', breadcrumbs_script)
            .replace('${breadcrumbs}', render_breadcrumbs('index_breadcrumbs.json', {
                'domain_name': domain_config['name']
            }))
            .replace('${data}', json.dumps(payload))
        )


scorecard_path = os.path.join(domains_root, domain['id'], 'business', 'scorecard.json')
scorecard = load_json_if_exists(scorecard_path)

if scorecard is not None:
    create_docs(domain, scorecard)
