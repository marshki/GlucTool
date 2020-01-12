#!/usr/bin/env python3

"""Utility to convert blood glucose levels between Intl. and US standards.
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

def user_float():
    """User-defined floating point int.
    Args: Value to convert.
    Returns: Floating point int.
    Raises: ValueError.
    """

    while True:
        try:
            return float(input('Enter plasma glucose level to convert:  '))
        except ValueError:
            print('Bad value, try again.')

def menu():
    """Menu prompt.
    Args: User-defined input.
    Returns: Choice if arg in: 1, 2, or 3.
    Raises:
    """

    while True:
        print('1. Convert plasma glucose level from mg/dl to mmol/l.')
        print('2. Convert plasma glucose level from mmol/l to mg/dl.')
        print('3. Quit.')
        print()
        choice = input('Select an option (1, 2 or 3):  ')
        if choice in ('1', '2', '3'):
            return choice

def interactive_mode():
    """Interactive mode.
    Args: User-defined input.
    Returns: Converted float({:.4f} print to 4th decimal point).
    Raises:
    """

    while True:
        choice = menu()
        if choice == '3':
            break
        elif choice == '1':
            mg = user_float()
            mmol = convert_mg_to_mmol(mg)
            print('\n{:.4f} mg/dl   =   {:.4f} mmol/l\n'.format(mg, mmol))
        elif choice == '2':
            mmol = user_float()
            mg = convert_mmol_to_mg(mmol)
            print('\n{:.4f} mmol/l   =   {:.4f} mg/dl\n'.format(mmol, mg))

if __name__ == '__main__':
    args = parse_cli_args()

    if args.mg_to_mmol:
        conv_table(args.mg_to_mmol, convert_mg_to_mmol, 'mg/dl', 'mmol/l')
    elif args.mmol_to_mg:
        conv_table(args.mmol_to_mg, convert_mmol_to_mg, 'mmol/l', 'mg/dl')
    else:

        print('\nWelcome to the GluConverter!\n')
        interactive_mode()
        print('\nThanks for visiting!\n')
