import json
import os
import shutil
import datetime
from domain_cli import load_domain_args

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
os.chdir(os.path.join(REPO_ROOT, 'docs', 'product-domains'))

date_string = datetime.date.today().strftime('%Y-%m-%d')

domains_root = '../../_config/product-domains/'
templates_root = '../../_templates/customers/'
domain, site_config = load_domain_args()

tabs_style = open(templates_root + '../_imports/tabs/style.html').read()
tabs_script = open(templates_root + '../_imports/tabs/script.html').read()
common_style = open(templates_root + '../_imports/common/style.html').read()
breadcrumbs_style = open(templates_root + '../_imports/breadcrumbs/style.html').read()
breadcrumbs_script = open(templates_root + '../_imports/breadcrumbs/script.html').read()


def render_breadcrumbs(template_name, replacements):
    breadcrumbs = open(os.path.join(templates_root, template_name)).read()
    for key, value in replacements.items():
        breadcrumbs = breadcrumbs.replace('${' + key + '}', value)
    return breadcrumbs


def load_insights(domain_id):
    insights_file_path = domains_root + domain_id + '/customers/insights.json'
    if not os.path.exists(insights_file_path):
        return {"items": []}
    insights = json.load(open(insights_file_path))
    source_lookup = {source.get('id'): source for source in insights.get('sources', [])}
    for item in insights.get('items', []):
        resolved_sources = []
        for source_id in item.get('sourceIds', []):
            if source_id in source_lookup:
                resolved_sources.append(source_lookup[source_id])
        if resolved_sources:
            item['sources'] = resolved_sources
    return insights


def load_links(domain_id):
    links_file_path = domains_root + domain_id + '/customers/links.json'
    if not os.path.exists(links_file_path):
        return {"groups": []}
    return json.load(open(links_file_path))


def copy_media(icons_path, docs_folder):
    if os.path.exists(icons_path):
        for filename in os.listdir(icons_path):
            src = os.path.join(icons_path, filename)
            dst = os.path.join(docs_folder, filename)
            if os.path.isfile(src):
                shutil.copy2(src, dst)


def load_stream_brick_kinds(domain_id):
    """Map stream/brick ids to their kind so JTBD streamsNeeded entries can
    link to the corresponding stream or brick landing page."""
    kinds = {}

    def walk(node, key, out):
        if isinstance(node, dict):
            for item in node.get(key, []) or []:
                if isinstance(item, dict) and item.get('id'):
                    out.append(str(item['id']))
            for group_key in ('rootGroups', 'subGroups', 'groups'):
                for child in node.get(group_key, []) or []:
                    walk(child, key, out)
        elif isinstance(node, list):
            for child in node:
                walk(child, key, out)

    bricks_path = domains_root + domain_id + '/product-bricks/product-bricks.json'
    if os.path.exists(bricks_path):
        ids = []
        walk(json.load(open(bricks_path)), 'bricks', ids)
        for brick_id in ids:
            kinds[brick_id] = 'brick'
    streams_path = domains_root + domain_id + '/product-bricks/product-stream.json'
    if os.path.exists(streams_path):
        ids = []
        walk(json.load(open(streams_path)), 'streams', ids)
        for stream_id in ids:
            kinds[stream_id] = 'stream'
    return kinds


def create_overview_docs(domain, docs_folder, customers, insights, links):
    if os.path.exists(docs_folder): shutil.rmtree(docs_folder)
    os.makedirs(os.path.join(docs_folder, 'icons'), exist_ok=True)
    os.makedirs(os.path.join(docs_folder, 'media'), exist_ok=True)

    copy_media(templates_root + 'icons', docs_folder + 'icons')
    copy_media(domains_root + domain['id'] + '/customers/icons', docs_folder + 'icons')
    copy_media(domains_root + domain['id'] + '/customers/media', docs_folder + 'media')

    with open(os.path.join(docs_folder, 'index.html'), 'w') as html_file:
        template = open(templates_root + 'index.html').read()
        html_file.write(template
                        .replace('${tabs_style}', tabs_style)
                        .replace('${tabs_script}', tabs_script)
                        .replace('${breadcrumbs_style}', breadcrumbs_style)
                        .replace('${breadcrumbs_script}', breadcrumbs_script)
                        .replace('${breadcrumbs}', render_breadcrumbs('index_breadcrumbs.json', {
                            'domain_name': domain['name']
                        }))
                        .replace('${tabs_style}', tabs_style)
                        .replace('${tabs_script}', tabs_script)
                        .replace('${date}', date_string)
                        .replace('${domain_name}', domain['name'])
                        .replace('${domain_description}', domain['description'])
                        .replace('${customers}', json.dumps(customers))
                        .replace('${insights}', json.dumps(insights))
                        .replace('${links}', json.dumps(links)))


def create_landing_pages(customers, docs_folder, insights):
    os.makedirs(os.path.join(docs_folder, 'landing_pages'), exist_ok=True)

    template = open(templates_root + 'landing_page.html').read()

    dateString = datetime.date.today().strftime('%Y-%m-%d')

    all_customers = []

    for group in customers:
        print(group['group'])
        for customer in group['customers']:
            customer['domain'] = group['group']
            all_customers.append(customer)

    for group in customers:
        for customer in group['customers']:
            name = customer['name']
            customer_insights = []
            for insight in insights.get('items', []):
                for link in insight.get('linkedCustomers', []):
                    if link.get('customerId') == customer['id']:
                        customer_insights.append({
                            "id": insight.get('id'),
                            "title": insight.get('title'),
                            "summary": insight.get('summary'),
                            "implication": insight.get('implication'),
                            "priority": insight.get('priority'),
                            "tags": insight.get('tags', []),
                            "sources": insight.get('sources', []),
                            "link": link
                        })
                        break

            landing_page_file = docs_folder + '/landing_pages/' + str(customer['id']) + '.html'
            with open(landing_page_file, 'w') as html_file:
                html_file.write(template
                                .replace('${common_style}', common_style)
                                .replace('${tabs_style}', tabs_style)
                                .replace('${tabs_script}', tabs_script)
                                .replace('${breadcrumbs_style}', breadcrumbs_style)
                                .replace('${breadcrumbs_script}', breadcrumbs_script)
                                .replace('${breadcrumbs}', render_breadcrumbs('landing_page_breadcrumbs.json', {
                                    'domain_name': domain['name'],
                                    'customer_name': customer['name']
                                }))
                                .replace('${date}', dateString)
                                .replace('${config}', json.dumps(site_config))
                                .replace('${all_customers}', json.dumps(all_customers))
                                .replace('${customer_name}', customer['name'])
                                .replace('${customer}', json.dumps(customer))
                                .replace('${stream_brick_kinds}', json.dumps(stream_brick_kinds))
                                .replace('${customer_insights}', json.dumps(customer_insights)))

domain_id = domain['id']
customers_file_path = domains_root + domain_id + '/customers/customers.json'
if not os.path.exists(customers_file_path):
    raise SystemExit(f"Missing customers config for domain '{domain_id}'")

customers = json.load(open(customers_file_path))
insights = load_insights(domain_id)
links = load_links(domain_id)
stream_brick_kinds = load_stream_brick_kinds(domain_id)

docs_folder = domain_id + '/customers/'
create_overview_docs(domain, docs_folder, customers, insights, links)
create_landing_pages(customers, docs_folder, insights)
