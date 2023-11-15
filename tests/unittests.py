import unittest
import textwrap
from unittest.mock import patch
from io import StringIO
from gluctool import parse_cli_args, convert_mmol_to_mg, convert_mg_to_mmol, conv_table

class TestGluConverter(unittest.TestCase):

    def test_parse_cli_args_mg_to_mmol(self):
        with patch('sys.argv', ['script_name', '--mg-to-mmol', '100', '150']):
            args = parse_cli_args()
        self.assertEqual(args.mg_to_mmol, [100, 150])
        self.assertIsNone(args.mmol_to_mg)

    def test_parse_cli_args_mmol_to_mg(self):
        with patch('sys.argv', ['script_name', '--mmol-to-mg', '5.5', '6.0']):
            args = parse_cli_args()
        self.assertEqual(args.mmol_to_mg, [5.5, 6.0])
        self.assertIsNone(args.mg_to_mmol)

    def test_convert_mmol_to_mg(self):
        result = convert_mmol_to_mg(5.0)
        self.assertAlmostEqual(result, 90.091)

    def test_convert_mg_to_mmol(self):
        result = convert_mg_to_mmol(90.091)
        self.assertAlmostEqual(result, 5.0)

    def test_conv_table(self):
        col1 = [100, 150]
        col2_func = convert_mg_to_mmol
        c1_hdr = 'mg/dl'
        c2_hdr = 'mmol/l'

        # Redirect stdout to capture printed output
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            conv_table(col1, col2_func, c1_hdr, c2_hdr)

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
