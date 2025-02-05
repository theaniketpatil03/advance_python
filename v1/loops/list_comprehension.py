numbers = [12, 13, 14,] 
doubled = [x *2 for x in numbers] 
print(doubled)


list = [i for i in range(11) if i % 2 == 0] 
print(list)

matrix = [[j for j in range(3)] for i in range(3)] 
	
print(matrix)


# Empty list 
List = [] 

# Traditional approach of iterating 
for character in 'Geeks 4 Geeks!': 
	List.append(character) 

# Display list 
print(List) 


# Using list comprehension to iterate through loop 
List = [character for character in 'Geeks 4 Geeks!'] 

# Displaying list 
print(List) 

# Import required module 
import time 


# define function to implement for loop 
def for_loop(n): 
	result = [] 
	for i in range(n): 
		result.append(i**2) 
	return result 


# define function to implement list comprehension 
def list_comprehension(n): 
	return [i**2 for i in range(n)] 


# Driver Code 

# Calculate time taken by for_loop() 
begin = time.time() 
for_loop(10**6) 
end = time.time() 

# Display time taken by for_loop() 
print('Time taken for_loop:', round(end-begin, 2)) 

# Calculate time takens by list_comprehension() 
begin = time.time() 
list_comprehension(10**6) 
end = time.time() 

# Display time taken by for_loop() 
print('Time taken for list_comprehension:', round(end-begin, 2)) 


# Nested list comprehension 
matrix = [[j for j in range(5)] for i in range(3)] 

print(matrix) 


# using lambda to print table of 10 
numbers = list(map(lambda i: i*10, [i for i in range(1, 6)])) 

print(numbers) 


lis = ["Even number" if i % 2 == 0
	else "Odd number" for i in range(8)] 
print(lis) 
