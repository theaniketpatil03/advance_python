# String is a sequence immutable data type 
string_val = 'hello, boy!'

print(string_val)
print(type(string_val))

# Creation
s1 = 'one'
s2 = "two"
s3 = '''i am 
a good boy
you are a bad boy
heeeee'''
print(s1)
print(s2)
print(s3)

# accessing characters in string (only integer support not float)
print(s1[0])
print(s1[-1])


# String Slicing
print(s2[:])
print(s2[:2])
print(s2[1:])
print(s2[-1:0])

# reverse the string
print(s2[::-1])
# and this will revers and also exclueds the characters (print notprint notprint print)
print(s2[::-2])


# there si reverse function in python which returns the iterator 
# so if you are reversing the string the you have to use join method to again join the list output to string
ulta = reversed(s2)
print(list(ulta))
ulta_stg = "".join(reversed(s2))
print(ulta_stg)

del ulta_stg
# print(ulta_stg)

# but we cannot update or delete individual character as string is immutable
# but we can use slicing to do so 
new_s2 = s2[:1] + s2[2:]
print(new_s2)
# or if wnat to update
new_s2 = s2[:1] + 'n' + s2[2:]
print(new_s2)
