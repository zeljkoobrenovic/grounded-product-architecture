import json
import os
import re
import shutil
from domain_cli import load_domain_args
from generator_common import (
    copy_icons,
    enter_docs_root,
    load_json_if_exists,
    load_json_items_from_paths as load_json_from_paths,
    today_string,
)
from product_bricks_support import (
    flatten_product_bricks,
    flatten_product_streams,
    load_data_assets_payload,
    load_product_bricks_payload,
    load_product_streams_payload,
    sanitize_product_stream_root_groups,
)

enter_docs_root()

date_string = today_string()

domains_root = '../../_config/product-domains/'
root_templates = '../../_templates/product-bricks/'
domain, site_config = load_domain_args()
evidence_fragments_cache = load_json_if_exists('../../_evidence/database/all-evidence.json', [])

common_style = open(root_templates + '../_imports/common/style.html').read()

breadcrumbs_style = open(root_templates + '../_imports/breadcrumbs/style.html').read()
breadcrumbs_script = open(root_templates + '../_imports/breadcrumbs/script.html').read()

evidence_style = open(root_templates + '../_imports/evidence/style.html').read()
evidence_script = open(root_templates + '../_imports/evidence/script.html').read()

tabs_style = open(root_templates + '../_imports/tabs/style.html').read()
tabs_script = open(root_templates + '../_imports/tabs/script.html').read()


def build_evidence_lookup(cache_groups):
    lookup = {}
    for group in cache_groups:
        group_title = group.get('group', {}).get('title', '')
        group_description = group.get('group', {}).get('description', '')
        for fragment in group.get('fragments', []):
            enriched_fragment = dict(fragment)
            if 'facts' not in enriched_fragment:
                if enriched_fragment.get('summary'):
                    enriched_fragment['facts'] = [enriched_fragment['summary']]
                else:
                    enriched_fragment['facts'] = []
            elif not isinstance(enriched_fragment.get('facts'), list):
                enriched_fragment['facts'] = [str(enriched_fragment.get('facts', ''))]
            enriched_fragment.pop('summary', None)
            fragment_id = str(enriched_fragment.get('id', '')).strip()
            if not fragment_id:
                continue
            enriched_fragment['id'] = fragment_id
            enriched_fragment['evidenceGroupTitle'] = group_title
            enriched_fragment['evidenceGroupDescription'] = group_description
            lookup[fragment_id] = enriched_fragment
    return lookup


evidence_fragment_lookup = build_evidence_lookup(evidence_fragments_cache)


def build_customer_lookup(customers):
    lookup = {}
    for group in customers:
        group_name = group.get('group', '')
        for customer in group.get('customers', []):
            enriched = dict(customer)
            enriched['group'] = group_name
            lookup[customer['id']] = enriched
    return lookup


