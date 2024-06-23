class Student:
    grade = 20


    @classmethod
    def change_grade(cls, value):
        cls.grade = value

    def change_grade_without_classmethod(cls, value):
        cls.grade = value

    @staticmethod
    def just_print(value):
        print(f"printing {value}")


s1 = Student()
s1.just_print('cool')

s1.change_grade(30)
print(s1.grade)

Student.change_grade(20)
print(s1.grade)

Student.change_grade_without_classmethod(Student, 10)
print(s1.grade)