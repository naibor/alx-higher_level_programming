#!/usr/bin/python3
"""
Module: 8-rectangle
A class Rectangle that inherits from BaseGeometry

"""


# Import BaseGeometry class
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Class Rectangle, that inherits from BaseGeometry. """

    def __init__(self, width, height):
        """ Instantiate class rectangle
        Args:
            width: private instance attribute
            height: private instance attribute
        """
        # validate values using integer_validator method
        w = BaseGeometry.integer_validator(self, name="width", value=width)
        h = BaseGeometry.integer_validator(self, name="height", value=height)
        self.__width = w
        self.__height = h
