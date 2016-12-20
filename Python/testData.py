from faker import Factory

def generate_mocked_data(fake):
    for _ in range(1):
        write_mocked_data_to_file(fake.name() +"," + fake.city() +"," +country())


def write_mocked_data_to_file(data):
    outputFile = "/Users/shakirgooty/work/programming/python/mockDataCreator/data.csv"
    with open(outputFile,'w') as f :
        f.write(data)


def retrive_data_from_file() :
    inputFile = "/Users/shakirgooty/work/programming/python/mockDataCreator/data.csv"
    with open(inputFile,'r') as f:
        print (f.read())


if __name__ == "__main__":
    fake = Factory.create()
    generate_mocked_data(fake)
    retrive_data_from_file()

