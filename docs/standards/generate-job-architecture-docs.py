import datetime
import json
import shutil
from pathlib import Path


DATE_STRING = datetime.date.today().strftime('%Y-%m-%d')
REPO_ROOT = Path(__file__).resolve().parents[2]
CONFIG_PATH = REPO_ROOT / '_config' / 'standards' / 'management' / 'job-architecture' / 'job-architecture.json'
TEMPLATE_ROOT = REPO_ROOT / '_templates' / 'standards' / 'job-architecture'
TEMPLATE_PATH = TEMPLATE_ROOT / 'index.html'
DOCS_ROOT = Path(__file__).resolve().parent / 'job-architecture'


def render_template(template_path, replacements):
    content = template_path.read_text()
    for key, value in replacements.items():
        content = content.replace('${' + key + '}', value)
    return content


def main():
    if DOCS_ROOT.exists():
        shutil.rmtree(DOCS_ROOT)

    DOCS_ROOT.mkdir(parents=True, exist_ok=True)

    job_architecture = json.loads(CONFIG_PATH.read_text())
    rendered = render_template(TEMPLATE_PATH, {
        'date': DATE_STRING,
        'job_architecture': json.dumps(job_architecture),
    })

    output_path = DOCS_ROOT / 'index.html'
    output_path.write_text(rendered)
    print(output_path)


if __name__ == '__main__':
    main()
