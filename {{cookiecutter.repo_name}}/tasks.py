# -*- coding: utf-8 -*-
# pylint: disable=wildcard-import, unused-wildcard-import, bad-continuation
""" Project automation for Invoke.
"""
# Copyright ©  {{ cookiecutter.year }} {{ cookiecutter.full_name }} <{{ cookiecutter.email }}>
#
# ## LICENSE_SHORT ##
from __future__ import absolute_import, unicode_literals

import os
import shutil
import tempfile

from rituals.easy import *  # pylint: disable=redefined-builtin


@task(name='fresh-cookies',
    help={
        'mold': "git URL or directory to use for the refresh",
    },
)
def fresh_cookies(ctx, mold=''):
    """Refresh the project from the original cookiecutter template."""
    mold = mold or "https://github.com/Springerle/py-generic-project.git"  # TODO: URL from config
    tmpdir = os.path.join(tempfile.gettempdir(), "cc-upgrade-{{ cookiecutter.repo_name }}")

    if os.path.isdir('.git'):
        # TODO: Ensure there are no local unstashed changes
        pass

    # Make a copy of the new mold version
    if os.path.isdir(tmpdir):
        shutil.rmtree(tmpdir)
    if os.path.exists(mold):
        shutil.copytree(mold, tmpdir, ignore=shutil.ignore_patterns(
            ".git", ".svn", "*~",
        ))
    else:
        ctx.run("git clone {} {}".format(mold, tmpdir))

    # Copy recorded "cookiecutter.json" into mold
    shutil.copy2("project.d/cookiecutter.json", tmpdir)

    with pushd('..'):
        ctx.run("cookiecutter --no-input {}".format(tmpdir))
    if os.path.exists('.git'):
        ctx.run("git status")

namespace.add_task(fresh_cookies)


@task
def ci(ctx):
    """Perform continuous integration tasks."""
    opts = ['']

    # 'tox' makes no sense in Travis
    if os.environ.get('TRAVIS', '').lower() == 'true':
        opts += ['test.pytest']
    else:
        opts += ['test.tox']

    ctx.run("invoke --echo --pty clean --all build --docs check --reports{}".format(' '.join(opts)))

namespace.add_task(ci)
