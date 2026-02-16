GlucTool :drop_of_blood: :toolbox:
========================================================================================
|travis| |codacy| |maintained| |python| |mit| |open source|

.. |travis| image:: https://app.travis-ci.com/marshki/GlucTool.svg?branch=master
    :target: https://app.travis-ci.com/marshki/GlucTool
    :alt: Travis

.. |codacy| image:: https://api.codacy.com/project/badge/Grade/717665e06c8e41c7b4184ad40682aed4
   :target: https://www.codacy.com/app/marshki/GlucTool?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=marshki/GlucTool&amp;utm_campaign=Badge_Grade
   :alt: Codacy

.. |maintained| image:: https://img.shields.io/badge/Maintained%3F-yes-green.svg
   :target: https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity
   :alt: Maintained

.. |python| image:: https://img.shields.io/badge/Made%20with-Python-1f425f.svg
   :target: https://www.python.org/
   :alt: Python

.. |mit| image:: https://img.shields.io/badge/License-MIT-blue.svg
   :target: https://opensource.org/license/MIT   
   :alt: MIT

.. |open source| image:: https://badges.frapsoft.com/os/v3/open-source.svg?v=103
   :target: https://github.com/ellerbrock/open-source-badges/
   :alt: Open Source

A blood sugar conversion tool
-----------------------------
Python 3 utility for converting plasma glucose ("blood sugar") units_ using argument parsing.

.. _units: https://en.wikipedia.org/wiki/Blood_sugar#Units

Convert:

* milligram per decileter to millimole per liter (mg/dl to mmol/l)
* millimole per liter to milligram per decileter (mmol/l to mg/dl)

Output: 

* a table of the conversion, e.g:
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
* a csv of the conversion, e.g.:

    mg/dl,mmol/l
    70.0,3.885
    71.0,3.9405
    72.0,3.996
    73.0,4.0515
    74.0,4.107

Requirements
------------
None.

Usage
-----
Synopsis:

.. code-block:: Python3
   
    [-h] [--mg-to-mmol MG_TO_MMOL [MG_TO_MMOL ...] | --mmol-to-mg MMOL_TO_MG [MMOL_TO_MG ...]]

Examples
--------
Single conversion:

.. code-block:: Python3

    python3 gluctool.py --mmol-to-mg 4.0515

Multiple conversions:

(spaced arguments)

.. code-block:: Python3

    python3 gluctool.py --mg-to-mmol 7.5 8.5 9.5 10 

(brace expanson)

.. code-block:: Python3

    python3 gluctool.py --mg-to-mmol 7{0..9}

TODOs
-----
   + Offer argument that integrates csv_ module to allow input or export of values.
     Issue #4 in Github (branch: feature/add_csv)

.. _argparser: https://docs.python.org/3/library/argparse.html
.. _csv: https://docs.python.org/3/library/csv.html

Change Log
----------
CHANGELOG_

.. _CHANGELOG: https://github.com/marshki/blood_glucose_conversion/blob/master/CHANGELOG.rst

License
-------
LICENSE_

.. _LICENSE: https://github.com/marshki/blood_glucose_conversion/blob/master/LICENSE.txt
