#!/usr/bin/python3
"""Place the class that derives from BaseClass here."""
from models.base_model import BaseModel


class Place(BaseModel):
    """creates a new Place instance."""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0
    longitude = 0
    amenity_ids = []
