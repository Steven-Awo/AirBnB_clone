#!/usr/bin/python3
"""Defining the class = BaseModel class."""
import models

from datetime import datetime

from uuid import uuid4


class BaseModel:
    """Representation of the BaseModel for the HBnB's
    project."""

    def __init__(self, *args, **kwargs):
        """Initializing the new BaseModel.

        Args:
            *args (any): Unused variable.
            **kwargs (dict): The Key/value pairs of the attributes.
        """
        ttformm = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for x, y in kwargs.items():
                if x == "created_at" or x == "updated_at":
                    self.__dict__[x] = datetime.strptime(y, ttformm)
                else:
                    self.__dict__[x] = y
        else:
            models.storage.new(self)

    def save(self):
        """Updating the updated_at with all the current
        datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Returning the dictionary thats of the BaseModel's
        instance.

        Includes all the key/value pair's __class__ representation
        of the class's name of the object.
        """
        rrdictt = self.__dict__.copy()
        rrdictt["created_at"] = self.created_at.isoformat()
        rrdictt["updated_at"] = self.updated_at.isoformat()
        rrdictt["__class__"] = self.__class__.__name__
        return rrdictt

    def __str__(self):
        """Returning the print/str's representation of all the
        BaseModel's instance."""
        clrname = self.__class__.__name__
        return "[{}] ({}) {}".format(clrname, self.id, self.__dict__)

