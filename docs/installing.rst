..  documentation: installing

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

Installing Python Software
==========================

This is a guide for end-users on how to easily install Python software on the major platforms.
See :doc:`packaging` for the related developer guide
with distribution methods that enable this painless installation experience.


.. _quick-setup:

TL;DR
-----

This is a no-frills version of basic installation procedures for the three major PC platforms.
Read the other sections for more details, especially if you encounter any problems with
these condensed instructions.
Once the basic setup is done, refer to either :ref:`pip-from-pypi` or :ref:`pip-from-github`
to get an application installed – and in case the project author provides a
**P**\ ython **Ex**\ ecutable archive, prefer an :ref:`pex-install`.

On **Linux**, make sure you have the right version of *Python* pre-installed, and the basic
developer toolset available. On Debian-like systems, the following makes sure of that:

.. code-block:: shell

    sudo apt-get install python python-setuptools python-pkg-resources \
        python-virtualenv python-pip python-dev libffi-dev build-essential git

For *Python3*, replace each occurence of ``python`` with ``python3`` in the above command –
this requires a fairly recent distribution though, like *Debian Jessie*.

On **Mac OS X**, install a modern *Python* tool chain and
missing *GNU* utilities that are often needed by helper scripts:

.. code-block:: shell

    sudo easy_install pip && sudo pip install virtualenv
    brew install coreutils

For **Windows**, see the :ref:`win-python` and :ref:`babun` sections.
The former is recommended for users who just want to run some Python software,
the latter for developers and ‘power users’
with some existing Python and Linux experience.

More recent options are `bash for Windows`_, `Docker for Windows`_,
and `Windows Containers`_.
After you install one of these, act like you're on a **Linux** system,
because as long as you operate within those environments, you actually are.

.. note::

    Remember that the next step is either :ref:`pip-from-pypi` or :ref:`pip-from-github`.


Installing Python
-----------------

There are different ways to get a working Python installation, depending on your
computer's operating system. Note that there are two major versions of Python,
and at this time Python 2.7 and Python 3.4 are the recommended versions to use.

Read the documentation of any software you want to install regarding the versions
of Python that particular software runs on, and act accordingly by e.g. calling
``virtualenv-3`` instead of just ``virtualenv``.

See also these other resources on the web…

  * `Picking an Interpreter <http://docs.python-guide.org/en/latest/starting/which-python/>`_



POSIX (Linux, BSD, …)
^^^^^^^^^^^^^^^^^^^^^

On *POSIX systems*, use whatever package manager your distribution offers, and
as the minimum install Python itself and everything to manage Python virtual environments.
Usually, the Python interpreter is already installed, but some of the essential extensions
and tools might be missing. For Debian-like systems, you need:

.. code-block:: shell

    apt-get install python python-setuptools python-pkg-resources \
                    python-virtualenv python-pip

To successfully install C extension packages like ``lxml`` from source into a ``virtualenv``,
you also need the necessary build tools like ``gcc`` or ``clang``.
On Debian-like systems, this means:

.. code-block:: shell

    apt-get install python-dev libffi-dev build-essential git

While the new ``wheel`` format for binary distributions can make this unneccessary,
there are practical limitations: wheels have to be built and uploaded to PyPI, which is
seldom the case for every combination of packages and platforms. Also, wheels are not
yet fully supported for POSIX at the time of this writing.


.. _win-python:

Windows (python.org)
^^^^^^^^^^^^^^^^^^^^

To get the official *python.org* distribution on *Windows*, open the
`Python Releases for Windows`_ page and select the appropriate version.
You might want to install both a Python 2 and 3 version, to cover all
possible needs of any applications.

It's also recommended to install the `Python Extensions for Windows`_,
because many applications rely on them to access Windows-specific features.

Finally, for Python 2 you should install *PyLauncher* to be able to start
applications distributed as an *‘executbale ZIP’*, see its
`download page <https://bitbucket.org/vinay.sajip/pylauncher/downloads>`_.
Python 3 already has it pre-installed.


.. _babun:

