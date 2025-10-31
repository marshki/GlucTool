#!/usr/bin/env python3

"""
Unit testing class for gluctool.
"""

import os
import sys
from io import StringIO
import textwrap
import unittest
from unittest.mock import patch

from gluctool.gluctool import (
    parse_cli_args,
    convert_mmol_to_mg,
    convert_mg_to_mmol,
    conversion_table
)

class TestGluctool(unittest.TestCase):

    """
    Unit tests.
    """

    def test_parse_cli_args_mg_to_mmol(self):
        """
        Test argument parser.
        """
        with patch('sys.argv', ['script_name', '--mg-to-mmol', '100', '150']):
            args = parse_cli_args()
        self.assertEqual(args.mg_to_mmol, [100, 150])
        self.assertIsNone(args.mmol_to_mg)

    def test_parse_cli_args_mmol_to_mg(self):
        """
        Test argument parser.
        """
        with patch('sys.argv', ['script_name', '--mmol-to-mg', '5.5', '6.0']):
            args = parse_cli_args()
        self.assertEqual(args.mmol_to_mg, [5.5, 6.0])
        self.assertIsNone(args.mg_to_mmol)

    def test_convert_mmol_to_mg(self):
        """
        Test conversion.
        """
        result = convert_mmol_to_mg(5.0)
        self.assertAlmostEqual(result, 90.091, places=3)

    def test_convert_mg_to_mmol(self):
        """
        Test conversion.
        """
        result = convert_mg_to_mmol(90.091)
        self.assertAlmostEqual(result, 5.0, places=3)

    def test_conversion_table(self):
        """
        Test table output.
        """
        col1 = [100, 150]
        col2_func = convert_mg_to_mmol
        c1_hdr = 'mg/dl'
        c2_hdr = 'mmol/l'

        # Redirect stdout to capture printed output
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            conversion_table(col1, col2_func, c1_hdr, c2_hdr)

        expected_output = textwrap.dedent("""
           +------------+------------+
           |   mg/dl    |   mmol/l   |
           +------------+------------+
           |  100.0000  |   5.5499   |
           |  150.0000  |   8.3249   |
           +------------+------------+
        """).strip().replace(" ", "")

        actual_output = mock_stdout.getvalue().strip().replace(" ", "")

        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()
