'''
    bool values
    build in method bool()
    equals conditions (==, !=)
    retuns bool depending on values
    is , is not keyword


'''


# bool values

true = True
false = False

# build in method
var = 10
print(bool(var))

val = 0
print(bool(val))

print(bool(''))

# equals conditions

print(var == val)
print(val == 0)
print(val == 10)
print(var != val)

# retursn bool depending on values

print(bool(var))

# is operator - basicaly it validate that is object pointing to same pointer

l1 = [2, 3, 4, 5]
l2 = [2, 3, 4, 5]

num1 = 3
num2 = 3

print(l1 is l2)
print(l1 is not l2)
print(num1 is num2)
print(num1 is not num2)
