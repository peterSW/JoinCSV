
def join_records_on_id(inputTable):
    rowIt = iter(inputTable)
    inputHeader = rowIt.next()

    joiner = RecordJoiner(rowIt)
    
    result = [make_header(inputHeader, joiner.count())]
    result.extend(joiner.result())
    return result
    
def make_header(header, numRepeat):
    keyFieldName = header[0]
    result = [keyFieldName]
    otherFields = header[1:]
    for i in range(numRepeat):
        for field in otherFields:
            result.append(append_index(field, i+1))
    return result

def append_index(fieldName, index):
    return ' '.join((fieldName, str(index)))

class RecordJoiner():
    def __init__(self, records):
        self.records_by_id = {}
        self.ordered_keys = []
        
        self.parseRecords(records)
        
    def parseRecords(self, records):
        for record in records:
            key = record[0]
            if key not in self.records_by_id:
                self.records_by_id[key] = []
                self.ordered_keys.append(key)
            self.records_by_id[key].append(record[1:])
        
    def result(self):
        results = [self.processKey(key) for key in self.ordered_keys]
        
        return results
    
            
    def processKey(self, key):
        result = [key]
        for subRecord in self.records_by_id[key]:
            result.extend(subRecord)
        return result
    
    def count(self):
        return max([self.numRecordsForKey(key) for key in self.ordered_keys])

    def numRecordsForKey(self, key):
        return len(self.records_by_id[key])
    
    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()