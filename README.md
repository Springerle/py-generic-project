# py-generic-project

 [![Logo](https://raw.githubusercontent.com/Springerle/py-generic-project/master/docs/_static/img/logo.png)](https://py-generic-project.readthedocs.io/)

A cookiecutter template that creates a basic Python setuptools project,
which can be later on augmented with various optional accessories.
See the [demo](https://github.com/Springerle/py-generic-project/tree/master/demo)
for getting a 1ˢᵗ impression on how this Cookiecutter template can be used,
including screenshots of the terminal session.

 [![Logo](https://raw.github.com/Springerle/py-generic-project/master/docs/_static/img/springerle-logo.png)](http://springerle.github.io/)
 [![Groups](https://img.shields.io/badge/Google_groups-springerle--users-orange.svg)](https://groups.google.com/forum/#!forum/springerle-users)
 ![MIT+CC0 licensed](http://img.shields.io/badge/license-MIT+CC0-red.svg)
 [![Travis CI](https://api.travis-ci.org/Springerle/py-generic-project.svg)](https://travis-ci.org/Springerle/py-generic-project)
 [![GitHub Issues](https://img.shields.io/github/issues/Springerle/py-generic-project.svg)](https://github.com/Springerle/py-generic-project/issues)
 [![GitHub Release](https://img.shields.io/github/release/Springerle/py-generic-project.svg)](https://github.com/Springerle/py-generic-project/releases)


## Features

The resulting project uses
[rituals](https://github.com/jhermann/rituals)
and [invoke](https://github.com/pyinvoke/invoke/)
for task automation, and
[setuptools](https://bitbucket.org/pypa/setuptools)
for building and distributing the project.
A provided [autoenv](https://github.com/kennethreitz/autoenv) script takes care
of creating a fully boot-strapped `virtualenv` – it can also be used manually
if you don't want to install `autoenv`.

Other integrated tools are `pylint` for code quality checking,
`pytest` for testing support, and a Travis CI configuration.
To ease writing code that supports both Python 2 _and_ Python 3,
Jinja2's `_compat` module is available in the package, and fitting
``__future__`` imports are placed in every module.
See [Porting to Python 3 Redux](http://lucumr.pocoo.org/2013/5/21/porting-to-python-3-redux/)
for a pragmatic porting guide, based on actual experience.

:books: | Get to know all the details on [Read The Docs](https://py-generic-project.readthedocs.io/).
----: | :----


## Split Licensing

Since the files contained in the ``{{cookiecutter.repo_name}}`` archetype itself
will comprise the foundation of your project, they're unlicensed using the
“Creative Commons Zero v1.0 Universal” license.
All other files outside the ``{{cookiecutter.repo_name}}`` directory are
MIT-licensed – this effectively means you only have to attribute this project
if you re-use all or parts of the contained templating mechanics and documentation.

* [![Project License](http://img.shields.io/badge/license-MIT-red.svg)](https://github.com/Springerle/py-generic-project/blob/master/LICENSE_MIT) for the project.
* [![Template License](http://img.shields.io/badge/license-CC0-blue.svg)](https://github.com/Springerle/py-generic-project/blob/master/LICENSE_CC0) for the template proper (everything in `{{cookiecutter.repo_name}}`), unless specified otherwise within the file itself.


## References

**Similar Archetypes**

* [cookiecutter-pyvanguard](https://github.com/robinandeer/cookiecutter-pyvanguard)
* [cookiecutter-pylibrary](https://github.com/ionelmc/cookiecutter-pylibrary)
* [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage)
* [tony/cookiecutter-pypackage](https://github.com/tony/cookiecutter-pypackage)
* [Nekroze/cookiecutter-pypackage](https://github.com/Nekroze/cookiecutter-pypackage)
* [darvid/cookiecutter-pylibng](https://github.com/darvid/cookiecutter-pylibng)
* [transcode-de/cookiecutter-django-project](https://github.com/transcode-de/cookiecutter-django-project)
* [mozilla/sugardough](https://github.com/mozilla/sugardough)

* [PyScaffold](https://github.com/blue-yonder/pyscaffold)
* [weber-minimal](https://github.com/vmalloc/weber-minimal) – A Flask application skeleton with Ansible deployment.

See also the full list at [Cookiecutter's README](https://github.com/audreyr/cookiecutter#python).
