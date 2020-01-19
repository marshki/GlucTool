#!/usr/bin/env python3

"""Unit testing class.
"""

choice = '1'

def interactive_mode():
    """Interactive mode.
    """

    while True:
        #choice = menu()
        if choice == '3':
            break
        elif choice == '1':
            #mg = user_float()
            #mmol = convert_mg_to_mmol(mg)
            mg = float(5)
            mmol = (mg*18.0182)
            print('\n{:.4f} mg/dl   =   {:.4f} mmol/l\n'.format(mg, mmol))
            break
        elif choice == '2':
            mmol = user_float()
            mg = convert_mmol_to_mg(mmol)
            print('\n{:.4f} mmol/l   =   {:.4f} mg/dl\n'.format(mmol, mg))

interactive_mode()
