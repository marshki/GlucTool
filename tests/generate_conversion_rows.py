#!/usr/bin/env python

"""Mock function to take converted values and output to row(s).
"""

from gluctool import convert_mg_to_mmol

def generate_conversion_rows(values, conversion_func, from_unit, to_unit):
    """
    Generate converted glucose values as rows.
    Returns a list of dicts suitable for CSV or STDOUT.
    """
    rows = []
    for value in values:
        rows.append({
            from_unit: round(value, 4),
            to_unit: round(conversion_func(value), 4),
        })
    return rows

if __name__ == "__main__":
    result_rows = generate_conversion_rows(
        [100, 125, 150, 175, 200],
        convert_mg_to_mmol,
        "mg/dl",
        "mmol/l"
    )

    print(result_rows)