def build_brick_context(brick, products, customers):
    customer_lookup = build_customer_lookup(customers)
    linked_products = []
    supported_jobs = []
    supported_jobs_index = {}

    brick_id = str(brick.get('id', '')).strip().lower()
    brick_name = str(brick.get('name', '')).strip().lower()

    def stream_matches(stream):
        stream_code = str(stream.get('id', stream.get('streamCode', ''))).strip().lower()
        stream_name = str(stream.get('name', stream.get('streamName', ''))).strip().lower()
        return stream_code == brick_id or stream_name == brick_name

    def append_supported_job(customer, primary_customer, product, job, step, stream, matched_stream):
        item_key = (
            customer.get('id', primary_customer.get('id', '')),
            product.get('id', ''),
            job.get('id', ''),
        )
        if item_key not in supported_jobs_index:
            supported_jobs_index[item_key] = {
                'customerId': customer.get('id', primary_customer.get('id', '')),
                'customerName': customer.get('name', primary_customer.get('name', '')),
                'customerGroup': customer.get('group', ''),
                'customerIcon': customer.get('icon', 'customer.png'),
                'productId': product.get('id', ''),
                'productName': product.get('name', ''),
                'productIcon': product.get('icon', 'product.png'),
                'jobId': job.get('id', ''),
                'jobName': job.get('name', ''),
                'jobWhatItIs': job.get('what_it_is', ''),
                'jobOutcome': job.get('outcome', ''),
                'supportRationale': stream.get('how_it_supports', '') or matched_stream.get('whyNeeded', ''),
                'usedInSteps': []
            }
            supported_jobs.append(supported_jobs_index[item_key])

        supported_job = supported_jobs_index[item_key]
        used_step = {
            'step': step.get('step', ''),
            'description': step.get('description', ''),
            'howItSupports': stream.get('how_it_supports', '') or matched_stream.get('whyNeeded', ''),
            'media': step.get('media', [])
        }
        if used_step not in supported_job['usedInSteps']:
            supported_job['usedInSteps'].append(used_step)

    for product in products.get('portfolio', {}).get('products', []):
        matched_stream = None
        for stream in product.get('neededStreams', []):
            if stream_matches(stream):
                matched_stream = stream
                break

        if not matched_stream:
            continue

        linked_products.append({
            'id': product.get('id', ''),
            'name': product.get('name', ''),
            'icon': product.get('icon', 'product.png'),
            'type': product.get('type', ''),
            'whyUsed': matched_stream.get('whyNeeded', '')
        })

        for primary_customer in product.get('primaryCustomers', []):
            customer = customer_lookup.get(primary_customer.get('id', ''), {})
            for job in customer.get('jobsToBeDone', []):
                for step in job.get('steps', []):
                    # streamsNeeded references product streams; bricksNeeded carries the
                    # lower-level brick implementation dependencies. Match against both so a
                    # brick page surfaces the jobs it supports directly or via a stream.
                    for stream in step.get('streamsNeeded', []) + step.get('bricksNeeded', []):
                        if stream_matches(stream):
                            append_supported_job(customer, primary_customer, product, job, step, stream, matched_stream)

    return linked_products, supported_jobs


def _iter_team_groups(groups):
    """Yield (group, team) for every team in the recursive group tree."""
    for group in groups or []:
        for team in group.get('teams', []):
            yield group, team
        for descendant in _iter_team_groups(group.get('groups', [])):
            yield descendant


def build_brick_team_context(brick, teams_payload):
    related_teams = []
    brick_id = str(brick.get('id', '')).strip()

    for group, team in _iter_team_groups(teams_payload.get('groups', [])):
        links = team.get('brickDependencies', [])
        if not any(str(link.get('brickId', '')).strip() == brick_id for link in links):
            continue

        related_teams.append({
            'teamId': team.get('id', ''),
            'teamName': team.get('name', team.get('id', '')),
            'teamType': team.get('type', ''),
            'groupId': group.get('id', ''),
            'groupName': group.get('name', ''),
            'role': 'related',
            'roleLabel': 'Related team'
        })

    related_teams.sort(key=lambda item: item['teamName'].lower())
    return related_teams


def build_team_lookup(teams_payload):
    """Map teamId -> {teamId, teamName, groupName, teamType} for ownership resolution."""
    lookup = {}
    for group, team in _iter_team_groups(teams_payload.get('groups', [])):
        team_id = str(team.get('id', '')).strip()
        if not team_id:
            continue
        lookup[team_id] = {
            'teamId': team_id,
            'teamName': team.get('name', team_id),
            'teamType': team.get('type', ''),
            'groupName': group.get('name', ''),
        }
    return lookup


def flatten_data_assets_with_context(root_groups):
    """Flatten the recursive data-asset group tree, annotating each asset with its
    rootGroup / group names so landing pages can show the catalog path."""
    flat = []

    def walk(groups, root_name, parent_name):
        for group in groups or []:
            group_name = group.get('name', '')
            current_root = root_name or group_name
            for asset in group.get('assets', []):
                annotated = dict(asset)
                annotated['rootGroup'] = current_root
                annotated['group'] = group_name
                flat.append(annotated)
            walk(group.get('subGroups', []), current_root, group_name)

    walk(root_groups, '', '')
    return flat


