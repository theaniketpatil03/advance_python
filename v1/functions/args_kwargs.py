'''
*args (Non-Keyword Arguments)
**kwargs (Keyword Arguments)
Note: “We use the “wildcard” or “*” notation like this – *args OR **kwargs – as our function’s argument when we have doubts about the number of  arguments we should pass in a function.” 
'''

def myFun(*argv):
    for arg in argv:
        print(arg)


myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')


def myFun(arg1, *argv):
    print("First argument :", arg1)
    for arg in argv:
        print("Next argument through *argv :", arg)


myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')


'''
The special syntax **kwargs in function definitions in Python is used to pass a keyworded, variable-length argument list. We use the name kwargs with the double star. The reason is that the double star allows us to pass through keyword arguments (and any number of them).

A keyword argument is where you provide a name to the variable as you pass it into the function.
One can think of the kwargs as being a dictionary that maps each keyword to the value that we pass alongside it. That is why when we iterate over the kwargs there doesn’t seem to be any order in which they were printed out.
'''

def myFun(**kwargs):
    # here kwargs i dic
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


# Driver code
myFun(first='Geeks', mid='for', last='Geeks')


def myFun(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)


# Now we can use *args or **kwargs to
# pass arguments to this function :
args = ("Geeks", "for", "Geeks")
def myFun(karg1, karg2, karg3):
    print("karg1:", karg1)
    print("karg2:", karg2)
    print("karg3:", karg3)
myFun(*args)

kwargs = {"karg1": "Geeks", "karg2": "for", "karg3": "Geeks"}
myFun(**kwargs)


def myFun(*args, **kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)


# Now we can use both *args ,**kwargs
# to pass arguments to this function :
myFun('geeks', 'for', 'geeks', first="Geeks", mid="for", last="Geeks")


# defining car class
class Car():
    # args receives unlimited no. of arguments as an array
    def __init__(self, *args):
        # access args index like array does
        self.speed = args[0]
        self.color = args[1]


# creating objects of car class
audi = Car(200, 'red')
bmw = Car(250, 'black')
mb = Car(190, 'white')

# printing the color and speed of the cars
print(audi.color)
print(bmw.speed)


# defining car class
class Car():
    # args receives unlimited no. of arguments as an array
    def __init__(self, **kwargs):
        # access args index like array does
        self.speed = kwargs['s']
        self.color = kwargs['c']


# creating objects of car class
audi = Car(s=200, c='red')
bmw = Car(s=250, c='black')
mb = Car(s=190, c='white')

# printing the color and speed of cars
print(audi.color)
print(bmw.speed)

