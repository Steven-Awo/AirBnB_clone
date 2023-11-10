#!/usr/bin/python3
"""Defining unittests for models/user.py.

Unittest classes:
    TestUser_instantiation
    TestUser_save
    TestUser_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.user import User


class TestUser_instantiation(unittest.TestCase):
    """Unittests thats for testing the instantiation of
    the User class."""

    def testing_no_args_instantiates(self):
        self.assertEqual(User, type(User()))

    def testing_new_instance_stored_in_objects(self):
        self.assertIn(User(), models.storage.all().values())

    def testing_id_is_public_str(self):
        self.assertEqual(str, type(User().id))

    def testing_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(User().created_at))

    def testing_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(User().updated_at))

    def testing_email_is_public_str(self):
        self.assertEqual(str, type(User.email))

    def testing_password_is_public_str(self):
        self.assertEqual(str, type(User.password))

    def testing_first_name_is_public_str(self):
        self.assertEqual(str, type(User.first_name))

    def testing_last_name_is_public_str(self):
        self.assertEqual(str, type(User.last_name))

    def testing_two_users_unique_ids(self):
        us11 = User()
        us22 = User()
        self.assertNotEqual(us11.id, us22.id)

    def testing_two_users_different_created_at(self):
        us11 = User()
        sleep(0.05)
        us22 = User()
        self.assertLess(us11.created_at, us22.created_at)

    def testing_two_users_different_updated_at(self):
        us11 = User()
        sleep(0.05)
        us22 = User()
        self.assertLess(us11.updated_at, us22.updated_at)

    def testing_str_representation(self):
        dtt = datetime.today()
        dtt_reprr = repr(dtt)
        usr = User()
        usr.id = "123456"
        usr.created_at = usr.updated_at = dtt
        usrstr = usr.__str__()
        self.assertIn("[User] (123456)", usrstr)
        self.assertIn("'id': '123456'", usrstr)
        self.assertIn("'created_at': " + dtt_reprr, usrstr)
        self.assertIn("'updated_at': " + dtt_reprr, usrstr)

    def testing_args_unused(self):
        usr = User(None)
        self.assertNotIn(None, usr.__dict__.values())

    def testing_instantiation_with_kwargs(self):
        dtt = datetime.today()
        dt_iso = dtt.isoformat()
        usr = User(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(usr.id, "345")
        self.assertEqual(usr.created_at, dtt)
        self.assertEqual(usr.updated_at, dtt)

    def testing_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)


class TestUser_save(unittest.TestCase):
    """Unittests thats for testing the save method of
    the class."""

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
        usr = User()
        sleep(0.05)
        the_first_updatedd_at = usr.updated_at
        usr.save()
        self.assertLess(the_first_updatedd_at, usr.updated_at)

    def testing_two_saves(self):
        usr = User()
        sleep(0.05)
        the_first_updatedd_at = usr.updated_at
        usr.save()
        the_second_updated_at = usr.updated_at
        self.assertLess(the_first_updatedd_at, the_second_updated_at)
        sleep(0.05)
        usr.save()
        self.assertLess(the_second_updated_at, usr.updated_at)

    def testing_save_with_arg(self):
        usr = User()
        with self.assertRaises(TypeError):
            usr.save(None)

    def testing_save_updates_file(self):
        usr = User()
        usr.save()
        usid = "User." + usr.id
        with open("file.json", "r") as f:
            self.assertIn(usid, f.read())


class TestUser_to_dict(unittest.TestCase):
    """Unittests thats for testing the to_dict method of
    the User class."""

    def testing_to_dict_type(self):
        self.assertTrue(dict, type(User().to_dict()))

    def testing_to_dict_contains_correct_keys(self):
        usr = User()
        self.assertIn("id", usr.to_dict())
        self.assertIn("created_at", usr.to_dict())
        self.assertIn("updated_at", usr.to_dict())
        self.assertIn("__class__", usr.to_dict())

    def testing_to_dict_contains_added_attributes(self):
        usr = User()
        usr.middle_name = "Holberton"
        usr.my_number = 98
        self.assertEqual("Holberton", usr.middle_name)
        self.assertIn("my_number", usr.to_dict())

    def testing_to_dict_datetime_attributes_are_strs(self):
        usr = User()
        us_dict = usr.to_dict()
        self.assertEqual(str, type(us_dict["id"]))
        self.assertEqual(str, type(us_dict["created_at"]))
        self.assertEqual(str, type(us_dict["updated_at"]))

    def testing_to_dict_output(self):
        dtt = datetime.today()
        usr = User()
        usr.id = "123456"
        usr.created_at = usr.updated_at = dtt
        tdict = {
            'id': '123456',
            '__class__': 'User',
            'created_at': dtt.isoformat(),
            'updated_at': dtt.isoformat(),
        }
        self.assertDictEqual(usr.to_dict(), tdict)

    def testing_contrast_to_dict_dunder_dict(self):
        usr = User()
        self.assertNotEqual(usr.to_dict(), usr.__dict__)

    def testing_to_dict_with_arg(self):
        usr = User()
        with self.assertRaises(TypeError):
            usr.to_dict(None)


if __name__ == "__main__":
    unittest.main()

