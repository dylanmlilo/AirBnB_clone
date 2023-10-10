#!/usr/bin/python3
""" Defines a python test module """


import unittest
from models.base_model import BaseModel

def test_id_is_string(self):
    obj = BaseModel()
    self.assertIsInstance(obj.id, str)

def test_created_at_is_string(self):
    obj = BaseModel()
    self.assertIsInstance(obj.created_at, str)

def test_updated_at_is_string(self):
    obj = BaseModel()
    self.assertIsInstance(obj.updated_at, str)

if __name__ == '__main__':
    unittest.main() 
