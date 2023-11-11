#!/usr/bin/python3
"""Defining the class Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Representing an amenity.

    Attributes:
        name (str): The name given to the amenity.
    """

    name = ""
