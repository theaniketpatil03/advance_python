"""
Definition: 
A lambda function is a small anonymous function (because it does not have a name). 
It can take any number of arguments but can have only one expression. 
The result of the expression is automatically returned.

Syntax: 
lambda arguments: expression

if we are referencing the lambda function to the variable then that variable we can call as function it looks like the name of function.

but best practice is if you are give variable name to the lambda function then just define normal function with def and use lambda in short hand with map, filter, etc
"""




from loguru import logger




# use lambda function inside another function
# multiply the argument with number
def multiply_number(n):

    return lambda a : a * n




if __name__ == "__main__":

    '''

    res = lambda a : a + 10

    logger.info(res(10))

    logger.debug(res.__name__) # proof that it is still anonymous even we gave it reference name as 'res'
    '''


    calculate = multiply_number(5)

    logger.info(calculate(5))






