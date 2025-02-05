a = True
print(type(a) )

b = False
print(type(b))

# Python program to illustrate 
# built-in method bool() 

# Returns False as x is not equal to y 
x = 5
y = 10
print(bool(x==y)) 

# Returns False as x is None 
x = None
print(bool(x)) 

# Returns False as x is an empty sequence 
x = () 
print(bool(x)) 

# Returns False as x is an empty mapping 
x = {} 
print(bool(x)) 

# Returns False as x is 0 
x = 0.0
print(bool(x)) 

# Returns True as x is a non empty string 
x = 'GeeksforGeeks'
print(bool(x)) 


# Declaring variables 
a = 10
b = 20

# Comparing variables 
print(a == b)


var1 = 0
print(bool(var1)) 

var2 = 1
print(bool(var2)) 

var3 = -9.7
print(bool(var3))


# Python program to demonstrate 
# equivalent an not equivalent 
# operator 

a = 0
b = 1

if a == 0: 
	print(True) 
	
if a == b: 
	print(True) 
	
if a != b: 
	print(True)

# Python program to demonstrate 
# is keyword 


x = 10
y = 10

if x is y: 
	print(True) 
else: 
	print(False) 

x = ["a", "b", "c", "d"] 
y = ["a", "b", "c", "d"] 

print(x is y)

# Python program to demonstrate 
# in keyword 

# Create a list 
animals = ["dog", "lion", "cat"] 

# Check if lion in list or not 
if "lion" in animals: 
	print(True)
