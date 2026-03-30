import datetime
import json
import os
import shutil


date_string = datetime.date.today().strftime('%Y-%m-%d')

domains_root = '../../_config/product-domains/'
templates_root = '../../_templates/ktlo/'
initiatives_templates_root = '../../_templates/initiatives/'

config = json.load(open(domains_root + 'config.json'))


def copy_media(source_path, target_path):
    if os.path.exists(source_path):
        for filename in os.listdir(source_path):
            src = os.path.join(source_path, filename)
            dst = os.path.join(target_path, filename)
            if os.path.isfile(src):
                shutil.copy2(src, dst)


def objective_items(payload):
    return payload.get('objectives', [])


def create_overview_docs(domain, docs_folder, ktlo_payload, initiatives_payload):
    if os.path.exists(docs_folder):
        shutil.rmtree(docs_folder)

    os.makedirs(os.path.join(docs_folder, 'icons'), exist_ok=True)
    os.makedirs(os.path.join(docs_folder, 'landing_pages'), exist_ok=True)

    copy_media(initiatives_templates_root + 'icons', docs_folder + 'icons')
    copy_media(templates_root + 'icons', docs_folder + 'icons')
    copy_media(domains_root + domain['id'] + '/ktlo/icons', docs_folder + 'icons')

    template = open(templates_root + 'index.html').read()
    with open(os.path.join(docs_folder, 'index.html'), 'w') as html_file:
        html_file.write(template
                        .replace('${domain_name}', domain['name'])
                        .replace('${ktlo}', json.dumps(ktlo_payload))
                        .replace('${initiatives}', json.dumps(initiatives_payload)))


def create_landing_pages(domain, docs_folder, ktlo_payload, initiatives_payload):
    template = open(templates_root + 'landing_page.html').read()
    initiative_template = open(initiatives_templates_root + 'landing_page.html').read()

    for objective in objective_items(ktlo_payload):
        linked_initiatives = [
            item for item in initiatives_payload.get('items', [])
            if (item.get('keyResultId') or '').startswith((objective.get('id') or '') + '/')
        ]

        page = (template
                .replace('${page_title}', f"KTLO | {objective.get('title', 'Objective')} ({domain['name']})")
                .replace('${domain_name}', domain['name'])
                .replace('${date}', date_string)
                .replace('${objective_title}', objective.get('title', 'KTLO Objective'))
                .replace('${objective_statement}', objective.get('objective', ''))
                .replace('${objective_status}', objective.get('status', 'active'))
                .replace('${objective_period}', (objective.get('period') or {}).get('type', 'rolling'))
                .replace('${objective_id}', objective.get('id', ''))
                .replace('${ktlo_objective}', json.dumps(objective))
                .replace('${initiatives}', json.dumps(linked_initiatives)))

        with open(os.path.join(docs_folder, 'landing_pages', objective['id'] + '.html'), 'w') as html_file:
            html_file.write(page)

    for initiative in initiatives_payload.get('items', []):
        page = (initiative_template
                .replace('${initiative}', json.dumps(initiative))
                .replace('${domain_name}', domain['name']))
        landing_page_id = initiative.get('landingPageId') or ('initiative-' + initiative.get('initiativeId', 'item'))
        with open(os.path.join(docs_folder, 'landing_pages', landing_page_id + '.html'), 'w') as html_file:
            html_file.write(page)


for domain in config['domains']:
    ktlo_file_path = domains_root + domain['id'] + '/ktlo/ktlo.json'
    initiatives_file_path = domains_root + domain['id'] + '/ktlo/initiatives.json'

    if not os.path.exists(ktlo_file_path):
        continue

    ktlo_payload = json.load(open(ktlo_file_path))
    initiatives_payload = {"items": []}
    if os.path.exists(initiatives_file_path):
        initiatives_payload = json.load(open(initiatives_file_path))
    for initiative in initiatives_payload.get('items', []):
        if initiative.get('initiativeId'):
            initiative['landingPageId'] = 'initiative-' + initiative['initiativeId']

    docs_folder = domain['id'] + '/ktlo/'
    create_overview_docs(domain, docs_folder, ktlo_payload, initiatives_payload)
    create_landing_pages(domain, docs_folder, ktlo_payload, initiatives_payload)
