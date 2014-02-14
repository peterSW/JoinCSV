#!/usr/bin/env python2.7
import tkFileDialog
from corow import TableDifference
from corow import table_io
import os.path
import sys


filetypes = [("Spreadsheets", "*.csv"),
             ("Spreadsheets", "*.xls"),
             ("Spreadsheets", "*.xlsx")]

def checked_openfilename():
    filename = tkFileDialog.askopenfilename(
            filetypes=filetypes)

    if not os.path.isfile(filename):
        exit(0)
    return filename

if __name__ == '__main__':

    input1FN = checked_openfilename()
    input2FN = checked_openfilename()

    outputFN = tkFileDialog.asksaveasfilename(
        filetypes=filetypes,
        defaultextension=".csv")

    if outputFN:
        opener = table_io.InputTableFactory()
        input1 = opener.open_input_table(input1FN)
        input2 = opener.open_input_table(input2FN)
        difference = TableDifference(input1, input2)
        
        writer = table_io.get_writer(outputFN)
        print difference.result
        writer.save(difference.result)
