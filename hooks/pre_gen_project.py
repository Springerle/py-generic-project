#! /usr/bin/env python
# pylint: disable=bad-whitespace, superfluous-parens
"""
    Cookiecutter pre-gen hook.

    This gets called with no arguments, and with the project directory
    as the working directory. That is empty on the first run, but might
    also already be populated when Cookiecutter is called on a pre-
    existing project.

    Copyright (c) 2015 Juergen Hermann

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
"""
import os
import sys
import pprint
from collections import OrderedDict

DEBUG = False


def run():
    """Main loop."""
    # Fallback for working with older Cookiecutter versions
    Undefined = None # pylint: disable=invalid-name, unused-variable

    # Make pylint happy
    version = verbose = checkout = repo_dir = context_file = cookiecutter = None

    version = {{ version | pprint }}
    try:
        version_info = tuple(int(i) for i in (version or '').split('.'))
    except (ValueError, TypeError):
        version_info = ()

    verbose = {{ verbose | pprint }}
    checkout = {{ checkout | pprint }}
    repo_dir = {{ repo_dir | pprint }}
    context_file = {{ context_file | pprint }}
    context = {{ cookiecutter | pprint }}

    if verbose or DEBUG:
        print('*' * 78)
        print('{} "{}"'.format(__doc__.split('.', 1)[0].strip(), sys.argv[0]))
        print('')
        print(u"    verbose={}".format(verbose))
        print(u"    checkout={}".format(checkout))
        print(u"    version={}".format(version))
        print(u"    version_info={}".format(version_info))
        print(u"    repo_dir={}".format(repo_dir))
        print(u"    context_file={}".format(context_file))
        print(u"    context={}".format(context))
        print(u"""    context[pprint]={{ cookiecutter | pprint }}""")
        print(u"    argv={}".format(sys.argv))
        print(u"    cwd={}".format(os.getcwd()))
        print(u"    ls={}".format(os.listdir('.')))
        print('*' * 78)


if __name__ == '__main__':
    run()
