#!/usr/bin/python3
"""
Module: 3-is_kind_of_class
checks if object is an instance of a class
"""


def is_kind_of_class(obj, a_class):
    """ Is instance of a class
    Args:
        obj: the object to check
        a_class: the class to check against
    Returns:
        returns True if is else False
    """
    return isinstance(obj, a_class)
