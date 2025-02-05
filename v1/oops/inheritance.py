'''
One of the core concepts in object-oriented programming (OOP) languages is inheritance. It is a mechanism that allows you to create a hierarchy of classes that share a set of properties and methods by deriving a class from another class. Inheritance is the capability of one class to derive or inherit the properties from another class. 
'''

'''
Benefits of inheritance are:

Inheritance allows you to inherit the properties of a class, i.e., base class to another, i.e., derived class. The benefits of Inheritance in Python are as follows:

It represents real-world relationships well.
It provides the reusability of a code. We don’t have to write the same code again and again. Also, it allows us to add more features to a class without modifying it.
It is transitive in nature, which means that if class B inherits from another class A, then all the subclasses of B would automatically inherit from class A.
Inheritance offers a simple, understandable model structure. 
Less development and maintenance expenses result from an inheritance. 
Python Inheritance Syntax
The syntax of simple inheritance in Python is as follows:

Class BaseClass:
    {Body}
Class DerivedClass(BaseClass):
    {Body}

'''


# A Python program to demonstrate inheritance

# Base or Super class. Note object in bracket.
# (Generally, object is made ancestor of all classes)
# In Python 3.x "class Person" is
# equivalent to "class Person(object)"


class Person(object): # no need to define object in python > 3.x

	# Constructor
	def __init__(self, name):
		self.name = name

	# To get name
	def getName(self):
		return self.name

	# To check if this person is an employee
	def isEmployee(self):
		return False


# Inherited or Subclass (Note Person in bracket)
class Employee(Person):

	# Here we return true
	def isEmployee(self):
		return True


# Driver code
emp = Person("Geek1") # An Object of Person
print(emp.getName(), emp.isEmployee())

emp = Employee("Geek2") # An Object of Employee
print(emp.getName(), emp.isEmployee())


class Person:
	def __init__(self, name):
		self.name = name

class Empoyee(Person):
    def __init__(self, name, salary):
        self.salary = salary
		
        super().__init__(name)

# or 

class Employee(Person):
	
    def __init__(self, name, salary):
        self.salary = salary

        Person.__init__(self, name)

'''Different types of inheritance'''

'''
Single inheritance: When a child class inherits from only one parent class, it is called single inheritance. We saw an example above.

Multiple inheritances: When a child class inherits from multiple parent classes, it is called multiple inheritances. 

Multilevel inheritance: When we have a child and grandchild relationship. This means that a child class will inherit from its parent class, which in turn is inheriting from its parent class.

Hierarchical inheritance More than one derived class can be created from a single base.

Hybrid inheritance: This form combines more than one form of inheritance. Basically, it is a blend of more than one type of inheritance.
'''

# Python example to show the working of multiple
# inheritance

class Base1(object):
	def __init__(self):
		self.str1 = "Geek1"
		print("Base1")


class Base2(object):
	def __init__(self):
		self.str2 = "Geek2"
		print("Base2")


class Derived(Base1, Base2):
	def __init__(self):

		# Calling constructors of Base1
		# and Base2 classes
		Base1.__init__(self)
		Base2.__init__(self)
		print("Derived")

	def printStrs(self):
		print(self.str1, self.str2)


ob = Derived()
ob.printStrs()


# A Python program to demonstrate inheritance

# Base or Super class. Note object in bracket.
# (Generally, object is made ancestor of all classes)
# In Python 3.x "class Person" is
# equivalent to "class Person(object)"

class Base(object):

	# Constructor
	def __init__(self, name):
		self.name = name

	# To get name
	def getName(self):
		return self.name


# Inherited or Sub class (Note Person in bracket)
class Child(Base):

	# Constructor
	def __init__(self, name, age):
		Base.__init__(self, name)
		self.age = age

	# To get name
	def getAge(self):
		return self.age

# Inherited or Sub class (Note Person in bracket)


class GrandChild(Child):

	# Constructor
	def __init__(self, name, age, address):
		Child.__init__(self, name, age)
		self.address = address

	# To get address
	def getAddress(self):
		return self.address


# Driver code
g = GrandChild("Geek1", 23, "Noida")
print(g.getName(), g.getAge(), g.getAddress())


# Python program to demonstrate private members
# of the parent class

class C(object):
	def __init__(self):
		self.c = 21

		# d is private instance variable
		self.__d = 42


class D(C):
	def __init__(self):
		self.e = 84
		C.__init__(self)

object1 = D()

# produces an error as d is private instance variable
print(object1.c)
print(object1.__d)
