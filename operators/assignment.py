'''
Assignment Operator

=

Assign the value of the right side of the expression to the left side operand	c = a + b 
Addition Assignment Operator

+=


Add right side operand with left side operand and then assign the result to left operand	a += b   
Subtraction Assignment Operator

-=

Subtract right side operand from left side operand and then assign the result to left operand	a -= b  
Multiplication Assignment Operator

*=

Multiply right operand with left operand and then assign the result to the left operand	a *= b     
Division Assignment Operator

/=

Divide left operand with right operand and then assign the result to the left operand	a /= b
Modulus Assignment Operator

%=

Divides the left operand with the right operand and then assign the remainder to the left operand	a %= b  
Floor Division Assignment Operator

//=

Divide left operand with right operand and then assign the value(floor) to left operand	a //= b   
Exponentiation Assignment Operator

**=

Calculate exponent(raise power) value using operands and then assign the result to left operand	a **= b     
Bitwise AND Assignment Operator

&=

Performs Bitwise AND on operands and assign the result to left operand	a &= b   
Bitwise OR Assignment Operator

|=

Performs Bitwise OR on operands and assign the value to left operand	a |= b    
Bitwise XOR Assignment Operator

^=

Performs Bitwise XOR on operands and assign the value to left operand	a ^= b    
Bitwise Right Shift Assignment Operator

>>=

Performs Bitwise right shift on operands and assign the result to left operand	a >>= b     

Bitwise Left Shift Assignment Operator

<<=

Performs Bitwise left shift on operands and assign the result to left operand	a <<= b 
Walrus Operator

:=

Assign a value to a variable within an expression

a := exp
'''

# a list
a = [1, 2, 3, 4, 5]

# walrus operator
while(x := len(a)) > 2:
    a.pop()
    print(x)
'''
output - 
5
4
3
'''