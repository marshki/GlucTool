========
GlucTool
========
.. image:: https://landscape.io/github/marshki/blood_glucose_conversion/master/landscape.svg?style=flat
   :target: https://landscape.io/github/marshki/blood_glucose_conversion/master
   :alt: Code Health

.. image:: https://requires.io/github/marshki/blood_glucose_conversion/requirements.svg?branch=master
   :target: https://requires.io/github/marshki/blood_glucose_conversion/requirements/?branch=master
   :alt: Requirements Status

A blood sugar conversion tool 
-----------------------------
Python3 utility for converting plasma glucose ("blood sugar") units_ using argument parsing, or a text-based menu.

.. _units: https://en.wikipedia.org/wiki/Blood_sugar#Units

In either mode, you can convert: 

* milligram per decileter to millimole per liter (mg/dl to mmol/l), or 
* millimole per liter to milligram per decileter (mmol/l to mg/dl).

and a receive a table of the conversion, e.g: 

+------------+------------+
|   mg/dl    |   mmol/l   |
+============+============+
|    70.0000 |     3.8850 |
+------------+------------+
|    71.0000 |     3.9405 |
+------------+------------+
|    72.0000 |     3.9960 |
+------------+------------+
|    73.0000 |     4.0515 |
+------------+------------+
|    74.0000 |     4.1070 |
+------------+------------+

Requirements
------------
Install argparse with:  
:: 
	pip3 install argparse
 
Usage
-----
Synopsis: 
::
	[-h] [--mg-to-mmol MG_TO_MMOL [MG_TO_MMOL ...] | --mmol-to-mg MMOL_TO_MG [MMOL_TO_MG ...]]

Examples
--------
Single conversion: 
::
	python3 gluc_tool_2.0.py --mmol-to-mg 13.45

Multiple conversions: 
::
	python3 gluc_tool_2.0.py --mg-to-mmol {0..10}    

Menu-driven program: 
::
	python3 gluc_tool_2.0.py 
 
Change Log  
----------
CHANGELOG_

.. _CHANGELOG: https://github.com/marshki/blood_glucose_conversion/blob/master/CHANGELOG.rst

License
-------
LICENSE_

.. _LICENSE: https://github.com/marshki/blood_glucose_conversion/blob/master/LICENSE
