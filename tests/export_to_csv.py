#!/usr/local/bin/env python

"""
Open 'scratch.csv' and write:
a header
a new row with the content of one (1) rown from 'rows'
"""

import csv

rows = [
    {"mg/dl": 100.0, "mmol/l": 5.5499},
    {"mg/dl": 110.0, "mmol/l": 6.1049},
    {"mg/dl": 120.0, "mmol/l": 6.6599},
    {"mg/dl": 130.0, "mmol/l": 7.2149},
    {"mg/dl": 140.0, "mmol/l": 7.7699},
    {"mg/dl": 150.0, "mmol/l": 8.3249},
    {"mg/dl": 160.0, "mmol/l": 8.8799},
    {"mg/dl": 170.0, "mmol/l": 9.4349},
    {"mg/dl": 180.0, "mmol/l": 9.9899},
    {"mg/dl": 190.0, "mmol/l": 10.5449},
    {"mg/dl": 200.0, "mmol/l": 11.0999},
]

with open("scratch.csv", "w", newline="") as fh:
    writer = csv.DictWriter(fh, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)
