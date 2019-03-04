{{ cookiecutter.repo_name }}
=============================================================================

{{ cookiecutter.short_description }}.

{% if "travis" in cookiecutter.features.replace(',', ' ').split() -%}
 |Travis CI|  |Coveralls| {% endif -%}  |GitHub Issues|  |License|
 |Latest Version|  |Downloads|

.. contents:: **Contents**


Overview
--------

**TODO**


Installation
------------

*{{ cookiecutter.project_name }}* can be installed via
``pip install {{ cookiecutter.repo_name }}`` as usual, see `releases`_
for an overview of available versions. To get a bleeding-edge version
from source, use these commands (ideally within an activated virtualenv):

.. code:: sh

    repo="{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}"
    python3 -m pip install -r "https://raw.githubusercontent.com/$repo/master/requirements.txt"
    python3 -m pip install "https://github.com/$repo/archive/master.zip#egg=${repo#*/}"

See `Contributing`_ on how to create a full development environment.

{%- if "cli" in cookiecutter.features.replace(',', ' ').split() %}

To add bash completion, read the `Click docs`_ about it, or just follow
these instructions:

.. code:: sh

    cmdname={{ cookiecutter.repo_name }}
    mkdir -p ~/.bash_completion.d
    ( export _$(tr a-z- A-Z_ <<<"$cmdname")_COMPLETE=source ; \
      $cmdname >~/.bash_completion.d/$cmdname.sh )
    grep /.bash_completion.d/$cmdname.sh ~/.bash_completion >/dev/null \
        || echo >>~/.bash_completion ". ~/.bash_completion.d/$cmdname.sh"
    . "/etc/bash_completion"
{%- endif %}


Usage
-----

…


Contributing
------------

Contributing to this project is easy, and reporting an issue or adding
to the documentation also improves things for every user. You don’t need
to be a developer to contribute. See `CONTRIBUTING`_ for more.

As a documentation author or developer, to **create a working
directory** for this project, call these commands:

.. code:: sh

    git clone "{{ cookiecutter.github_url }}.git"
    cd "{{ cookiecutter.repo_name }}"
    command . .env --yes --develop
    invoke build --docs test check

For this to work, you might also need to follow some `setup procedures`_
to make the necessary basic commands available on *Linux*, *Mac OS X*,
and *Windows*.

**Running the test suite** can be done several ways, just call
``invoke test`` for a quick check. Run ``invoke test.tox`` for testing
with *all* supported Python versions (if you `have them available`_), or
be more selective by e.g. calling ``invoke test.tox -e py27,py34``.

Use ``invoke check`` to **run a code-quality scan**.

To **start a watchdog that auto-rebuilds documentation** and reloads the
opened browser tab on any change, call ``invoke docs -w -b`` (stop the
watchdog using the ``-k`` option).


Trouble-Shooting
----------------

'pkg-resources not found' or similar during virtualenv creation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you get errors regarding ``pkg-resources`` during the virtualenv
creation, update your build machine's ``pip`` and ``virtualenv``. The
versions on many distros are just too old to handle current
infrastructure (especially PyPI).

This is the one exception to “never sudo pip”, so go ahead and do this:

.. code:: sh

    sudo pip install -U pip virtualenv


References
----------

**Tools**

-  `Cookiecutter`_
-  `PyInvoke`_
-  `pytest`_
-  `tox`_
-  `Pylint`_
-  `twine`_
-  `bpython`_
-  `yolk3k`_

**Packages**

-  `Rituals`_ {%- if "cli" in cookiecutter.features.replace(',', '
   ').split() %}
-  `Click`_ {%- endif %}


Acknowledgements
----------------

…

.. _releases: {{ cookiecutter.github_url }}/releases
.. _Click docs: http://click.pocoo.org/4/bashcomplete/#activation
.. _CONTRIBUTING: {{ cookiecutter.github_url }}/blob/master/CONTRIBUTING.md
.. _setup procedures: https://py-generic-project.readthedocs.io/en/latest/installing.html#quick-setup
.. _have them available: https://github.com/jhermann/priscilla/tree/master/pyenv
.. _Cookiecutter: http://cookiecutter.readthedocs.io/en/latest/
.. _PyInvoke: http://www.pyinvoke.org/
.. _pytest: http://pytest.org/latest/contents.html
.. _tox: https://tox.readthedocs.io/en/latest/
.. _Pylint: http://docs.pylint.org/
.. _twine: https://github.com/pypa/twine#twine
.. _bpython: http://docs.bpython-interpreter.org/
.. _yolk3k: https://github.com/myint/yolk#yolk
.. _Rituals: https://jhermann.github.io/rituals
.. _Click: http://click.pocoo.org/

.. |Travis CI| image:: https://api.travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.svg
   :target: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}
.. |Coveralls| image:: https://img.shields.io/coveralls/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.svg
   :target: https://coveralls.io/r/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}
.. |GitHub Issues| image:: https://img.shields.io/github/issues/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.svg
   :target: {{ cookiecutter.github_url }}/issues
.. |License| image:: https://img.shields.io/pypi/l/{{ cookiecutter.repo_name }}.svg
   :target: {{ cookiecutter.github_url }}/blob/master/LICENSE
.. |Latest Version| image:: https://img.shields.io/pypi/v/{{ cookiecutter.repo_name }}.svg
   :target: https://pypi.python.org/pypi/{{ cookiecutter.repo_name }}/
.. |Downloads| image:: https://img.shields.io/pypi/dw/{{ cookiecutter.repo_name }}.svg
   :target: https://pypi.python.org/pypi/{{ cookiecutter.repo_name }}/
