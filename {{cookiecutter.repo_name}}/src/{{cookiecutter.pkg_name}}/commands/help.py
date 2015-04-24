{% if "cli" in cookiecutter.features.replace(',', ' ').split() -%}
# -*- coding: utf-8 -*-
# pylint: disable=bad-continuation, too-few-public-methods
""" 'help' command.
"""
# Copyright ©  {{ cookiecutter.year }} {{ cookiecutter.full_name }} <{{ cookiecutter.email }}>
#
# ## LICENSE_SHORT ##
from __future__ import absolute_import, unicode_literals, print_function

import os
import sys

from rudiments.reamed import click

from .. import config


@config.cli.command(name='help')
@click.option('-c', '--config-dump', is_flag=True, default=False, help='Dump the merged configuration to stdout.')
@click.pass_context
def help_command(ctx, config_dump=False):
    """Print some information on the system environment."""
    def banner(title):
        "Helper"
        click.echo('')
        click.secho('~~~ {} ~~~'.format(title), fg='green', bg='black', bold=True)

    if config_dump:
        ctx.obj.cfg.dump()
        sys.exit(0)

    app_name = ctx.find_root().info_name
    click.secho('*** "{}" Help & Information ***'.format(app_name), fg='white', bg='blue', bold=True)

    banner('Version Information')
    click.echo(config.version_info(ctx))

    banner('Configuration')
    locations = ctx.obj.cfg.locations(exists=False)
    locations = [(u'✔' if os.path.exists(i) else u'✘', click.pretty_path(i)) for i in locations]
    click.echo(u'The following configuration files are merged in order, if they exist:\n    {0}'.format(
        u'\n    '.join(u'{}   {}'.format(*i) for i in locations),
    ))

    banner('More Help')
    click.echo("Call '{} --help' to get a list of available commands & options.".format(app_name))
    click.echo("Call '{} «command» --help' to get help on a specific command.".format(app_name))
    click.echo("Call '{} --version' to get the above version information separately.".format(app_name))
    click.echo("Call '{} --license' to get licensing informatioon.".format(app_name))

    # click.echo('\ncontext = {}'.format(repr(vars(ctx))))
    # click.echo('\nparent = {}'.format(repr(vars(ctx.parent))))
{% endif -%}
