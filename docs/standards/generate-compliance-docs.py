import datetime
import json
import shutil
from pathlib import Path


DATE_STRING = datetime.date.today().strftime('%Y-%m-%d')
REPO_ROOT = Path(__file__).resolve().parents[2]
CONFIG_PATH = REPO_ROOT / '_config' / 'standards' / 'compliance' / 'eu_cto_security_compliance.json'
TEMPLATE_ROOT = REPO_ROOT / '_templates' / 'standards' / 'compliance'
TEMPLATE_PATH = TEMPLATE_ROOT / 'index.html'
LANDING_TEMPLATE_PATH = TEMPLATE_ROOT / 'landing_page.html'
DOCS_ROOT = Path(__file__).resolve().parent / 'compliance'


def render_template(template_path, replacements):
    content = template_path.read_text()
    for key, value in replacements.items():
        content = content.replace('${' + key + '}', value)
    return content


def main():
    if DOCS_ROOT.exists():
        shutil.rmtree(DOCS_ROOT)

    DOCS_ROOT.mkdir(parents=True, exist_ok=True)
    if (TEMPLATE_ROOT / 'icons').exists():
        shutil.copytree(TEMPLATE_ROOT / 'icons', DOCS_ROOT / 'icons', dirs_exist_ok=True)

    compliance = json.loads(CONFIG_PATH.read_text())
    rendered = render_template(TEMPLATE_PATH, {
        'date': DATE_STRING,
        'data': json.dumps(compliance),
    })

    output_path = DOCS_ROOT / 'index.html'
    output_path.write_text(rendered)

    landing_pages_root = DOCS_ROOT / 'landing_pages'
    landing_pages_root.mkdir(parents=True, exist_ok=True)

    for domain in compliance.get('domains', []):
        for control in domain.get('controls', []):
            landing_rendered = render_template(LANDING_TEMPLATE_PATH, {
                'control_name': control.get('name', control.get('id', 'Compliance Control')),
                'control': json.dumps(control),
                'domain': json.dumps({
                    'id': domain.get('id'),
                    'name': domain.get('name'),
                    'description': domain.get('description'),
                    'weight': domain.get('weight'),
                }),
                'scoring_model': json.dumps(compliance.get('scoring_model', {})),
            })
            (landing_pages_root / f"{control['id']}.html").write_text(landing_rendered)

    print(output_path)


if __name__ == '__main__':
    main()
