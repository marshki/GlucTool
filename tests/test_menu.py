#!/usr/bin/env python3

"""Unit testing class.
"""

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

menu()
