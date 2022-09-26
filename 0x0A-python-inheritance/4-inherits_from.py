#!/usr/bin/python3
"""
Module: 4-inherit_from
Check if a class is inherited from a specific class
"""


def inherits_from(obj, a_class):
    """ Is Inherited?
    Args:
        obj: the obj to check
        a_class: the class to check against
    Returns:
        Returns True if is else False
    """
    return isinstance(obj, a_class) and type(obj) != a_class
