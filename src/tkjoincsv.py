
import tkFileDialog
import joincsv

if __name__ == '__main__':
    filetypes=[("csv", "*.csv")]
    inputFile = tkFileDialog.askopenfile(mode='rb', filetypes=filetypes)
    outputFile = tkFileDialog.asksaveasfile(mode='wb', filetypes=filetypes, defaultextension=".csv")
    
    joiner = joincsv.CSVRecordJoiner(inputFile)
    joiner.save(outputFile)