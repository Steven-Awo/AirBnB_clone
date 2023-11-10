#!/usr/bin/python3
"""Defines unittests for models/place.py.

Unittest classes:
    TestingPlace_instantiation
    TestingPlace_save
    TestingPlace_to_dict
"""
import os

import unittest

import models

from datetime import datetime

from time import sleep

from models.place import Place


class TestPlace_instantiation(unittest.TestCase):
    """Unittests that's for testing the instantiation of
    the Place class."""

    def testing_no_argss_instantiates(self):
        self.assertEqual(Place, type(Place()))

    def testing_new_instance_storedd_in_objects(self):
        self.assertIn(Place(), models.storage.all().values())

    def testing_id_iss_public_str(self):
        self.assertEqual(str, type(Place().id))

    def testing_created_at_iss_public_datetime(self):
        self.assertEqual(datetime, type(Place().created_at))

    def testing_updated_at_iss_public_datetime(self):
        self.assertEqual(datetime, type(Place().updated_at))

    def testing_city_id_iss_public_class_attribute(self):
        pll = Place()
        self.assertEqual(str, type(Place.city_id))
        self.assertIn("city_id", dir(pll))
        self.assertNotIn("city_id", pll.__dict__)

    def testing_user_id_is_public_class_attribute(self):
        pll = Place()
        self.assertEqual(str, type(Place.user_id))
        self.assertIn("user_id", dir(pll))
        self.assertNotIn("user_id", pll.__dict__)

    def testing_name_is_public_class_attribute(self):
        pll = Place()
        self.assertEqual(str, type(Place.name))
        self.assertIn("name", dir(pll))
        self.assertNotIn("name", pll.__dict__)

    def testing_description_is_public_class_attribute(self):
        pll = Place()
        self.assertEqual(str, type(Place.description))
        self.assertIn("description", dir(pll))
        self.assertNotIn("desctiption", pll.__dict__)

    def testing_number_rooms_is_public_class_attribute(self):
        pll = Place()
        self.assertEqual(int, type(Place.number_rooms))
        self.assertIn("number_rooms", dir(pll))
        self.assertNotIn("number_rooms", pll.__dict__)

    def testing_number_bathrooms_is_public_class_attribute(self):
        pll = Place()
        self.assertEqual(int, type(Place.number_bathrooms))
        self.assertIn("number_bathrooms", dir(pll))
        self.assertNotIn("number_bathrooms", pll.__dict__)

    def testing_max_guest_is_public_class_attribute(self):
        pll = Place()
        self.assertEqual(int, type(Place.max_guest))
        self.assertIn("max_guest", dir(pll))
        self.assertNotIn("max_guest", pll.__dict__)

    def testing_price_by_night_is_public_class_attribute(self):
        pll = Place()
        self.assertEqual(int, type(Place.price_by_night))
        self.assertIn("price_by_night", dir(pll))
        self.assertNotIn("price_by_night", pll.__dict__)

    def testing_latitude_is_public_class_attribute(self):
        pll = Place()
        self.assertEqual(float, type(Place.latitude))
        self.assertIn("latitude", dir(pll))
        self.assertNotIn("latitude", pll.__dict__)

    def testing_longitude_is_public_class_attribute(self):
        pll = Place()
        self.assertEqual(float, type(Place.longitude))
        self.assertIn("longitude", dir(pll))
        self.assertNotIn("longitude", pll.__dict__)

    def testing_amenity_ids_is_public_class_attribute(self):
        pll = Place()
        self.assertEqual(list, type(Place.amenity_ids))
        self.assertIn("amenity_ids", dir(pll))
        self.assertNotIn("amenity_ids", pll.__dict__)

    def testing_two_places_unique_ids(self):
        pl1 = Place()
        pl2 = Place()
        self.assertNotEqual(pl1.id, pl2.id)

    def testing_two_places_different_created_at(self):
        pl1 = Place()
        sleep(0.05)
        pl2 = Place()
        self.assertLess(pl1.created_at, pl2.created_at)

    def testing_two_places_differentt_updated_at(self):
        pl1 = Place()
        sleep(0.05)
        pl2 = Place()
        self.assertLess(pl1.updated_at, pl2.updated_at)

    def testing_strr_representation(self):
        dtt = datetime.today()
        dtt_reprr = repr(dtt)
        pll = Place()
        pll.id = "123456"
        pll.created_at = pll.updated_at = dtt
        plsstrr = pll.__str__()
        self.assertIn("[Place] (123456)", plsstrr)
        self.assertIn("'id': '123456'", plsstrr)
        self.assertIn("'created_at': " + dtt_reprr, plsstrr)
        self.assertIn("'updated_at': " + dtt_reprr, plsstrr)

    def testing_args_unused(self):
        pll = Place(None)
        self.assertNotIn(None, pll.__dict__.values())

    def testing_instantiation_with_kwargs(self):
        dtt = datetime.today()
        dtt_isoo = dtt.isoformat()
        pll = Place(id="345", created_at=dtt_isoo, updated_at=dtt_isoo)
        self.assertEqual(pll.id, "345")
        self.assertEqual(pll.created_at, dtt)
        self.assertEqual(pll.updated_at, dtt)

    def testing_instantiation_withh_None_kwargs(self):
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)


