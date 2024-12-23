#!/usr/bin/env python3

"""Arg parser converts blood glucose levels btwn. Intl. (mmol/l) and US (mg/dl) stnds.
"""

import argparse

MMOL_TO_MG_CONVERSION_FACTOR = 18.0182

def parse_cli_args():
    """Define argument parser w/mutually exclusive arguments to convert.
    Returns:
        argparse.Namespace: Parsed command line arguments.
    """
    parser = argparse.ArgumentParser(description= \
        "Convert blood glucose levels between mmol/l and mg/dl.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--mg-to-mmol", help="mg/dl to mmol/l", nargs='+', type=float)
    group.add_argument("--mmol-to-mg", help="mmol/l to mg/dl", nargs='+', type=float)
    return parser.parse_args()

def convert_mmol_to_mg(mmol_value):
    """Convert mmol/l to mg/dl.
    Args:
        mmol_value (float): Glucose level in mmol/l.
    Returns:
        float: Glucose level in mg/dl.
    """
    return mmol_value * MMOL_TO_MG_CONVERSION_FACTOR

def convert_mg_to_mmol(mg_value):
    """Convert mg/dl to mmol/l.
    Args:
        mg_value (float): Glucose level in mg/dl.
    Returns:
        float: Glucose level in mmol/l.
    """
    return mg_value / MMOL_TO_MG_CONVERSION_FACTOR

def conversion_table(values, conversion_func, from_unit, to_unit):
    """Print a formatted table of converted glucose values.
    Args:
        values (list of float): List of glucose values to convert.
        conversion_func (function): Conversion.
        from_unit (str): Unit of input values.
        to_unit (str): Unit of output values.
    """
    print('+------------+------------+')
    print(f'| {from_unit:^10} | {to_unit:^10} |')
    print('+------------+------------+')
    for value in values:
        converted_value = conversion_func(value)
        print(f'| {value:10.4f} | {converted_value:10.4f} |')
    print('+------------+------------+')

def main():
    """Main function to parse command line arguments and print the conversion table
    for blood glucose levels.
    """
    args = parse_cli_args()

    if args.mg_to_mmol:
        conversion_table(args.mg_to_mmol, convert_mg_to_mmol, 'mg/dl', 'mmol/l')
    elif args.mmol_to_mg:
        conversion_table(args.mmol_to_mg, convert_mmol_to_mg, 'mmol/l', 'mg/dl')

if __name__ == '__main__':
    main()
