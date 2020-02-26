..  documentation master file

    Copyright (c) 2015 Jürgen Hermann

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


=============================================================================
Welcome to the “py-generic-project” manual!
=============================================================================

.. image:: _static/img/logo.png

This is a Cookiecutter template that creates a basic Python Setuptools project,
which can be later on augmented with various optional accessories. See the
`demo <https://github.com/Springerle/py-generic-project/tree/master/demo>`_
for getting a 1ˢᵗ impression on how this Cookiecutter template can be
used, including screenshots of the terminal session.

If you have questions or need any other kind of help, please join the
`springerle-users <https://groups.google.com/forum/#!forum/springerle-users>`_
Google group.


Features
--------

The resulting project uses `rituals`_ and
`invoke <https://github.com/pyinvoke/invoke/>`_ for task automation, and
`setuptools <https://bitbucket.org/pypa/setuptools>`_ for building and
distributing the project. A provided
`autoenv <https://github.com/kennethreitz/autoenv>`_ script takes care
of creating a fully boot-strapped Python 3 ``venv`` or Python 2 ``virtualenv``
– it can also be called manually if you don't want to install ``autoenv``.

The ``setup.py`` script follows the DRY principle and tries to minimize
repetition of project metadata by loading it from other places (like the
package's ``__init__.py``). Incidently, this makes the script almost
identical between different projects, and thus provides an easy update
experience later on. Usually, the only specific thing in it is the
docstring with the project's name and license notice. This relies on
conventions, especially check out
`\_\_init\_\_.py <https://github.com/Springerle/py-generic-project/blob/master/%7B%7Bcookiecutter.repo_name%7D%7D/src/%7B%7Bcookiecutter.pkg_name%7D%7D/__init__.py>`_
and
`\_\_main\_\_.py <https://github.com/Springerle/py-generic-project/blob/master/%7B%7Bcookiecutter.repo_name%7D%7D/src/%7B%7Bcookiecutter.pkg_name%7D%7D/__main__.py>`_
in the ``src`` folder, for their double-underscore meta variables.

It is also importable (by using the usual ``if __name__ == '__main__'``
idiom), and exposes the project's setup data in a ``project`` dict. This
allows other tools to exploit the contained data assembling code, and
again supports the DRY principle. The ``rituals`` package uses that to
provide Invoke tasks that work for any project, based on its project
metadata.

Other integrated tools are ``pylint`` for code quality checking,
``pytest`` for testing support, and a Travis CI configuration.


Documentation Contents
----------------------

.. toctree::
    :maxdepth: 4

    usage
    packaging
    installing
    authoring
    LICENSE


References
----------

Tools
^^^^^

-  `Cookiecutter <https://cookiecutter.readthedocs.io/en/latest/>`_
-  `PyInvoke <http://www.pyinvoke.org/>`_
-  `pytest <http://pytest.org/latest/contents.html>`_
-  `tox <https://tox.readthedocs.io/en/latest/>`_
-  `Pylint <http://docs.pylint.org/>`_
-  `pypa/setuptools <https://bitbucket.org/pypa/setuptools>`_
-  `pypa/sampleproject <https://github.com/pypa/sampleproject>`_
-  `twine <https://github.com/pypa/twine#twine>`_
-  `autoenv <https://github.com/kennethreitz/autoenv>`_
-  `bpython <http://docs.bpython-interpreter.org/>`_
-  `yolk3k <https://github.com/myint/yolk#yolk>`_

Packages
^^^^^^^^

-  `rituals`_
-  `click <http://click.pocoo.org/>`_


Indices and Tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


.. _`rituals`: https://jhermann.github.io/rituals
