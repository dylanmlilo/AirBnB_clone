#!/usr/bin/python3
""" Defines a module for testing the BaseModel class"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ Test cases for the BaseModel class """
    def test_init(self):
        """ Testing the initialization of the BaseModel instance """
        test_model = BaseModel()
        self.assertIsInstance(test_model, BaseModel)
        self.assertIsNotNone(test_model.id)
        self.assertIsInstance(test_model.created_at, datetime)
        self.assertIsInstance(test_model.updated_at, datetime)

    def test_str(self):
        """ Testing the string representation of the BaseModel instance """
        t_model = BaseModel()
        exp = f"[{type(t_model).__name__}] ({t_model.id}) {t_model.__dict__}"
        self.assertEqual(str(t_model), exp)

    def test_save_method(self):
        """
           Testing that the save method updates the
           updated_at attribute to the current datetime
        """
        test_model = BaseModel()
        initial = test_model.updated_at
        updated = test_model.save()
        self.assertNotEqual(initial, updated)

    def test_to_dict(self):
        """ Testing the to_dict method of the BaseModel instance """
        tmod = BaseModel()
        model_dict = tmod.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict["__class__"], type(tmod).__name__)
        self.assertEqual(model_dict["id"], tmod.id)
        self.assertEqual(model_dict["created_at"], tmod.created_at.isoformat())
        self.assertEqual(model_dict["updated_at"], tmod.updated_at.isoformat())

    def test_instance_of_datetime(self):
        """
        Testing that the created_at and updated_at
        attributes are instances of datetime
        """
        test_model = BaseModel()
        self.assertIsInstance(test_model.created_at, datetime)
        self.assertIsInstance(test_model.updated_at, datetime)


if __name__ == '__main__':
    unittest.main()
