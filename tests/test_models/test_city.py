#!/usr/bin/python3
"""Testing City class with unittest"""
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """Testing City Class"""

    c = City()
    alist = ["state_id", "name"]

    def test_city_is_subclass_of_basemodel(self):
        """Tests if city is a subclass of BaseModel"""
        self.assertTrue(issubclass(type(TestCity.c), BaseModel))

    def test_attrs_are_class_attrs(self):
        """test if attributes are class attributes"""
        for attr in TestCity.alist:
            self.assertIs(type(getattr(TestCity.c, attr)), str)
            self.assertFalse(bool(getattr(TestCity.c, attr)))
