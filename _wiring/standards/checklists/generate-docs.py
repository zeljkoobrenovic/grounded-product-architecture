import json
import datetime

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[3] / 'docs' / 'standards' / 'checklists'
CONFIG_PATH = Path(__file__).resolve().parents[3] / '_config' / 'standards' / 'chelcists' / 'config.json'
config = json.loads(CONFIG_PATH.read_text())
data = json.loads((BASE_DIR / 'data' / 'data.json').read_text())
dateString = datetime.date.today().strftime('%Y-%m-%d')

with (BASE_DIR / 'docs' / 'index.html').open('w') as html_file:
    template = (BASE_DIR / 'templates' / 'documents.html').read_text()
    html_file.write(template
                    .replace('${date}', dateString)
                    .replace('${source_link}', config['sheets']['data'])
                    .replace('${data}', json.dumps(data)))
