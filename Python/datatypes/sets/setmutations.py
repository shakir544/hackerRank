#https://www.hackerrank.com/challenges/py-set-mutations/problem

a = int(input())
seta = set(list(map(int,input().split()))[:a])
N = int(input())
for _ in range(N):
    eval("seta.{0}({1})".format(input().split()[0],set(list(map(int,input().split())))))
print(sum(seta))
