..  documentation: authoring

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

Writing Sphinx Documentation
============================

This is a directory of links to information and hints you need
when you want to write (software) documentation using
`reStructuredText`_ and `Sphinx`_.


Introduction & Cheatsheets
--------------------------

* `Sphinx reStructuredText primer <http://sphinx-doc.org/rest.html>`_


Useful Extensions
-----------------

* `PlantUML <https://pypi.python.org/pypi/sphinxcontrib-plantuml>`_


Tools
-----

*Lists*

* `reStructuredText tool support <http://stackoverflow.com/questions/2746692/restructuredtext-tool-support>`_ @ Stack Overflow.
* `Awesome Sphinx <https://github.com/yoloseem/awesome-sphinxdoc>`_

*General*

* `restview`_ – A HTML viewer for reStructuredText documents that renders them on the fly.

*gedit3*

* reStructuredText preview and highlighting

  * `For Python3 and gedit 3.8 <https://github.com/bittner/gedit-reST-plugin>`_
  * `For Python2 <https://github.com/mcepl/reStPlugin>`_

* `gedit3 language definition for reStructuredText`_




.. _Sphinx: http://sphinx-doc.org/index.html
.. _reStructuredText: http://docutils.sourceforge.net/rst.html
.. _restview: https://github.com/mgedmin/restview#restview
.. _gedit3 language definition for reStructuredText: https://github.com/jhermann/ruby-slippers/blob/master/home/.local/share/gtksourceview-3.0/language-specs/restructuredtext.lang


How-Tos
-------

Adding a Custom Pygments Lexer to Sphinx
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In order for Sphinx to load and recognize a custom lexer, two things are needed:

 1. Add the package name of the lexer to the ``extensions`` list in ``conf.py``.
    Of course, that package has to be importable, either by using a virtualenv
    or manipulating ``sys.path``.
 2. Give your lexer package a Setuptools ``pygments.lexers`` entry point.

Then use it in a ``code-block`` as if it were a built-in. That's all.
