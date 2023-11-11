#!/usr/bin/env/ python3

"""Unit test class.
"""

def conv_table(col1, col2_func, c1_hdr, c2_hdr):
    """Formatted table with (2) columns and (2) headers.
    """

    print('+------------+------------+')
    print('| {:^10} | {:^10} |'.format(c1_hdr, c2_hdr))
    print('+------------+------------+')
    for x_value in col1:
        y_value = col2_func(x_value)
        print('| {:10.4f} | {:10.4f} |'.format(x_value, y_value))
    print('+------------+------------+')

conv_table(col1, col2_func, c1_hdr, c2_hdr)
