class GeeksforGeeks:
	def __init__(self, topic):
		self.topic = topic

	def display_topic(self):
		print("Topic:", self.topic)

# Creating an instance of GeeksforGeeks
gfg_instance = GeeksforGeeks("Python")

# Calling the display_topic method
gfg_instance.display_topic()


'''
In Python, the ‘self‘ keyword is used to reference the instance of a class within its methods. Unlike some other programming languages, Python does not implicitly pass the instance to the method; instead, it requires the explicit use of ‘self.’ This explicit reference to the instance allows for better readability, clarity, and adherence to OOP principles.

Advantages
Instance Clarity: ‘self’ specifies the instance on which a method operates, avoiding ambiguity.
Attribute Access: Ensures direct access to instance attributes within class methods.
Encapsulation Aid: Supports encapsulation by linking methods to specific instances.
Pythonic Convention: Adheres to Pythonic style, enhancing code readability and consistency.
'''

class Circle:
	def __init__(self, radius):
		self.radius = radius

	def calculate_area(self):
		area = 3.14 * self.radius ** 2
		return area

# Creating an instance of Circle
circle_instance = Circle(5)

# Calling the calculate_area method
print("Area of the circle:", circle_instance.calculate_area())
