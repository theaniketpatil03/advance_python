class Student:

    grade = 4

    __slots__ = ['name', 'age'] #explecitly declare data members

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def get_data(self):
        print(f"name: {self.name} and age: {self.age} and grade: {self.grade}")

    @classmethod
    def update_grade(cls, grade):
        cls.grade = grade

    @staticmethod
    def check_age(age):
        if age > 18:
            print('above 18')
        else:
            print('below 18')


    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name


s1 =  Student('aniket', 25)
s1.get_data()

# s1.grade = 10
print(s1.grade)

s2 = Student('ritesh', 24)
print(s2.grade)
# s2.update_grade(20) # not working for all
Student.update_grade(30)
print('grades')

print(s1.get_data())
print(s2.get_data())

s1.check_age(18)

print(str(s1))
print(repr(s1))