def build_data_asset_brick_usage(asset_id, bricks):
    """Mirror the index page's buildDataAssetUsage: split linking bricks into
    producing (own/write/publish/replicate/delete) and consuming (read/query/...)."""
    producing = []
    consuming = []
    producing_roles = {'own', 'write', 'publish', 'replicate', 'delete'}
    for brick in bricks:
        for dep in brick.get('dataDependencies', []):
            if dep.get('assetId') != asset_id:
                continue
            entry = {
                'id': brick.get('id', ''),
                'name': brick.get('name', brick.get('id', '')),
                'role': dep.get('role', ''),
                'description': dep.get('description', ''),
            }
            if str(dep.get('role', '')).lower() in producing_roles:
                producing.append(entry)
            else:
                consuming.append(entry)
    return producing, consuming


def build_evidence(object_id, evidence_items):
    matched_item = next((item for item in evidence_items if str(item.get('object-id', '')).strip() == str(object_id).strip()), None)
    if not matched_item:
        return {'objectId': object_id, 'tabs': []}

    tabs_payload = matched_item.get('tabs', [])
    if not tabs_payload and matched_item.get('evidence-groups'):
        tabs_payload = [{
            'label': 'Source Code',
            'evidence-groups': matched_item.get('evidence-groups', [])
        }]

    tabs = []
    for tab in tabs_payload:
        groups = []
        for item in tab.get('evidence-groups', []):
            fragments = []
            use_regex = bool(item.get('useRegex', False))
            evidence_refs = item.get('evidence-ids', [])
            if use_regex:
                matched_ids = set()
                for evidence_ref in evidence_refs:
                    pattern = evidence_ref.get('id', '') if isinstance(evidence_ref, dict) else evidence_ref
                    try:
                        regex = re.compile(pattern)
                    except re.error:
                        continue
                    for fragment_id, fragment in evidence_fragment_lookup.items():
                        if fragment_id in matched_ids:
                            continue
                        if regex.search(fragment_id):
                            fragment_with_context = dict(fragment)
                            if isinstance(evidence_ref, dict) and evidence_ref.get('note'):
                                fragment_with_context['note'] = evidence_ref.get('note')
                            fragments.append(fragment_with_context)
                            matched_ids.add(fragment_id)
            else:
                for evidence_ref in evidence_refs:
                    fragment_id = evidence_ref.get('id', '') if isinstance(evidence_ref, dict) else evidence_ref
                    fragment = evidence_fragment_lookup.get(fragment_id)
                    if fragment:
                        fragment_with_context = dict(fragment)
                        if isinstance(evidence_ref, dict) and evidence_ref.get('note'):
                            fragment_with_context['note'] = evidence_ref.get('note')
                        fragments.append(fragment_with_context)
            groups.append({
                'name': item.get('group-name', ''),
                'description': item.get('description', ''),
                'fragments': fragments
            })

        tabs.append({
            'label': tab.get('label', 'Evidence'),
            'groups': groups
        })

    return {'objectId': object_id, 'tabs': tabs}


def dedupe_by(items, key_builder):
    index = {}
    ordered = []
    for item in items:
        key = key_builder(item)
        if key in index:
            continue
        index[key] = True
        ordered.append(item)
    return ordered


def merge_supported_jobs(items):
    merged = {}
    ordered = []

    for item in items:
        key = (
            item.get('customerId', ''),
            item.get('productId', ''),
            item.get('jobId', '')
        )
        if key not in merged:
            merged[key] = dict(item)
            merged[key]['usedInSteps'] = list(item.get('usedInSteps', []))
            ordered.append(merged[key])
            continue

        existing = merged[key]
        if not existing.get('supportRationale') and item.get('supportRationale'):
            existing['supportRationale'] = item.get('supportRationale')

        existing_steps = existing.setdefault('usedInSteps', [])
        for step in item.get('usedInSteps', []):
            if step not in existing_steps:
                existing_steps.append(step)

    return ordered


