li = ['a', 'b', ]
print(list(reversed(li)))

str = 'aniket'
print("".join(reversed(str)))


seq_range = range(1, 9)
print(list(reversed(seq_range)))

str = "Reversed in python"
for char in reversed(str):
    print(char, end='')



# custom object in class
class Test:
    def  __init__(self, values) -> None:
        self.values = values

    def __reversed__(self):
        return reversed(self.values)

print('\n')
test_val = Test([1, 2, 3, 4, 5])
print(list(reversed(test_val)))
# or
print(list(test_val.__reversed__()))

test_str = 'abcdefgh'
reversed_test_str = reversed(test_str)
print(next(reversed_test_str))
print(next(reversed_test_str))
print(next(reversed_test_str))
print(next(reversed_test_str))