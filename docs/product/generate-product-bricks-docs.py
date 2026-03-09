import json
import datetime
import os
import shutil


def copy_icons(icons_path, docs_folder):
    if os.path.exists(icons_path):
        for filename in os.listdir(icons_path):
            src = os.path.join(icons_path, filename)
            dst = os.path.join(docs_folder, 'icons', filename)
            if os.path.isfile(src):
                shutil.copy2(src, dst)


date_string = datetime.date.today().strftime('%Y-%m-%d')

print(os.getcwd())

domains_root = '../../_config/product-domains/'
root_templates = '../../_templates/product/product-bricks/'

config = json.load(open(domains_root + 'config.json'))
template_config = json.load(open(root_templates + 'config.json'))


def create_landing_pages(capabilities, documents, dependency_data, roadmap, targets):
    landing_page_template = open(root_templates + 'landing_page.html').read();

    for capability in targets['data']:
        capability['data'] = [a for a in capability['data'] if a.get('target')];

    capabilities_map = {}
    for capability in capabilities['data'][0]['data']:
        capabilities_map[capability['capability']] = capability

    for discussion in documents['data']:
        cap_name = discussion['source']
        if capabilities_map.get(cap_name):
            capabilities_map[cap_name]['discussions'] = discussion['data']

    def target_by_name(name):
        for target in targets['data']:
            if target['source'].lower() == name.lower():
                return target['data']

        return []

    capabilities_name_index = {}

    for capability in capabilities['data'][0]['data']:
        name = capability['capability']
        capabilities_name_index[name.lower().strip()] = capability

    def capability_by_name(name):
        if capabilities_name_index.get(name.lower().strip()):
            return capabilities_name_index[name.lower().strip()]
        return {'id': 0}

    for capability in capabilities['data'][0]['data']:
        name = capability['capability']

        # roadmaps
        capability_roadmap = []

        for road in roadmap:
            if road['capability'].lower() == name.lower():
                capability_roadmap.append(road)

        # synergies and dependencies
        dependencies = []
        for dependency_group in dependency_data['data']:
            for dependency in dependency_group['data']:
                if dependency.get('capability') and dependency.get('dependency') and dependency['capability'].lower() == name.lower():
                    dependency['image_id'] = capability_by_name(dependency['dependency'])['id']
                    dependencies.append(dependency)

        reverse_dependencies = []
        for dependency_group in dependency_data['data']:
            for dependency in dependency_group['data']:
                if dependency.get('dependency') and dependency['dependency'].lower() == name.lower() and dependency.get('usage_commitment'):
                    dependency['source'] = dependency_group['source']
                    dependency['image_id'] = capability_by_name(dependency['capability'])['id']
                    reverse_dependencies.append(dependency)

        htmlFile = docs_folder + 'landing_pages/' + str(capability['id']) + '.html'
        print(htmlFile)
        with open(htmlFile, 'w') as html_file:
            html_file.write(landing_page_template
                            .replace('${date}', date_string)
                            .replace('${config}', json.dumps(config))
                            .replace('${all_capabilities}', json.dumps(capabilities['data'][0]['data']))
                            .replace('${capability_name}', name.replace('&', '&amp;'))
                            .replace('${capability_data}', json.dumps(capability))
                            .replace('${capability_targets}', json.dumps(target_by_name(name)))
                            .replace('${roadmap}', json.dumps(capability_roadmap))
                            .replace('${dependencies}', json.dumps(dependencies))
                            .replace('${reverse_dependencies}', json.dumps(reverse_dependencies)))


def create_roadmap_docs(domain_id, docs_folder, bricks):
    roadmap_data = json.load(open(domains_root + domain_id + '/product-bricks/roadmap/roadmap.json'))
    with open(docs_folder + 'roadmap-report.html', 'w') as html_file:
        template = open(root_templates + 'progress-report.html').read()
        content = template.replace('${data}', json.dumps(roadmap_data))
        content = content.replace('${capabilities}', json.dumps(bricks))
        html_file.write(content)

    with open(docs_folder + 'roadmap-per-capability.html', 'w') as html_file:
        template = open(root_templates + 'roadmap-per-capability.html').read()
        content = template.replace('${data}', json.dumps(roadmap_data))
        html_file.write(content)

    with open(docs_folder + 'roadmap-sum.html', 'w') as html_file:
        template = open(root_templates + 'roadmap-sum.html').read()
        content = template.replace('${config}', json.dumps(template_config))
        content = content.replace('${data}', json.dumps(roadmap_data))
        html_file.write(content)

    with open(docs_folder + 'roadmap-per-year.html', 'w') as html_file:
        template = open(root_templates + 'roadmap-per-year.html').read()
        content = template.replace('${data}', json.dumps(roadmap_data))
        content = content.replace('${capabilities}', json.dumps(bricks))
        html_file.write(content)