def merge_named_records(items, id_field, list_fields=None):
    merged = {}
    ordered = []
    list_fields = list_fields or []

    for item in items:
        item_id = item.get(id_field, '')
        if item_id not in merged:
            merged[item_id] = dict(item)
            for field in list_fields:
                merged[item_id][field] = list(item.get(field, []))
            ordered.append(merged[item_id])
            continue

        existing = merged[item_id]
        for field, value in item.items():
            if field in list_fields:
                continue
            if not existing.get(field) and value:
                existing[field] = value

        for field in list_fields:
            existing_values = existing.setdefault(field, [])
            for value in item.get(field, []):
                if value not in existing_values:
                    existing_values.append(value)

    return ordered


def create_landing_pages(bricks, products, customers, evidence_items, teams_payload):
    landing_page_template = open(root_templates + 'brick_landing_page.html').read();
    breadcrumbs = open(root_templates + 'brick_landing_page_breadcrumbs.json').read();

    for brick in bricks:
        name = brick['name']
        linked_products, supported_jobs = build_brick_context(brick, products, customers)
        related_teams = build_brick_team_context(brick, teams_payload)
        evidence = build_evidence(brick['id'], evidence_items)

        htmlFile = docs_folder + 'landing_pages/' + str(brick['id']) + '.html'
        with open(htmlFile, 'w') as html_file:
            html_file.write(landing_page_template
                            .replace('${tabs_style}', tabs_style)
                            .replace('${tabs_script}', tabs_script)
                            .replace('${date}', date_string)
                            .replace('${config}', json.dumps(site_config))
                            .replace('${all_bricks}', json.dumps(bricks))
                            .replace('${all_streams}', json.dumps(flat_streams))
                            .replace('${bricks_metadata}', json.dumps(data.get('metadata', {})))
                            .replace('${brick_data}', json.dumps(brick))
                            .replace('${data_assets}', json.dumps(data_assets_payload))
                            .replace('${common_style}', common_style)
                            .replace('${breadcrumbs_style}', breadcrumbs_style)
                            .replace('${breadcrumbs_script}', breadcrumbs_script)
                            .replace('${breadcrumbs}', breadcrumbs)
                            .replace('${domain_name}', domain['name'])
                            .replace('${evidence_style}', evidence_style)
                            .replace('${evidence_script}', evidence_script)
                            .replace('${evidence}', json.dumps(evidence))
                            .replace('${brick_name}', name.replace('&', '&amp;'))
                            .replace('${related_teams}', json.dumps(related_teams))
                            .replace('${linked_products}', json.dumps(linked_products))
                            .replace('${supported_jobs}', json.dumps(supported_jobs)))


