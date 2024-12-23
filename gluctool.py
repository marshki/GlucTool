#!/usr/bin/env python3

"""An argument parser to convert blood glucose levels between
International (mmol/l) and US (mg/dl) standards.
"""

import argparse

MMOL_TO_MG = 18.0182

def parse_cli_args():
    """Define parser w/arguments.
    """

    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--mg-to-mmol", help="mg/dl to mmol/l", nargs='+', type=float)
    group.add_argument("--mmol-to-mg", help="mmol/l to mg/dl", nargs='+', type=float)
    args = parser.parse_args()
    return args

def convert_mmol_to_mg(x_value):
    """Convert mmol/l to mg/dl equivalent.
    """
    return x_value*MMOL_TO_MG

def convert_mg_to_mmol(x_value):
    """Convert mg/dl to mmol/l equivalent.
    """
    return x_value/MMOL_TO_MG

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

if __name__ == '__main__':
    cli_args = parse_cli_args()

    if cli_args.mg_to_mmol:
        conv_table(cli_args.mg_to_mmol, convert_mg_to_mmol, 'mg/dl', 'mmol/l')
    if cli_args.mmol_to_mg:
        conv_table(cli_args.mmol_to_mg, convert_mmol_to_mg, 'mmol/l', 'mg/dl')
