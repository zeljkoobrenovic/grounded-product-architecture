import json
import datetime

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[3] / 'docs' / 'standards' / 'principles'
data = json.loads((BASE_DIR / 'data' / 'principles.json').read_text())
template = (BASE_DIR / 'templates' / 'principles.html').read_text()
indexTemplate = (BASE_DIR / 'templates' / 'index.html').read_text()
dateString = datetime.date.today().strftime('%Y-%m-%d')

for group in data['data']:
    htmlFile = BASE_DIR / 'docs' / (group['source'] + '.html')
    print(htmlFile)
    with htmlFile.open('w') as html_file:
        html_file.write(template.replace('${date}', dateString).replace('${data}', json.dumps(group['data'])))

htmlIndexFile = BASE_DIR / 'docs' / 'index.html'
with htmlIndexFile.open('w') as html_index_file:
    print(htmlIndexFile)
    html_index_file.write(indexTemplate.replace('${date}', dateString).replace('${data}', json.dumps(data['data'])))