def create_stream_landing_pages(streams, bricks, products, customers, evidence_items, teams_payload):
    landing_page_template = open(root_templates + 'stream_landing_page.html').read();
    brick_lookup = {brick['id']: brick for brick in bricks}
    breadcrumbs = open(root_templates + 'stream_landing_page_breadcrumbs.json').read();

    for stream in streams:
        related_bricks = []
        linked_products = list(stream.get('supportedProducts', []))
        supported_jobs = list(stream.get('supportedCustomerJobs', []))
        related_teams = list(stream.get('owningTeams', []))

        for dep in stream.get('brickDependencies', []):
            brick_id = dep.get('targetBrickId', dep.get('targetobjectId', ''))
            if not brick_id or brick_id not in brick_lookup:
                continue
            brick = brick_lookup[brick_id]
            related_bricks.append(brick)
            brick_linked_products, brick_supported_jobs = build_brick_context(brick, products, customers)
            linked_products.extend(brick_linked_products)
            supported_jobs.extend(brick_supported_jobs)
            related_teams.extend(build_brick_team_context(brick, teams_payload))

        related_bricks = dedupe_by(related_bricks, lambda item: item.get('id', ''))
        linked_products = merge_named_records(linked_products, 'id')
        supported_jobs = merge_supported_jobs(supported_jobs)
        related_teams = merge_named_records(related_teams, 'teamId')

        evidence = build_evidence(stream['id'], evidence_items)
        html_file = docs_folder + 'stream_pages/' + str(stream['id']) + '.html'
        with open(html_file, 'w') as html_file:
            html_file.write(landing_page_template
                            .replace('${tabs_style}', tabs_style)
                            .replace('${tabs_script}', tabs_script)
                            .replace('${config}', json.dumps(site_config))
                            .replace('${all_bricks}', json.dumps(bricks))
                            .replace('${all_streams}', json.dumps(streams))
                            .replace('${stream_data}', json.dumps(stream))
                            .replace('${related_bricks}', json.dumps(related_bricks))
                            .replace('${common_style}', common_style)
                            .replace('${breadcrumbs_style}', breadcrumbs_style)
                            .replace('${breadcrumbs_script}', breadcrumbs_script)
                            .replace('${breadcrumbs}', breadcrumbs)
                            .replace('${domain_name}', domain['name'])
                            .replace('${evidence_style}', evidence_style)
                            .replace('${evidence_script}', evidence_script)
                            .replace('${breadcrumbs_style}', breadcrumbs_style)
                            .replace('${breadcrumbs_script}', breadcrumbs_script)
                            .replace('${stream_name}', stream.get('name', stream.get('id', '')).replace('&', '&amp;'))
                            .replace('${evidence}', json.dumps(evidence))
                            .replace('${linked_products}', json.dumps(linked_products))
                            .replace('${related_teams}', json.dumps(related_teams))
                            .replace('${supported_jobs}', json.dumps(supported_jobs)))


def create_data_asset_landing_pages(data_assets_payload, bricks, teams_payload):
    template_path = root_templates + 'data_asset_landing_page.html'
    breadcrumbs_path = root_templates + 'data_asset_landing_page_breadcrumbs.json'
    if not os.path.exists(template_path):
        return

    landing_page_template = open(template_path).read()
    breadcrumbs = open(breadcrumbs_path).read()

    assets = flatten_data_assets_with_context(data_assets_payload.get('rootGroups', []))
    stores = data_assets_payload.get('stores', [])
    team_lookup = build_team_lookup(teams_payload)

    # Lightweight catalog for the nav strip on each page (no need to inline everything).
    nav_assets = [{'id': asset.get('id', ''), 'name': asset.get('name', asset.get('id', ''))} for asset in assets]

    for asset in assets:
        asset_id = str(asset.get('id', '')).strip()
        if not asset_id:
            continue

        producing_bricks, consuming_bricks = build_data_asset_brick_usage(asset_id, bricks)
        owner_team = team_lookup.get(str(asset.get('ownerTeamId', '')).strip()) if asset.get('ownerTeamId') else None
        steward_teams = [
            team_lookup[steward_id]
            for steward_id in asset.get('stewardTeamIds', [])
            if str(steward_id).strip() in team_lookup
        ]

        html_path = docs_folder + 'data_pages/' + asset_id + '.html'
        with open(html_path, 'w') as html_file:
            html_file.write(landing_page_template
                            .replace('${tabs_style}', tabs_style)
                            .replace('${tabs_script}', tabs_script)
                            .replace('${config}', json.dumps(site_config))
                            .replace('${all_bricks}', json.dumps(bricks))
                            .replace('${all_assets}', json.dumps(nav_assets))
                            .replace('${asset_data}', json.dumps(asset))
                            .replace('${all_stores}', json.dumps(stores))
                            .replace('${producing_bricks}', json.dumps(producing_bricks))
                            .replace('${consuming_bricks}', json.dumps(consuming_bricks))
                            .replace('${owner_team}', json.dumps(owner_team))
                            .replace('${steward_teams}', json.dumps(steward_teams))
                            .replace('${common_style}', common_style)
                            .replace('${breadcrumbs_style}', breadcrumbs_style)
                            .replace('${breadcrumbs_script}', breadcrumbs_script)
                            .replace('${breadcrumbs}', breadcrumbs)
                            .replace('${domain_name}', domain['name'])
                            .replace('${asset_name}', (asset.get('name', asset_id)).replace('&', '&amp;')))


