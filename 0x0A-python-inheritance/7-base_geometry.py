#!/usr/bin/python3
"""
Module: 7-base_geometry
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
