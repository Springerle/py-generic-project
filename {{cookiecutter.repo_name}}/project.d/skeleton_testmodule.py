# pylint: disable=wildcard-import, missing-docstring, no-self-use
# pylint: disable=invalid-name, redefined-outer-name, too-few-public-methods
""" Test :py:mod:`«some_module»`.
"""
# Copyright ©  {{ cookiecutter.year }} {{ cookiecutter.full_name }} <{{ cookiecutter.email }}>
#
# ## LICENSE_SHORT ##
from {{ cookiecutter.pkg_name }} import some_module


def test_fails():
    assert False, "This test needs to get some sensible logic"
