
import jointable
import table_io

class RecordJoiner():
    def __init__(self, filename):
        self.load(filename)
    
    def load(self, filename):
        f = table_io.InputTableFactory()
        input_table = f.open_input_table(filename)
        self.joint_table = jointable.join_records_on_id(input_table)
        
    def save(self, filename):
        writer = table_io.get_writer(filename)
        writer.save(self.joint_table)
        
        

