#! /usr/bin/env python
# pylint: disable=bad-whitespace, superfluous-parens
"""
    Cookiecutter post-gen hook.

    This gets called with no arguments, and with the project directory
    as the working directory. All templates are expanded and copied,
    and the post hook can add, modify, or delete files.

    Copyright (c) 2015 Juergen Hermann

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
"""
import io
import os
import sys
import json
import pprint
import shutil
from collections import OrderedDict
from fnmatch import fnmatchcase as globmatch


VERBOSE = True
DEBUG = bool(os.environ.get('CC_DEBUG_HOOK', 'False'))
NOSCAN_DIRS = set((
    '.git', '.svn', '.hg',
    '.env', '.venv', '.tox',
    'build', 'bin', 'lib', 'local', 'include', 'share', '*.egg-info',
))
KEEP_FILES = set(('__init__.py'))

# Map from short / file name to Trove name
LICENSES = {
    "Apache 2.0": "Apache Software License",
    "Artistic": "Artistic License",
    "BSD 2-clause": "BSD License",
    "BSD 3-clause": "BSD License",
    "BSD ISC": "BSD License",
    "CC0": "License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication",
    "Eclipse": "License :: Other/Proprietary License",
    "GPLv2": "GNU General Public License v2 (GPLv2)",
    "GPLv2+": "GNU General Public License v2 or later (GPLv2+)",
    "GPLv3+": "GNU General Public License v3 or later (GPLv3+)",
    "LGPL v2": "GNU Lesser General Public License v2 (LGPLv2)",
    "LGPL v3": "GNU Lesser General Public License v3 (LGPLv3)",
    "MIT": "MIT License",
    "Mozilla v2.0": "Mozilla Public License 2.0 (MPL 2.0)",
    "Unlicense": "License :: Public Domain",
    "Internal": "License :: Other/Proprietary License",
}
LICENSE_OSI = "License :: OSI Approved :: "
LICENSE_MARKER = "## LICENSE_SHORT ##"
LICENSE_TROVE = "## LICENSE_TROVE ##"


def get_context():
    """Return context as a dict."""
    cookiecutter = None  # Make pylint happy
    return {{ cookiecutter | pprint }}


def walk_project():
    """Yield all files in the created project."""
    for path, dirs, files in os.walk(os.getcwd()):
        for dirname in dirs[:]:
            if any(globmatch(dirname, i) for i in NOSCAN_DIRS):
                dirs.remove(dirname)
        # sys.stderr.write(repr((files, dirs, path)) + '\n'); continue

        for filename in files:
            yield os.path.join(path, filename)


def replace_marker(filepath, marker, lines):
    """Replace given marker with provides lines."""
    # Read source file
    with io.open(filepath, 'r', encoding='utf-8') as handle:
        source_lines = handle.readlines()

    # Replace marker, and use any text before it as an indent string
    changed = False
    for idx, line in enumerate(source_lines):
        if line.rstrip().endswith(marker):
            line = line.rstrip().replace(marker, '')
            source_lines[idx] = '\n'.join((line + i).rstrip() for i in lines) + '\n'
            changed = True

    if changed:
        # Write back modified source
        with io.open(filepath, 'w', encoding='utf-8') as handle:
            handle.writelines(source_lines)

    return changed


def dump_context(context, filename):
    """Dump JSON context to given file."""
    with io.open(filename, 'w', encoding='ascii') as handle:
        data = json.dumps(context, indent=4, sort_keys=True, ensure_ascii=True)
        data = '\n'.join([i.rstrip() for i in data.splitlines()])
        handle.write(data + '\n')


def prune_empty_files():
    """ Prune any empty files left over from switched off features.

        Empty in this case also means "has just 1 or 2 bytes".
    """
    for filepath in walk_project():
        if os.path.getsize(filepath) <= 2 and os.path.basename(filepath) not in KEEP_FILES:
            if VERBOSE:
                sys.stderr.write("Removing {} byte sized '{}'...\n".format(
                    os.path.getsize(filepath), filepath
                ))
            os.unlink(filepath)


def copy_license(name):
    """Copy license file."""
    repo_dir = os.getcwd()
    filename = os.path.join(repo_dir, 'licenses.in', name.replace(' ', '_') + '.txt')
    trove_name = LICENSES.get(name, None)
    if trove_name:  # Known license?
        if '::' not in trove_name:
            trove_name = LICENSE_OSI + trove_name

        # Write main LICENSE file
        if VERBOSE:
            sys.stderr.write("Writing license file for '{}'... [{}]\n".format(name, trove_name,))
        shutil.copyfile(filename, "LICENSE")

        # Read in short license form for source files
        filename_short = os.path.join(repo_dir, 'licenses.in', 'short', name.replace(' ', '_') + '.txt')
        with io.open(filename_short, 'r', encoding='utf-8') as handle:
            license_short = handle.readlines()

        # Iterate over files and insert license notices
        count = 0
        for filepath in walk_project():
            if os.path.basename(filepath) == 'classifiers.txt':
                if replace_marker(filepath, LICENSE_TROVE, [trove_name + '\n']):
                    count += 1
            elif filepath.endswith('.py'):
                if replace_marker(filepath, LICENSE_MARKER, license_short):
                    count += 1

        if VERBOSE:
            sys.stderr.write("Rewrote {} source files with a license notice added.\n".format(count,))
    elif VERBOSE:
        sys.stderr.write("Unknown license '{}', I know about: {}\n".format(
            name, ', '.join(sorted(LICENSES.keys())),
        ))

    shutil.rmtree(os.path.join(repo_dir, 'licenses.in'))


def run():
    """Main loop."""
    Undefined = None # pylint: disable=invalid-name, unused-variable

    context = get_context()
    dump_context(context, 'project.d/cookiecutter.json')
    prune_empty_files()
    copy_license(context['license'])


if __name__ == '__main__':
    run()
