class Test:
    def __init__(self) -> None:
        self.str = 'aniket'
        self.x = 20

def fun():
    return Test()

t = fun()
print(t.str)
print(t.x)


def lun():
    return 1, 2, 3, 4, [5, 6]
print(lun())


def create_adder(x):
    def adder(y):
        return x + y

    return adder

add_15 = create_adder(10)
print(add_15(15))

