
def join_records_on_id(input_table):
    row_it = iter(input_table)
    input_header = row_it.next()

    joiner = RecordJoiner(row_it)

    result = [make_header(input_header, joiner.count())]
    result.extend(joiner.result())
    return result


def make_header(input_header, num_repeat):
    key_field_name = input_header[0]
    result = [key_field_name]
    other_fields = input_header[1:]
    for i in range(num_repeat):
        for field in other_fields:
            result.append(append_index(field, i+1))
    return result


def append_index(field_name, index):
    return ' '.join((field_name, str(index)))


class RecordJoiner():
    def __init__(self, records):
        self.records_by_id = {}
        self.ordered_keys = []

        self.parse_records(records)

    def parse_records(self, records):
        for record in records:
            key = record[0]
            if key not in self.records_by_id:
                self.records_by_id[key] = []
                self.ordered_keys.append(key)
            self.records_by_id[key].append(record[1:])

    def result(self):
        results = [self.process_key(key) for key in self.ordered_keys]

        return results

    def process_key(self, key):
        result = [key]
        for sub_record in self.records_by_id[key]:
            result.extend(sub_record)
        return result

    def count(self):
        return max([self.num_records_for_key(key) for
                    key in self.ordered_keys])

    def num_records_for_key(self, key):
        return len(self.records_by_id[key])
