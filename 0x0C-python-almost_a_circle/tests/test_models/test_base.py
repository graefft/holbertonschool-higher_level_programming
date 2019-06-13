#!/usr/bin/python3
"""Unittest for Base class"""

import json
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """Tests for Base class"""

    @classmethod
    def setUpClass(cls):
        """sets up class"""
        Base._Base__nb_objects = 0
        cls.b1 = Base()
        cls.b2 = Base()
        cls.b3 = Base()
        cls.b4 = Base(12)
        cls.b5 = Base()

    def test_0_create_0(self):
        """tests for creation"""
        self.assertTrue(self.b1)

    def test_0_create_1(self):
        """tests for creation with id"""
        self.assertEqual(self.b4.id, 12)

    def test_0_create_2(self):
        """tests for correct ids"""
        Base.initialize()
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(42)
        b5 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 42)
        self.assertEqual(b5.id, 4)

    def test_0_create_3(self):
        """test for negative id"""
        b6 = Base(-6)
        self.assertEqual(b6.id, -6)

    def test_0_create_4(self):
        """test for string id"""
        b7 = Base("Hello")
        self.assertEqual(b7.id, "Hello")

    def test_0_create_5(self):
        """test for list id"""
        b8 = Base([3, 2, 1])
        self.assertEqual(b8.id, [3, 2, 1])

    def test_0_create_6(self):
        """test for dict id"""
        b9 = Base({"Student": "Thomas"})
        self.assertEqual(b9.id, {"Student": "Thomas"})

    def test_0_create_7(self):
        """test for tuple id"""
        b10 = Base((1, 2, 3))
        self.assertEqual(b10.id, (1, 2, 3))

    def test_0_create_8(self):
        """test for float id"""
        b11 = Base(5.5)
        self.assertEqual(b11.id, 5.5)

    def test_0_create_9(self):
        """test for None id"""
        Base.initialize()
        b12 = Base(None)
        self.assertEqual(b12.id, 1)

    def test_0_create_10(self):
        """test for 0 id"""
        b13 = Base(0)
        self.assertEqual(b13.id, 0)

    def test_1_type_1(self):
        """test if __nb_objects is private"""
        with self.assertRaises(AttributeError) as e:
            print(Base.__nb_objects)
        self.assertEqual(str(e.exception), "type object 'Base' has no" +
                         " attribute '_TestBase__nb_objects'")

    def test_1_type_2(self):
        """test if json string is string"""
        json_dict = Base.to_json_string("Hi")
        self.assertEqual(type(json_dict), str)

    def test_2_json_1(self):
        """test to_json_string with None"""
        json_dict = Base.to_json_string(None)
        self.assertEqual(json_dict, "[]")

    def test_2_json_2(self):
        """test to_json_string with NaN"""
        with self.assertRaises(TypeError) as e:
            json_dict = Base.to_json_string(float('NaN'))
        self.assertEqual(str(e.exception), "object of type \'float\'" +
                         " has no len()")

    def test_3_save_to_1(self):
        """test save_to_file with no arguments"""
        with self.assertRaises(TypeError) as e:
            result = Base.save_to_file()
        self.assertEqual('save_to_file() missing 1 required positional' +
                         ' argument: \'list_objs\'', str(e.exception))

    def test_3_save_to_2(self):
        """test save_to_file with None"""
        Base.save_to_file([])
        with open('Base.json', 'r') as f:
            self.assertEqual(f.read(), "[]")