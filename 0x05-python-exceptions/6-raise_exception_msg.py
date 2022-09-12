#!/usr/bin/python3
def raise_exception_msg(message=""):
    """ Raise an exception message
    Args:
        message: the message
    """
    try:
        raise NameError(message)
    except (NameError):
        raise
