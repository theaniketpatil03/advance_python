

class MyClass:
    def __enter__(self):
        print("Entering context")
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        print('closing class')
        return self


with MyClass():
    print('doing something inside class')