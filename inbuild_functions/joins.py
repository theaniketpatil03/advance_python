'''
Python join() is an inbuilt string function used to join elements of a sequence separated by a string separator. This function joins elements of a sequence and makes it a string.
'''

str = '-'.join('hello')
print(str)  

list1 = ['g', 'e', 'e', 'k', 's']
print("".join(list1))

list1 = ('1', '2', '3', '4')

s = "-" 

new = s.join(list1)
print(new)

list1 = {'1', '2', '3', '4', '4'} 

# put any character to join
s = "-#-"

# joins elements of list1 by '-#-'
# and stores in string s
s = s.join(list1)

# join use to join a list of
# strings to a separator s
print(s)

dic = {'key1': 'val1', 'key2': 'val2', 'key3': 'val3'}
string_joins_only_key  = '_'.join(dic)
print(string_joins_only_key)


# also can use loop to iterate the values 
words = ["apple", "", "banana", "cherry", ""]
separator = "@ "
result = separator.join(val for val in words if val)
print(result)