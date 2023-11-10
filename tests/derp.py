#!/usr/bin/env python3

import argparse
import sys
import unittest

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', required=True)
    args = parser.parse_args()
    print(f'Hello {args.name}')

if __name__ == '__main__':
    sys.exit(main())

from main import main

def test(capsys):
    main(["--name", "Moish"])
    captured = capsys.readouterr()
    assert captured.out == "Hello Moish\n"


