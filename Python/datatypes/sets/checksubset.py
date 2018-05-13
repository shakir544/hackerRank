# https://www.hackerrank.com/challenges/py-check-subset/problem

# method 1
testcases=int(input())
for testcase in range(testcases):
    a,seta = int(input()),set(list(map(int,input().split())))
    b,setb = int(input()),set(list(map(int,input().split())))
    print(seta.issubset(setb))


# Pythonic code
for _ in range(int(input())):
    a,seta,b,setb = input(),set(input().split()),input(),set(input().split())
    print(seta.issubset(setb))
