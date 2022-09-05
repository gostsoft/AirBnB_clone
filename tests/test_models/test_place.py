#!/usr/bin/python3
"""Testing place Class using unittest"""
import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """Testing Place class"""

    p = Place()
    alist = ["name", "user_id", "city_id", "description",
             "number_bathrooms", "max_guest", "number_rooms",
             "price_by_night", "latitude", "longitude", "amenity_ids"]

    def test_place_obj_is_a_subclass_of_basemodel(self):
        """Tests Place is subclass of BaseModel"""
        self.assertTrue(issubclass(type(TestPlace.p), BaseModel))

    def test_attrs_are_class_attrs(self):
        """test attributes are class attributes"""
        for attr in TestPlace.alist:
            self.assertTrue(hasattr(Place, attr))

    def test_class_attrs(self):
        """Test all class attributes"""
        self.assertIs(type(TestPlace.p.name), str)
        self.assertIs(type(TestPlace.p.city_id), str)
        self.assertIs(type(TestPlace.p.user_id), str)
        self.assertIs(type(TestPlace.p.description), str)
        self.assertIs(type(TestPlace.p.number_bathrooms), int)
        self.assertIs(type(TestPlace.p.max_guest), int)
        self.assertIs(type(TestPlace.p.number_rooms), int)
        self.assertIs(type(TestPlace.p.price_by_night), int)
        self.assertIs(type(TestPlace.p.amenity_ids), list)
