#https://www.hackerrank.com/challenges/no-idea/problem

a, b = map(int,input().split())
arr = list(map(int,input().split()))

seta = set(map(int,input().split()))
setb = set(map(int,input().split()))

happiness = 0
for val in arr:
    if val in seta:
        happiness +=1
    if val in setb:
        happiness -=1

print(happiness)