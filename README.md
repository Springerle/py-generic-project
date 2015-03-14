py-generic-project
==================

A cookiecutter template that creates a basic Python setuptools project, which can be later on augmented with various optional accessories.

![Apache 2.0 licensed](http://img.shields.io/badge/license-Apache_2.0-red.svg)


## Preparations

In case you don't have the `cookiecutter` command line tool yet, here's
[how to install](https://github.com/Springerle/springerle.github.io#installing-the-cookiecutter-cli) it.


## Using the template

Creating a new Python project based on this template goes like this (make sure
you're in the directory you want your project added to):

```sh
cookiecutter "https://github.com/Springerle/py-generic-project.git"
```

It's advisable to `git add` the created directory directly afterwards, before any
generated files are added, that you don't want to have in your repository.

:bulb: | To get *your* defaults for common template values `cookiecutter` will ask you for when you use a template, it makes sense to have a [~/.cookiecutterrc](https://github.com/jhermann/ruby-slippers/blob/master/home/.cookiecutterrc) in your home directory. Follow the link to see an example.
---- | :----


To bootstrap the project (as mentioned, best after `git add`), use these commands from within its directory:

```sh
. .env # answer the prompt with (y)es
inv ci | less -R
"$(basename $(pwd))" --help
```


## References

* [pypa/sampleproject](https://github.com/pypa/sampleproject)
* [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage)
