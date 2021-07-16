# pylint: disable=wildcard-import, missing-docstring, no-self-use
""" Test the package metadata.
"""
# Copyright ©  {{ cookiecutter.year }} {{ cookiecutter.full_name }} <{{ cookiecutter.email }}>
#
# ## LICENSE_SHORT ##
from {{ cookiecutter.pkg_name }} import __version__ as version


def test_semver():
    """Test a proper semantic version is used."""
    # TODO Test rules according to PEP440 - Version Identification and Dependency Specification
    assert len(version.split('.')) == 3, "Semantic version M.m.µ OK"
    assert all(i.isdigit for i in version.split('.')), "Semantic version parts are numeric"


def test_dir_fixtures(project_dir, tests_dir, build_dir):
    """Test global fixtures providing project directories."""
    assert project_dir / 'src' == tests_dir.parent
    assert project_dir / 'build' == build_dir
    assert build_dir.exists()
