import json
import datetime

data = json.load(open('data/budget.json'))
template = open('templates/budget.html').read();
dateString = datetime.date.today().strftime('%Y-%m-%d')

for group in data['data']:
    htmlFile = 'docs/index.html'
    print(htmlFile)
    with open(htmlFile, 'w') as html_file:
        html_file.write(template.replace('${date}', dateString).replace('${data}', json.dumps(group['data'])))

