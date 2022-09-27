#!/usr/bin/python3
"""
Module: 6-load_from_json_file
Creates an object from json file
"""
import json


def load_from_json_file(filename):
    """ Load from json file
    Args:
        filename: the file to get the data from
    """
    # open file as f
    with open(filename, 'r') as f:
        # load from json
        return json.load(f)
