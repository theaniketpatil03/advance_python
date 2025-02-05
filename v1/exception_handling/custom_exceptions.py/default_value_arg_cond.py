def safe_divide(a, b):
    return a / b if b != 0 else float('inf')

print(safe_divide(2, 0))


