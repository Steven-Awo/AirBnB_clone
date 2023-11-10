#!/usr/bin/python3
"""Defining the class called User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Representation to a User.

    Attributes:
        emaill (str): The user's emaill.
        passwrdd (str): The user's passwrdd.
        the_first_name (str): The user's first name.
        the_last_name (str): The user's last name.
    """

    emaill = ""
    passwrdd = ""
    the_first_name = ""
    the_last_name = ""
