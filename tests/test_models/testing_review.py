#!/usr/bin/python3
"""Defining the unittests thats for the models/review.py.

Unittest classes:
    TestReview_instantiation
    TestReview_save
    TestReview_to_dict
"""
import os

import unittest

import models

from datetime import datetime

from time import sleep

from models.review import Review


class TestReview_instantiation(unittest.TestCase):
    """Unittests thats for testing the instantiation of the
    Review class."""

    def testing_no_argss_instantiates(self):
        self.assertEqual(Review, type(Review()))

    def testing_new_instance_storedd_in_objects(self):
        self.assertIn(Review(), models.storage.all().values())

    def testing_id_is_public_str(self):
        self.assertEqual(str, type(Review().id))

    def testing_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().created_at))

    def testing_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().updated_at))

    def testing_place_id_is_public_class_attribute(self):
        rvv = Review()
        self.assertEqual(str, type(Review.placee_id))
        self.assertIn("placee_id", dir(rvv))
        self.assertNotIn("placee_id", rvv.__dict__)

    def testing_user_id_is_public_class_attribute(self):
        rvv = Review()
        self.assertEqual(str, type(Review.userr_id))
        self.assertIn("userr_id", dir(rvv))
        self.assertNotIn("userr_id", rvv.__dict__)

    def testing_text_is_public_class_attribute(self):
        rvv = Review()
        self.assertEqual(str, type(Review.textt))
        self.assertIn("textt", dir(rvv))
        self.assertNotIn("textt", rvv.__dict__)

    def testing_two_reviews_unique_ids(self):
        rv11 = Review()
        rv22 = Review()
        self.assertNotEqual(rv11.id, rv22.id)

    def testing_two_reviews_different_created_at(self):
        rv11 = Review()
        sleep(0.05)
        rv22 = Review()
        self.assertLess(rv11.created_at, rv22.created_at)

    def testing_two_reviews_different_updated_at(self):
        rv11 = Review()
        sleep(0.05)
        rv22 = Review()
        self.assertLess(rv11.updated_at, rv22.updated_at)

    def testing_str_representation(self):
        dtt = datetime.today()
        dtt_reprr = repr(dtt)
        rvv = Review()
        rvv.id = "123456"
        rvv.created_at = rvv.updated_at = dtt
        rvvstrr = rvv.__str__()
        self.assertIn("[Review] (123456)", rvvstrr)
        self.assertIn("'id': '123456'", rvvstrr)
        self.assertIn("'created_at': " + dtt_reprr, rvvstrr)
        self.assertIn("'updated_at': " + dtt_reprr, rvvstrr)

    def testing_args_unused(self):
        rvv = Review(None)
        self.assertNotIn(None, rvv.__dict__.values())

    def testing_instantiation_with_kwargs(self):
        dtt = datetime.today()
        dtt_isoo = dtt.isoformat()
        rvv = Review(id="345", created_at=dtt_isoo, updated_at=dtt_isoo)
        self.assertEqual(rvv.id, "345")
        self.assertEqual(rvv.created_at, dtt)
        self.assertEqual(rvv.updated_at, dtt)

    def testing_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)


class TestReview_save(unittest.TestCase):
    """Unittests thats for testing the save method of
    the Review class."""

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
        rvv = Review()
        sleep(0.05)
        the_first_updatedd_at = rvv.updated_at
        rvv.save()
        self.assertLess(the_first_updatedd_at, rvv.updated_at)

    def testing_two_saves(self):
        rvv = Review()
        sleep(0.05)
        the_first_updatedd_at = rvv.updated_at
        rvv.save()
        the_second_updatedd_at = rvv.updated_at
        self.assertLess(the_first_updatedd_at, the_second_updatedd_at)
        sleep(0.05)
        rvv.save()
        self.assertLess(the_second_updatedd_at, rvv.updated_at)

    def testing_save_with_arg(self):
        rvv = Review()
        with self.assertRaises(TypeError):
            rvv.save(None)

    def testing_save_updates_file(self):
        rvv = Review()
        rvv.save()
        rvid = "Review." + rvv.id
        with open("file.json", "r") as f:
            self.assertIn(rvid, f.read())


class TestReview_to_dict(unittest.TestCase):
    """Unittests thats for testing the to_dict method of
    the Review class."""

    def testing_to_dict_type(self):
        self.assertTrue(dict, type(Review().to_dict()))

    def testing_to_dict_contains_correct_keys(self):
        rvv = Review()
        self.assertIn("id", rvv.to_dict())
        self.assertIn("created_at", rvv.to_dict())
        self.assertIn("updated_at", rvv.to_dict())
        self.assertIn("__class__", rvv.to_dict())

    def testing_to_dict_contains_added_attributes(self):
        rvv = Review()
        rvv.middle_name = "Holberton"
        rvv.my_number = 98
        self.assertEqual("Holberton", rvv.middle_name)
        self.assertIn("my_number", rvv.to_dict())

    def testing_to_dict_datetime_attributes_are_strs(self):
        rvv = Review()
        rvv_dictt = rvv.to_dict()
        self.assertEqual(str, type(rvv_dictt["id"]))
        self.assertEqual(str, type(rvv_dictt["created_at"]))
        self.assertEqual(str, type(rvv_dictt["updated_at"]))

    def testing_to_dict_output(self):
        dtt = datetime.today()
        rvv = Review()
        rvv.id = "123456"
        rvv.created_at = rvv.updated_at = dtt
        ttdictt = {
            'id': '123456',
            '__class__': 'Review',
            'created_at': dtt.isoformat(),
            'updated_at': dtt.isoformat(),
        }
        self.assertDictEqual(rvv.to_dict(), ttdictt)

    def testing_contrast_to_dict_dunder_dict(self):
        rvv = Review()
        self.assertNotEqual(rvv.to_dict(), rvv.__dict__)

    def testing_to_dict_with_arg(self):
        rvv = Review()
        with self.assertRaises(TypeError):
            rvv.to_dict(None)


if __name__ == "__main__":
    unittest.main()

