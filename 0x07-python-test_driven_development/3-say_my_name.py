#!/usr/bin/python3
"""
Module say_my_name
It prints out a name(string) given
"""


def say_my_name(first_name, last_name=""):
    """Prints out given name
    Args:
        first_name: your first name
        last_name: your last name
    Exceptions:
        raise TypeError if first name or lastname is not string
    """
    # handle exceptions
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
