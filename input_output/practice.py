'''

Variables - 
    single assignment
    multiple variable assignment
    assigning different result to variables

Input - 
    single input
    multiple input
    conditional input
    converting the input to other data type

Output - 
    concatination
    multiple concatination
    fstring
    Multiple assignment
    format
    modulo - % operator
    sep
    end

    
'''

'''*** Variables***'''

# single assignment
var = 9
var = 'cool'

# multiple assignment
var1, var2 = 2, 'cool'

# assigning results
res = (8 * 10) / 2

res1, res2 = 'cool' + 'hot' , 2 ** 5


'''**** Inputs ***'''

# single input

sing_inp = input('enter your age: ')

# multiple input

inp1, inp2 = input('enter your 2 fev numbers: ').split()


# converting the input to other data type

num = int(input("enther your age again:"))

# conditional input - condition after getting input 

test_input = input('enter age')
if int(test_input) > 18:
    print('You can drink rum.')
else:
    print('Drink milk.')

'''*** Outputs ***'''

print(var)

# concatination

print('value', var)

# multiple concatination

print('two values', var1, var2)

# fstring

print(f'your response is: {res}')

# multiple assignment
print(inp1, inp2)

# format
print('your age in float is {:.2f}'.format(num))

# modulo
print('your age is %2d, in float %5.2f and in octal %o in hexadecimal %x'%(num, num, num, num))

# sep

print(inp1, inp2, sep=' :-: ')

# end

print(num, end='printed num')


