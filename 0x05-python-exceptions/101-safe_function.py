#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """ Executes a function safely
    Args:
        fct: the pointer to a function
        args: arguments
    Returns:
        returns result of function
        else, None if something happens
    """
    if fct:
        try:
            result = fct(*args)
            return result
        except Exception as err:
            print("Exception: {}".format(err), file=sys.stderr)
            return None
