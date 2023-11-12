#!/usr/bin/python3
"""Defining the unittests for the console.py file.

Unittest classes:
    Testing_HBNB_Command_prompting
    Testing_HBNB_Command_help
    Testing_HBNB_Command_exit
    Testing_HBNB_Command_create
    Testing_HBNB_Command_show
    Testing_HBNB_Command_all
    Testing_HBNB_Command_destroy
    Testing_HBNB_Command_update
"""
import os

import sys

import unittest

from console import HBNBCommand

from models import storage

from models.engine.file_storage import FileStorage

from io import StringIO

from unittest.mock import patch


class Testing_HBNB_Command_prompting(unittest.TestCase):
    """Unittests thats for testing the prompting of the HBNB's
    command interpreter."""

    def testing_prompt_string(self):
        self.assertEqual("(hbnb) ", HBNBCommand.promptt)

    def testing_empty_line(self):
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", out_put.getvalue().strip())


class Testing_HBNB_Command_help(unittest.TestCase):
    """Unittests used for testing the help messages of the
    HBNB command interpreter."""

    def testing_help_quit(self):
        hh = "The quit commandd for exiting the program."
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(hh, out_put.getvalue().strip())

    def testing_help_create(self):
        hh = ("Usage: create <class>\n        "
        "Creating a new class's instance and to print out its id.")
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("help create"))
            self.assertEqual(hh, out_put.getvalue().strip())

    def testing_help_EOF(self):
        hh = "EOF signal for the exit the program."
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(hh, out_put.getvalue().strip())

    def testing_help_show(self):
        hh = ("Usage: show <class> <id> or <class>.show(<id>)\n        "
             "Displays the string's representation of a class's instance of"
             " a given id.")
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("help show"))
            self.assertEqual(hh, out_put.getvalue().strip())

    def testing_help_destroy(self):
        hh = ("Usage: destroy <class> <id> or <class>.destroy(<id>)\n        "
             "Deletes a class's instance of the given id.")
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("help destroys"))
            self.assertEqual(hh, out_put.getvalue().strip())

    def testing_help_all(self):
        hh = ("Usage: all or all <class> or <class>.all()\n        "
             "Displays the string's representations of all the instances of the class given"
             ".\n        If there is no class specified, displays all the instantiated "
             "objects.")
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("help all"))
            self.assertEqual(hh, out_put.getvalue().strip())

    def testing_help_count(self):
        hh = ("Usage: count <class> or <class>.count()\n        "
             "Retrieves all the number of the instances of the class given.")
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("help count"))
            self.assertEqual(hh, out_put.getvalue().strip())

    def testing_help_update(self):
        hh = ("Usage: update <class> <id> <attribute_name> <attribute_value> or"
             "\n       <class>.update(<id>, <attribute_name>, <attribute_value"
             ">) or\n       <class>.update(<id>, <dictionary>)\n        "
             "Updates a class's instance of the given id by adding or by updating\n   "
             "     a given attribute's key/value pair or dictionary.")
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("help update"))
            self.assertEqual(hh, out_put.getvalue().strip())

    def testing_help(self):
        hh = ("Documented commands (type help <topic>):\n"
             "========================================\n"
             "EOF  all  count  create  destroy  help  quit  show  update")
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("help"))
            self.assertEqual(hh, out_put.getvalue().strip())


class Testing_HBNB_Command_exit(unittest.TestCase):
    """Unittests used for testing to exiting from the HBNB
    command interpreter."""

    def testing_quit_exits(self):
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def testing_EOF_exits(self):
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertTrue(HBNBCommand().onecmd("EOF"))


