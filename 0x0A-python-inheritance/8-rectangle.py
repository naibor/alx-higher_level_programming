#!/usr/bin/python3
"""
Module: 5-base_geometry
A class BaseGeometry
"""


class BaseGeometry():
    """ A class BaseGeometry."""

    def area(self):
        """ Area
        Exceptions:
            raise exception area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates integers
        Args:
            name: the string
            value: the value
        Exceptions:
            Raise TypeError value must be an integer
            Raise ValueError if value is <= 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer". format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0". format(name))


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
