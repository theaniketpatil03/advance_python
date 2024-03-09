'''
Stack - Last in first out
'''


my_stack = []

my_stack.append(1)
my_stack.append(2)

popped_element = my_stack.pop()
print(popped_element)
print(my_stack)

# 1 Push (Add element to the stack)
def push(stack, element):
    stack.append(element)



# 2 Pop ( Remove and return the top element from the stack)
def pop(stack):
    if len(stack) != 0:
        return stack.pop()

# 3 Peek ( Return the top element without removing it ) - not an internal function
def peek(stack):
    if len(stack) != 0:
        return stack[-1]

# 4 is empty ( to check if stack is empty)
def is_empty(stack):
        return len(stack) == 0

# Use case

class BrowseHistory:
    def __init__(self) -> None:
        self.stack = []

    def visit_page(self, url):
        self.stack.append(url)

    def go_back(self):
        if not is_empty(self.stack):
            current_page = self.stack.pop()
            print(f"Going back from {current_page}")

    def current_page(self):
        return peek(self.stack)


# Example Usage:
browser = BrowseHistory()
browser.visit_page("www.example.com")
browser.visit_page("www.example.com/page2")
print("Current Page", browser.current_page())

browser.go_back()
print("Current Page: ", browser.current_page())