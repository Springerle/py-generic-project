# pylint: disable=
""" py.test dynamic configuration.

    For details needed to understand these tests, refer to:
        https://pytest.org/
        http://pythontesting.net/start-here/
"""
# Copyright ©  {{ cookiecutter.year }} {{ cookiecutter.full_name }} <{{ cookiecutter.email }}>
#
# ## LICENSE_SHORT ##
import os
import logging
from pathlib import Path

import pytest


# Globally available fixtures
@pytest.fixture(scope='session')
def logger() -> logging.Logger:
    """Test logger instance as a fixture."""
    level = os.getenv('TESTS_LOG_LEVEL', 'DEBUG')
    logging.basicConfig(level=getattr(logging, level))
    return logging.getLogger('tests')


@pytest.fixture(scope='session')
def tests_dir() -> Path:
    """Directory where tests + data is located."""
    return Path(__file__).parent


@pytest.fixture(scope='session')
def project_dir(tests_dir) -> Path:
    """ Root directory of the project.
    """
    return tests_dir.parent.parent


@pytest.fixture(scope='session')
def build_dir(project_dir) -> Path:
    """Build directory for dynamic data (created if missing)."""
    result = project_dir / "build"
    result.mkdir(exist_ok=True)
    return result
