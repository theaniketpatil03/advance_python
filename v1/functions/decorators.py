'''
Decorators are a very powerful and useful tool in Python since it allows programmers to modify the behaviour of a function or class. Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it. But before diving deep into decorators let us understand some concepts that will come in handy in learning the decorators.
'''

# defining a decorator
def hello_decorator(func):

	# inner1 is a Wrapper function in 
	# which the argument is called
	
	# inner function can access the outer local
	# functions like in this case "func"
	def inner1():
		print("Hello, this is before function execution")

		# calling the actual function now
		# inside the wrapper function.
		func()

		print("This is after function execution")
		
	return inner1


# defining a function, to be called inside wrapper
def function_to_be_used():
	print("This is inside the function !!")


# passing 'function_to_be_used' inside the
# decorator to control its behaviour
function_to_be_used = hello_decorator(function_to_be_used)


# calling the function
function_to_be_used()


# second approch

# importing libraries
import time
import math

# decorator to calculate duration
# taken by any function.
def calculate_time(func):
	
	# added arguments inside the inner1,
	# if function takes any arguments,
	# can be added like this.
    def inner1(*args, **kwargs):
        # storing time before function execution
        print('inside inner')
        print(args)
        print(kwargs)

        begin = time.time()

        func(*args, **kwargs)

        # storing time after function execution
        end = time.time()
        print("Total time taken in : ", func.__name__, end - begin)
        

    return inner1



# this can be added to any function present,
# in this case to calculate a factorial
@calculate_time
def factorial(num):

    print('num insside fact fun', num)
    # sleep 2 seconds because it takes very less time
    # so that you can see the actual difference
    time.sleep(2)
    print(math.factorial(num))

# calling the function.
factorial(10)




def decorator_func(func):
    print('decorater initialized')
    def inner_func(val):
        print('inside inner')
        func(val)
        print('func evaluated')
    def inner_fun2(val):
          print('inside second inner')
          func(val)
          print('second inner completed')
    return inner_func, inner_fun2


@decorator_func
def main(val):
      print(val)

in1, in2 = main
in1(4)
in2(5)


def hello_decorator(func):
	def inner1(*args, **kwargs):
		
		print("before Execution")
		
		# getting the returned value
		returned_value = func(*args, **kwargs)
		print("after Execution")
		
		# returning the value to the original frame
		return returned_value
		
	return inner1


# adding decorator to the function
@hello_decorator
def sum_two_numbers(a, b):
	print("Inside the function")
	return a + b

a, b = 1, 2

# getting the value through return of the function
print("Sum =", sum_two_numbers(a, b))


# code for testing decorator chaining 
def decor1(func): 
	def inner(): 
		x = func() 
		return x * x 
	return inner 

def decor(func): 
	def inner(): 
		x = func() 
		return 2 * x 
	return inner 

@decor1
@decor
def num(): 
	return 10

@decor
@decor1
def num2():
	return 10

print(num()) 
print(num2())
