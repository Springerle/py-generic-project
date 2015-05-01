# py-generic-project

 [![Logo](https://raw.githubusercontent.com/Springerle/py-generic-project/master/docs/img/logo.png)](https://py-generic-project.readthedocs.org/)

A cookiecutter template that creates a basic Python setuptools project,
which can be later on augmented with various optional accessories.
See the [demo](https://github.com/Springerle/py-generic-project/tree/master/demo)
for getting a 1ˢᵗ impression on how this Cookiecutter template can be used,
including screenshots of the terminal session.

 [![Logo](https://raw.github.com/Springerle/springerle.github.io/master/static/img/logo-64.png)](http://springerle.github.io/)
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

The `setup.py` script follows the DRY principle and tries to
minimize repetition of project metadata by loading it from other
places (like the package's `__init__.py`). Incidently, this makes
the script almost identical between different projects, and thus
provides an easy update experience later on. Usually, the only specific
thing in it is the docstring with the project's name and license notice.
This relies on conventions, especially check out
[\_\_init\_\_.py](https://github.com/Springerle/py-generic-project/blob/master/%7B%7Bcookiecutter.repo_name%7D%7D/src/%7B%7Bcookiecutter.pkg_name%7D%7D/__init__.py)
and
[\_\_main\_\_.py](https://github.com/Springerle/py-generic-project/blob/master/%7B%7Bcookiecutter.repo_name%7D%7D/src/%7B%7Bcookiecutter.pkg_name%7D%7D/__main__.py)
in the `src` folder, for their double-underscore meta variables.

It is also importable (by using the usual `if __name__ == '__main__'`
idiom), and exposes the project's setup data in a `project` dict.
This allows other tools to exploit the contained data assembling code,
and again supports the DRY principle. The `rituals` package
uses that to provide Invoke tasks that work for any project, based on
its project metadata.

Other integrated tools are `pylint` for code quality checking,
`pytest` for testing support, and a Travis CI configuration.
To ease writing code that supports both Python 2 _and_ Python 3,
Jinja2's `_compat` module is available in the package, and fitting
``__future__`` imports are placed in every module.
See [Porting to Python 3 Redux](http://lucumr.pocoo.org/2013/5/21/porting-to-python-3-redux/)
for a pragmatic porting guide, based on actual experience.


## Using the Template

### Preparations

In case you don't have the `cookiecutter` command line tool yet, here's
[how to install](https://github.com/Springerle/springerle.github.io#installing-the-cookiecutter-cli) it.

:loudspeaker: | For `py-generic-project` v1.2 and upwards, you need at least `cookiecutter` v1.1, or v1.0 with degraded functionality – for `pipsi` installs, just issue a `pipsi upgrade cookiecutter` command and you're done.
---- | :----


### Project Creation

Creating a new Python project based on this template goes like this (make sure
you're in the directory you want your project added to):

```sh
cookiecutter "https://github.com/Springerle/py-generic-project.git"
```

It's advisable to `git add` the created directory directly afterwards, before any
generated files are added, that you don't want to have in your repository.

:bulb: | To get *your* defaults for common template values `cookiecutter` will ask you for when you use a template, it makes sense to have a [~/.cookiecutterrc](https://github.com/jhermann/ruby-slippers/blob/master/home/.cookiecutterrc) in your home directory. Follow the link to see an example.
---- | :----

You should at least check these files regarding their content and adapt them according to your needs:

 * ``project.d/classifiers.txt`` – Add the correct [categories](http://pypi.python.org/pypi?:action=list_classifiers) (a/k/a Trove classifiers) for your project.
 * ``requirements.txt`` – Add any Python packages you need for your project _at runtime_.

To bootstrap the project (as mentioned, best after `git add`), use these commands from within its directory:

```sh
. .env --yes --develop
inv ci | less -R
"$(basename $(pwd))" --help
```


## Feature Toggles

This template has a few options that can be turned on and off even after initial creation,
which the following terminal session demonstrates for Travis CI support.

![Demo Terminal Session](https://raw.githubusercontent.com/Springerle/py-generic-project/master/docs/img/feature-toggles.png)

At the moment of this writing, those feature are ``travis``, ``flake8``, and ``cli``.
See the ``features`` value in ``cookiecutter.json`` for a current list.

Note that since the whole template is re-created, you should make sure that
you have no pending changes in your working directory, i.e. everything is
either safely committed or stashed away.
After changing ``project.d/cookiecutter.json`` and the call to ``invoke moar-cookies``,
you should look at the diff, and ``git add`` any files that can just be updated (e.g. typically
``.travis.yml``, ``setup.py``, and some others).

Files with considerable changes you have to merge manually, e.g. by dumping a diff, resetting
the affected files, reducing the diffs to the changes you really want, and then applying the edited diff.
Note that the easiest way to do such a reset to the last commit is calling ``git stash && git stash drop``.

Another option is to work with two directories, i.e. clone a copy of your project for the update process,
perform the update, and then selectively copy changes to your main working directory.
There might be a more stream-lined way applying some ``git`` magic, we'll see (ideas are welcome).
Still this is better than wading through commit logs to catch up with an evolving template.


## Split Licensing

Since the files contained in the template itself will comprise the foundation of your project,
they're unlicensed using the “Creative Commons Zero v1.0 Universal” license.
All other files are MIT-licensed – this effectively means you only have to attribute this project
if you re-use all or parts of the contained templating mechanics.

* [![Project License](http://img.shields.io/badge/license-MIT-red.svg)](https://github.com/Springerle/py-generic-project/blob/master/LICENSE_MIT) for the project.
* [![Template License](http://img.shields.io/badge/license-CC0-blue.svg)](https://github.com/Springerle/py-generic-project/blob/master/LICENSE_CC0) for the template proper (everything in `{{cookiecutter.repo_name}}`), unless specified otherwise within the file itself.


## References

**Tools**


* [Cookiecutter](http://cookiecutter.readthedocs.org/en/latest/)
* [PyInvoke](http://www.pyinvoke.org/)
* [pytest](http://pytest.org/latest/contents.html)
* [tox](https://tox.readthedocs.org/en/latest/)
* [Pylint](http://docs.pylint.org/)
* [pypa/setuptools](https://bitbucket.org/pypa/setuptools)
* [pypa/sampleproject](https://github.com/pypa/sampleproject)
* [twine](https://github.com/pypa/twine#twine)
* [autoenv](https://github.com/kennethreitz/autoenv)
* [bpython](http://docs.bpython-interpreter.org/)
* [yolk3k](https://github.com/myint/yolk#yolk)

**Packages**

* [Rituals](https://jhermann.github.io/rituals)
* [Click](http://click.pocoo.org/)

**Similar Archetypes**

* [cookiecutter-pyvanguard](https://github.com/robinandeer/cookiecutter-pyvanguard)
* [cookiecutter-pylibrary](https://github.com/ionelmc/cookiecutter-pylibrary)
* [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage)
* [tony/cookiecutter-pypackage](https://github.com/tony/cookiecutter-pypackage)
* [Nekroze/cookiecutter-pypackage](https://github.com/Nekroze/cookiecutter-pypackage)
* [transcode-de/cookiecutter-django-project](https://github.com/transcode-de/cookiecutter-django-project)
* [mozilla/sugardough](https://github.com/mozilla/sugardough)

* [PyScaffold](https://github.com/blue-yonder/pyscaffold)

See also the full list at [Cookiecutter's README](https://github.com/audreyr/cookiecutter#python).
