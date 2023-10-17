#!/usr/bin/python3
""" Defining the tests for the Place class"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """ Tests for the Place class"""
    def setUp(self):
        """
        Set up the test case.
        """
        self.place = Place()

    def cleanUp(self):
        """
        Clean up after the test case.
        """
        pass

    def test_amenity_ids(self):
        """
        Testing the amenity_ids attribute.
        """
        amenity_ids = ["2", "1", "3"]
        self.place.amenity_ids = amenity_ids
        self.assertEqual(self.place.amenity_ids, amenity_ids)

    def test_city_id(self):
        """
        Testing the city_id attribute.
        """
        city_id = "123456789"
        self.place.city_id = city_id
        self.assertEqual(self.place.city_id, city_id)

    def test_description(self):
        """
        Testing the description attribute.
        """
        description = "Bulawayo City of Kings"
        self.place.description = description
        self.assertEqual(self.place.description, description)

    def test_latitude(self):
        """
        Testing the latitude attribute.
        """
        latitude = 67.3354
        self.place.latitude = latitude
        self.assertEqual(self.place.latitude, latitude)

    def test_longitude(self):
        """
        Testing the longitude attribute.
        """
        longitude = 13.536
        self.place.longitude = longitude
        self.assertEqual(self.place.longitude, longitude)

    def test_max_guest(self):
        """
        Testing the max_guest attribute.
        """
        max_guest = 5
        self.place.max_guest = max_guest
        self.assertEqual(self.place.max_guest, max_guest)

    def test_name(self):
        """
        Testing the name attribute.
        """
        name = "Gugulethu"
        self.place.name = name
        self.assertEqual(self.place.name, name)

    def test_number_bathrooms(self):
        """
        Testing the number_bathrooms attribute.
        """
        number_bathrooms = 3
        self.place.number_bathrooms = number_bathrooms
        self.assertEqual(self.place.number_bathrooms, number_bathrooms)

    def test_number_rooms(self):
        """
        Testing the number_rooms attribute.
        """
        number_rooms = 6
        self.place.number_rooms = number_rooms
        self.assertEqual(self.place.number_rooms, number_rooms)

    def test_price_by_night(self):
        """
        Testing the price_by_night attribute.
        """
        price_by_night = 40
        self.place.price_by_night = price_by_night
        self.assertEqual(self.place.price_by_night, price_by_night)

    def test_user_id(self):
        """
        Testing the user_id attribute.
        """
        user_id = "123456"
        self.place.user_id = user_id
        self.assertEqual(self.place.user_id, user_id)


if __name__ == '__main__':
    unittest.main()
