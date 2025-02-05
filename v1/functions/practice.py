# clousure - means it can access the variable of outuer function in inner function


def outer():
    x = 1

    def inner():
        return x

    return inner


clousure = outer()
print(clousure())



# lambda

x = lambda : print('hello')
x()

li = [lambda arg=x : arg**2 for x in range(5)]
for item in li:

    print(item())


# map

def square(x):
    return x**2

nums = [1, 3, 5, 7]

data = map(square, nums)
print(list(data))


data2 = map( lambda arg  : arg**2 , nums)
print(list(data2))


number1 = [1, 2, 3, 4]
number2 = [4, 3, 2, 1]

data3 = map(lambda x, y : [x+y, x-y], number1, number2)
print(list(data3))


# Filter - only returs if value
values = [0, 1, 'aniket', '']
filts = filter(lambda x: x, values)

print(list(filts))


def fun(val):
    if isinstance(val, int):
        return val

int_filtl = filter(fun, values)
print(list(int_filtl))

# reduce - it applies function and reduce to single value

lis = [1, 2, 3, 4]

fu = lambda x , y : x + y

from functools import reduce
red = reduce(fu, lis)

print(red)

fu2 = lambda a, b : a if a > b else b

red2 = reduce(fu2, lis)
print(red2)

fu3 = lambda a, b : a + b

red3 = reduce(fu3, lis)

print(red3)