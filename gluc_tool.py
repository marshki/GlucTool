#!/sur/bin/env python3 

#import argparse


MMOL_TO_MG = 18.0182

def convert_mmol_to_mg(x):
    return x*MMOL_TO_MG

def convert_mg_to_mmol(x):
    return x/MMOL_TO_MG

def user_float():
    while True:
        try:
            return float(input('Type in a number:  '))
        except ValueError:
            print('Bad value, try again')


def menu():
    while True:
        print('1. I want to convert a plasma glucose level from mg/dl to mmol/l.')
        print('2. I want to convert a plasma glucose level from mmol/l to mg/dl.')
        print('3. I want to quit.')
        print()
        choice = input('Select an option (1, 2 or 3):  ')
        if choice in ('1','2','3'):
            return choice



def interactive_mode():
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

print('Welcome to the GluConverter!\n')
interactive_mode()
print('bye!')
