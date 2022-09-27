#!/usr/bin/python3
"""
Module: 2-append_write
appends a string at the end of a text file(UTF8)
"""


def append_write(filename="", text=""):
    """Append write
    Args:
        filename: the file to manipulate
        text: the text to append
    Return:
        return the number of characters
    """
    # open the file as f with mode=a+ to append
    with open(filename, 'a+', encoding="utf-8") as f:
        # write into the file and return
        return f.write(text)
