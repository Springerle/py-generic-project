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
import shlex
import shutil

from invoke import run, task
from rituals.invoke_tasks import help, pushd
from rituals.util import antglob, notify


@task(help=dict(
    venv="Include an existing virtualenv (in '.venv')",
    extra="Any extra patterns, space-separated and possibly quoted",
))
def clean(venv=False, extra=''): # pylint: disable=redefined-builtin
    """Perform house-keeping."""
    notify.banner("Cleaning up project files")

    # Add patterns based on given parameters
    venv_dirs = ['.venv']
    patterns = ['new-project/', 'pip-selfcheck.json', '**/*~']
    if venv:
        patterns.extend([i + '/' for i in venv_dirs])
    if extra:
        patterns.extend(shlex.split(extra))

    # Build fileset
    patterns = [antglob.includes(i) for i in patterns]
    if not venv:
        # Do not scan venv dirs when not cleaning them
        patterns.extend([antglob.excludes(i + '/') for i in venv_dirs])
    fileset = antglob.FileSet('.', patterns)

    # Iterate over matches and remove them
    for name in fileset:
        notify.info('rm {0}'.format(name))
        if name.endswith('/'):
            shutil.rmtree(name)
        else:
            os.unlink(name)


@task
def test():
    """Perform integration tests."""
    sh = lambda cmd: run(cmd, echo=True)
    sh("py.test")

    with pushd('new-project'):
        if os.environ.get('TRAVIS', '') == 'true':
            notify.info("Installing archetype requirements...")
            sh("pip --log pip-install.log -q install -r dev-requirements.txt")
            sh("invoke ci")
        else:
            sh("bash -c '. .env --yes && invoke ci'")

        sh("new-project --help")
        sh("new-project --version")
        sh("new-project help")
