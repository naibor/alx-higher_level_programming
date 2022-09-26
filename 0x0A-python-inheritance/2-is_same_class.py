#!/usr/bin/python3
"""
Module 2-is_same_class
Checks if the object is same as instance of a class
"""


def is_same_class(obj, a_class):
    """ Is the same class?
    Args:
        obj: the object to check the instance of
        a_class: the class to check against
    Returns:
        Returns True if it is and False else
    """
    return (type(obj) is a_class)
