import json
import datetime
import os
import shutil
from initiatives_support import load_domain_activity, filter_for_brick

def load_json_if_exists(path, default_value):
    if os.path.exists(path):
        return json.load(open(path))
    return default_value


def copy_icons(icons_path, docs_folder):
    if os.path.exists(icons_path):
        for filename in os.listdir(icons_path):
            src = os.path.join(icons_path, filename)
            dst = os.path.join(docs_folder, 'icons', filename)
            if os.path.isfile(src):
                shutil.copy2(src, dst)


date_string = datetime.date.today().strftime('%Y-%m-%d')

domains_root = '../../_config/product-domains/'
root_templates = '../../_templates/product-bricks/'

config = json.load(open(domains_root + 'config.json'))
template_config = json.load(open(root_templates + 'config.json'))


def create_landing_pages(bricks, activity_data):
    landing_page_template = open(root_templates + 'landing_page.html').read();

    capabilities_map = {}
    for brick in bricks:
        capabilities_map[brick['name']] = brick

    capabilities_name_index = {}

    for brick in bricks:
        name = brick['name']
        capabilities_name_index[name.lower().strip()] = brick

    for brick in bricks:
        name = brick['name']

        htmlFile = docs_folder + 'landing_pages/' + str(brick['id']) + '.html'
        with open(htmlFile, 'w') as html_file:
            html_file.write(landing_page_template
                            .replace('${date}', date_string)
                            .replace('${config}', json.dumps(config))
                            .replace('${all_bricks}', json.dumps(bricks))
                            .replace('${brick_name}', name.replace('&', '&amp;'))
                            .replace('${brick_data}', json.dumps(brick))
                            .replace('${initiatives}', json.dumps(filter_for_brick(activity_data['initiatives'], brick['id'])))
                            .replace('${releases}', json.dumps(filter_for_brick(activity_data['releases'], brick['id']))))


for domain in config['domains']:
    domain_id = domain['id']
    domain_name = domain['name']

    docs_folder = domain_id + '/product-bricks/'

    root_domain = domains_root + docs_folder

    product_bricks_config_path = root_domain + 'product-bricks.json'

    if not os.path.exists(product_bricks_config_path):
        print("Skipping " + root_domain)
        continue

    print(root_domain)

    if os.path.exists(docs_folder): shutil.rmtree(docs_folder)
    os.makedirs(os.path.join(docs_folder, 'icons'), exist_ok=True)
    os.makedirs(os.path.join(docs_folder, 'landing_pages'), exist_ok=True)

    data = json.load(open(product_bricks_config_path))
    activity_data = load_domain_activity(domains_root, domain_id)

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

            sub_groups[key]['items'].append(item)

        return groups_list


    copy_icons(root_templates + 'icons', docs_folder)
    copy_icons(domains_root + domain_id + '/product-bricks/icons', docs_folder)

    def process():
        with open(docs_folder + 'index.html', 'w') as html_file:
            template = open(root_templates + 'index.html').read()
            content = template.replace('${domain_name}', domain_name)
            html_file.write(content)

        with open(docs_folder + 'map.html', 'w') as html_file:
            template = open(root_templates + 'map.html').read()
            content = template.replace('${bricks}', json.dumps(data))
            content = content.replace('${domain_name}', domain_name)
            content = content.replace('${config}', json.dumps(template_config))
            html_file.write(content)

    process()

    create_landing_pages(data, activity_data)
