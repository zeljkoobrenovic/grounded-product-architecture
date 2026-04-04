import json
import datetime

index = json.load(open('index.json'))

cache = []

for group in index['evidence-fragment-files']:
    data = json.load(open(group['file']))
    cache.append({
        'group': group,
        'fragments': data['fragments']
    })

file_path = 'database/all-evidence.json'

with open(file_path, 'w') as file:
    print(file_path)
    file.write(json.dumps(cache))
