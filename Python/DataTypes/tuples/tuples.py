'''
Use python's hash() to calculate the hash of a object
Usage :
example :
2
1 2
3713081631934410656
'''


if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    print(hash(tuple(integer_list)))
