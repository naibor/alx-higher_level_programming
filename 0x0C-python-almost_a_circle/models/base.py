#!/usr/bin/python3
"""
Module: base

"""


class Base:
    """Base class
    Private class attribute:
        __nb_objects = 0
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initilize class base
        Args:
            id(int)
        """
        # check attribute id and assign it
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Dict to  json string representation
        Args:
            list_dictionaries (json): An inputted jason list of dictionaries
        Returns:
            A json repreentation
        """
        if list_dictionaries is None or not list_dictionaries:
            return '[]'
        return json.dumps(list_dictionaries)

