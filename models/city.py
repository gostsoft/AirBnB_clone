#!/usr/bin/python3
"""City class descended from BaseClass."""

from models.base_model import BaseModel


class City(BaseModel):
    """makes a city object."""

    state_id = ""
    name = ""
