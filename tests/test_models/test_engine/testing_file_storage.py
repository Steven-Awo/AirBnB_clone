#!/usr/bin/python3
"""Defining the unittests thats for the models/engine/file_storage.py.

Unittest classes:
    TestFileStorage_instantiation
    TestFileStorage_methods
"""
import os
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorage_instantiation(unittest.TestCase):
    """Unittests thats for testing the instantiation of the
    FileStorage class."""

    def testing_FileStorage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def testing_FileStorage_instantiation_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def testing_FileStorage_file_path_is_private_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_objects_is_private_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def testing_storage_initializes(self):
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorage_methods(unittest.TestCase):
    """Unittests thats for testing the methods of the
    FileStorage class."""

    @classmethod
    def setsUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearsDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def testing_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def testing_all_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def testing_new(self):
        bmm = BaseModel()
        usr = User()
        stte = State()
        pll = Place()
        cyy = City()
        amm = Amenity()
        rvv = Review()
        models.storage.new(bmm)
        models.storage.new(usr)
        models.storage.new(stte)
        models.storage.new(pll)
        models.storage.new(cyy)
        models.storage.new(amm)
        models.storage.new(rvv)
        self.assertIn("BaseModel." + bmm.id, models.storage.all().keys())
        self.assertIn(bmm, models.storage.all().values())
        self.assertIn("User." + usr.id, models.storage.all().keys())
        self.assertIn(usr, models.storage.all().values())
        self.assertIn("State." + stte.id, models.storage.all().keys())
        self.assertIn(stte, models.storage.all().values())
        self.assertIn("Place." + pll.id, models.storage.all().keys())
        self.assertIn(pll, models.storage.all().values())
        self.assertIn("City." + cyy.id, models.storage.all().keys())
        self.assertIn(cyy, models.storage.all().values())
        self.assertIn("Amenity." + amm.id, models.storage.all().keys())
        self.assertIn(amm, models.storage.all().values())
        self.assertIn("Review." + rvv.id, models.storage.all().keys())
        self.assertIn(rvv, models.storage.all().values())

    def testing_new_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def testing_save(self):
        bmm = BaseModel()
        usr = User()
        stte = State()
        pll = Place()
        cyy = City()
        amm = Amenity()
        rvv = Review()
        models.storage.new(bmm)
        models.storage.new(usr)
        models.storage.new(stte)
        models.storage.new(pll)
        models.storage.new(cyy)
        models.storage.new(amm)
        models.storage.new(rvv)
        models.storage.save()
        savee_text = ""
        with open("file.json", "r") as f:
            savee_text = f.read()
            self.assertIn("BaseModel." + bmm.id, savee_text)
            self.assertIn("User." + usr.id, savee_text)
            self.assertIn("State." + stte.id, savee_text)
            self.assertIn("Place." + pll.id, savee_text)
            self.assertIn("City." + cyy.id, savee_text)
            self.assertIn("Amenity." + amm.id, savee_text)
            self.assertIn("Review." + rvv.id, savee_text)

    def testing_save_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def testing_reload(self):
        bmm = BaseModel()
        usr = User()
        stte = State()
        pll = Place()
        cyy = City()
        amm = Amenity()
        rvv = Review()
        models.storage.new(bmm)
        models.storage.new(usr)
        models.storage.new(stte)
        models.storage.new(pll)
        models.storage.new(cyy)
        models.storage.new(amm)
        models.storage.new(rvv)
        models.storage.save()
        models.storage.reload()
        objjs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + bmm.id, objjs)
        self.assertIn("User." + usr.id, objjs)
        self.assertIn("State." + stte.id, objjs)
        self.assertIn("Place." + pll.id, objjs)
        self.assertIn("City." + cyy.id, objjs)
        self.assertIn("Amenity." + amm.id, objjs)
        self.assertIn("Review." + rvv.id, objjs)

    def testing_reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()

