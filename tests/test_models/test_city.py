#!/usr/bin/python3
""" Defines tests for the City class """
import unittest
from datetime import datetime
from models.city import City


class TestCity(unittest.TestCase):
    """ Tests for the City class"""
    def test_init(self):
        """Testing the initialization of the City instance"""
        city = City()
        self.assertIsInstance(city, City)
        self.assertIsInstance(city.created_at, datetime)
        self.assertIsInstance(city.updated_at, datetime)
        self.assertEqual(city.name, "")
        self.assertEqual(city.state_id, "")

    def test_name_assignment(self):
        """Testing the assignment of the name attribute"""
        city = City()
        city.name = "Bulawayo"
        self.assertEqual(city.name, "Bulawayo")

    def test_state_id_assignment(self):
        """Testing the assignment of the state_id attribute"""
        city = City()
        city.state_id = "Matabele"
        self.assertEqual(city.state_id, "Matabele")

    def test_str(self):
        """Testing the string representation of the City instance"""
        city = City()
        expected = f"[{type(city).__name__}] ({city.id}) {city.__dict__}"
        self.assertEqual(str(city), expected)


if __name__ == '__main__':
    unittest.main()
