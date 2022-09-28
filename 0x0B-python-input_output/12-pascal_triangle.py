#!/usr/bin/python3
"""
Module: 12-pascal_triangle
A function that returns a list of lists of integers
representing the pascal's triangle n
"""


def pascal_triangle(n):
    """ Pascal triangle
    Args:
        - n(int): argument
    Returns:
        Empty list if n <= 0
    """
    pascal = []
    tri = []
    if n <= 0:
        return []
    else:
        for i in range(int(n)):
            new_list = pascal[:]
            new_list.append(1)
            position = len(pascal)
            for i in range(1, position):
                new_list[i] = pascal[i - 1] + pascal[i]
            pascal = new_list[:]
            tri.append(pascal)
        return tri
