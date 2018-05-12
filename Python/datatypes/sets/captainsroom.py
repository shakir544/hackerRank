# https://www.hackerrank.com/challenges/py-the-captains-room/problem
N = int(input())
rooms = list(map(int,input().split()))
dict = {}

for room in rooms:
    if room not in dict:
        dict[room] = 1
    else:
        dict[room] +=1

for key in dict.keys():
    if dict[key] == 1:
        print(key)
        break