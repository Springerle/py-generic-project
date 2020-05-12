# pylint: disable=wildcard-import, unused-wildcard-import, bad-continuation
# pylint: disable=superfluous-parens, redefined-builtin, unused-import
""" Project automation for Invoke.
"""
# Copyright (c) 2015 - 2019 Jürgen Hermann
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
import sys
import shlex
import shutil
import subprocess

from rituals.easy import task, Collection, pushd
from rituals.util import antglob, notify
from rituals.acts.documentation import namespace as _docs

WINDOWS = all(os.getenv(x) for x in ("SYSTEMROOT", "WINDIR"))


@task(help=dict(
    docs="Also clean the documentation build area",
    venv="Include an existing virtualenv (in '.venv')",
    extra="Any extra patterns, space-separated and possibly quoted",
))
def clean(ctx, docs=False, venv=False, extra=''):
    """Perform house-keeping."""
    notify.banner("Cleaning up project files")

    # Add patterns based on given parameters
    venv_dirs = ['.venv']
    patterns = ['new-project/', 'pip-selfcheck.json', '**/*~']
    if docs:
        patterns.append('docs/_build/')
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


@task(pre=[clean])
def test(ctx):
    """Perform integration tests."""
    run = subprocess.check_call if WINDOWS else ctx.run
    run("touch '{{cookiecutter.repo_name}}/empty-testfile'")
    run("pytest")
    run("rm '{{cookiecutter.repo_name}}/empty-testfile'")

    with pushd('new-project'):
        assert not os.path.exists('empty-testfile'), "empty file is removed"

        if any(os.environ.get(x, '').lower() == 'true' for x in {'TRAVIS', 'GITHUB_ACTIONS'}):
            venv_bin = ''
            notify.info("Installing archetype requirements...")
            run("pip --log pip-install.log -q install -r dev-requirements.txt")
            run("invoke --echo --pty ci")
        else:
            venv_bin = '.venv/bin/'
            run("bash -c '. .env --yes && invoke ci'")

        run(venv_bin + "new-project --help")
        run(venv_bin + "new-project --version")
        run(venv_bin + "new-project help")


namespace = Collection.from_module(sys.modules[__name__], name='')
namespace.add_collection(_docs)
