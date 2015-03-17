py-generic-project
==================

A cookiecutter template that creates a basic Python setuptools project, which can be later on augmented with various optional accessories.

![Apache 2.0 licensed](http://img.shields.io/badge/license-Apache_2.0-red.svg)


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
This relies on conventions, specially check out
[\_\_init\_\_.py](https://github.com/Springerle/py-generic-project/blob/master/%7B%7Bcookiecutter.repo_name%7D%7D/src/%7B%7Bcookiecutter.repo_name%7D%7D/__init__.py)
and
[\_\_main\_\_.py](https://github.com/Springerle/py-generic-project/blob/master/%7B%7Bcookiecutter.repo_name%7D%7D/src/%7B%7Bcookiecutter.repo_name%7D%7D/__main__.py)
in the `src` folder, for their double-underscore meta variables.

It is also importable (by using the usual `if __name__ == '__main__'`
idiom), and exposes the project's setup data in a `project` dict.
This allows other tools to exploit the contained data assembling code,
and again supports the DRY principle. The `rituals` package
uses that to provide Invoke tasks that work for any project, based on
its project metadata.

Other integrated tools are `pylint` for code quality checking,
`pytest` for testing support, and a Travis CI configuration.


## Using the Template

### Preparations

In case you don't have the `cookiecutter` command line tool yet, here's
[how to install](https://github.com/Springerle/springerle.github.io#installing-the-cookiecutter-cli) it.

:loudpseaker: | For `py-generic-project` v1.2 and upwards, you need at least `cookiecutter` v1.0 – for `pipsi` installs, just issue a `pipsi upgrade cookiecutter` command and you're done.
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

 * `` classifiers.txt`` – Add the correct [categories](http://pypi.python.org/pypi?:action=list_classifiers) (a/k/a Trove classifiers) for your project.
 * ``requirements.txt`` – Add any Python packages you need for your project _at runtime_.

To bootstrap the project (as mentioned, best after `git add`), use these commands from within its directory:

```sh
. .env # answer the prompt with (y)es
inv ci | less -R
"$(basename $(pwd))" --help
```


## References

* [audreyr/cookiecutter](https://github.com/audreyr/cookiecutter)
* [jhermann/rituals](https://github.com/jhermann/rituals)
* [pyinvoke/invoke](https://github.com/pyinvoke/invoke)
* [kennethreitz/autoenv](https://github.com/kennethreitz/autoenv)
* [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage)
* [pypa/sampleproject](https://github.com/pypa/sampleproject)
* [pypa/setuptools](https://bitbucket.org/pypa/setuptools)
