#!/usr/bin/python3
"""
Module: 1-my_list
Inherits list
"""


class MyList(list):
    """ A class that inherits list. """

    def print_sorted(self):
        """ Prints a sorted(ascending) list."""
        new_list = self[:]
        new_list.sort()
        print("{}".format(new_list))
