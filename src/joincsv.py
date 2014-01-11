import csv
import jointable

class CSVRecordJoiner():
    def __init__(self, csvfile):
        self.load(csvfile)
    
    def load(self, csvfile):
        reader = csv.reader(csvfile)
        self.joint_table = jointable.join_records_on_id(reader)
    
    def save(self, csvfile):
            writter = csv.writer(csvfile)
            for row in self.joint_table:
                writter.writerow(row)

