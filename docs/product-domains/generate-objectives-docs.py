import copy
import datetime
import json
import os
import shutil

from initiatives_support import enrich_discoveries, load_domain_activity


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


def build_activity_lookup(delivery_path):
    if not os.path.exists(delivery_path):
        return {}

    items = json.load(open(delivery_path)).get('items', [])
    sorted_items = sorted(enumerate(items), key=lambda item: item[1].get('date', ''), reverse=True)
    item_map = {}

    for landing_index, (source_index, item) in enumerate(sorted_items):
        lookup_item = {
            'landingPageIndex': landing_index,
            'title': item.get('title') or item.get('name'),
            'name': item.get('name') or item.get('title'),
            'description': item.get('description', ''),
            'id': item.get('initiativeId') or item.get('releaseId') or item.get('id')
        }
        lookup_keys = [
            f"{item.get('date', '')}|{item.get('title', '').strip()}",
            f"{item.get('date', '')}|{item.get('name', '').strip()}",
            f"{item.get('date', '')}|{item.get('description', '').strip()}"
        ]
        for key in lookup_keys:
            if key != f"{item.get('date', '')}|":
                item_map[key] = lookup_item
        item_map[str(source_index)] = lookup_item

    return item_map


def enrich_activity_links(items, activity_lookup, id_field):
    enriched_items = []
    for item in items:
        enriched = dict(item)
        key = f"{item.get('date', '')}|{item.get('description', '')}"
        activity_info = activity_lookup.get(key, {})
        if activity_info.get('landingPageIndex') is not None:
            enriched['landingPageIndex'] = activity_info.get('landingPageIndex')
        if activity_info.get('title') and not enriched.get('title'):
            enriched['title'] = activity_info.get('title')
        if activity_info.get('name') and not enriched.get('name'):
            enriched['name'] = activity_info.get('name')
        if activity_info.get('id') and not enriched.get(id_field):
            enriched[id_field] = activity_info.get('id')
        enriched_items.append(enriched)
    return enriched_items


def enrich_source_objective_links(source_objective, initiative_lookup, release_lookup):
    enriched_objective = copy.deepcopy(source_objective)
    enriched_objective['linkedInitiatives'] = enrich_activity_links(
        source_objective.get('linkedInitiatives', []),
        initiative_lookup,
        'initiativeId'
    )
    enriched_objective['linkedReleases'] = enrich_activity_links(
        source_objective.get('linkedReleases', []),
        release_lookup,
        'releaseId'
    )
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


def merge_insights(items):
    lookup = {}
    for item in items or []:
        key = item.get('insightId') or item.get('id') or item.get('insightTitle') or item.get('title')
        if key and key not in lookup:
            lookup[key] = dict(item)
    return list(lookup.values())


def source_objective_page_id(source_objective):
    return source_objective['id']


def company_objective_page_id(company_objective, payload):
    quarter = payload.get('quarter') or payload.get('timeframe', 'period')
    safe_quarter = quarter.lower().replace(' ', '-')
    return f"{safe_quarter}-{company_objective['id']}"


