Installing Python Software
==========================

This is a guide for end-users on how to easily install Python software on the major platforms.
See `Packaging Python Software <packaging.rst>`_ for the related developer guide
with distribution methods that enable this painless installation experience.


Installing Python
-----------------

There are different ways to get a working Python installation, depending on your
computer's operating system.


POSIX (Linux, BSD, …)
^^^^^^^^^^^^^^^^^^^^^

On *POSIX systems*, use whatever package manager your distribution offers, and
as the minimum install Python itself and everything to manage Python virtual environments.
Usually, the Python interpreter is already installed, but some of the essential extensions
and tools might be missing. For Debian-like systems, you need::

    apt-get install python python-setuptools python-pkg-resources \
                    python-virtualenv python-pip

To successfully install C extension packages like ``lxml`` from source into a ``virtualenv``,
you also need the necessary build tools like ``gcc`` or ``clang``.
On Debian-like systems, this means::

    apt-get install build-essential python-dev

While the new ``wheel`` format for binary distributions can make this unneccessary,
there are practical limitations: wheels have to be built and uploaded to PyPI, which is
seldom the case for every combination of packages and platforms. Also, wheels are not
yet fully supported for POSIX at the time of this writing.


Windows
^^^^^^^

On *Windows*, … **TODO**


Conda (Windows, Mac OS X, Linux)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Alternatively, there is also the *cross-platform*, Python-agnostic binary package manager `Conda`_,
with roots in the Scientific Python community and part of the ``Anaconda`` data processing platform.

`Miniconda`_ is a minimal distribution containing only the Conda package manager and Python.
Once Miniconda is installed, you can use the ``conda`` command to install any other packages
and create environments (``conda`` is the equivalent of ``pip``).


Installing releases from PyPI
-----------------------------

**TODO**


Installing directly from GitHub
-------------------------------

In case you *really* need the freshest source from GitHub,
there are several ways to install a setuptools-enabled project from its repository.
Be aware that this is nothing a casual user should really do,
gain some experience using ``virtualenv`` and ``pip`` before trying this.
The following shows different ways to get ``pip`` to download and install the source directly,
with a single command.

*   Via a ZIP archive download (does not need ``git`` installed)::

        pip install https://github.com/jhermann/configobj/archive/‹TAG-OR-SHA›.zip

    Usually, ``‹TAG-OR-SHA›`` will be ``master`` or ``develop`` –
    in the GitHub web UI, you can use the ``branch`` selector above the file listing
    to first select a branch, then the ``Download ZIP`` button at the bottom of the sidebar
    gives you the neccessary link.

*   Via ``git clone``::

        pip install git+https://github.com/‹USER›/‹REPO-NAME›.git

*   Via ``git clone`` with a tag or hash::

        pip install git+https://github.com/‹USER›/‹REPO-NAME›.git@‹TAG-OR-SHA›

*   From a *working directory* you manually cloned into your file system::

        pip install ‹working-directory-path›

*   The forms that use ``git+`` or a ``git`` directory can also be done as an editable package –
    the difference is that the package will end up in a top-level ``src`` directory
    instead of the deeply nested ``…/site-packages`` one, and any changes to the source will
    be instantly visible to any process that imports it.
    When you plan to change the source or otherwise need easy access to it, that makes this easy::

        pip install -e git+….git#egg=‹PKG-NAME›

Note that all these forms work in requirements files,
which in the end are only lists of ``pip install`` arguments.


.. _`Conda`: http://conda.pydata.org/
.. _`Miniconda`: http://conda.pydata.org/miniconda.html#miniconda
