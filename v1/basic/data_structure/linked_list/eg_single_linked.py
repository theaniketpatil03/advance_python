# 1 Dynamic Memory Allocation:
'''
Singly linked lists allow for dynamic memory allocation, as memory can be allocated and deallocated as needed without the need for contiguous memory.
'''


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

    
def create_linked_list(values):
    head = Node(values[0])
    current = head
    for value in values[1:]:
        current.next = Node(value)
        current = current.next
    return head


linked_list = create_linked_list([0,1,2,3,4])
print(linked_list.data)



# 2 Efficient Insertions and Deletions:
'''
Singly linked lists excel in scenarios where frequent insertions and deletions are required, as these operations can be performed in constant time.
'''


def insert_at_beginning(head, new_data):
    new_node = Node(new_data)
    new_node.next = head

    return new_node



def delete_node(head, key):
    current = head
    

    if current is not None and current ==  key:
        return current.next
    
    while current.next is not None:
        if current.next.data == key:
            current.next = current.next.next
            break

        current = current.next



    return head


def display_linked_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

# Example  usage
linked_list = Node(1)
linked_list.next = Node(2)
linked_list.next.next = Node(3)
linked_list.next.next.next = Node(4)

# Display original linked list
print("Original Linked List")
display_linked_list(linked_list)

# Insert at the begining
linked_list = insert_at_beginning(linked_list, 0)
print("\nAfter inserting at begining")
display_linked_list(linked_list)

# Delete node with data 2: so new node will be 0 -> 1 -> 3 -> 4
linked_list = delete_node(linked_list, 2)
print("\nAfter Deleting node wiht Data 2")
display_linked_list(linked_list)