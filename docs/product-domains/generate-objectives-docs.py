import copy
import datetime
import json
import os
import shutil

from initiatives_support import enrich_discoveries


date_string = datetime.date.today().strftime('%Y-%m-%d')

domains_root = '../../_config/product-domains/'
templates_root = '../../_templates/objectives/'

config = json.load(open(domains_root + 'config.json'))


def copy_icons(icons_path, docs_folder):
    if os.path.exists(icons_path):
        for filename in os.listdir(icons_path):
            src = os.path.join(icons_path, filename)
            dst = os.path.join(docs_folder, 'icons', filename)
            if os.path.isfile(src):
                shutil.copy2(src, dst)


def objective_items(payload):
    return payload.get('objectives', payload.get('goals', []))


def company_objective_items(payload):
    return payload.get('companyObjectives', [])


def build_activity_index(delivery_path):
    if not os.path.exists(delivery_path):
        return {}

    items = json.load(open(delivery_path)).get('items', [])
    sorted_items = sorted(enumerate(items), key=lambda item: item[1].get('date', ''), reverse=True)
    index_map = {}

    for landing_index, (source_index, item) in enumerate(sorted_items):
        key = f"{item.get('date', '')}|{item.get('title') or item.get('name') or item.get('description', '').strip()}"
        index_map[key] = landing_index
        index_map[str(source_index)] = landing_index

    return index_map


def enrich_source_objective_links(source_objective, initiative_index_map, release_index_map):
    enriched_objective = copy.deepcopy(source_objective)
    enriched_initiatives = []
    enriched_releases = []

    for item in source_objective.get('linkedInitiatives', []):
        enriched = dict(item)
        key = f"{item.get('date', '')}|{item.get('description', '')}"
        enriched['landingPageIndex'] = initiative_index_map.get(key)
        enriched_initiatives.append(enriched)

    for item in source_objective.get('linkedReleases', []):
        enriched = dict(item)
        key = f"{item.get('date', '')}|{item.get('description', '')}"
        enriched['landingPageIndex'] = release_index_map.get(key)
        enriched_releases.append(enriched)

    enriched_objective['linkedInitiatives'] = enriched_initiatives
    enriched_objective['linkedReleases'] = enriched_releases
    return enriched_objective


def enrich_insights(items, discovery_lookup):
    enriched_items = []
    for item in items or []:
        enriched_item = dict(item)
        discovery_info = discovery_lookup.get(item.get('insightId', '') or item.get('id', ''), {})
        if discovery_info.get('landingPageIndex') is not None:
            enriched_item['landingPageIndex'] = discovery_info.get('landingPageIndex')
        if discovery_info.get('name') and not enriched_item.get('insightTitle'):
            enriched_item['insightTitle'] = discovery_info.get('name')
        if discovery_info.get('status') and not enriched_item.get('status'):
            enriched_item['status'] = discovery_info.get('status')
        enriched_items.append(enriched_item)
    return enriched_items


def source_objective_page_id(source_objective):
    return source_objective['id']


def company_objective_page_id(company_objective, payload):
    quarter = payload.get('quarter') or payload.get('timeframe', 'period')
    safe_quarter = quarter.lower().replace(' ', '-')
    return f"{safe_quarter}-{company_objective['id']}"


def prepare_payload(payload, initiative_index_map, release_index_map, discovery_lookup):
    prepared = copy.deepcopy(payload)
    prepared['objectives'] = [
        enrich_source_objective_links(item, initiative_index_map, release_index_map)
        for item in objective_items(prepared)
    ]

    objective_lookup = {}
    for source_objective in prepared['objectives']:
        source_objective['landingPageId'] = source_objective_page_id(source_objective)
        source_objective['inspiredByInsights'] = enrich_insights(source_objective.get('inspiredByInsights', []), discovery_lookup)
        objective_lookup[source_objective['id']] = {
            'pageId': source_objective['landingPageId'],
            'title': source_objective.get('title', 'Objective'),
            'linkedInitiatives': source_objective.get('linkedInitiatives', []),
            'linkedReleases': source_objective.get('linkedReleases', [])
        }

    for company_objective in company_objective_items(prepared):
        company_objective['landingPageId'] = company_objective_page_id(company_objective, prepared)
        company_objective['inspiredByInsights'] = enrich_insights(company_objective.get('inspiredByInsights', []), discovery_lookup)
        initiative_map = {}
        release_map = {}
        for key_result in company_objective.get('keyResults', []):
            key_result['inspiredByInsights'] = enrich_insights(key_result.get('inspiredByInsights', []), discovery_lookup)
            source_id = key_result.get('sourceObjectiveId')
            if source_id in objective_lookup:
                key_result['sourceObjectivePageId'] = objective_lookup[source_id]['pageId']
                for item in objective_lookup[source_id]['linkedInitiatives']:
                    key = item.get('id') or f"{item.get('date', '')}|{item.get('description', '')}"
                    initiative_map[key] = dict(item)
                for item in objective_lookup[source_id]['linkedReleases']:
                    key = item.get('id') or f"{item.get('date', '')}|{item.get('description', '')}"
                    release_map[key] = dict(item)
        company_objective['linkedInitiatives'] = sorted(
            initiative_map.values(),
            key=lambda item: item.get('date', ''),
            reverse=True
        )
        company_objective['linkedReleases'] = sorted(
            release_map.values(),
            key=lambda item: item.get('date', ''),
            reverse=True
        )

    for source_objective in prepared['objectives']:
        source_objective['companyObjectiveRefs'] = []
        for company_id in source_objective.get('companyObjectiveIds', []):
            for company_objective in company_objective_items(prepared):
                if company_objective.get('id') == company_id:
                    source_objective['companyObjectiveRefs'].append({
                        'id': company_id,
                        'title': company_objective.get('title'),
                        'landingPageId': company_objective.get('landingPageId')
                    })

    return prepared


