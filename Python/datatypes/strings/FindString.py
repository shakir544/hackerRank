# Find sub string from a give string


def count_substring(string, sub_string):
    result = 0
    index = string.find(sub_string)

    while index != -1:
        result += 1
        string = string[index+1:]
        index = string.find(sub_string)
    return result

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)