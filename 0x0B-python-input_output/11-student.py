#!/usr/bin/python3
"""
Module: 11-student
A class student
Public instance attributes: first_name, last_name, age
"""


class Student:
    """ Student class
    Public instance attributes:
        first_name
        last_name
        age
    Public method:
        to_json
        reload_from_json
    """

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

    def to_json(self, attrs=None):
        """ Retrieves a dict repr of Student instance.
        Args:
            attrs: list of attributes to check
        Returns:
            Dictionary representation
        """
        new_dict = {}
        if type(attrs) is list and all(type(x) is str for x in attrs):
            for x in attrs:
                if x in self.__dict__:
                    new_dict.update({x: self.__dict__[x]})
            return new_dict
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """ Reload from json
        Args:
            json: the json in question
        """
        for item in json:
            self.__dict__.update({item: json[item]})
