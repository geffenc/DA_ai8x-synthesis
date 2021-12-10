###################################################################################################
# Copyright (C) 2019-2021 Maxim Integrated Products, Inc. All Rights Reserved.
#
# Maxim Integrated Products, Inc. Default Copyright Notice:
# https://www.maximintegrated.com/en/aboutus/legal/copyrights.html
###################################################################################################
"""
Print error message to stderr, and stdout as well if needed
"""
import sys

import colorama

from . import state


def eprint(*args, error=True, notice=False, prefix=True, exit_code=1, **kwargs):
    """
    Print message to stderr, and stdout as well IF stdout was overridden.
    Add a `prefix` if set (and `error` chooses which).
    """
    if prefix:
        pfx = 'ERROR:' if error else 'WARNING:' if not notice else 'NOTICE:'

        if not state.output_is_console:
            print(pfx, *args, **kwargs)

        ansi_on = colorama.Fore.RED if error else colorama.Fore.YELLOW \
            if not notice else colorama.Fore.GREEN
        pfx = ansi_on + pfx + colorama.Style.RESET_ALL

        print(pfx, *args, file=sys.stderr, **kwargs)
    else:
        if not state.output_is_console:
            print(*args, **kwargs)

        print(*args, file=sys.stderr, **kwargs)

    if error and exit_code is not None:
        sys.exit(error)


def wprint(*args, **kwargs):
    """
    Print message to stderr, and stdout as well IF stdout was overridden.
    Add a WARNING: prefix.
    """
    eprint(*args, error=False, **kwargs)


def nprint(*args, **kwargs):
    """
    Print message to stderr, and stdout as well IF stdout was overridden.
    Add a NOTICE: prefix.
    """
    eprint(*args, error=False, notice=True, **kwargs)


def eprint_noprefix(*args, **kwargs):
    """
    Print message to stderr, and stdout as well IF stdout was overridden.
    """
    eprint(*args, prefix=False, exit_code=None, **kwargs)
