#!/usr/bin/python3
"""Testing State Class using unittest"""
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """Testing State class"""

    s = State()

    def test_state_a_subclass(self):
        """Tests if is Subclass of BaseModel"""
        self.assertTrue(issubclass(type(TestState.s), BaseModel))

    def test_attr_is_class_attr(self):
        """Test if is Class attribute"""
        self.assertTrue(hasattr(TestState.s, "name"))

    def test_class_attrs(self):
        """Tests if class attributes are class attributes"""
        self.assertIs(type(TestState.s.name), str)
        self.assertFalse(bool(TestState.s.name))
