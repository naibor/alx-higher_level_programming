#!/usr/bin/python3
"""
Module:
Inserts a line after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """ Append after
    Args:
        filename (str): The name of the file
        search_string (str): The string to search
        new_string (str): The string to insert after matching
    """
    # open file as f and read
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    # search for string
    for i in range(len(lines)):
        if search_string in lines[i]:
            lines.insert(i + 1, new_string)
    # open and read
    with open(filename, 'w', encoding='utf-8') as f:
        content = "".join(lines)
        f.write(content)
