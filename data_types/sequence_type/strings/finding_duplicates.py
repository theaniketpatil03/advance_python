string = "geeksforgeeeks"

def navive_method():
    '''
    calculate how repetation of letter in string
    '''
    global string
    chars = {}

    for char in string:
        if char not in chars:
            chars[char] = 1
        else:
            chars[char] += 1

    return chars

print(navive_method())


# from Coounter function 
from collections import Counter
# print(help(Counter))
check   = Counter(string)
print(check)


# using count method

def find_duplicates():
    global string

    x = []
    for i in string:
        if i not in x and string.count(i)> 1:
            x.append(i)
    return x
print(find_duplicates())

print(string.count('g'))


# using filter()

def find_dup_chara_filter():
    global string
    x = lambda x : set([x for x in string if string.count(x) > 3])
    # x = lambda x : string.count(x) >=2

    y = filter(lambda x: string.count(x) >=2, string)
    print(' '.join(set(y)))
    return y

print(find_dup_chara_filter())



# using sets
def find_duplicate_chars(string):
	# Create empty sets to store unique and duplicate characters
	unique_chars = set()
	duplicate_chars = set()

	# Iterate through each character in the string
	for char in string:
		# If the character is already in unique_chars, it is a duplicate
		if char in unique_chars:
			duplicate_chars.add(char)
		# Otherwise, add it to unique_chars
		else:
			unique_chars.add(char)
	return duplicate_chars

# Example usage:
print(find_duplicate_chars("geeksforgeeks")) # Output: ['e', 'g', 'k', 's']


# using functools
from functools import reduce

def find_dup_char(input):
	x = reduce(lambda x, b: x + b if input.rindex(b) != input.index(b) and b not in x else x, input, '')
	print(x)


# Driver Code
if __name__ == "__main__":
	input = 'geeksforgeeks'
	find_dup_char(input)
