#!/usr/bin/python3
"""
Module: 1-write_file
Writes a string to a text file(UTF8) and return the number of characters
"""


def write_file(filename="", text=""):
    """Write into a file
    Args:
        filename: the filename of the file
        text: what to write
    Returns:
        return number of characters
    """
    # open the file as f
    # create if not there or override if it does mode='w'
    with open(filename, 'w+', encoding="utf-8") as f:
        # write into the file and return
        return f.write(text)
