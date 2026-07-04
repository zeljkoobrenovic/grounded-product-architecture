#!/usr/bin/env python3
import re
import sys
from pathlib import Path


SKILL_NAME_RE = re.compile(r'^[a-z0-9-]+$')
SKILL_LINK_RE = re.compile(r'\]\(([^)]+/SKILL\.md)\)')


def parse_frontmatter(path):
    text = path.read_text()
    if not text.startswith('---\n'):
        return {}, 'missing opening frontmatter fence'
    parts = text.split('---\n', 2)
    if len(parts) != 3:
        return {}, 'missing closing frontmatter fence'
    fields = {}
    for line in parts[1].strip().splitlines():
        if ':' not in line:
            return fields, f'bad frontmatter line: {line}'
        key, value = line.split(':', 1)
        fields[key.strip()] = value.strip().strip('"')
    return fields, None


def main():
    skills_root = Path(__file__).resolve().parents[1]
    errors = []

    skill_files = sorted(skills_root.glob('*/*/SKILL.md'))
    if not skill_files:
        errors.append('No nested SKILL.md files found under core-skills, skill-clusters, or meta-skills.')

    seen_names = {}
    for path in skill_files:
        fields, error = parse_frontmatter(path)
        rel = path.relative_to(skills_root)
        if error:
            errors.append(f'{rel}: {error}')
            continue

        extra_fields = sorted(set(fields) - {'name', 'description'})
        if extra_fields:
            errors.append(f'{rel}: unsupported frontmatter fields: {", ".join(extra_fields)}')

        name = fields.get('name', '')
        description = fields.get('description', '')
        if not name:
            errors.append(f'{rel}: missing name')
        elif not SKILL_NAME_RE.fullmatch(name):
            errors.append(f'{rel}: invalid skill name: {name}')
        elif name != path.parent.name:
            errors.append(f'{rel}: skill name does not match folder name: {name} != {path.parent.name}')
        elif name in seen_names:
            errors.append(f'{rel}: duplicate skill name also used by {seen_names[name]}')
        else:
            seen_names[name] = rel

        if not description:
            errors.append(f'{rel}: missing description')
        elif len(description) < 60:
            errors.append(f'{rel}: description is too short to trigger reliably')

        body = path.read_text().split('---\n', 2)[-1].strip()
        if len(body.splitlines()) < 20:
            errors.append(f'{rel}: body is too short for a useful skill')

    overview_path = skills_root / 'SKILLS-OVERVIEW.md'
    if not overview_path.exists():
        errors.append('Missing SKILLS-OVERVIEW.md')
    else:
        overview = overview_path.read_text()
        links = SKILL_LINK_RE.findall(overview)
        missing = [link for link in links if not (skills_root / link).exists()]
        for link in missing:
            errors.append(f'SKILLS-OVERVIEW.md: broken skill link: {link}')

        linked_paths = {(skills_root / link).resolve() for link in links}
        unlinked = [path.relative_to(skills_root) for path in skill_files if path.resolve() not in linked_paths]
        for rel in unlinked:
            errors.append(f'SKILLS-OVERVIEW.md: skill is not linked: {rel}')

    prompt_path = skills_root / 'NEW-DOMAIN-PROMPT.md'
    if not prompt_path.exists():
        errors.append('Missing NEW-DOMAIN-PROMPT.md')
    else:
        prompt = prompt_path.read_text()
        stale_patterns = [
            '_config/_prompts',
            'domina, group and brick',
            'Proper tree',
            'RIPE NCC',
        ]
        for pattern in stale_patterns:
            if pattern in prompt:
                errors.append(f'NEW-DOMAIN-PROMPT.md: stale text found: {pattern}')

    if errors:
        print('Skill validation failed:')
        for error in errors:
            print(f'- {error}')
        return 1

    print(f'Skill validation passed: {len(skill_files)} SKILL.md files checked.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
