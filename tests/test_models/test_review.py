#!/usr/bin/python3
""" Defining a class for testing Review class"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """ Tests for the Review class """
    def setUp(self):
        """
        Set up the test case.
        """
        self.review = Review()

    def cleanUp(self):
        """
        Clean up after the test case.
        """
        pass

    def test_place_id(self):
        """
        Testing the place_id attribute.
        """
        place_id = "123456"
        self.review.place_id = place_id
        self.assertEqual(self.review.place_id, place_id)

    def test_user_id(self):
        """
        Testing the user_id attribute.
        """
        user_id = "34527"
        self.review.user_id = user_id
        self.assertEqual(self.review.user_id, user_id)

    def test_text(self):
        """
        Testing the text attribute.
        """
        text = "Review class"
        self.review.text = text
        self.assertEqual(self.review.text, text)


if __name__ == '__main__':
    unittest.main()
