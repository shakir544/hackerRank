# https://www.hackerrank.com/challenges/py-set-union/problem

# Non pythonic way

def nonpythonic():
    a = int(input())
    seta = set(map(int, input().split()))
    b = int(input())
    setb = set(map(int, input().split()))
    print(len(seta.union(setb)))


# pythonic way
def pythonic1():
    _,a,_,b = [set(input().split()) for _ in '1234']
    print(len(a|b))

