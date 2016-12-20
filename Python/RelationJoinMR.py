import sys
from collections import OrderedDict


class MapReduce:
    def __init__(self):
        self.intermediate = OrderedDict()
        self.result = []

    def emitIntermediate(self, key, value):
        self.intermediate.setdefault(key, [])
        self.intermediate[key].append(value)

    def emit(self, value):
        self.result.append(value)

    def execute(self, data, mapper, reducer):
        for record in data:
            mapper(record)

        for key in self.intermediate:
            reducer(key, self.intermediate[key])

        self.result.sort()
        for item in self.result:
            print(item)


mapReducer = MapReduce()


def mapper(record):
    # Start writing the Map code here
    line = record.split(",")
    if line[0] == 'Department':
        mapReducer.emitIntermediate(line[1], (line[0], line[2]))
    if line[0] == 'Employee':
        mapReducer.emitIntermediate(line[2], (line[0], line[1]))


def reducer(key, list_of_values):
    # Start writing the Reduce code here
    depts = []
    names = []

    for value in list_of_values:
        if value[0] == 'Employee':
            names.append(value[1])
        else:
            depts.append(value[1])

    for name in names:
        for dept in depts:
            mapReducer.emit((key,name,dept))


if __name__ == '__main__':
    inputData = ["Department,1234,Sales","Employee,Susan,1234","Department,1233,Marketing","Employee,Joe,1233", "Department,1233,Accounts"]
    mapReducer.execute(inputData, mapper, reducer)
