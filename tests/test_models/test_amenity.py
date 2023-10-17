#!/usr/bin/python3
""" Defines tests for the Amenity class """
import unittest
from datetime import datetime
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """ Test cases for the Amenity class """
    def test_init(self):
        """Testing the initialization of the Amenity instance"""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertIsInstance(amenity.created_at, datetime)
        self.assertIsInstance(amenity.updated_at, datetime)
        self.assertEqual(amenity.name, "")

    def test_name_assignment(self):
        """Testing the assignment of the name attribute"""
        amenity = Amenity()
        amenity.name = "Wifi"
        self.assertEqual(amenity.name, "Wifi")

    def test_str(self):
        """Testing the string representation of the Amenity instance"""
        amenity = Amenity()
        exp = f"[{type(amenity).__name__}] ({amenity.id}) {amenity.__dict__}"
        self.assertEqual(str(amenity), exp)


if __name__ == '__main__':
    unittest.main()
