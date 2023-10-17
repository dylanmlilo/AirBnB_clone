#!/usr/bin/python3
""" Defining the tests for the state class """
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """ Tests for the State class """
    def setUp(self):
        """
        Set up the test case.
        """
        self.state = State()

    def cleanUp(self):
        """
        Clean up after the test case.
        """
        pass

    def test_name(self):
        """
        Test the name attribute.
        """
        name = "Matabeleland"
        self.state.name = name
        self.assertEqual(self.state.name, name)


if __name__ == '__main__':
    unittest.main()
