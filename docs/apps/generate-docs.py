import json

product = json.load(open('data/product.json'))

template = open('templates/apps.html').read();

htmlFile = 'docs/index.html'
print(htmlFile)

with open(htmlFile, 'w') as html_file:
    html_file.write(template
                    .replace('${product}', json.dumps(product)))
