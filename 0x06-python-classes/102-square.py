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
        self.__size = size

    def __eq__(self, other):
        """Equal. =="""
        if hasattr(other, 'size'):
            return self.__size == other.__size
        return self.__size == other

    def __ne__(self, other):
        """Not equal. !="""
        return not self.__eq__(other)

    def __lt__(self, other):
        """Less than. <"""
        if hasattr(other, 'size'):
            return self.__size < other.__size
        return self.__size < other

    def __gt__(self, other):
        """Greater than. >"""
        if hasattr(other, 'size'):
            return self.__size > other.__size
        return self.__size > other

    def __le__(self, other):
        """Less than or equal.<="""
        if hasattr(other, 'size'):
            return self.__size <= other.__size
        return self.__size <= other

    def __ge__(self, other):
        """Greater than or equal.<="""
        if hasattr(other, 'size'):
            return self.__size >= other.__size
        return self.__size >= other

    @property
    def size(self):
        """ Retrieves the attribute size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Set the attribute size
        Args:
            value (int): New value for size
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ Calculate the area of a square
        """
        return self.__size ** 2
