#!/usr/bin/python3
import unittest
from models.user import User


class TestUser(unittest.TestCase):

    def setUp(self):
        """
        Setting up the test case.
        """
        self.user = User()

    def cleanUp(self):
        """
        Clean up after the test case.
        """
        pass

    def test_email(self):
        """
        Testing the email attribute.
        """
        email = "dylanmlilo@example.com"
        self.user.email = email
        self.assertEqual(self.user.email, email)

    def test_first_name(self):
        """
        Testing the first_name attribute.
        """
        first_name = "John"
        self.user.first_name = first_name
        self.assertEqual(self.user.first_name, first_name)

    def test_last_name(self):
        """
        Testing the last_name attribute.
        """
        last_name = "Dylan"
        self.user.last_name = last_name
        self.assertEqual(self.user.last_name, last_name)

    def test_password(self):
        """
        Testing the password attribute.
        """
        password = "123456pass"
        self.user.password = password
        self.assertEqual(self.user.password, password)


if __name__ == '__main__':
    unittest.main()
