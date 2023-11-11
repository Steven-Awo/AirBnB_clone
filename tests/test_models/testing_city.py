#!/usr/bin/python3
"""Defining the unittests for the models/city.py.

Unittest classes:
    TestingCity_instantiation
    TestingCity_save
    TestingCity_to_dict
"""
import os

import unittest

import models

from datetime import datetime

from time import sleep

from models.city import City


class TestCity_instantiation(unittest.TestCase):
    """Unittests that is for testing the instantiation of the
    City class."""

    def testing_no_argss_instantiates(self):
        self.assertEqual(City, type(City()))

    def testing_new_instance_storedd_in_objects(self):
        self.assertIn(City(), models.storage.all().values())

    def testing_id_iss_public_str(self):
        self.assertEqual(str, type(City().id))

    def testing_created_at_iss_public_datetime(self):
        self.assertEqual(datetime, type(City().created_at))

    def testing_updated_at_iss_public_datetime(self):
        self.assertEqual(datetime, type(City().updated_at))

    def testing_state_id_is_public_class_attribute(self):
        cyy = City()
        self.assertEqual(str, type(City.statee_id))
        self.assertIn("statee_id", dir(cyy))
        self.assertNotIn("statee_id", cyy.__dict__)

    def testing_name_is_public_class_attribute(self):
        cyy = City()
        self.assertEqual(str, type(City.namme))
        self.assertIn("namme", dir(cyy))
        self.assertNotIn("namme", cyy.__dict__)

    def testing_two_cities_unique_ids(self):
        cy11 = City()
        cy22 = City()
        self.assertNotEqual(cy11.id, cy22.id)

    def testing_two_cities_different_created_at(self):
        cy11 = City()
        sleep(0.05)
        cy22 = City()
        self.assertLess(cy11.created_at, cy22.created_at)

    def testing_two_cities_different_updated_at(self):
        cy11 = City()
        sleep(0.05)
        cy22 = City()
        self.assertLess(cy11.updated_at, cy22.updated_at)

    def testing_str_representation(self):
        dtt = datetime.today()
        dtt_reprr = repr(dtt)
        cyy = City()
        cyy.id = "123456"
        cyy.created_at = cyy.updated_at = dtt
        cystr = cyy.__str__()
        self.assertIn("[City] (123456)", cystr)
        self.assertIn("'id': '123456'", cystr)
        self.assertIn("'created_at': " + dtt_reprr, cystr)
        self.assertIn("'updated_at': " + dtt_reprr, cystr)

    def testing_args_unused(self):
        cyy = City(None)
        self.assertNotIn(None, cyy.__dict__.values())

    def testing_instantiation_with_kwargs(self):
        dtt = datetime.today()
        dtt_isoo = dtt.isoformat()
        cyy = City(id="345", created_at=dtt_isoo, updated_at=dtt_isoo)
        self.assertEqual(cyy.id, "345")
        self.assertEqual(cyy.created_at, dtt)
        self.assertEqual(cyy.updated_at, dtt)

    def testing_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)


class TestCity_save(unittest.TestCase):
    """Unittests that is for testing the save method of
    the City class."""

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
        cyy = City()
        sleep(0.05)
        the_first_updatedd_at = cyy.updated_at
        cyy.save()
        self.assertLess(the_first_updatedd_at, cyy.updated_at)

    def testing_two_saves(self):
        cyy = City()
        sleep(0.05)
        the_first_updatedd_at = cyy.updated_at
        cyy.save()
        the_second_updatedd_at = cyy.updated_at
        self.assertLess(the_first_updatedd_at, the_second_updatedd_at)
        sleep(0.05)
        cyy.save()
        self.assertLess(the_second_updatedd_at, cyy.updated_at)

    def testing_save_with_arg(self):
        cyy = City()
        with self.assertRaises(TypeError):
            cyy.save(None)

    def testing_save_updates_file(self):
        cyy = City()
        cyy.save()
        cyid = "City." + cyy.id
        with open("file.json", "r") as f:
            self.assertIn(cyid, f.read())


class TestCity_to_dict(unittest.TestCase):
    """Unittests that is for testing the to_dict method of
    the City class."""

    def testing_to_dict_type(self):
        self.assertTrue(dict, type(City().to_dict()))

    def testing_to_dict_contains_correct_keys(self):
        cyy = City()
        self.assertIn("id", cyy.to_dict())
        self.assertIn("created_at", cyy.to_dict())
        self.assertIn("updated_at", cyy.to_dict())
        self.assertIn("__class__", cyy.to_dict())

    def testing_to_dict_contains_added_attributes(self):
        cyy = City()
        cyy.middle_name = "Holberton"
        cyy.my_number = 98
        self.assertEqual("Holberton", cyy.middle_name)
        self.assertIn("my_number", cyy.to_dict())

    def testing_to_dict_datetime_attributes_are_strs(self):
        cyy = City()
        cy_dict = cyy.to_dict()
        self.assertEqual(str, type(cy_dict["id"]))
        self.assertEqual(str, type(cy_dict["created_at"]))
        self.assertEqual(str, type(cy_dict["updated_at"]))

    def testing_to_dict_output(self):
        dtt = datetime.today()
        cyy = City()
        cyy.id = "123456"
        cyy.created_at = cyy.updated_at = dtt
        tdict = {
            'id': '123456',
            '__class__': 'City',
            'created_at': dtt.isoformat(),
            'updated_at': dtt.isoformat(),
        }
        self.assertDictEqual(cyy.to_dict(), tdict)

    def testing_contrast_to_dict_dunder_dict(self):
        cyy = City()
        self.assertNotEqual(cyy.to_dict(), cyy.__dict__)

    def testing_to_dict_with_arg(self):
        cyy = City()
        with self.assertRaises(TypeError):
            cyy.to_dict(None)


if __name__ == "__main__":
    unittest.main()

