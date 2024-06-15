print('Hello from the other side!')

# Print single and multiple variables 
name = 'Alice'
print("name", name) # concatination
print(f"name {name}") # fstring
age = 30
print("Name", name, "Age", age) # concatinaion
print(name, age) # multiple assignment 

# multiple variable assignment
a, b, c = 2, 'b', 4.5
print(a, b, c)

# assigning different result to variables 
d, e = (a + c), (a * c)
print(d, e)


# Using Format()
amount = 150.75
print("Amount: ${:.3f}".format(amount))

# Using Modulo
print('aniket: %2d, age : %5.2f' % (1, 05.333))

'''more refrence - https://www.geeksforgeeks.org/python-output-formatting/'''

# Using Sep and end

# end parameter
print('Python', end='@')
print('aniket')

# seprting with comma
print('a', 's', 'p', sep='')  ,
print('a', 's', 'p', sep='-')

# Using % operator
'''
%d - integer
%f - float
%s - string
%x - hexadecimal
%o - octal
'''
# single input
num = int(input('Enter a value: '))
add =  num + 5
print('the sum is %d' %add)

# multiple input
x, y = input('Enter two vlaues: ').split()
print("first val:", x)
print("second val:", y)

# conditional input
# Prompting the user for input
age_input = input("Enter your age: ")

# Converting the input to an integer
age = int(age_input)

# Checking conditions based on user input
if age < 0:
    print("Please enter a valid age.")
elif age < 18:
    print("You are a minor.")
elif age >= 18 and age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")