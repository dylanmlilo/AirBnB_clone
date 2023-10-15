#!/usr/bin/python3
""" Defines the Place class """
from models.base_model import BaseModel


class Place(BaseModel):
    """ Defines the Place class that inherits from BaseModel"""
    amenity_ids = []
    city_id = ""
    description = ""
    latitude = 0.0
    longitude = 0.0
    max_guest = 0
    name = ""
    number_bathrooms = 0
    number_rooms = 0
    price_by_night = 0
    user_id = ""
