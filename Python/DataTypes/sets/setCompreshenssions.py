# create set

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_set1 = set()

for num in nums:
    my_set1.add(num)
print(my_set1)


# use compreshenssions to create the set

my_set2 = {num for num in nums}
print(my_set2)