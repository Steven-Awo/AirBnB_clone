#!/usr/bin/python3
"""Defining the unittests for the models/amenity.py.

Unittest classes:
    TestAmenity_instantiation
    TestAmenity_save
    TestAmenity_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenity_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Amenity class."""

    def testing_no_args_instantiates(self):
        self.assertEqual(Amenity, type(Amenity()))

    def testing_new_instance_stored_in_objects(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def testing_id_is_public_str(self):
        self.assertEqual(str, type(Amenity().id))

    def testing_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def testing_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def testing_name_is_public_class_attribute(self):
        amm = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", amm.__dict__)

    def testing_two_amenities_unique_ids(self):
        am11 = Amenity()
        am22 = Amenity()
        self.assertNotEqual(am11.id, am22.id)

    def testing_two_amenities_different_created_at(self):
        am11 = Amenity()
        sleep(0.05)
        am22 = Amenity()
        self.assertLess(am11.created_at, am22.created_at)

    def testing_two_amenities_different_updated_at(self):
        am11 = Amenity()
        sleep(0.05)
        am22 = Amenity()
        self.assertLess(am11.updated_at, am22.updated_at)

    def testing_str_representation(self):
        dtt = datetime.today()
        dtt_reprr = repr(dtt)
        amm = Amenity()
        amm.id = "123456"
        amm.created_at = amm.updated_at = dtt
        amstr = amm.__str__()
        self.assertIn("[Amenity] (123456)", amstr)
        self.assertIn("'id': '123456'", amstr)
        self.assertIn("'created_at': " + dtt_reprr, amstr)
        self.assertIn("'updated_at': " + dtt_reprr, amstr)

    def testing_args_unused(self):
        amm = Amenity(None)
        self.assertNotIn(None, amm.__dict__.values())

    def testing_instantiation_with_kwargs(self):
        """instantiation that is with kwargs's testing method"""
        dtt = datetime.today()
        dtt_iso = dtt.isoformat()
        amm = Amenity(id="345", created_at=dtt_iso, updated_at=dtt_iso)
        self.assertEqual(amm.id, "345")
        self.assertEqual(amm.created_at, dtt)
        self.assertEqual(amm.updated_at, dtt)

    def testing_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)


class TestAmenity_save(unittest.TestCase):
    """Unittests that is for testing the saved method of the
    Amenity class."""

    @classmethod
    def setsUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

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
        amm = Amenity()
        sleep(0.05)
        the_first_updated_at = amm.updated_at
        amm.save()
        self.assertLess(the_first_updated_at, amm.updated_at)

    def testing_two_saves(self):
        amm = Amenity()
        sleep(0.05)
        the_first_updated_at = amm.updated_at
        amm.save()
        the_second_updatedd_at = amm.updated_at
        self.assertLess(the_first_updated_at, the_second_updatedd_at)
        sleep(0.05)
        amm.save()
        self.assertLess(the_second_updatedd_at, amm.updated_at)

    def testing_save_with_arg(self):
        amm = Amenity()
        with self.assertRaises(TypeError):
            amm.save(None)

    def testing_save_updates_file(self):
        amm = Amenity()
        amm.save()
        amid = "Amenity." + amm.id
        with open("file.json", "r") as f:
            self.assertIn(amid, f.read())


class TestAmenity_to_dict(unittest.TestCase):
    """Unittests that is for testing the to_dict method of the
    Amenity class."""

    def testing_to_dict_type(self):
        self.assertTrue(dict, type(Amenity().to_dict()))

    def testing_to_dict_contains_correct_keys(self):
        amm = Amenity()
        self.assertIn("id", amm.to_dict())
        self.assertIn("created_at", amm.to_dict())
        self.assertIn("updated_at", amm.to_dict())
        self.assertIn("__class__", amm.to_dict())

    def testing_to_dict_contains_added_attributes(self):
        amm = Amenity()
        amm.middle_name = "Holberton"
        amm.my_number = 98
        self.assertEqual("Holberton", amm.middle_name)
        self.assertIn("my_number", amm.to_dict())

    def testing_to_dict_datetime_attributes_are_strs(self):
        amm = Amenity()
        amm_dicty = amm.to_dict()
        self.assertEqual(str, type(amm_dicty["id"]))
        self.assertEqual(str, type(amm_dicty["created_at"]))
        self.assertEqual(str, type(amm_dicty["updated_at"]))

    def testing_to_dict_output(self):
        dtt = datetime.today()
        amm = Amenity()
        amm.id = "123456"
        amm.created_at = amm.updated_at = dtt
        tdict = {
            'id': '123456',
            '__class__': 'Amenity',
            'created_at': dtt.isoformat(),
            'updated_at': dtt.isoformat(),
        }
        self.assertDictEqual(amm.to_dict(), tdict)

    def testing_contrast_to_dict_dunder_dict(self):
        amm = Amenity()
        self.assertNotEqual(amm.to_dict(), amm.__dict__)

    def testing_to_dict_with_arg(self):
        amm = Amenity()
        with self.assertRaises(TypeError):
            amm.to_dict(None)


if __name__ == "__main__":
    unittest.main()

