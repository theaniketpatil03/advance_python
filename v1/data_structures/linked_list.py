'''
not build in python

single_linked_list = head(data) -> (data, next) -> (data, next) -> (data, null)
double_linked_list = head(data) <-> (previous, data, next) <-> (previous, data, next) -> (previous, data, null)
'''

'''
array vs linked list
array - 
    size - fixed no, size need to be specified during declaration
    storage_capacity - static : it's location is allocated during compile time
    order and storing - stored consecutively 
    accessing the element - direct or random access method, specify the array index or subscript 
    searching - binary , linear

linked list - 
    size - grow contract since of insertions and eleetions
    storage capacity - dynamic: it's node is located during run time
    order and storing - stored randomly 
    accessing the elenment - sequential access method, traverse starting from the first node in the list by pointer
    searching - linear 
'''


class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Linked_list:
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        current = self.head

        while current.next != None:
            current = current.next
        
        current.next = new_node

    def length(self):
        current = self.head
        total_node = 0

        while current.next != None:
            total_node +=1
            current = current.next

        return total_node
    
    def diaplay(self):
        all_nodes = []
        current = self.head

        while current.next != None:
            current = current.next
            all_nodes.append(current.data)

        print(all_nodes)


    def get(self, index):
        if index >= self.length():
            print("Error: 'get index out of range")
            return None

        current_index = 0
        current_node = self.head

        while True:
            current_node = current_node.next
            if current_index == index:
                return current_node.data
            current_index += 1


    def erase(self, index):
        if index >= self.length():
            print("Error: 'get index out of range")
            return None
        current_index = 0
        current_node = self.head

        while True:
            last_node = current_node
            current_node = current_node.next

            if current_index == index:
                last_node.next = current_node.next

                return
            current_index += 1
    


one = Linked_list()
one.append(1)
one.append('1')
print(one.length())
one.diaplay()
one.append('three')
one.append('four')
print(one.get(2))
one.diaplay()
one.erase(2)
one.diaplay()
# print



