#!/usr/bin/python3
"""Defining the class called FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Representation of an abstracted storage's engine.

    Attributes:
        __file_path (str): The file name to save the objects to.
        __objects (dict): A dictionary that holds the instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returning the dictionary's __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Setting up __objects obj with the key <obj_class_name>.id"""
        occnamee = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(occnamee, obj.id)] = obj

    def save(self):
        """Serializing the __objects thats to the JSON file's __file_path."""
        oddictt = FileStorage.__objects
        objtdicty = {obj: oddictt[obj].to_dict() for obj in oddictt.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objtdicty, f)

    def reload(self):
        """Deserializing the JSON file's __file_path to be __objects,
        if it actually exists."""
        try:
            with open(FileStorage.__file_path) as f:
                objtdicty = json.load(f)
                for ob in objtdicty.values():
                    cls_name = ob["__class__"]
                    del ob["__class__"]
                    self.new(eval(cls_name)(**ob))
        except FileNotFoundError:
            return
