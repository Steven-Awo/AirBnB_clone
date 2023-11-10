#!/usr/bin/python3
"""Defining the unittests thats for the models/base_model.py.

Unittest classes:
    TestingBaseModel_instantiation
    TestinngBaseModel_save
    TestingBaseModel_to_dict
"""
import os

import unittest

import models

from datetime import datetime

from time import sleep

from models.base_model import BaseModel


class TestBaseModel_instantiation(unittest.TestCase):
    """Unittests thats for testing instantiation of the
    BaseModel class."""

    def testing_no_argss_instantiates(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def testing_new_instance_storedd_in_objects(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def testing_id_iss_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def testing_created_at_iss_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def testing_updated_at_iss_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def testing_two_models_unique_ids(self):
        bm11 = BaseModel()
        bm22 = BaseModel()
        self.assertNotEqual(bm11.id, bm22.id)

    def testing_two_models_differentt_created_at(self):
        bm11 = BaseModel()
        sleep(0.05)
        bm22 = BaseModel()
        self.assertLess(bm11.created_at, bm22.created_at)

    def testing_two_models_differentt_updated_at(self):
        bm11 = BaseModel()
        sleep(0.05)
        bm22 = BaseModel()
        self.assertLess(bm11.updated_at, bm22.updated_at)

    def testing_strr_representation(self):
        dtt = datetime.today()
        dt_repr = repr(dtt)
        bmm = BaseModel()
        bmm.id = "123456"
        bmm.created_at = bmm.updated_at = dtt
        bmstr = bmm.__str__()
        self.assertIn("[BaseModel] (123456)", bmstr)
        self.assertIn("'id': '123456'", bmstr)
        self.assertIn("'created_at': " + dt_repr, bmstr)
        self.assertIn("'updated_at': " + dt_repr, bmstr)

    def testing_argss_unused(self):
        bmm = BaseModel(None)
        self.assertNotIn(None, bmm.__dict__.values())

    def testing_instantiation_withh_kwargs(self):
        dtt = datetime.today()
        dt_iso = dtt.isoformat()
        bmm = BaseModel(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bmm.id, "345")
        self.assertEqual(bmm.created_at, dtt)
        self.assertEqual(bmm.updated_at, dtt)

    def testing_instantiation_withh_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def testing_instantiation_withh_args_andd_kwargs(self):
        dtt = datetime.today()
        dt_iso = dtt.isoformat()
        bmm = BaseModel("12", id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bmm.id, "345")
        self.assertEqual(bmm.created_at, dtt)
        self.assertEqual(bmm.updated_at, dtt)


class TestBaseModel_save(unittest.TestCase):
    """Unittests thats for testing save method of the BaseModel class."""

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

    def testing_one_save(self):
        bmm = BaseModel()
        sleep(0.05)
        the_firstt_updated_at = bmm.updated_at
        bmm.save()
        self.assertLess(the_firstt_updated_at, bmm.updated_at)

    def testing_two_saves(self):
        bmm = BaseModel()
        sleep(0.05)
        the_firstt_updated_at = bmm.updated_at
        bmm.save()
        the_secondd_updated_at = bmm.updated_at
        self.assertLess(the_firstt_updated_at, the_secondd_updated_at)
        sleep(0.05)
        bmm.save()
        self.assertLess(the_secondd_updated_at, bmm.updated_at)

    def testing_save_with_arg(self):
        bmm = BaseModel()
        with self.assertRaises(TypeError):
            bmm.save(None)

    def testing_save_updates_file(self):
        bmm = BaseModel()
        bmm.save()
        bmid = "BaseModel." + bmm.id
        with open("file.json", "r") as f:
            self.assertIn(bmid, f.read())


class TestBaseModel_to_dict(unittest.TestCase):
    """Unittests thats for testing the to_dict method of the
    BaseModel class."""

    def testing_to_dict_type(self):
        bmm = BaseModel()
        self.assertTrue(dict, type(bmm.to_dict()))

    def testing_to_dict_contains_correct_keys(self):
        bmm = BaseModel()
        self.assertIn("id", bmm.to_dict())
        self.assertIn("created_at", bmm.to_dict())
        self.assertIn("updated_at", bmm.to_dict())
        self.assertIn("__class__", bmm.to_dict())

    def testing_to_dict_contains_added_attributes(self):
        bmm = BaseModel()
        bmm.name = "Holberton"
        bmm.my_number = 98
        self.assertIn("name", bmm.to_dict())
        self.assertIn("my_number", bmm.to_dict())

    def testing_to_dict_datetime_attributes_are_strs(self):
        bmm = BaseModel()
        bmm_dictt = bmm.to_dict()
        self.assertEqual(str, type(bmm_dictt["created_at"]))
        self.assertEqual(str, type(bmm_dictt["updated_at"]))

    def testing_to_dict_output(self):
        dtt = datetime.today()
        bmm = BaseModel()
        bmm.id = "123456"
        bmm.created_at = bmm.updated_at = dtt
        tdict = {
            'id': '123456',
            '__class__': 'BaseModel',
            'created_at': dtt.isoformat(),
            'updated_at': dtt.isoformat()
        }
        self.assertDictEqual(bmm.to_dict(), tdict)

    def testing_contrast_to_dict_dunder_dict(self):
        bmm = BaseModel()
        self.assertNotEqual(bmm.to_dict(), bmm.__dict__)

    def testing_to_dict_with_arg(self):
        bmm = BaseModel()
        with self.assertRaises(TypeError):
            bmm.to_dict(None)


if __name__ == "__main__":
    unittest.main()

