#!/usr/bin/env python2.7
import tkFileDialog
from corow import joincsv
import os.path
import sys

if __name__ == '__main__':
    filetypes=[("Spreadsheets", "*.csv"),
               ("Spreadsheets", "*.xls"),
               ("Spreadsheets", "*.xlsx")]
    
    if len(sys.argv) == 2:
        input_filename = sys.argv[1]
    else:
        input_filename = tkFileDialog.askopenfilename(filetypes=filetypes)
    
    if not os.path.isfile(input_filename):
        exit(0)
    
    output_filename = tkFileDialog.asksaveasfilename(filetypes=filetypes, defaultextension=".csv")
    
    if output_filename:
        joiner = joincsv.RecordJoiner(input_filename)
        joiner.save(output_filename)

