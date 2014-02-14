from corow import TableDifference
import unittest


class TestTableDifference(unittest.TestCase):
    

    def testOneExtraRecord(self):
        input1 = [['Header'],
                       ['1']]
        input2 = [['Header'],
                       ['2'],
                       ['1']]
        expected = [['Header'],
                         ['2']]
        
        difference = TableDifference(input1, input2)
        assert(expected == difference.result)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()