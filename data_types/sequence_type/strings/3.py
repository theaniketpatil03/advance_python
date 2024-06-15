# Format

# Python Program for
# Formatting of Strings

# Default order
String1 = "{} {} {}".format('Geeks', 'For', 'Life')
print("Print String in default order: ")
print(String1)

# Positional Formatting
String1 = "{1} {0} {2}".format('Geeks', 'For', 'Life')
print("\nPrint String in Positional order: ")
print(String1)

# Keyword Formatting
String1 = "{l} {f} {g}".format(g='Geeks', f='For', l='Life')
print("\nPrint String in order of Keywords: ")
print(String1)



# rouding 
# converting to binary only convert integer values
string = "{0:b}".format(16)
print('binary value of 16 is ', string)
print('binary of aniket is {0:b}'.format(2))

# formatting float to exponential
string1 = "{0:e}".format(165.6458)
print('\n Exponent representation of 165.648 is ', string1)


# rounding of integers 
string3 = "{0:2f} and {1:0.2f}".format(1/6, 2/3)
print('calculations are', string3)


string = "|{:<10}|{:^10}|{:>10}".format('aniket', 'sunil', 'patil')
print(string)

String1 = "\n{0:^16} was founded in {1:<4}!".format("GeeksforGeeks",
                                                    2009)
print(String1)


# old style 
Integer1 = 12.3456789
print("Formatting in 3.2f format: ")
print('The value of Integer1 is %3.2f' % Integer1)
print("\nFormatting in 3.4f format: ")
print('The value of Integer1 is %3.4f' % Integer1)
