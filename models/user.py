#!/usr/bin/python3
"""user class that derives from BaseModel."""

from models.base_model import BaseModel


class User(BaseModel):
    """This method creates a new User object."""

    email = ""
    password = ""
    first_name = ""
    lastname = ""
