# Python program to demonstrate 
# break statement 

s = 'geeksforgeeks'
# Using for loop 
for letter in s: 

	print(letter) 
	# break the loop as soon it sees 'e' 
	# or 's' 
	if letter == 'e' or letter == 's': 
		break

print("Out of for loop") 
print() 

i = 0

# Using while loop 
while True: 
	print(s[i]) 

	# break the loop as soon it sees 'e' 
	# or 's' 
	if s[i] == 'e' or s[i] == 's': 
		break
	i += 1

print("Out of while loop")


# Python program to demonstrate 
# break statement with nested 
# for loop 

# first for loop 
for i in range(1, 5): 
	
	# second for loop 
	for j in range(2, 6): 
		
		# break the loop if 
		# j is divisible by i 
		if j%i == 0: 
			break
			
		print(i, " ", j)


# Python program to 
# demonstrate continue 
# statement 

# loop from 1 to 10 
for i in range(1, 11): 

	# If i is equals to 6, 
	# continue to next iteration 
	# without printing 
	if i == 6: 
		continue
	else: 
		# otherwise print the value 
		# of i 
		print(i, end = " ")

# Python program to demonstrate 
# pass statement 

s = "geeks"

# Empty loop 
for i in s: 
	# No error will be raised 
	pass

# Empty function 
def fun(): 
	pass

# No error will be raised 
fun() 

# Pass statement 
for i in s: 
	if i == 'k': 
		print('Pass executed') 
		pass
	print(i) 

# continue - it will ignore all things from continue means if also and rest of loop function and will continue to next loop
for i in range(1, 5):
	if i == 3:
		continue
	print(i)
	
print('pass')
for i in range(1, 5):
	if i == 3:
		pass # this will just pass to next line means here it will just not perform rest of if loop from pas and it will exit the if 
        
	print(i)