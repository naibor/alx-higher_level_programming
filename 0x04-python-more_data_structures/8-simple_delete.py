#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """ deletes a key in a dictionary
    Args:
        a_dictionary: the dict to work on
        key: the key
    Returns:
        returns a dict
    """
    if key in a_dictionary:
        del (a_dictionary[key])
    return a_dictionary
