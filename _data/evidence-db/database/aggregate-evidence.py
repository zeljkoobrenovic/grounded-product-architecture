import json
from pathlib import Path


def build_group(stem):
    return {
        'id': stem,
        'name': stem,
        'file': f'database/evidence-files/{stem}.json',
    }


database_root = Path(__file__).resolve().parent
evidence_files_root = database_root / 'evidence-files'
cache = []

for path in sorted(evidence_files_root.glob('*.json')):
    data = json.loads(path.read_text())
    cache.append({
        'group': build_group(path.stem),
        'fragments': data.get('fragments', [])
    })

file_path = database_root / 'all-evidence.json'
print(str(file_path))
file_path.write_text(json.dumps(cache))
