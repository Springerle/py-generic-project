{% if "cli" in cookiecutter.features.replace(',', ' ').split() -%}
# pylint: disable=bad-continuation
""" Configuration utilities.
"""
# Copyright ©  {{ cookiecutter.year }} {{ cookiecutter.full_name }} <{{ cookiecutter.email }}>
#
# ## LICENSE_SHORT ##
import os
import re
import sys
import logging

from rudiments.reamed.click import Configuration  # noqa pylint: disable=unused-import


# Determine path this command is located in (installed to)
try:
    CLI_PATH = sys.modules['__main__'].__file__
except (KeyError, AttributeError):
    CLI_PATH = __file__
CLI_PATH = os.path.dirname(CLI_PATH)
if CLI_PATH.endswith('/bin'):
    CLI_PATH = CLI_PATH[:-4]
elif CLI_PATH.endswith(r'\Scripts'):
    CLI_PATH = CLI_PATH[:-8]
if CLI_PATH.startswith(os.path.expanduser('~') + os.sep):
    CLI_PATH = '~' + CLI_PATH[len(os.path.expanduser('~')):]

VERSION_INFO = '%(prog)s %(version)s from {} [Python {}]'.format(CLI_PATH, ' '.join(sys.version.split()[:1]),)
"""str: Extended version info for use by :py:func:`click.version_option`."""

# These will be filled by `__main__`
APP_NAME = None
"""str: Application name, used e.g. in configuration filenames."""
cli = None  # pylint: disable=invalid-name
""" click.core.Group: The main command object, needed to define sub-commands.
    This is set in :py:mod:`~mam_generic_config.__main__` *before* the
    sub-command modules are imported.
"""
LOG = logging.getLogger()
"""~logging.Logger: The main / default logger."""


def version_info(ctx=None):
    """ Return version information just like --version does.

        Args:
            ctx (~click.Context): The Click context, used to determine
                any dynamic program names when given.

        Returns:
            str: Extended version info based on :py:data:`VERSION_INFO`.
    """
    from . import __version__  # pylint: disable=import-outside-toplevel

    prog = ctx.find_root().info_name if ctx else APP_NAME
    version = __version__
    try:
        import pkg_resources  # pylint: disable=import-outside-toplevel
    except ImportError:
        pass
    else:
        for dist in iter(pkg_resources.working_set):
            scripts = dist.get_entry_map().get('console_scripts') or {}
            for _, entry_point in scripts.items():
                if entry_point.module_name == (__package__ + '.__main__'):
                    version = dist.version
                    break

    return VERSION_INFO % dict(prog=prog, version=version)


def envvar(name, default=None):
    """ Return an environment variable specific for this application (using a prefix).

        Before lookup, any dashes are replaced by underscores, and the name is converted to upper case.

        Args:
            name (str): Name of the variable, without the ``<APP_NAME>_`` prefix.
            default (str): An optional default value.
    """
    varname = (APP_NAME + '-' + name).upper().replace('-', '_')
    return os.environ.get(varname, default)
{% endif -%}
