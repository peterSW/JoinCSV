
import tkFileDialog
import joincsv

if __name__ == '__main__':
    filetypes=[("csv", "*.csv")]
    inputFile = tkFileDialog.askopenfile(filetypes=filetypes)
    outputFile = tkFileDialog.asksaveasfile(filetypes=filetypes, defaultextension=".csv")
    
    joiner = joincsv.CSVRecordJoiner(inputFile)
    joiner.save(outputFile)