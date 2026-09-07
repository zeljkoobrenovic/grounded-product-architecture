"""Check package links follow the current published domain groups."""

import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from domain_paths import discover_domain_dirs, domain_docs_path


SPEC = importlib.util.spec_from_file_location(
    'start_apps_generator', Path(__file__).with_name('generate-start-apps-docs.py')
)
START_APPS = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(START_APPS)


class StartAppLinksTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix='productscape-app-links-')
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        (self.root / 'current-group' / 'example').mkdir(parents=True)
        for name, replacement in (
            ('discover_domain_dirs', lambda: discover_domain_dirs(self.root)),
            ('domain_docs_path', lambda domain_id, *parts: domain_docs_path(domain_id, *parts, domains_root=self.root)),
        ):
            patcher = patch.object(START_APPS, name, side_effect=replacement)
            patcher.start()
            self.addCleanup(patcher.stop)

    def test_old_and_current_links_follow_the_source_group(self):
        for url in (
            '../product-domains/example/start/index.html?embed=1#details',
            '../../product-domains/example/start/index.html?embed=1#details',
            '../../old-group/example/start/index.html?embed=1#details',
            '../../current-group/example/start/index.html?embed=1#details',
        ):
            with self.subTest(url=url):
                self.assertEqual(
                    START_APPS.rebase_start_apps_url(url),
                    '../../current-group/example/start/index.html?embed=1#details',
                )

    def test_local_and_external_resources_are_preserved(self):
        for url in ('icons/logo.png', '../../evidence-explorer/index.html',
                    'https://example.com/product-domains/example/', '//example.com/icon.png',
                    'data:image/png;base64,abc', '#details', '', None):
            with self.subTest(url=url):
                self.assertEqual(START_APPS.rebase_start_apps_url(url), url)

    def test_app_links_and_icons_are_resolved_without_mutating_sources(self):
        app = {
            'name': 'Example',
            'link': '../../former-group/example/start/index.html',
            'icon': '../../former-group/example/start/icons/logo.png',
        }
        source = {'apps': [{'apps': [{'apps': [app]}]}]}
        rendered = START_APPS.rebase_app_links(source)['apps'][0]['apps'][0]['apps'][0]
        self.assertEqual(rendered['link'], '../../current-group/example/start/index.html')
        self.assertEqual(rendered['icon'], '../../current-group/example/start/icons/logo.png')
        self.assertEqual(app['link'], '../../former-group/example/start/index.html')

    def test_invalid_domain_link_preserves_existing_package_output(self):
        source = self.root / '_packages' / 'launcher'
        output_root = self.root / '_published'
        source.mkdir(parents=True)
        existing = output_root / 'launcher' / 'index.html'
        existing.parent.mkdir(parents=True)
        existing.write_text('Previous page')
        (source / 'apps.json').write_text(json.dumps({
            'config': {'name': 'Launcher', 'description': 'Example launcher'},
            'apps': [{'apps': [{'apps': [{'link': '../product-domains/missing/start/index.html'}]}]}],
        }))
        with patch.object(START_APPS, 'DOCS_PACKAGES_ROOT', output_root):
            with self.assertRaisesRegex(ValueError, 'Unknown domain'):
                START_APPS.render_package(source, '${apps}')
        self.assertEqual(existing.read_text(), 'Previous page')


if __name__ == '__main__':
    unittest.main()
