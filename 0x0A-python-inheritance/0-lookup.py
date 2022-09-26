#!/usr/bin/python3
"""
Module: 0-lookup
Contains a function that returns the attributes and methods of objects
"""


def lookup(obj):
    """ Looks up attributes and methods
    Args:
        obj: the object to look up
    Returns:
        returns a list
    """
    return dir(obj)
