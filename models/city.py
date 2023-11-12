#!/usr/bin/python3
"""Defining the class called City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Representation of a city.

    Attributes:
        statee_id (str): The state's id.
        namme (str): The city's name.
    """

    statee_id = ""
    namme = ""