domain_id = domain['id']
docs_folder = domain_id + '/product-bricks/'
root_domain = domains_root + docs_folder
product_bricks_config_path = root_domain + 'product-bricks.json'
product_streams_config_path = root_domain + 'product-stream.json'
data_assets_config_path = domains_root + domain_id + '/data/data-assets.json'

if not os.path.exists(product_bricks_config_path):
    raise SystemExit(f"Missing product bricks config for domain '{domain_id}'")

print(root_domain)

# Parse every input BEFORE wiping the output folder, so a config error
# leaves the previously generated docs intact instead of destroying them.
data = load_product_bricks_payload(product_bricks_config_path)
flat_bricks = flatten_product_bricks(data)
streams_payload = load_product_streams_payload(product_streams_config_path)
flat_streams = flatten_product_streams(streams_payload)
data_assets_payload = load_data_assets_payload(data_assets_config_path)
products = load_json_if_exists(domains_root + domain_id + '/product-deployments/products.json', {'portfolio': {'products': []}})
customers = load_json_if_exists(domains_root + domain_id + '/customers/customers.json', [])
teams_payload = load_json_if_exists(domains_root + domain_id + '/teams/teams.json', {'groups': []})
bricks_evidence_items = load_json_from_paths([
    root_domain + 'brick-evidence.json',
    root_domain + 'bricks-evidence.json',
], [])
streams_evidence_items = load_json_from_paths([
    root_domain + 'stream-evidence.json',
    root_domain + 'streams-evidence.json',
], [])

if os.path.exists(docs_folder): shutil.rmtree(docs_folder)
os.makedirs(os.path.join(docs_folder, 'icons'), exist_ok=True)
os.makedirs(os.path.join(docs_folder, 'landing_pages'), exist_ok=True)
os.makedirs(os.path.join(docs_folder, 'stream_pages'), exist_ok=True)
os.makedirs(os.path.join(docs_folder, 'data_pages'), exist_ok=True)

copy_icons(root_templates + 'icons', docs_folder)
copy_icons(domains_root + domain_id + '/product-bricks/icons', docs_folder)
copy_icons('../../_evidence/icons', docs_folder)

with open(docs_folder + 'index.html', 'w') as html_file:
    template = open(root_templates + 'index.html').read()

    breadcrumbs = open(root_templates + 'index_breadcrumbs.json').read();

    content = template.replace('${domain_description}', domain['description'])
    content = content.replace('${bricks}', json.dumps(data)) \
        .replace('${data_assets}', json.dumps(data_assets_payload)) \
        .replace('${tabs_style}', tabs_style) \
        .replace('${tabs_script}', tabs_script) \
        .replace('${breadcrumbs_style}', breadcrumbs_style) \
        .replace('${breadcrumbs_script}', breadcrumbs_script) \
        .replace('${breadcrumbs}', breadcrumbs) \
        .replace('${domain_name}', domain['name'])

    content = content.replace('${product_streams}', json.dumps({
        'metadata': streams_payload.get('metadata', {}),
        'rootGroups': sanitize_product_stream_root_groups(streams_payload.get('rootGroups', [])),
        'experiences': flat_streams,
        'streams': flat_streams
    }))
    html_file.write(content)

create_landing_pages(flat_bricks, products, customers, bricks_evidence_items, teams_payload)
create_stream_landing_pages(flat_streams, flat_bricks, products, customers, streams_evidence_items, teams_payload)
create_data_asset_landing_pages(data_assets_payload, flat_bricks, teams_payload)
