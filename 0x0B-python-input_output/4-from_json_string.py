#!/usr/bin/python3
"""
Module: 4-from_json_string
converts a json string to a python data structure
"""
import json


def from_json_string(my_str):
    """ From json string
    Args:
        my_str: the json string
    Returns:
        returns the object converted
    """
    return json.loads(my_str)
