if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    # Get the max out of the list
    max_i = max(arr)
    filter_arr = list(filter(lambda x: x != max_i, arr))
    print(max(filter_arr))



    




