'''
Tuples VS Lists:
Similarities	Differences
Functions that can be used for both lists and tuples:

len(), max(), min(), sum(), any(), all(), sorted()

Methods that cannot be used for tuples:

append(), insert(), remove(), pop(), clear(), sort(), reverse()

Methods that can be used for both lists and tuples:

count(), Index()

we generally use ‘tuples’ for heterogeneous (different) data types and ‘lists’ for homogeneous (similar) data types.
Tuples can be stored in lists.	Iterating through a ‘tuple’ is faster than in a ‘list’.
Lists can be stored in tuples.	‘Lists’ are mutable whereas ‘tuples’ are immutable.
Both ‘tuples’ and ‘lists’ can be nested.	Tuples that contain immutable elements can be used as a key for a dictionary.

'''

# Slicing of a Tuple

# Slicing of a Tuple
# with Numbers
Tuple1 = tuple('GEEKSFORGEEKS')

# Removing First element
print("Removal of First Element: ")
print(Tuple1[1:])

# Reversing the Tuple
print("\nTuple after sequence of Element is reversed: ")
print(Tuple1[::-1])

# Printing elements of a Range
print("\nPrinting elements between Range 4-9: ")
print(Tuple1[4:9])


