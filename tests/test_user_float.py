#!/usr/bin/env python3
# pylint: disable=W0613,W0622

"""Unit testing class for numerical input.
"""

import unittest
from unittest.mock import patch

def user_float():
    """User-defined floating point int.
    """

    while True:
        try:
            return float(input('Enter plasma glucose level to convert:  '))
        except ValueError:
            print('Bad value, try again.')
            raise

class UserFloatTest(unittest.TestCase):

    """Unit tests.
    Use `patch()` to mock objects for testing.
    For reference: https://docs.python.org/3/library/unittest.mock.html
    """

    @patch('builtins.input', return_value='5')
    def test_user_float_01(self, input):
        """Valid return value.
        """
        self.assertIsInstance(user_float(), float)

    @patch('builtins.input', return_value='10')
    def test_user_float_02(self, input):
        """Valid return value.
        """
        self.assertIsInstance(user_float(), float)

    @patch('builtins.input', return_value='Derp!')
    def test_user_float_03(self, input):
        """Invalid return value.
        """
        with self.assertRaises(ValueError):
            user_float()

if __name__ == '__main__':
    unittest.main()
