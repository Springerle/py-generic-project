{% if "cli" in cookiecutter.features.replace(',', ' ').split() -%}
# pylint: disable=unused-import
""" Implementation of CLI sub-commands.
"""
# Copyright ©  {{ cookiecutter.year }} {{ cookiecutter.full_name }} <{{ cookiecutter.email }}>
#
# ## LICENSE_SHORT ##

# Load the command modules for registration
from . import help  # noqa pylint: disable=redefined-builtin
{% endif -%}
