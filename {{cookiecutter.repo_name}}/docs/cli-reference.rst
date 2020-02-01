{%- if "cli" in cookiecutter.features.replace(',', ' ').split() %}
..  Click CLI reference

    Copyright ©  {{ cookiecutter.year }} {{ cookiecutter.full_name }} <{{ cookiecutter.email }}>

    ## LICENSE_SHORT ##
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**********************
Complete CLI Reference
**********************

This is a full reference of the :command:`{{ cookiecutter.repo_name }}` command,
with the same information as you get from using :option:`--help`.
It is generated from source code and thus always up to date.
See :doc:`usage` for a more detailed description.

.. contents:: Available Commands
   :local:

.. click:: {{ cookiecutter.pkg_name }}.__main__:cli
   :prog: {{ cookiecutter.repo_name }}
   :show-nested:
{%- endif %}
