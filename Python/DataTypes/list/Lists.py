'''Input : n  - number of usecases
example :
2
insert 1 10
print '''


n = int(input())
L = []
for iCommand in range(n):
    command = input().strip().split()
    args = [int(arg) for arg in command[1:]]
    if command[0] == 'print':
        print(L)
    else:
        getattr(L, command[0])(*args)
