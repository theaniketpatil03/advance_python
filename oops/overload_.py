'''
The @overload decorator, along with typing.overload, is used primarily for type hinting and documentation purposes. It does not contain any implementation logic itself; rather, it specifies different function signatures that the actual implementation of the method or function should adhere to.

Example of Using @overload with typing.overload
Here’s an example that demonstrates how to properly use @overload with typing.overload to define multiple function signatures for a method in a class:



Explanation:
@overload Decorators:

Each @overload decorator declares a different type signature for the process_data method.
These decorators do not contain any implementation logic (i.e., no actual code inside), but instead, they provide type hints and return type annotations.
Single Implementation:

The actual implementation of process_data is provided at the end of the class. This implementation handles all cases based on the provided type signatures.
Inside the method, based on the type of x, different logic is applied (x * 2 for integers and x.upper() for strings).
Usage:

You can call process_data with either an integer or a string, and the method will behave according to the specified overloads.
Key Points:
Type Hints: @overload along with typing.overload is used to declare multiple function signatures with specific argument types and return types.

No Implementation: The @overload decorators themselves do not contain any logic or functionality. They are purely for type checking and documentation purposes.

Single Implementation: There is only one implementation of the method provided at the end of the class, which handles all cases based on the type signatures declared with @overload.

Benefits of Using @overload:
Clarity: Clearly documents the expected types and return values for each variant of the method.

Readability: Improves code readability by explicitly stating the method's behavior with different argument types.

Type Checking: Helps IDEs and type checkers understand the method's behavior and provide better static analysis.

Conclusion:
@overload in Python, used together with typing.overload, is a powerful tool for declaring multiple function signatures within a single method or function. It enhances code clarity, aids in documentation, and improves type safety without requiring redundant implementations for different argument types.



'''

from typing import overload


class MyClass:
    @overload
    def process_data(self, x: int) -> int:
        ...

    @overload
    def process_data(self, x: str) -> str:
        ...

    def process_data(self, x):
        if isinstance(x, int):
            return x * 2
        elif isinstance(x, str):
            return x.upper()

# Usage
obj = MyClass()

result_int = obj.process_data(5)
print(result_int)  # Output: 10

result_str = obj.process_data("hello")
print(result_str)  # Output: HELLO
