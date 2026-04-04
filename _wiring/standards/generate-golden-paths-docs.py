import datetime
import json
import shutil
from pathlib import Path


DATE_STRING = datetime.date.today().strftime('%Y-%m-%d')
REPO_ROOT = Path(__file__).resolve().parents[2]
CONFIG_ROOT = REPO_ROOT / '_config' / 'standards' / 'golden-paths'
TEMPLATES_ROOT = REPO_ROOT / '_templates' / 'standards' / 'golden-paths'
DOCS_ROOT = REPO_ROOT / 'docs' / 'standards' / 'golden-paths'

SECTIONS = {
    'guidelines': {
        'overview_template': 'overview.html',
        'owners_template': 'owners.html',
        'paths_template': 'paths.html',
        'summary_template': 'summaries.html',
    },
    'tech': {
        'overview_template': 'overview.html',
        'owners_template': 'owners.html',
        'paths_template': 'paths.html',
        'summary_template': None,
    },
}


def render_template(template_path, replacements):
    content = template_path.read_text()
    for key, value in replacements.items():
        content = content.replace('${' + key + '}', value)
    return content


def copy_directory_if_exists(source, destination):
    if source.exists():
        shutil.copytree(source, destination, dirs_exist_ok=True)


def generate_section(section_id, section_config):
    section_config_root = CONFIG_ROOT / section_id
    section_templates_root = TEMPLATES_ROOT / section_id
    section_docs_root = DOCS_ROOT / section_id
    output_root = section_docs_root / 'docs'

    if section_docs_root.exists():
        shutil.rmtree(section_docs_root)

    output_root.mkdir(parents=True, exist_ok=True)
    copy_directory_if_exists(section_templates_root / 'icons', output_root / 'icons')
    copy_directory_if_exists(section_templates_root / 'slides', output_root / 'slides')

    data = json.loads((section_config_root / 'paths.json').read_text())

    paths_template = section_templates_root / section_config['paths_template']
    owners_template = section_templates_root / section_config['owners_template']
    overview_template = section_templates_root / section_config['overview_template']
    summary_template_name = section_config['summary_template']

    for group in data['data']:
        filename = group['source'].lower() + '.html'
        template_path = owners_template if group['source'].lower() == 'owners' else paths_template
        rendered = render_template(template_path, {
            'date': DATE_STRING,
            'data': json.dumps(group['data']),
        })
        output_path = output_root / filename
        output_path.write_text(rendered)
        print(output_path)

    overview_output_path = output_root / 'overview.html'
    overview_output_path.write_text(render_template(overview_template, {
        'date': DATE_STRING,
        'data': json.dumps(data['data']),
    }))
    print(overview_output_path)

    if summary_template_name:
        summaries_output_path = output_root / 'summaries.html'
        summaries_output_path.write_text(render_template(section_templates_root / summary_template_name, {
            'date': DATE_STRING,
            'data': json.dumps(data['data']),
        }))
        print(summaries_output_path)

    index_output_path = output_root / 'index.html'
    index_output_path.write_text(render_template(section_templates_root / 'index.html', {
        'date': DATE_STRING,
    }))
    print(index_output_path)


for section_id, section_config in SECTIONS.items():
    generate_section(section_id, section_config)
