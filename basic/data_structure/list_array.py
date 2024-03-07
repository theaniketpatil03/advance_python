#Creation: 
my_list = [1, 2, 3, 'four', 5.0]

# Length : length start from 1 but indexing start from 0
print(len(my_list))
# Accessing Elements: 

print(my_list[0]) # Output: 1

# Slicing: it wil incloude first index specified (1) and but it will exclude last specified index (4)
print(my_list[1:4]) # Output: [2, 3, 'four']

# Appending: 
my_list.append(6)

# Inserting: 
my_list.insert(2, 'new_element')

# Removing: - it will remove any element which you will specify in paranthesis 
my_list.remove('four')

# Pop: - it will pop/remove single element from end
print(my_list)
popped_element = my_list.pop()
print(my_list)

# Creation array
import array

my_array_int = array.array('i', [1, 2, 3, 4])
my_array_int.append(5)
my_array_int.append('j')
print(my_array_int)

# other types
'''
'i': Signed integer (e.g., 1, 2, 3, ...)
'f': Floating-point (e.g., 1.0, 2.5, ...)
'd': Double-precision floating-point - array.array('d', [1.234, 2.567, -3.789, 4.012])
'b': Signed byte - array.array('b', [-1, 0, 1, 2, -3])
'c': Character - array.array('c', ['a', 'b', 'c', 'd'])
'u': unicode character - array.array('u', ['John', 'Doe', 'Alice'])
'''

# **** array of dictonary is not defined os instead use list of dictonary

# eg
my_array = array.array('i', [1, 2, 3, 4])

# Accessing Elements: 
print(my_array[2]) # Output: 3

# Updating Elements: 
my_array[1] = 10


'''
Use Lists:

    When you need a dynamic, versatile data structure with a variety of built-in methods.
    When dealing with different data types within the same collection.
    
Use Arrays:

    When working with large datasets and numerical operations.
    When performance is critical, and you want to leverage lower-level memory operations.
    When you need a fixed-size collection and want to explicitly define the data type.

'''