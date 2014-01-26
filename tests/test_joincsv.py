
import unittest
from corow import joincsv
import os


class TestJoinCSV(unittest.TestCase):

    def assert_files_match(self, fn_of_expected, fn_of_actual):
        with open(fn_of_expected, 'rb') as expectedFile, \
                open(fn_of_actual, 'rb') as actualFile:
            for expectedLine, actualLine in zip(expectedFile, actualFile):
                if expectedLine != actualLine:
                    self.fail("Expected: " + expectedLine +
                              "  Actual: " + actualLine)

    def setUp(self):
        self.inputFN = "tests/input.csv"
        self.outputFN = "tests/output.csv"
        self.expectedOutputFN = "tests/expected_output.csv"

    def testJoinCSV(self):
        joiner = joincsv.RecordJoiner(self.inputFN)
        joiner.save(self.outputFN)

        self.assert_files_match(self.expectedOutputFN, self.outputFN)

        os.remove(self.outputFN)


@unittest.skip("Result comparison not working")
class TestJoinXLSX(TestJoinCSV):
    def setUp(self):
        self.inputFN = "tests/input.xlsx"
        self.outputFN = "tests/output.xlsx"
        self.expectedOutputFN = "tests/expected_output.xlsx"
