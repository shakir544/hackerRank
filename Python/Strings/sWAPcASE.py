''' You are given a string . Your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.'''

import string

name = "Hello World, I Love Python "

'''Method - 1 Using SwapCase Method'''
result = name.swapcase()
print(result)

'''Method -2 : Using inline for loop '''

result = "".join(c.lower() if c.isupper() else c.upper() for c in name)
print(result)

