#!/usr/bin/python3
"""Defining a class Square."""


class Square:
    """ A square
    Attributes:
        size (int): private attribute
    """
    def __init__(self, size):
        """ Initilize the class with attributes

        Args:
            size (int): the private attributes
        """
        self.__size = size
