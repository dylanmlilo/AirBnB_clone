#!/usr/bin/python3
""" Defines a console module """
import cmd
import json
from models.base_model import BaseModel
from models import storage
from models.user import User


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
        """Creates a new instance of BaseModel,
        saves it to JSON file and prints the id"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()

        class_name = args[0]

        if class_name not in ["BaseModel", "User", "Place", "Review",
                              "State", "City", "Amenity"]:
            print("** class doesn't exist **")
            return

        new_instance = eval(class_name)()

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

        if class_name not in ["BaseModel"]:
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

        if class_name not in ["BaseModel"]:
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

    def do_all(self, arg):
        """
        Prints the string representation of
        all instances based on the class name
        """
        classes = ["BaseModel"]
        instances = storage.all()

        if not arg:
            print([str(instance) for instance in instances.values()])
            return

        class_name = arg.split()[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return

        filtered_instances = [str(instance)
                              for instance in instances.values()
                              if type(instance).__name__ == class_name]
        print(filtered_instances)

    def do_update(self, arg):
        """
        Updates an instance based on the class name
        and id by adding or updating attribute
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = args[0] + "." + instance_id
        instances = storage.all()

        if key not in instances:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        attribute_name = args[2]
        attribute_value = args[3]
        instance = instances[key]

        if attribute_name in ["id", "created_at", "updated_at"]:
            return

        if args[0] == "User":
            if attribute_name not in User.__dict__:
                print("** attribute doesn't exist **")
                return
        else:
            if attribute_name not in BaseModel.__dict__:
                print("** attribute doesn't exist **")
                return

        try:
            attribute_value = type(getattr(instance, attribute_name))
            (attribute_value)
        except ValueError:
            print("** value missing **")
            return

        setattr(instance, attribute_name, attribute_value)
        instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
