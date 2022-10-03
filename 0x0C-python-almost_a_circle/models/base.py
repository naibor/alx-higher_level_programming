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
        if id in not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
