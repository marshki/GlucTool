#!/usr/bin/env python3
# pylint: disable=W0613,W0622

"""Unit testing class.
"""

import unittest
from unittest.mock import patch

def menu():
    """Menu prompt.
    """

    while True:
        choice = input('Select an option (1, 2 or 3):  ')
        if choice in ('1', '2', '3'):
            return choice

class PlayAgainTest(unittest.TestCase):
    """Testing class.
    """

    @patch('builtins.input', return_value='1')
    def test_menu_01(self, input):
        """Valid return values.
        """
        self.assertIn(menu(), ('1', '2', '3'))

    @patch('builtins.input', return_value='3')
    def test_menu_02(self, input):
        """Valid return values.
        """
        self.assertIn(menu(), ('1', '2', '3'))

if __name__ == '__main__':
    unittest.main()
