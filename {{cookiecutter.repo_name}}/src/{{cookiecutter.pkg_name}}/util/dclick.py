{% if "cli" in cookiecutter.features.replace(',', ' ').split() -%}
# -*- coding: utf-8 -*-
# pylint: disable=bad-continuation
""" ‘Double Click’ – Extensions to Click.
"""
# Copyright ©  {{ cookiecutter.year }} {{ cookiecutter.full_name }} <{{ cookiecutter.email }}>
#
# ## LICENSE_SHORT ##
from __future__ import absolute_import, unicode_literals, print_function

import os
import re

import click


def pretty_path(path, _home_re=re.compile('^' + re.escape(os.path.expanduser('~') + os.sep))):
    """Prettify path for humans, and make it Unicode."""
    path = click.format_filename(path)
    path = _home_re.sub('~' + os.sep, path)
    return path


def serror(message, *args, **kwargs):
    """Print a styled error message."""
    if args or kwargs:
        message = message.format(*args, **kwargs)
    return click.secho(message, fg='white', bg='red', bold=True)


class LoggedFailure(click.UsageError):
    """Report a failure condition to the user."""

    def __init__(self, message):
        message = click.style(message, fg='white', bg='red', bold=True)
        click.UsageError.__init__(self, message)


class AliasedGroup(click.Group):
    """ A command group with alias names.

        Inherit from this class and define a ``MAP`` class variable,
        which is a mapping from alias names to canonical command names.
        Then use that derived class as the ``cls`` parameter for a
        ``click.group`` decorator.
    """

    MAP = {}

    def get_command(self, ctx, cmd_name):
        """Map some aliases to their 'real' names."""
        cmd_name = self.MAP.get(cmd_name, cmd_name)
        return click.Group.get_command(self, ctx, cmd_name)
{% endif -%}
