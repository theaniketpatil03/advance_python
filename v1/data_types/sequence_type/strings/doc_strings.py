def my_function():
	'''Demonstrates triple double quotes
	docstrings and does nothing really.'''

	return None

print("Using __doc__:")
print(my_function.__doc__)

print("Using help:")
help(my_function)

# google style docstring
def multiply_numbers(a, b):
	"""
	Multiplies two numbers and returns the result.

	Args:
		a (int): The first number.
		b (int): The second number.

	Returns:
		int: The product of a and b.
	"""
	return a * b
print(multiply_numbers(3,5))


# numpy docstyle
def divide_numbers(a, b):
	"""
	Divide two numbers.

	Parameters
	----------
	a : float
		The dividend.
	b : float
		The divisor.

	Returns
	-------
	float
		The quotient of the division.
	"""
	if b == 0:
		raise ValueError("Division by zero is not allowed.")
	return a / b
print(divide_numbers(3,6))


class Employee:
	"""
	A class representing an employee.

	Attributes:
		name (str): The name of the employee.
		age (int): The age of the employee.
		department (str): The department the employee works in.
		salary (float): The salary of the employee.
	"""

	def __init__(self, name, age, department, salary):
		"""
		Initializes an Employee object.

		Parameters:
			name (str): The name of the employee.
			age (int): The age of the employee.
			department (str): The department the employee works in.
			salary (float): The salary of the employee.
		"""
		self.name = name
		self.age = age
		self.department = department
		self.salary = salary

	def promote(self, raise_amount):
		"""
		Promotes the employee and increases their salary.

		Parameters:
			raise_amount (float): The raise amount to increase the salary.

		Returns:
			str: A message indicating the promotion and new salary.
		"""
		self.salary += raise_amount
		return f"{self.name} has been promoted! New salary: ${self.salary:.2f}"

	def retire(self):
		"""
		Marks the employee as retired.

		Returns:
			str: A message indicating the retirement status.
		"""
		# Some implementation for retiring an employee
		return f"{self.name} has retired. Thank you for your service!"

# Access the Class docstring using help()
help(Employee)
