#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd

import re

from models import storage

from shlex import split

from models.base_model import BaseModel

from models.state import State

from models.user import User

from models.city import City

from models.place import Place

from models.amenity import Amenity

from models.review import Review


def parse(arg):
    curlyy_bracess = re.search(r"\{(.*?)\}", arg)
    bracketss = re.search(r"\[(.*?)\]", arg)
    if curlyy_bracess is None:
        if bracketss is None:
            return [x.strip(",") for x in split(arg)]
        else:
            lexerr = split(arg[:bracketss.span()[0]])
            retll = [x.strip(",") for x in lexerr]
            retll.append(bracketss.group())
            return retll
    else:
        lexerr = split(arg[:curlyy_bracess.span()[0]])
        retll = [x.strip(",") for x in lexerr]
        retll.append(curlyy_bracess.group())
        return retll


class HBNBCommand(cmd.Cmd):
    """Defining the HolbertonBnB's commandd interpreter.

    Attributes:
        promptt (str): The commandd's promptt.
    """

    promptt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """Do not do anything upon receiving any empty line."""
        pass

    def default(self, arg):
        """Default for the behavior for the cmd module when the input
        is invalid"""
        arggdictt = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        matchh = re.search(r"\.", arg)
        if matchh is not None:
            argll = [arg[:matchh.span()[0]], arg[matchh.span()[1]:]]
            matchh = re.search(r"\((.*?)\)", argll[1])
            if matchh is not None:
                commandd = [argll[1][:matchh.span()[0]], matchh.group()[1:-1]]
                if commandd[0] in arggdictt.keys():
                    calll = "{} {}".format(argll[0], commandd[1])
                    return arggdictt[commandd[0]](calll)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """The quit commandd for exiting the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal for the exit the program."""
        print("")
        return True

    def do_create(self, arg):
        """Usage: create <class>
        Creating a new class's instance and to print out its id.
        """
        argll = parse(arg)
        if len(argll) == 0:
            print("** class name missing **")
        elif argll[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(argll[0])().id)
            storage.save()

    def do_show(self, arg):
        """Usage: show <class> <id> or <class>.show(<id>)
        Displays the string's representation of a class's instance of a given id.
        """
        argll = parse(arg)
        objdictt = storage.all()
        if len(argll) == 0:
            print("** class name missing **")
        elif argll[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argll) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argll[0], argll[1]) not in objdictt:
            print("** no instance found **")
        else:
            print(objdictt["{}.{}".format(argll[0], argll[1])])

    def do_destroy(self, arg):
        """Usage: destroy <class> <id> or <class>.destroy(<id>)
        Deleting a class's instance of the id given."""
        argll = parse(arg)
        objdictt = storage.all()
        if len(argll) == 0:
            print("** class name missing **")
        elif argll[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argll) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argll[0], argll[1]) not in objdictt.keys():
            print("** no instance found **")
        else:
            del objdictt["{}.{}".format(argll[0], argll[1])]
            storage.save()

    def do_all(self, arg):
        """Usage: all or all <class> or <class>.all()
        Displays the string's representations of all the instances of the class given.
        If there is no class specified, displays all the instantiated objects."""
        argll = parse(arg)
        if len(argll) > 0 and argll[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objl = []
            for objt in storage.all().values():
                if len(argll) > 0 and argll[0] == objt.__class__.__name__:
                    objl.append(objt.__str__())
                elif len(argll) == 0:
                    objl.append(objt.__str__())
            print(objl)

    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        Retrieves all the number of the instances of the class given."""
        argll = parse(arg)
        countt = 0
        for objt in storage.all().values():
            if argll[0] == objt.__class__.__name__:
                countt += 1
        print(countt)

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
       <class>.update(<id>, <attribute_name>, <attribute_value>) or
       <class>.update(<id>, <dictionary>)
        Updates a class's instance of the given id by adding or by updating
        a given attribute's key/value pair or dictionary."""
        argll = parse(arg)
        objdictt = storage.all()

        if len(argll) == 0:
            print("** class name missing **")
            return False
        if argll[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(argll) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argll[0], argll[1]) not in objdictt.keys():
            print("** no instance found **")
            return False
        if len(argll) == 2:
            print("** attribute name missing **")
            return False
        if len(argll) == 3:
            try:
                type(eval(argll[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(argll) == 4:
            objt = objdictt["{}.{}".format(argll[0], argll[1])]
            if argll[2] in objt.__class__.__dict__.keys():
                valutype = type(objt.__class__.__dict__[argll[2]])
                objt.__dict__[argll[2]] = valutype(argll[3])
            else:
                objt.__dict__[argll[2]] = argll[3]
        elif type(eval(argll[2])) == dict:
            objt = objdictt["{}.{}".format(argll[0], argll[1])]
            for a, b in eval(argll[2]).items():
                if (a in objt.__class__.__dict__.keys() and
                        type(objt.__class__.__dict__[a]) in {str, int, float}):
                    valutype = type(objt.__class__.__dict__[a])
                    objt.__dict__[a] = valutype(b)
                else:
                    objt.__dict__[a] = b
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()

