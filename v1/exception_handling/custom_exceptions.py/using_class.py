class DivisionByZero(Exception):
    '''
    Raised when the divider is zero
    '''
    
    def __init__(self,val) -> None:
        super().__init__(f"you Cannot divide by {val}, it will lead to infinity")

def divide(x, y):
    if y == 0:
        raise DivisionByZero(y)
    
    else:
        print(x/y)


divide(1, 2)