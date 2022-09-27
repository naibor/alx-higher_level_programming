#!/usr/bin/python3
"""
Module: 3-to_json_string
Returns a json representation of an object(string)
"""
import json


def to_json_string(my_obj):
    """ To json string
    Args:
        my_obj: what to convert to json
    Returns:
        returns json
    """
    return json.dumps(my_obj)
