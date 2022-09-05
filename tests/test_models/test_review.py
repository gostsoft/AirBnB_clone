#!/usr/bin/python3
"""Testing Review class using unittest"""
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """Testing Review class"""

    r = Review()
    alist = [
            "place_id",
            "user_id",
            "text"
            ]

    def test_review_is_subclass(self):
        """Test Review is subclass of BaseModel"""
        self.assertTrue(issubclass(type(TestReview.r), BaseModel))

    def test_attr_is_class_attr(self):
        """Test attribute is class attribute"""
        for attr in TestReview.alist:
            self.assertTrue(hasattr(TestReview.r, attr))

    def test_class_attrs(self):
        """Test attributes are class attributes"""
        for attr in TestReview.alist:
            self.assertIs(type(getattr(TestReview.r, attr)), str)
            self.assertFalse(bool(getattr(TestReview.r, attr)))
