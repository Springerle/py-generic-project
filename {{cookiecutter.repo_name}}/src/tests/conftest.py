# pylint: disable=
""" py.test dynamic configuration.

    For details needed to understand these tests, refer to:
        https://pytest.org/
        http://pythontesting.net/start-here/
"""
# Copyright ©  {{ cookiecutter.year }} {{ cookiecutter.full_name }} <{{ cookiecutter.email }}>
#
# ## LICENSE_SHORT ##
import logging

import pytest


# Globally available fixtures
@pytest.fixture(scope='session')
def logger():
    """Test logger instance as a fixture."""
    logging.basicConfig(level=logging.DEBUG)
    return logging.getLogger('tests')
