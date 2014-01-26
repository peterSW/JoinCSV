import xlrd


def get_extension(filename):
    return filename.split(".")[-1]


def CSVTable(filename):
    import csv
    inputFile = open(filename, 'rb')
    return csv.reader(inputFile)


class XlrdTable(object):
    """
    A wrapper around a xlrd.Sheet object.
    Provides the needed interface for use with
    jointable.
    """

    def __init__(self, filename):
        first_sheet = xlrd.open_workbook(filename).sheet_by_index(0)

        self.xlrd_sheet = first_sheet

    def __iter__(self):
        return iter(
            [self.xlrd_sheet.row_values(row)
             for row in range(self.xlrd_sheet.nrows)])


class InputTableFactory(object):
    input_table_map = {"xlsx": XlrdTable,
                       "xls": XlrdTable,
                       "csv": CSVTable}

    def input_table_type_from(self, extension):
        if extension in self.input_table_map:
            return self.input_table_map[extension]
        else:
            raise ValueError()

    def open_input_table(self, filename):
        ext = get_extension(filename)
        TableType = self.input_table_type_from(ext)
        return TableType(filename)


class CSVWriter(object):
    def __init__(self, filename):
        self.filename = filename

    def save(self, table):
        import csv
        with open(self.filename, 'wb') as csvfile:
            writer = csv.writer(csvfile)
            for row in table:
                writer.writerow(row)


class XlwtWriter(object):
    def __init__(self, filename):
        self.filename = filename

    def save(self, table):
        import xlwt
        wb = xlwt.Workbook()
        ws = wb.add_sheet("Sheet1")

        for j in range(len(table)):
            xlrow = ws.row(j)
            data_row = table[j]
            for i in range(len(data_row)):
                xlrow.write(i, data_row[i])

        wb.save(self.filename)

writer_ext_map = {"xlsx": XlwtWriter,
                  "xls": XlwtWriter,
                  "csv": CSVWriter}


def get_writer(filename):
    WriterType = writer_ext_map[get_extension(filename)]
    return WriterType(filename)
