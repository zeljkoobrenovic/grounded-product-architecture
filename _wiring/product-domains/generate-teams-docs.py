import datetime
import json
import os
import shutil
from domain_cli import load_domain_args

from initiatives_support import (
    build_bricks_lookup,
    build_customers_lookup,
    load_domain_activity,
)
from product_bricks_support import load_product_bricks_payload

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
os.chdir(os.path.join(REPO_ROOT, 'docs', 'product-domains'))

date_string = datetime.date.today().strftime('%Y-%m-%d')

domains_root = '../../_config/product-domains/'
templates_root = '../../_templates/teams/'
domain, _ = load_domain_args()
common_style = open(templates_root + '../_imports/common/style.html').read()
tabs_style = open(templates_root + '../_imports/tabs/style.html').read()
tabs_script = open(templates_root + '../_imports/tabs/script.html').read()
breadcrumbs_style = open(templates_root + '../_imports/breadcrumbs/style.html').read()
breadcrumbs_script = open(templates_root + '../_imports/breadcrumbs/script.html').read()


def render_breadcrumbs(template_name, replacements):
    breadcrumbs = open(os.path.join(templates_root, template_name)).read()
    for key, value in replacements.items():
        breadcrumbs = breadcrumbs.replace('${' + key + '}', value)
    return breadcrumbs


def copy_icons(icons_path, docs_folder):
    if os.path.exists(icons_path):
        for filename in os.listdir(icons_path):
            src = os.path.join(icons_path, filename)
            dst = os.path.join(docs_folder, 'icons', filename)
            if os.path.isfile(src):
                shutil.copy2(src, dst)


def load_json_if_exists(path, default):
    if os.path.exists(path):
        return json.load(open(path))
    return default


def normalize_icon_name(icon_name):
    value = icon_name or 'customer.png'
    while value.endswith('.png.png'):
        value = value[:-4]
    while value.endswith('.svg.png'):
        value = value[:-4]
    if '.' in value:
        return value
    return value + '.png'


def build_team_lookup(teams_payload):
    lookup = {}
    for group in teams_payload.get('groups', []):
        for team in group.get('teams', []):
            lookup[team['id']] = {
                'id': team['id'],
                'name': team.get('name', team['id']),
                'teamType': team.get('teamType', ''),
                'groupId': group.get('id', ''),
                'groupName': group.get('name', '')
            }
    return lookup


def find_related_items(items, team_id, section_folder):
    related = []
    for item in items.get('items', []):
        teams = item.get('teams', {})
        primary = teams.get('primaryTeamIds', [])
        supporting = teams.get('supportingTeamIds', [])
        if team_id in primary or team_id in supporting:
            related.append({
                'date': item.get('date', ''),
                'description': item.get('description', ''),
                'landingPageKey': str(item.get('landingPageIndex', 0)),
                'sectionFolder': section_folder,
                'teamRole': 'primary' if team_id in primary else 'supporting',
                'teamRoleLabel': 'Primary team' if team_id in primary else 'Supporting team'
            })
    return related


def find_related_discoveries(discoveries, team_id):
    related = []
    for item in discoveries.get('items', []):
        assignments = ((item.get('teams') or {}).get('assignments') or [])
        for assignment in assignments:
            if assignment.get('teamId') == team_id:
                related.append({
                    'date': (item.get('startDate', '') + ' -> ' + item.get('endDate', '')).strip(),
                    'description': item.get('name', ''),
                    'landingPageKey': str(item.get('landingPageIndex', 0)),
                    'sectionFolder': 'discoveries',
                    'teamRole': assignment.get('role', ''),
                    'teamRoleLabel': assignment.get('roleLabel', assignment.get('role', '')),
                    'how': assignment.get('how', '')
                })
                break
    return related


