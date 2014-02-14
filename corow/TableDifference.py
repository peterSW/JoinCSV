

class TableDifference(object):
    
    
    def __init__(self, input1, input2):
        it_2 = iter(input2)
        self.result = [it_2.next()]
        for record_from_2 in it_2:
            it_1 = iter(input1)
            it_1.next()
            present_in_1 = False
            for record_from_1 in it_1:
                if record_from_1 == record_from_2:
                    present_in_1 = True
            
            if not present_in_1:
                self.result.append(record_from_2)