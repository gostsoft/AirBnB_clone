#!/usr/bin/python3
"""Testing Amenity class using unittest"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Testing Amenity class"""

    a = Amenity()

    def test_amenity_is_subclass(self):
        """Tests if is Subclass of BaseModel"""
        self.assertTrue(issubclass(type(TestAmenity.a), BaseModel))

    def test_attr_is_class_attr(self):
        """Tests if attribute is class attribute"""
        self.assertTrue(hasattr(TestAmenity.a, "name"))

    def test_class_attr(self):
        """Tests if is class attribute"""
        self.assertIs(type(TestAmenity.a.name), str)
        self.assertFalse(bool(getattr(TestAmenity.a, "name")))

    def test_Amenity_dict(self):
        """Tests Amenity_dict"""
        self.assertTrue('id' in TestAmenity.a.__dict__)
        self.assertTrue('created_at' in TestAmenity.a.__dict__)
        self.assertTrue('updated_at' in TestAmenity.a.__dict__)

    def test_save_Amenity(self):
        """Tests Amenity save"""
        TestAmenity.a.save()
        self.assertNotEqual(TestAmenity.a.created_at, TestAmenity.a.updated_at)


if __name__ == '__main__':
    unittest.main()
