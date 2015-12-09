{% if "cli" in cookiecutter.features.replace(',', ' ').split() -%}
# -*- coding: utf-8 -*-
# pylint: disable=bad-continuation
""" Configuration utilities.
"""
# Copyright ©  {{ cookiecutter.year }} {{ cookiecutter.full_name }} <{{ cookiecutter.email }}>
#
# ## LICENSE_SHORT ##
from __future__ import absolute_import, unicode_literals, print_function

import os
import re
import sys

from rudiments.reamed.click import Configuration  # noqa pylint: disable=unused-import

from ._compat import iteritems

# Determine path this command is located in (installed to)
try:
    CLI_PATH = sys.modules['__main__'].__file__
except (KeyError, AttributeError):
    CLI_PATH = __file__
CLI_PATH = os.path.dirname(CLI_PATH)
if CLI_PATH.endswith('/bin'):
    CLI_PATH = CLI_PATH[:-4]
CLI_PATH = re.sub('^' + os.path.expanduser('~'), '~', CLI_PATH)

# Extended version info for use by `click.version_option`
VERSION_INFO = '%(prog)s %(version)s from {} [Python {}]'.format(CLI_PATH, ' '.join(sys.version.split()[:1]),)

# These will be filled by `__main__`
APP_NAME = None
cli = None  # pylint: disable=invalid-name


def version_info(ctx=None):
    """Return version information just like --version does."""
    from . import __version__

    prog = ctx.find_root().info_name if ctx else APP_NAME
    version = __version__
    try:
        import pkg_resources
    except ImportError:
        pass
    else:
        for dist in iter(pkg_resources.working_set):
            scripts = dist.get_entry_map().get('console_scripts') or {}
            for _, entry_point in iteritems(scripts):
                if entry_point.module_name == (__package__ + '.__main__'):
                    version = dist.version
                    break

    return VERSION_INFO % dict(prog=prog, version=version)


def envvar(name, default=None):
    """Return an environment variable specific for this application (using a prefix)."""
    varname = (APP_NAME + '-' + name).upper().replace('-', '_')
    return os.environ.get(varname, default)
{% endif -%}
