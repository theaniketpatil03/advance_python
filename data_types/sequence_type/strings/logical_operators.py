str1 = ''
str2 = 'geeks'

print(repr(str1 and str2))
print(repr(str2 and str1))
print(repr(str2 or str1))
print(type(str2 or str1))
print(type(repr(str2 or str1)))

print(f"repr string using f string have to mention !r {str2!r}")