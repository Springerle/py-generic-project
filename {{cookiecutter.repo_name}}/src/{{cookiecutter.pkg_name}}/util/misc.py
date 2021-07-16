""" Miscellaneous helpers.
"""
# Copyright ©  {{ cookiecutter.year }} {{ cookiecutter.full_name }} <{{ cookiecutter.email }}>
#
# ## LICENSE_SHORT ##
import sys
import logging


def make_logger(name):
    """ Create a working (non-silent) logger instance.

        *Working* means the parent defaults to the root logger,
        and if that one has no attached handlers, the newly created
        logger get attached directly to stderr.

        Args;
            name (str): Logger name.

        Returns:
            ~logging.Logger: The new logger instance.
    """
    logger = logging.Logger(name)
    if not logger.parent:  # anchor to root logger if free-floating
        logger.parent = logging.getLogger()
    if not logger.parent.handlers:  # log to stderr if unhandled in parent
        logger.addHandler(logging.StreamHandler(sys.stderr))
    return logger
