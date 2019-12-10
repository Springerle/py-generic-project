{% if "cli" in cookiecutter.features.replace(',', ' ').split() -%}
# pylint: disable=bad-continuation
""" Command line interface.
"""
# Copyright ©  {{ cookiecutter.year }} {{ cookiecutter.full_name }} <{{ cookiecutter.email }}>
#
# ## LICENSE_SHORT ##
import re
import time
import logging

import click
from munch import Munch as Bunch

from . import config
from .util import misc


# Default name of the app, and its app directory
__app_name__ = '{{ cookiecutter.repo_name }}'
config.APP_NAME = __app_name__

# The `click` custom context settings
CONTEXT_SETTINGS = dict(
    obj=Bunch(cfg=None, log=None, quiet=False, verbose=False),  # namespace for custom stuff
    help_option_names=['-h', '--help'],
    auto_envvar_prefix=__app_name__.upper().replace('-', '_'),
)


# `--license` option decorator
def license_option(*param_decls, **attrs):
    """``--license`` option that prints license information and then exits."""
    def decorator(func):
        "decorator inner wrapper"
        def callback(ctx, _dummy, value):
            "click option callback"
            if not value or ctx.resilient_parsing:
                return

            from . import __doc__ as license_text
            license_text = re.sub(r"``([^`]+?)``", lambda m: click.style(m.group(1), bold=True), license_text)
            click.echo(license_text)
            ctx.exit()

        attrs.setdefault('is_flag', True)
        attrs.setdefault('expose_value', False)
        attrs.setdefault('is_eager', True)
        attrs.setdefault('help', 'Show the license and exit.')
        attrs['callback'] = callback
        return click.option(*(param_decls or ('--license',)), **attrs)(func)

    return decorator


def init_logging(ctx, json_log):
    """Initialize logging subsystem."""
    import json_logging  # pylint: disable=import-outside-toplevel

    log_level = logging.WARNING if ctx.obj.quiet else logging.DEBUG if ctx.obj.verbose else logging.INFO
    logging.basicConfig(level=log_level)
    if json_log:
        json_logging.ENABLE_JSON_LOGGING = True
    json_logging._logger.setLevel(logging.ERROR)  # get rid of ugly warning  pylint: disable=protected-access
    json_logging.init_non_web()
    json_logging.config_root_logger()
    json_logging._logger.setLevel(logging.INFO)  # pylint: disable=protected-access

    ctx.obj.log = misc.make_logger(ctx.info_name)
    ctx.obj.log.setLevel(log_level)


# Main command (root)
@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option(message=config.VERSION_INFO)
@license_option()
@click.option('-q', '--quiet', is_flag=True, default=False, help='Be quiet (show only errors).')
@click.option('-v', '--verbose', is_flag=True, default=False, help='Create extra verbose output.')
@click.option('-J', '--json-log', is_flag=True, default=False, help='Enforce JSON logging.')
@click.option('-c', '--config', "config_paths", metavar='FILE',
              multiple=True, type=click.Path(), help='Load given configuration file(s).')
@click.pass_context
def cli(ctx, quiet=False, verbose=False, json_log=False, config_paths=None):  # pylint: disable=unused-argument
    """'{{ cookiecutter.repo_name }}' command line tool."""
    def log_runtime():
        "Log total runtime."
        if ctx.obj.log:
            ctx.obj.log.info('Execution took {:.2f}s'.format(time.time() - ctx.obj.startup))

    ctx.obj.startup = time.time()
    if verbose:
        ctx.call_on_close(log_runtime)

    ctx.obj.quiet = quiet
    ctx.obj.verbose = verbose
    init_logging(ctx, json_log)

    config.Configuration.from_context(ctx, config_paths)


# Import sub-commands to define them AFTER `cli` is defined
config.cli = cli
from . import commands as _  # noqa pylint: disable=unused-import, wrong-import-position

if __name__ == "__main__":  # imported via "python -m"?
    __package__ = '{{ cookiecutter.pkg_name }}'  # pylint: disable=redefined-builtin
    cli()  # pylint: disable=no-value-for-parameter
{% endif -%}
