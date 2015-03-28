# -*- coding: utf-8 -*-
# pylint: disable=invalid-name
""" py.test markers.

    For details needed to understand these tests, refer to:
        https://pytest.org/
        http://pythontesting.net/start-here/
"""
# Copyright ©  {{ cookiecutter.year }} {{ cookiecutter.full_name }} <{{ cookiecutter.email }}>
#
# ## LICENSE_SHORT ##
from __future__ import absolute_import, unicode_literals, print_function

import pytest


# See also setup.cfg » [pytest] » markers
cli = pytest.mark.cli
integration = pytest.mark.integration
online = pytest.mark.online


# Export all markers
__all__ = [_k
           for _k, _v in globals().items()
           if _v.__class__ is cli.__class__]
