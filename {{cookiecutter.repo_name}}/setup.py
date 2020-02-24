#! /usr/bin/env python3
# pylint: disable=bad-whitespace, attribute-defined-outside-init, invalid-name
# pylint: disable=too-many-statements, wrong-import-position
"""
    {{ cookiecutter.project_name }} – {{ cookiecutter.short_description }}.

    This setuptools script follows the DRY principle and tries to
    minimize repetition of project metadata by loading it from other
    places (like the package's `__init__.py`). Incidently, this makes
    the script almost identical between different projects.

    It is also importable (by using the usual `if __name__ == '__main__'`
    idiom), and exposes the project's setup data in a `project` dict.
    This allows other tools to exploit the data assembling code contained
    in here, and again supports the DRY principle. The `rituals` package
    uses that to provide Invoke tasks that work for any project, based on
    its project metadata.

    Copyright ©  {{ cookiecutter.year }} {{ cookiecutter.full_name }} <{{ cookiecutter.email }}>

    ## LICENSE_SHORT ##
"""

# Project data (the rest is parsed from __init__.py and other project files)
name = '{{ cookiecutter.repo_name }}'
package_name = '{{ cookiecutter.pkg_name }}'
entry_points = {}


# ~~~ BEGIN springerle/py-generic-project ~~~
# Stdlib imports
import io
import os
import re
import sys
import json
import textwrap
from collections import defaultdict

# Import setuptools
try:
    from setuptools import setup, find_packages
    from setuptools.command.test import test as TestCommand
except ImportError as exc:
    raise RuntimeError("Cannot install '{0}', setuptools is missing ({1})".format(name, exc))

# Helpers
project_root = os.path.abspath(os.path.dirname(__file__))

def srcfile(*args):
    "Helper for path building."
    return os.path.join(*((project_root,) + args))

class PyTest(TestCommand):
    """pytest integration into setuptool's `test` command."""
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        if 0 and os.environ.get('DH_VIRTUALENV_INSTALL_ROOT', None):
            return  # disable tests during dh-virtualenv build

        # import locally, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        if errno:
            sys.exit(errno)

def _build_metadata(): # pylint: disable=too-many-locals, too-many-branches
    "Return project's metadata as a dict."
    # Handle metadata in package source
    expected_keys = ('url', 'version', 'license', 'author', 'author_email', 'long_description', 'keywords')
    metadata = {}
    with io.open(srcfile('src', package_name, '__init__.py'), encoding='utf-8') as handle:
        pkg_init = handle.read()
        # Get default long description from docstring
        metadata['long_description'] = re.search(r'^"""(.+?)^"""$', pkg_init, re.DOTALL|re.MULTILINE).group(1)
        for line in pkg_init.splitlines():
            match = re.match(r"""^__({0})__ += (?P<q>['"])(.+?)(?P=q)$""".format('|'.join(expected_keys)), line)
            if match:
                metadata[match.group(1)] = match.group(3)

    if not all(i in metadata for i in expected_keys):
        raise RuntimeError("Missing or bad metadata in '{0}' package: {1}"
                           .format(name, ', '.join(sorted(set(expected_keys) - set(metadata.keys()))),))

    text = metadata['long_description'].strip()
    if text:
        metadata['description'], text = text.split('.', 1)
        metadata['description'] = ' '.join(metadata['description'].split()).strip() + '.' # normalize whitespace
        metadata['long_description'] = textwrap.dedent(text).strip()
    metadata['keywords'] = metadata['keywords'].replace(',', ' ').strip().split()

    # Load requirements files
    requirements_files = dict(
        install = 'requirements.txt',
        setup = 'setup-requirements.txt',
        test = 'test-requirements.txt',
    )
    requires = {}
    for key, filename in requirements_files.items():
        requires[key] = []
        if os.path.exists(srcfile(filename)):
            with io.open(srcfile(filename), encoding='utf-8') as handle:
                for line in handle:
                    line = line.strip()
                    if line and not line.startswith('#') and ';' not in line:
                        if any(line.startswith(i) for i in ('-e', 'http://', 'https://')):
                            line = line.split('#egg=')[1]
                        elif line.startswith('http'):
                            line = line.split('#egg=')[1]
                        requires[key].append(line)
    if not any('pytest' == re.split('[\t ,<=>]', i.lower())[0] for i in requires['test']):
        requires['test'].append('pytest') # add missing requirement

    # CLI entry points
    console_scripts = []
    for path, dirs, files in os.walk(srcfile('src', package_name)):
        dirs = [i for i in dirs if not i.startswith('.')]
        if '__main__.py' in files:
            path = path[len(srcfile('src') + os.sep):]
            appname = path.split(os.sep)[-1]
            with io.open(srcfile('src', path, '__main__.py'), encoding='utf-8') as handle:
                for line in handle.readlines():
                    match = re.match(r"""^__app_name__ += (?P<q>['"])(.+?)(?P=q)$""", line)
                    if match:
                        appname = match.group(2)
            console_scripts.append('{0} = {1}.__main__:cli'.format(appname, path.replace(os.sep, '.')))

    # Add some common files to EGG-INFO
    candidate_files = [
        'LICENSE', 'NOTICE',
        'README', 'README.md', 'README.rst', 'README.txt',
        'CHANGES', 'CHANGELOG', 'debian/changelog',
    ]
    data_files = defaultdict(list)
    for filename in candidate_files:
        if os.path.exists(srcfile(filename)):
            data_files['EGG-INFO'].append(filename)

    # Complete project metadata
    classifiers = []
    python_requires = (99, 0)
    for classifiers_txt in ('classifiers.txt', 'project.d/classifiers.txt'):
        classifiers_txt = srcfile(classifiers_txt)
        if os.path.exists(classifiers_txt):
            with io.open(classifiers_txt, encoding='utf-8') as handle:
                for line in handle:
                    if line.strip() and not line.startswith('#'):
                        classifiers.append(line.strip())
                        if line.startswith('Programming Language :: Python :: '):
                            try:
                                major, minor = map(int, line.split('::')[-1].strip().split('.'))
                            except ValueError:
                                pass
                            else:
                                if python_requires > (major, minor):
                                    python_requires = (major, minor)
            break
    if python_requires < (99, 0):
        metadata.setdefault('python_requires', '>={}.{}'.format(*python_requires))
    entry_points.setdefault('console_scripts', []).extend(console_scripts)

    metadata.update(dict(
        name = name,
        package_dir = {'': 'src'},
        packages = find_packages(srcfile('src'), exclude=['tests']),
        data_files = data_files.items(),
        zip_safe = False,
        include_package_data = True,
        install_requires = requires['install'],
        setup_requires = requires['setup'],
        tests_require =  requires['test'],
        classifiers = classifiers,
        cmdclass = dict(
            test = PyTest,
        ),
        entry_points = entry_points,
    ))
    return metadata

# Ensure "setup.py" is importable by other tools, to access the project's metadata
project = _build_metadata()
__all__ = ['project', 'project_root', 'package_name', 'srcfile']
if __name__ == '__main__':
    if '--metadata' in sys.argv[:2]:
        json.dump(project, sys.stdout, default=repr, indent=4, sort_keys=True)
        sys.stdout.write('\n')
    else:
        setup(**project)
