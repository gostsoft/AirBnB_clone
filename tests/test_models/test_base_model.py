#!/usr/bin/python3
"""Testing BaseModel using unitest"""


import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Testing BaseModel"""

    m = BaseModel()

    def test_id(self):
        """Tests if instance has an id"""
        self.assertTrue(hasattr(TestBaseModel.m, 'id'))

    def test_id_str(self):
        """ Tests if id is str"""
        self.assertTrue(type(TestBaseModel.m.id) is str)

    def test_id_unique(self):
        """Tests if id is unique"""
        temp = BaseModel()
        self.assertNotEqual(TestBaseModel.m, temp)

    def test_str_repr(self):
        """Tests if string representation is correct"""
        st = f"[BaseModel] ({TestBaseModel.m.id}) {TestBaseModel.m.__dict__}"
        self.assertEqual(str(TestBaseModel.m), st)

    def test_created_at(self):
        """Tests if created_at is datetime"""
        self.assertTrue(type(TestBaseModel.m.created_at) is datetime)

    def test_updated_at(self):
        """Tests if updated_at is datetime"""
        self.assertTrue(type(TestBaseModel.m.updated_at) is datetime)

    def test_save(self):
        """Tests if save updates updated_at"""
        temp = TestBaseModel.m
        temp.save()
        self.assertNotEqual(temp.created_at, temp.updated_at)
        self.assertGreater(temp.updated_at.microsecond,
                           temp.created_at.microsecond)

    def test_to_dict(self):
        """Tests if to_dict() returns a dict object"""
        self.assertTrue(type(TestBaseModel.m.to_dict()) is dict)

    def test_kwarg(self):
        """Tets if kwargs is used to settattr from dict"""
        temp = BaseModel(name="base")
        self.assertEqual(type(temp).__name__, "BaseModel")
        self.assertFalse(hasattr(temp, "id"))
        self.assertFalse(hasattr(temp, "created_at"))
        self.assertTrue(hasattr(temp, "name"))
        self.assertFalse(hasattr(temp, "updated_at"))
        self.assertTrue(hasattr(temp, "__class__"))

    def test_empty_kwargs(self):
        """Tests if id, created_at and updated_at
        are initiatilzed if not in kwargs"""
        temp_dic = {}
        temp = BaseModel(**temp_dic)
        self.assertTrue(type(temp.id) is str)
        self.assertTrue(type(temp.created_at) is datetime)
        self.assertTrue(type(temp.updated_at) is datetime)


if __name__ == "__main__":
    unittest.main()