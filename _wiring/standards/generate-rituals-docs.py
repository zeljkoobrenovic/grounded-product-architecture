import datetime
import json
import os
import shutil


date_string = datetime.date.today().strftime('%Y-%m-%d')
repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

config_root = os.path.join(repo_root, '_config/standards/rituals')
templates_root = os.path.join(repo_root, '_templates/rituals')
docs_folder = os.path.join(repo_root, 'docs/standards/rituals')

with open(os.path.join(config_root, 'meetings.json')) as config_file:
    rituals = json.load(config_file)

context = {
    'name': 'Standards',
    'description': 'Shared operating rituals and recurring meetings used across product domains.'
}


def copy_icons(icons_path, destination_folder):
    if os.path.exists(icons_path):
        os.makedirs(os.path.join(destination_folder, 'icons'), exist_ok=True)
        for filename in os.listdir(icons_path):
            src = os.path.join(icons_path, filename)
            dst = os.path.join(destination_folder, 'icons', filename)
            if os.path.isfile(src):
                shutil.copy2(src, dst)


def create_overview_docs():
    if os.path.exists(docs_folder):
        shutil.rmtree(docs_folder)
    os.makedirs(os.path.join(docs_folder, 'landing_pages'), exist_ok=True)
    copy_icons(os.path.join(templates_root, 'icons'), docs_folder)

    with open(os.path.join(docs_folder, 'index.html'), 'w') as html_file:
        with open(os.path.join(templates_root, 'index.html')) as template_file:
            template = template_file.read()
        html_file.write(template
                        .replace('${date}', date_string)
                        .replace('${domain_name}', context['name'])
                        .replace('${domain_description}', context['description'])
                        .replace('${rituals}', json.dumps(rituals)))


def create_landing_pages():
    with open(os.path.join(templates_root, 'landing_page.html')) as template_file:
        template = template_file.read()

    for meeting in rituals.get('meetings', []):
        landing_page_file = os.path.join(docs_folder, 'landing_pages', str(meeting['id']) + '.html')
        with open(landing_page_file, 'w') as html_file:
            html_file.write(template
                            .replace('${date}', date_string)
                            .replace('${domain_name}', context['name'])
                            .replace('${meeting_title}', meeting.get('title', 'Ritual'))
                            .replace('${meeting}', json.dumps(meeting)))


create_overview_docs()
create_landing_pages()
