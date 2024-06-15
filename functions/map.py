'''
map function returns iterator of map object of result after applying the give function to each item of a give iterable(list, tuple)
syntax - map(fun, iter)
'''



def addition(n):
    return n + n

numbers = (1, 2, 3, 4)

print(addition(numbers))

map_result = map(addition, numbers)
print(list(map_result))


# with lambda
result = map(lambda x: x + x , numbers)
print(list(result))


# Add two lists using map and lambda

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

result = map(lambda x, y: [x + y, x - y], numbers1, numbers2)
print(list(result))

# List of strings
l = ['sat', 'bat', 'cat', 'mat']

# map() can listify the list of strings individually
test = list(map(list, l))
print(test)

# Define a function that doubles even numbers and leaves odd numbers as is
def double_even(num):
	if num % 2 == 0:
		return num * 2
	else:
		return num

# Create a list of numbers to apply the function to
numbers = [1, 2, 3, 4, 5]

# Use map to apply the function to each element in the list
result = list(map(double_even, numbers))

# Print the result
print(result) # [1, 4, 3, 8, 5]

