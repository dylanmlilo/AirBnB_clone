#!/usr/bin/python3
""" Defines a console module """


import cmd
import datetime
import re
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State

all_classes = {
    "Amenity": Amenity,
    "BaseModel": BaseModel,
    "City": City,
    "Place": Place,
    "Review": Review,
    "State": State,
    "User": User
}

attributes = {
    "BaseModel": {
        "id": str,
        "created_at": datetime.datetime,
        "updated_at": datetime.datetime
    },
    "User": {
        "email": str,
        "password": str,
        "first_name": str,
        "last_name": str
    },
    "State": {
        "name": str
    },
    "City": {
        "state_id": str,
        "name": str
    },
    "Amenity": {
        "name": str
    },
    "Place": {
        "city_id": str,
        "user_id": str,
        "name": str,
        "description": str,
        "number_rooms": int,
        "number_bathrooms": int,
        "max_guest": int,
        "price_by_night": int,
        "latitude": float,
        "longitude": float,
        "amenity_ids": list
    },
    "Review": {
        "place_id": str,
        "user_id": str,
        "text": str
    }
}


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        return True

    def help_quit(self):
        """Exit the program"""
        print("Quit command to exit the program")

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_create(self, arg):
        """ Creates a new instance of BaseModel,
        saves it to JSON file and prints the id """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]

        if class_name not in all_classes:
            print("** class doesn't exist **")
            return

        new_instance = all_classes[class_name]()
        new_instance.save()

        print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an
        instance based on the class name and id
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]

        if class_name not in all_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = class_name + "." + instance_id
        instances = storage.all()

        if key not in instances:
            print("** no instance found **")
            return

        instance = instances[key]
        print(instance)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]

        if class_name not in all_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = class_name + "." + instance_id
        instances = storage.all()

        if key not in instances:
            print("** no instance found **")
            return

        del instances[key]
        storage.save()

    def do_update(self, args):
        """
        Updates a specified instance of a class using the id
        and either adding more attributes or updating an attribute
        """
        if not args:
            print("** class name missing **")
            return

        paten = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(paten, args)
        if not match:
            print("** class name missing **")
            return

        class_name = match.group(1)
        instance_id = match.group(2)
        attribute_name = match.group(3)
        value = match.group(4)

        if class_name not in all_classes:
            print("** class doesn't exist **")
            return

        if not instance_id:
            print("** instance id missing **")
            return

        instance_key = "{}.{}".format(class_name, instance_id)
        if instance_key not in storage.all():
            print("** no instance found **")
            return

        instance = storage.all()[instance_key]
        if attribute_name:
            if not value:
                print("** value missing **")
                return

            if attribute_name in attributes[class_name]:
                value = attributes[class_name][attribute_name](value)
            else:
                try:
                    if '.' in value:
                        value = float(value)
                    else:
                        value = int(value)
                except ValueError:
                    pass

            setattr(instance, attribute_name, value)
            instance.save()
        else:
            print("** attribute name missing **")

    def do_all(self, arg):
        """
        Prints the string representation of
        all instances based on the class name
        """
        if not arg:
            print([str(instance) for instance in storage.all().values()])
            return

        class_name = arg.split()[0]
        if class_name not in all_classes:
            print("** class doesn't exist **")
            return

        instances = [str(instance)
                     for instance in storage.all().values()
                     if isinstance(instance, all_classes[class_name])]
        print(instances)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
