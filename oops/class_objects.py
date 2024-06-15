'''
classes are created by keyword class
attributes are the variables that belong to a class
attributes are always public and can be accessed using the dot (.) operator
eg - MyClass.Myattribute

object is an instance of a class. class is like a blueprint 
object consist of -
    state: it is represented by the attributes of an object. It also reflects the properties of an object
    behavior: it is represented by the methos of an object. It also reflects the response of an object to other objects.
    identity: it gives a unique name to an object and enables one object to interact with other objects.

egs class - Dog
    identity - name of dog
    state/attributes - breed, age, color
    behaviors - bark, sleep, eat
'''

class Employee:
    company_name = 'microsec'
    def __init__(self, name, department, salary) -> None:
        self.name =  name
        self.department =  department
        self.salary = salary

    def set_experiance(self, experiance):
        self.experiance = experiance

    def __str__(self) -> str:
        return self.name

emp1 = Employee('aniket', 'backend', 60000)
emp2 = Employee('rabi', 'devops', 35000)
print(emp1.company_name, emp1.department)
print(emp2.company_name, emp2.department)

emp1.set_experiance(3)
emp2.set_experiance(2)
print(f"company: {emp1.company_name}\nname: {emp1.name}\ndepartment: {emp1.department}\nexperiance: {emp1.experiance}\nsalary: {emp1.salary}")
print(f"company: {emp2.company_name}\nname: {emp2.name}\ndepartment: {emp2.department}\nexperiance: {emp2.experiance}\nsalary: {emp2.salary}")
