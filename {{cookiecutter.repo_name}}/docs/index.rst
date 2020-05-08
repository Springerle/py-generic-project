..  documentation master file

    Copyright ©  {{ cookiecutter.year }} {{ cookiecutter.full_name }} <{{ cookiecutter.email }}>

    ## LICENSE_SHORT ##
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#############################################################################
Welcome to the “{{ cookiecutter.project_name }}” manual!
#############################################################################

.. image:: _static/img/logo.png

{{ cookiecutter.short_description }}.


**********
Installing
**********

*{{ cookiecutter.project_name }}* can be installed from PyPI
via ``pip install {{ cookiecutter.repo_name }}`` as usual,
see `releases <{{ cookiecutter.repo_url }}/releases>`_
on GitHub for an overview of available versions – the project uses
`semantic versioning <http://semver.org/>`_ and follows
`PEP 440 <https://www.python.org/dev/peps/pep-0440/>`_ conventions.
If no releases are available yet, install from source as described right below.

To get a bleeding-edge version from source, use these commands:

.. code-block:: shell

    repo="{{ cookiecutter.git_username }}/{{ cookiecutter.repo_name }}"
    python3 -m venv ~/.local/venvs/{{ cookiecutter.repo_name }} && . $_/bin/activate
    python3 -m pip install -r "https://raw.githubusercontent.com/$repo/master/requirements.txt"
    python3 -m pip install -e "git+https://github.com/$repo.git#egg=${repo#*/}"
{%- if "cli" in cookiecutter.features.replace(',', ' ').split() %}
    ln -nfs ../.local/venvs/{{ cookiecutter.repo_name }}/bin/{{ cookiecutter.repo_name }} ~/.local/bin
{%- endif %}

See the following section on how to create a full development environment.

{%- if "cli" in cookiecutter.features.replace(',', ' ').split() %}

To add bash completion, read the
`Click docs <http://click.pocoo.org/4/bashcomplete/#activation>`_
about it, or just follow these instructions:

.. code-block:: shell

    cmdname={{ cookiecutter.repo_name }}
    mkdir -p ~/.bash_completion.d
    ( export _$(tr a-z- A-Z_ <<<"$cmdname")_COMPLETE=source ; \
      $cmdname >~/.bash_completion.d/$cmdname.sh )
    grep /.bash_completion.d/$cmdname.sh ~/.bash_completion >/dev/null \
        || echo >>~/.bash_completion ". ~/.bash_completion.d/$cmdname.sh"
    . "/etc/bash_completion"
{%- endif %}

After installation, continue with :doc:`usage`.


************
Contributing
************

To create a working directory for this project, call these commands:

.. code-block:: shell

    git clone "{{ cookiecutter.repo_url }}.git"
    cd "{{ cookiecutter.repo_name }}"
    . .env --yes --develop
    invoke build --docs test check

Contributing to this project is easy, and reporting an issue or
adding to the documentation also improves things for every user.
You don’t need to be a developer to contribute.
See :doc:`CONTRIBUTING` for more.


**********************
Documentation Contents
**********************

.. toctree::
    :maxdepth: 4

    usage
{%- if "cli" in cookiecutter.features.replace(',', ' ').split() %}
    cli-reference
{%- endif %}
    api-reference
    CONTRIBUTING
    LICENSE


**********
References
**********

Tools
=====

-  `Cookiecutter <https://cookiecutter.readthedocs.io/en/latest/>`_
-  `PyInvoke <http://www.pyinvoke.org/>`_
-  `pytest <http://pytest.org/latest/contents.html>`_
-  `tox <https://tox.readthedocs.io/en/latest/>`_
-  `Pylint <http://docs.pylint.org/>`_
-  `twine <https://github.com/pypa/twine#twine>`_
-  `bpython <http://docs.bpython-interpreter.org/>`_
-  `yolk3k <https://github.com/myint/yolk#yolk>`_

Packages
========

-  `Rituals <https://jhermann.github.io/rituals>`_
{%- if "cli" in cookiecutter.features.replace(',', ' ').split() %}
-  `Click <http://click.pocoo.org/>`_
{%- endif %}


Indices and Tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
