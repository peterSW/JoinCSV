
import unittest
import joincsv
import os

class TestJoinCSV(unittest.TestCase):

    def setUp(self):
        self.inputFN = "input.csv"
        self.outputFN = "output.csv"
        self.expectedOutputFN = "expected_output.csv"

    def testJoinCSV(self):
        with open(self.inputFN, 'rb') as inputFile:
            joiner = joincsv.CSVRecordJoiner(inputFile)
        with open(self.outputFN, 'wb') as outputFile:
            joiner.save(outputFile)
        
        with open(self.expectedOutputFN , 'rb') as expectedFile:
            with open(self.outputFN, 'rb') as actualFile:
                for expectedLine, actualLine in zip(expectedFile, actualFile):
                    if expectedLine != actualLine:
                        self.fail("Expected: " + expectedLine + "  Actual: " + actualLine)

        os.remove(self.outputFN)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()