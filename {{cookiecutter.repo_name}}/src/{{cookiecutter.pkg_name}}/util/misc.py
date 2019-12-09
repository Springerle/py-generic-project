# pylint: disable=bad-continuation
""" Miscellaneous helpers.
"""
# Copyright ©  {{ cookiecutter.year }} {{ cookiecutter.full_name }} <{{ cookiecutter.email }}>
#
# ## LICENSE_SHORT ##
import sys
import logging


def make_logger(name):
    """ Create a working (non-silent) logger instance.
    """
    logger = logging.Logger(name)
    if not logger.parent:  # anchor to root logger if free-floating
        logger.parent = logging.getLogger()
    if not logger.parent.handlers:  # log to stderr if unhandled in parent
        logger.addHandler(logging.StreamHandler(sys.stderr))
    return logger
