'''
    Defination - Map function applies a given function to item of list or tuple ( iterables ) and returns a map object ( which is an iterator ).

    Syntax - map(function, iterable-1, iterable-2, .... iterable-n)

    return - class of map object - can be directly iterate with loop or can convert to list 
'''

# imports
from loguru import logger


# basic integration - convert list of string numbers to integer
def list_string_number_to_integer():
    list_of_int_string = [ '1', '2', '3', '4' ]

    res = map(int, list_of_int_string)

    for i in res:
        logger.debug(i)

    logger.info(f"Converted interger list object class of map: \n{res}\n")
    logger.info(f"Converted list of string integer to list of integer: \n{list(res)}")

    return None


# with lambda function - to make function shorter
def lambda_map_to_double_digit():

    values = [ 1, 2, 3, 4 ]

    response = list(map(lambda x: x * 2, values))

    # logger.info(response)

    return response

# with multiple iterables
def add_list_items():

    list1 = [ 1, 2, 3 ]
    list2 =  [ 4, 5, 6 ]
    list3 =  [ 7, 8, 9 ]

    response = list(map(lambda x, y, z: x + y + z, list1, list2, list3))

    return response


# converting to uppercase
def converting_to_uppercase():
    '''
        1. short hand lambda function to convert string to upper case 
        2. response with direct operation with upper works as 
            str.upper(item) - map applies this directly on each item when we call str.upper
    '''
    fruits = [ 'apple', 'banana', 'cherry' ]

    list(map(lambda x: x.upper(), fruits))
    response = list(map(str.upper, fruits))


    return response

# converting to uppercase if items are not string

def converting_to_uppercase_with_no_string():

    list1 = ['aniket', 1, 'patil', None]

    response = list(map(lambda x: x.upper() if isinstance(x,str) else x, list1))

    return response


# convert to upper case only if string item else filterout the item
def converting_to_uppecase_with_filterout_non_string():

    list1 = ['aniket', 1, 'patil', None]

    response = list(map(str.upper, filter(lambda x: isinstance(x, str), list1)))

    return response

if __name__ == "__main__":

    
    ans = converting_to_uppecase_with_filterout_non_string()

    logger.debug(ans)

