#!/usr/bin/python3
"""
Module: 11-square
A class square that inherits Rectangle class
"""


# import rectangle class
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ square class, inherits Rectangle. """

    def __init__(self, size):
        """ Instantiation of square
        Args:
            size: private attribute
        """
        # Validate usind integer validator function and initialize
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """ Formatted string"""
        return str("[Square] {}/{}".format(self.__size, self.__size))

    def area(self):
        """ Override area function
        Calculate area of square
        """
        return self.__size ** 2
