#!/usr/bin/python3
"""
Module: 9-student
A class student
Public instance attributes: first_name, last_name, age
"""


class Student:
    """ Student class """

    def __init__(self, first_name, last_name, age):
        """ Inititalization
        Args:
            first_name: public instance attribute
            last_name: public instance attribute
            age: public instance attribute
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Retrieves a dict repr of Student instance.
        Returns:
            Dictionary representation
        """
        return self.__dict__
