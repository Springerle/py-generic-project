# *- coding: utf-8 -*-
# pylint: disable=
""" Test the template.
"""
# Copyright (c) 2015 Jürgen Hermann
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
from __future__ import absolute_import, unicode_literals

import os
from codecs import open


def test_project_base(project):
    """Test the created project base dir."""
    assert os.path.exists(project), "Project was created"
    assert os.path.isdir(project), "Project base directory was created"


def test_src_package(project):
    """Test the created project package source."""
    pkg_name = os.path.basename(project).replace('-', '_')
    init_py = '{0}/src/{1}/__init__.py'.format(project, pkg_name)

    assert os.path.isfile(init_py), "Project package was created"


def test_readme(project):
    """Test the README contents."""
    with open(project + '/README.md', encoding='utf-8') as handle:
        readme = handle.read()

    # TODO: cookiecutter needs a --no-rc option, so we'll always get 'jschmoe'
    assert any("https://github.com/{}/new-project".format(i) in readme
        for i in ('jschmoe', 'jhermann')), "README contains repo URL"
    assert readme.endswith('\n'), "README has the newline at end of file"
