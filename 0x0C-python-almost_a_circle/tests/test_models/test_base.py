#!/usr/bin/python3
""" Unittest base
Test cases for Base class
"""


import unittest
import os
from models.base import Base


class TestBase(unittest.TestCase):
    """ Test class Base """

    def setUp(self):
        """ Test class setup"""
        Base._Base__nb_objects = 0
    
    # Task 1
    def test_001_0(self):
        """ Creating a new instance of Base class. Check attribute id """
        
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
        b5 = Base()
        self.assertEqual(b5.id, 5)
        b6 = Base(-6)
        self.assertEqual(b6.id, -6)

    def test_001_0(self):
        """ Test the type and instance"""
        
        # create an instance
        b7 = Base()
        self.assertEqual(type(b7), Base)
        self.assertTrue(isinstance(b7, Base))


    # Task 15
    def test_015_0(self):
        """Test static method to_json_string with regular dict."""

        d = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        json_d = Base.to_json_string([d])
        self.assertTrue(isinstance(d, dict))
        self.assertTrue(isinstance(json_d, str))
        self.assertCountEqual(
            json_d, '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]')
        json_d_1 = Base.to_json_string([])
        self.assertEqual(json_d_1, "[]")
        json_d_2 = Base.to_json_string(None)
        self.assertEqual(json_d_1, "[]")

    def test_015_1(self):
        """Test static method to_json_string with wrong types."""

        with self.assertRaises(TypeError) as x:
            Base.to_json_string(9)
        self.assertEqual(
            "list_dictionaries must be a list of dictionaries", str(
                x.exception))
        with self.assertRaises(TypeError) as x:
            Base.to_json_string("Hello")
        self.assertEqual(
            "list_dictionaries must be a list of dictionaries", str(
                x.exception))
        with self.assertRaises(TypeError) as x:
            Base.to_json_string(["Hi", "Here"])
        self.assertEqual(
            "list_dictionaries must be a list of dictionaries", str(
                x.exception))
        with self.assertRaises(TypeError) as x:
            Base.to_json_string(7.8)
        self.assertEqual(
            "list_dictionaries must be a list of dictionaries", str(
                x.exception))
        with self.assertRaises(TypeError) as x:
            Base.to_json_string([2, 1, 3, 4])
        self.assertEqual(
            "list_dictionaries must be a list of dictionaries", str(
                x.exception))
        with self.assertRaises(TypeError) as x:
            Base.to_json_string({1: 'hi', 2: 'there'})
        self.assertEqual(
            "list_dictionaries must be a list of dictionaries", str(
                x.exception))
        with self.assertRaises(TypeError) as x:
            Base.to_json_string((9, 0))
        self.assertEqual(
            "list_dictionaries must be a list of dictionaries", str(
                x.exception))
        with self.assertRaises(TypeError) as x:
            Base.to_json_string(True)
        self.assertEqual(
            "list_dictionaries must be a list of dictionaries", str(
                x.exception))

    def test_015_2(self):
        """Test static method to_json_string with wrong number of args."""

        s1 = ("to_json_string() missing 1 required positional argument: " +
              "'list_dictionaries'")
        with self.assertRaises(TypeError) as x:
            Base.to_json_string()
        self.assertEqual(s1, str(x.exception))
        s2 = "to_json_string() takes 1 positional argument but 2 were given"
        with self.assertRaises(TypeError) as x:
            Base.to_json_string([{1, 2}], [{3, 4}])
        self.assertEqual(s2, str(x.exception))
