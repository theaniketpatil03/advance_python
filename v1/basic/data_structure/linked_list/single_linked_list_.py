'''
A linked list is a linear data structure where elements are stored in nodes, and each node points to the next node in the sequence. Linked lists provide dynamic memory allocation and efficient insertion and deletion of elements. There are different types of linked lists, such as singly linked lists and doubly linked lists.
'''


# 1 - Singly Linked List
'''In a single linked list, each node points to the next node in the sequence, forming a unidirectional chain'''
# node structure
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

# Example

# Creating nodes 
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

# Linking nodes
node1.next = node2
node2.next = node3


# Operations:

#  - Insertion at the begining

new_node = Node(0)
new_node.next = node1

print(new_node.data)
print(new_node.next.data)

# - Insertion at the end

new_node = Node(4)
node3.next = new_node

print(new_node.data)
print(node3.next.data)


# - Deletion of node ( add next node )
node1.next = node2.next
print(node1.next.data)

#  - Traversal
print('Traversal')
current_node = node1
while current_node is not None:
    print(current_node.data)
    current_node = current_node.next