n = 10

try:
    res = n / 0
except ZeroDivisionError as e:
    print(e)