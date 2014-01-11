
from jointable import *
import unittest


class TestMakeHeader(unittest.TestCase):
    def setUp(self):
        self.input = ['ID', 'Start'   , 'End'     , 'Description']
        self.expected2 = ['ID', 'Start 1', 'End 1'    , 'Description 1', 'Start 2' , 'End 2'   , 'Description 2']

    def testMakeHeader2(self):
        self.assertEqual(self.expected2, make_header(self.input, 2))
    
    def testAppendIndex(self):
        self.assertEqual('Field 1', append_index('Field', 1))

class TestRecordJoiner(unittest.TestCase):
    def setUp(self):
        self.input = [['1' , '01/12/12', '01/12/13', 'N/A'],
                      ['1' , '01/12/13', '01/12/14', 'Lots']]

        self.expected = [['1',  '01/12/12', '01/12/13', 'N/A'          , '01/12/13', '01/12/14', 'Lots']]
        
        self.joiner = RecordJoiner(self.input)
        
    def testJoin(self):
        self.assertEqual(self.expected, self.joiner.result())
    def testCount(self):
        self.assertEqual(2, self.joiner.count())

class TestJoinRows(unittest.TestCase):
    def setUp(self):
        self.input = [['ID', 'Start'   , 'End'     , 'Description'],
                      ['1' , '01/12/12', '01/12/13', 'N/A'],
                      ['1' , '01/12/13', '01/12/14', 'Lots']]

        self.expected = [['ID', 'Start 1', 'End 1'    , 'Description 1', 'Start 2' , 'End 2'   , 'Description 2'],
                         ['1',  '01/12/12', '01/12/13', 'N/A'          , '01/12/13', '01/12/14', 'Lots']]

    def testJoinRows(self):
        self.assertEqual(self.expected, join_records_on_id(self.input))




if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()