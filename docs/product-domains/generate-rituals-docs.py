import datetime
import json
import os
import shutil


date_string = datetime.date.today().strftime('%Y-%m-%d')

domains_root = '../../_config/product-domains/'
templates_root = '../../_templates/rituals/'

config = json.load(open(domains_root + 'config.json'))
default_rituals = json.load(open(domains_root + 'rituals/meetings.json'))


def copy_icons(icons_path, docs_folder):
    if os.path.exists(icons_path):
        os.makedirs(os.path.join(docs_folder, 'icons'), exist_ok=True)
        for filename in os.listdir(icons_path):
            src = os.path.join(icons_path, filename)
            dst = os.path.join(docs_folder, 'icons', filename)
            if os.path.isfile(src):
                shutil.copy2(src, dst)


def load_rituals_for_domain(domain_id):
    domain_rituals_path = os.path.join(domains_root, domain_id, 'rituals', 'meetings.json')
    if os.path.exists(domain_rituals_path):
        return json.load(open(domain_rituals_path))
    return default_rituals


def create_overview_docs(domain, docs_folder, rituals):
    if os.path.exists(docs_folder):
        shutil.rmtree(docs_folder)
    os.makedirs(os.path.join(docs_folder, 'landing_pages'), exist_ok=True)
    copy_icons(os.path.join(templates_root, 'icons'), docs_folder)

    with open(os.path.join(docs_folder, 'index.html'), 'w') as html_file:
        template = open(templates_root + 'index.html').read()
        html_file.write(template
                        .replace('${date}', date_string)
                        .replace('${domain_name}', domain['name'])
                        .replace('${domain_description}', domain['description'])
                        .replace('${rituals}', json.dumps(rituals)))


def create_landing_pages(domain, docs_folder, rituals):
    template = open(templates_root + 'landing_page.html').read()

    for meeting in rituals.get('meetings', []):
        landing_page_file = os.path.join(docs_folder, 'landing_pages', str(meeting['id']) + '.html')
        with open(landing_page_file, 'w') as html_file:
            html_file.write(template
                            .replace('${date}', date_string)
                            .replace('${domain_name}', domain['name'])
                            .replace('${meeting_title}', meeting.get('title', 'Ritual'))
                            .replace('${meeting}', json.dumps(meeting)))


for domain in config['domains']:
    docs_folder = domain['id'] + '/rituals/'
    rituals = load_rituals_for_domain(domain['id'])
    create_overview_docs(domain, docs_folder, rituals)
    create_landing_pages(domain, docs_folder, rituals)
