#!/usr/bin/python3
"""Testing FileStorage using unittest"""
import unittest
import models
from models import base_model
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.place import Place


class TestFileStorageInit(unittest.TestCase):
    """Testing FileStorage class"""

    def test_file_path_is_private(self):
        """Tests if __file_path is private"""
        self.assertFalse(hasattr(FileStorage(), "__file_path"))

    def test_objects_is_private(self):
        """tests if __objects is private"""
        self.assertFalse(hasattr(FileStorage(), "__objects"))

    def test_init_without_arg(self):
        """Tests initialization without args"""
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_init_with_arg(self):
        """Tests initialization with args"""
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_storage_init(self):
        """Tests storage created in __init__.py"""
        self.assertEqual(type(models.storage), FileStorage)


if __name__ == "__main__":
    unittest.main()
