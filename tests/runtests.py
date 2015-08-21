#!/usr/bin/env python
import django
import os
import sys

project_root = os.path.abspath(os.path.join(__file__, os.pardir, os.pardir))
sys.path.insert(0, project_root)

os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.settings'

# Fix for Django>=1.7
if hasattr(django, 'setup'):
    django.setup()


try:
    from django_coverage.coverage_runner import CoverageRunner as TestRunner
except ImportError:
    try:
        from django.test.runner import DiscoverRunner as TestRunner
    except ImportError:
        from django.test.simple import DjangoTestSuiteRunner as TestRunner

def runtests():
    test_runner = TestRunner(verbosity=1, interactive=True)
    failures = test_runner.run_tests(['tests'])
    sys.exit(failures)


if __name__ == '__main__':
    runtests()
