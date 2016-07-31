#!/usr/bin/env python3 

"""
A menu-driven program which converts plasma glucose levels from:
	* milligram per declieter to millimole per liter (mg/dl to mmol/l)
        * millimole per liter to milligram per decileter (mmol/l to mg/dl)
"""

# Define global

MMOL_TO_MG = 18.0182 			# mmol/l * 18.0182 = mg/dl 

# Define functions 

def convert_mmol_to_mg(x):
    """Convert mmol/l to mg/dl equivalent"""
    return x*MMOL_TO_MG


def convert_mg_to_mmol(x): 
    """Convert mg/dl to mmol/l equivalent"""
    return x/MMOL_TO_MG


def user_float():
    """Prompt user for input, accepting only valid input""" 
    while True:
        try:
            return float(input('Enter the plasma glucose level you want to convert:  '))
        except ValueError:
            print('Bad value, try again.')


def menu():
    """Menu prompt for user to select program option"""
    while True:
        print('1. I want to convert a plasma glucose level from mg/dl to mmol/l.')
        print('2. I want to convert a plasma glucose level from mmol/l to mg/dl.')
        print('3. I want to quit.')
        print()
        choice = input('Select an option (1, 2 or 3):  ')
        if choice in ('1','2','3'):
            return choice


def interactive_mode():
    """Guts of the program""" 
    while True:
        choice = menu()
        if choice == '3':
            break
        elif choice == '1':
            mg = user_float()
            mmol = convert_mg_to_mmol(mg)
            print('\n{:.4f} mg/dl   =   {:.4f} mmol/l\n'.format(mg, mmol))	# {:.4f} print to 4th decimal point
        elif choice == '2':
            mmol = user_float()
            mg = convert_mmol_to_mg(mmol)
            print('\n{:.4f} mmol/l   =   {:.4f} mg/dl\n'.format(mmol, mg))		

print('\nWelcome to the GluConverter!\n')
interactive_mode()
print('\nThanks for visiting!\n')