def create_overview_docs(domain, docs_folder, current_payload, next_payload, archive_payload):
    if os.path.exists(docs_folder):
        shutil.rmtree(docs_folder)
    os.makedirs(os.path.join(docs_folder, 'icons'), exist_ok=True)

    copy_icons(templates_root + 'icons', docs_folder)

    with open(os.path.join(docs_folder, 'index.html'), 'w') as html_file:
        template = open(templates_root + 'index.html').read()
        html_file.write(template
                        .replace('${date}', date_string)
                        .replace('${domain_name}', domain['name'])
                        .replace('${domain_description}', domain['description'])
                        .replace('${current_payload}', json.dumps(current_payload))
                        .replace('${next_payload}', json.dumps(next_payload))
                        .replace('${archive_payload}', json.dumps(archive_payload)))


def create_landing_pages(docs_folder, payloads, domain):
    os.makedirs(os.path.join(docs_folder, 'landing_pages'), exist_ok=True)
    template = open(templates_root + 'landing_page.html').read()

    for payload in payloads:
        for source_objective in objective_items(payload):
            landing_page_file = os.path.join(docs_folder, 'landing_pages', source_objective['landingPageId'] + '.html')
            with open(landing_page_file, 'w') as html_file:
                html_file.write(template
                                .replace('${date}', date_string)
                                .replace('${domain_name}', domain['name'])
                                .replace('${page_title}', source_objective.get('title', 'Objective'))
                                .replace('${page_kind}', 'source-objective')
                                .replace('${page_payload}', json.dumps(source_objective)))

        for company_objective in company_objective_items(payload):
            landing_page_file = os.path.join(docs_folder, 'landing_pages', company_objective['landingPageId'] + '.html')
            with open(landing_page_file, 'w') as html_file:
                html_file.write(template
                                .replace('${date}', date_string)
                                .replace('${domain_name}', domain['name'])
                                .replace('${page_title}', company_objective.get('title', 'Company Objective'))
                                .replace('${page_kind}', 'company-objective')
                                .replace('${page_payload}', json.dumps(company_objective)))


for domain in config['domains']:
    domain_id = domain['id']
    objectives_root = domains_root + domain_id + '/objectives/'
    current_path = objectives_root + 'current.json'
    next_path = objectives_root + 'next.json'
    archive_path = objectives_root + 'archive.json'

    if not os.path.exists(current_path):
        continue

    current_payload = json.load(open(current_path))
    next_payload = json.load(open(next_path)) if os.path.exists(next_path) else {'objectives': [], 'companyObjectives': []}
    archive_payload = json.load(open(archive_path)) if os.path.exists(archive_path) else {'objectives': [], 'companyObjectives': []}
    initiative_index_map = build_activity_index(domains_root + domain_id + '/delivery/initiatives.json')
    release_index_map = build_activity_index(domains_root + domain_id + '/delivery/releases.json')
    ongoing_discoveries_path = domains_root + domain_id + '/discoveries/ongoing.json'
    archived_discoveries_path = domains_root + domain_id + '/discoveries/archived.json'
    ongoing_discoveries = json.load(open(ongoing_discoveries_path)) if os.path.exists(ongoing_discoveries_path) else {'items': []}
    archived_discoveries = json.load(open(archived_discoveries_path)) if os.path.exists(archived_discoveries_path) else {'items': []}
    discoveries_enriched = enrich_discoveries(ongoing_discoveries, archived_discoveries, {})
    discovery_lookup = {
        item.get('id', ''): {
            'landingPageIndex': item.get('landingPageIndex'),
            'name': item.get('name', ''),
            'status': item.get('status', '')
        }
        for item in discoveries_enriched.get('items', [])
        if item.get('id')
    }

    current_payload = prepare_payload(current_payload, initiative_index_map, release_index_map, discovery_lookup)
    next_payload = prepare_payload(next_payload, initiative_index_map, release_index_map, discovery_lookup)
    archive_payload = prepare_payload(archive_payload, initiative_index_map, release_index_map, discovery_lookup)

    docs_folder = domain_id + '/objectives/'
    create_overview_docs(domain, docs_folder, current_payload, next_payload, archive_payload)
    create_landing_pages(docs_folder, [current_payload, next_payload, archive_payload], domain)
