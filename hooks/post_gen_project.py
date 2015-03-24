#! /usr/bin/env python
# -*- coding: utf-8 -*-
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
from __future__ import absolute_import, unicode_literals, print_function

import io
import os
import sys
import json
import pprint
from fnmatch import fnmatchcase as globmatch


VERBOSE = True
DEBUG = False
NOSCAN_DIRS = set((
    '.git', '.svn', '.hg',
    '.env', '.venv', '.tox',
    'build', 'bin', 'lib', 'local', 'include', 'share', '*.egg-info',
))
KEEP_FILES = set(('__init__.py'))


def get_context():
    """Return context as a dict."""
    cookiecutter = None  # Make pylint happy
    return {{ cookiecutter | pprint }}


def dump_context(context, filename):
    """Dump JSON context to given file."""
    with io.open(filename, 'w', encoding='ascii') as handle:
        data = json.dumps(context, indent=4, sort_keys=True, ensure_ascii=True)
        handle.write(data + '\n')


def prune_empty_files():
    """ Prune any empty files left over from switched off features.

        Empty in this case also means "has just 1 or 2 bytes".
    """
    for path, dirs, files in os.walk(os.getcwd()):
        for dirname in dirs[:]:
            if any(globmatch(dirname, i) for i in NOSCAN_DIRS):
                dirs.remove(dirname)
        # sys.stderr.write(repr((files, dirs, path)) + '\n'); continue

        for filename in files:
            filepath = os.path.join(path, filename)
            if os.path.getsize(filepath) <= 2 and filename not in KEEP_FILES:
                if VERBOSE:
                    sys.stderr.write("Removing {} byte sized '{}'...\n".format(
                        os.path.getsize(filepath), filepath
                    ))
                os.unlink(filepath)


def run():
    """Main loop."""
    context = get_context()
    dump_context(context, 'project.d/cookiecutter.json')
    prune_empty_files()


if __name__ == '__main__':
    run()
