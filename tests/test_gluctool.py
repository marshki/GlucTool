"""Unit testing class for gluctool.
"""

from io import StringIO
import os
import tempfile
import textwrap
import unittest
from unittest.mock import patch

from gluctool.gluctool import (
    parse_cli_args,
    convert_mmol_to_mg,
    convert_mg_to_mmol,
    build_rows,
    conversion_table,
    export_to_csv
)

class TestCLIParsing(unittest.TestCase):
    """CLI argument parsing test class.
    """

    def test_parse_cli_args_mmol_to_mg(self):
        """Test argument parser.
        """
        with patch('sys.argv', ['script_name', '--mmol-to-mg', '5.5', '6.0']):
            args = parse_cli_args()
        self.assertEqual(args.mmol_to_mg, [5.5, 6.0])
        self.assertIsNone(args.mg_to_mmol)

    def test_parse_cli_args_mg_to_mmol(self):
        """Test arguments parser.
        """
        with patch('sys.argv', ['script_name', '--mg-to-mmol', '100', '150']):
            args = parse_cli_args()
        self.assertEqual(args.mg_to_mmol, [100, 150])
        self.assertIsNone(args.mmol_to_mg)

class TestConversions(unittest.TestCase):
    """Unit conversion test class.
    """

    def test_convert_mmol_to_mg(self):
        """Test conversion.
        """
        result = convert_mmol_to_mg(5.0)
        self.assertAlmostEqual(result, 90.0910, places=4)

    def test_convert_mg_to_mmol(self):
        """Test conversion.
        """
        result = convert_mg_to_mmol(90.0910)
        self.assertAlmostEqual(result, 5.0, places=4)

class TestRowGeneration(unittest.TestCase):
    """Row generation test class.
    """

    def test_build_rows(self):
        """
        Test rows are generated.
        """
        rows = build_rows(
            [100, 150],
            convert_mg_to_mmol,
            "mg/dl",
            "mmol/l"
        )

        expected = [
            {"mg/dl": 100.0, "mmol/l": 5.5499},
            {"mg/dl": 150.0, "mmol/l": 8.3249},
        ]
        self.assertEqual(rows, expected)

    def test_conversion_table(self):
        """
        Test table is generated.
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

    def test_export_to_csv_empty_rows_raises(self):
        """Test for empty row(s).
        """
        with self.assertRaises(ValueError):
            export_to_csv([], "out.csv")

    def test_export_to_csv_creates_file(self):
        """Test rows export to .csv
        """
        rows = [{"a": 1}]

        with tempfile.TemporaryDirectory() as tmpdir:
            outpath = os.path.join(tmpdir, "out.csv")
            export_to_csv(rows, outpath)
            self.assertTrue(os.path.exists(outpath))

if __name__ == '__main__':
    unittest.main()
