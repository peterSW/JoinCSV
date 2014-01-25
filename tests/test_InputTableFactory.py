from corow import table_io

import unittest

class TestInputTableFactory(unittest.TestCase):

    def setUp(self):
        self.factory = table_io.InputTableFactory()

    def test_xlsx(self):
        input_table = self.factory.open_input_table("tests/input.xlsx")
        self.assertIsInstance(input_table, table_io.XlrdTable)
    def test_csv(self):
        input_table = self.factory.open_input_table("tests/input.csv")
        

class TestTypeLookup(unittest.TestCase):
    def setUp(self):
        self.f = table_io.InputTableFactory()
        
    def test_xlsx(self):
        self.assertIs(
              self.f.input_table_type_from("xlsx"), table_io.XlrdTable)
    
    def test_csv(self):
        self.assertIs(
              self.f.input_table_type_from("csv"), table_io.CSVTable)
        
    def test_invalid(self):
        self.assertRaises(ValueError,
                          self.f.input_table_type_from,
                          "aksdl")
    
    def test_get_extension(self):
        self.assertEqual("xlsx", table_io.get_extension("input.xlsx"))
    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
