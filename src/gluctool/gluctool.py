#!/usr/bin/env python3

"""Argument parser converts blood glucose levels between 
International (mmol/l) and US (mg/dl) standards.
"""

import argparse
import csv

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

def convert_to_rows(values, conversion_func, from_unit, to_unit):
    """Convert glucose value(s) in to row(s) with labels. 
    Args:
        values (list[float]): List of glucose values to convert.
        conversion_func (callable): Converst a single value.
        from_unit (str): Unit of input values.
        to_unit (str): Unit of output values.
    Returns:
        list[dict]: Dictionary maps units to values.
    """
    rows = []
    for value in values:
        rows.append({
            from_unit: round(value, 4),
            to_unit: round(conversion_func(value),4),
        })
    return rows

def conversion_table(values, conversion_func, from_unit, to_unit):
    """Print a formatted table of converted glucose values.
    Args:
        values (list[float]): List of glucose values to convert.
        conversion_func (callable): Convert a single value.
        from_unit (str): Unit of input values.
        to_unit (str): Unit of converted values.
    Returns:
        None
    """
    rows = convert_to_rows(values, conversion_func, from_unit, to_unit)

    print('+------------+------------+')
    print(f'| {from_unit:^10} | {to_unit:^10} |')
    print('+------------+------------+')

    for row in rows:
        print(f'| {row[from_unit]:10.4f} | {row[to_unit]:10.4f} |')

    print('+------------+------------+')

def export_to_csv(rows, filename):
    """Write converted rows to a .csv file.
    """
    if not rows:
        return

    fieldnames = rows[0].keys()

    with open(filename, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

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
