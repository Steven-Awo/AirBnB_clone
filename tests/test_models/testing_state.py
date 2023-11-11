#!/usr/bin/python3
"""Defining the unittests thats for the models/state.py.

Unittest classes:
    TestingState_instantiation
    TestingState_save
    TestingState_to_dict
"""
import os

import unittest

import models

from datetime import datetime

from time import sleep

from models.state import State


class TestState_instantiation(unittest.TestCase):
    """Unittests thats for testing the instantiation of
    the State class."""

    def testing_no_argss_instantiates(self):
        self.assertEqual(State, type(State()))

    def testing_new_instance_storedd_in_objects(self):
        self.assertIn(State(), models.storage.all().values())

    def testing_id_iss_public_str(self):
        self.assertEqual(str, type(State().id))

    def testing_created_at_iss_public_datetime(self):
        self.assertEqual(datetime, type(State().created_at))

    def testing_updated_at_iss_public_datetime(self):
        self.assertEqual(datetime, type(State().updated_at))

    def testing_name_is_public_class_attribute(self):
        stte = State()
        self.assertEqual(str, type(State.namme))
        self.assertIn("namme", dir(stte))
        self.assertNotIn("namme", stte.__dict__)

    def testing_two_states_unique_ids(self):
        st11 = State()
        st22 = State()
        self.assertNotEqual(st11.id, st22.id)

    def testing_two_states_different_created_at(self):
        st11 = State()
        sleep(0.05)
        st22 = State()
        self.assertLess(st11.created_at, st22.created_at)

    def testing_two_states_different_updated_at(self):
        st11 = State()
        sleep(0.05)
        st22 = State()
        self.assertLess(st11.updated_at, st22.updated_at)

    def testing_str_representation(self):
        dtt = datetime.today()
        dtt_reprr = repr(dtt)
        stte = State()
        stte.id = "123456"
        stte.created_at = stte.updated_at = dtt
        ststr = stte.__str__()
        self.assertIn("[State] (123456)", ststr)
        self.assertIn("'id': '123456'", ststr)
        self.assertIn("'created_at': " + dtt_reprr, ststr)
        self.assertIn("'updated_at': " + dtt_reprr, ststr)

    def testing_args_unused(self):
        stte = State(None)
        self.assertNotIn(None, stte.__dict__.values())

    def testing_instantiation_with_kwargs(self):
        dtt = datetime.today()
        dtt_isoo = dtt.isoformat()
        stte = State(id="345", created_at=dtt_isoo, updated_at=dtt_isoo)
        self.assertEqual(stte.id, "345")
        self.assertEqual(stte.created_at, dtt)
        self.assertEqual(stte.updated_at, dtt)

    def testing_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            State(id=None, created_at=None, updated_at=None)


class TestState_save(unittest.TestCase):
    """Unittests thats for testing the save method of
    the State class."""

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
        stte = State()
        sleep(0.05)
        the_first_updatedd_at = stte.updated_at
        stte.save()
        self.assertLess(the_first_updatedd_at, stte.updated_at)

    def testing_two_saves(self):
        stte = State()
        sleep(0.05)
        the_first_updatedd_at = stte.updated_at
        stte.save()
        the_second_updatedd_at = stte.updated_at
        self.assertLess(the_first_updatedd_at, the_second_updatedd_at)
        sleep(0.05)
        stte.save()
        self.assertLess(the_second_updatedd_at, stte.updated_at)

    def testing_save_with_arg(self):
        stte = State()
        with self.assertRaises(TypeError):
            stte.save(None)

    def testing_save_updates_file(self):
        stte = State()
        stte.save()
        stid = "State." + stte.id
        with open("file.json", "r") as f:
            self.assertIn(stid, f.read())


class TestState_to_dict(unittest.TestCase):
    """Unittests thats for testing the to_dict method of
    the State class."""

    def testing_to_dict_type(self):
        self.assertTrue(dict, type(State().to_dict()))

    def testing_to_dict_contains_correct_keys(self):
        stte = State()
        self.assertIn("id", stte.to_dict())
        self.assertIn("created_at", stte.to_dict())
        self.assertIn("updated_at", stte.to_dict())
        self.assertIn("__class__", stte.to_dict())

    def testing_to_dict_contains_added_attributes(self):
        stte = State()
        stte.middle_name = "Holberton"
        stte.my_number = 98
        self.assertEqual("Holberton", stte.middle_name)
        self.assertIn("my_number", stte.to_dict())

    def testing_to_dict_datetime_attributes_are_strs(self):
        stte = State()
        stt_dictt = stte.to_dict()
        self.assertEqual(str, type(stt_dictt["id"]))
        self.assertEqual(str, type(stt_dictt["created_at"]))
        self.assertEqual(str, type(stt_dictt["updated_at"]))

    def testing_to_dict_output(self):
        dtt = datetime.today()
        stte = State()
        stte.id = "123456"
        stte.created_at = stte.updated_at = dtt
        tdict = {
            'id': '123456',
            '__class__': 'State',
            'created_at': dtt.isoformat(),
            'updated_at': dtt.isoformat(),
        }
        self.assertDictEqual(stte.to_dict(), tdict)

    def testing_contrast_to_dict_dunder_dict(self):
        stte = State()
        self.assertNotEqual(stte.to_dict(), stte.__dict__)

    def testing_to_dict_with_arg(self):
        stte = State()
        with self.assertRaises(TypeError):
            stte.to_dict(None)


if __name__ == "__main__":
    unittest.main()

