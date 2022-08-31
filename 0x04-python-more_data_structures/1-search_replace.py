#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """ Searches and replaces an element
    Args:
        my_list: the list to work on
        search: the value to search
        replace: the value to replace it with
    Returns:
    """
    new_list = []
    for item in my_list:
        if search == item:
            new_list.append(replace)
        else:
            new_list.append(item)
    return new_list
