#!/usr/bin/python3
"""
Module: base

"""
import json


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

    @classmethod
    def save_to_file(cls, list_objs):
        """Json string repressentation list object to a file
        Args:
            list_objs (list): object list to save
        Returns:
            json object to save in file
        """
        file_name = cls.__name__ + ".json"
        string = []
        if list_objs is not None:
            for i in list_objs:
                string.append(cls.to_dictionary(i))
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(cls.to_json_string(string))

    @staticmethod
    def from_json_string(json_string):
        """list of json to string representation
        Args:
            json_string (string): json object
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create
        Args:
            dictionary (dict): dictionary
        Return:
            An instance with all attributer already set
        """
        if cls.__name__ == "Rectangle":
            temp = cls(1, 1)
        if cls.__name__ == "Square":
            temp = cls(1)
        temp.update(**dictionary)
        return temp

    @classmethod
    def load_from_file(cls):
        """Load from file
        Return:
            A list of instances
        """
        file_name = cls.__name__ + ".json"
        json_obj = []
        try:
            with open(file_name, 'r', encoding='utf-8') as file:
                json_obj = cls.from_json_string(file.read())
            for key, value in enumerate(json_obj):
                json_obj[key] = cls.create(**json_obj[key])
        except:
            pass
        return json_obj
