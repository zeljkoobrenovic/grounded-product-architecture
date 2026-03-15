import json
import os
import shutil
import datetime


date_string = datetime.date.today().strftime('%Y-%m-%d')

domains_root = '../../_config/product-domains/'
templates_root = '../../_templates/goals/'

config = json.load(open(domains_root + 'config.json'))


def copy_icons(icons_path, docs_folder):
    if os.path.exists(icons_path):
        for filename in os.listdir(icons_path):
            src = os.path.join(icons_path, filename)
            dst = os.path.join(docs_folder, 'icons', filename)
            if os.path.isfile(src):
                shutil.copy2(src, dst)


def create_overview_docs(domain, docs_folder, current_goals, next_goals, archive_goals):
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
                        .replace('${current_goals}', json.dumps(current_goals))
                        .replace('${next_goals}', json.dumps(next_goals))
                        .replace('${archive_goals}', json.dumps(archive_goals)))


def flatten_goals(*payloads):
    result = []
    for payload in payloads:
        for goal in payload.get('goals', []):
            result.append(goal)
    return result


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


def enrich_goal_links(goal, initiative_index_map, release_index_map):
    enriched_goal = dict(goal)
    enriched_initiatives = []
    enriched_releases = []

    for item in goal.get('linkedInitiatives', []):
        enriched = dict(item)
        key = f"{item.get('date', '')}|{item.get('description', '')}"
        enriched['landingPageIndex'] = initiative_index_map.get(key)
        enriched_initiatives.append(enriched)

    for item in goal.get('linkedReleases', []):
        enriched = dict(item)
        key = f"{item.get('date', '')}|{item.get('description', '')}"
        enriched['landingPageIndex'] = release_index_map.get(key)
        enriched_releases.append(enriched)

    enriched_goal['linkedInitiatives'] = enriched_initiatives
    enriched_goal['linkedReleases'] = enriched_releases
    return enriched_goal


def create_landing_pages(docs_folder, goals, domain):
    os.makedirs(os.path.join(docs_folder, 'landing_pages'), exist_ok=True)
    template = open(templates_root + 'landing_page.html').read()

    for goal in goals:
        landing_page_file = os.path.join(docs_folder, 'landing_pages', str(goal['id']) + '.html')
        with open(landing_page_file, 'w') as html_file:
            html_file.write(template
                            .replace('${date}', date_string)
                            .replace('${domain_name}', domain['name'])
                            .replace('${goal_title}', goal.get('title', 'Goal'))
                            .replace('${goal}', json.dumps(goal)))


for domain in config['domains']:
    domain_id = domain['id']
    goals_root = domains_root + domain_id + '/goals/'
    current_path = goals_root + 'current.json'
    next_path = goals_root + 'next.json'
    archive_path = goals_root + 'archive.json'

    if not os.path.exists(current_path):
        continue

    current_goals = json.load(open(current_path))
    next_goals = json.load(open(next_path)) if os.path.exists(next_path) else {'goals': []}
    archive_goals = json.load(open(archive_path)) if os.path.exists(archive_path) else {'goals': []}
    initiative_index_map = build_activity_index(domains_root + domain_id + '/delivery/initiatives.json')
    release_index_map = build_activity_index(domains_root + domain_id + '/delivery/releases.json')

    current_goals['goals'] = [enrich_goal_links(goal, initiative_index_map, release_index_map) for goal in current_goals.get('goals', [])]
    next_goals['goals'] = [enrich_goal_links(goal, initiative_index_map, release_index_map) for goal in next_goals.get('goals', [])]
    archive_goals['goals'] = [enrich_goal_links(goal, initiative_index_map, release_index_map) for goal in archive_goals.get('goals', [])]

    docs_folder = domain_id + '/goals/'
    create_overview_docs(domain, docs_folder, current_goals, next_goals, archive_goals)
    create_landing_pages(docs_folder, flatten_goals(current_goals, next_goals, archive_goals), domain)
