#!/usr/bin/env python3

"""Command line utility to convert blood glucose levels between Intl. and US standards:
Millimoles Per Litre (mmol/l) --> mmol/l * 18.0182 = mg/dl
Milligrams Per Decileter (mg/dl) --> mg/dl / 18.0182 = mmol/l
"""

import argparse

MMOL_TO_MG = 18.0182

def parse_cli_args():
    """Define CLI parameters and return arguments.
    """

    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--mg-to-mmol", help="mg/dl to mmol/l", nargs='+', type=float)
    group.add_argument("--mmol-to-mg", help="mmol/l to mg/dl", nargs='+', type=float)
    args = parser.parse_args()
    return args

def convert_mmol_to_mg(x):
    """Convert mmol/l to mg/dl equivalent
    """
    return x*MMOL_TO_MG

def convert_mg_to_mmol(x):
    """Convert mg/dl to mmol/l equivalent
    """
    return x/MMOL_TO_MG

def conv_table(col1, col2_func, c1_hdr, c2_hdr):
    """Return conversions in two-column tabular format.
    """

    print('+------------+------------+')
    print('| {:^10} | {:^10} |'.format(c1_hdr, c2_hdr))
    print('+------------+------------+')
    for x in col1:
        y = col2_func(x)
        print('| {:10.4f} | {:10.4f} |'.format(x, y))
    print('+------------+------------+')

def user_float():
    """Prompt user for input, accepting only valid input.
    """

    while True:
        try:
            return float(input('Enter the plasma glucose level you want to convert:  '))
        except ValueError:
            print('Bad value, try again.')

def menu():
    """Menu prompt for user to select program option.
    """

    while True:
        print('1. I want to convert a plasma glucose level from mg/dl to mmol/l.')
        print('2. I want to convert a plasma glucose level from mmol/l to mg/dl.')
        print('3. I want to quit.')
        print()
        choice = input('Select an option (1, 2 or 3):  ')
        if choice in ('1', '2', '3'):
            return choice

def interactive_mode():
    """Display menu-driven options and return conversions.
    """

    while True:
        choice = menu()
        if choice == '3':
            break
        elif choice == '1':
            mg = user_float()
            mmol = convert_mg_to_mmol(mg)
            print('\n{:.4f} mg/dl   =   {:.4f} mmol/l\n'.format(mg, mmol))
            # {:.4f} print to 4th decimal point
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
