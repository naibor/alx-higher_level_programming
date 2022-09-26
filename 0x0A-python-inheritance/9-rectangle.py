#!/usr/bin/python3
"""
Module: 9-rectangle
A class BaseGeometry
"""


# Import BaseGeometry
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Class Rectangle, that inherits from BaseGeometry. """

    def __init__(self, width, height):
        """ Instantiate class rectangle
        Args:
            width: private argument
            height: private argument
        """
        # validate values using integer_validator method
        w = BaseGeometry.integer_validator(self, name="width", value=width)
        h = BaseGeometry.integer_validator(self, name="height", value=height)
        self.__width = w
        self.__height = h

    def __str__(self):
        """ Formating string"""

        return str("[Rectangle] {}/{}".format(self.__width, self.__height))

    def area(self):
        """ Override function area()
        Include calculating the area
        """
        return self.__width * self.__heigth