for domain in config['domains']:
    domain_id = domain['id']
    domain_name = domain['name']

    docs_folder = domain_id + '/product-bricks/'

    if os.path.exists(docs_folder): shutil.rmtree(docs_folder)
    os.makedirs(os.path.join(docs_folder, 'icons'), exist_ok=True)
    os.makedirs(os.path.join(docs_folder, 'landing_pages'), exist_ok=True)

    root_domain = domains_root + docs_folder
    print(root_domain)

    data = json.load(open(root_domain + 'product-bricks.json'))
    targets = json.load(open(root_domain + 'targets.json'))
    documents = json.load(open(root_domain + 'documents.json'))

    for brick in targets['data']:
        brick['data'] = [a for a in brick['data'] if True];


    def get_groups(bricks_list):
        groups_map = {}
        groups_list = []
        sub_groups = {}

        for (item) in bricks_list:
            sub_domain = item['domain'].strip()

            if sub_domain not in groups_map:
                groups_map[sub_domain] = []
                groups_list.append({'domain': sub_domain, 'groups': groups_map[sub_domain]})

            if item.get('group'):
                sub_group = item['group']
            else:
                sub_group = ''

            key = sub_domain + '_' + sub_group

            if key not in sub_groups:
                sub_groups[key] = {'group': sub_group, 'items': []}
                groups_map[sub_domain].append(sub_groups[key])

            item['inflight'] = not item.get('status') or not item['status'].lower().startswith('not')
            sub_groups[key]['items'].append(item)

        return groups_list


    copy_icons(root_templates + 'icons', docs_folder)
    copy_icons(domains_root + domain_id + '/product-bricks/icons', docs_folder)

    shutil.copy2(root_templates + 'roadmaps.html', docs_folder + 'roadmaps.html')


    def process(all_list):
        all = get_groups(all_list)

        with open(docs_folder + 'index.html', 'w') as html_file:
            template = open(root_templates + 'index.html').read()
            content = template.replace('${documents_sheet}', domain['sheets']['documents'])
            content = content.replace('${targets_sheet}', domain['sheets']['targets'])
            content = content.replace('${dependencies_sheet}', domain['sheets']['dependencies'])
            content = content.replace('${roadmap_sheet}', domain['sheets']['roadmap'])
            content = content.replace('${details_sheet}', domain['sheets']['details'])
            html_file.write(content)

        with open(docs_folder + 'map.html', 'w') as html_file:
            template = open(root_templates + 'map.html').read()
            content = template.replace('${data}', json.dumps(all)).replace('${targets}', json.dumps(targets))
            content = content.replace('${config}', json.dumps(template_config))
            html_file.write(content)

        with open(docs_folder + 'progress-report.html', 'w') as html_file:
            template = open(root_templates + 'progress-report.html').read()
            content = template.replace('${data}', json.dumps(all)).replace('${targets}', json.dumps(targets))
            html_file.write(content)

        with open(docs_folder + 'map-discussions.html', 'w') as html_file:
            template = open(root_templates + 'map-discussions.html').read()
            content = template.replace('${data}', json.dumps(all)).replace('${discussions}', json.dumps(documents['data']))
            content = content.replace('${config}', json.dumps(template_config))
            html_file.write(content)

        with open(docs_folder + 'map-discussions-list.html', 'w') as html_file:
            template = open(root_templates + 'map-discussions-list.html').read()
            content = template \
                .replace('${data}', json.dumps(all)) \
                .replace('${discussions}', json.dumps(documents['data']))
            html_file.write(content)


    process(data['data'][0]['data'])

    create_roadmap_docs(domain_id, docs_folder, data['data'][0]['data'])

    create_landing_pages(data, documents, {'data': []}, [], targets)
