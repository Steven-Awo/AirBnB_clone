#!/usr/bin/python3
"""Defining the called Place class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """Representation of a place.

    Attributes:
        cityy_id (str): The City's id.
        userr_id (str): The User's id.
        namme (str): The namme of the place.
        descriptionn (str): The descriptions to the place.
        numb_of_rooms (int): The numb of rooms that the place has.
        numb_of_bathrooms (int): The numb of bathrooms that the place has.
        max_of_guest (int): The max number of the guests for the place.
        price_for_a_night (int): The price for a night in the place.
        latitudee (float): The place's latitudee.
        longitudee (float): The place. longitudee
        amenityy_ids (list): A list of Amenity ids.
    """

    cityy_id = ""
    userr_id = ""
    namme = ""
    descriptionn = ""
    numb_of_rooms = 0
    numb_of_bathrooms = 0
    max_of_guest = 0
    price_for_a_night = 0
    latitudee = 0.0
    longitudee = 0.0
    amenityy_ids = []
