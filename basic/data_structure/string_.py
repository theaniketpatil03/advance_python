# Creation: 
my_string = "Hello, World!"

# Concatenation: 
new_string = my_string + " Welcome"

# Substring: like slicing 
substring = my_string[7:12] # Output: World

# finding in list
if 'H' in my_string:
    print(True)

# replace in string - but it will only create new instance of that string
new_string = my_string.replace('Hello', 'Bye')
print(my_string)
print(new_string)