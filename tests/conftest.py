# pylint: disable=
""" py.test dynamic configuration.

    For details needed to understand these tests, refer to:
        https://pytest.org/
        http://pythontesting.net/start-here/
"""
# Copyright (c) 2015 Jürgen Hermann
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import os
import shutil
import logging
import subprocess

import pytest


# Globally available fixtures
@pytest.fixture(scope='session')
def project():
    """Materialize cookiecutter template (once)."""
    new_project = 'new-project'

    if os.path.exists(new_project):
        shutil.rmtree(new_project)
    subprocess.check_call(['cookiecutter', '--no-input', '.'])

    return os.path.abspath(new_project)


@pytest.fixture(scope='session')
def logger():
    """Test logger instance as a fixture."""
    logging.basicConfig(level=logging.DEBUG)
    return logging.getLogger('tests')
