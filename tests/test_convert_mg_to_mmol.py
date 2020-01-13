#!/user/bin/env python

"""Unit test class.
"""

import unittest

MMOL_TO_MG = 18.0182

def convert_mg_to_mmol(x_value):
    """Convert mg/dl to mmol/l equivalent.
    """
    return x_value/MMOL_TO_MG

class ConversionTest(unittest.TestCase):
    """Unit tests.
    """

    def test_convert_mg_to_mmol(self):
        """Valid return values.
        """
        self.assertEqual(round(convert_mg_to_mmol(5), 4), 0.2775)
        self.assertEqual(round(convert_mg_to_mmol(10), 4), 0.5550)
        self.assertEqual(convert_mg_to_mmol(0), 0)

if __name__ == '__main__':
    unittest.main()
