'''
Python Lambda Functions are anonymous functions means that the function is without a name. As we already know the def keyword is used to define a normal function in Python. Similarly, the lambda keyword is used to define an anonymous function in Python. 
'''

str1 = 'GeeksforGeeks'

upper = lambda string: string.upper()
print(upper(str1))


format_numeric = lambda num: f"{num:e}" if isinstance(num, int) else f"{num:,.2f}"

print("Int formatting:", format_numeric(1000000))
print("float formatting:", format_numeric(999999.789541235))


def cube(y):
	return y*y*y

lambda_cube = lambda y: y*y*y
print("Using function defined with `def` keyword, cube:", cube(5))
print("Using lambda function, cube:", lambda_cube(5))


'''
With lambda function
    Supports single-line sometimes statements that return some value.
	Good for performing short operations/data manipulations.
	Using the lambda function can sometime reduce the readability of code.

Without lambda function
	Supports any number of lines inside a function block
	Good for any cases that require multiple lines of code.
	We can use comments and function descriptions for easy readability.

'''

is_even_list = [lambda arg=x: arg * 10 for x in range(1, 5)]
for item in is_even_list:
	print(item())


Max = lambda a, b : a if(a > b) else b
print(Max(1, 2))


List = [[4, 3, 1], [1, 4, 16, 64], [3, 6, 9, 12]]
# print('sorting')
# sort_list = [lambda x: (sorted(i) for i in List)]
# for i in sort_list:
# 	print(i)


sorts = map(lambda x : sorted(x), List)
print(list(sorts))

sortList = lambda x : (sorted(i) for i in x)
print(sortList)
secondLargest = lambda x, f : [y[len(y) - 2] for y in f(x)]
res = secondLargest(List, sortList)
print(res)

li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

final_list = list(filter(lambda x: (x % 2 != 0), li))
print(final_list)



ages = [13, 90, 17, 59, 21, 60, 5]
adults = list(filter(lambda age: age > 18, ages))

print(adults)



li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

final_list = list(map(lambda x: x*2, li))
print(final_list)


animals = ['dog', 'cat', 'parrot', 'rabbit']
uppered_animals = list(map(lambda animal: animal.upper(), animals))

print(uppered_animals)


from functools import reduce
li = [5, 8, 10, 20, 50, 100]
sum = reduce((lambda x, y: x + y), li)
print(sum)


import functools
lis = [1, 3, 5, 6, 2, ]
print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, lis))
