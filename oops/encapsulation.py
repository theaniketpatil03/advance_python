'''
private, public, protacted variables
access_modifiers
'''

class Employee:
    def __init__(self) -> None:
        self.name = "aniket"
        self._age = 24
        self.__department = 'backend'

emp1 = Employee()

print(emp1.name) # public
print(emp1._age) # protected
# print(emp1.__department) # cannont acces directly
print(emp1._Employee__department) # can be access indirectly - name mangling can acdess private