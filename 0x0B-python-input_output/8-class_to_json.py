#!/usr/bin/python3
"""
Module: 8-class_to_json
Returns a dictionary description with simple data structure
for json serialization of an object
"""


def class_to_json(obj):
    """ Create a dictionary description of obj
    Args:
        obj: the object to describe
    Returns:
        returns dictionary description
    """
    return obj.__dict__