def prepare_payload(payload, initiative_lookup, release_lookup, discovery_lookup, enriched_initiatives=None, enriched_releases=None):
    prepared = copy.deepcopy(payload)
    prepared['objectives'] = [
        enrich_source_objective_links(item, initiative_lookup, release_lookup)
        for item in objective_items(prepared)
    ]

    company_lookup = {}
    for company_objective in company_objective_items(prepared):
        company_objective['landingPageId'] = company_objective_page_id(company_objective, prepared)
        company_objective['inspiredByInsights'] = enrich_insights(company_objective.get('inspiredByInsights', []), discovery_lookup)
        company_objective['sourceObjectiveRefs'] = []
        company_objective['linkedInitiatives'] = []
        company_objective['linkedReleases'] = []
        company_objective['keyResultsCount'] = 0
        company_objective['highIntegrityCommitmentCount'] = 0
        company_lookup[company_objective['id']] = company_objective

    objective_lookup = {}
    for source_objective in prepared['objectives']:
        source_objective['landingPageId'] = source_objective_page_id(source_objective)
        source_objective['inspiredByInsights'] = enrich_insights(source_objective.get('inspiredByInsights', []), discovery_lookup)
        enriched_key_results = []
        for key_result in source_objective.get('keyResults', []):
            enriched_key_result = dict(key_result)
            enriched_key_results.append(enriched_key_result)
        source_objective['keyResults'] = enriched_key_results
        objective_lookup[source_objective['id']] = {
            'pageId': source_objective['landingPageId'],
            'title': source_objective.get('title', 'Objective'),
            'linkedInitiatives': source_objective.get('linkedInitiatives', []),
            'linkedReleases': source_objective.get('linkedReleases', []),
            'keyResultsCount': len(source_objective.get('keyResults', [])),
            'highIntegrityCommitmentCount': len([
                item for item in source_objective.get('keyResults', [])
                if item.get('commitmentType') == 'high_integrity_commitment'
            ])
        }

    for company_objective in company_objective_items(prepared):
        initiative_map = {}
        release_map = {}
        source_refs = []
        for source_objective in prepared['objectives']:
            if company_objective.get('id') not in source_objective.get('companyObjectiveIds', []):
                continue
            source_refs.append({
                'id': source_objective.get('id'),
                'title': source_objective.get('title'),
                'landingPageId': source_objective.get('landingPageId'),
                'quarter': (source_objective.get('period') or {}).get('quarter'),
                'keyResultsCount': len(source_objective.get('keyResults', [])),
                'highIntegrityCommitmentCount': len([
                    item for item in source_objective.get('keyResults', [])
                    if item.get('commitmentType') == 'high_integrity_commitment'
                ])
            })
            company_objective['keyResultsCount'] += len(source_objective.get('keyResults', []))
            company_objective['highIntegrityCommitmentCount'] += len([
                item for item in source_objective.get('keyResults', [])
                if item.get('commitmentType') == 'high_integrity_commitment'
            ])
            for item in source_objective.get('linkedInitiatives', []):
                key = item.get('initiativeId') or item.get('id') or f"{item.get('date', '')}|{item.get('description', '')}"
                initiative_map[key] = dict(item)
            for item in source_objective.get('linkedReleases', []):
                key = item.get('releaseId') or item.get('id') or f"{item.get('date', '')}|{item.get('description', '')}"
                release_map[key] = dict(item)
        company_objective['sourceObjectiveRefs'] = sorted(
            source_refs,
            key=lambda item: (item.get('quarter', ''), item.get('title', ''))
        )
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

    # Attach full enriched initiative/release items to each objective
    enriched_init_list = enriched_initiatives.get('items', []) if enriched_initiatives else []
    enriched_rel_list = enriched_releases.get('items', []) if enriched_releases else []

    # Build lookup: landingPageIndex -> full enriched item
    init_by_index = {item.get('landingPageIndex'): item for item in enriched_init_list}
    rel_by_index = {item.get('landingPageIndex'): item for item in enriched_rel_list}

    for source_objective in prepared['objectives']:
        enriched_inits = []
        objective_prefix = (source_objective.get('id') or '') + '/'
        matched_by_kr = [
            item for item in enriched_init_list
            if (item.get('keyResultId') or '').startswith(objective_prefix)
        ]
        seen_init_keys = set()
        for item in matched_by_kr:
            key = item.get('initiativeId') or item.get('title') or json.dumps(item, sort_keys=True)
            if key not in seen_init_keys:
                enriched_inits.append(item)
                seen_init_keys.add(key)
        for linked in source_objective.get('linkedInitiatives', []):
            idx = linked.get('landingPageIndex')
            if idx is not None and idx in init_by_index:
                item = init_by_index[idx]
                key = item.get('initiativeId') or item.get('title') or json.dumps(item, sort_keys=True)
                if key not in seen_init_keys:
                    enriched_inits.append(item)
                    seen_init_keys.add(key)
        source_objective['enrichedInitiatives'] = enriched_inits

        enriched_rels = []
        linked_init_ids = {
            item.get('initiativeId')
            for item in enriched_inits
            if item.get('initiativeId')
        }
        matched_releases = [
            item for item in enriched_rel_list
            if item.get('initiativeId') in linked_init_ids
        ]
        seen_release_keys = set()
        for item in matched_releases:
            key = item.get('releaseId') or item.get('title') or json.dumps(item, sort_keys=True)
            if key not in seen_release_keys:
                enriched_rels.append(item)
                seen_release_keys.add(key)
        for linked in source_objective.get('linkedReleases', []):
            idx = linked.get('landingPageIndex')
            if idx is not None and idx in rel_by_index:
                item = rel_by_index[idx]
                key = item.get('releaseId') or item.get('title') or json.dumps(item, sort_keys=True)
                if key not in seen_release_keys:
                    enriched_rels.append(item)
                    seen_release_keys.add(key)
        source_objective['enrichedReleases'] = enriched_rels

    for company_objective in company_objective_items(prepared):
        enriched_inits = []
        for linked in company_objective.get('linkedInitiatives', []):
            idx = linked.get('landingPageIndex')
            if idx is not None and idx in init_by_index:
                enriched_inits.append(init_by_index[idx])
        company_objective['enrichedInitiatives'] = enriched_inits

        enriched_rels = []
        for linked in company_objective.get('linkedReleases', []):
            idx = linked.get('landingPageIndex')
            if idx is not None and idx in rel_by_index:
                enriched_rels.append(rel_by_index[idx])
        company_objective['enrichedReleases'] = enriched_rels

    return prepared


