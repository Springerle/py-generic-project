# *- coding: utf-8 -*-
# pylint: disable=wildcard-import, missing-docstring, no-self-use, bad-continuation
""" Test the package metadata.
"""
# Copyright ©  {{ cookiecutter.year }} {{ cookiecutter.full_name }} <{{ cookiecutter.email }}>
#
# ## LICENSE_SHORT ##
from __future__ import absolute_import, unicode_literals, print_function

from {{ cookiecutter.pkg_name }} import __version__ as version


def test_semver():
    """Test a proper semantic version is used."""
    # TODO Test rules according to PEP440 - Version Identification and Dependency Specification
    assert len(version.split('.')) == 3, "Semantic version M.m.µ OK"
    assert all(i.isdigit for i in version.split('.')), "Semantic version parts are numeric"