def enrich_team(team, team_lookup, customers_lookup, bricks_lookup, initiatives, releases, group):
    enriched = dict(team)
    enriched['groupId'] = group.get('id', '')
    enriched['groupName'] = group.get('name', '')
    enriched['groupLeadership'] = group.get('groupLeadership', {})

    enriched_customers = []
    for customer in team.get('primaryCustomers', []):
        info = customers_lookup.get(customer.get('customerId', ''), {
            'icon': 'customer.png',
            'name': customer.get('customerName', customer.get('customerId', ''))
        })
        enriched_customers.append({
            'customerId': customer.get('customerId', ''),
            'customerName': customer.get('customerName', info.get('name', customer.get('customerId', ''))),
            'relatedKPIs': customer.get('relatedKPIs', []),
            'icon': normalize_icon_name(info.get('icon', 'customer.png'))
        })

    def enrich_bricks(bricks):
        result = []
        for brick in bricks:
            brick_id = str(brick.get('brickId', ''))
            info = bricks_lookup.get(brick_id, {
                'id': brick_id,
                'name': brick.get('brickName', brick_id),
                'domain': '',
                'group': '',
                'icon': 'capability_404.png'
            })
            result.append({
                'brickId': brick_id,
                'brickName': brick.get('brickName', info.get('name', brick_id)),
                'brick': info
            })
        return result

    enriched['primaryCustomers'] = enriched_customers
    enriched['ownedProductBricks'] = enrich_bricks(team.get('ownedProductBricks', []))
    enriched['supportingProductBricks'] = enrich_bricks(team.get('supportingProductBricks', []))
    enriched['dependsOnTeams'] = [team_lookup[team_id] for team_id in team.get('dependsOnTeamIds', []) if team_id in team_lookup]
    enriched['defaultSupportingTeams'] = [team_lookup[team_id] for team_id in team.get('defaultSupportingTeamIds', []) if team_id in team_lookup]
    enriched['relatedInitiatives'] = find_related_items(initiatives, team['id'], 'initiatives')
    enriched['relatedReleases'] = find_related_items(releases, team['id'], 'releases')
    return enriched


def add_dependency_data(enriched_payload):
    teams = []
    for group in enriched_payload.get('groups', []):
        for team in group.get('teams', []):
            teams.append(team)

    def brick_ids(team):
        ids = set()
        for brick in team.get('ownedProductBricks', []):
            ids.add(str(brick.get('brickId', '')))
        for brick in team.get('supportingProductBricks', []):
            ids.add(str(brick.get('brickId', '')))
        return ids

    def brick_name_map(team):
        names = {}
        for brick in team.get('ownedProductBricks', []) + team.get('supportingProductBricks', []):
            brick_id = str(brick.get('brickId', ''))
            brick_name = brick.get('brickName') or ((brick.get('brick') or {}).get('name')) or brick_id
            names[brick_id] = brick_name
        return names

    def item_keys(items):
        return {str(item.get('landingPageKey', '')) for item in items if item.get('landingPageKey') is not None}

    def item_lookup(items):
        lookup = {}
        for item in items:
            key = str(item.get('landingPageKey', ''))
            if key:
                lookup[key] = {
                    'landingPageKey': key,
                    'sectionFolder': item.get('sectionFolder', ''),
                    'description': item.get('description', ''),
                    'date': item.get('date', '')
                }
        return lookup

    for team in teams:
        current_brick_ids = brick_ids(team)
        current_brick_names = brick_name_map(team)
        current_initiatives = item_keys(team.get('relatedInitiatives', []))
        current_releases = item_keys(team.get('relatedReleases', []))
        current_initiative_lookup = item_lookup(team.get('relatedInitiatives', []))
        current_release_lookup = item_lookup(team.get('relatedReleases', []))

        shared_bricks = []
        shared_initiatives = []
        shared_releases = []

        for other in teams:
            if other.get('id') == team.get('id'):
                continue

            overlap_bricks = sorted(current_brick_ids.intersection(brick_ids(other)))
            if overlap_bricks:
                shared_bricks.append({
                    'teamId': other.get('id', ''),
                    'teamName': other.get('name', other.get('id', '')),
                    'sharedBrickIds': overlap_bricks,
                    'sharedBrickNames': [current_brick_names.get(brick_id, brick_id) for brick_id in overlap_bricks]
                })

            overlap_initiatives = sorted(current_initiatives.intersection(item_keys(other.get('relatedInitiatives', []))))
            if overlap_initiatives:
                shared_initiatives.append({
                    'teamId': other.get('id', ''),
                    'teamName': other.get('name', other.get('id', '')),
                    'sharedInitiativeKeys': overlap_initiatives,
                    'sharedInitiatives': [
                        current_initiative_lookup.get(key, {
                            'landingPageKey': key,
                            'sectionFolder': 'initiatives',
                            'description': key,
                            'date': ''
                        })
                        for key in overlap_initiatives
                    ]
                })

            overlap_releases = sorted(current_releases.intersection(item_keys(other.get('relatedReleases', []))))
            if overlap_releases:
                shared_releases.append({
                    'teamId': other.get('id', ''),
                    'teamName': other.get('name', other.get('id', '')),
                    'sharedReleaseKeys': overlap_releases,
                    'sharedReleases': [
                        current_release_lookup.get(key, {
                            'landingPageKey': key,
                            'sectionFolder': 'releases',
                            'description': key,
                            'date': ''
                        })
                        for key in overlap_releases
                    ]
                })

        explicit_relationships = []
        for other in team.get('dependsOnTeams', []):
            explicit_relationships.append({
                'teamId': other.get('id', ''),
                'teamName': other.get('name', other.get('id', '')),
                'relationshipType': 'depends_on',
                'relationshipLabel': 'depends on'
            })
        for other in team.get('defaultSupportingTeams', []):
            explicit_relationships.append({
                'teamId': other.get('id', ''),
                'teamName': other.get('name', other.get('id', '')),
                'relationshipType': 'supported_by',
                'relationshipLabel': 'supported by'
            })

        team['dependencyData'] = {
            'sharedProductBricks': shared_bricks,
            'sharedInitiatives': shared_initiatives,
            'sharedReleases': shared_releases,
            'explicitRelationships': explicit_relationships
        }


