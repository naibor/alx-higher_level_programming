#!/usr/bin/python3
"""Defining a class Square."""


class Square:
    """ A Square
    Attributes:
        size (int): private attribute
    """
    def __init__(self, size=0):
        """ Intitilize class square with attribute size
        Args:
            size (int): parameter
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ Calculate the area of a square
        """
        return self.__size ** 2
