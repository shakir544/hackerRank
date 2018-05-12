# textwrap example

import textwrap

def wrap(string,width):
    return textwrap.fill(string,width)


if __name__ == '__main__' :
    string = input().strip()
    width = int(input().strip())

    result = wrap(string,width)

    print(result)