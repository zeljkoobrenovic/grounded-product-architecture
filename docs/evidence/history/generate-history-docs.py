import json
import datetime

data = json.load(open('data/history.json'))
logos = json.load(open('data/logos.json'))
template = open('templates/history.html').read()

for source in data['data']:
    htmlFile = 'docs/' + source['source'] + '.html'
    print(htmlFile)
    with open(htmlFile, 'w') as html_file:
        content = template.replace('${logos}', json.dumps(logos)).replace('${data}', json.dumps([source], ensure_ascii=False))
        html_file.write(content)

dateString = datetime.date.today().strftime('%Y-%m-%d')
content = template.replace('${logos}', json.dumps(logos)).replace('${date}', dateString).replace('${data}', json.dumps(data['data'], ensure_ascii=False))

with open('docs/index.html', 'w') as html_file:
    html_file.write(content.replace("class=\"hidden", ""))

with open('docs/embed.html', 'w') as html_file:
    html_file.write(content)
