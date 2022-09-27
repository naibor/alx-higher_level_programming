#!/usr/bin/python3
"""
Module: 0-read_file
Reads a text file(UTF6) nd prints in stdout
"""


def read_file(filename=""):
    """Read file
    Args:
        filename: the name of file
    """
    # open the file as f
    with open(filename, encoding="utf-8") as f:
        # then read the file
        read_file = f.read()
        # print it to stdout
        print("{}". format(read_file))