def create_period_docs(domain, docs_folder, period, period_label, payload, period_links):
    os.makedirs(os.path.join(docs_folder, 'icons'), exist_ok=True)

    copy_icons(templates_root + 'icons', docs_folder)

    with open(os.path.join(docs_folder, 'index.html'), 'w') as html_file:
        template = open(templates_root + 'index.html').read()
        html_file.write(template
                        .replace('${date}', date_string)
                        .replace('${domain_name}', domain['name'])
                        .replace('${domain_description}', domain['description'])
                        .replace('${period}', period)
                        .replace('${period_label}', period_label)
                        .replace('${payload}', json.dumps(payload))
                        .replace('${current_href}', period_links['current'])
                        .replace('${next_href}', period_links['next'])
                        .replace('${archived_href}', period_links['archived'])
                        .replace('${ktlo_href}', period_links['ktlo']))


def create_root_redirect(docs_folder):
    with open(os.path.join(docs_folder, 'index.html'), 'w') as html_file:
        html_file.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="refresh" content="0; url=current/index.html">
    <title>Objectives</title>
</head>
<body>
    <p><a href="current/index.html">Open current objectives</a></p>
</body>
</html>
""")


def create_landing_pages(docs_folder, payload, domain):
    os.makedirs(os.path.join(docs_folder, 'landing_pages'), exist_ok=True)
    template = open(templates_root + 'landing_page.html').read()

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
    current_path = objectives_root + 'current/objectives.json'
    next_path = objectives_root + 'next/objectives.json'
    archive_path = objectives_root + 'archived/objectives.json'
    ktlo_path = objectives_root + 'ktlo/objectives.json'

    if not os.path.exists(current_path):
        continue

    current_payload = json.load(open(current_path))
    next_payload = json.load(open(next_path)) if os.path.exists(next_path) else {'objectives': [], 'companyObjectives': []}
    archive_payload = json.load(open(archive_path)) if os.path.exists(archive_path) else {'objectives': [], 'companyObjectives': []}
    ktlo_payload = json.load(open(ktlo_path)) if os.path.exists(ktlo_path) else {'objectives': [], 'companyObjectives': []}
    initiative_lookup = build_activity_lookup(objectives_root + 'current/initiatives.json')
    initiative_lookup.update(build_activity_lookup(objectives_root + 'next/initiatives.json'))
    initiative_lookup.update(build_activity_lookup(objectives_root + 'archived/initiatives.json'))
    initiative_lookup.update(build_activity_lookup(objectives_root + 'ktlo/initiatives.json'))
    release_lookup = build_activity_lookup(domains_root + domain_id + '/delivery/releases.json')
    ongoing_discoveries_path = objectives_root + 'current/discoveries.json'
    next_discoveries_path = objectives_root + 'next/discoveries.json'
    archived_discoveries_path = objectives_root + 'archived/discoveries.json'
    ongoing_discoveries = {'items': []}
    if os.path.exists(ongoing_discoveries_path):
        ongoing_discoveries['items'].extend(json.load(open(ongoing_discoveries_path)).get('items', []))
    if os.path.exists(next_discoveries_path):
        ongoing_discoveries['items'].extend(json.load(open(next_discoveries_path)).get('items', []))
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

    # Load full enriched initiatives and releases for embedding in landing pages
    domain_activity = load_domain_activity(domains_root, domain_id)
    enriched_initiatives = domain_activity.get('initiatives', {'items': []})
    enriched_releases = domain_activity.get('releases', {'items': []})

    current_payload = prepare_payload(current_payload, initiative_lookup, release_lookup, discovery_lookup, enriched_initiatives, enriched_releases)
    next_payload = prepare_payload(next_payload, initiative_lookup, release_lookup, discovery_lookup, enriched_initiatives, enriched_releases)
    archive_payload = prepare_payload(archive_payload, initiative_lookup, release_lookup, discovery_lookup, enriched_initiatives, enriched_releases)
    ktlo_payload = prepare_payload(ktlo_payload, initiative_lookup, release_lookup, discovery_lookup, enriched_initiatives, enriched_releases)

    docs_folder = domain_id + '/objectives/'
    if os.path.exists(docs_folder):
        shutil.rmtree(docs_folder)
    os.makedirs(docs_folder, exist_ok=True)
    create_root_redirect(docs_folder)

    create_period_docs(
        domain,
        os.path.join(docs_folder, 'current'),
        'current',
        'Current',
        current_payload,
        {'current': '../current/index.html', 'next': '../next/index.html', 'archived': '../archived/index.html', 'ktlo': '../ktlo/index.html'}
    )
    create_period_docs(
        domain,
        os.path.join(docs_folder, 'next'),
        'next',
        'Next',
        next_payload,
        {'current': '../current/index.html', 'next': '../next/index.html', 'archived': '../archived/index.html', 'ktlo': '../ktlo/index.html'}
    )
    create_period_docs(
        domain,
        os.path.join(docs_folder, 'archived'),
        'archived',
        'Archived',
        archive_payload,
        {'current': '../current/index.html', 'next': '../next/index.html', 'archived': '../archived/index.html', 'ktlo': '../ktlo/index.html'}
    )
    create_period_docs(
        domain,
        os.path.join(docs_folder, 'ktlo'),
        'ktlo',
        'KTLO',
        ktlo_payload,
        {'current': '../current/index.html', 'next': '../next/index.html', 'archived': '../archived/index.html', 'ktlo': '../ktlo/index.html'}
    )
    create_landing_pages(os.path.join(docs_folder, 'current'), current_payload, domain)
    create_landing_pages(os.path.join(docs_folder, 'next'), next_payload, domain)
    create_landing_pages(os.path.join(docs_folder, 'archived'), archive_payload, domain)
    create_landing_pages(os.path.join(docs_folder, 'ktlo'), ktlo_payload, domain)
