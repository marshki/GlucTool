#!/user/bin/env python

"""Unit test class.
"""

import unittest

MMOL_TO_MG = 18.0182

def convert_mmol_to_mg(x_value):
    """Convert mmol/l to mg/dl equivalent.
    """
    return x_value*MMOL_TO_MG

class ConversionTest(unittest.TestCase):
    """Unit tests.
    """

    def test_convert_mmol_to_mg(self):
        """Valid return values.
        """
        self.assertEqual(round(convert_mmol_to_mg(5), 4), 90.0910)
        self.assertEqual(round(convert_mmol_to_mg(10), 4), 180.1820)
        self.assertEqual(convert_mmol_to_mg(0), 0)

if __name__ == '__main__':
    unittest.main()
