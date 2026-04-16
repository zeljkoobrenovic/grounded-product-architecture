import json
import os
import shutil
import datetime

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
os.chdir(os.path.join(REPO_ROOT, 'docs'))

date_string = datetime.date.today().strftime('%Y-%m-%d')

apps = json.load(open('../_config/start-apps/apps.json'))

templates_root = '../_templates/start/'
apps_root = '../_config/start-apps/'


def copy_icons(icons_path, docs_folder):
    if os.path.exists(icons_path):
        for filename in os.listdir(icons_path):
            src = os.path.join(icons_path, filename)
            dst = os.path.join(docs_folder, 'icons', filename)
            if os.path.isfile(src):
                shutil.copy2(src, dst)


docs_folder = 'start-apps/'

if os.path.exists(docs_folder): shutil.rmtree(docs_folder)
os.makedirs(os.path.join(docs_folder, 'icons'), exist_ok=True)

copy_icons(templates_root + 'icons', docs_folder)
copy_icons(apps_root + 'icons', docs_folder)

with open(os.path.join(docs_folder, 'index.html'), 'w') as html_file:
    template = open(templates_root + 'index.html').read()
    html_file.write(template
                    .replace('${date}', date_string)
                    .replace('${apps}', json.dumps(apps))
                    .replace('${domain_name}', 'AI-Driven Product Architectures')
                    .replace('${domain_description}', 'Defining customer-centric product architecture rooted in reality,<br> combining the power of GenAI with <a target="_blank" href="https://grounded-architecture.io/">grounded architecture</a> principles. Available free on on <a target="_blank" href="https://github.com/zeljkoobrenovic/grounded-product-architecture">GitHub'))

