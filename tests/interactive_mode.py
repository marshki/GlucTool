#!/usr/bin/env python3

"""Unit testing class.
"""

CHOICE = '2'

def interactive_mode():
    """Interactive mode.
    """

    while True:
        #choice = menu()
        if CHOICE == '3':
            break
        elif CHOICE == '1':
            #mg = user_float()
            #mmol = convert_mg_to_mmol(mg)
            mg = float(5)
            mmol = (mg*18.0182)
            print('\n{:.4f} mg/dl   =   {:.4f} mmol/l\n'.format(mg, mmol))
            break
        elif CHOICE == '2':
            #mmol = user_float()
            #mg = convert_mmol_to_mg(mmol)
            mmol = float(10)
            mg = (mmol/18.0182)
            print('\n{:.4f} mmol/l   =   {:.4f} mg/dl\n'.format(mmol, mg))
            break

interactive_mode()
