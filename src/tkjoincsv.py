
import tkFileDialog
import joincsv
import os.path

if __name__ == '__main__':
    filetypes=[("Spreadsheets", "*.csv"),
               ("Spreadsheets", "*.xls"),
               ("Spreadsheets", "*.xlsx")]
    
    input_filename = tkFileDialog.askopenfilename(filetypes=filetypes)
    
    if not os.path.isfile(input_filename):
        exit(0)
    
    output_filename = tkFileDialog.asksaveasfilename(filetypes=filetypes, defaultextension=".csv")
    if not os.path.isfile(output_filename):
        exit(0)
        
    joiner = joincsv.RecordJoiner(input_filename)
    joiner.save(output_filename)
    