#!/usr/bin/python

#
# Check a challenge entry
#

import sys
import os
import argparse

THIS = os.path.basename(sys.argv[0])
DEFAULT_INPUT = "hex-entry"

# Main
def main():
    arg_parser = argparse.ArgumentParser(prog=THIS)
    arg_parser.add_argument("-f", "--file", default=DEFAULT_INPUT,
                            help="specify the input file (default: %(default)s)", metavar="file")
    args = arg_parser.parse_args()

    # Open input file

    input_path = os.path.abspath(args.file)
    if not os.path.exists(input_path):
        print("%s: Error: File '%s' not found" % (THIS, args.file))
        return 1

    input = open(input_path, "r")
    if input is None:
        print("%s: Error: Couldn't open file '%s'" % (THIS, input_path))
        return 1

    try:
        grid = eval(input.readline().strip())
    except Exception as e:
        print(THIS + ": Error: Malformed input")
        return 1

    # Main loop

    order = len(grid[0])

    return 0


if __name__ == "__main__":
    sys.exit(main())
