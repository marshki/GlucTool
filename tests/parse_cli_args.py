#!/usr/bin/env python3

"""Unit testing class.
"""

import argparse

def parse_cli_args():
    """Define parser w/arguments.
    """

    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--mg-to-mmol", help="mg/dl to mmol/l", nargs='+', type=float)
    group.add_argument("--mmol-to-mg", help="mmol/l to mg/dl", nargs='+', type=float)
    args = parser.parse_args()
    return args
