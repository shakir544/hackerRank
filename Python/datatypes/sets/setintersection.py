# https://www.hackerrank.com/challenges/py-set-intersection-operation


# pythonic code
_,a,_,b = [input().split() for i in "1234"]
print(len(set(a).intersection(set(b))))