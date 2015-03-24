# -*- coding: utf-8 -*-
# pylint: disable=wildcard-import, unused-wildcard-import, bad-continuation
""" Project automation for Invoke.
"""
from __future__ import absolute_import, unicode_literals

import os
import shutil
import tempfile

from invoke import run, task
from rituals.invoke_tasks import * # pylint: disable=redefined-builtin


@task(name='moar-cookies',
    help={
        'mold': "git URL or directory to use for the refresh",
    },
)
def moar_cookies(mold=''):
    """Refresh the project from the original cookiecutter template."""
    mold = mold or "https://github.com/Springerle/py-generic-project.git"
    tmpdir = os.path.join(tempfile.gettempdir(), "moar-{{ cookiecutter.repo_name }}")

    # Make a copy of the new mold version
    if os.path.isdir(tmpdir):
        shutil.rmtree(tmpdir)
    if os.path.exists(mold):
        shutil.copytree(mold, tmpdir, ignore=shutil.ignore_patterns(
            ".git", ".svn", "*~",
        ))
    else:
        run("git clone {} {}".format(mold, tmpdir), echo=True)

    # Copy recorded "cookiecutter.json" into mold
    shutil.copy2("project.d/cookiecutter.json", tmpdir)

    with pushd('..'):
        run("cookiecutter --no-input {}".format(tmpdir), echo=True)
    run("git status", echo=True)


@task
def ci(): # pylint: disable=invalid-name
    """Perform continuous integration tasks."""
    run("invoke clean --all build --docs test check --reports 2>&1")
