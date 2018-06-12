========
GlucTool
========
.. image:: https://api.codacy.com/project/badge/Grade/717665e06c8e41c7b4184ad40682aed4
   :target: https://www.codacy.com/app/marshki/GlucTool?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=marshki/GlucTool&amp;utm_campaign=Badge_Grade

.. image:: https://img.shields.io/badge/Made%20with-Python-1f425f.svg
   :target: https://www.python.org/

.. image:: https://requires.io/github/marshki/GlucTool/requirements.svg?branch=master
   :target: https://requires.io/github/marshki/GlucTool/requirements/?branch=master
   :alt: Requirements Status

.. image:: https://img.shields.io/badge/License-MIT-blue.svg
   :target: https://lbesson.mit-license.org/

A blood sugar conversion tool
-----------------------------
Python3 utility for converting plasma glucose ("blood sugar") units_ using argument parsing, or a text-based menu.

.. _units: https://en.wikipedia.org/wiki/Blood_sugar#Units

In either mode, you can convert:

* milligram per decileter to millimole per liter (mg/dl to mmol/l), or
* millimole per liter to milligram per decileter (mmol/l to mg/dl),

and receive a table of the conversion, e.g:

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
	python3 gluctool.py --mmol-to-mg 4.0515

Multiple conversions:
::
	python3 gluctool.py --mg-to-mmol 7{0..9}

Menu-driven program:
::
	python3 gluctool.py

TODO
----
* Unit testing
* Integrate TravisCI

Change Log
----------
CHANGELOG_

.. _CHANGELOG: https://github.com/marshki/blood_glucose_conversion/blob/master/CHANGELOG.rst

License
-------
LICENSE_

.. _LICENSE: https://github.com/marshki/blood_glucose_conversion/blob/master/LICENSE.txt
