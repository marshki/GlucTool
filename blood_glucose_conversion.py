#!/bin/py
#Python 3.4.3
"""
This is a menu-driven program which converts plasma glucose levels from: 
	* milligram per declieter to millimole per liter (mg/dl to mmol/l) 
	* millimole per liter to milligram per decileter (mmol/l to mg/dl)
"""

#Define menu function 
def menu():
	"""
	This funtion prints menu options and prompts user input 
	""" 
	print()
	print('What would you like to do?')
	print()
	print('1. I want to convert a plasma glucose level from mg/dl to mmol/l.')
	print()
	print('2. I want to convert a plasma glucose level from mmol/l to mg/dl.')
	print()
	print('3. I want to quit.')
	print()
	return input('Type the option (1,2,3) you want to perform, then press Enter: ')
()

#Define functions
def convert_mg_to_mmol():
	"""
	This function converts plasma to glucose levels from mg/dl to mmol/l
	Formula for conversion: 
	mg/dl * 0.0555 = mmol/l
	"""
	try: 
		print()
		mg_dl = float(input('Enter the plasma glucose level in mg/dl, then press Enter: '))
		print()
		print('*** A plasma glucose level of:',mg_dl,'mg/dl converts to:',mg_dl*0.0555,'mmol/l. ***')
	
	except ValueError:
		print('*** Sorry, that\'s not a valid input. Try again. ***')
()

def convert_mmol_to_mg():
	"""
	This function converts plasma to glucose levels from mmol/l to mg/dl 
	Formula for conversion: 
	mmol/l * 18.0182 = mg/dl
	"""
	try: 
		print()
		mmol=float(input('Enter the plasma glucose level in mmol/l, then press Enter: '))
		print('')
		print('*** A plasma glucose level of:',mmol,'mmo/l converts to:',mmol*18.0182,'mg/dl. ***')

	except ValueError:
		print('*** Sorry, that\'s not a valid input. Try again. ***')
()

#Program 
loop = 1 
choice = 0
while loop == 1: 
	choice = menu()
	if choice == '1':
		convert_mg_to_mmol()
	elif choice == '2': 
		convert_mmol_to_mg()
	elif choice == '3': 
		loop = 0  
	else: 
		print()
		print('*** Sorry, you must select a valid option (1,2,3), then press Enter. Try again. ***')
	
