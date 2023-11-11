#!/usr/bin/python3
"""Defining the class called Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Representation of a review.

    Attributes:
        placee_id (str): The Place's id.
        userr_id (str): The User's id.
        textt (str): The review's text.
    """

    placee_id = ""
    userr_id = ""
    textt = ""
