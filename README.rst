========
GlucTool
========
A blood sugar conversion tool 
-----------------------------
Python3 utility for converting plasma glucose ("blood sugar") units_ using argument parsing, or a text-based menu.
 
.. _units: https://en.wikipedia.org/wiki/Blood_sugar#Units

.. image:: https://landscape.io/github/marshki/blood_glucose_conversion/master/landscape.svg?style=flat
   :target: https://landscape.io/github/marshki/blood_glucose_conversion/master
   :alt: Code Health

.. image:: https://requires.io/github/marshki/blood_glucose_conversion/requirements.svg?branch=master
   :target: https://requires.io/github/marshki/blood_glucose_conversion/requirements/?branch=master
   :alt: Requirements Status

Requirements
~~~~~~~~~~~~
.. code-block:: 
	
	pip3 install argparse


 
## Usage

This program accepts command-line arguments, and may also be run via a text-based menu. 
In either mode, this program converts plasma glucose levels from: 

* milligram per decileter to millimole per liter (mg/dl to mmol/l),	

* millimole per liter to milligram per decileter (mmol/l to mg/dl). 

To run this program with command line arguments: 

make the program executable with: `chmod 744 gluc_tool_2.0.py`, 
then consult the tool's help menu with: `./gluc_tool_2.0.py --help`.

Here's an  example: `./gluc_tool_2.0.py --mg-to-mmol {0..100}`, which will convert the numbers between 0.0 and 100.0 MG to MMOL.    

You can also run the menu-driven program with: 

`python3 gluc_tool_2.0`. 

 
__This program is for informational purposes and should not be used as a substitute for qualified medical counsel.__

Screenshots: 

![Alt text](https://github.com/marshki/blood_glucose_conversion/blob/master/arg_parse.png "arg_parse_help")

![Alt text](https://github.com/marshki/blood_glucose_conversion/blob/master/gluc_convert.png?raw+true "gluc_tool")

##TODO: 

- [x] Add argument parsing for the CLI via `argparse.
- [x] Format output to table.
- [ ] Unit tests! 
- [ ] Integrate `travis-ci` 
- [x] `landscape.io` 
 
## History 

First commit Apr. 22, 2016 @17:33 ET.

Version 2.0 July 31, 2016. 

