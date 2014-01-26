#!/usr/bin/env python2.7
"""
A command line interface for JoinCSV
"""

from corow import joincsv
import sys
from argparse import ArgumentParser


class FullHelpArgParser(ArgumentParser):
    """
    An ArgumentParser that outputs the full usage
    message if there is an error parsing the arguments.
    """

    def error(self, message):
        sys.stderr.write('error: %s\n' % message)
        self.print_help()
        sys.exit(2)

if __name__ == '__main__':
    parser = FullHelpArgParser()
    parser.add_argument(
        'input',
        help="The input filename. It must be in .csv format. "
             "The first row is read as field headers. "
             "The First column is used as the value to join records on.")
    parser.add_argument(
        'output',
        help="The output filename. For example: output.csv")

    args = parser.parse_args()

    joiner = joincsv.RecordJoiner(args.input)
    joiner.save(args.output)
