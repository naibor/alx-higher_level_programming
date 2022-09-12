#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """ Prints an integer
    Args:
        value: the int to print
    Returns:
        return True if value is correctly printed else false
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return False
    else:
        return False
