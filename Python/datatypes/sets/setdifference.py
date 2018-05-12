# https://www.hackerrank.com/challenges/py-set-difference-operation/problem

#pythonic code
_,a,_,b = [input().split() for i in "1234"]
print(len(set(a).difference(set(b))))