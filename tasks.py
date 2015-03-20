# *- coding: utf-8 -*-
# pylint: disable=wildcard-import, unused-wildcard-import, bad-continuation, superfluous-parens
""" Project automation for Invoke.
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

import os
import shutil

from invoke import run, task
#from rituals.invoke_tasks import * # pylint: disable=redefined-builtin


@task
def test():
    """Perform integration test."""
    run("cookiecutter --no-input . 2>&1")

    new_project = 'new-project'
    init_py = '{0}/src/{1}/__init__.py'.format(new_project, new_project.replace('-', '_'))
    try:
        assert os.path.exists(new_project), "Project was created"
        assert os.path.isdir(new_project), "Project base directory was created"
        assert os.path.isfile(init_py), "Project package was created"
        with open(new_project + '/README.md') as handle:
            assert "https://github.com/jhermann/new-project" in handle.read(), "README contains repo URL"
    except AssertionError as exc:
        print("FAILURE: {}".format(exc))
        print("'{}' directory was kept for introspection!".format(new_project))
    else:
        print("ALL OK!")
        shutil.rmtree(new_project)
