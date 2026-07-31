import json
import os
import shutil

# Resolve repo root relative to this script (_wiring/evidence-explorer/).
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

EVIDENCE_JSON = os.path.join(REPO_ROOT, '_evidence', 'database', 'all-evidence.json')
EVIDENCE_ICONS = os.path.join(REPO_ROOT, '_evidence', 'icons')
TEMPLATE = os.path.join(REPO_ROOT, '_templates', 'evidence-explorer', 'index.html')
TEMPLATE_ICONS = os.path.join(REPO_ROOT, '_templates', 'evidence-explorer', 'icons')
OUTPUT_DIR = os.path.join(REPO_ROOT, 'docs', 'evidence-explorer')

# Icons are copied next to the page under ./icons/, so the page references them
# with this relative base. The fragment "icon" field holds just the filename.
ICON_BASE = 'icons/'


def render(template, replacements):
    for key, value in replacements.items():
        template = template.replace('${' + key + '}', value)
    return template


def main():
    evidence = json.load(open(EVIDENCE_JSON))

    template = open(TEMPLATE).read()
    html = render(template, {
        # json.dumps produces valid JS literal; embedded directly into <script>.
        'evidence_data': json.dumps(evidence, ensure_ascii=False),
        'icon_base': ICON_BASE,
    })

    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)
    os.makedirs(os.path.join(OUTPUT_DIR, 'icons'), exist_ok=True)

    with open(os.path.join(OUTPUT_DIR, 'index.html'), 'w') as f:
        f.write(html)

    # Copy evidence fragment icons first, then template icons (logo.png etc.),
    # so template assets win on any name collision.
    for icons_dir in (EVIDENCE_ICONS, TEMPLATE_ICONS):
        if os.path.exists(icons_dir):
            for filename in os.listdir(icons_dir):
                src = os.path.join(icons_dir, filename)
                if os.path.isfile(src):
                    shutil.copy2(src, os.path.join(OUTPUT_DIR, 'icons', filename))

    fragment_count = sum(len(g.get('fragments', [])) for g in evidence)
    print(f'Wrote {OUTPUT_DIR}/index.html ({fragment_count} fragments)')


if __name__ == '__main__':
    main()
