# {{ cookiecutter.repo_name }}

{{ cookiecutter.short_description }}.

{% if "travis" in cookiecutter.features.replace(',', ' ').split() -%}
 [![Travis CI](https://api.travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.svg)](https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }})
 [![Coveralls](https://img.shields.io/coveralls/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.svg)](https://coveralls.io/r/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }})
{% endif -%}
 [![GitHub Issues](https://img.shields.io/github/issues/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.svg)]({{ cookiecutter.github_url }}/issues)
 [![License](https://img.shields.io/pypi/l/{{ cookiecutter.repo_name }}.svg)]({{ cookiecutter.github_url }}/blob/master/LICENSE)
 [![Development Status](https://pypip.in/status/{{ cookiecutter.repo_name }}/badge.svg)](https://pypi.python.org/pypi/{{ cookiecutter.repo_name }}/)
 [![Latest Version](https://img.shields.io/pypi/v/{{ cookiecutter.repo_name }}.svg)](https://pypi.python.org/pypi/{{ cookiecutter.repo_name }}/)
 [![Download format](https://pypip.in/format/{{ cookiecutter.repo_name }}/badge.svg)](https://pypi.python.org/pypi/{{ cookiecutter.repo_name }}/)
 [![Downloads](https://img.shields.io/pypi/dw/{{ cookiecutter.repo_name }}.svg)](https://pypi.python.org/pypi/{{ cookiecutter.repo_name }}/)


## Overview

…


## Installation

*{{ cookiecutter.project_name }}* can be installed via ``pip install {{ cookiecutter.repo_name }}`` as usual,
see [releases]({{ cookiecutter.github_url }}/releases) for an overview of available versions.
To get a bleeding-edge version from source, use these commands:

```sh
repo="{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}"
pip install -r "https://raw.githubusercontent.com/$repo/master/requirements.txt"
pip install -UI -e "git+https://github.com/$repo.git#egg=${repo#*/}"
```

See [Contributing](#contributing) on how to create a full development environment.

{%- if "cli" in cookiecutter.features.replace(',', ' ').split() %}

To add bash completion, read the [Click docs](http://click.pocoo.org/4/bashcomplete/#activation) about it,
or just follow these instructions:

```sh
cmdname={{ cookiecutter.repo_name }}
mkdir -p ~/.bash_completion.d
( export _$(tr a-z- A-Z_ <<<"$cmdname")_COMPLETE=source ; \
  $cmdname >~/.bash_completion.d/$cmdname.sh )
grep /.bash_completion.d/$cmdname.sh ~/.bash_completion >/dev/null \
    || echo >>~/.bash_completion ". ~/.bash_completion.d/$cmdname.sh"
. "/etc/bash_completion"
```
{%- endif %}


## Usage

…


## Contributing

Contributing to this project is easy, and reporting an issue or
adding to the documentation also improves things for every user.
You don’t need to be a developer to contribute.
See [CONTRIBUTING]({{ cookiecutter.github_url }}/blob/master/CONTRIBUTING.md) for more.

As a documentation author or developer,
to **create a working directory** for this project,
call these commands:

```sh
git clone "{{ cookiecutter.github_url }}.git"
cd "{{ cookiecutter.repo_name }}"
. .env --yes --develop
invoke build --docs test check
```

You might also need to follow some
[setup procedures](https://py-generic-project.readthedocs.org/en/latest/installing.html#quick-setup)
to make the necessary basic commands available on *Linux*, *Mac OS X*, and *Windows*.

**Running the test suite** can be done several ways, just call ``invoke test`` for a quick check,
or ``invoke test.tox`` for testing with all supported Python versions
(if you [have them available](https://github.com/jhermann/priscilla/tree/master/pyenv)).
Use ``invoke check`` to **run a code-quality scan**.

To **start a watchdog that auto-rebuilds documentation** and reloads the opened browser tab on any change,
call ``invoke docs -w -b`` (stop the watchdog using the ``-k`` option).


## References

**Tools**

* [Cookiecutter](http://cookiecutter.readthedocs.org/en/latest/)
* [PyInvoke](http://www.pyinvoke.org/)
* [pytest](http://pytest.org/latest/contents.html)
* [tox](https://tox.readthedocs.org/en/latest/)
* [Pylint](http://docs.pylint.org/)
* [twine](https://github.com/pypa/twine#twine)
* [bpython](http://docs.bpython-interpreter.org/)
* [yolk3k](https://github.com/myint/yolk#yolk)

**Packages**

* [Rituals](https://jhermann.github.io/rituals)
{%- if "cli" in cookiecutter.features.replace(',', ' ').split() %}
* [Click](http://click.pocoo.org/)
{%- endif %}


## Acknowledgements

…
