#!/usr/bin/python3
def raise_exception():
    """ raise a type exception
    Args:
        None
    Returns:
        exception raised
    """
    try:
        raise TypeError
    except (TypeError):
        raise
