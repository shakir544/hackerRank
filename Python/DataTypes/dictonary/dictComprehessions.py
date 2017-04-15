# Dictonary comprehessions

names = ['Shah Ruk Khan', 'Salman khan', 'amir khan', 'Hrithik roshan', 'ranbir kapoor']
movies = ['raaes', 'bajarangi bhaijan', 'daanal', 'kaabil', 'aae dil hai mushkhil']

my_dict1 = { }
for name,movie in zip(names,movies) :
    my_dict1[name] =movie
print(my_dict1)



# create a dict using comprehessions
my_dict2 = {name:movie for name,movie in zip(names,movies)}
print(my_dict2)