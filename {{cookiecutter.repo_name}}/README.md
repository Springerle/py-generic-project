# {{ cookiecutter.repo_name }}

{{ cookiecutter.short_description }}.

{% if "travis" in cookiecutter.features.replace(',', ' ').split() -%}
 [![Travis CI](https://api.travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.svg)](https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }})
{% endif -%}
 [![GitHub Issues](https://img.shields.io/github/issues/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.svg)]({{ cookiecutter.github_url }}/issues)
 [![License](https://img.shields.io/pypi/l/{{ cookiecutter.repo_name }}.svg)]({{ cookiecutter.github_url }}/blob/master/LICENSE)
 [![Development Status](https://pypip.in/status/{{ cookiecutter.repo_name }}/badge.svg)](https://pypi.python.org/pypi/{{ cookiecutter.repo_name }}/)
 [![Latest Version](https://img.shields.io/pypi/v/{{ cookiecutter.repo_name }}.svg)](https://pypi.python.org/pypi/{{ cookiecutter.repo_name }}/)
 [![Download format](https://pypip.in/format/{{ cookiecutter.repo_name }}/badge.svg)](https://pypi.python.org/pypi/{{ cookiecutter.repo_name }}/)
 [![Downloads](https://img.shields.io/pypi/dw/{{ cookiecutter.repo_name }}.svg)](https://pypi.python.org/pypi/{{ cookiecutter.repo_name }}/)


## Overview

…


## Usage

…


## Contributing

To create a working directory for this project, call these commands:

```sh
git clone "{{ cookiecutter.github_url }}.git"
cd "{{ cookiecutter.repo_name }}"
. .env --yes --develop
invoke build --docs test check
```

See [CONTRIBUTING]({{ cookiecutter.github_url }}/blob/master/CONTRIBUTING.md) for more.


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
