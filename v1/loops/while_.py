# Prints all letters except 'e' and 's' 
i = 0
a = 'geeksforgeeks'

while i < len(a): 
	if a[i] == 'e' or a[i] == 's': 
		i += 1
		continue
		
	print('Current Letter :', a[i]) 
	i += 1


# Python program to demonstrate 
# while-else loop 

i = 0
while i < 4: 
	i += 1
	print(i) 
else: # Executed because no break in for 
	print("No Break\n") 

i = 0
while i < 4: 
	i += 1
	print(i) 
	break
else: # Not executed as there is a break 
	print("No Break") 


# Initialize a counter 
count = 0

# Loop infinitely 
while True: 
	# Increment the counter 
	count += 1
	print(f"Count is {count}") 

	# Check if the counter has reached a certain value 
	if count == 10: 
		# If so, exit the loop 
		break

# This will be executed after the loop exits 
print("The loop has ended.") 


countdown = 10
while countdown > 0: 
	print(countdown) 
	countdown -= 1
print("Blast off!") 
