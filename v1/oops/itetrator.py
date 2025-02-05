'''
An iterator in Python is an object that is used to iterate over iterable objects like lists, tuples, dicts, and sets. The Python iterators object is initialized using the iter() method. It uses the next() method for iteration.
__iter__(): The iter() method is called for the initialization of an iterator. This returns an iterator object
__next__(): The next method returns the next value for the iterable. When we use a for loop to traverse any iterable object, internally it uses the iter() method to get an iterator object, which further uses the next() method to iterate over. This method raises a StopIteration to signal the end of the iteration.
'''

string = "GFG"
ch_iterator = iter(string)

print(next(ch_iterator))
print(next(ch_iterator))
print(next(ch_iterator))


class Test:

    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        self.x = 10
        return self

    def __next__(self):

        x = self.x

        if x > self.limit:
            raise StopIteration

        self.x = x + 1
        return x


for i in Test(15):
    print(i)

for i in Test(5):
    print(i)



# Sample built-in iterators

# Iterating over a list
print("List Iteration")
l = ["geeks", "for", "geeks"]
for i in l:
	print(i)
	
# Iterating over a tuple (immutable)
print("\nTuple Iteration")
t = ("geeks", "for", "geeks")
for i in t:
	print(i)
	
# Iterating over a String
print("\nString Iteration") 
s = "Geeks"
for i in s :
	print(i)
	
# Iterating over dictionary
print("\nDictionary Iteration") 
d = dict() 
d['xyz'] = 123
d['abc'] = 345
for i in d :
	print("%s %d" %(i, d[i]))


'''
Iterable vs Iterator
Python iterable and Python iterator are different. The main difference between them is, iterable in Python cannot save the state of the iteration, whereas in iterators the state of the current iteration gets saved.

Note: Every iterator is also an iterable, but not every iterable is an iterator in
'''

tup = ('a', 'b', 'c', 'd', 'e')

for item in tup:
	print(item)

tup = ('a', 'b', 'c', 'd', 'e')

# creating an iterator from the tuple
tup_iter = iter(tup)

print("Inside loop:")
# iterating on each item of the iterator object
for index, item in enumerate(tup_iter):
	print(item)

	# break outside loop after iterating on 3 elements
	if index == 2:
		break

# we can print the remaining items to be iterated using next()
# thus, the state was saved
print("Outside loop:")
print(next(tup_iter))
print(next(tup_iter))



'''
Getting StopIteration Error while using iterator
Iterable in Python can be iterated over multiple times, but iterators raise StopIteration Error when all items are already iterated.

Here, we are trying to get the next element from the iterator after the completion of the for-loop. Since the iterator is already exhausted, it raises a StopIteration Exception. Whereas, using an iterable, we can iterate on multiple times using for loop or can get items using indexing.
'''


iterable = (1, 2, 3, 4)
iterator_obj = iter(iterable)

print("Iterable loop 1:")
# iterating on iterable
for item in iterable:
	print(item, end=",")

print("\nIterable Loop 2:")
for item in iterable:
	print(item, end=",")

print("\nIterating on an iterator:")
# iterating on an iterator object multiple times
for item in iterator_obj:
	print(item, end=",")

print("\nIterator: Outside loop")
# this line will raise StopIteration Exception
# since all items are iterated in the previous for-loop
print(next(iterator_obj))
