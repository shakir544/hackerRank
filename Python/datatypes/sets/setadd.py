# https://www.hackerrank.com/challenges/py-set-add/problem

N = int(input())
countries = set()

for country in range(N):
    countries.add(input())

print(len(countries))