def create_overview_docs(domain, docs_folder, teams_payload):
    if os.path.exists(docs_folder):
        shutil.rmtree(docs_folder)

    os.makedirs(os.path.join(docs_folder, 'landing_pages'), exist_ok=True)
    os.makedirs(os.path.join(docs_folder, 'icons'), exist_ok=True)

    copy_icons(os.path.join(templates_root, 'icons'), docs_folder)

    template = open(os.path.join(templates_root, 'index.html')).read()
    with open(os.path.join(docs_folder, 'index.html'), 'w') as html_file:
        html_file.write(template
                        .replace('${tabs_style}', tabs_style)
                        .replace('${tabs_script}', tabs_script)
                        .replace('${breadcrumbs_style}', breadcrumbs_style)
                        .replace('${breadcrumbs_script}', breadcrumbs_script)
                        .replace('${breadcrumbs}', render_breadcrumbs('index_breadcrumbs.json', {
                            'domain_name': domain['name']
                        }))
                        .replace('${date}', date_string)
                        .replace('${domain_name}', domain['name'])
                        .replace('${domain_description}', domain['description'])
                        .replace('${teams}', json.dumps(teams_payload)))


def create_landing_pages(domain, docs_folder, teams_payload):
    template = open(os.path.join(templates_root, 'landing_page.html')).read()

    for group in teams_payload.get('groups', []):
        for team in group.get('teams', []):
            landing_page_file = os.path.join(docs_folder, 'landing_pages', str(team['id']) + '.html')
            with open(landing_page_file, 'w') as html_file:
                html_file.write(template
                                .replace('${common_style}', common_style)
                                .replace('${tabs_style}', tabs_style)
                                .replace('${tabs_script}', tabs_script)
                                .replace('${breadcrumbs_style}', breadcrumbs_style)
                                .replace('${breadcrumbs_script}', breadcrumbs_script)
                                .replace('${breadcrumbs}', render_breadcrumbs('landing_page_breadcrumbs.json', {
                                    'domain_name': domain['name'],
                                    'team_name': team.get('name', team['id'])
                                }))
                                .replace('${date}', date_string)
                                .replace('${domain_name}', domain['name'])
                                .replace('${team_name}', team.get('name', team['id']))
                                .replace('${team}', json.dumps(team)))

domain_id = domain['id']
teams_path = domains_root + domain_id + '/teams/teams.json'
if not os.path.exists(teams_path):
    raise SystemExit(f"Missing teams config for domain '{domain_id}'")

customers = load_json_if_exists(domains_root + domain_id + '/customers/customers.json', [])
bricks = load_product_bricks_payload(domains_root + domain_id + '/product-bricks/product-bricks.json')
customers_lookup, kpi_lookup = build_customers_lookup(customers)
bricks_lookup = build_bricks_lookup(bricks)
activity_data = load_domain_activity(domains_root, domain_id)
initiatives_enriched = activity_data.get('initiatives', {'items': []})
releases_enriched = activity_data.get('releases', {'items': []})
discoveries_enriched = activity_data.get('discoveries', {'items': []})

teams_payload = json.load(open(teams_path))
team_lookup = build_team_lookup(teams_payload)

enriched_payload = {
    'orgDesign': teams_payload.get('orgDesign', {}),
    'groups': []
}

for group in teams_payload.get('groups', []):
    enriched_payload['groups'].append({
        'id': group.get('id', ''),
        'name': group.get('name', ''),
        'mission': group.get('mission', ''),
        'parentGroupId': group.get('parentGroupId', ''),
        'parentGroupName': group.get('parentGroupName', ''),
        'groupLeadership': group.get('groupLeadership', {}),
        'teams': [
            dict(
                enrich_team(team, team_lookup, customers_lookup, bricks_lookup, initiatives_enriched, releases_enriched, group),
                relatedDiscoveries=find_related_discoveries(discoveries_enriched, team['id'])
            )
            for team in group.get('teams', [])
        ]
    })

add_dependency_data(enriched_payload)

docs_folder = domain_id + '/teams/'
create_overview_docs(domain, docs_folder, enriched_payload)
create_landing_pages(domain, docs_folder, enriched_payload)
