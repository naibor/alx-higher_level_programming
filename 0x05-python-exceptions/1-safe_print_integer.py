#!/usr/bin/python3
def safe_print_integer(value):
    """ Print integers

    Args:
        value: what to print
    Returns:
        return true or false
    """
    if value:
        try:
            print("{:d}".format(value))
            return True
        except:
            return False
