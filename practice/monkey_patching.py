class MyClass:
    def greet(self):
        print('hello from my class')

def new_greet(self):
    print('hello from new monkey patch')

cl = MyClass()
cl.greet()

MyClass.greet = new_greet

cl.greet()