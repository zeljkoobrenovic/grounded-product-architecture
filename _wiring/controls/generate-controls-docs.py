import datetime
import json
import shutil
from pathlib import Path

DATE_STRING = datetime.date.today().strftime('%Y-%m-%d')
REPO_ROOT = Path(__file__).resolve().parents[2]
TEMPLATE_ROOT = REPO_ROOT / '_templates' / 'controls'
TEMPLATE_PATH = TEMPLATE_ROOT / 'index.html'
LANDING_TEMPLATE_PATH = TEMPLATE_ROOT / 'landing_page.html'

CONFIG_ROOT = REPO_ROOT / '_config' / 'controls'
DOCS_ROOT = REPO_ROOT / 'docs' / 'controls'

CONTROLS = [
    {
        'config': CONFIG_ROOT / 'security_controls.json',
        'docs': DOCS_ROOT / 'security-controls'
    },
    {
        'config': CONFIG_ROOT / 'management_controls.json',
        'docs': DOCS_ROOT / 'management-controls'
    },
    {
        'config': CONFIG_ROOT / 'operational_controls.json',
        'docs': DOCS_ROOT / 'operational-controls'
    },
    {
        'config': CONFIG_ROOT / 'engineering_controls.json',
        'docs': DOCS_ROOT / 'engineering-controls'
    }
]


def render_template(template_path, replacements):
    content = template_path.read_text()
    for key, value in replacements.items():
        content = content.replace('${' + key + '}', value)
    return content


def main():
    for control in CONTROLS:
        docs_root = control['docs']
        if docs_root.exists():
            shutil.rmtree(docs_root)

        docs_root.mkdir(parents=True, exist_ok=True)
        if (TEMPLATE_ROOT / 'icons').exists():
            shutil.copytree(TEMPLATE_ROOT / 'icons', docs_root / 'icons', dirs_exist_ok=True)
        if (CONFIG_ROOT / 'icons').exists():
            shutil.copytree(CONFIG_ROOT / 'icons', docs_root / 'icons', dirs_exist_ok=True)

        compliance = json.loads(control['config'].read_text())
        rendered = render_template(TEMPLATE_PATH, {
            'date': DATE_STRING,
            'data': json.dumps(compliance),
        })

        output_path = docs_root / 'index.html'
        output_path.write_text(rendered)

        landing_pages_root = docs_root / 'landing_pages'
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
                    'icon': compliance.get('metadata', {}).get('icon', ''),
                })
                (landing_pages_root / f"{control['id']}.html").write_text(landing_rendered)

        print(output_path)


if __name__ == '__main__':
    main()
