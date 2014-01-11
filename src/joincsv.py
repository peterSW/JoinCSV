import csv
import jointable
import sys
from argparse import ArgumentParser

class FullHelpArgParser(ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: %s\n' % message)
        self.print_help()
        sys.exit(2)

if __name__ == '__main__':
    parser = FullHelpArgParser()
    parser.add_argument('input', help = "The input filename. It must be in .csv format. The first row is read as field headers. The First column is used as the value to join records on.")
    parser.add_argument('output', help = "The output filename. For example: output.csv")
    args = parser.parse_args()
    
    joint_table = None
    with open(args.input, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        
        joint_table = jointable.join_records_on_id(reader)
        
    with open(args.output, 'wb') as csvfile:
        writter = csv.writer(csvfile)
        for row in joint_table:
            writter.writerow(row)