class CutomDivisionByZeroError(Exception):
    '''
    raise when someone tries to devide by zero
    '''

    def __init__(self, val) -> None:
        super().__init__(f"you can not divide {val} by 0, it will lead to infinity.")


def divide(x, y):

    if y == 0 :
        raise CutomDivisionByZeroError (x)
    
    else : return x / y


try:

    resp = divide(1, 0)
    print(resp)
except Exception as e:
    print(e)

print ( '********* cool' )
resp = divide(1, 0)
print(resp)

print ( '********* cool once more' )