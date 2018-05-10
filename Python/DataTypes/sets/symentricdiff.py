# https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem

_,a,_,b = [input().split() for i in "1234"]
print(len(set(a).symmetric_difference(set(b))))