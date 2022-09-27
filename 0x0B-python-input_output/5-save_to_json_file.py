#!/usr/bin/python3
"""
Module: 5-save_to_json_file
writes a onject to a text file using json
"""
import json


def save_to_json_file(my_obj, filename):
    """ Save to json file
    Args:
        my_obj: the object to save as json
        filename: the file to save it to
    """
    # open file as f
    with open(filename, 'w+') as f:
        # serialize to a file
        json.dump(my_obj, f)
