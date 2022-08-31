#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """ deletes specific keys in a dict
    Args:
        a_dictionary: the dictionary to work with
        value: what to delete
    Returns:
        a dict
    """
    key_to_del = []
    for key, the_value in a_dictionary.items():
        if the_value == value:
            key_to_del.append(key)
    for item in key_to_del:
        del (a_dictionary[item])
    return a_dictionary