class Testing_HBNB_Command_create(unittest.TestCase):
    """Unittests used for testing to create from the HBNB
    command interpreter."""

    @classmethod
    def setsUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

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

    def testing_create_missing_class(self):
        correctts = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual(correctts, out_put.getvalue().strip())

    def testing_create_invalid_class(self):
        correctts = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("create MyModel"))
            self.assertEqual(correctts, out_put.getvalue().strip())

    def testing_create_invalid_syntax(self):
        correctts = "*** Unknown syntax: MyModel.create()"
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("MyModel.create()"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        correctts = "*** Unknown syntax: BaseModel.create()"
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.create()"))
            self.assertEqual(correctts, out_put.getvalue().strip())

    def testing_create_object(self):
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertLess(0, len(out_put.getvalue().strip()))
            testing_Key = "BaseModel.{}".format(out_put.getvalue().strip())
            self.assertIn(testing_Key, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertLess(0, len(out_put.getvalue().strip()))
            testing_Key = "User.{}".format(out_put.getvalue().strip())
            self.assertIn(testing_Key, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertLess(0, len(out_put.getvalue().strip()))
            testing_Key = "State.{}".format(out_put.getvalue().strip())
            self.assertIn(testing_Key, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertLess(0, len(out_put.getvalue().strip()))
            testing_Key = "City.{}".format(out_put.getvalue().strip())
            self.assertIn(testing_Key, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertLess(0, len(out_put.getvalue().strip()))
            testing_Key = "Amenity.{}".format(out_put.getvalue().strip())
            self.assertIn(testing_Key, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertLess(0, len(out_put.getvalue().strip()))
            testing_Key = "Place.{}".format(out_put.getvalue().strip())
            self.assertIn(testing_Key, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            self.assertLess(0, len(out_put.getvalue().strip()))
            testing_Key = "Review.{}".format(out_put.getvalue().strip())
            self.assertIn(testing_Key, storage.all().keys())


class Testing_HBNB_Command_show(unittest.TestCase):
    """Unittests that's for testing the shows from the HBNB's
    command interpreter"""

    @classmethod
    def setsUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

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

    def testing_show_missing_class(self):
        correctts = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("show"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd(".show()"))
            self.assertEqual(correctts, out_put.getvalue().strip())

    def testing_show_invalid_class(self):
        correctts = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("shows MyModel"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("MyModel.show()"))
            self.assertEqual(correctts, out_put.getvalue().strip())

    def testing_show_missing_id_space_notation(self):
        correctts = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("shows BaseModel"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("shows User"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("shows State"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("shows City"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("shows Amenity"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("shows Place"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("shows Review"))
            self.assertEqual(correctts, out_put.getvalue().strip())

    def testing_show_missing_id_dot_notation(self):
        correctts = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.show()"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("User.show()"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("State.show()"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("City.show()"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("Amenity.show()"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("Place.show()"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("Review.show()"))
            self.assertEqual(correctts, out_put.getvalue().strip())

    def testing_show_no_instance_found_space_notation(self):
        correctts = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("shows BaseModel 1"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("shows User 1"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("shows State 1"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("shows City 1"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("shows Amenity 1"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("shows Place 1"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("shows Review 1"))
            self.assertEqual(correctts, out_put.getvalue().strip())

    def testing_show_no_instance_found_dot_notation(self):
        correctts = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.show(1)"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("User.show(1)"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("State.show(1)"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("City.show(1)"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("Amenity.show(1)"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("Place.show(1)"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("Review.show(1)"))
            self.assertEqual(correctts, out_put.getvalue().strip())

    def testing_show_objects_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            testing_ID = out_put.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as out_put:
            obj = storage.all()["BaseModel.{}".format(testing_ID)]
            command = "shows BaseModel {}".format(testing_ID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            testing_ID = out_put.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as out_put:
            obj = storage.all()["User.{}".format(testing_ID)]
            command = "shows User {}".format(testing_ID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            testing_ID = out_put.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as out_put:
            obj = storage.all()["State.{}".format(testing_ID)]
            command = "shows State {}".format(testing_ID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            testing_ID = out_put.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as out_put:
            obj = storage.all()["Place.{}".format(testing_ID)]
            command = "shows Place {}".format(testing_ID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            testing_ID = out_put.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as out_put:
            obj = storage.all()["City.{}".format(testing_ID)]
            command = "shows City {}".format(testing_ID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            testing_ID = out_put.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as out_put:
            obj = storage.all()["Amenity.{}".format(testing_ID)]
            command = "shows Amenity {}".format(testing_ID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            testing_ID = out_put.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as out_put:
            obj = storage.all()["Review.{}".format(testing_ID)]
            command = "shows Review {}".format(testing_ID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), out_put.getvalue().strip())

    def testing_show_objects_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            testing_ID = out_put.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as out_put:
            obj = storage.all()["BaseModel.{}".format(testing_ID)]
            command = "BaseModel.show({})".format(testing_ID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            testing_ID = out_put.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as out_put:
            obj = storage.all()["User.{}".format(testing_ID)]
            command = "User.show({})".format(testing_ID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            testing_ID = out_put.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as out_put:
            obj = storage.all()["State.{}".format(testing_ID)]
            command = "State.show({})".format(testing_ID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            testing_ID = out_put.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as out_put:
            obj = storage.all()["Place.{}".format(testing_ID)]
            command = "Place.show({})".format(testing_ID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            testing_ID = out_put.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as out_put:
            obj = storage.all()["City.{}".format(testing_ID)]
            command = "City.show({})".format(testing_ID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            testing_ID = out_put.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as out_put:
            obj = storage.all()["Amenity.{}".format(testing_ID)]
            command = "Amenity.show({})".format(testing_ID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            testing_ID = out_put.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as out_put:
            obj = storage.all()["Review.{}".format(testing_ID)]
            command = "Review.show({})".format(testing_ID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), out_put.getvalue().strip())


class Testing_HBNB_Command_destroy(unittest.TestCase):
    """Unittests thats for testing the destroy from the HBNB's
    command interpreter."""

    @classmethod
    def setsUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

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
        storage.reload()

    def testing_destroy_missing_class(self):
        correctts = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("destroy"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd(".destroy()"))
            self.assertEqual(correctts, out_put.getvalue().strip())

    def testing_destroy_invalid_class(self):
        correctts = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("destroy MyModel"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("MyModel.destroy()"))
            self.assertEqual(correctts, out_put.getvalue().strip())

    def testing_destroy_id_missing_space_notation(self):
        correctts = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("destroy User"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("destroy State"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("destroy City"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("destroy Amenity"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("destroy Place"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("destroy Review"))
            self.assertEqual(correctts, out_put.getvalue().strip())

    def testing_destroy_id_missing_dot_notation(self):
        correctts = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.destroy()"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("User.destroy()"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("State.destroy()"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("City.destroy()"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("Amenity.destroy()"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("Place.destroy()"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("Review.destroy()"))
            self.assertEqual(correctts, out_put.getvalue().strip())

    def testing_destroy_invalid_id_space_notation(self):
        correctts = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel 1"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("destroy User 1"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("destroy State 1"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("destroy City 1"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("destroy Amenity 1"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("destroy Place 1"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("destroy Review 1"))
            self.assertEqual(correctts, out_put.getvalue().strip())

    def testing_destroy_invalid_id_dot_notation(self):
        correctts = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.destroy(1)"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("User.destroy(1)"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("State.destroy(1)"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("City.destroy(1)"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("Amenity.destroy(1)"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("Place.destroy(1)"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("Review.destroy(1)"))
            self.assertEqual(correctts, out_put.getvalue().strip())

    def testing_destroy_objects_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            testing_ID = out_put.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as out_put:
            obj = storage.all()["BaseModel.{}".format(testing_ID)]
            command = "destroy BaseModel {}".format(testing_ID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            testing_ID = out_put.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as out_put:
            obj = storage.all()["User.{}".format(testing_ID)]
            command = "shows User {}".format(testing_ID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            testing_ID = out_put.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as out_put:
            obj = storage.all()["State.{}".format(testing_ID)]
            command = "shows State {}".format(testing_ID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            testing_ID = out_put.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as out_put:
            obj = storage.all()["Place.{}".format(testing_ID)]
            command = "shows Place {}".format(testing_ID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            testing_ID = out_put.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as out_put:
            obj = storage.all()["City.{}".format(testing_ID)]
            command = "shows City {}".format(testing_ID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            testing_ID = out_put.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as out_put:
            obj = storage.all()["Amenity.{}".format(testing_ID)]
            command = "shows Amenity {}".format(testing_ID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            testing_ID = out_put.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as out_put:
            obj = storage.all()["Review.{}".format(testing_ID)]
            command = "shows Review {}".format(testing_ID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())

    def testing_destroy_objects_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            testing_ID = out_put.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as out_put:
            obj = storage.all()["BaseModel.{}".format(testing_ID)]
            command = "BaseModel.destroy({})".format(testing_ID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            testing_ID = out_put.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as out_put:
            obj = storage.all()["User.{}".format(testing_ID)]
            command = "User.destroy({})".format(testing_ID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            testing_ID = out_put.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as out_put:
            obj = storage.all()["State.{}".format(testing_ID)]
            command = "State.destroy({})".format(testing_ID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            testing_ID = out_put.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as out_put:
            obj = storage.all()["Place.{}".format(testing_ID)]
            command = "Place.destroy({})".format(testing_ID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            testing_ID = out_put.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as out_put:
            obj = storage.all()["City.{}".format(testing_ID)]
            command = "City.destroy({})".format(testing_ID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            testing_ID = out_put.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as out_put:
            obj = storage.all()["Amenity.{}".format(testing_ID)]
            command = "Amenity.destroy({})".format(testing_ID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            testing_ID = out_put.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as out_put:
            obj = storage.all()["Review.{}".format(testing_ID)]
            command = "Review.destory({})".format(testing_ID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())


class Testing_HBNB_Command_all(unittest.TestCase):
    """Unittests thats for testing the all of the HBNB's
    command interpreter."""

    @classmethod
    def setsUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

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

    def testing_all_invalid_class(self):
        correctts = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("all MyModel"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("MyModel.all()"))
            self.assertEqual(correctts, out_put.getvalue().strip())

    def testing_all_objects_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("all"))
            self.assertIn("BaseModel", out_put.getvalue().strip())
            self.assertIn("User", out_put.getvalue().strip())
            self.assertIn("State", out_put.getvalue().strip())
            self.assertIn("Place", out_put.getvalue().strip())
            self.assertIn("City", out_put.getvalue().strip())
            self.assertIn("Amenity", out_put.getvalue().strip())
            self.assertIn("Review", out_put.getvalue().strip())

    def testing_all_objects_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd(".all()"))
            self.assertIn("BaseModel", out_put.getvalue().strip())
            self.assertIn("User", out_put.getvalue().strip())
            self.assertIn("State", out_put.getvalue().strip())
            self.assertIn("Place", out_put.getvalue().strip())
            self.assertIn("City", out_put.getvalue().strip())
            self.assertIn("Amenity", out_put.getvalue().strip())
            self.assertIn("Review", out_put.getvalue().strip())

    def testing_all_single_object_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("all BaseModel"))
            self.assertIn("BaseModel", out_put.getvalue().strip())
            self.assertNotIn("User", out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("all User"))
            self.assertIn("User", out_put.getvalue().strip())
            self.assertNotIn("BaseModel", out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("all State"))
            self.assertIn("State", out_put.getvalue().strip())
            self.assertNotIn("BaseModel", out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("all City"))
            self.assertIn("City", out_put.getvalue().strip())
            self.assertNotIn("BaseModel", out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("all Amenity"))
            self.assertIn("Amenity", out_put.getvalue().strip())
            self.assertNotIn("BaseModel", out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("all Place"))
            self.assertIn("Place", out_put.getvalue().strip())
            self.assertNotIn("BaseModel", out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("all Review"))
            self.assertIn("Review", out_put.getvalue().strip())
            self.assertNotIn("BaseModel", out_put.getvalue().strip())

    def testing_all_single_object_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.all()"))
            self.assertIn("BaseModel", out_put.getvalue().strip())
            self.assertNotIn("User", out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("User.all()"))
            self.assertIn("User", out_put.getvalue().strip())
            self.assertNotIn("BaseModel", out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("State.all()"))
            self.assertIn("State", out_put.getvalue().strip())
            self.assertNotIn("BaseModel", out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("City.all()"))
            self.assertIn("City", out_put.getvalue().strip())
            self.assertNotIn("BaseModel", out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("Amenity.all()"))
            self.assertIn("Amenity", out_put.getvalue().strip())
            self.assertNotIn("BaseModel", out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("Place.all()"))
            self.assertIn("Place", out_put.getvalue().strip())
            self.assertNotIn("BaseModel", out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("Review.all()"))
            self.assertIn("Review", out_put.getvalue().strip())
            self.assertNotIn("BaseModel", out_put.getvalue().strip())


class Testing_HBNB_Command_update(unittest.TestCase):
    """Unittests thats for testing the update from the HBNB
    command interpreter."""

    @classmethod
    def setsUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

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

    def testing_update_missing_class(self):
        correctts = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("update"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd(".update()"))
            self.assertEqual(correctts, out_put.getvalue().strip())

    def testing_update_invalid_class(self):
        correctts = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("update MyModel"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("MyModel.update()"))
            self.assertEqual(correctts, out_put.getvalue().strip())

    def testing_update_missing_id_space_notation(self):
        correctts = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("update BaseModel"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("update User"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("update State"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("update City"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("update Amenity"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("update Place"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("update Review"))
            self.assertEqual(correctts, out_put.getvalue().strip())

    def testing_update_missing_id_dot_notation(self):
        correctts = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.update()"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("User.update()"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("State.update()"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("City.update()"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("Amenity.update()"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("Place.update()"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("Review.update()"))
            self.assertEqual(correctts, out_put.getvalue().strip())

    def testing_update_invalid_id_space_notation(self):
        correctts = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("update BaseModel 1"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("update User 1"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("update State 1"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("update City 1"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("update Amenity 1"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("update Place 1"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("update Review 1"))
            self.assertEqual(correctts, out_put.getvalue().strip())

    def testing_update_invalid_id_dot_notation(self):
        correctts = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.update(1)"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("User.update(1)"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("State.update(1)"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("City.update(1)"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("Amenity.update(1)"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("Place.update(1)"))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("Review.update(1)"))
            self.assertEqual(correctts, out_put.getvalue().strip())

    def testing_update_missing_attr_name_space_notation(self):
        correctts = "** attribute name missing **"
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            testing_Id = out_put.getvalue().strip()
            testing_Cmd = "update BaseModel {}".format(testing_Id)
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd(testing_Cmd))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            testing_Id = out_put.getvalue().strip()
            testing_Cmd = "update User {}".format(testing_Id)
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd(testing_Cmd))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            testing_Id = out_put.getvalue().strip()
            testing_Cmd = "update State {}".format(testing_Id)
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd(testing_Cmd))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            testing_Id = out_put.getvalue().strip()
            testing_Cmd = "update City {}".format(testing_Id)
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd(testing_Cmd))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            testing_Id = out_put.getvalue().strip()
            testing_Cmd = "update Amenity {}".format(testing_Id)
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd(testing_Cmd))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            testing_Id = out_put.getvalue().strip()
            testing_Cmd = "update Place {}".format(testing_Id)
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd(testing_Cmd))
            self.assertEqual(correctts, out_put.getvalue().strip())

    def testing_update_missing_attr_name_dot_notation(self):
        correctts = "** attribute name missing **"
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            testing_Id = out_put.getvalue().strip()
            testing_Cmd = "BaseModel.update({})".format(testing_Id)
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd(testing_Cmd))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            testing_Id = out_put.getvalue().strip()
            testing_Cmd = "User.update({})".format(testing_Id)
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd(testing_Cmd))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            testing_Id = out_put.getvalue().strip()
            testing_Cmd = "State.update({})".format(testing_Id)
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd(testing_Cmd))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            testing_Id = out_put.getvalue().strip()
            testing_Cmd = "City.update({})".format(testing_Id)
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd(testing_Cmd))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            testing_Id = out_put.getvalue().strip()
            testing_Cmd = "Amenity.update({})".format(testing_Id)
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd(testing_Cmd))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            testing_Id = out_put.getvalue().strip()
            testing_Cmd = "Place.update({})".format(testing_Id)
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd(testing_Cmd))
            self.assertEqual(correctts, out_put.getvalue().strip())

    def testing_update_missing_attr_value_space_notation(self):
        correctts = "** value missing **"
        with patch("sys.stdout", new=StringIO()) as out_put:
            HBNBCommand().onecmd("create BaseModel")
            testing_Id = out_put.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as out_put:
            testing_Cmd = "update BaseModel {} attr_name".format(testing_Id)
            self.assertFalse(HBNBCommand().onecmd(testing_Cmd))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            HBNBCommand().onecmd("create User")
            testing_Id = out_put.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as out_put:
            testing_Cmd = "update User {} attr_name".format(testing_Id)
            self.assertFalse(HBNBCommand().onecmd(testing_Cmd))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            HBNBCommand().onecmd("create State")
            testing_Id = out_put.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as out_put:
            testing_Cmd = "update State {} attr_name".format(testing_Id)
            self.assertFalse(HBNBCommand().onecmd(testing_Cmd))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            HBNBCommand().onecmd("create City")
            testing_Id = out_put.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as out_put:
            testing_Cmd = "update City {} attr_name".format(testing_Id)
            self.assertFalse(HBNBCommand().onecmd(testing_Cmd))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            HBNBCommand().onecmd("create Amenity")
            testing_Id = out_put.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as out_put:
            testing_Cmd = "update Amenity {} attr_name".format(testing_Id)
            self.assertFalse(HBNBCommand().onecmd(testing_Cmd))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            HBNBCommand().onecmd("create Place")
            testing_Id = out_put.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as out_put:
            testing_Cmd = "update Place {} attr_name".format(testing_Id)
            self.assertFalse(HBNBCommand().onecmd(testing_Cmd))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            HBNBCommand().onecmd("create Review")
            testing_Id = out_put.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as out_put:
            testing_Cmd = "update Review {} attr_name".format(testing_Id)
            self.assertFalse(HBNBCommand().onecmd(testing_Cmd))
            self.assertEqual(correctts, out_put.getvalue().strip())

    def testing_update_missing_attr_value_dot_notation(self):
        correctts = "** value missing **"
        with patch("sys.stdout", new=StringIO()) as out_put:
            HBNBCommand().onecmd("create BaseModel")
            testing_Id = out_put.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as out_put:
            testing_Cmd = "BaseModel.update({}, attr_name)".format(testing_Id)
            self.assertFalse(HBNBCommand().onecmd(testing_Cmd))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            HBNBCommand().onecmd("create User")
            testing_Id = out_put.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as out_put:
            testing_Cmd = "User.update({}, attr_name)".format(testing_Id)
            self.assertFalse(HBNBCommand().onecmd(testing_Cmd))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            HBNBCommand().onecmd("create State")
            testing_Id = out_put.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as out_put:
            testing_Cmd = "State.update({}, attr_name)".format(testing_Id)
            self.assertFalse(HBNBCommand().onecmd(testing_Cmd))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            HBNBCommand().onecmd("create City")
            testing_Id = out_put.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as out_put:
            testing_Cmd = "City.update({}, attr_name)".format(testing_Id)
            self.assertFalse(HBNBCommand().onecmd(testing_Cmd))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            HBNBCommand().onecmd("create Amenity")
            testing_Id = out_put.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as out_put:
            testing_Cmd = "Amenity.update({}, attr_name)".format(testing_Id)
            self.assertFalse(HBNBCommand().onecmd(testing_Cmd))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            HBNBCommand().onecmd("create Place")
            testing_Id = out_put.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as out_put:
            testing_Cmd = "Place.update({}, attr_name)".format(testing_Id)
            self.assertFalse(HBNBCommand().onecmd(testing_Cmd))
            self.assertEqual(correctts, out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            HBNBCommand().onecmd("create Review")
            testing_Id = out_put.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as out_put:
            testing_Cmd = "Review.update({}, attr_name)".format(testing_Id)
            self.assertFalse(HBNBCommand().onecmd(testing_Cmd))
            self.assertEqual(correctts, out_put.getvalue().strip())

    def testing_update_valid_string_attr_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as out_put:
            HBNBCommand().onecmd("create BaseModel")
            testing_Id = out_put.getvalue().strip()
        testing_Cmd = "update BaseModel {} attr_name 'attr_value'".format(testing_Id)
        self.assertFalse(HBNBCommand().onecmd(testing_Cmd))
        testing_dict = storage.all()["BaseModel.{}".format(testing_Id)].__dict__
        self.assertEqual("attr_value", testing_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as out_put:
            HBNBCommand().onecmd("create User")
            testing_Id = out_put.getvalue().strip()
        testing_Cmd = "update User {} attr_name 'attr_value'".format(testing_Id)
        self.assertFalse(HBNBCommand().onecmd(testing_Cmd))
        testing_dict = storage.all()["User.{}".format(testing_Id)].__dict__
        self.assertEqual("attr_value", testing_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as out_put:
            HBNBCommand().onecmd("create State")
            testing_Id = out_put.getvalue().strip()
        testing_Cmd = "update State {} attr_name 'attr_value'".format(testing_Id)
        self.assertFalse(HBNBCommand().onecmd(testing_Cmd))
        testing_dict = storage.all()["State.{}".format(testing_Id)].__dict__
        self.assertEqual("attr_value", testing_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as out_put:
            HBNBCommand().onecmd("create City")
            testing_Id = out_put.getvalue().strip()
        testing_Cmd = "update City {} attr_name 'attr_value'".format(testing_Id)
        self.assertFalse(HBNBCommand().onecmd(testing_Cmd))
        testing_dict = storage.all()["City.{}".format(testing_Id)].__dict__
        self.assertEqual("attr_value", testing_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as out_put:
            HBNBCommand().onecmd("create Place")
            testing_Id = out_put.getvalue().strip()
        testing_Cmd = "update Place {} attr_name 'attr_value'".format(testing_Id)
        self.assertFalse(HBNBCommand().onecmd(testing_Cmd))
        testing_dict = storage.all()["Place.{}".format(testing_Id)].__dict__
        self.assertEqual("attr_value", testing_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as out_put:
            HBNBCommand().onecmd("create Amenity")
            testing_Id = out_put.getvalue().strip()
        testing_Cmd = "update Amenity {} attr_name 'attr_value'".format(testing_Id)
        self.assertFalse(HBNBCommand().onecmd(testing_Cmd))
        testing_dict = storage.all()["Amenity.{}".format(testing_Id)].__dict__
        self.assertEqual("attr_value", testing_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as out_put:
            HBNBCommand().onecmd("create Review")
            testing_Id = out_put.getvalue().strip()
        testing_Cmd = "update Review {} attr_name 'attr_value'".format(testing_Id)
        self.assertFalse(HBNBCommand().onecmd(testing_Cmd))
        testing_dict = storage.all()["Review.{}".format(testing_Id)].__dict__
        self.assertTrue("attr_value", testing_dict["attr_name"])

    def testing_update_valid_string_attr_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as out_put:
            HBNBCommand().onecmd("create BaseModel")
            tIdd = out_put.getvalue().strip()
        testing_Cmd = "BaseModel.update({}, attr_name, 'attr_value')".format(tIdd)
        self.assertFalse(HBNBCommand().onecmd(testing_Cmd))
        testing_dict = storage.all()["BaseModel.{}".format(tIdd)].__dict__
        self.assertEqual("attr_value", testing_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as out_put:
            HBNBCommand().onecmd("create User")
            tIdd = out_put.getvalue().strip()
        testing_Cmd = "User.update({}, attr_name, 'attr_value')".format(tIdd)
        self.assertFalse(HBNBCommand().onecmd(testing_Cmd))
        testing_dict = storage.all()["User.{}".format(tIdd)].__dict__
        self.assertEqual("attr_value", testing_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as out_put:
            HBNBCommand().onecmd("create State")
            tIdd = out_put.getvalue().strip()
        testing_Cmd = "State.update({}, attr_name, 'attr_value')".format(tIdd)
        self.assertFalse(HBNBCommand().onecmd(testing_Cmd))
        testing_dict = storage.all()["State.{}".format(tIdd)].__dict__
        self.assertEqual("attr_value", testing_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as out_put:
            HBNBCommand().onecmd("create City")
            tIdd = out_put.getvalue().strip()
        testing_Cmd = "City.update({}, attr_name, 'attr_value')".format(tIdd)
        self.assertFalse(HBNBCommand().onecmd(testing_Cmd))
        testing_dict = storage.all()["City.{}".format(tIdd)].__dict__
        self.assertEqual("attr_value", testing_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as out_put:
            HBNBCommand().onecmd("create Place")
            tIdd = out_put.getvalue().strip()
        testing_Cmd = "Place.update({}, attr_name, 'attr_value')".format(tIdd)
        self.assertFalse(HBNBCommand().onecmd(testing_Cmd))
        testing_dict = storage.all()["Place.{}".format(tIdd)].__dict__
        self.assertEqual("attr_value", testing_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as out_put:
            HBNBCommand().onecmd("create Amenity")
            tIdd = out_put.getvalue().strip()
        testing_Cmd = "Amenity.update({}, attr_name, 'attr_value')".format(tIdd)
        self.assertFalse(HBNBCommand().onecmd(testing_Cmd))
        testing_dict = storage.all()["Amenity.{}".format(tIdd)].__dict__
        self.assertEqual("attr_value", testing_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as out_put:
            HBNBCommand().onecmd("create Review")
            tIdd = out_put.getvalue().strip()
        testing_Cmd = "Review.update({}, attr_name, 'attr_value')".format(tIdd)
        self.assertFalse(HBNBCommand().onecmd(testing_Cmd))
        testing_dict = storage.all()["Review.{}".format(tIdd)].__dict__
        self.assertEqual("attr_value", testing_dict["attr_name"])

    def testing_update_valid_int_attr_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as out_put:
            HBNBCommand().onecmd("create Place")
            testing_Id = out_put.getvalue().strip()
        testing_Cmd = "update Place {} max_of_guest 98".format(testing_Id)
        self.assertFalse(HBNBCommand().onecmd(testing_Cmd))
        testing_dict = storage.all()["Place.{}".format(testing_Id)].__dict__
        self.assertEqual(98, testing_dict["max_of_guest"])

    def testing_update_valid_int_attr_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as out_put:
            HBNBCommand().onecmd("create Place")
            tIdd = out_put.getvalue().strip()
        testing_Cmd = "Place.update({}, max_of_guest, 98)".format(tIdd)
        self.assertFalse(HBNBCommand().onecmd(testing_Cmd))
        testing_dict = storage.all()["Place.{}".format(tIdd)].__dict__
        self.assertEqual(98, testing_dict["max_of_guest"])

    def testing_update_valid_float_attr_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as out_put:
            HBNBCommand().onecmd("create Place")
            testing_Id = out_put.getvalue().strip()
        testing_Cmd = "update Place {} latitudee 7.2".format(testing_Id)
        self.assertFalse(HBNBCommand().onecmd(testing_Cmd))
        testing_dict = storage.all()["Place.{}".format(testing_Id)].__dict__
        self.assertEqual(7.2, testing_dict["latitudee"])

    def testing_update_valid_float_attr_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as out_put:
            HBNBCommand().onecmd("create Place")
            tIdd = out_put.getvalue().strip()
        testing_Cmd = "Place.update({}, latitudee, 7.2)".format(tIdd)
        self.assertFalse(HBNBCommand().onecmd(testing_Cmd))
        testing_dict = storage.all()["Place.{}".format(tIdd)].__dict__
        self.assertEqual(7.2, testing_dict["latitudee"])

    def testing_update_valid_dictionary_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as out_put:
            HBNBCommand().onecmd("create BaseModel")
            testing_Id = out_put.getvalue().strip()
        testing_Cmd = "update BaseModel {} ".format(testing_Id)
        testing_Cmd += "{'attr_name': 'attr_value'}"
        HBNBCommand().onecmd(testing_Cmd)
        testing_dict = storage.all()["BaseModel.{}".format(testing_Id)].__dict__
        self.assertEqual("attr_value", testing_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as out_put:
            HBNBCommand().onecmd("create User")
            testing_Id = out_put.getvalue().strip()
        testing_Cmd = "update User {} ".format(testing_Id)
        testing_Cmd += "{'attr_name': 'attr_value'}"
        HBNBCommand().onecmd(testing_Cmd)
        testing_dict = storage.all()["User.{}".format(testing_Id)].__dict__
        self.assertEqual("attr_value", testing_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as out_put:
            HBNBCommand().onecmd("create State")
            testing_Id = out_put.getvalue().strip()
        testing_Cmd = "update State {} ".format(testing_Id)
        testing_Cmd += "{'attr_name': 'attr_value'}"
        HBNBCommand().onecmd(testing_Cmd)
        testing_dict = storage.all()["State.{}".format(testing_Id)].__dict__
        self.assertEqual("attr_value", testing_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as out_put:
            HBNBCommand().onecmd("create City")
            testing_Id = out_put.getvalue().strip()
        testing_Cmd = "update City {} ".format(testing_Id)
        testing_Cmd += "{'attr_name': 'attr_value'}"
        HBNBCommand().onecmd(testing_Cmd)
        testing_dict = storage.all()["City.{}".format(testing_Id)].__dict__
        self.assertEqual("attr_value", testing_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as out_put:
            HBNBCommand().onecmd("create Place")
            testing_Id = out_put.getvalue().strip()
        testing_Cmd = "update Place {} ".format(testing_Id)
        testing_Cmd += "{'attr_name': 'attr_value'}"
        HBNBCommand().onecmd(testing_Cmd)
        testing_dict = storage.all()["Place.{}".format(testing_Id)].__dict__
        self.assertEqual("attr_value", testing_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as out_put:
            HBNBCommand().onecmd("create Amenity")
            testing_Id = out_put.getvalue().strip()
        testing_Cmd = "update Amenity {} ".format(testing_Id)
        testing_Cmd += "{'attr_name': 'attr_value'}"
        HBNBCommand().onecmd(testing_Cmd)
        testing_dict = storage.all()["Amenity.{}".format(testing_Id)].__dict__
        self.assertEqual("attr_value", testing_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as out_put:
            HBNBCommand().onecmd("create Review")
            testing_Id = out_put.getvalue().strip()
        testing_Cmd = "update Review {} ".format(testing_Id)
        testing_Cmd += "{'attr_name': 'attr_value'}"
        HBNBCommand().onecmd(testing_Cmd)
        testing_dict = storage.all()["Review.{}".format(testing_Id)].__dict__
        self.assertEqual("attr_value", testing_dict["attr_name"])

    def testing_update_valid_dictionary_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as out_put:
            HBNBCommand().onecmd("create BaseModel")
            testing_Id = out_put.getvalue().strip()
        testing_Cmd = "BaseModel.update({}".format(testing_Id)
        testing_Cmd += "{'attr_name': 'attr_value'})"
        HBNBCommand().onecmd(testing_Cmd)
        testing_dict = storage.all()["BaseModel.{}".format(testing_Id)].__dict__
        self.assertEqual("attr_value", testing_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as out_put:
            HBNBCommand().onecmd("create User")
            testing_Id = out_put.getvalue().strip()
        testing_Cmd = "User.update({}, ".format(testing_Id)
        testing_Cmd += "{'attr_name': 'attr_value'})"
        HBNBCommand().onecmd(testing_Cmd)
        testing_dict = storage.all()["User.{}".format(testing_Id)].__dict__
        self.assertEqual("attr_value", testing_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as out_put:
            HBNBCommand().onecmd("create State")
            testing_Id = out_put.getvalue().strip()
        testing_Cmd = "State.update({}, ".format(testing_Id)
        testing_Cmd += "{'attr_name': 'attr_value'})"
        HBNBCommand().onecmd(testing_Cmd)
        testing_dict = storage.all()["State.{}".format(testing_Id)].__dict__
        self.assertEqual("attr_value", testing_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as out_put:
            HBNBCommand().onecmd("create City")
            testing_Id = out_put.getvalue().strip()
        testing_Cmd = "City.update({}, ".format(testing_Id)
        testing_Cmd += "{'attr_name': 'attr_value'})"
        HBNBCommand().onecmd(testing_Cmd)
        testing_dict = storage.all()["City.{}".format(testing_Id)].__dict__
        self.assertEqual("attr_value", testing_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as out_put:
            HBNBCommand().onecmd("create Place")
            testing_Id = out_put.getvalue().strip()
        testing_Cmd = "Place.update({}, ".format(testing_Id)
        testing_Cmd += "{'attr_name': 'attr_value'})"
        HBNBCommand().onecmd(testing_Cmd)
        testing_dict = storage.all()["Place.{}".format(testing_Id)].__dict__
        self.assertEqual("attr_value", testing_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as out_put:
            HBNBCommand().onecmd("create Amenity")
            testing_Id = out_put.getvalue().strip()
        testing_Cmd = "Amenity.update({}, ".format(testing_Id)
        testing_Cmd += "{'attr_name': 'attr_value'})"
        HBNBCommand().onecmd(testing_Cmd)
        testing_dict = storage.all()["Amenity.{}".format(testing_Id)].__dict__
        self.assertEqual("attr_value", testing_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as out_put:
            HBNBCommand().onecmd("create Review")
            testing_Id = out_put.getvalue().strip()
        testing_Cmd = "Review.update({}, ".format(testing_Id)
        testing_Cmd += "{'attr_name': 'attr_value'})"
        HBNBCommand().onecmd(testing_Cmd)
        testing_dict = storage.all()["Review.{}".format(testing_Id)].__dict__
        self.assertEqual("attr_value", testing_dict["attr_name"])

    def testing_update_valid_dictionary_with_int_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as out_put:
            HBNBCommand().onecmd("create Place")
            testing_Id = out_put.getvalue().strip()
        testing_Cmd = "update Place {} ".format(testing_Id)
        testing_Cmd += "{'max_guest': 98})"
        HBNBCommand().onecmd(testing_Cmd)
        testing_dict = storage.all()["Place.{}".format(testing_Id)].__dict__
        self.assertEqual(98, testing_dict["max_guest"])

    def testing_update_valid_dictionary_with_int_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as out_put:
            HBNBCommand().onecmd("create Place")
            testing_Id = out_put.getvalue().strip()
        testing_Cmd = "Place.update({}, ".format(testing_Id)
        testing_Cmd += "{'max_guest': 98})"
        HBNBCommand().onecmd(testing_Cmd)
        testing_dict = storage.all()["Place.{}".format(testing_Id)].__dict__
        self.assertEqual(98, testing_dict["max_guest"])

    def testing_update_valid_dictionary_with_float_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as out_put:
            HBNBCommand().onecmd("create Place")
            testing_Id = out_put.getvalue().strip()
        testing_Cmd = "update Place {} ".format(testing_Id)
        testing_Cmd += "{'latitude': 9.8})"
        HBNBCommand().onecmd(testing_Cmd)
        testing_dict = storage.all()["Place.{}".format(testing_Id)].__dict__
        self.assertEqual(9.8, testing_dict["latitude"])

    def testing_update_valid_dictionary_with_float_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as out_put:
            HBNBCommand().onecmd("create Place")
            testing_Id = out_put.getvalue().strip()
        testing_Cmd = "Place.update({}, ".format(testing_Id)
        testing_Cmd += "{'latitude': 9.8})"
        HBNBCommand().onecmd(testing_Cmd)
        testing_dict = storage.all()["Place.{}".format(testing_Id)].__dict__
        self.assertEqual(9.8, testing_dict["latitude"])


class Testing_HBNB_Command_count(unittest.TestCase):
    """Unittests thats for testing the count method of HBNB
    comand interpreter."""

    @classmethod
    def setsUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

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

    def testing_count_invalid_class(self):
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("MyModel.count()"))
            self.assertEqual("0", out_put.getvalue().strip())

    def testing_count_object(self):
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.count()"))
            self.assertEqual("1", out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("create User"))
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("User.count()"))
            self.assertEqual("1", out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("create State"))
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("State.count()"))
            self.assertEqual("1", out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("Place.count()"))
            self.assertEqual("1", out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("create City"))
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("City.count()"))
            self.assertEqual("1", out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("Amenity.count()"))
            self.assertEqual("1", out_put.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as out_put:
            self.assertFalse(HBNBCommand().onecmd("Review.count()"))
            self.assertEqual("1", out_put.getvalue().strip())


if __name__ == "__main__":
    unittest.main()

