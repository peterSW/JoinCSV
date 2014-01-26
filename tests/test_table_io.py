
from corow import jointable
from corow import table_io
import unittest


class Test(unittest.TestCase):

    def getFirstSheet(self):
        f = table_io.InputTableFactory()
        return f.open_input_table("tests/input.xlsx")

    def test_row_iteration(self):
        iter(self.getFirstSheet())

    def test_with_jointable(self):
        self.joint_table = jointable.join_records_on_id(self.getFirstSheet())


class TestCSV(Test):
    def getFirstSheet(self):
        f = table_io.InputTableFactory()
        return f.open_input_table("tests/input.csv")


class TestXlwt(unittest.TestCase):
    def test_xlwt(self):
        data = [["ID", "Desc"], [1, "Hmm"]]
        writer = table_io.get_writer("tests/output.xlsx")
        writer.save(data)