Babun (Windows)
^^^^^^^^^^^^^^^

*Babun* is a turn-key *CygWin* distribution for developers
and is very easy to install and maintain.
For a Python developer, *Babun* allows working in an almost-POSIX environment
– with some limitations, of course.
This causes less friction when handling FOSS projects
that are often biased towards a standard Linux environment,
e.g. by using shell scripts for boot-strapping and things like that.

To install it, follow these steps:

  * Download the installer ZIP archive from the `Babun homepage`_.
  * Unzip the archive (e.g. using *Windows Explorer*).
  * Double-click the installer (``install.bat``), and wait…
  * Catch up (``babun update``).
  * Change the default shell from ``zsh`` to ``bash`` if you prefer that (``babun shell /bin/bash``).
  * Edit ``~/.bashrc`` to activate loading of ``~/.bash_aliases``.
  * Install additional *Python* essentials:

    .. code-block:: shell

        pact install python-setuptools python-ming
        pact install libxml2-devel libxslt-devel libyaml-devel
        curl -skS https://bootstrap.pypa.io/get-pip.py | python
        pip install virtualenv
        curl -skS https://raw.githubusercontent.com/mitsuhiko/pipsi/master/get-pipsi.py | python

  * Enjoy!


Conda (Windows, Mac OS X, Linux)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Alternatively, there is also the *cross-platform*, Python-agnostic binary package manager `Conda`_,
with roots in the Scientific Python community and being part of the ``Anaconda`` data processing platform.

`Miniconda`_ is a minimal distribution containing only the Conda package manager and Python.
Once Miniconda is installed, you can use the ``conda`` command to install any other packages
and create environments (``conda`` is the equivalent of ``virtualenv`` and ``pip``).


RyRun (Mac OS X, Linux, FreeBSD)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Yet another contender is `PyRun`_ from *eGenix*. It is a one file Python runtime,
that combines a Python interpreter with an almost complete Python standard library
into a single easy-to-use executable of about 12 MiB in size.
The selling point is easy installation by only handling a single file, which also
results in easy relocation – ideal for using it on an USB stick for portable
applications, or part of a self-contained bundle for server installations.
It covers all the relevant Python versions (2.6, 2.7, and 3.4), and comes
in 32bit and 64bit flavours.

From an application installation standpoint, *PyRun* allows you to
efficiently create isolated runtime environments that include their own
Python interpreter and standard library, i.e. are even more detached
from the host setup than normal virtualenvs.

.. _`PyRun`: https://www.egenix.com/products/python/PyRun/


pyenv (Simple Python Version Management)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`pyenv`_ works for Mac OS X and POSIX systems and is a simple way
to obtain access to Python versions that are not available from
your system's software repositories, and switch between them at will.

See the `pyenv installation instructions`_ for details.


.. _pex-install:

Installation With PEX
---------------------

`PEX files`_ are **P**\ ython **Ex**\ ecutable ZIP files, a format that contains
a full distribution of a Python application in a single archive
(just like executable JARs for Java).
PEX files can be targeted at a specific platform and Python version,
but might also support multiple runtime environments.
Consult the documentation of your application for further guidance.

Installing a PEX file is as easy as downloading it from the project's download page
(e.g. *Bintray* or the *GitHub* releases section of a project), using your browser
or ``curl``, and then just start it from where you saved it to in your file system.
On *Windows*, give the file a ``.pyz`` or ``.pyzw`` extension,
which the *Python Launcher* is registered for.
On POSIX systems, ``chmod +x`` the file to make it executable.

See `PEP 441`_ for a formal description of the underlying mechanics and all the details.

.. _`PEX files`: https://youtu.be/NmpnGhRwsu0
.. _`PEP 441`: https://www.python.org/dev/peps/pep-0441/


.. _pip-from-pypi:

Installing Releases From PyPI
-----------------------------

