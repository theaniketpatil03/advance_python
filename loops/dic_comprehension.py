# Python code to demonstrate dictionary 
# comprehension

# Lists to represent keys and values
keys = ['a','b','c','d','e']
values = [1,2,3,4,5] 

# but this line shows dict comprehension here 
myDict = { k:v for (k,v) in zip(keys, values)} 

# We can use below too
# myDict = dict(zip(keys, values)) 

print (myDict)


dic=dict.fromkeys(range(5), [True, False])

print(dic)


# Python code to demonstrate dictionary 
# creation using list comprehension
myDict = {x: x**2 for x in [1,2,3,4,5]}
print (myDict)



sDict = {x.upper(): x*3 for x in 'coding '}
print (sDict)


# Python code to demonstrate dictionary 
# comprehension using if.
newdict = {x: x**3 for x in range(10) if x**3 % 4 == 0}
print(newdict)


# given string
l="GFG"

# using dictionary comprehension
dic = {
	x: {y: x + y for y in l} for x in l
}

print(dic)