class TestPlace_save(unittest.TestCase):
    """Unittests thats for testing the save method of
    the Place class."""

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
        pll = Place()
        sleep(0.05)
        the_first_updatedd_at = pll.updated_at
        pll.save()
        self.assertLess(the_first_updatedd_at, pll.updated_at)

    def testing_two_saves(self):
        pll = Place()
        sleep(0.05)
        the_first_updatedd_at = pll.updated_at
        pll.save()
        the_second_updatedd_at = pll.updated_at
        self.assertLess(the_first_updatedd_at, the_second_updatedd_at)
        sleep(0.05)
        pll.save()
        self.assertLess(the_second_updatedd_at, pll.updated_at)

    def testing_save_with_arg(self):
        pll = Place()
        with self.assertRaises(TypeError):
            pll.save(None)

    def testing_save_updates_file(self):
        pll = Place()
        pll.save()
        plid = "Place." + pll.id
        with open("file.json", "r") as f:
            self.assertIn(plid, f.read())


class TestPlace_to_dict(unittest.TestCase):
    """Unittests thats for testing the to_dict method of
    the Place class."""

    def testing_to_dict_type(self):
        self.assertTrue(dict, type(Place().to_dict()))

    def testing_to_dict_contains_correct_keys(self):
        pll = Place()
        self.assertIn("id", pll.to_dict())
        self.assertIn("created_at", pll.to_dict())
        self.assertIn("updated_at", pll.to_dict())
        self.assertIn("__class__", pll.to_dict())

    def testing_to_dict_contains_added_attributes(self):
        pll = Place()
        pll.middle_name = "Holberton"
        pll.my_number = 98
        self.assertEqual("Holberton", pll.middle_name)
        self.assertIn("my_number", pll.to_dict())

    def testing_to_dict_datetime_attributes_are_strs(self):
        pll = Place()
        pll_dictt = pll.to_dict()
        self.assertEqual(str, type(pll_dictt["id"]))
        self.assertEqual(str, type(pll_dictt["created_at"]))
        self.assertEqual(str, type(pll_dictt["updated_at"]))

    def testing_to_dict_output(self):
        dtt = datetime.today()
        pll = Place()
        pll.id = "123456"
        pll.created_at = pll.updated_at = dtt
        tdict = {
            'id': '123456',
            '__class__': 'Place',
            'created_at': dtt.isoformat(),
            'updated_at': dtt.isoformat(),
        }
        self.assertDictEqual(pll.to_dict(), tdict)

    def testing_contrast_to_dict_dunder_dict(self):
        pll = Place()
        self.assertNotEqual(pll.to_dict(), pll.__dict__)

    def testing_to_dict_with_arg(self):
        pll = Place()
        with self.assertRaises(TypeError):
            pll.to_dict(None)


if __name__ == "__main__":
    unittest.main()

