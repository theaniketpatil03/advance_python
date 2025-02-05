# Creation: 
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

# Accessing Values: 
print(my_dict['name']) # Output: John

# Adding/Updating Values: 
my_dict['occupation'] = 'Developer'

# Removing Key-Value Pair: 
del my_dict['age']


#  looping with only key
for key in my_dict:
    print(key)
    
# looping with index and item
for index, key in enumerate(my_dict):
    print(f"{index}: {key}")

# extract only keys in dict 
print(my_dict.keys())
print(list(my_dict.keys()))