For releases published on `PyPI`_, you should use ``pip`` to install them
(i.e. do not use ``easy_install`` anymore). It's common procedure to
not install into ``/usr/local`` on Linux, but instead create a so-called
*virtualenv*, which is a runtime environment that is (by default) isolated
against the host system and its packages, as well as against other virtualenvs.
This means that you don't have to carefully manage version numbers, you can
let ``pip`` install exactly those versions an application works best with.

To create a virtualenv, go to the desired install location, and create
the new environment, also giving it a name:

.. code-block:: shell

    cd ~/.local/virtualenvs
    virtualenv ‹newenv›
    . ‹newenv›/bin/activate
    pip install -U pip setuptools # get newest tooling

The third command *activates* the virtualenv, which means that
when you call ``python`` or ``pip``, they run in the context of
that virtualenv.

Now all you have to do is call ``pip install ‹my-new-app›`` and
it'll get installed into that environment. If the package provides
command line tools, don't forget to add the ``bin`` directory to
your ``PATH`` – or better yet symlink those commands into your
``~/bin`` directory or add some definitions to ``~/.bash_aliases``,
to make them selectively available.

If you're installing a Python package that contains a single command,
then `pipsi`_ (*Python Script Installer*) allows installing and updating
with a simple one-liner. ``pipsi`` is just a convenient wrapper
around ``pip`` and ``virtualenv``, and works in POSIX environments
including *CygWin*.

.. _`PyPI`: https://pypi.python.org/pypi
.. _`pipsi`: https://github.com/mitsuhiko/pipsi#readme


.. _pip-from-github:

Installing Directly From GitHub
-------------------------------

In case you *really* need the freshest source from GitHub,
there are several ways to install a setuptools-enabled project from its repository.
Be aware that this is nothing a casual user should really do,
gain some experience using ``virtualenv`` and ``pip`` before trying this.
The following shows different ways to get ``pip`` to download and install the source directly,
with a single command.

  * Via a ZIP archive download (does not need ``git`` installed):

    .. code-block:: shell

        pip install "https://github.com/‹USER›/‹REPO-NAME›/archive/‹TAG-OR-SHA›.zip"

    Usually, ``‹TAG-OR-SHA›`` will be ``master`` or ``develop`` –
    in the GitHub web UI, you can use the ``branch`` selector above the file listing
    to first select a branch, then the ``Download ZIP`` button at the bottom of the sidebar
    gives you the neccessary link.

  * Via ``git clone``:

    .. code-block:: shell

        pip install "git+https://github.com/‹USER›/‹REPO-NAME›.git"

  * Via ``git clone`` with a tag or hash:

    .. code-block:: shell

        pip install "git+https://github.com/‹USER›/‹REPO-NAME›.git@‹TAG-OR-SHA›"

  * From a *working directory* you manually cloned into your file system:

    .. code-block:: shell

        pip install "‹working-directory-path›"

  * The forms that use ``git+`` or a ``git`` directory can also be done as an editable package –
    the difference is that the package will end up in a top-level ``src`` directory
    instead of the deeply nested ``…/site-packages`` one, and any changes to the source will
    be instantly visible to any process that imports it.
    When you plan to change the source or otherwise need quick access to it, that makes this easy:

    .. code-block:: shell

        pip install -e "git+….git#egg=‹PKG-NAME›"

Note that all these forms work in requirements files,
which in the end are only lists of ``pip install`` arguments.


.. _`Python Releases for Windows`: https://www.python.org/downloads/windows/
.. _`Python Extensions for Windows`: http://sourceforge.net/projects/pywin32/files/
.. _`Babun homepage`: http://babun.github.io/
.. _`bash for Windows`: https://msdn.microsoft.com/en-us/commandline/wsl/about
.. _`Docker for Windows`: https://docs.docker.com/docker-for-windows/
.. _`Windows Containers`: https://docs.microsoft.com/en-us/virtualization/windowscontainers/about/
.. _`Conda`: http://conda.pydata.org/
.. _`Miniconda`: http://conda.pydata.org/miniconda.html#miniconda
.. _`pyenv`: https://github.com/yyuu/pyenv
.. _`pyenv installation instructions`: https://github.com/yyuu/pyenv#installation
